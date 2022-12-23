grammar BKOOL;

@lexer::header {
from lexererr import *
}

options{
	language=Python3;
}

program: (vardclr | funcdclr)+ EOF;// write your rule here;


//And some other rules for variable declaration, function declaration and other rules

vardclr: typ (ID (COM ID)*) SEMI ;

funcdclr: typ ID paramdclr body;

paramdclr: LB (param (SEMI param)*)? RB;

param:typ (ID (COM ID)*);

typ: INT | FLOAT;

COM:',';

body: 'body';

INT:'int';
FLOAT: 'float';

ID: [a-zA-Z]+; // includes a sequence of alphabetic characters.;

WS: [ \t\r\n] -> skip;

ERROR_CHAR: . {raise ErrorToken(self.text)};





// mptype: INTTYPE | VOIDTYPE ;

// body: funcall SEMI;

exp: funcall | INTLIT ;

funcall: ID LB exp? RB ;

// INTTYPE: 'int' ;

// VOIDTYPE: 'void'  ;

// ID: [a-zA-Z]+ ;

INTLIT: [0-9]+;

LB: '(' ;

RB: ')' ;

LP: '{';

RP: '}';

SEMI: ';' ;

// WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines


// ERROR_CHAR: .;
// UNCLOSE_STRING: .;
// ILLEGAL_ESCAPE: .;