from tokenize import String
from typing import Final, final, override
from AST import (
    AST,
    ArrayType,
    BoolType,
    Expr,
    FloatType,
    Id,
    IntType,
    StringType,
    StructType,
    Type,
    VoidType,
)
from StaticError import (
    CannotAssignToConstant,
    Constant,
    Function,
    Identifier,
    Redeclared,
    TypeMismatch,
    Undeclared,
    Variable,
)
from Utils import Utils
from functools import reduce

from Visitor import BaseVisitor


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

    def __str__(self):
        return (
            "MType(["
            + ",".join(str(x) for x in self.partype)
            + "],"
            + str(self.rettype)
            + ")"
        )


class Symbol:
    def __init__(self, name, mtype, value=None):
        self.name = name
        self.mtype = mtype
        self.value = value

    def __str__(self):
        return (
            "Symbol("
            + str(self.name)
            + ","
            + str(self.mtype)
            + ("" if self.value is None else "," + str(self.value))
            + ")"
        )


@final
class StaticChecker(BaseVisitor, Utils):
    ast: AST
    global_envi: Final[list[Symbol]] = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putInt", MType([IntType()], VoidType())),
        Symbol("putIntLn", MType([IntType()], VoidType())),
        Symbol("getFloat", MType([], FloatType())),
        Symbol("putFloat", MType([FloatType()], VoidType())),
        Symbol("putFloatLn", MType([FloatType()], VoidType())),
        Symbol("getBool", MType([], BoolType())),
        Symbol("putBool", MType([BoolType()], VoidType())),
        Symbol("putBoolLn", MType([BoolType()], VoidType())),
        Symbol("getString", MType([], StringType())),
        Symbol("putString", MType([StringType()], VoidType())),
        Symbol("putStringLn", MType([StringType()], VoidType())),
        Symbol("putLn", MType([], VoidType())),
    ]

    def __init__(self, ast: AST) -> None:
        self.ast = ast

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, param):
        reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.decl, param)
        return param

    def visitVarDecl(self, ast, param) -> Symbol:
        res = self.lookup(ast.varName, param, lambda x: x.name)

        if res is not None:
            raise Redeclared(Variable(), ast.varName)

        if ast.varInit is None:
            return Symbol(ast.varName, ast.varType, None)

        init_type = self.visit(ast.varInit, param)
        if init_type is None:
            raise TypeMismatch(ast)

        if ast.varType is None:
            ast.varType = init_type
        elif type(ast.varType) is not type(init_type):
            raise TypeMismatch(ast)

        return Symbol(ast.varName, ast.varType, None)

    def visitFuncDecl(self, ast, param) -> Symbol:
        res = self.lookup(ast.name, param, lambda x: x.name)

        if res is not None:
            raise Redeclared(Function(), ast.name)

        local_scope = []
        self.visit(ast.body, local_scope + param)

        return Symbol(ast.name, MType([], ast.retType))

    @override
    def visitBlock(self, ast, param):
        for stmt in ast.member:
            self.visit(stmt, param)

    @override
    def visitIntLiteral(self, ast, param) -> IntType:
        return IntType()

    @override
    def visitFloatLiteral(self, ast, param) -> FloatType:
        return FloatType()

    @override
    def visitBooleanLiteral(self, ast, param) -> BoolType:
        return BoolType()

    @override
    def visitStringLiteral(self, ast, param) -> StringType:
        return StringType()

    @override
    def visitNilLiteral(self, ast, param) -> VoidType:
        return VoidType()

    @override
    def visitArrayLiteral(self, ast, param) -> ArrayType:
        expected_type = self.visit(ast.eleType, param)

        def check_all_elements(node):
            if isinstance(node, list):
                for subnode in node:
                    check_all_elements(subnode)
            else:
                actual_type = self.visit(node, param)
                if type(expected_type) is not type(actual_type):
                    raise TypeMismatch(ast)

        check_all_elements(ast.value)

        return ArrayType(ast.dimens, expected_type)

    @override
    def visitIntType(self, ast, param) -> IntType:
        return IntType()

    @override
    def visitFloatType(self, ast, param) -> FloatType:
        return FloatType()

    @override
    def visitBoolType(self, ast, param) -> BoolType:
        return BoolType()

    @override
    def visitStringType(self, ast, param) -> StringType:
        return StringType()

    @override
    def visitVoidType(self, ast, param) -> VoidType:
        return VoidType()

    @override
    def visitArrayType(self, ast, param) -> ArrayType:
        elemnet_type: Final = self.visit(ast.eleType, param)
        return ArrayType(ast.dimens, elemnet_type)

    @override
    def visitStructType(self, ast, param) -> StructType:
        new_elements: Final = [
            (name, self.visit(typ, param)) for name, typ in ast.elements
        ]

        for method in ast.methods:
            self.visit(method, param)

        return StructType(ast.name, new_elements, ast.methods)

    def visitId(self, ast, param) -> Id:
        res = self.lookup(ast.name, param, lambda x: x.name)

        if res is None:
            raise Undeclared(Identifier(), ast.name)

        return res.mtype

    @override
    def visitConstDecl(self, ast, param) -> Symbol:
        if self.lookup(ast.conName, param, lambda x: x.name):
            raise Redeclared(Constant(), ast.conName)

        init_type = self.visit(ast.iniExpr, param)
        if init_type is None:
            raise TypeMismatch(ast)

        if ast.conType is None:
            ast.conType = init_type
        elif type(ast.conType) is not type(init_type):
            raise TypeMismatch(ast)

        return Symbol(ast.conName, ast.conType, ast.iniExpr)

    @override
    def visitAssign(self, ast, param):
        if isinstance(ast.lhs, Id):
            sym = self.lookup(ast.lhs.name, param, lambda x: x.name)
            if self._isConst(sym):
                raise CannotAssignToConstant(ast.lhs.name)

        lhs_type = self.visit(ast.lhs, param)
        rhs_type = self.visit(ast.rhs, param)

        if isinstance(lhs_type, VoidType):
            raise TypeMismatch(ast)

        if isinstance(lhs_type, ArrayType):
            self._checkArrayAssignment(lhs_type, rhs_type, ast)
        else:
            self._checkScalarAssignment(lhs_type, rhs_type, ast)

        return lhs_type

    def _isConst(self, sym):
        return sym is not None and isinstance(sym.value, Expr)

    def _checkArrayAssignment(self, lhs_type, rhs_type, ast):
        if not isinstance(rhs_type, ArrayType):
            raise TypeMismatch(ast)

        if len(lhs_type.dimens) != len(rhs_type.dimens):
            raise TypeMismatch(ast)

        lhs_elem = lhs_type.eleType
        rhs_elem = rhs_type.eleType
        if not self._isTypeCompatible(lhs_elem, rhs_elem):
            raise TypeMismatch(ast)

    def _checkScalarAssignment(self, lhs_type, rhs_type, ast):
        if not self._isTypeCompatible(lhs_type, rhs_type):
            raise TypeMismatch(ast)

    def _isTypeCompatible(self, lhs_type, rhs_type):
        return type(lhs_type) is type(rhs_type) or (
            isinstance(lhs_type, FloatType) and isinstance(rhs_type, IntType)
        )
