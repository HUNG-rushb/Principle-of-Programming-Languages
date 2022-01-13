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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\4\3\4\5\4\26\n\4\3\5\3\5\5\5\32\n")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\5\7\'\n")
        buf.write("\7\3\7\3\7\3\7\7\7,\n\7\f\7\16\7/\13\7\5\7\61\n\7\3\7")
        buf.write("\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\64\2\16\3\2\2\2\4\20")
        buf.write("\3\2\2\2\6\25\3\2\2\2\b\27\3\2\2\2\n\35\3\2\2\2\f\"\3")
        buf.write("\2\2\2\16\17\7@\2\2\17\3\3\2\2\2\20\21\5\b\5\2\21\22\7")
        buf.write("?\2\2\22\5\3\2\2\2\23\26\5\b\5\2\24\26\7\6\2\2\25\23\3")
        buf.write("\2\2\2\25\24\3\2\2\2\26\7\3\2\2\2\27\31\7\66\2\2\30\32")
        buf.write("\5\6\4\2\31\30\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33")
        buf.write("\34\7\67\2\2\34\t\3\2\2\2\35\36\7\3\2\2\36\37\7F\2\2\37")
        buf.write(" \7\3\2\2 !\b\6\1\2!\13\3\2\2\2\"#\7\23\2\2#\60\7\66\2")
        buf.write("\2$\'\7\4\2\2%\'\5\f\7\2&$\3\2\2\2&%\3\2\2\2\'(\3\2\2")
        buf.write("\2(-\7=\2\2),\7\4\2\2*,\5\f\7\2+)\3\2\2\2+*\3\2\2\2,/")
        buf.write("\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\61\3\2\2\2/-\3\2\2\2\60")
        buf.write("&\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\7\67\2\2\63")
        buf.write("\r\3\2\2\2\b\25\31&+-\60")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'$'", "'Break'", 
                     "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
                     "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
                     "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
                     "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
                     "'New'", "'By'", "'::'", "<INVALID>", "'_'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "<INVALID>", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "TYPE", "CONDITION", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "IDENTIFIERS", "DOLLAR", "BREAK", 
                      "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
                      "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                      "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", 
                      "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "DOUBLECOLONOP", 
                      "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", "MINUSOP", 
                      "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", 
                      "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GT", "LT", 
                      "GTE", "LTE", "STREQUALOP", "STRCONCATOP", "LB", "RB", 
                      "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", 
                      "SEMICOLON", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR", "ID", "STRING_CHAR" ]

    RULE_program = 0
    RULE_body = 1
    RULE_exp = 2
    RULE_funcall = 3
    RULE_stringlit = 4
    RULE_indexarraylit = 5

    ruleNames =  [ "program", "body", "exp", "funcall", "stringlit", "indexarraylit" ]

    EOF = Token.EOF
    T__0=1
    TYPE=2
    CONDITION=3
    INTLIT=4
    FLOATLIT=5
    BOOLLIT=6
    IDENTIFIERS=7
    DOLLAR=8
    BREAK=9
    CONTINUE=10
    IF=11
    ELSEIF=12
    ELSE=13
    FOREACH=14
    TRUE=15
    FALSE=16
    ARRAY=17
    IN=18
    INT=19
    FLOAT=20
    BOOLEAN=21
    STRING=22
    RETURN=23
    NULL=24
    CLASS=25
    VAL=26
    VAR=27
    CONSTRUCTOR=28
    DESTRUCTOR=29
    NEW=30
    BY=31
    DOUBLECOLONOP=32
    DOUBLEDOTOP=33
    UNDERSCORE=34
    PLUSOP=35
    MINUSOP=36
    MULTIPLYOP=37
    DIVIDEOP=38
    MODULOOP=39
    NOTOP=40
    ANDOP=41
    OROP=42
    EQUALOP=43
    ASSIGNOP=44
    NOTEQUAL=45
    GT=46
    LT=47
    GTE=48
    LTE=49
    STREQUALOP=50
    STRCONCATOP=51
    LB=52
    RB=53
    LSB=54
    RSB=55
    LCB=56
    RCB=57
    DOT=58
    COMMA=59
    COLON=60
    SEMICOLON=61
    BLOCK_COMMENT=62
    WS=63
    UNCLOSE_STRING=64
    ILLEGAL_ESCAPE=65
    ERROR_CHAR=66
    ID=67
    STRING_CHAR=68

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
            self.state = 12
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
            self.state = 14
            self.funcall()
            self.state = 15
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
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
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
            self.state = 21
            self.match(D96Parser.LB)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTLIT or _la==D96Parser.LB:
                self.state = 22
                self.exp()


            self.state = 25
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringlitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_CHAR(self):
            return self.getToken(D96Parser.STRING_CHAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stringlit




    def stringlit(self):

        localctx = D96Parser.StringlitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_stringlit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(D96Parser.T__0)
            self.state = 28
            self.match(D96Parser.STRING_CHAR)

            self.state = 29
            self.match(D96Parser.T__0)

            	self.text = str(self.text)[1:-1].replace('\"','')

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexarraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def TYPE(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.TYPE)
            else:
                return self.getToken(D96Parser.TYPE, i)

        def indexarraylit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.IndexarraylitContext)
            else:
                return self.getTypedRuleContext(D96Parser.IndexarraylitContext,i)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_indexarraylit




    def indexarraylit(self):

        localctx = D96Parser.IndexarraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_indexarraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(D96Parser.ARRAY)
            self.state = 33
            self.match(D96Parser.LB)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.TYPE or _la==D96Parser.ARRAY:
                self.state = 36
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TYPE]:
                    self.state = 34
                    self.match(D96Parser.TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 35
                    self.indexarraylit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 38
                self.match(D96Parser.COMMA)
                self.state = 43
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.TYPE or _la==D96Parser.ARRAY:
                    self.state = 41
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.TYPE]:
                        self.state = 39
                        self.match(D96Parser.TYPE)
                        pass
                    elif token in [D96Parser.ARRAY]:
                        self.state = 40
                        self.indexarraylit()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 45
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 48
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





