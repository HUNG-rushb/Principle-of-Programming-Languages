# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3G")
        buf.write("\32\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\4\3\4\5\4\22\n\4\3\5\3\5\5\5\26\n\5\3\5\3\5\3\5\2")
        buf.write("\2\6\2\4\6\b\2\2\2\27\2\n\3\2\2\2\4\f\3\2\2\2\6\21\3\2")
        buf.write("\2\2\b\23\3\2\2\2\n\13\7@\2\2\13\3\3\2\2\2\f\r\5\b\5\2")
        buf.write("\r\16\7>\2\2\16\5\3\2\2\2\17\22\5\b\5\2\20\22\7\3\2\2")
        buf.write("\21\17\3\2\2\2\21\20\3\2\2\2\22\7\3\2\2\2\23\25\7\65\2")
        buf.write("\2\24\26\5\6\4\2\25\24\3\2\2\2\25\26\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\30\7\66\2\2\30\t\3\2\2\2\4\21\25")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'::'", "<INVALID>", "'_'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "<INVALID>", "','", "':'", "';'", "'$'" ]

    symbolicNames = [ "<INVALID>", "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", 
                      "INDEXEDARRAYLIT", "MULTIDIMENSIONALARRAYLIT", "BREAK", 
                      "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                      "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", 
                      "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                      "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                      "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                      "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", 
                      "GT", "LT", "GTE", "LTE", "STREQUALOP", "STRCONCATOP", 
                      "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                      "COLON", "SEMICOLON", "DOLLARD", "BLOCK_COMMENT", 
                      "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_SEQ", 
                      "ESC_ILLEGAL", "ERROR_CHAR", "ID" ]

    RULE_program = 0
    RULE_body = 1
    RULE_exp = 2
    RULE_funcall = 3

    ruleNames =  [ "program", "body", "exp", "funcall" ]

    EOF = Token.EOF
    INTLIT=1
    FLOATLIT=2
    BOOLLIT=3
    STRINGLIT=4
    INDEXEDARRAYLIT=5
    MULTIDIMENSIONALARRAYLIT=6
    BREAK=7
    CONTINUE=8
    IF=9
    ELSEIF=10
    ELSE=11
    FOREACH=12
    TRUE=13
    FALSE=14
    ARRAY=15
    IN=16
    INT=17
    FLOAT=18
    BOOLEAN=19
    STRING=20
    RETURN=21
    NULL=22
    CLASS=23
    VAL=24
    VAR=25
    CONSTRUCTOR=26
    DESTRUCTOR=27
    NEW=28
    BY=29
    SELF=30
    DOUBLECOLONOP=31
    DOUBLEDOTOP=32
    UNDERSCORE=33
    PLUSOP=34
    MINUSOP=35
    MULTIPLYOP=36
    DIVIDEOP=37
    MODULOOP=38
    NOTOP=39
    ANDOP=40
    OROP=41
    EQUALOP=42
    ASSIGNOP=43
    NOTEQUAL=44
    GT=45
    LT=46
    GTE=47
    LTE=48
    STREQUALOP=49
    STRCONCATOP=50
    LB=51
    RB=52
    LSB=53
    RSB=54
    LCB=55
    RCB=56
    DOT=57
    COMMA=58
    COLON=59
    SEMICOLON=60
    DOLLARD=61
    BLOCK_COMMENT=62
    WS=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ESC_SEQ=66
    ESC_ILLEGAL=67
    ERROR_CHAR=68
    ID=69

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BLOCK_COMMENT(self):
            return self.getToken(D96Parser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(D96Parser.BLOCK_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.funcall()
            self.state = 11
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(D96Parser.INTLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(D96Parser.LB)
            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTLIT or _la==D96Parser.LB:
                self.state = 18
                self.exp()


            self.state = 21
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





