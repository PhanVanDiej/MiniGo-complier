grammar MiniGo;

@lexer::header {
from lexererr import *
}

@lexer::members {
    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit()
            text = result.text
            if text[-1] in ['\n', '\r']:
                raise UncloseString(text[:-1]) 
            else:
                raise UncloseString(text)       
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text)    
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        else:
            return super().emit()
}

options{
	language = Python3;
}

// ==================== Parser Rules ====================
program: decl+ EOF;
decl: funcdecl | vardecl;
vardecl: 'var' ID 'int' ';';
funcdecl: 'func' ID '(' ')' '{' '}';

// ====================== Literals ======================
INTLIT: DecimalLit | OctalLit | HexLit | BinaryLit;
fragment DecimalLit: [1-9][0-9]* | '0';
fragment OctalLit: '0' [0-7]+;
fragment HexLit: '0' [xX][0-9a-fA-F]+;
fragment BinaryLit: '0' [bB][01]+;

FLOATLIT: DecimalFloat | HexFloat;
fragment DecimalFloat:
	[0-9]+ '.' [0-9]* ([eE][+-]? [0-9]+)?
	| '.' [0-9]+ ([eE][+-]? [0-9]+)?
	| [0-9]+ [eE][+-]? [0-9]+;
fragment HexFloat:
	'0' [xX] ([0-9a-fA-F]+ '.'? | [0-9a-fA-F]* '.' [0-9a-fA-F]+) [pP][+-]? [0-9]+;

BOOLLIT: 'true' | 'false';

STRINGLIT: '"' (~["\\\n] | EscapeSeq)* '"';
fragment EscapeSeq: '\\' [btnfr'"\\];

RUNELIT: '\'' (~['\\\n] | EscapeSeq) '\'';

// ====================== Keywords ======================
VAR: 'var';
FUNC: 'func';
IF: 'if';
ELSE: 'else';
FOR: 'for';
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'boolean';

// ===================== Operators ======================
INCREMENT: '++';
DECREMENT: '--';
PLUS_ASSIGN: '+=';
MINUS_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';
EQ: '==';
NEQ: '!=';
LE: '<=';
GE: '>=';
LT: '<';
GT: '>';
AND: '&&';
OR: '||';
NOT: '!';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';

// ==================== Separators ======================
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
LBRACKET: '[';
RBRACKET: ']';
SEMI: ';';
COMMA: ',';
COLON: ':';
DOT: '.';

// ==================== Identifier ======================
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// ==================== Whitespace ======================
WS: [ \t\r\n]+ -> skip;
LINE_COMMENT: '//' ~[\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// ==================== Error Rules ====================
UNCLOSE_STRING: '"' (~["\\\n] | EscapeSeq)* (EOF | '\n');
ILLEGAL_ESCAPE: '"' (~["\\\n] | EscapeSeq)* '\\' ~[btnfr'"\\];
ERROR_CHAR: . { raise ErrorToken(self.text) };