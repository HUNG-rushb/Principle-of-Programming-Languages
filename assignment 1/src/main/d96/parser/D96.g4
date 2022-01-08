// Trinh Duy Hung
// 1913652

grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: mptype 'main' LB RB LP body? RP EOF;

mptype: INTTYPE | VOIDTYPE;

body: funcall SEMI;

exp: funcall | INTLIT;

funcall: ID LB exp? RB;

INTTYPE: 'int';

VOIDTYPE: 'void';

// fragment LOWERCASE_LETTER   :  [a-z] ;
// fragment DIGIT              :  [0-9] ;
// fragment SIGN               :  [+-]? ;
// fragment SCIENTIFIC         :  [e](SIGN)(DIGIT)+ ;
// fragment DECIMAL_POINT      :  [.](DIGIT)+ ;

// REAL               :  SIGN(DIGIT)+(DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC) ;
// INT                :  SIGN(DIGIT)+ ;
// ID                 :  LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)* ;
// STRING             :  ['][^']+['] ;

ID: [a-zA-Z]+;

INTLIT: [0-9]+;

LB: '(';

RB: ')';

LP: '{';

RP: '}';

SEMI: ';';

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;


// Alphabet
fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];