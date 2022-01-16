// Trinh Duy Hung
// 1913652

grammar D96;

@lexer::header {
from lexererr import *
import inspect
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit() # result mean for input

    # delete later
    print('--------------------------------------------------------------------------------')
    attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
    user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
    for i in user_defined_attr:
        if tk == i[1]:
            print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
    print('--------------------------------------------------------------------------------')
    return result
}

options {
	language = Python3;
}

// program: mptype 'main' LCB RCB LB body? RB EOF;
program: BLOCK_COMMENT;
// program: (vardclr | funcdclr)+ EOF;

// mptype: INTTYPE | VOIDTYPE;

// body: funcall SEMICOLON;

// exp: funcall | INTLIT;

// funcall:  LB exp? RB;

//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\

// Class declaration


// Variable declaration/
attr_declaration: (VAR | VAL) identifier_list COLON variable_type (value_list)? SEMICOLON;

// Method declaration
method_declaration: IDENTIFIERS LB list_parameters RB block_statements;



// Statements
block_statements: LCB statements RCB;


statements:;







// Exxpression
exp: exp ( op_and_then | op_or_else ) exp1 | exp1;

exp1: exp2 ( EQ | NEQ | GT | LT | GTE | LTE ) exp2 | exp2 ;

exp2: exp2 ( ADD | SUB | OR ) exp3 | exp3;

exp3: exp3 ( DIV | MUL | MOD | DIV_INT | AND ) exp4 | exp4;

exp4: (NOT | SUB) exp4 | operands ;

// Constructor Destructor
// constructor_dclr: CONSTRUCTOR LB list_parameters RB ;
// destructor_dclr: DESTRUCTOR;



// Array literal
array_lit: ARRAY LB array_val RB;
array_val: expr COMMA array_val | expr;

// Literals
literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit;


// List of parameters
list_parameters: parameters | ;
parameters: param SEMICOLON parameters | param;
param: identifier_list COLON variable_type;

// Identifiers list
// a, _b, C123
identifier_list: IDENTIFIERS (COMMA IDENTIFIERS)*;
// identifier_list: (identifier_list COMMA | IDENTIFIERS);

// Value list
value_list: literal (COMMA literal)*;







// Class type

// Array type
array_type: ARRAY LSB array_element_type COMMA array_size RSB;
array_element_type: array_type | INT | FLOAT | BOOLEAN | STRING;
array_size: INTLIT;

// Primitive type
primitive_type: BOOLEAN | INT | FLOAT | STRING;

// Variable type
variable_type: primitive_type | array_type;

//   _      ________   ________ _____  
//  | |    |  ____\ \ / /  ____|  __ \ 
//  | |    | |__   \ V /| |__  | |__) |
//  | |    |  __|   > < |  __| |  _  / 
//  | |____| |____ / . \| |____| | \ \ 
//  |______|______/_/ \_\______|_|  \_\                    

// Stop Statement
BREAK: 'Break';
CONTINUE: 'Continue';

// Flow Statement
IF: 'If';
ELSEIF: 'Elseif';
ELSE: 'Else';
FOREACH: 'Foreach';

// Boolean literal 
BOOLLIT: TRUE | FALSE;

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
DOUBLEDOTOP: '..';
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
GTE: '>=';
LTE: '<=';
GT : '>' ;
LT : '<' ;
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
COLON: ':';
SEMICOLON: ';';
// SEPARATOR: ;

// Identifiers
IDENTIFIERS: (DOLLAR [_a-zA-Z0-9]+) | ([_a-zA-Z] [_a-zA-Z0-9]*);
fragment DOLLAR: '$';

// String literal 
// '" -> "
STRINGLIT: ('"') STRING_CHAR* ('"') 
{
	self.text = str(self.text)[1:-1].replace('\'"','"')
	
};

// Float literal 
// fragment DECIMALPART: '.' ('0'+ | '0'* DEC) ;
// fragment EXPONENTPART: E UNDERSCORE* (MINUSOP | PLUSOP)? ('0'* DEC | '0'+);
fragment DECIMALPART: UNDERSCORE* '.' UNDERSCORE* ('0'+ | '0'* UNDERSCORE* DEC) UNDERSCORE*;
fragment EXPONENTPART: UNDERSCORE* E UNDERSCORE* (MINUSOP | PLUSOP)? UNDERSCORE*  ('0'* UNDERSCORE* DEC | '0'+) UNDERSCORE*;
// FLOATLIT: ((DEC | '0') (DECIMALPART EXPONENTPART? | EXPONENTPART) | (DECIMALPART EXPONENTPART)) 
FLOATLIT: ( (UNDERSCORE* (DEC | '0') UNDERSCORE* DECIMALPART UNDERSCORE* EXPONENTPART) 
            | (UNDERSCORE* (DEC | '0') UNDERSCORE* DECIMALPART)
            | (UNDERSCORE* (DEC | '0') UNDERSCORE* EXPONENTPART))
{self.text = self.text.replace("_", "")};

// Interher literal
fragment DEC: [1-9] (UNDERSCORE | [0-9])*;
fragment HEX: '0' X (UNDERSCORE | [0-9a-fA-F]+) (UNDERSCORE [0-9a-fA-F]+)*;
fragment OCT: '0' (UNDERSCORE | [0-7]+) (UNDERSCORE [0-7]+)*; 
fragment BIN: '0' B (UNDERSCORE | [01]+) (UNDERSCORE [01]+)*;
INTLIT: (DEC 
	| HEX 
	| OCT 
	| BIN) {self.text = self.text.replace("_", "")} 
	| '0';


// UNCLOSE_STRING: '"' STRING_CHAR* ( [\t\r\n\f\b"'\\] | EOF )
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

fragment ESC_UNAVAILABLE: '\\' ~[trnfb"'\\] | ~'\\';

// Skip comments
BLOCK_COMMENT: '##' .*? '##' -> skip;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

ERROR_CHAR: . { raise ErrorToken(self.text) };

// Name
ID: [_a-zA-Z]+;

// Alphabet
fragment B: [bB];
fragment E: [eE];
fragment X: [xX];