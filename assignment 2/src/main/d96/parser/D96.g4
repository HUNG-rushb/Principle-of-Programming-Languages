// 1913652
// Trịnh Duy Hưng

grammar D96;

@lexer::header {
from lexererr import *
import inspect
}

// @lexer::members {
// def emit(self):
//     tk = self.type
//     result = super().emit() # result mean for input

//     # delete later
//     print('--------------------------------------------------------------------------------')
//     attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
//     user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
//     for i in user_defined_attr:
//         if tk == i[1]:
//             print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
//     print('--------------------------------------------------------------------------------')
//     return result
// }

options {
	language = Python3;
}


// program: class_declarations class_main_program_declarations class_declarations EOF;
program: class_declarations EOF;

//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\

// Class declaration

// class_main_program_declarations: CLASS PROGRAM program_block_class_statements;
// class_declarations: class_declaration class_declarations | class_declaration | ;
class_declarations: class_declaration class_declarations | class_declaration ;
class_declaration: CLASS VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance block_class_statements;
class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;
// class_inheritance: COLON VARIABLE_IN_FUNC_IDENTIFIERS class_inheritance | COLON VARIABLE_IN_FUNC_IDENTIFIERS | ;

// Constructor Destructor
constructor_dclr: CONSTRUCTOR LB list_parameters RB block_statements;
destructor_dclr: DESTRUCTOR LB RB block_statements;

// Method declaration
method_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;

// STATEMENTS ------------------------------------------------------------------------------

// Variable declaration
// Var
var_variable_declaration: VAR (var_declare_initiate_list | var_no_value_assign_declare_list) SEMICOLON;
var_no_value_assign_declare_list: var_no_value_assign_declare var_no_value_assign_declare_list| var_no_value_assign_declare;
var_no_value_assign_declare: VARIABLE_IN_FUNC_IDENTIFIERS COMMA 
                                | VARIABLE_IN_FUNC_IDENTIFIERS 
                                | COLON variable_type;

var_declare_initiate_list: VARIABLE_IN_FUNC_IDENTIFIERS var_type_and_assign expr
                                | variable_in_func_identifier_list COLON variable_type;
var_type_and_assign: COMMA VARIABLE_IN_FUNC_IDENTIFIERS var_type_and_assign expr COMMA
                        | COLON variable_type ASSIGNOP;

// Val
val_variable_declaration: VAL (val_declare_initiate_list | val_no_value_assign_declare_list) SEMICOLON;
val_no_value_assign_declare_list: val_no_value_assign_declare val_no_value_assign_declare_list| val_no_value_assign_declare;
val_no_value_assign_declare: (VARIABLE_IN_FUNC_IDENTIFIERS COMMA 
                                        | VARIABLE_IN_FUNC_IDENTIFIERS 
                                        | COLON variable_type);

val_declare_initiate_list: VARIABLE_IN_FUNC_IDENTIFIERS val_type_and_assign expr
                                | variable_in_func_identifier_list COLON variable_type;
val_type_and_assign: COMMA VARIABLE_IN_FUNC_IDENTIFIERS val_type_and_assign expr COMMA
                        | COLON variable_type ASSIGNOP;

// Dollar declaration
// dollar_variable_declaration: (VAR | VAL) dollar_declare_initiate_in_func_list SEMICOLON;
// dollar_declare_initiate_in_func_list: DOLLAR_IDENTIFIERS dollar_type_and_assign_in_func expr
//                                 | variable_in_func_identifier_list COLON variable_type;
// dollar_type_and_assign_in_func: COMMA DOLLAR_IDENTIFIERS dollar_type_and_assign_in_func expr COMMA
//                         | COLON variable_type ASSIGNOP;

// Both declaration
// Var
var_both_variable_declaration: VAR (var_both_declare_initiate_list | var_both_no_value_assign_declare_list) SEMICOLON;
var_both_no_value_assign_declare_list: var_both_no_value_assign_declare var_both_no_value_assign_declare_list| var_both_no_value_assign_declare;
var_both_no_value_assign_declare: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | COLON variable_type;

var_both_declare_initiate_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) var_both_type_and_assign expr
                                | variable_in_func_identifier_list COLON variable_type;
var_both_type_and_assign: COMMA (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) var_both_type_and_assign expr COMMA
                        | COLON variable_type ASSIGNOP;

// Val
val_both_variable_declaration: VAL (val_both_declare_initiate_list | val_both_no_value_assign_declare_list) SEMICOLON;
val_both_no_value_assign_declare_list: val_both_no_value_assign_declare val_both_no_value_assign_declare_list| val_both_no_value_assign_declare;
val_both_no_value_assign_declare: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | COLON variable_type;

val_both_declare_initiate_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) val_both_type_and_assign expr
                                | variable_in_func_identifier_list COLON variable_type;
val_both_type_and_assign: COMMA (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) val_both_type_and_assign expr COMMA
                        | COLON variable_type ASSIGNOP;



















// Function declaration
function_declaration: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) LB list_parameters RB block_statements;
// main_function_declaration: MAIN LB RB block_statements_in_main;

call_func_statement: call_func_header call_func_attr_list call_func_end SEMICOLON;
call_func: call_func_header call_func_attr_list call_func_end;

call_func_header: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) (index_operators | ) (DOUBLECOLONOP DOLLAR_IDENTIFIERS | );

call_func_attr_list: call_func_attr call_func_attr_list | call_func_attr | ;
call_func_attr: DOT (VARIABLE_IN_FUNC_IDENTIFIERS | VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB);                 
             
call_func_end: DOT VARIABLE_IN_FUNC_IDENTIFIERS LB value_list RB;

// Assignment statement
assignment_statements: lhs ASSIGNOP expr SEMICOLON;
lhs: (VARIABLE_IN_FUNC_IDENTIFIERS 
        | instance_attr_access 
        | static_attr_access 
        ) (index_operators | );






// If statements 
if_condition: LB expr RB;
// if_statements: IF if_condition block_statements (elseif_list_statements else_statement | elseif_list_statements | else_statement | );
if_statements: IF if_condition block_statements elseif_list_statements;

// elseif_list_statements: elseif_statement elseif_list_statements |  elseif_statement;
elseif_list_statements: elseif_statement elseif_list_statements |  elseif_statement | else_statement_or_none;
elseif_statement: ELSEIF if_condition block_statements else_statement_or_none;
else_statement_or_none: else_statement | ;
else_statement: ELSE block_statements;






// For In statement
by_expr: (BY expr) | ;
forin_statements: FOREACH LB (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) 
                    IN expr DOUBLEDOTOP expr by_expr RB block_statements;

// Member access
instance_attr_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS;
instance_method_access: expr DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;

static_attr_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS;
static_method_access: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;

// Method invocation statement
method_invocation: instance_method_access | static_method_access;
method_invocation_statement: method_invocation SEMICOLON;

// Break statement
break_statements: BREAK SEMICOLON;

// Continue statement
continue_statements: CONTINUE SEMICOLON;

// Return statement
return_expr: expr | ;
return_statements: RETURN return_expr SEMICOLON;


// Block statements ---------------------------------------------------------------------------------

// program_block_class_statements: LCB statements_class main_function_declaration statements_class RCB;
block_class_statements: LCB statements_class RCB;
block_statements: LCB statements RCB;
// block_statements_in_main: LCB statements RETURN SEMICOLON RCB;

statements_class: statement_class statements_class | statement_class | ;
statements: statement statements | statement | ;

statement_class: var_both_variable_declaration
                | val_both_variable_declaration
                | function_declaration
                | constructor_dclr
                | destructor_dclr ;

// no function declaration
// no $
statement: var_variable_declaration 
            | val_variable_declaration 
            | assignment_statements 
            | if_statements 
            | forin_statements 
            | call_func_statement
            | method_invocation_statement
            | break_statements
            | continue_statements
            | return_statements ;

// EXPRESSIONS ----------------------------------------------------------------------------------

// a.b[1]              a.b()[1]           a.b[1]            a.b()[1].b()[1]
// a::b[1]             a::b()[1]          a::b[1]           a::b()[1]::b()[1]  
// Ưu tiên gọi access trước

expr: expr1 (STRCONCATOP | STREQUALOP) expr1 | expr1;
expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
expr2: expr2 (ANDOP | OROP) expr3 | expr3;
expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
expr5: NOTOP expr5 | expr6;
expr6: MINUSOP expr6 | expr7;
expr7: expr7 index_operators | expr8;
expr8: expr8 instance_accesses | expr9;
expr9: VARIABLE_IN_FUNC_IDENTIFIERS static_accesses | expr10;

expr10: NEW expr LB list_expr RB | expr11;
expr11: literal 
        | VARIABLE_IN_FUNC_IDENTIFIERS 
        | SELF 
        | expr12; 
expr12: LB expr RB;

// a[1][2]
index_operators: index_operators LSB expr RSB  | LSB expr RSB ;
index_expr: index | index index_operators;
index: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)
        | (expr instance_attr_access (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS)) | ;

// Instance, Static accesses
instance_accesses: instance_access instance_accesses | instance_access;
instance_access:  DOT VARIABLE_IN_FUNC_IDENTIFIERS
                | DOT VARIABLE_IN_FUNC_IDENTIFIERS LB list_expr RB;

static_accesses: static_access static_accesses | static_access;
static_access:  DOUBLECOLONOP DOLLAR_IDENTIFIERS
                | DOUBLECOLONOP DOLLAR_IDENTIFIERS LB list_expr RB;

// Expression list 
list_expr: expr COMMA list_expr | expr | ;

// --------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------
// --------------------------------------------------------------------------------------------------

// Array literal
array_lit: ARRAY LB array_val RB;
array_val: expr COMMA array_val | expr | ;

// Literals
literal: INTLIT_IN_ARRAY | INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit;

// List of parameters
list_parameters: param SEMICOLON list_parameters | param | ;
// param a:Int
param: identifier_list COLON variable_type;

// Identifiers list
// a,b,c
identifier_list: (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) COMMA identifier_list 
                | (VARIABLE_IN_FUNC_IDENTIFIERS | DOLLAR_IDENTIFIERS) | ;
variable_in_func_identifier_list: VARIABLE_IN_FUNC_IDENTIFIERS COMMA variable_in_func_identifier_list 
                                        | VARIABLE_IN_FUNC_IDENTIFIERS | ;
// identifier_list: (identifier_list COMMA | IDENTIFIERS);

// Value list
// value_list: (literal (COMMA literal)* | expr (COMMA expr)*);
value_list: (literal | expr) COMMA value_list | (literal | expr) | ;


// Array type
array_type: ARRAY LSB array_element_type COMMA INTLIT_IN_ARRAY RSB;
array_element_type: array_type | INT | FLOAT | BOOLEAN | STRING;
// array_element_type: array_type | INT | FLOAT | BOOLEAN | STRING | VARIABLE_IN_FUNC_IDENTIFIERS;

// Primitive type
primitive_type: BOOLEAN | INT | FLOAT | STRING;

// Variable type
variable_type: primitive_type | array_type | VARIABLE_IN_FUNC_IDENTIFIERS;



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
// PROGRAM: 'Program';
// MAIN: 'main';
VARIABLE_IN_FUNC_IDENTIFIERS: [_a-zA-Z] [_a-zA-Z0-9]*;
DOLLAR_IDENTIFIERS:  DOLLAR [_a-zA-Z0-9]+; 
fragment DOLLAR: '$';

// String literal 
// '" -> "
// self.text = str(self.text)[1:-1].replace('\'"','\"')
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

// Float literal 
fragment DECIMALPART: '.' [0-9]*;
fragment EXPONENTPART: E (MINUSOP | PLUSOP)? ('0'* [1-9] [0-9]* | '0'+); 

FLOATLIT: ( ((DEC | '0') DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') DECIMALPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') EXPONENTPART) {self.text = self.text.replace("_", "")}
            | (DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")})
            // | DECIMALPART)
{self.text = self.text.replace("_", "")};

// Interher literal
fragment DEC: [1-9] (UNDERSCORE [0-9] | [0-9])*;

fragment HEX: '0' X ([1-9A-F]+ ((UNDERSCORE [0-9A-F]+)* | [0-9A-F]*) | '0');

fragment OCT: '0' ([1-7]+ ((UNDERSCORE [0-7]+)* | [0-7]* ) | '0'); 

fragment BIN: '0' B ('1'+ ((UNDERSCORE [01]+)* | [01]*)| '0');

fragment HEX_ARRAY_SIZE: '0' X ([1-9A-F]+ ((UNDERSCORE [0-9A-F]+)* | [0-9A-F]*));
fragment OCT_ARRAY_SIZE: '0' ([1-7]+ ((UNDERSCORE [0-7]+)* | [0-7])); 
fragment BIN_ARRAY_SIZE: '0' B ('1'+ ((UNDERSCORE [01]+)* | [01]*));

INTLIT_IN_ARRAY: (DEC
                | HEX_ARRAY_SIZE 
                | OCT_ARRAY_SIZE 
                | BIN_ARRAY_SIZE) {self.text = self.text.replace("_", "")};

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

// Skip comments
BLOCK_COMMENT: '##' .*? '##' -> skip;

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

ERROR_CHAR: . { raise ErrorToken(self.text) };

// Alphabet
fragment B: [bB];
fragment E: [eE];
fragment X: [xX];