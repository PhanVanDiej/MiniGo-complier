# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#packageDecl.
    def visitPackageDecl(self, ctx:MiniGoParser.PackageDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#importDecl.
    def visitImportDecl(self, ctx:MiniGoParser.ImportDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#importSpec.
    def visitImportSpec(self, ctx:MiniGoParser.ImportSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#vardecl.
    def visitVardecl(self, ctx:MiniGoParser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#shortVardecl.
    def visitShortVardecl(self, ctx:MiniGoParser.ShortVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typedecl.
    def visitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcdecl.
    def visitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodDecl.
    def visitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#receiver.
    def visitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#result.
    def visitResult(self, ctx:MiniGoParser.ResultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramlist.
    def visitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typespec.
    def visitTypespec(self, ctx:MiniGoParser.TypespecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primitiveType.
    def visitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrayType.
    def visitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#sliceType.
    def visitSliceType(self, ctx:MiniGoParser.SliceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structType.
    def visitStructType(self, ctx:MiniGoParser.StructTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#pointerType.
    def visitPointerType(self, ctx:MiniGoParser.PointerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functionType.
    def visitFunctionType(self, ctx:MiniGoParser.FunctionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceType.
    def visitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#mapType.
    def visitMapType(self, ctx:MiniGoParser.MapTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#stmt.
    def visitStmt(self, ctx:MiniGoParser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#simpleStmt.
    def visitSimpleStmt(self, ctx:MiniGoParser.SimpleStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignstmt.
    def visitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprStmt.
    def visitExprStmt(self, ctx:MiniGoParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#incDecStmt.
    def visitIncDecStmt(self, ctx:MiniGoParser.IncDecStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifstmt.
    def visitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forstmt.
    def visitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#switchstmt.
    def visitSwitchstmt(self, ctx:MiniGoParser.SwitchstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#caseclause.
    def visitCaseclause(self, ctx:MiniGoParser.CaseclauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#blockstmt.
    def visitBlockstmt(self, ctx:MiniGoParser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#gostmt.
    def visitGostmt(self, ctx:MiniGoParser.GostmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#deferstmt.
    def visitDeferstmt(self, ctx:MiniGoParser.DeferstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnstmt.
    def visitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakstmt.
    def visitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continuestmt.
    def visitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryExpr.
    def visitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#unaryOp.
    def visitUnaryOp(self, ctx:MiniGoParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#binaryOp.
    def visitBinaryOp(self, ctx:MiniGoParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#primaryExpr.
    def visitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#basicLit.
    def visitBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#functionLit.
    def visitFunctionLit(self, ctx:MiniGoParser.FunctionLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#compositeLit.
    def visitCompositeLit(self, ctx:MiniGoParser.CompositeLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalType.
    def visitLiteralType(self, ctx:MiniGoParser.LiteralTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyValList.
    def visitKeyValList(self, ctx:MiniGoParser.KeyValListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#keyVal.
    def visitKeyVal(self, ctx:MiniGoParser.KeyValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#conversion.
    def visitConversion(self, ctx:MiniGoParser.ConversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprlist.
    def visitExprlist(self, ctx:MiniGoParser.ExprlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#idlist.
    def visitIdlist(self, ctx:MiniGoParser.IdlistContext):
        return self.visitChildren(ctx)



del MiniGoParser