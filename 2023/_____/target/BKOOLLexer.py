# Generated from main/bkool/parser/BKOOL.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\22")
        buf.write("^\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\6")
        buf.write("\7C\n\7\r\7\16\7D\3\b\6\bH\n\b\r\b\16\bI\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\20\3\20\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22\3")
        buf.write("\2\5\5\2\13\f\17\17\"\"\4\2C\\c|\3\2\62;\2_\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5+\3\2\2\2\7")
        buf.write("\64\3\2\2\2\t8\3\2\2\2\13<\3\2\2\2\rB\3\2\2\2\17G\3\2")
        buf.write("\2\2\21K\3\2\2\2\23M\3\2\2\2\25O\3\2\2\2\27Q\3\2\2\2\31")
        buf.write("S\3\2\2\2\33U\3\2\2\2\35X\3\2\2\2\37Z\3\2\2\2!\\\3\2\2")
        buf.write("\2#$\7x\2\2$%\7c\2\2%&\7t\2\2&\'\7f\2\2\'(\7g\2\2()\7")
        buf.write("e\2\2)*\7n\2\2*\4\3\2\2\2+,\7h\2\2,-\7w\2\2-.\7p\2\2.")
        buf.write("/\7e\2\2/\60\7f\2\2\60\61\7g\2\2\61\62\7e\2\2\62\63\7")
        buf.write("n\2\2\63\6\3\2\2\2\64\65\t\2\2\2\65\66\3\2\2\2\66\67\b")
        buf.write("\4\2\2\67\b\3\2\2\289\7k\2\29:\7p\2\2:;\7v\2\2;\n\3\2")
        buf.write("\2\2<=\7x\2\2=>\7q\2\2>?\7k\2\2?@\7f\2\2@\f\3\2\2\2AC")
        buf.write("\t\3\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\16\3")
        buf.write("\2\2\2FH\t\4\2\2GF\3\2\2\2HI\3\2\2\2IG\3\2\2\2IJ\3\2\2")
        buf.write("\2J\20\3\2\2\2KL\7*\2\2L\22\3\2\2\2MN\7+\2\2N\24\3\2\2")
        buf.write("\2OP\7}\2\2P\26\3\2\2\2QR\7\177\2\2R\30\3\2\2\2ST\7=\2")
        buf.write("\2T\32\3\2\2\2UV\13\2\2\2VW\b\16\3\2W\34\3\2\2\2XY\13")
        buf.write("\2\2\2Y\36\3\2\2\2Z[\13\2\2\2[ \3\2\2\2\\]\13\2\2\2]\"")
        buf.write("\3\2\2\2\5\2DI\4\b\2\2\3\16\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    WS = 3
    INTTYPE = 4
    VOIDTYPE = 5
    ID = 6
    INTLIT = 7
    LB = 8
    RB = 9
    LP = 10
    RP = 11
    SEMI = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15
    UNTERMINATED_COMMENT = 16

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'vardecl'", "'funcdecl'", "'int'", "'void'", "'('", "')'", 
            "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", 
            "RP", "SEMI", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "WS", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", 
                  "LB", "RB", "LP", "RP", "SEMI", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[12] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


