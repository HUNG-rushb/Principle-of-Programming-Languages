# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3;")
        buf.write("\13\4\2\t\2\4\3\t\3\3\2\3\2\3\3\3\3\3\3\2\2\4\2\4\2\3")
        buf.write("\3\2\62\65\2\b\2\6\3\2\2\2\4\b\3\2\2\2\6\7\7\2\2\3\7\3")
        buf.write("\3\2\2\2\b\t\t\2\2\2\t\5\3\2\2\2\2")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'auto'", "'break'", "'do'", 
                     "'else'", "'for'", "'if'", "'return'", "'while'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'true'", "'false'", 
                     "'boolean'", "'float'", "'integer'", "'string'", "'void'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'::'", "'>='", "'<='", "'='", "'>'", 
                     "'<'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
                     "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "AUTO", "BREAK", "DO", "ELSE", 
                      "FOR", "IF", "RETURN", "WHILE", "OUT", "CONTINUE", 
                      "OF", "INHERIT", "TRUE", "FALSE", "BOOLEAN", "FLOAT", 
                      "INTEGER", "STRING", "VOID", "PLUSOP", "MINUSOP", 
                      "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", 
                      "OROP", "EQUALOP", "NOTEQUALOP", "DOUBLECOLONOP", 
                      "GTE", "LTE", "EQUAL", "GT", "LT", "LB", "RB", "LSB", 
                      "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "VARIABLE_IDENTIFIERS", "BOOLLIT", "FLOATLIT", "INTLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
                      "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_literal = 1

    ruleNames =  [ "program", "literal" ]

    EOF = Token.EOF
    FUNCTION=1
    AUTO=2
    BREAK=3
    DO=4
    ELSE=5
    FOR=6
    IF=7
    RETURN=8
    WHILE=9
    OUT=10
    CONTINUE=11
    OF=12
    INHERIT=13
    TRUE=14
    FALSE=15
    BOOLEAN=16
    FLOAT=17
    INTEGER=18
    STRING=19
    VOID=20
    PLUSOP=21
    MINUSOP=22
    MULTIPLYOP=23
    DIVIDEOP=24
    MODULOOP=25
    NOTOP=26
    ANDOP=27
    OROP=28
    EQUALOP=29
    NOTEQUALOP=30
    DOUBLECOLONOP=31
    GTE=32
    LTE=33
    EQUAL=34
    GT=35
    LT=36
    LB=37
    RB=38
    LSB=39
    RSB=40
    LCB=41
    RCB=42
    DOT=43
    COMMA=44
    COLON=45
    SEMICOLON=46
    VARIABLE_IDENTIFIERS=47
    BOOLLIT=48
    FLOATLIT=49
    INTLIT=50
    STRINGLIT=51
    UNCLOSE_STRING=52
    ILLEGAL_ESCAPE=53
    WS=54
    BLOCK_CMT=55
    LINE_CMT=56
    ERROR_CHAR=57

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLLIT) | (1 << MT22Parser.FLOATLIT) | (1 << MT22Parser.INTLIT) | (1 << MT22Parser.STRINGLIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





