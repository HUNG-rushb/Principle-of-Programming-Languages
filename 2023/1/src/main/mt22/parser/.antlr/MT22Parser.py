# Generated from d:\Github\Principle-of-Programming-Languages\2023\1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3<")
        buf.write("\u009e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\5\3-\n\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\64\n\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5<\n\5\f\5\16\5")
        buf.write("?\13\5\3\6\3\6\3\6\3\6\3\6\3\6\7\6G\n\6\f\6\16\6J\13\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\7\7R\n\7\f\7\16\7U\13\7\3\b\3")
        buf.write("\b\3\b\5\bZ\n\b\3\t\3\t\3\t\5\t_\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\7\nf\n\n\f\n\16\ni\13\n\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fx\n\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u0085\n\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u008c\n\17\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\5\21\u009a")
        buf.write("\n\21\3\22\3\22\3\22\2\6\b\n\f\22\23\2\4\6\b\n\f\16\20")
        buf.write("\22\24\26\30\32\34\36 \"\2\7\5\2 !#$&\'\3\2\36\37\3\2")
        buf.write("\30\31\3\2\32\34\3\2\23\26\2\u009d\2$\3\2\2\2\4,\3\2\2")
        buf.write("\2\6\63\3\2\2\2\b\65\3\2\2\2\n@\3\2\2\2\fK\3\2\2\2\16")
        buf.write("Y\3\2\2\2\20^\3\2\2\2\22`\3\2\2\2\24j\3\2\2\2\26w\3\2")
        buf.write("\2\2\30y\3\2\2\2\32\u0084\3\2\2\2\34\u008b\3\2\2\2\36")
        buf.write("\u008d\3\2\2\2 \u0099\3\2\2\2\"\u009b\3\2\2\2$%\5\34\17")
        buf.write("\2%&\7\2\2\3&\3\3\2\2\2\'(\5\6\4\2()\7\"\2\2)*\5\6\4\2")
        buf.write("*-\3\2\2\2+-\5\6\4\2,\'\3\2\2\2,+\3\2\2\2-\5\3\2\2\2.")
        buf.write("/\5\b\5\2/\60\t\2\2\2\60\61\5\b\5\2\61\64\3\2\2\2\62\64")
        buf.write("\5\b\5\2\63.\3\2\2\2\63\62\3\2\2\2\64\7\3\2\2\2\65\66")
        buf.write("\b\5\1\2\66\67\5\n\6\2\67=\3\2\2\289\f\4\2\29:\t\3\2\2")
        buf.write(":<\5\n\6\2;8\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2\2>\t")
        buf.write("\3\2\2\2?=\3\2\2\2@A\b\6\1\2AB\5\f\7\2BH\3\2\2\2CD\f\4")
        buf.write("\2\2DE\t\4\2\2EG\5\f\7\2FC\3\2\2\2GJ\3\2\2\2HF\3\2\2\2")
        buf.write("HI\3\2\2\2I\13\3\2\2\2JH\3\2\2\2KL\b\7\1\2LM\5\16\b\2")
        buf.write("MS\3\2\2\2NO\f\4\2\2OP\t\5\2\2PR\5\16\b\2QN\3\2\2\2RU")
        buf.write("\3\2\2\2SQ\3\2\2\2ST\3\2\2\2T\r\3\2\2\2US\3\2\2\2VW\7")
        buf.write("\35\2\2WZ\5\16\b\2XZ\5\20\t\2YV\3\2\2\2YX\3\2\2\2Z\17")
        buf.write("\3\2\2\2[\\\7\31\2\2\\_\5\20\t\2]_\5\22\n\2^[\3\2\2\2")
        buf.write("^]\3\2\2\2_\21\3\2\2\2`a\b\n\1\2ab\5\24\13\2bg\3\2\2\2")
        buf.write("cd\f\4\2\2df\5\26\f\2ec\3\2\2\2fi\3\2\2\2ge\3\2\2\2gh")
        buf.write("\3\2\2\2h\23\3\2\2\2ig\3\2\2\2jk\7(\2\2kl\5\4\3\2lm\7")
        buf.write(")\2\2m\25\3\2\2\2no\7*\2\2op\5\4\3\2pq\7+\2\2qr\5\26\f")
        buf.write("\2rx\3\2\2\2st\7*\2\2tu\5\4\3\2uv\7+\2\2vx\3\2\2\2wn\3")
        buf.write("\2\2\2ws\3\2\2\2x\27\3\2\2\2yz\7\20\2\2z{\7*\2\2{|\5\32")
        buf.write("\16\2|}\7+\2\2}\31\3\2\2\2~\177\5\4\3\2\177\u0080\7/\2")
        buf.write("\2\u0080\u0081\5\32\16\2\u0081\u0085\3\2\2\2\u0082\u0085")
        buf.write("\5\4\3\2\u0083\u0085\3\2\2\2\u0084~\3\2\2\2\u0084\u0082")
        buf.write("\3\2\2\2\u0084\u0083\3\2\2\2\u0085\33\3\2\2\2\u0086\u008c")
        buf.write("\7\65\2\2\u0087\u008c\7\64\2\2\u0088\u008c\7\63\2\2\u0089")
        buf.write("\u008c\7\66\2\2\u008a\u008c\5\30\r\2\u008b\u0086\3\2\2")
        buf.write("\2\u008b\u0087\3\2\2\2\u008b\u0088\3\2\2\2\u008b\u0089")
        buf.write("\3\2\2\2\u008b\u008a\3\2\2\2\u008c\35\3\2\2\2\u008d\u008e")
        buf.write("\7\20\2\2\u008e\u008f\7*\2\2\u008f\u0090\5 \21\2\u0090")
        buf.write("\u0091\7+\2\2\u0091\u0092\7\16\2\2\u0092\u0093\5\"\22")
        buf.write("\2\u0093\37\3\2\2\2\u0094\u0095\7\65\2\2\u0095\u0096\7")
        buf.write("/\2\2\u0096\u009a\5 \21\2\u0097\u009a\7\65\2\2\u0098\u009a")
        buf.write("\3\2\2\2\u0099\u0094\3\2\2\2\u0099\u0097\3\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a!\3\2\2\2\u009b\u009c\t\6\2\2\u009c")
        buf.write("#\3\2\2\2\16,\63=HSY^gw\u0084\u008b\u0099")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'function'", "'auto'", "'break'", "'do'", 
                     "'else'", "'for'", "'if'", "'return'", "'while'", "'out'", 
                     "'continue'", "'of'", "'inherit'", "'array'", "'true'", 
                     "'false'", "'boolean'", "'float'", "'integer'", "'string'", 
                     "'void'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
                     "'&&'", "'||'", "'=='", "'!='", "'::'", "'>='", "'<='", 
                     "'='", "'>'", "'<'", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'", "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "FUNCTION", "AUTO", "BREAK", "DO", "ELSE", 
                      "FOR", "IF", "RETURN", "WHILE", "OUT", "CONTINUE", 
                      "OF", "INHERIT", "ARRAY", "TRUE", "FALSE", "BOOLEAN", 
                      "FLOAT", "INTEGER", "STRING", "VOID", "PLUSOP", "MINUSOP", 
                      "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", 
                      "OROP", "EQUALOP", "NOTEQUALOP", "DOUBLECOLONOP", 
                      "GTE", "LTE", "EQUAL", "GT", "LT", "LB", "RB", "LSB", 
                      "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "VARIABLE_IDENTIFIERS", "BOOLLIT", "FLOATLIT", "INTLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
                      "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_expr = 1
    RULE_expr1 = 2
    RULE_expr2 = 3
    RULE_expr3 = 4
    RULE_expr4 = 5
    RULE_expr5 = 6
    RULE_expr6 = 7
    RULE_expr7 = 8
    RULE_expr8 = 9
    RULE_index_operators = 10
    RULE_array_lit = 11
    RULE_array_val = 12
    RULE_literal = 13
    RULE_array_type = 14
    RULE_array_dimension = 15
    RULE_atomic_types = 16

    ruleNames =  [ "program", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "index_operators", 
                   "array_lit", "array_val", "literal", "array_type", "array_dimension", 
                   "atomic_types" ]

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
    ARRAY=14
    TRUE=15
    FALSE=16
    BOOLEAN=17
    FLOAT=18
    INTEGER=19
    STRING=20
    VOID=21
    PLUSOP=22
    MINUSOP=23
    MULTIPLYOP=24
    DIVIDEOP=25
    MODULOOP=26
    NOTOP=27
    ANDOP=28
    OROP=29
    EQUALOP=30
    NOTEQUALOP=31
    DOUBLECOLONOP=32
    GTE=33
    LTE=34
    EQUAL=35
    GT=36
    LT=37
    LB=38
    RB=39
    LSB=40
    RSB=41
    LCB=42
    RCB=43
    DOT=44
    COMMA=45
    COLON=46
    SEMICOLON=47
    VARIABLE_IDENTIFIERS=48
    BOOLLIT=49
    FLOATLIT=50
    INTLIT=51
    STRINGLIT=52
    UNCLOSE_STRING=53
    ILLEGAL_ESCAPE=54
    WS=55
    BLOCK_CMT=56
    LINE_CMT=57
    ERROR_CHAR=58

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

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.literal()
            self.state = 35
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def DOUBLECOLONOP(self):
            return self.getToken(MT22Parser.DOUBLECOLONOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expr)
        try:
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.expr1()
                self.state = 38
                self.match(MT22Parser.DOUBLECOLONOP)
                self.state = 39
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQUALOP(self):
            return self.getToken(MT22Parser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(MT22Parser.NOTEQUALOP, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def LTE(self):
            return self.getToken(MT22Parser.LTE, 0)

        def GTE(self):
            return self.getToken(MT22Parser.GTE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.expr2(0)
                self.state = 45
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUALOP) | (1 << MT22Parser.NOTEQUALOP) | (1 << MT22Parser.GTE) | (1 << MT22Parser.LTE) | (1 << MT22Parser.GT) | (1 << MT22Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 46
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def ANDOP(self):
            return self.getToken(MT22Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MT22Parser.OROP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 54
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 55
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ANDOP or _la==MT22Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 56
                    self.expr3(0) 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def PLUSOP(self):
            return self.getToken(MT22Parser.PLUSOP, 0)

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 70
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 65
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 66
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUSOP or _la==MT22Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 67
                    self.expr4(0) 
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MULTIPLYOP(self):
            return self.getToken(MT22Parser.MULTIPLYOP, 0)

        def DIVIDEOP(self):
            return self.getToken(MT22Parser.DIVIDEOP, 0)

        def MODULOOP(self):
            return self.getToken(MT22Parser.MODULOOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 76
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 77
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULTIPLYOP) | (1 << MT22Parser.DIVIDEOP) | (1 << MT22Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 78
                    self.expr5() 
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(MT22Parser.NOTOP, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr5)
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 84
                self.match(MT22Parser.NOTOP)
                self.state = 85
                self.expr5()
                pass
            elif token in [MT22Parser.MINUSOP, MT22Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.expr6()
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


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr6)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(MT22Parser.MINUSOP)
                self.state = 90
                self.expr6()
                pass
            elif token in [MT22Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.expr7(0)
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


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(MT22Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(MT22Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 97
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 98
                    self.index_operators() 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr8




    def expr8(self):

        localctx = MT22Parser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expr8)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(MT22Parser.LB)
            self.state = 105
            self.expr()
            self.state = 106
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(MT22Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_index_operators




    def index_operators(self):

        localctx = MT22Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_index_operators)
        try:
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 108
                self.match(MT22Parser.LSB)
                self.state = 109
                self.expr()
                self.state = 110
                self.match(MT22Parser.RSB)
                self.state = 111
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 113
                self.match(MT22Parser.LSB)
                self.state = 114
                self.expr()
                self.state = 115
                self.match(MT22Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def array_val(self):
            return self.getTypedRuleContext(MT22Parser.Array_valContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array_lit




    def array_lit(self):

        localctx = MT22Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MT22Parser.ARRAY)
            self.state = 120
            self.match(MT22Parser.LSB)
            self.state = 121
            self.array_val()
            self.state = 122
            self.match(MT22Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def array_val(self):
            return self.getTypedRuleContext(MT22Parser.Array_valContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_val




    def array_val(self):

        localctx = MT22Parser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_array_val)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.expr()
                self.state = 125
                self.match(MT22Parser.COMMA)
                self.state = 126
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


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

        def array_lit(self):
            return self.getTypedRuleContext(MT22Parser.Array_litContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_literal)
        try:
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.match(MT22Parser.INTLIT)
                pass
            elif token in [MT22Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(MT22Parser.FLOATLIT)
                pass
            elif token in [MT22Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 134
                self.match(MT22Parser.BOOLLIT)
                pass
            elif token in [MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 135
                self.match(MT22Parser.STRINGLIT)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 136
                self.array_lit()
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(MT22Parser.Array_dimensionContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_types(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typesContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.match(MT22Parser.ARRAY)
            self.state = 140
            self.match(MT22Parser.LSB)
            self.state = 141
            self.array_dimension()
            self.state = 142
            self.match(MT22Parser.RSB)
            self.state = 143
            self.match(MT22Parser.OF)
            self.state = 144
            self.atomic_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dimensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def array_dimension(self):
            return self.getTypedRuleContext(MT22Parser.Array_dimensionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_dimension




    def array_dimension(self):

        localctx = MT22Parser.Array_dimensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_dimension)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.match(MT22Parser.INTLIT)
                self.state = 147
                self.match(MT22Parser.COMMA)
                self.state = 148
                self.array_dimension()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.match(MT22Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_types




    def atomic_types(self):

        localctx = MT22Parser.Atomic_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_atomic_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr2_sempred
        self._predicates[4] = self.expr3_sempred
        self._predicates[5] = self.expr4_sempred
        self._predicates[8] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




