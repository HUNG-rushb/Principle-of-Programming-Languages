# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\35")
        buf.write("\u012c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\5\21\u00cd\n\21\3\22\6\22\u00d0\n\22\r\22\16\22\u00d1")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\7\30\u00e2\n\30\f\30\16\30\u00e5\13\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\31\6\31\u00ed\n\31\r\31\16")
        buf.write("\31\u00ee\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35")
        buf.write("\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3")
        buf.write("$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\u00e3\2\67\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\2;\2=\2?\2A\2C\2E\2G\2I\2K\2M\2O\2")
        buf.write("Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2\3\2\36\3\2")
        buf.write("\62;\5\2\n\f\16\17\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFf")
        buf.write("f\4\2GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2")
        buf.write("MMmm\4\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4")
        buf.write("\2TTtt\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZz")
        buf.write("z\4\2[[{{\4\2\\\\||\2\u0115\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\3m\3\2\2\2\5q\3\2\2")
        buf.write("\2\7v\3\2\2\2\t|\3\2\2\2\13\u0085\3\2\2\2\r\u0088\3\2")
        buf.write("\2\2\17\u008f\3\2\2\2\21\u0094\3\2\2\2\23\u009c\3\2\2")
        buf.write("\2\25\u00a1\3\2\2\2\27\u00a7\3\2\2\2\31\u00b0\3\2\2\2")
        buf.write("\33\u00b6\3\2\2\2\35\u00be\3\2\2\2\37\u00c5\3\2\2\2!\u00cc")
        buf.write("\3\2\2\2#\u00cf\3\2\2\2%\u00d3\3\2\2\2\'\u00d5\3\2\2\2")
        buf.write(")\u00d7\3\2\2\2+\u00d9\3\2\2\2-\u00db\3\2\2\2/\u00dd\3")
        buf.write("\2\2\2\61\u00ec\3\2\2\2\63\u00f2\3\2\2\2\65\u00f4\3\2")
        buf.write("\2\2\67\u00f6\3\2\2\29\u00f8\3\2\2\2;\u00fa\3\2\2\2=\u00fc")
        buf.write("\3\2\2\2?\u00fe\3\2\2\2A\u0100\3\2\2\2C\u0102\3\2\2\2")
        buf.write("E\u0104\3\2\2\2G\u0106\3\2\2\2I\u0108\3\2\2\2K\u010a\3")
        buf.write("\2\2\2M\u010c\3\2\2\2O\u010e\3\2\2\2Q\u0110\3\2\2\2S\u0112")
        buf.write("\3\2\2\2U\u0114\3\2\2\2W\u0116\3\2\2\2Y\u0118\3\2\2\2")
        buf.write("[\u011a\3\2\2\2]\u011c\3\2\2\2_\u011e\3\2\2\2a\u0120\3")
        buf.write("\2\2\2c\u0122\3\2\2\2e\u0124\3\2\2\2g\u0126\3\2\2\2i\u0128")
        buf.write("\3\2\2\2k\u012a\3\2\2\2mn\7k\2\2no\7p\2\2op\7v\2\2p\4")
        buf.write("\3\2\2\2qr\7x\2\2rs\7q\2\2st\7k\2\2tu\7f\2\2u\6\3\2\2")
        buf.write("\2vw\5;\36\2wx\5[.\2xy\5A!\2yz\59\35\2z{\5M\'\2{\b\3\2")
        buf.write("\2\2|}\5=\37\2}~\5U+\2~\177\5S*\2\177\u0080\5_\60\2\u0080")
        buf.write("\u0081\5I%\2\u0081\u0082\5S*\2\u0082\u0083\5a\61\2\u0083")
        buf.write("\u0084\5A!\2\u0084\n\3\2\2\2\u0085\u0086\5I%\2\u0086\u0087")
        buf.write("\5C\"\2\u0087\f\3\2\2\2\u0088\u0089\5A!\2\u0089\u008a")
        buf.write("\5O(\2\u008a\u008b\5]/\2\u008b\u008c\5A!\2\u008c\u008d")
        buf.write("\5I%\2\u008d\u008e\5C\"\2\u008e\16\3\2\2\2\u008f\u0090")
        buf.write("\5A!\2\u0090\u0091\5O(\2\u0091\u0092\5]/\2\u0092\u0093")
        buf.write("\5A!\2\u0093\20\3\2\2\2\u0094\u0095\5C\"\2\u0095\u0096")
        buf.write("\5U+\2\u0096\u0097\5[.\2\u0097\u0098\5A!\2\u0098\u0099")
        buf.write("\59\35\2\u0099\u009a\5=\37\2\u009a\u009b\5G$\2\u009b\22")
        buf.write("\3\2\2\2\u009c\u009d\5_\60\2\u009d\u009e\5[.\2\u009e\u009f")
        buf.write("\5a\61\2\u009f\u00a0\5A!\2\u00a0\24\3\2\2\2\u00a1\u00a2")
        buf.write("\5C\"\2\u00a2\u00a3\59\35\2\u00a3\u00a4\5O(\2\u00a4\u00a5")
        buf.write("\5]/\2\u00a5\u00a6\5A!\2\u00a6\26\3\2\2\2\u00a7\u00a8")
        buf.write("\59\35\2\u00a8\u00a9\5[.\2\u00a9\u00aa\5[.\2\u00aa\u00ab")
        buf.write("\59\35\2\u00ab\u00ac\5i\65\2\u00ac\u00ad\5I%\2\u00ad\u00ae")
        buf.write("\5S*\2\u00ae\u00af\5_\60\2\u00af\30\3\2\2\2\u00b0\u00b1")
        buf.write("\5C\"\2\u00b1\u00b2\5O(\2\u00b2\u00b3\5U+\2\u00b3\u00b4")
        buf.write("\59\35\2\u00b4\u00b5\5_\60\2\u00b5\32\3\2\2\2\u00b6\u00b7")
        buf.write("\5;\36\2\u00b7\u00b8\5U+\2\u00b8\u00b9\5U+\2\u00b9\u00ba")
        buf.write("\5O(\2\u00ba\u00bb\5A!\2\u00bb\u00bc\59\35\2\u00bc\u00bd")
        buf.write("\5S*\2\u00bd\34\3\2\2\2\u00be\u00bf\5]/\2\u00bf\u00c0")
        buf.write("\5_\60\2\u00c0\u00c1\5[.\2\u00c1\u00c2\5I%\2\u00c2\u00c3")
        buf.write("\5S*\2\u00c3\u00c4\5E#\2\u00c4\36\3\2\2\2\u00c5\u00c6")
        buf.write("\5S*\2\u00c6\u00c7\5a\61\2\u00c7\u00c8\5O(\2\u00c8\u00c9")
        buf.write("\5O(\2\u00c9 \3\2\2\2\u00ca\u00cd\5\23\n\2\u00cb\u00cd")
        buf.write("\5\25\13\2\u00cc\u00ca\3\2\2\2\u00cc\u00cb\3\2\2\2\u00cd")
        buf.write("\"\3\2\2\2\u00ce\u00d0\t\2\2\2\u00cf\u00ce\3\2\2\2\u00d0")
        buf.write("\u00d1\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2$\3\2\2\2\u00d3\u00d4\7*\2\2\u00d4&\3\2\2\2\u00d5")
        buf.write("\u00d6\7+\2\2\u00d6(\3\2\2\2\u00d7\u00d8\7}\2\2\u00d8")
        buf.write("*\3\2\2\2\u00d9\u00da\7\177\2\2\u00da,\3\2\2\2\u00db\u00dc")
        buf.write("\7=\2\2\u00dc.\3\2\2\2\u00dd\u00de\7,\2\2\u00de\u00df")
        buf.write("\7,\2\2\u00df\u00e3\3\2\2\2\u00e0\u00e2\13\2\2\2\u00e1")
        buf.write("\u00e0\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e4\3\2\2\2")
        buf.write("\u00e3\u00e1\3\2\2\2\u00e4\u00e6\3\2\2\2\u00e5\u00e3\3")
        buf.write("\2\2\2\u00e6\u00e7\7,\2\2\u00e7\u00e8\7,\2\2\u00e8\u00e9")
        buf.write("\3\2\2\2\u00e9\u00ea\b\30\2\2\u00ea\60\3\2\2\2\u00eb\u00ed")
        buf.write("\t\3\2\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00f0\3\2\2\2")
        buf.write("\u00f0\u00f1\b\31\2\2\u00f1\62\3\2\2\2\u00f2\u00f3\13")
        buf.write("\2\2\2\u00f3\64\3\2\2\2\u00f4\u00f5\13\2\2\2\u00f5\66")
        buf.write("\3\2\2\2\u00f6\u00f7\13\2\2\2\u00f78\3\2\2\2\u00f8\u00f9")
        buf.write("\t\4\2\2\u00f9:\3\2\2\2\u00fa\u00fb\t\5\2\2\u00fb<\3\2")
        buf.write("\2\2\u00fc\u00fd\t\6\2\2\u00fd>\3\2\2\2\u00fe\u00ff\t")
        buf.write("\7\2\2\u00ff@\3\2\2\2\u0100\u0101\t\b\2\2\u0101B\3\2\2")
        buf.write("\2\u0102\u0103\t\t\2\2\u0103D\3\2\2\2\u0104\u0105\t\n")
        buf.write("\2\2\u0105F\3\2\2\2\u0106\u0107\t\13\2\2\u0107H\3\2\2")
        buf.write("\2\u0108\u0109\t\f\2\2\u0109J\3\2\2\2\u010a\u010b\t\r")
        buf.write("\2\2\u010bL\3\2\2\2\u010c\u010d\t\16\2\2\u010dN\3\2\2")
        buf.write("\2\u010e\u010f\t\17\2\2\u010fP\3\2\2\2\u0110\u0111\t\20")
        buf.write("\2\2\u0111R\3\2\2\2\u0112\u0113\t\21\2\2\u0113T\3\2\2")
        buf.write("\2\u0114\u0115\t\22\2\2\u0115V\3\2\2\2\u0116\u0117\t\23")
        buf.write("\2\2\u0117X\3\2\2\2\u0118\u0119\t\24\2\2\u0119Z\3\2\2")
        buf.write("\2\u011a\u011b\t\25\2\2\u011b\\\3\2\2\2\u011c\u011d\t")
        buf.write("\26\2\2\u011d^\3\2\2\2\u011e\u011f\t\27\2\2\u011f`\3\2")
        buf.write("\2\2\u0120\u0121\t\30\2\2\u0121b\3\2\2\2\u0122\u0123\t")
        buf.write("\31\2\2\u0123d\3\2\2\2\u0124\u0125\t\32\2\2\u0125f\3\2")
        buf.write("\2\2\u0126\u0127\t\33\2\2\u0127h\3\2\2\2\u0128\u0129\t")
        buf.write("\34\2\2\u0129j\3\2\2\2\u012a\u012b\t\35\2\2\u012bl\3\2")
        buf.write("\2\2\7\2\u00cc\u00d1\u00e3\u00ee\3\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTTYPE = 1
    VOIDTYPE = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSEIF = 6
    ELSE = 7
    FOREACH = 8
    TRUE = 9
    FALSE = 10
    ARRAYINT = 11
    FLOAT = 12
    BOOLEAN = 13
    STRING = 14
    NULL = 15
    BOOLLIT = 16
    INTLIT = 17
    LB = 18
    RB = 19
    LP = 20
    RP = 21
    SEMI = 22
    BLOCK_COMMENT = 23
    WS = 24
    ERROR_CHAR = 25
    UNCLOSE_STRING = 26
    ILLEGAL_ESCAPE = 27

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAYINT", "FLOAT", "BOOLEAN", 
            "STRING", "NULL", "BOOLLIT", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "BLOCK_COMMENT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "INTTYPE", "VOIDTYPE", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAYINT", "FLOAT", 
                  "BOOLEAN", "STRING", "NULL", "BOOLLIT", "INTLIT", "LB", 
                  "RB", "LP", "RP", "SEMI", "BLOCK_COMMENT", "WS", "ERROR_CHAR", 
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


