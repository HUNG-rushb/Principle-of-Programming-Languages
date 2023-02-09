grammar BKOOL;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;

// ID: [a-z][a-z\d]* ;

// fragment COM: [0-9] | [1-9][0-9] | [1-9][0-9][0-9];
// ID:  COM'.'COM'.'COM'.'COM;

fragment DIGIT: [0-9];
ID: [0-9]+(('.'DIGIT+)|'e'('+'|'-'|)DIGIT+|'.'DIGIT+'e'('+'|'-'|)DIGIT+);

SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines



ERROR_CHAR: . {raise ErrorToken(self.text)};
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;