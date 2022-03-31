grammar D96;

options {
	language = Python3;
}

// câu 1
fragment M: [0-9] | [1-9][0-9] | [1-9][0-9][0-9];
IP: M '.' M '.' M '.' M ;


program: var_decl* EOF;

var_decl: VARNAME EQ exp SEMI;

