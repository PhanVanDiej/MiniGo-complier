# Generated from d:/Nam3-HK2/KienTrucPM/TaiLieu/Assignment1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,54,32,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,10,8,0,11,0,12,
        0,11,1,0,1,0,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,0,0,4,0,2,4,6,0,0,29,0,9,1,0,0,0,2,17,1,0,0,
        0,4,19,1,0,0,0,6,24,1,0,0,0,8,10,3,2,1,0,9,8,1,0,0,0,10,11,1,0,0,
        0,11,9,1,0,0,0,11,12,1,0,0,0,12,13,1,0,0,0,13,14,5,0,0,1,14,1,1,
        0,0,0,15,18,3,6,3,0,16,18,3,4,2,0,17,15,1,0,0,0,17,16,1,0,0,0,18,
        3,1,0,0,0,19,20,5,6,0,0,20,21,5,48,0,0,21,22,5,14,0,0,22,23,5,44,
        0,0,23,5,1,0,0,0,24,25,5,7,0,0,25,26,5,48,0,0,26,27,5,38,0,0,27,
        28,5,39,0,0,28,29,5,40,0,0,29,30,5,41,0,0,30,7,1,0,0,0,2,11,17
    ]

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
        self.checkVersion("4.13.1")
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
                if not (_la==6 or _la==7):
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




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.funcdecl()
                pass
            elif token in [6]:
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





