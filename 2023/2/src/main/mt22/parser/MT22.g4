// Trịnh Duy Hưng 
// 1913652
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: global_statements EOF ;

//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\

// Main function
// main_function: MAIN COLON FUNCTION (all_type | VOID) LB RB block_statements;
main_function: MAIN COLON FUNCTION (all_type | VOID) LB param_list RB (inherit_function | ) block_statements;

// Function declaration
function_declaration: VARIABLE_IDENTIFIERS COLON FUNCTION (all_type | VOID) LB param_list RB (inherit_function | ) block_statements;

inherit_function: INHERIT VARIABLE_IDENTIFIERS;


// List of parameters
param_list: param_list_no_empty | ;
param_list_no_empty: param COMMA param_list_no_empty | param;
param: (INHERIT | ) (OUT | ) VARIABLE_IDENTIFIERS COLON all_type;

// Variable declaration
// a, b, c : int;
variable_declaration_no_init: variable_id_list COLON all_type_no_void SEMICOLON;
// a, b, c: int = 1, 2, 3;
variable_declaration_init:  VARIABLE_IDENTIFIERS variable_declaration_init_list expr SEMICOLON;
variable_declaration_init_list: COMMA VARIABLE_IDENTIFIERS variable_declaration_init_list expr COMMA
                                | COLON all_type_no_void EQUAL ;

// Assignment statement
assignment_statements: lhs EQUAL expr SEMICOLON;
lhs: VARIABLE_IDENTIFIERS | VARIABLE_IDENTIFIERS LSB expr_list_no_empty RSB; 


// Method invocation statement
method_invocation_statements: (VARIABLE_IDENTIFIERS LB expr_list RB 
                            | read_integer_function
                            | print_integer_function
                            | read_float_function
                            | write_float_function
                            | read_boolean_function
                            | print_boolean_function
                            | read_string_function
                            | print_string_function
                            | super_function
                            | prevent_default_function) SEMICOLON;

// Special function
read_integer_function: READ_INTEGER LB expr_list RB;
print_integer_function: PRINT_INTEGER LB expr_list RB;
read_float_function: READ_FLOAT LB expr_list RB;
write_float_function: WRITE_FLOAT LB expr_list RB;
read_boolean_function: READ_BOOLEAN LB expr_list RB;
print_boolean_function: PRINT_BOOLEAN LB expr_list RB;
read_string_function: READ_STRING LB expr_list RB;
print_string_function: PRINT_STRING LB expr_list RB;
super_function: SUPER LB expr_list RB;
prevent_default_function: PREVENT_DEFAULT LB expr_list RB;


// If statements 
if_statements: IF LB expr RB (block_statements | statement) elseif_list_statements ;
elseif_list_statements: elseif_statement | else_statement | ;
elseif_statement: ELSE IF LB expr RB (block_statements | statement) elseif_list_statements;
else_statement: ELSE (block_statements | statement) | ;

// For In statement
for_statements: FOR LB VARIABLE_IDENTIFIERS EQUAL expr COMMA expr COMMA expr RB (block_statements_no_func_decl | statement_no_var_no_func);

// While statement
while_statements: WHILE LB expr RB (block_statements_no_func_decl | statement_no_var_no_func);

// Do - While statement
do_while_statements: DO block_statements_no_func_decl WHILE LB expr RB SEMICOLON;

// Break statement
break_statements: BREAK SEMICOLON;

// Continue statement
continue_statements: CONTINUE SEMICOLON;

// Return statement
return_expr: expr | ;
return_statements: RETURN return_expr SEMICOLON;
return_nothing_statements: RETURN SEMICOLON;

// **************************************************
// **************************************************
// **************************************************
// Statements 
global_statements: global_statement global_statements | global_statement ;
global_statement: variable_declaration_no_init 
                | variable_declaration_init 
                | function_declaration
                | main_function;

block_statements: LCB statements RCB;
block_statements_no_func_decl: LCB statements_no_func_decl RCB;


statements: statement statements | statement | ;
statement:  variable_declaration_no_init 
            | variable_declaration_init 
            | function_declaration 
            | assignment_statements 
            | if_statements 
            | for_statements 
            | while_statements
            | do_while_statements
            | method_invocation_statements
            | return_statements 
            | return_nothing_statements
            | in_loop_statement
            | block_statements;

statements_no_func_decl: statement_no_func_decl statements_no_func_decl | statement_no_func_decl | ;
statement_no_func_decl:  variable_declaration_no_init 
                        | variable_declaration_init 
                        | assignment_statements 
                        | if_statements 
                        | for_statements 
                        | while_statements
                        | do_while_statements
                        | method_invocation_statements
                        | return_statements 
                        | return_nothing_statements
                        | in_loop_statement
                        | block_statements_no_func_decl;

statements_no_var_no_func: statement_no_var_no_func statements_no_var_no_func | statement_no_var_no_func | ;
statement_no_var_no_func: assignment_statements 
                        | if_statements 
                        | for_statements 
                        | while_statements
                        | do_while_statements
                        | method_invocation_statements
                        | return_statements 
                        | return_nothing_statements
                        | in_loop_statement
                        | block_statements;


// block_in_loop_statements: LCB in_loop_statements RCB;
// in_loop_statements: in_loop_statement in_loop_statements | in_loop_statement | ;
in_loop_statement: break_statements | continue_statements;

// EXPRESSIONS ----------------------------------------------------------------------------------
expr_list: expr_list_no_empty | ;
expr_list_no_empty: expr COMMA expr_list_no_empty | expr;

expr: expr1 DOUBLECOLONOP expr1 | expr1;
expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
expr2: expr2 (ANDOP | OROP) expr3 | expr3;
expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
expr5: NOTOP expr5 | expr6;
expr6: MINUSOP expr6 | expr7;
// a[1]
expr7: expr7 LSB expr_list_no_empty RSB | expr8;
// foo()
expr8: VARIABLE_IDENTIFIERS LB expr_list RB | expr9;
expr9: literal | VARIABLE_IDENTIFIERS | array_init | LCB RCB | expr10; 
expr10: LB expr RB;



// --------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------

// Array init
array_init: LCB expr_list RCB;

// Array literal
array_lit: ARRAY LSB expr_list RSB ;

// Literals
literal:  INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit ;

all_type: atomic_types | array_type | AUTO | VOID;
all_type_no_void: atomic_types | array_type | AUTO ;

// Array type
array_type: ARRAY LSB integer_list_no_empty RSB OF atomic_types;
integer_list_no_empty: INTLIT COMMA integer_list_no_empty | INTLIT;

// Atomic types
atomic_types: BOOLEAN | INTEGER | FLOAT | STRING;

// Variable id list
variable_id_list: VARIABLE_IDENTIFIERS COMMA variable_id_list | VARIABLE_IDENTIFIERS;


//   _      ________   ________ _____  
//  | |    |  ____\ \ / /  ____|  __ \ 
//  | |    | |__   \ V /| |__  | |__) |
//  | |    |  __|   > < |  __| |  _  / 
//  | |____| |____ / . \| |____| | \ \ 
//  |______|______/_/ \_\______|_|  \_\                    

MAIN: 'main';
FUNCTION: 'function';

// Special function
READ_INTEGER: 'readInteger';
PRINT_INTEGER: 'printInteger';
READ_FLOAT: 'readFloat';
WRITE_FLOAT: 'writeFloat';
READ_BOOLEAN: 'readBoolean';
PRINT_BOOLEAN: 'printBoolean';
READ_STRING: 'readString';
PRINT_STRING: 'printString';
SUPER: 'super';
PREVENT_DEFAULT: 'preventDefault';

// Keywords
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
ARRAY:'array';

// Boolean
// TRUE: 'true';
// FALSE: 'false';

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

// Boolean literal 
BOOLLIT: 'true' | 'false';


// Variable indentifiers
VARIABLE_IDENTIFIERS: [_a-zA-Z] [_a-zA-Z0-9]*;





// Float literal 
fragment DECIMALPART: '.' [0-9]*;
fragment EXPONENTPART: E (MINUSOP | PLUSOP)? ('0'* [1-9] [0-9]* | '0'+); 

FLOATLIT: ( ((DEC | '0') DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') DECIMALPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') EXPONENTPART) {self.text = self.text.replace("_", "")}
            | (DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")}
			) {self.text = self.text.replace("_", "")}; 

// Integer literal
fragment DEC: [1-9] (UNDERSCORE [0-9] | [0-9])* ;

INTLIT: (DEC) {self.text = self.text.replace("_", "")} | '0';

// String literal 
// \" -> "
STRINGLIT: ('"') STRING_CHAR* ('"') 
{	
	self.text = str(self.text)[1:-1].replace('\"','"')
};

UNCLOSE_STRING: '"' STRING_CHAR* 
{
	current = str(self.text)
	raise UncloseString(current[1:])
} 
| '"' STRING_CHAR* ('\n' | EOF)
{
	Quynh = str(self.text)
	index = Quynh.find('\n')
	if index != -1:
		raise UncloseString(Quynh[1:index - 1])
	self.text = Quynh
	raise UncloseString(self.text[1:])
};


ILLEGAL_ESCAPE: '"' STRING_CHAR* ESC_UNAVAILABLE
{
	current = str(self.text)
	raise IllegalEscape(current[1:])
};

// String char except special character 
fragment STRING_CHAR:  '\\"'| ESC_CHAR | ~[\\"\n\f\r];

fragment ESC_CHAR: '\\' [trnfb'\\];

fragment ESC_UNAVAILABLE: '\\' ~[trnfb'\\] | '\\';

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

// Skip comments
BLOCK_CMT: '/*' .*? '*/' -> skip;
LINE_CMT: '//' ~[\r\n]* -> skip;

ERROR_CHAR: . { raise ErrorToken(self.text) };

fragment E: [eE];