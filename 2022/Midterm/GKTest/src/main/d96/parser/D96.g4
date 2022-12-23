// 1912683
// Nguyen Thien Bao
grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: vardecl+ EOF;
vardecl: idlist AT typ SM; 
// Khi convert sang AST:
// class ASTGeneration(XVisitor):
//	def visit<Tên rule viết hoa chữ đầu>(self, ctx: XParser.<Tên rule viết hoa chữ cái đầu>Context):
	
idlist: mem (CM mem)*;
mem: STATIC? ID;
typ: INT | FLOAT;
INT: 'int';
FLOAT: 'float';
AT: '@';
CM: ',';
STATIC: 'static';
SM: ';';
ID: [a-zA-Z]+;
WS: [ \r\n] -> skip;
