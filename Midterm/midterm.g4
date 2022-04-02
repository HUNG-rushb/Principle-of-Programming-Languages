grammar D96;

options {
	language = Python3;
}

// câu 1
fragment M: [0-9] | [1-9][0-9] | [1-9][0-9][0-9];
IP: M '.' M '.' M '.' M ;


program: var_decl* EOF;

var_decl: VARNAME EQ exp SEMI;


asso_array: ARRAY LP list_pairs RP;

list_pairs: pairs COMMA list_pairs | pairs | ;

pairs: PAIRNAME ARROW exp;

// --------------------------------------------------
indexed_array: ARRAY LP list_exp RP;

list_exp: exp COMMA list_exp | exp | ;

exp: exp1 DQUES exp1 | exp1;
exp1: exp2 (ADD | SUB) exp1 | exp2;
exp2: exp2 (MUL | DIV | MOD) exp3 | exp3;
exp3: exp3 DOT exp4 | exp4;
exp4: exp5 DSTAR exp4 | exp5;
exp5: VARNAME 
		| INTLIT 
		| FLOATLIT 
		| STRINGLIT 
		| indexed_array 
		| asso_array
		| exp6;
exp6: LP exp RP;






