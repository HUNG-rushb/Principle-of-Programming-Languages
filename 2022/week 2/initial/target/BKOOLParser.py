# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\6\2\27\n\2\r\2\16\2\30\3")
        buf.write("\2\3\2\3\3\3\3\3\3\3\3\7\3!\n\3\f\3\16\3$\13\3\3\3\3\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\61\n\5\f\5\16")
        buf.write("\5\64\13\5\5\5\66\n\5\3\5\3\5\3\6\3\6\3\6\3\6\7\6>\n\6")
        buf.write("\f\6\16\6A\13\6\3\7\3\7\3\b\3\b\3\t\3\t\5\tI\n\t\3\n\3")
        buf.write("\n\3\n\5\nN\n\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22")
        buf.write("\2\3\3\2\5\6\2P\2\26\3\2\2\2\4\34\3\2\2\2\6\'\3\2\2\2")
        buf.write("\b,\3\2\2\2\n9\3\2\2\2\fB\3\2\2\2\16D\3\2\2\2\20H\3\2")
        buf.write("\2\2\22J\3\2\2\2\24\27\5\4\3\2\25\27\5\6\4\2\26\24\3\2")
        buf.write("\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\32\3\2\2\2\32\33\7\2\2\3\33\3\3\2\2\2\34\35")
        buf.write("\5\f\7\2\35\"\7\7\2\2\36\37\7\4\2\2\37!\7\7\2\2 \36\3")
        buf.write("\2\2\2!$\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#%\3\2\2\2$\"\3")
        buf.write("\2\2\2%&\7\17\2\2&\5\3\2\2\2\'(\5\f\7\2()\7\7\2\2)*\5")
        buf.write("\b\5\2*+\5\16\b\2+\7\3\2\2\2,\65\7\13\2\2-\62\5\n\6\2")
        buf.write("./\7\17\2\2/\61\5\n\6\2\60.\3\2\2\2\61\64\3\2\2\2\62\60")
        buf.write("\3\2\2\2\62\63\3\2\2\2\63\66\3\2\2\2\64\62\3\2\2\2\65")
        buf.write("-\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\678\7\f\2\28\t\3")
        buf.write("\2\2\29:\5\f\7\2:?\7\7\2\2;<\7\4\2\2<>\7\7\2\2=;\3\2\2")
        buf.write("\2>A\3\2\2\2?=\3\2\2\2?@\3\2\2\2@\13\3\2\2\2A?\3\2\2\2")
        buf.write("BC\t\2\2\2C\r\3\2\2\2DE\7\3\2\2E\17\3\2\2\2FI\5\22\n\2")
        buf.write("GI\7\n\2\2HF\3\2\2\2HG\3\2\2\2I\21\3\2\2\2JK\7\7\2\2K")
        buf.write("M\7\13\2\2LN\5\20\t\2ML\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP")
        buf.write("\7\f\2\2P\23\3\2\2\2\n\26\30\"\62\65?HM")
        return buf.getvalue()


class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'body'", "','", "'int'", "'float'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "COM", "INT", "FLOAT", "ID", 
                      "WS", "ERROR_CHAR", "INTLIT", "LB", "RB", "LP", "RP", 
                      "SEMI" ]

    RULE_program = 0
    RULE_vardclr = 1
    RULE_funcdclr = 2
    RULE_paramdclr = 3
    RULE_param = 4
    RULE_typ = 5
    RULE_body = 6
    RULE_exp = 7
    RULE_funcall = 8

    ruleNames =  [ "program", "vardclr", "funcdclr", "paramdclr", "param", 
                   "typ", "body", "exp", "funcall" ]

    EOF = Token.EOF
    T__0=1
    COM=2
    INT=3
    FLOAT=4
    ID=5
    WS=6
    ERROR_CHAR=7
    INTLIT=8
    LB=9
    RB=10
    LP=11
    RP=12
    SEMI=13

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
            return self.getToken(BKOOLParser.EOF, 0)

        def vardclr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.VardclrContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.VardclrContext,i)


        def funcdclr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.FuncdclrContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.FuncdclrContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 18
                    self.vardclr()
                    pass

                elif la_ == 2:
                    self.state = 19
                    self.funcdclr()
                    pass


                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
                    break

            self.state = 24
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def SEMI(self):
            return self.getToken(BKOOLParser.SEMI, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COM)
            else:
                return self.getToken(BKOOLParser.COM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_vardclr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardclr" ):
                return visitor.visitVardclr(self)
            else:
                return visitor.visitChildren(self)




    def vardclr(self):

        localctx = BKOOLParser.VardclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vardclr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.typ()

            self.state = 27
            self.match(BKOOLParser.ID)
            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COM:
                self.state = 28
                self.match(BKOOLParser.COM)
                self.state = 29
                self.match(BKOOLParser.ID)
                self.state = 34
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35
            self.match(BKOOLParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def paramdclr(self):
            return self.getTypedRuleContext(BKOOLParser.ParamdclrContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdclr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdclr" ):
                return visitor.visitFuncdclr(self)
            else:
                return visitor.visitChildren(self)




    def funcdclr(self):

        localctx = BKOOLParser.FuncdclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.typ()
            self.state = 38
            self.match(BKOOLParser.ID)
            self.state = 39
            self.paramdclr()
            self.state = 40
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.ParamContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.ParamContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.SEMI)
            else:
                return self.getToken(BKOOLParser.SEMI, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_paramdclr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamdclr" ):
                return visitor.visitParamdclr(self)
            else:
                return visitor.visitChildren(self)




    def paramdclr(self):

        localctx = BKOOLParser.ParamdclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_paramdclr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(BKOOLParser.LB)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.INT or _la==BKOOLParser.FLOAT:
                self.state = 43
                self.param()
                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKOOLParser.SEMI:
                    self.state = 44
                    self.match(BKOOLParser.SEMI)
                    self.state = 45
                    self.param()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 53
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(BKOOLParser.TypContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.ID)
            else:
                return self.getToken(BKOOLParser.ID, i)

        def COM(self, i:int=None):
            if i is None:
                return self.getTokens(BKOOLParser.COM)
            else:
                return self.getToken(BKOOLParser.COM, i)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.typ()

            self.state = 56
            self.match(BKOOLParser.ID)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKOOLParser.COM:
                self.state = 57
                self.match(BKOOLParser.COM)
                self.state = 58
                self.match(BKOOLParser.ID)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(BKOOLParser.INT, 0)

        def FLOAT(self):
            return self.getToken(BKOOLParser.FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_typ

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = BKOOLParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typ)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==BKOOLParser.INT or _la==BKOOLParser.FLOAT):
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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return BKOOLParser.RULE_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBody" ):
                return visitor.visitBody(self)
            else:
                return visitor.visitChildren(self)




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(BKOOLParser.T__0)
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
            return self.getTypedRuleContext(BKOOLParser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(BKOOLParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKOOLParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKOOLParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.funcall()
                pass
            elif token in [BKOOLParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(BKOOLParser.INTLIT)
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

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def LB(self):
            return self.getToken(BKOOLParser.LB, 0)

        def RB(self):
            return self.getToken(BKOOLParser.RB, 0)

        def exp(self):
            return self.getTypedRuleContext(BKOOLParser.ExpContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncall" ):
                return visitor.visitFuncall(self)
            else:
                return visitor.visitChildren(self)




    def funcall(self):

        localctx = BKOOLParser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(BKOOLParser.ID)
            self.state = 73
            self.match(BKOOLParser.LB)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKOOLParser.ID or _la==BKOOLParser.INTLIT:
                self.state = 74
                self.exp()


            self.state = 77
            self.match(BKOOLParser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





