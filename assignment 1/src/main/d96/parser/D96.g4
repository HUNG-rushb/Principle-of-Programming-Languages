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

// INTTYPE: 'int';

// VOIDTYPE: 'void';	
	

// fragment SIGN               :  [+-]? ;
// fragment SCIENTIFIC         :  [e](SIGN)(DIGIT)+ ;
// fragment DECIMAL_POINT      :  [.](DIGIT)+ ;

// REAL               :  SIGN(DIGIT)+(DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC) ;
// INT                :  SIGN(DIGIT)+ ;
// ID                 :  LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)* ;
// STRING             :  ['][^']+['] ;


// Integer literal 
INTLIT: DEC | HEX | OCT | BIN;

fragment DEC:([1-9] [0-9]* (UNDERSCORE [0-9]+)*){ self.text = self.text.replace("_", "")} | '0';
fragment HEX: '0' X [1-9]+;
fragment OCT: '0' [0-9a-fA-F]+; 
fragment BIN: '0' B [01]+;


// Float literal 
FLOATLIT: DEC DECIMALPART EXPONENTPART;
fragment DECIMALPART: (DOT [0-9]+)?;
fragment EXPONENTPART:[0-9]*? (E (MINUSOP | PLUSOP)? [1-9]+)?;

// Boolean literal 
BOOLLIT: TRUE | FALSE;

// String literal 
STRINGLIT:;

// Indexed Array literal 
INDEXEDARRAYLIT:;

// Multi-dimensional Array literal 
MULTIDIMENSIONALARRAYLIT:;

// -----------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------
// -----------------------------------------------------------------------------------------
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

SELF: 'Self';

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
DOT: '.';
COMMA: ',';
COLON:':';
SEMICOLON: ';';
// SEPARATOR: ;


DOLLARD: '$';

// Skip comments
// BLOCK_COMMENT: ('**' .*? '**' | LP .*? RP) -> skip ;
BLOCK_COMMENT: '**' .*? '**' -> skip;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;


ESC_SEQ: '\\' [btnfr"'\\] ;
ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\' ;


ERROR_CHAR: . { raise ErrorToken(self.text) };

// Name
ID:[_a-zA-Z];

// Alphabet
fragment B: [bB];
fragment E: [eE];
fragment X: [xX];