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


program: class_declarations class_main_program_declarations class_declarations EOF;
// program: forin_statements;

// program: variable_declaration+;
// program: expr+;


//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\

// Class declaration
class_main_program_declarations: CLASS PROGRAM program_block_class_statements;


class_declarations: class_declaration class_declarations | class_declaration | ;
class_declaration: CLASS VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance block_class_statements;
class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;
// class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance | COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;

// Constructor Destructor
constructor_dclr: CONSTRUCTOR LB list_parameters RB block_statements;
destructor_dclr: DESTRUCTOR LB RB block_statements;

// Member access
instance_attr_access: expr DOT (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS | SELF);
instance_method_access: expr DOT (VARIABLE_IN_FUNC_IDENTIFIERS| DOLLAR_IDENTIFIERS | SELF) LB list_expr RB;

static_attr_access: expr DOUBLECOLONOP (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS | SELF);
static_method_access: expr DOUBLECOLONOP (VARIABLE_IN_FUNC_IDENTIFIERS| DOLLAR_IDENTIFIERS | SELF) LB list_expr RB;

// Object creation
obj_creation: NEW (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_expr RB;

// Attribute declaration
// attribute_declaration: (VAR | VAL) identifier_list COLON variable_type ((ASSIGNOP (value_list | )) | ) SEMICOLON;

// Method declaration
method_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;



// STATEMENTS ------------------------------------------------------------------------------
// STATEMENTS ------------------------------------------------------------------------------
// STATEMENTS ------------------------------------------------------------------------------

// Variable declaration
variable_declaration: (VAR | VAL) identifier_list COLON variable_type (ASSIGNOP value_list | ) SEMICOLON;

// // Function declaration
function_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
main_function_declaration: MAIN LB RB block_statements;

// Assignment statement
assignment_statements: (VARIABLE_IN_FUNC_IDENTIFIERS 
                        | DOLLAR_IDENTIFIERS 
                        | instance_attr_access
                        | static_attr_access) ASSIGNOP expr SEMICOLON;

// If statements 
if_statements: IF LB expr RB (block_statements | ) elseif_list_statements else_statement;
elseif_list_statements: elseif_statement elseif_list_statements |  elseif_statement | ;
elseif_statement: ELSEIF LB expr RB (block_statements | );
else_statement: ELSE (block_statements | );

// For In statement
by_expr: (BY expr) | ;
forin_statements: FOREACH LB (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) IN expr DOUBLEDOTOP expr by_expr RB block_statements;


// Method invocation statement
methodinvocation_statement: (instance_method_access | static_method_access) SEMICOLON;
call_func: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_expr RB;
call_func_statement: call_func SEMICOLON;


// Break statement
break_statements: BREAK SEMICOLON;

// Continue statement
continue_statements: CONTINUE SEMICOLON;

// Return statement
return_expr: expr | ;
return_statements: RETURN return_expr SEMICOLON;

// Block statements ---------------------------------------------------------------------------------
// Block statements ---------------------------------------------------------------------------------
// Block statements ---------------------------------------------------------------------------------


program_block_class_statements: LCB statements_class main_function_declaration statements_class RCB;
block_class_statements: LCB statements_class RCB;
block_statements: LCB statements RCB;

statements_class: statement_class statements_class | statement_class | ;
statements: statement statements | statement | ;

statement_class: variable_declaration 
            | function_declaration
            | assignment_statements 
            | if_statements 
            | forin_statements 
            | methodinvocation_statement
            | call_func_statement
            | break_statements
            | continue_statements
            | return_statements;

// no function declaration
statement: variable_declaration 
            | assignment_statements 
            | if_statements 
            | forin_statements 
            | methodinvocation_statement
            | call_func_statement
            | break_statements
            | continue_statements
            | return_statements;


// EXPRESSIONS ----------------------------------------------------------------------------------
// EXPRESSIONS ----------------------------------------------------------------------------------
// EXPRESSIONS ----------------------------------------------------------------------------------
expr: expr1 (STRCONCATOP | STREQUALOP) expr1 | expr1;
expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
expr2: expr2 (ANDOP | OROP) expr3 | expr3;
expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
expr5: NOTOP expr5 | expr6;
expr6: MINUSOP expr6 | expr7;
expr7: expr7 index_operators | expr8;
expr8: expr8 (DOT | DOUBLEDOTOP) expr9 | expr9;
expr9: NEW (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_expr RB | expr10;
expr10: literal 
        | VARIABLE_IN_FUNC_IDENTIFIERS 
        | DOLLAR_IDENTIFIERS 
        | SELF 
        | call_func 
        | obj_creation 
        | expr11; 
expr11: LB expr RB;

index_operators: LSB expr RSB | LSB expr RSB index_operators;

// Expression list 
list_expr: expr COMMA list_expr | expr | ;


// --------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------

// Array literal
array_lit: ARRAY LB array_val RB;
array_val: expr COMMA array_val | expr | ;

// Literals
literal: INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit;

// List of parameters
list_parameters: param SEMICOLON list_parameters | param | ;
// param a:Int
param: identifier_list COLON variable_type;

// Identifiers list
// a,b,c
identifier_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA identifier_list | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | ;
variable_in_func_identifier_list: VARIABLE_IN_FUNC_IDENTIFIERS COMMA variable_in_func_identifier_list | VARIABLE_IN_FUNC_IDENTIFIERS | ;
// identifier_list: (identifier_list COMMA | IDENTIFIERS);

// Value list
// value_list: (literal (COMMA literal)* | expr (COMMA expr)*);
value_list: (literal | expr) COMMA value_list | (literal | expr) | ;


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

// Main
MAIN: 'main';

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
NOTEQUALOP: '!=';
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

// Identifiers
PROGRAM: 'Program';
VARIABLE_IN_FUNC_IDENTIFIERS: [_a-zA-Z] [_a-zA-Z0-9]* ;
DOLLAR_IDENTIFIERS:  DOLLAR [_a-zA-Z0-9]+; 
// IDENTIFIERS: DOLLAR_IDENTIFIERS | VARIABLE_IN_FUNC_IDENTIFIERS;
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
// fragment DECIMALPART: UNDERSCORE* '.' UNDERSCORE* ('0'+ | '0'* UNDERSCORE* DEC) UNDERSCORE*;
// fragment DECIMALPART: '.' '0'* ([1-9] [0-9]*)? ;
fragment DECIMALPART: '.' [0-9]* ;
fragment EXPONENTPART: E  (MINUSOP | PLUSOP)?   ('0'*  [1-9] [0-9]* | '0'+); 
// FLOATLIT: ((DEC | '0') (DECIMALPART EXPONENTPART? | EXPONENTPART) | (DECIMALPART EXPONENTPART)) 
FLOATLIT: ( ((DEC | '0') DECIMALPART EXPONENTPART) 
            | ((DEC | '0') DECIMALPART)
            | ((DEC | '0') EXPONENTPART)
            | (DECIMALPART EXPONENTPART))
            // | DECIMALPART)
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
// fragment ESC_UNAVAILABLE: '\\' ~[trnfb'\\] | '\\';

// Skip comments
BLOCK_COMMENT: '##' .*? '##' -> skip;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

ERROR_CHAR: . { raise ErrorToken(self.text) };

// Alphabet
fragment B: [bB];
fragment E: [eE];
fragment X: [xX];