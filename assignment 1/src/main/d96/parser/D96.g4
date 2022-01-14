// Trinh Duy Hung
// 1913652

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

// program: mptype 'main' LCB RCB LB body? RB EOF;
program: BLOCK_COMMENT;
// program: (vardclr | funcdclr)+ EOF;

// mptype: INTTYPE | VOIDTYPE;

body: funcall SEMICOLON;

exp: funcall | INTLIT;

funcall:  LB exp? RB;

//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\



// String literal 
STRINGLIT: ('"') STRING_CHAR* ('"') 
{
	self.text = str(self.text)[1:-1].replace('\"','')
};

// Indexed Array literal 
indexarraylit: ARRAY LB ((TYPE | indexarraylit) (COMMA (TYPE | indexarraylit)*))? RB;

// Multi-dimensional Array literal 
// multidimensionalarraylit:;

// -----------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------
//   _      ________   ________ _____  
//  | |    |  ____\ \ / /  ____|  __ \ 
//  | |    | |__   \ V /| |__  | |__) |
//  | |    |  __|   > < |  __| |  _  / 
//  | |____| |____ / . \| |____| | \ \ 
//  |______|______/_/ \_\______|_|  \_\                    

TYPE: INT | FLOAT | BOOLEAN | STRING;
// VALUE: NULL | INTLIT | FLOATLIT | STRINGLIT | BOOLLIT | INDEXEDARRAYLIT | MULTIDIMENSIONALARRAYLIT;
CONDITION: IF | ELSEIF | ELSE;

// Integer literal 
INTLIT: DEC { 
	self.text = self.text.replace("_", "")
	} 
	| HEX 
	| OCT 
	| BIN;
fragment DEC: [1-9]+ (UNDERSCORE | [0-9])*  ;
fragment HEX: '0' X [0-9a-fA-F]+;
fragment OCT: '0' [0-7]+; 
fragment BIN: '0' B [01]+;


// Float literal 
FLOATLIT: [0-9]+ (DECIMALPART EXPONENTPART? | EXPONENTPART);
fragment DECIMALPART: '.' [0-9]+;
fragment EXPONENTPART:E (MINUSOP | PLUSOP)? [0-9]+;
// fragment EXPONENTPART:E [+-]? [0-9]+;

// Boolean literal 
BOOLLIT: TRUE | FALSE;

// Identifiers
IDENTIFIERS: (DOLLAR [_a-zA-Z0-9]+) | ([_a-zA-Z] [_a-zA-Z0-9]*);
fragment DOLLAR: '$';

// Stop Statement
BREAK: 'Break';
CONTINUE: 'Continue';

// Flow Statement
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';

// Boolean Value
TRUE: 'True';
FALSE: 'False';

// Primitive Types
ARRAY: 'Array';
IN: 'In';
INT: 'Int';
FLOAT: 'Float';
BOOLEAN:'Boolean';
STRING: 'String';
RETURN: 'Return';

// Null
NULL: 'Null';

// Class
CLASS: 'Class';
VAL: 'Val';
VAR: 'Var';
CONSTRUCTOR: 'Constructor';
DESTRUCTOR: 'Destructor';
NEW: 'New';
BY: 'By';
// SELF: 'Self';

// Operators
DOUBLECOLONOP: '::';
DOUBLEDOTOP: '.';
UNDERSCORE: '_';
PLUSOP: '+';
MINUSOP: '-';
MULTIPLYOP: '*';
DIVIDEOP: '/';
MODULOOP: '%';
NOTOP: '!';
ANDOP: '&&';
OROP: '||';
EQUALOP: '==';
ASSIGNOP: '=';
NOTEQUAL: '!=';
GT : '>' ;
LT : '<' ;
GTE: '>=';
LTE: '<=';
STREQUALOP: '==.';
STRCONCATOP: '+.';

// Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
// DOT: '.';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';
// SEPARATOR: ;

// Skip comments
BLOCK_COMMENT: '##' .*? '##' -> skip;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

// UNCLOSE_STRING: '"' STRING_CHAR* ( [\t\r\n\f\b"'\\] | EOF )
UNCLOSE_STRING: '"' STRING_CHAR* 
{
	current = str(self.text)
	raise UncloseString(y[1:])
};

ILLEGAL_ESCAPE: '"' STRING_CHAR* ESC_UNAVAILABLE
{
	current = str(self.text)
	raise IllegalEscape(current[1:])
};

// String char except special character 

// fragment STRING_CHAR: ~[\\"] | ESC_CHAR | '\'"';
fragment STRING_CHAR: ~[\b\t\n\f\r"'\\] | ESC_CHAR;

fragment ESC_CHAR: '\\' [trnfb"'\\];

fragment ESC_UNAVAILABLE: '\\' ~[trnfb"'\\] | ~'\\';


ERROR_CHAR: . { raise ErrorToken(self.text) };

// Name
ID: [_a-zA-Z]+;

// Alphabet
fragment B: [bB];
fragment E: [eE];
fragment X: [xX];