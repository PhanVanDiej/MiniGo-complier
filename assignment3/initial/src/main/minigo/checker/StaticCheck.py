from tokenize import String
from typing import Final, final, override
from AST import (
    AST,
    ArrayType,
    BoolType,
    ConstDecl,
    Expr,
    FloatType,
    FuncDecl,
    Id,
    IntType,
    InterfaceType,
    StringType,
    StructType,
    Type,
    VarDecl,
    VoidType,
)
from StaticError import (
    CannotAssignToConstant,
    Constant,
    Function,
    Identifier,
    Method,
    Parameter,
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

        func_sym = Symbol(ast.name, MType([p.parType for p in ast.params], ast.retType))

        local_scope = [func_sym]
        for par in ast.params:
            if self.lookup(par.parName, local_scope, lambda x: x.name):
                raise Redeclared(Parameter(), par.parName)
            local_scope.append(Symbol(par.parName, par.parType))

        self.visit(ast.body, local_scope + param)
        return func_sym

    @override
    def visitBlock(self, ast, param):
        local = param.copy()
        for stmt in ast.member:
            sym = self.visit(stmt, local)
            if isinstance(stmt, (VarDecl, ConstDecl)):
                local.insert(0, sym)

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

    @override
    def visitIf(self, ast, param):
        cond_type = self.visit(ast.expr, param)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)

        self.visit(ast.thenStmt, param)
        if ast.elseStmt is not None:
            self.visit(ast.elseStmt, param)

        return None

    @override
    def visitForBasic(self, ast, param):
        cond_type = self.visit(ast.cond, param)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)

        self.visit(ast.loop, param)
        return None

    @override
    def visitForStep(self, ast, param) -> None:
        local_env = param.copy()

        init_result = self.visit(ast.init, local_env)
        if isinstance(ast.init, (VarDecl, ConstDecl)):
            local_env.insert(0, init_result)

        cond_type = self.visit(ast.cond, local_env)
        if not isinstance(cond_type, BoolType):
            raise TypeMismatch(ast)

        self.visit(ast.upda, local_env)
        self.visit(ast.loop, local_env)

        return None

    @override
    def visitForEach(self, ast, param) -> None:
        arr_type = self.visit(ast.arr, param)
        if not isinstance(arr_type, ArrayType):
            raise TypeMismatch(ast)

        local_env = param.copy()

        local_env.insert(0, Symbol(ast.idx.name, IntType()))
        local_env.insert(0, Symbol(ast.value.name, arr_type.eleType))

        self.visit(ast.loop, local_env)
        return None

    @override
    def visitBreak(self, ast, param) -> None:
        return None

    @override
    def visitContinue(self, ast, param) -> None:
        return None

    @override
    def visitReturn(self, ast, param):
        func_type = None
        for sym in param:
            if isinstance(sym.mtype, MType):
                func_type = sym.mtype.rettype
                break

        if func_type is None:
            raise TypeMismatch(ast)

        if isinstance(func_type, VoidType):
            if ast.expr is not None:
                raise TypeMismatch(ast)
        else:
            if ast.expr is None:
                raise TypeMismatch(ast)
            expr_type = self.visit(ast.expr, param)
            if not self._isTypeCompatible(func_type, expr_type):
                raise TypeMismatch(ast)

        return None

    @override
    def visitBinaryOp(self, ast, param):
        left_type = self.visit(ast.left, param)
        right_type = self.visit(ast.right, param)
        op = ast.op

        if op in ["+", "-", "*", "/"]:
            return self._handleArithmeticOp(op, left_type, right_type, ast)

        if op == "%":
            return self._handleModuloOp(left_type, right_type, ast)

        if op in ["==", "!=", "<", "<=", ">", ">="]:
            return self._handleComparisonOp(op, left_type, right_type, ast)

        if op in ["&&", "||"]:
            return self._handleBooleanOp(left_type, right_type, ast)

        raise TypeMismatch(ast)

    def _handleArithmeticOp(self, op, left, right, ast):
        if isinstance(left, StringType) and isinstance(right, StringType) and op == "+":
            return StringType()
        if self._isNumeric(left) and self._isNumeric(right):
            return (
                FloatType()
                if isinstance(left, FloatType) or isinstance(right, FloatType)
                else IntType()
            )
        raise TypeMismatch(ast)

    def _handleModuloOp(self, left, right, ast):
        if isinstance(left, IntType) and isinstance(right, IntType):
            return IntType()
        raise TypeMismatch(ast)

    def _handleComparisonOp(self, op, left, right, ast):
        if type(left) is not type(right):
            raise TypeMismatch(ast)
        if isinstance(left, (IntType, FloatType, StringType)):
            return BoolType()
        raise TypeMismatch(ast)

    def _handleBooleanOp(self, left, right, ast):
        if isinstance(left, BoolType) and isinstance(right, BoolType):
            return BoolType()
        raise TypeMismatch(ast)

    def _isNumeric(self, typ):
        return isinstance(typ, (IntType, FloatType))

    @override
    def visitUnaryOp(self, ast, param):
        operand_type = self.visit(ast.body, param)
        op = ast.op

        if op == "!":
            if isinstance(operand_type, BoolType):
                return BoolType()
            raise TypeMismatch(ast)

        if op == "-":
            if isinstance(operand_type, IntType):
                return IntType()
            if isinstance(operand_type, FloatType):
                return FloatType()
            raise TypeMismatch(ast)

        raise TypeMismatch(ast)

    @override
    def visitFuncCall(self, ast, param) -> Type:
        sym = self.lookup(ast.funName, param, lambda x: x.name)
        if sym is None:
            raise Undeclared(Function(), ast.funName)
        if not isinstance(sym.mtype, MType):
            raise TypeMismatch(ast)

        return self._checkFunctionCall(
            ast.funName, ast.args, param, sym.mtype.partype, sym.mtype.rettype, ast
        )

    def _checkFunctionCall(
        self, name: str, args: list, param, partypes, rettype, ast
    ) -> Type:
        if len(args) != len(partypes):
            raise TypeMismatch(ast)

        for arg, expected_type in zip(args, partypes):
            arg_type = self.visit(arg, param)
            if not self._isTypeCompatible(expected_type, arg_type):
                raise TypeMismatch(ast)

        return rettype

    @override
    def visitMethCall(self, ast, param):
        recv_type = self.visit(ast.receiver, param)
        if not isinstance(recv_type, (StructType, InterfaceType)):
            raise TypeMismatch(ast)

        method_decl = self._getMethodFromReceiver(recv_type, ast.metName, ast)

        if isinstance(method_decl, FuncDecl):
            partypes = [p.parType for p in method_decl.params]
            rettype = method_decl.retType
        else:
            partypes = method_decl.params
            rettype = method_decl.retType

        return self._checkFunctionCall(
            ast.metName, ast.args, param, partypes, rettype, ast
        )

    def _getMethodFromReceiver(self, recv_type, method_name, ast):
        if isinstance(recv_type, StructType):
            for m in recv_type.methods:
                if m.fun.name == method_name:
                    return m.fun
        elif isinstance(recv_type, InterfaceType):
            for proto in recv_type.methods:
                if proto.name == method_name:
                    return proto

        raise Undeclared(Method(), method_name)
