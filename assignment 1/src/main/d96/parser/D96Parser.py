# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write(".\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\5\4\24\n\4\3\5\3\5\5\5\30\n\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\5\6 \n\6\3\6\3\6\3\6\7\6%\n\6\f\6\16")
        buf.write("\6(\13\6\5\6*\n\6\3\6\3\6\3\6\2\2\7\2\4\6\b\n\2\2\2.\2")
        buf.write("\f\3\2\2\2\4\16\3\2\2\2\6\23\3\2\2\2\b\25\3\2\2\2\n\33")
        buf.write("\3\2\2\2\f\r\7>\2\2\r\3\3\2\2\2\16\17\5\b\5\2\17\20\7")
        buf.write("=\2\2\20\5\3\2\2\2\21\24\5\b\5\2\22\24\7\6\2\2\23\21\3")
        buf.write("\2\2\2\23\22\3\2\2\2\24\7\3\2\2\2\25\27\7\65\2\2\26\30")
        buf.write("\5\6\4\2\27\26\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31")
        buf.write("\32\7\66\2\2\32\t\3\2\2\2\33\34\7\22\2\2\34)\7\65\2\2")
        buf.write("\35 \7\4\2\2\36 \5\n\6\2\37\35\3\2\2\2\37\36\3\2\2\2 ")
        buf.write("!\3\2\2\2!&\7;\2\2\"%\7\4\2\2#%\5\n\6\2$\"\3\2\2\2$#\3")
        buf.write("\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'*\3\2\2\2(&\3\2")
        buf.write("\2\2)\37\3\2\2\2)*\3\2\2\2*+\3\2\2\2+,\7\66\2\2,\13\3")
        buf.write("\2\2\2\b\23\27\37$&)")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
                     "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
                     "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
                     "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", 
                     "'Destructor'", "'New'", "'By'", "'::'", "'.'", "'_'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", 
                     "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "STRINGLIT", "TYPE", "CONDITION", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "IDENTIFIERS", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "DOUBLECOLONOP", "DOUBLEDOTOP", 
                      "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                      "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", 
                      "NOTEQUAL", "GT", "LT", "GTE", "LTE", "STREQUALOP", 
                      "STRCONCATOP", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                      "COMMA", "COLON", "SEMICOLON", "BLOCK_COMMENT", "WS", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", 
                      "ID" ]

    RULE_program = 0
    RULE_body = 1
    RULE_exp = 2
    RULE_funcall = 3
    RULE_indexarraylit = 4

    ruleNames =  [ "program", "body", "exp", "funcall", "indexarraylit" ]

    EOF = Token.EOF
    STRINGLIT=1
    TYPE=2
    CONDITION=3
    INTLIT=4
    FLOATLIT=5
    BOOLLIT=6
    IDENTIFIERS=7
    BREAK=8
    CONTINUE=9
    IF=10
    ELSEIF=11
    ELSE=12
    FOREACH=13
    TRUE=14
    FALSE=15
    ARRAY=16
    IN=17
    INT=18
    FLOAT=19
    BOOLEAN=20
    STRING=21
    RETURN=22
    NULL=23
    CLASS=24
    VAL=25
    VAR=26
    CONSTRUCTOR=27
    DESTRUCTOR=28
    NEW=29
    BY=30
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
    COMMA=57
    COLON=58
    SEMICOLON=59
    BLOCK_COMMENT=60
    WS=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    ERROR_CHAR=64
    ID=65

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

        def BLOCK_COMMENT(self):
            return self.getToken(D96Parser.BLOCK_COMMENT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(D96Parser.BLOCK_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.funcall()
            self.state = 13
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exp)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(D96Parser.LB)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTLIT or _la==D96Parser.LB:
                self.state = 20
                self.exp()


            self.state = 23
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexarraylitContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndexarraylit" ):
                return visitor.visitIndexarraylit(self)
            else:
                return visitor.visitChildren(self)




    def indexarraylit(self):

        localctx = D96Parser.IndexarraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_indexarraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(D96Parser.ARRAY)
            self.state = 26
            self.match(D96Parser.LB)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.TYPE or _la==D96Parser.ARRAY:
                self.state = 29
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.TYPE]:
                    self.state = 27
                    self.match(D96Parser.TYPE)
                    pass
                elif token in [D96Parser.ARRAY]:
                    self.state = 28
                    self.indexarraylit()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 31
                self.match(D96Parser.COMMA)
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.TYPE or _la==D96Parser.ARRAY:
                    self.state = 34
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.TYPE]:
                        self.state = 32
                        self.match(D96Parser.TYPE)
                        pass
                    elif token in [D96Parser.ARRAY]:
                        self.state = 33
                        self.indexarraylit()
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 38
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 41
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





