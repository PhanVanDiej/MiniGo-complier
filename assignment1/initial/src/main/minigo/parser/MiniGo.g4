grammar MiniGo;

@lexer::header {
from lexererr import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit()
        raise UncloseString(result.text[0:])
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text[0:])
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    else:
        return super().emit()
}

options{
	language = Python3;
}

// Program structure
program: packageDecl importDecl* decl+ EOF;

// Package declaration
packageDecl: 'package' ID ';'?;

// Import declarations
importDecl: 'import' (STRINGLIT | '(' importSpec+ ')') ';'?;
importSpec: STRINGLIT ';'?;

// Declarations
decl: funcdecl | vardecl | typedecl;

// Variable declarations
vardecl:
	'var' (
		idlist typespec ';'
		| idlist typespec '=' exprlist ';'
		| '(' (ID typespec ('=' expr)? ';')* ')'
	);

// Short variable declarations (using :=)
shortVardecl: ID (',' ID)* ':=' exprlist ';';

// Type declarations
typedecl: 'type' ( ID typespec ';' | '(' (ID typespec ';')* ')');

// Function declarations
funcdecl:
	'func' ID '(' paramlist? ')' (typespec | '(' paramlist? ')')? blockstmt;

// Method declarations
methodDecl:
    'func' '(' receiver ')' ID '(' paramlist? ')' result? blockstmt;

receiver:
    ID ( '*'? typespec | '(' ID '*'? typespec ')' );

result:
    typespec 
    | '(' paramlist? ')'
    ;

// Parameter list
paramlist: param (',' param)*;
param:
	ID typespec
	| typespec
	| ID '...' typespec; // Variadic parameters with ...

// Type specifications
typespec:
	primitiveType
	| arrayType
	| sliceType
	| structType
	| pointerType
	| functionType
	| interfaceType
	| mapType;

primitiveType:
	'int'
	| 'int8'
	| 'int16'
	| 'int32'
	| 'int64'
	| 'uint'
	| 'uint8'
	| 'uint16'
	| 'uint32'
	| 'uint64'
	| 'float32'
	| 'float64'
	| 'float'
	| 'string'
	| 'bool'
	| 'byte'
	| 'rune';

arrayType: '[' expr ']' typespec;
sliceType: '[' ']' typespec;
structType: 'struct' '{' (ID typespec ';')* '}';
pointerType: '*' typespec;
functionType:
	'func' '(' paramlist? ')' (typespec | '(' paramlist? ')')?;
interfaceType:
	'interface' '{' (
		ID '(' paramlist? ')' (typespec | '(' paramlist? ')')? ';'
	)* '}';
mapType: 'map' '[' typespec ']' typespec;

// Statements
stmt:
	simpleStmt ';'
	| ifstmt
	| forstmt
	| switchstmt
	| blockstmt
	| returnstmt
	| breakstmt
	| continuestmt
	| gostmt
	| deferstmt
	| vardecl;

simpleStmt: assignstmt | shortVardecl | incDecStmt | exprStmt;

assignstmt:
	lhs ('=' | '+=' | '-=' | '*=' | '/=' | '%=') exprlist;
lhs: exprlist;

exprStmt: expr;

incDecStmt: expr ('++' | '--');

ifstmt:
	'if' (simpleStmt ';')? expr blockstmt (
		'else' (ifstmt | blockstmt)
	)?;

forstmt:
	'for' (
		| /* empty */
		| expr
		| simpleStmt? ';' expr? ';' simpleStmt?
		| ID (',' ID)* ':=' 'range' expr
	) blockstmt;

switchstmt:
	'switch' (simpleStmt ';')? expr? '{' caseclause* '}';
caseclause: ('case' exprlist | 'default') ':' stmt*;

blockstmt: '{' stmt* '}';

gostmt: 'go' expr ';';

deferstmt: 'defer' expr ';';

returnstmt: 'return' exprlist? ';';

breakstmt: 'break' ID? ';';

continuestmt: 'continue' ID? ';';

// Expressions - Fixed to handle operators correctly
expr:
	primaryExpr
	| unaryExpr
	| expr binaryOp expr
	| expr '?' expr ':' expr ; // Ternary operator (not actually in Go but useful)

unaryExpr: unaryOp expr;

unaryOp: '+' | '-' | '!' | '^' | '*' | '&' | '<-';
binaryOp:
	'+'
	| '-'
	| '*'
	| '/'
	| '%'
	| '&'
	| '|'
	| '^'
	| '<<'
	| '>>'
	| '&^'
	| '=='
	| '!='
	| '<'
	| '<='
	| '>'
	| '>='
	| '&&'
	| '||';

primaryExpr:
	operand
	| primaryExpr '.' ID
	| primaryExpr '[' expr ']'
	| primaryExpr '[' expr? ':' expr? ']' // Slice expressions
	| primaryExpr '(' exprlist? ')'
	| conversion;

operand:
	ID
	| basicLit
	| '(' expr ')'
	| functionLit
	| compositeLit;

basicLit: INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | RUNELIT;

functionLit:
	'func' '(' paramlist? ')' (typespec | '(' paramlist? ')')? blockstmt;

compositeLit: literalType '{' (keyValList | exprlist)? '}';
literalType: structType | arrayType | sliceType | mapType;
keyValList: keyVal (',' keyVal)*;
keyVal: (expr ':')? expr;

conversion: typespec '(' expr ')';

exprlist: expr (',' expr)*;

idlist: ID (',' ID)*;

// Operators - Removed BINOP and UNOP tokens All operators are now handled in the parser rules
// (unaryOp and binaryOp) We keep other tokens as before

// Literals
INTLIT: DECIMAL_LIT | OCTAL_LIT | HEX_LIT;
BINARY_LIT: '0' [bB][01]+;
DECIMAL_LIT: [1-9][0-9]* | '0';
OCTAL_LIT: '0' [0-7]+;
HEX_LIT: '0' [xX][0-9a-fA-F]+;

FLOATLIT: DECIMAL_FLOAT | HEX_FLOAT;
DECIMAL_FLOAT:
	[0-9]+ '.' [0-9]* EXPONENT?
	| '.' [0-9]+ EXPONENT?
	| [0-9]+ EXPONENT;
HEX_FLOAT:
	'0' [xX] [0-9a-fA-F]+ '.' [0-9a-fA-F]* HEX_EXPONENT
	| '0' [xX] '.' [0-9a-fA-F]+ HEX_EXPONENT
	| '0' [xX] [0-9a-fA-F]+ HEX_EXPONENT;
EXPONENT: [eE][+-]? [0-9]+;
HEX_EXPONENT: [pP][+-]? [0-9]+;

BOOLLIT: 'true' | 'false';
STRINGLIT: RAW_STRING | INTERPRETED_STRING;
RAW_STRING: '`' ~'`'* '`';
INTERPRETED_STRING: '"' ( ~["\r\n\\] | ESCAPED_CHAR)* '"';
ESCAPED_CHAR: '\\' [abfnrtv\\"'];

RUNELIT: '\'' ( ~['\r\n\\] | ESCAPED_CHAR) '\'';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Comments
COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' (BLOCK_COMMENT|.)*? '*/' -> skip;

// Whitespace
WS: [ \t\r\n]+ -> skip;

// Error handling
ERROR_CHAR: .
    {
        current = self.text
        if not hasattr(self, '_errors'):
            self._errors = []
        self._errors.append(ErrorToken(current))
    };
ILLEGAL_ESCAPE:
    '"' ( ~["\r\n\\] | '\\' [btnfr"'\\] )* '\\' ~[btnfr"'\\] (~["\r\n])*
    {
        result = self.text
        raise IllegalEscape(result[0:])
    }
    ;
    
fragment ESC_SEQ: '\\' [btnfr"'\\];
UNCLOSE_STRING:
	'"' (ESC_SEQ | ~["\\\r\n])* (EOF | [\r\n]) {
        text = self.text
        if text.endswith('\n') or text.endswith('\r\n'):
            text = text[:-1]
        raise UncloseString(text)
    };