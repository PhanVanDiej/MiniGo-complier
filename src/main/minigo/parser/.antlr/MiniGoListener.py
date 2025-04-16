# Generated from d:/Nam3-HK2/KienTrucPM/DoAn/MiniGo-complier/assignment1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete listener for a parse tree produced by MiniGoParser.
class MiniGoListener(ParseTreeListener):

    # Enter a parse tree produced by MiniGoParser#program.
    def enterProgram(self, ctx:MiniGoParser.ProgramContext):
        pass

    # Exit a parse tree produced by MiniGoParser#program.
    def exitProgram(self, ctx:MiniGoParser.ProgramContext):
        pass


    # Enter a parse tree produced by MiniGoParser#packageDecl.
    def enterPackageDecl(self, ctx:MiniGoParser.PackageDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#packageDecl.
    def exitPackageDecl(self, ctx:MiniGoParser.PackageDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#importDecl.
    def enterImportDecl(self, ctx:MiniGoParser.ImportDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#importDecl.
    def exitImportDecl(self, ctx:MiniGoParser.ImportDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#importSpec.
    def enterImportSpec(self, ctx:MiniGoParser.ImportSpecContext):
        pass

    # Exit a parse tree produced by MiniGoParser#importSpec.
    def exitImportSpec(self, ctx:MiniGoParser.ImportSpecContext):
        pass


    # Enter a parse tree produced by MiniGoParser#decl.
    def enterDecl(self, ctx:MiniGoParser.DeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#decl.
    def exitDecl(self, ctx:MiniGoParser.DeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#vardecl.
    def enterVardecl(self, ctx:MiniGoParser.VardeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#vardecl.
    def exitVardecl(self, ctx:MiniGoParser.VardeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#shortVardecl.
    def enterShortVardecl(self, ctx:MiniGoParser.ShortVardeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#shortVardecl.
    def exitShortVardecl(self, ctx:MiniGoParser.ShortVardeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typedecl.
    def enterTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typedecl.
    def exitTypedecl(self, ctx:MiniGoParser.TypedeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#funcdecl.
    def enterFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#funcdecl.
    def exitFuncdecl(self, ctx:MiniGoParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#methodDecl.
    def enterMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        pass

    # Exit a parse tree produced by MiniGoParser#methodDecl.
    def exitMethodDecl(self, ctx:MiniGoParser.MethodDeclContext):
        pass


    # Enter a parse tree produced by MiniGoParser#receiver.
    def enterReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass

    # Exit a parse tree produced by MiniGoParser#receiver.
    def exitReceiver(self, ctx:MiniGoParser.ReceiverContext):
        pass


    # Enter a parse tree produced by MiniGoParser#result.
    def enterResult(self, ctx:MiniGoParser.ResultContext):
        pass

    # Exit a parse tree produced by MiniGoParser#result.
    def exitResult(self, ctx:MiniGoParser.ResultContext):
        pass


    # Enter a parse tree produced by MiniGoParser#paramlist.
    def enterParamlist(self, ctx:MiniGoParser.ParamlistContext):
        pass

    # Exit a parse tree produced by MiniGoParser#paramlist.
    def exitParamlist(self, ctx:MiniGoParser.ParamlistContext):
        pass


    # Enter a parse tree produced by MiniGoParser#param.
    def enterParam(self, ctx:MiniGoParser.ParamContext):
        pass

    # Exit a parse tree produced by MiniGoParser#param.
    def exitParam(self, ctx:MiniGoParser.ParamContext):
        pass


    # Enter a parse tree produced by MiniGoParser#typespec.
    def enterTypespec(self, ctx:MiniGoParser.TypespecContext):
        pass

    # Exit a parse tree produced by MiniGoParser#typespec.
    def exitTypespec(self, ctx:MiniGoParser.TypespecContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primitiveType.
    def enterPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primitiveType.
    def exitPrimitiveType(self, ctx:MiniGoParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#arrayType.
    def enterArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#arrayType.
    def exitArrayType(self, ctx:MiniGoParser.ArrayTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#sliceType.
    def enterSliceType(self, ctx:MiniGoParser.SliceTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#sliceType.
    def exitSliceType(self, ctx:MiniGoParser.SliceTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#structType.
    def enterStructType(self, ctx:MiniGoParser.StructTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#structType.
    def exitStructType(self, ctx:MiniGoParser.StructTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#pointerType.
    def enterPointerType(self, ctx:MiniGoParser.PointerTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#pointerType.
    def exitPointerType(self, ctx:MiniGoParser.PointerTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#functionType.
    def enterFunctionType(self, ctx:MiniGoParser.FunctionTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#functionType.
    def exitFunctionType(self, ctx:MiniGoParser.FunctionTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#interfaceType.
    def enterInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#interfaceType.
    def exitInterfaceType(self, ctx:MiniGoParser.InterfaceTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#mapType.
    def enterMapType(self, ctx:MiniGoParser.MapTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#mapType.
    def exitMapType(self, ctx:MiniGoParser.MapTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#stmt.
    def enterStmt(self, ctx:MiniGoParser.StmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#stmt.
    def exitStmt(self, ctx:MiniGoParser.StmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#simpleStmt.
    def enterSimpleStmt(self, ctx:MiniGoParser.SimpleStmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#simpleStmt.
    def exitSimpleStmt(self, ctx:MiniGoParser.SimpleStmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#assignstmt.
    def enterAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#assignstmt.
    def exitAssignstmt(self, ctx:MiniGoParser.AssignstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#lhs.
    def enterLhs(self, ctx:MiniGoParser.LhsContext):
        pass

    # Exit a parse tree produced by MiniGoParser#lhs.
    def exitLhs(self, ctx:MiniGoParser.LhsContext):
        pass


    # Enter a parse tree produced by MiniGoParser#exprStmt.
    def enterExprStmt(self, ctx:MiniGoParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#exprStmt.
    def exitExprStmt(self, ctx:MiniGoParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#incDecStmt.
    def enterIncDecStmt(self, ctx:MiniGoParser.IncDecStmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#incDecStmt.
    def exitIncDecStmt(self, ctx:MiniGoParser.IncDecStmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#ifstmt.
    def enterIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#ifstmt.
    def exitIfstmt(self, ctx:MiniGoParser.IfstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#forstmt.
    def enterForstmt(self, ctx:MiniGoParser.ForstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#forstmt.
    def exitForstmt(self, ctx:MiniGoParser.ForstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#switchstmt.
    def enterSwitchstmt(self, ctx:MiniGoParser.SwitchstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#switchstmt.
    def exitSwitchstmt(self, ctx:MiniGoParser.SwitchstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#caseclause.
    def enterCaseclause(self, ctx:MiniGoParser.CaseclauseContext):
        pass

    # Exit a parse tree produced by MiniGoParser#caseclause.
    def exitCaseclause(self, ctx:MiniGoParser.CaseclauseContext):
        pass


    # Enter a parse tree produced by MiniGoParser#blockstmt.
    def enterBlockstmt(self, ctx:MiniGoParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#blockstmt.
    def exitBlockstmt(self, ctx:MiniGoParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#gostmt.
    def enterGostmt(self, ctx:MiniGoParser.GostmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#gostmt.
    def exitGostmt(self, ctx:MiniGoParser.GostmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#deferstmt.
    def enterDeferstmt(self, ctx:MiniGoParser.DeferstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#deferstmt.
    def exitDeferstmt(self, ctx:MiniGoParser.DeferstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#returnstmt.
    def enterReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#returnstmt.
    def exitReturnstmt(self, ctx:MiniGoParser.ReturnstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#breakstmt.
    def enterBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#breakstmt.
    def exitBreakstmt(self, ctx:MiniGoParser.BreakstmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#continuestmt.
    def enterContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        pass

    # Exit a parse tree produced by MiniGoParser#continuestmt.
    def exitContinuestmt(self, ctx:MiniGoParser.ContinuestmtContext):
        pass


    # Enter a parse tree produced by MiniGoParser#expr.
    def enterExpr(self, ctx:MiniGoParser.ExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#expr.
    def exitExpr(self, ctx:MiniGoParser.ExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#unaryExpr.
    def enterUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#unaryExpr.
    def exitUnaryExpr(self, ctx:MiniGoParser.UnaryExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#unaryOp.
    def enterUnaryOp(self, ctx:MiniGoParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#unaryOp.
    def exitUnaryOp(self, ctx:MiniGoParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#binaryOp.
    def enterBinaryOp(self, ctx:MiniGoParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by MiniGoParser#binaryOp.
    def exitBinaryOp(self, ctx:MiniGoParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by MiniGoParser#primaryExpr.
    def enterPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        pass

    # Exit a parse tree produced by MiniGoParser#primaryExpr.
    def exitPrimaryExpr(self, ctx:MiniGoParser.PrimaryExprContext):
        pass


    # Enter a parse tree produced by MiniGoParser#operand.
    def enterOperand(self, ctx:MiniGoParser.OperandContext):
        pass

    # Exit a parse tree produced by MiniGoParser#operand.
    def exitOperand(self, ctx:MiniGoParser.OperandContext):
        pass


    # Enter a parse tree produced by MiniGoParser#basicLit.
    def enterBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        pass

    # Exit a parse tree produced by MiniGoParser#basicLit.
    def exitBasicLit(self, ctx:MiniGoParser.BasicLitContext):
        pass


    # Enter a parse tree produced by MiniGoParser#functionLit.
    def enterFunctionLit(self, ctx:MiniGoParser.FunctionLitContext):
        pass

    # Exit a parse tree produced by MiniGoParser#functionLit.
    def exitFunctionLit(self, ctx:MiniGoParser.FunctionLitContext):
        pass


    # Enter a parse tree produced by MiniGoParser#compositeLit.
    def enterCompositeLit(self, ctx:MiniGoParser.CompositeLitContext):
        pass

    # Exit a parse tree produced by MiniGoParser#compositeLit.
    def exitCompositeLit(self, ctx:MiniGoParser.CompositeLitContext):
        pass


    # Enter a parse tree produced by MiniGoParser#literalType.
    def enterLiteralType(self, ctx:MiniGoParser.LiteralTypeContext):
        pass

    # Exit a parse tree produced by MiniGoParser#literalType.
    def exitLiteralType(self, ctx:MiniGoParser.LiteralTypeContext):
        pass


    # Enter a parse tree produced by MiniGoParser#keyValList.
    def enterKeyValList(self, ctx:MiniGoParser.KeyValListContext):
        pass

    # Exit a parse tree produced by MiniGoParser#keyValList.
    def exitKeyValList(self, ctx:MiniGoParser.KeyValListContext):
        pass


    # Enter a parse tree produced by MiniGoParser#keyVal.
    def enterKeyVal(self, ctx:MiniGoParser.KeyValContext):
        pass

    # Exit a parse tree produced by MiniGoParser#keyVal.
    def exitKeyVal(self, ctx:MiniGoParser.KeyValContext):
        pass


    # Enter a parse tree produced by MiniGoParser#conversion.
    def enterConversion(self, ctx:MiniGoParser.ConversionContext):
        pass

    # Exit a parse tree produced by MiniGoParser#conversion.
    def exitConversion(self, ctx:MiniGoParser.ConversionContext):
        pass


    # Enter a parse tree produced by MiniGoParser#exprlist.
    def enterExprlist(self, ctx:MiniGoParser.ExprlistContext):
        pass

    # Exit a parse tree produced by MiniGoParser#exprlist.
    def exitExprlist(self, ctx:MiniGoParser.ExprlistContext):
        pass


    # Enter a parse tree produced by MiniGoParser#idlist.
    def enterIdlist(self, ctx:MiniGoParser.IdlistContext):
        pass

    # Exit a parse tree produced by MiniGoParser#idlist.
    def exitIdlist(self, ctx:MiniGoParser.IdlistContext):
        pass



del MiniGoParser