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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u00a5\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3\66\n\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\3\5\3\5\5\5E\n\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\5\13_\n\13\3\f\3\f\3\f\3\f")
        buf.write("\3\f\5\ff\n\f\3\r\3\r\5\rj\n\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16q\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\7\20z\n")
        buf.write("\20\f\20\16\20}\13\20\3\21\3\21\3\21\7\21\u0082\n\21\f")
        buf.write("\21\16\21\u0085\13\21\3\22\3\22\3\22\7\22\u008a\n\22\f")
        buf.write("\22\16\22\u008d\13\22\3\23\3\23\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\5\24\u009b\n\24\3\25\3\25")
        buf.write("\3\26\3\26\3\27\3\27\5\27\u00a3\n\27\3\27\2\2\30\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,\2\4\3\2\25\26")
        buf.write("\3\2\16\21\2\u009f\2.\3\2\2\2\4\60\3\2\2\2\69\3\2\2\2")
        buf.write("\b?\3\2\2\2\nH\3\2\2\2\fL\3\2\2\2\16P\3\2\2\2\20R\3\2")
        buf.write("\2\2\22T\3\2\2\2\24^\3\2\2\2\26e\3\2\2\2\30i\3\2\2\2\32")
        buf.write("p\3\2\2\2\34r\3\2\2\2\36v\3\2\2\2 ~\3\2\2\2\"\u0086\3")
        buf.write("\2\2\2$\u008e\3\2\2\2&\u009a\3\2\2\2(\u009c\3\2\2\2*\u009e")
        buf.write("\3\2\2\2,\u00a2\3\2\2\2./\7A\2\2/\3\3\2\2\2\60\61\t\2")
        buf.write("\2\2\61\62\5\36\20\2\62\63\78\2\2\63\65\5,\27\2\64\66")
        buf.write("\5\"\22\2\65\64\3\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("8\79\2\28\5\3\2\2\29:\7:\2\2:;\7\60\2\2;<\5\30\r\2<=\7")
        buf.write("\61\2\2=>\5\f\7\2>\7\3\2\2\2?@\t\2\2\2@A\5 \21\2AB\78")
        buf.write("\2\2BD\5,\27\2CE\5\"\22\2DC\3\2\2\2DE\3\2\2\2EF\3\2\2")
        buf.write("\2FG\79\2\2G\t\3\2\2\2HI\7;\2\2IJ\7\'\2\2JK\5\20\t\2K")
        buf.write("\13\3\2\2\2LM\7\64\2\2MN\5\16\b\2NO\7\65\2\2O\r\3\2\2")
        buf.write("\2PQ\3\2\2\2Q\17\3\2\2\2RS\3\2\2\2S\21\3\2\2\2TU\7\f\2")
        buf.write("\2UV\7\60\2\2VW\5\24\13\2WX\7\61\2\2X\23\3\2\2\2YZ\5\20")
        buf.write("\t\2Z[\7\67\2\2[\\\5\24\13\2\\_\3\2\2\2]_\5\20\t\2^Y\3")
        buf.write("\2\2\2^]\3\2\2\2_\25\3\2\2\2`f\7>\2\2af\7=\2\2bf\7\t\2")
        buf.write("\2cf\7<\2\2df\5\22\n\2e`\3\2\2\2ea\3\2\2\2eb\3\2\2\2e")
        buf.write("c\3\2\2\2ed\3\2\2\2f\27\3\2\2\2gj\5\32\16\2hj\3\2\2\2")
        buf.write("ig\3\2\2\2ih\3\2\2\2j\31\3\2\2\2kl\5\34\17\2lm\79\2\2")
        buf.write("mn\5\32\16\2nq\3\2\2\2oq\5\34\17\2pk\3\2\2\2po\3\2\2\2")
        buf.write("q\33\3\2\2\2rs\5\36\20\2st\78\2\2tu\5,\27\2u\35\3\2\2")
        buf.write("\2v{\7:\2\2wx\7\67\2\2xz\7:\2\2yw\3\2\2\2z}\3\2\2\2{y")
        buf.write("\3\2\2\2{|\3\2\2\2|\37\3\2\2\2}{\3\2\2\2~\u0083\7;\2\2")
        buf.write("\177\u0080\7\67\2\2\u0080\u0082\7;\2\2\u0081\177\3\2\2")
        buf.write("\2\u0082\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084")
        buf.write("\3\2\2\2\u0084!\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u008b")
        buf.write("\5\26\f\2\u0087\u0088\7\67\2\2\u0088\u008a\5\26\f\2\u0089")
        buf.write("\u0087\3\2\2\2\u008a\u008d\3\2\2\2\u008b\u0089\3\2\2\2")
        buf.write("\u008b\u008c\3\2\2\2\u008c#\3\2\2\2\u008d\u008b\3\2\2")
        buf.write("\2\u008e\u008f\7\f\2\2\u008f\u0090\7\62\2\2\u0090\u0091")
        buf.write("\5&\24\2\u0091\u0092\7\67\2\2\u0092\u0093\5(\25\2\u0093")
        buf.write("\u0094\7\63\2\2\u0094%\3\2\2\2\u0095\u009b\5$\23\2\u0096")
        buf.write("\u009b\7\16\2\2\u0097\u009b\7\17\2\2\u0098\u009b\7\20")
        buf.write("\2\2\u0099\u009b\7\21\2\2\u009a\u0095\3\2\2\2\u009a\u0096")
        buf.write("\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0098\3\2\2\2\u009a")
        buf.write("\u0099\3\2\2\2\u009b\'\3\2\2\2\u009c\u009d\7>\2\2\u009d")
        buf.write(")\3\2\2\2\u009e\u009f\t\3\2\2\u009f+\3\2\2\2\u00a0\u00a3")
        buf.write("\5*\26\2\u00a1\u00a3\5$\23\2\u00a2\u00a0\3\2\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a3-\3\2\2\2\r\65D^eip{\u0083\u008b\u009a")
        buf.write("\u00a2")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "<INVALID>", "'True'", "'False'", 
                     "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'::'", "'..'", "'_'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'>='", "'<='", "'>'", "'<'", "'==.'", 
                     "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
                     "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "BOOLLIT", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", 
                      "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                      "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", 
                      "NOTEQUAL", "GTE", "LTE", "GT", "LT", "STREQUALOP", 
                      "STRCONCATOP", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                      "DOT", "COMMA", "COLON", "SEMICOLON", "IDENTIFIERS", 
                      "VARIABLE_IDENTIFIERS", "STRINGLIT", "FLOATLIT", "INTLIT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "BLOCK_COMMENT", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_attribute_declaration = 1
    RULE_method_declaration = 2
    RULE_variable_declaration = 3
    RULE_assignment_statements = 4
    RULE_block_statements = 5
    RULE_statements = 6
    RULE_expr = 7
    RULE_array_lit = 8
    RULE_array_val = 9
    RULE_literal = 10
    RULE_list_parameters = 11
    RULE_parameters = 12
    RULE_param = 13
    RULE_identifier_list = 14
    RULE_variable_identifier_list = 15
    RULE_value_list = 16
    RULE_array_type = 17
    RULE_array_element_type = 18
    RULE_array_size = 19
    RULE_primitive_type = 20
    RULE_variable_type = 21

    ruleNames =  [ "program", "attribute_declaration", "method_declaration", 
                   "variable_declaration", "assignment_statements", "block_statements", 
                   "statements", "expr", "array_lit", "array_val", "literal", 
                   "list_parameters", "parameters", "param", "identifier_list", 
                   "variable_identifier_list", "value_list", "array_type", 
                   "array_element_type", "array_size", "primitive_type", 
                   "variable_type" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    BOOLLIT=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    STRING=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    SELF=25
    DOUBLECOLONOP=26
    DOUBLEDOTOP=27
    UNDERSCORE=28
    PLUSOP=29
    MINUSOP=30
    MULTIPLYOP=31
    DIVIDEOP=32
    MODULOOP=33
    NOTOP=34
    ANDOP=35
    OROP=36
    EQUALOP=37
    ASSIGNOP=38
    NOTEQUAL=39
    GTE=40
    LTE=41
    GT=42
    LT=43
    STREQUALOP=44
    STRCONCATOP=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    LCB=50
    RCB=51
    DOT=52
    COMMA=53
    COLON=54
    SEMICOLON=55
    IDENTIFIERS=56
    VARIABLE_IDENTIFIERS=57
    STRINGLIT=58
    FLOATLIT=59
    INTLIT=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    BLOCK_COMMENT=63
    WS=64
    ERROR_CHAR=65

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
            self.state = 44
            self.match(D96Parser.BLOCK_COMMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attribute_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_attribute_declaration




    def attribute_declaration(self):

        localctx = D96Parser.Attribute_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_attribute_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 47
            self.identifier_list()
            self.state = 48
            self.match(D96Parser.COLON)
            self.state = 49
            self.variable_type()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT))) != 0):
                self.state = 50
                self.value_list()


            self.state = 53
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self):
            return self.getToken(D96Parser.IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_method_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(D96Parser.IDENTIFIERS)
            self.state = 56
            self.match(D96Parser.LB)
            self.state = 57
            self.list_parameters()
            self.state = 58
            self.match(D96Parser.RB)
            self.state = 59
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_declaration




    def variable_declaration(self):

        localctx = D96Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 62
            self.variable_identifier_list()
            self.state = 63
            self.match(D96Parser.COLON)
            self.state = 64
            self.variable_type()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT))) != 0):
                self.state = 65
                self.value_list()


            self.state = 68
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IDENTIFIERS, 0)

        def EQUALOP(self):
            return self.getToken(D96Parser.EQUALOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statements




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(D96Parser.VARIABLE_IDENTIFIERS)
            self.state = 71
            self.match(D96Parser.EQUALOP)
            self.state = 72
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statements




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(D96Parser.LCB)
            self.state = 75
            self.statements()
            self.state = 76
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_statements




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statements)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def array_val(self):
            return self.getTypedRuleContext(D96Parser.Array_valContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_lit




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(D96Parser.ARRAY)
            self.state = 83
            self.match(D96Parser.LB)
            self.state = 84
            self.array_val()
            self.state = 85
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def array_val(self):
            return self.getTypedRuleContext(D96Parser.Array_valContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_val




    def array_val(self):

        localctx = D96Parser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array_val)
        try:
            self.state = 92
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.expr()
                self.state = 88
                self.match(D96Parser.COMMA)
                self.state = 89
                self.array_val()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.expr()
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


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(D96Parser.Array_litContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_literal)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 94
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 96
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 97
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 98
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


    class List_parametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_parameters




    def list_parameters(self):

        localctx = D96Parser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_list_parameters)
        try:
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.IDENTIFIERS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.parameters()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

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


    class ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def parameters(self):
            return self.getTypedRuleContext(D96Parser.ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_parameters




    def parameters(self):

        localctx = D96Parser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_parameters)
        try:
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self.param()
                self.state = 106
                self.match(D96Parser.SEMICOLON)
                self.state = 107
                self.parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 109
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.identifier_list()
            self.state = 113
            self.match(D96Parser.COLON)
            self.state = 114
            self.variable_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.IDENTIFIERS)
            else:
                return self.getToken(D96Parser.IDENTIFIERS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier_list




    def identifier_list(self):

        localctx = D96Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(D96Parser.IDENTIFIERS)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 117
                self.match(D96Parser.COMMA)
                self.state = 118
                self.match(D96Parser.IDENTIFIERS)
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_identifier_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.VARIABLE_IDENTIFIERS)
            else:
                return self.getToken(D96Parser.VARIABLE_IDENTIFIERS, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_identifier_list




    def variable_identifier_list(self):

        localctx = D96Parser.Variable_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_variable_identifier_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(D96Parser.VARIABLE_IDENTIFIERS)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 125
                self.match(D96Parser.COMMA)
                self.state = 126
                self.match(D96Parser.VARIABLE_IDENTIFIERS)
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.LiteralContext)
            else:
                return self.getTypedRuleContext(D96Parser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_value_list




    def value_list(self):

        localctx = D96Parser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_value_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.literal()
            self.state = 137
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.COMMA:
                self.state = 133
                self.match(D96Parser.COMMA)
                self.state = 134
                self.literal()
                self.state = 139
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def array_element_type(self):
            return self.getTypedRuleContext(D96Parser.Array_element_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def array_size(self):
            return self.getTypedRuleContext(D96Parser.Array_sizeContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(D96Parser.ARRAY)
            self.state = 141
            self.match(D96Parser.LSB)
            self.state = 142
            self.array_element_type()
            self.state = 143
            self.match(D96Parser.COMMA)
            self.state = 144
            self.array_size()
            self.state = 145
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_element_type




    def array_element_type(self):

        localctx = D96Parser.Array_element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_array_element_type)
        try:
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 148
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 149
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 150
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 151
                self.match(D96Parser.STRING)
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


    class Array_sizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_size




    def array_size(self):

        localctx = D96Parser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(D96Parser.INTLIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
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


    class Variable_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_type




    def variable_type(self):

        localctx = D96Parser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_variable_type)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.array_type()
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





