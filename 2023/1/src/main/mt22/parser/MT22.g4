// Trịnh Duy Hưng 
// 1913652
grammar MT22;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program:   EOF ;

//   _____        _____   _____ ______ _____  
//  |  __ \ /\   |  __ \ / ____|  ____|  __ \ 
//  | |__) /  \  | |__) | (___ | |__  | |__) |
//  |  ___/ /\ \ |  _  / \___ \|  __| |  _  / 
//  | |  / ____ \| | \ \ ____) | |____| | \ \ 
//  |_| /_/    \_\_|  \_\_____/|______|_|  \_\

// Main function
// main_function: MAIN LB RB LCB statements return_nothing_statements RCB;












// // Variable declaration
// // a, b, c : int;
// variable_declaration_no_init: variable_id_list COLON atomic_types SEMICOLON;
// // a, b, c: int = 1, 2, 3;
// variable_declaration_init:  VARIABLE_IDENTIFIERS variable_declaration_init_list SEMICOLON;
// variable_declaration_init_list: COMMA VARIABLE_IDENTIFIERS variable_declaration_init_list expr COMMA
//                                 | COLON atomic_types EQUAL ;






// // Assignment statement
// assignment_statements: lhs EQUAL expr SEMICOLON;
// lhs: VARIABLE_IDENTIFIERS; 
// //         | instance_attr_access 
// //         | static_attr_access ) (index_operators | );

// // expr7 index operator
// lhs: scalar_variable | expr7; ;
// scalar_variable: VARIABLE_IN_FUNC_IDENTIFIERS 
//         | instance_attr_access 
//         | static_attr_access;


// // If statements 
// if_statements: IF LB expr RB block_statements elseif_list_statements;

// elseif_list_statements: elseif_statement  
//                         | else_statement 
//                         | ;
// elseif_statement: ELSE IF LB expr RB block_statements elseif_list_statements;
// else_statement: ELSE block_statements | ;

// // For In statement
// // forin_statements: FOR LB VARIABLE_IDENTIFIERS
// //                     IN expr DOUBLEDOTOP expr by_expr RB block_statements;


// // While statement
// while_statements: WHILE LB expr RB while_behavior;
// while_behavior: statement | block_statements;


// // Break statement
// break_statements: BREAK SEMICOLON;

// // Continue statement
// continue_statements: CONTINUE SEMICOLON;

// // Return statement
// return_expr: expr | ;
// return_statements: RETURN return_expr SEMICOLON;
// return_nothing_statements: RETURN SEMICOLON;


// // Block statements ---------------------------------------------------------------------------------

// block_statements: LCB statements RCB;
// // block_statements_in_main: LCB statements RETURN SEMICOLON RCB;

// statements: statement statements | statement | ;

// // statement_class: var_both_variable_declaration
// //                 | val_both_variable_declaration
// //                 | var_both_variable_declaration_noinnit
// //                 | val_both_variable_declaration_noinnit

// //                 | function_declaration
// //                 | constructor_dclr
// //                 | destructor_dclr ;

// statement: var_variable_declaration 
//             | val_variable_declaration_noinit 

//             | assignment_statements 
//             | if_statements 
//             | forin_statements 

//             | method_invocation_statement
//             | break_statements
//             | continue_statements
//             | return_statements ;

// // EXPRESSIONS ----------------------------------------------------------------------------------
// expr: expr1 DOUBLECOLONOP expr1 | expr1;
// expr1: expr2 (EQUALOP | NOTEQUALOP | LT | GT | LTE | GTE) expr2 | expr2;
// expr2: expr2 (ANDOP | OROP) expr3 | expr3;
// expr3: expr3 (PLUSOP | MINUSOP) expr4 | expr4;
// expr4: expr4 (MULTIPLYOP | DIVIDEOP | MODULOOP) expr5 | expr5;
// expr5: NOTOP expr5 | expr6;
// expr6: MINUSOP expr6 | expr7;
// expr7: expr7 index_operators | expr8;
// expr8: LB expr RB;

// index_operators: LSB expr RSB index_operators | LSB expr RSB ;






// // --------------------------------------------------------------------------------------------------
// // --------------------------------------------------------------------------------------------------
// // --------------------------------------------------------------------------------------------------

// // Array literal
// array_lit: ARRAY LSB array_val RSB ;
// array_val: expr COMMA array_val | expr | ;


// // Literals
// literal:  INTLIT | FLOATLIT | BOOLLIT | STRINGLIT | array_lit ;


// // Array type
// array_type: ARRAY LSB array_dimension RSB OF atomic_types;
// array_dimension:  INTLIT COMMA array_dimension | INTLIT | ;

// // Atomic types
// atomic_types: BOOLEAN | INTEGER | FLOAT | STRING;

// // Variable id list
// variable_id_list: VARIABLE_IDENTIFIERS COMMA variable_id_list | VARIABLE_IDENTIFIERS | ;


// // Special function
// read_integer_function: READ_INTEGER LB RB;
// print_integer_function: PRINT_INTEGER LB RB;
// read_float_function: READ_FLOAT LB RB;
// write_float_function: WRITE_FLOAT LB RB;
// read_boolean_function: READ_BOOLEAN LB RB;
// print_boolean_function: PRINT_BOOLEAN LB RB;
// read_string_function: READ_STRING LB RB;
// print_string_function: PRINT_STRING LB RB;
// super_function: SUPER LB RB;
// prevent_default_function: PREVENT_DEFAULT LB RB;

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
fragment DECIMALPART: '.' [0-9]+;
fragment EXPONENTPART: E (MINUSOP | PLUSOP)? ('0'* [1-9] [0-9]* | '0'+); 

FLOATLIT: ( ((DEC | '0') DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') DECIMALPART) {self.text = self.text.replace("_", "")}
            | ((DEC | '0') EXPONENTPART) {self.text = self.text.replace("_", "")}
            | (DECIMALPART EXPONENTPART) {self.text = self.text.replace("_", "")}
			) {self.text = self.text.replace("_", "")}; 

// Integer literal
fragment DEC: [1-9] (UNDERSCORE* [0-9] | [0-9])* ;

INTLIT: (DEC) {self.text = self.text.replace("_", "")} | '0';




// String literal 
// \" -> "
// self.text = str(self.text)[1:-1].replace('\\"','"')
//  self.text = str(self.text)[1:-1]
STRINGLIT: ('"') STRING_CHAR* ('"') 
{	
	self.text = str(self.text)[1:-1].replace('\"','"')
}
// if str(self.text)[-1] == '"' and str(self.text)[-2] == '\'': 
// 		if not str(self.text)[-3] == '\\':
// 			raise UncloseString(str(self.text)[1:])
	
// 	current = self.text.find('\n')
// 	if current != -1: 
// 		raise UncloseString(str(self.text[:current - 1]))

	

// 	if str(self.text)[-1] == '"':
// 		self.text = str(self.text)[0:-1].replace(str(self.text)[-1],'',1)

// 	if str(self.text)[0] == '"':
// 		self.text = str(self.text)[0:-1].replace(str(self.text)[0],'',1)


;

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
fragment STRING_CHAR:  '\\"'| ESC_CHAR | ~[\\"\n];

fragment ESC_CHAR: '\\' [trnfb'\\];

fragment ESC_UNAVAILABLE: '\\' ~[trnfb'\\] | '\\';

// Skip spaces, tabs, newlines
WS : [ \t\r\n\f\b]+ -> skip; 

// Skip comments
BLOCK_CMT: '/*' .*? '*/' -> skip;
LINE_CMT: '//' ~[\r\n]* -> skip;

ERROR_CHAR: . { raise ErrorToken(self.text) };

fragment E: [eE];