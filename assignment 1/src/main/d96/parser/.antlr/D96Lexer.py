# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("\u00d6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\6\5e\n\5\r\5\16")
        buf.write("\5f\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\7\13w\n\13\f\13\16\13z\13\13\3\13\3\13\3\13")
        buf.write("\3\13\7\13\u0080\n\13\f\13\16\13\u0083\13\13\3\13\3\13")
        buf.write("\5\13\u0087\n\13\3\13\3\13\3\f\3\f\3\f\3\f\7\f\u008f\n")
        buf.write("\f\f\f\16\f\u0092\13\f\3\f\3\f\3\r\6\r\u0097\n\r\r\r\16")
        buf.write("\r\u0098\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26")
        buf.write("\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34")
        buf.write("\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\4")
        buf.write("x\u0081\2+\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\2#\2%\2\'\2)\2+\2-\2")
        buf.write("/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2C\2E\2G\2I\2K\2")
        buf.write("M\2O\2Q\2S\2\3\2\37\3\2\62;\4\2\f\f\17\17\5\2\13\f\17")
        buf.write("\17\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HH")
        buf.write("hh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\2\u00c1\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\3U\3\2\2\2\5Z")
        buf.write("\3\2\2\2\7^\3\2\2\2\td\3\2\2\2\13h\3\2\2\2\rj\3\2\2\2")
        buf.write("\17l\3\2\2\2\21n\3\2\2\2\23p\3\2\2\2\25\u0086\3\2\2\2")
        buf.write("\27\u008a\3\2\2\2\31\u0096\3\2\2\2\33\u009c\3\2\2\2\35")
        buf.write("\u009e\3\2\2\2\37\u00a0\3\2\2\2!\u00a2\3\2\2\2#\u00a4")
        buf.write("\3\2\2\2%\u00a6\3\2\2\2\'\u00a8\3\2\2\2)\u00aa\3\2\2\2")
        buf.write("+\u00ac\3\2\2\2-\u00ae\3\2\2\2/\u00b0\3\2\2\2\61\u00b2")
        buf.write("\3\2\2\2\63\u00b4\3\2\2\2\65\u00b6\3\2\2\2\67\u00b8\3")
        buf.write("\2\2\29\u00ba\3\2\2\2;\u00bc\3\2\2\2=\u00be\3\2\2\2?\u00c0")
        buf.write("\3\2\2\2A\u00c2\3\2\2\2C\u00c4\3\2\2\2E\u00c6\3\2\2\2")
        buf.write("G\u00c8\3\2\2\2I\u00ca\3\2\2\2K\u00cc\3\2\2\2M\u00ce\3")
        buf.write("\2\2\2O\u00d0\3\2\2\2Q\u00d2\3\2\2\2S\u00d4\3\2\2\2UV")
        buf.write("\7o\2\2VW\7c\2\2WX\7k\2\2XY\7p\2\2Y\4\3\2\2\2Z[\7k\2\2")
        buf.write("[\\\7p\2\2\\]\7v\2\2]\6\3\2\2\2^_\7x\2\2_`\7q\2\2`a\7")
        buf.write("k\2\2ab\7f\2\2b\b\3\2\2\2ce\t\2\2\2dc\3\2\2\2ef\3\2\2")
        buf.write("\2fd\3\2\2\2fg\3\2\2\2g\n\3\2\2\2hi\7*\2\2i\f\3\2\2\2")
        buf.write("jk\7+\2\2k\16\3\2\2\2lm\7}\2\2m\20\3\2\2\2no\7\177\2\2")
        buf.write("o\22\3\2\2\2pq\7=\2\2q\24\3\2\2\2rs\7*\2\2st\7,\2\2tx")
        buf.write("\3\2\2\2uw\13\2\2\2vu\3\2\2\2wz\3\2\2\2xy\3\2\2\2xv\3")
        buf.write("\2\2\2y{\3\2\2\2zx\3\2\2\2{|\7,\2\2|\u0087\7+\2\2}\u0081")
        buf.write("\5\17\b\2~\u0080\13\2\2\2\177~\3\2\2\2\u0080\u0083\3\2")
        buf.write("\2\2\u0081\u0082\3\2\2\2\u0081\177\3\2\2\2\u0082\u0084")
        buf.write("\3\2\2\2\u0083\u0081\3\2\2\2\u0084\u0085\5\21\t\2\u0085")
        buf.write("\u0087\3\2\2\2\u0086r\3\2\2\2\u0086}\3\2\2\2\u0087\u0088")
        buf.write("\3\2\2\2\u0088\u0089\b\13\2\2\u0089\26\3\2\2\2\u008a\u008b")
        buf.write("\7\61\2\2\u008b\u008c\7\61\2\2\u008c\u0090\3\2\2\2\u008d")
        buf.write("\u008f\n\3\2\2\u008e\u008d\3\2\2\2\u008f\u0092\3\2\2\2")
        buf.write("\u0090\u008e\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0093\3")
        buf.write("\2\2\2\u0092\u0090\3\2\2\2\u0093\u0094\b\f\2\2\u0094\30")
        buf.write("\3\2\2\2\u0095\u0097\t\4\2\2\u0096\u0095\3\2\2\2\u0097")
        buf.write("\u0098\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009a\3\2\2\2\u009a\u009b\b\r\2\2\u009b\32\3\2")
        buf.write("\2\2\u009c\u009d\13\2\2\2\u009d\34\3\2\2\2\u009e\u009f")
        buf.write("\13\2\2\2\u009f\36\3\2\2\2\u00a0\u00a1\13\2\2\2\u00a1")
        buf.write(" \3\2\2\2\u00a2\u00a3\t\5\2\2\u00a3\"\3\2\2\2\u00a4\u00a5")
        buf.write("\t\6\2\2\u00a5$\3\2\2\2\u00a6\u00a7\t\7\2\2\u00a7&\3\2")
        buf.write("\2\2\u00a8\u00a9\t\b\2\2\u00a9(\3\2\2\2\u00aa\u00ab\t")
        buf.write("\t\2\2\u00ab*\3\2\2\2\u00ac\u00ad\t\n\2\2\u00ad,\3\2\2")
        buf.write("\2\u00ae\u00af\t\13\2\2\u00af.\3\2\2\2\u00b0\u00b1\t\f")
        buf.write("\2\2\u00b1\60\3\2\2\2\u00b2\u00b3\t\r\2\2\u00b3\62\3\2")
        buf.write("\2\2\u00b4\u00b5\t\16\2\2\u00b5\64\3\2\2\2\u00b6\u00b7")
        buf.write("\t\17\2\2\u00b7\66\3\2\2\2\u00b8\u00b9\t\20\2\2\u00b9")
        buf.write("8\3\2\2\2\u00ba\u00bb\t\21\2\2\u00bb:\3\2\2\2\u00bc\u00bd")
        buf.write("\t\22\2\2\u00bd<\3\2\2\2\u00be\u00bf\t\23\2\2\u00bf>\3")
        buf.write("\2\2\2\u00c0\u00c1\t\24\2\2\u00c1@\3\2\2\2\u00c2\u00c3")
        buf.write("\t\25\2\2\u00c3B\3\2\2\2\u00c4\u00c5\t\26\2\2\u00c5D\3")
        buf.write("\2\2\2\u00c6\u00c7\t\27\2\2\u00c7F\3\2\2\2\u00c8\u00c9")
        buf.write("\t\30\2\2\u00c9H\3\2\2\2\u00ca\u00cb\t\31\2\2\u00cbJ\3")
        buf.write("\2\2\2\u00cc\u00cd\t\32\2\2\u00cdL\3\2\2\2\u00ce\u00cf")
        buf.write("\t\33\2\2\u00cfN\3\2\2\2\u00d0\u00d1\t\34\2\2\u00d1P\3")
        buf.write("\2\2\2\u00d2\u00d3\t\35\2\2\u00d3R\3\2\2\2\u00d4\u00d5")
        buf.write("\t\36\2\2\u00d5T\3\2\2\2\t\2fx\u0081\u0086\u0090\u0098")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    INTLIT = 4
    LB = 5
    RB = 6
    LP = 7
    RP = 8
    SEMI = 9
    BLOCK_COMMENT = 10
    LINE_COMMENT = 11
    WS = 12
    ERROR_CHAR = 13
    UNCLOSE_STRING = 14
    ILLEGAL_ESCAPE = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "INTLIT", "LB", "RB", "LP", "RP", "SEMI", 
            "BLOCK_COMMENT", "LINE_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "INTLIT", "LB", "RB", "LP", 
                  "RP", "SEMI", "BLOCK_COMMENT", "LINE_COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "A", "B", "C", "D", 
                  "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", 
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


