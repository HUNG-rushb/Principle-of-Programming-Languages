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

//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\

// Literals
literal:  INTLIT | FLOATLIT | BOOLLIT | STRINGLIT ;
//  array_lit;


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

// Boolean
TRUE: 'true';
FALSE: 'false';

BOOLEAN: 'boolean';
FLOAT: 'float';
INTEGER: 'integer';
STRING: 'string';
VOID: 'void';


// Operators
fragment UNDERSCORE: '_';

// operators: PLUSOP | MINUSOP | MULTIPLYOP | DIVIDEOP | MODULOOP | NOTOP | ANDOP
// 			| OROP | EQUALOP | NOTEQUALOP | GTE | LTE | EQUAL | GT | LT | DOUBLECOLONOP;
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
DOUBLECOLONOP: '::';
GTE: '>=';
LTE: '<=';
EQUAL: '=';
GT : '>' ;
LT : '<' ;

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


// Variable indentifiers
VARIABLE_IDENTIFIERS: [_a-zA-Z] [_a-zA-Z0-9]*;

// Boolean literal 
BOOLLIT: TRUE | FALSE;


// Float literal 
fragment DECIMALPART: '.' [0-9]*;
fragment EXPONENTPART: E (MINUSOP | PLUSOP)? ('0'* [1-9] [0-9]* | '0'+); 

FLOATLIT: ( ((DEC | '0') DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') DECIMALPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') EXPONENTPART) {self.text = self.text.replace("_", "")}
            | (DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")})
            // | DECIMALPART)
{self.text = self.text.replace("_", "")};

// Integer literal
fragment DEC: [1-9] (UNDERSCORE [0-9] | [0-9])*;

INTLIT: DEC;




// String literal 
// '" -> "
STRINGLIT: ('"') STRING_CHAR* ('"') 
{
        if str(self.text)[-1] == '"' and str(self.text)[-2] == '\'': 
            if not str(self.text)[-3] == '\\':
                raise UncloseString(str(self.text)[1:])
        
        current = self.text.find('\n')
        if current != -1: 
            raise UncloseString(str(self.text[:current - 1]))
        self.text = str(self.text)[1:-1]
};

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



// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

// Skip comments
BLOCK_CMT: '/*' .*? '*/' -> skip;
LINE_CMT : '//' .*? [\n] -> skip;

ERROR_CHAR: . { raise ErrorToken(self.text) };

fragment E: [eE];