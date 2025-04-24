from AST import FloatType, IntType, VoidType
from StaticError import (
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


class StaticChecker(BaseVisitor, Utils):
    def __init__(self, ast) -> None:
        self.ast = ast
        self.global_envi = [
            Symbol("getInt", MType([], IntType())),
            Symbol("putInt", MType([IntType()], VoidType())),
            Symbol("putIntLn", MType([IntType()], VoidType())),
            Symbol("getFloat", MType([], FloatType())),
        ]

    def check(self):
        return self.visit(self.ast, self.global_envi)

    def visitProgram(self, ast, param):
        reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, ast.decl, param)
        return param

    def visitVarDecl(self, ast, param):
        res = self.lookup(ast.varName, param, lambda x: x.name)
        if not res is None:
            raise Redeclared(Variable(), ast.varName)
        if ast.varInit:
            initType = self.visit(ast.varInit, param)
            if ast.varType is None:
                ast.varType = initType
            if not type(ast.varType) is type(initType):
                raise TypeMismatch(ast)
        return Symbol(ast.varName, ast.varType, None)

    def visitFuncDecl(self, ast, param):
        res = self.lookup(ast.name, param, lambda x: x.name)
        if not res is None:
            raise Redeclared(Function(), ast.name)
        return Symbol(ast.name, MType([], ast.retType))

    def visitIntLiteral(self, ast, param):
        return IntType()

    def visitFloatLiteral(self, ast, param):
        return FloatType()

    def visitId(self, ast, param):
        res = self.lookup(ast.name, param, lambda x: x.name)
        if res is None:
            raise Undeclared(Identifier(), ast.name)
        return res.mtype
