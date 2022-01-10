# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("\u00b8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\4\6\4\\\n\4\r\4\16\4]\3\5\3\5\3\6\3\6\3\7\3\7\3\b")
        buf.write("\3\b\3\t\3\t\3\n\3\n\3\n\3\n\7\nn\n\n\f\n\16\nq\13\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\6\13y\n\13\r\13\16\13z\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3o\2)\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\2\37\2!\2#\2%\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67")
        buf.write("\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\2\3\2\36\3\2\62;")
        buf.write("\5\2\n\f\16\17\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2")
        buf.write("GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4")
        buf.write("\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTt")
        buf.write("t\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2")
        buf.write("[[{{\4\2\\\\||\2\u00a0\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\3Q\3\2\2\2\5U\3\2\2\2\7[\3\2")
        buf.write("\2\2\t_\3\2\2\2\13a\3\2\2\2\rc\3\2\2\2\17e\3\2\2\2\21")
        buf.write("g\3\2\2\2\23i\3\2\2\2\25x\3\2\2\2\27~\3\2\2\2\31\u0080")
        buf.write("\3\2\2\2\33\u0082\3\2\2\2\35\u0084\3\2\2\2\37\u0086\3")
        buf.write("\2\2\2!\u0088\3\2\2\2#\u008a\3\2\2\2%\u008c\3\2\2\2\'")
        buf.write("\u008e\3\2\2\2)\u0090\3\2\2\2+\u0092\3\2\2\2-\u0094\3")
        buf.write("\2\2\2/\u0096\3\2\2\2\61\u0098\3\2\2\2\63\u009a\3\2\2")
        buf.write("\2\65\u009c\3\2\2\2\67\u009e\3\2\2\29\u00a0\3\2\2\2;\u00a2")
        buf.write("\3\2\2\2=\u00a4\3\2\2\2?\u00a6\3\2\2\2A\u00a8\3\2\2\2")
        buf.write("C\u00aa\3\2\2\2E\u00ac\3\2\2\2G\u00ae\3\2\2\2I\u00b0\3")
        buf.write("\2\2\2K\u00b2\3\2\2\2M\u00b4\3\2\2\2O\u00b6\3\2\2\2QR")
        buf.write("\7k\2\2RS\7p\2\2ST\7v\2\2T\4\3\2\2\2UV\7x\2\2VW\7q\2\2")
        buf.write("WX\7k\2\2XY\7f\2\2Y\6\3\2\2\2Z\\\t\2\2\2[Z\3\2\2\2\\]")
        buf.write("\3\2\2\2][\3\2\2\2]^\3\2\2\2^\b\3\2\2\2_`\7*\2\2`\n\3")
        buf.write("\2\2\2ab\7+\2\2b\f\3\2\2\2cd\7}\2\2d\16\3\2\2\2ef\7\177")
        buf.write("\2\2f\20\3\2\2\2gh\7=\2\2h\22\3\2\2\2ij\7,\2\2jk\7,\2")
        buf.write("\2ko\3\2\2\2ln\13\2\2\2ml\3\2\2\2nq\3\2\2\2op\3\2\2\2")
        buf.write("om\3\2\2\2pr\3\2\2\2qo\3\2\2\2rs\7,\2\2st\7,\2\2tu\3\2")
        buf.write("\2\2uv\b\n\2\2v\24\3\2\2\2wy\t\3\2\2xw\3\2\2\2yz\3\2\2")
        buf.write("\2zx\3\2\2\2z{\3\2\2\2{|\3\2\2\2|}\b\13\2\2}\26\3\2\2")
        buf.write("\2~\177\13\2\2\2\177\30\3\2\2\2\u0080\u0081\13\2\2\2\u0081")
        buf.write("\32\3\2\2\2\u0082\u0083\13\2\2\2\u0083\34\3\2\2\2\u0084")
        buf.write("\u0085\t\4\2\2\u0085\36\3\2\2\2\u0086\u0087\t\5\2\2\u0087")
        buf.write(" \3\2\2\2\u0088\u0089\t\6\2\2\u0089\"\3\2\2\2\u008a\u008b")
        buf.write("\t\7\2\2\u008b$\3\2\2\2\u008c\u008d\t\b\2\2\u008d&\3\2")
        buf.write("\2\2\u008e\u008f\t\t\2\2\u008f(\3\2\2\2\u0090\u0091\t")
        buf.write("\n\2\2\u0091*\3\2\2\2\u0092\u0093\t\13\2\2\u0093,\3\2")
        buf.write("\2\2\u0094\u0095\t\f\2\2\u0095.\3\2\2\2\u0096\u0097\t")
        buf.write("\r\2\2\u0097\60\3\2\2\2\u0098\u0099\t\16\2\2\u0099\62")
        buf.write("\3\2\2\2\u009a\u009b\t\17\2\2\u009b\64\3\2\2\2\u009c\u009d")
        buf.write("\t\20\2\2\u009d\66\3\2\2\2\u009e\u009f\t\21\2\2\u009f")
        buf.write("8\3\2\2\2\u00a0\u00a1\t\22\2\2\u00a1:\3\2\2\2\u00a2\u00a3")
        buf.write("\t\23\2\2\u00a3<\3\2\2\2\u00a4\u00a5\t\24\2\2\u00a5>\3")
        buf.write("\2\2\2\u00a6\u00a7\t\25\2\2\u00a7@\3\2\2\2\u00a8\u00a9")
        buf.write("\t\26\2\2\u00a9B\3\2\2\2\u00aa\u00ab\t\27\2\2\u00abD\3")
        buf.write("\2\2\2\u00ac\u00ad\t\30\2\2\u00adF\3\2\2\2\u00ae\u00af")
        buf.write("\t\31\2\2\u00afH\3\2\2\2\u00b0\u00b1\t\32\2\2\u00b1J\3")
        buf.write("\2\2\2\u00b2\u00b3\t\33\2\2\u00b3L\3\2\2\2\u00b4\u00b5")
        buf.write("\t\34\2\2\u00b5N\3\2\2\2\u00b6\u00b7\t\35\2\2\u00b7P\3")
        buf.write("\2\2\2\6\2]oz\3\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    VOIDTYPE = 2
    INTLIT = 3
    LB = 4
    RB = 5
    LP = 6
    RP = 7
    SEMI = 8
    BLOCK_COMMENT = 9
    WS = 10
    ERROR_CHAR = 11
    UNCLOSE_STRING = 12
    ILLEGAL_ESCAPE = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "VOIDTYPE", "INTLIT", "LB", "RB", "LP", "RP", 
                  "SEMI", "BLOCK_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "A", "B", "C", "D", "E", "F", "G", "H", 
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
                  "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


