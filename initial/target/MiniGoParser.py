# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\38")
        buf.write("\"\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\6\2\f\n\2\r\2\16")
        buf.write("\2\r\3\2\3\2\3\3\3\3\5\3\24\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\2\2\6\2\4\6\b\2\2\2\37")
        buf.write("\2\13\3\2\2\2\4\23\3\2\2\2\6\25\3\2\2\2\b\32\3\2\2\2\n")
        buf.write("\f\5\4\3\2\13\n\3\2\2\2\f\r\3\2\2\2\r\13\3\2\2\2\r\16")
        buf.write("\3\2\2\2\16\17\3\2\2\2\17\20\7\2\2\3\20\3\3\2\2\2\21\24")
        buf.write("\5\b\5\2\22\24\5\6\4\2\23\21\3\2\2\2\23\22\3\2\2\2\24")
        buf.write("\5\3\2\2\2\25\26\7\b\2\2\26\27\7\62\2\2\27\30\7\20\2\2")
        buf.write("\30\31\7.\2\2\31\7\3\2\2\2\32\33\7\t\2\2\33\34\7\62\2")
        buf.write("\2\34\35\7(\2\2\35\36\7)\2\2\36\37\7*\2\2\37 \7+\2\2 ")
        buf.write("\t\3\2\2\2\4\r\23")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'var'", "'func'", "'if'", 
                     "'else'", "'for'", "'return'", "'break'", "'continue'", 
                     "'int'", "'float'", "'boolean'", "'++'", "'--'", "'+='", 
                     "'-='", "'*='", "'/='", "'=='", "'!='", "'<='", "'>='", 
                     "'<'", "'>'", "'&&'", "'||'", "'!'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "';'", "','", "':'", "'.'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                      "RUNELIT", "VAR", "FUNC", "IF", "ELSE", "FOR", "RETURN", 
                      "BREAK", "CONTINUE", "INT", "FLOAT", "BOOLEAN", "INCREMENT", 
                      "DECREMENT", "PLUS_ASSIGN", "MINUS_ASSIGN", "MUL_ASSIGN", 
                      "DIV_ASSIGN", "EQ", "NEQ", "LE", "GE", "LT", "GT", 
                      "AND", "OR", "NOT", "PLUS", "MINUS", "MUL", "DIV", 
                      "MOD", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                      "LBRACKET", "RBRACKET", "SEMI", "COMMA", "COLON", 
                      "DOT", "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3

    ruleNames =  [ "program", "decl", "vardecl", "funcdecl" ]

    EOF = Token.EOF
    INTLIT=1
    FLOATLIT=2
    BOOLLIT=3
    STRINGLIT=4
    RUNELIT=5
    VAR=6
    FUNC=7
    IF=8
    ELSE=9
    FOR=10
    RETURN=11
    BREAK=12
    CONTINUE=13
    INT=14
    FLOAT=15
    BOOLEAN=16
    INCREMENT=17
    DECREMENT=18
    PLUS_ASSIGN=19
    MINUS_ASSIGN=20
    MUL_ASSIGN=21
    DIV_ASSIGN=22
    EQ=23
    NEQ=24
    LE=25
    GE=26
    LT=27
    GT=28
    AND=29
    OR=30
    NOT=31
    PLUS=32
    MINUS=33
    MUL=34
    DIV=35
    MOD=36
    ASSIGN=37
    LPAREN=38
    RPAREN=39
    LBRACE=40
    RBRACE=41
    LBRACKET=42
    RBRACKET=43
    SEMI=44
    COMMA=45
    COLON=46
    DOT=47
    ID=48
    WS=49
    LINE_COMMENT=50
    BLOCK_COMMENT=51
    UNCLOSE_STRING=52
    ILLEGAL_ESCAPE=53
    ERROR_CHAR=54

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 8
                self.decl()
                self.state = 11 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.VAR or _la==MiniGoParser.FUNC):
                    break

            self.state = 13
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.FUNC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.funcdecl()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def SEMI(self):
            return self.getToken(MiniGoParser.SEMI, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(MiniGoParser.VAR)
            self.state = 20
            self.match(MiniGoParser.ID)
            self.state = 21
            self.match(MiniGoParser.INT)
            self.state = 22
            self.match(MiniGoParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def LPAREN(self):
            return self.getToken(MiniGoParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(MiniGoParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(MiniGoParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(MiniGoParser.RBRACE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(MiniGoParser.FUNC)
            self.state = 25
            self.match(MiniGoParser.ID)
            self.state = 26
            self.match(MiniGoParser.LPAREN)
            self.state = 27
            self.match(MiniGoParser.RPAREN)
            self.state = 28
            self.match(MiniGoParser.LBRACE)
            self.state = 29
            self.match(MiniGoParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





