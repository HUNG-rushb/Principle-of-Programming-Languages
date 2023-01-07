// Trịnh Duy Hưng 
// 1913652
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:  EOF ;






//   _      ________   ________ _____  
//  | |    |  ____\ \ / /  ____|  __ \ 
//  | |    | |__   \ V /| |__  | |__) |
//  | |    |  __|   > < |  __| |  _  / 
//  | |____| |____ / . \| |____| | \ \ 
//  |______|______/_/ \_\______|_|  \_\                    

FUNCTION: 'function';

AUTO: 'auto';
BREAK: 'break';
DO: 'do';
ELSE: 'else';
FOR: 'for';
IF: 'if';
RETURN: 'return';
WHILE: 'while';
OUT: 'out';
CONTINUE: 'continue';
OF: 'of';
INHERIT: 'inherit';


TRUE: 'true';
FALSE: 'false';

BOOLEAN: 'boolean';
FLOAT: 'float';
INTEGER: 'integer';
STRING: 'string';
VOID: 'void';


// Operators
fragment UNDERSCORE: '_';


PLUSOP: '+';
MINUSOP: '-';
MULTIPLYOP: '*';
DIVIDEOP: '/';
MODULOOP: '%';
NOTOP: '!';
ANDOP: '&&';
OROP: '||';
EQUALOP: '==';
NOTEQUALOP: '!=';
GTE: '>=';
LTE: '<=';
GT : '>' ;
LT : '<' ;
DOUBLECOLONOP: '::';

// Separators
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
LCB: '{';
RCB: '}';
DOT: '.';
COMMA: ',';
COLON: ':';
SEMICOLON: ';';
EQUAL: '=';







VARIABLE_IDENTIFIERS: [_a-zA-Z] [_a-zA-Z0-9]*;

UNCLOSE_STRING: '"' STRING_CHAR* 
{
	current = str(self.text)
	raise UncloseString(current[1:])
};

ILLEGAL_ESCAPE: '"' STRING_CHAR* ESC_UNAVAILABLE
{
	current = str(self.text)
	raise IllegalEscape(current[1:])
};


// String char except special character 
fragment STRING_CHAR:  '\'"'| ESC_CHAR | ~[\\"];

fragment ESC_CHAR: '\\' [trnfb'\\];

fragment ESC_UNAVAILABLE: '\\' ~[trnfb'\\] | '\\';

// Skip comments
COMMENT: '/*' .*? '*/' | '//' .*? [\n]-> skip;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

ERROR_CHAR: . { raise ErrorToken(self.text) };


