# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("\u00b6\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\6\5c\n\5\r\5\16\5d\3")
        buf.write("\6\6\6h\n\6\r\6\16\6i\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\6\fw\n\f\r\f\16\fx\3\f\3\f\3\r\3\r\3\16")
        buf.write("\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\2\2*\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\2!\2#\2%")
        buf.write("\2\'\2)\2+\2-\2/\2\61\2\63\2\65\2\67\29\2;\2=\2?\2A\2")
        buf.write("C\2E\2G\2I\2K\2M\2O\2Q\2\3\2\37\4\2C\\c|\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4")
        buf.write("\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNn")
        buf.write("n\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2")
        buf.write("UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4")
        buf.write("\2\\\\||\2\u009e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3S\3\2\2\2\5X\3\2\2\2")
        buf.write("\7\\\3\2\2\2\tb\3\2\2\2\13g\3\2\2\2\rk\3\2\2\2\17m\3\2")
        buf.write("\2\2\21o\3\2\2\2\23q\3\2\2\2\25s\3\2\2\2\27v\3\2\2\2\31")
        buf.write("|\3\2\2\2\33~\3\2\2\2\35\u0080\3\2\2\2\37\u0082\3\2\2")
        buf.write("\2!\u0084\3\2\2\2#\u0086\3\2\2\2%\u0088\3\2\2\2\'\u008a")
        buf.write("\3\2\2\2)\u008c\3\2\2\2+\u008e\3\2\2\2-\u0090\3\2\2\2")
        buf.write("/\u0092\3\2\2\2\61\u0094\3\2\2\2\63\u0096\3\2\2\2\65\u0098")
        buf.write("\3\2\2\2\67\u009a\3\2\2\29\u009c\3\2\2\2;\u009e\3\2\2")
        buf.write("\2=\u00a0\3\2\2\2?\u00a2\3\2\2\2A\u00a4\3\2\2\2C\u00a6")
        buf.write("\3\2\2\2E\u00a8\3\2\2\2G\u00aa\3\2\2\2I\u00ac\3\2\2\2")
        buf.write("K\u00ae\3\2\2\2M\u00b0\3\2\2\2O\u00b2\3\2\2\2Q\u00b4\3")
        buf.write("\2\2\2ST\7o\2\2TU\7c\2\2UV\7k\2\2VW\7p\2\2W\4\3\2\2\2")
        buf.write("XY\7k\2\2YZ\7p\2\2Z[\7v\2\2[\6\3\2\2\2\\]\7x\2\2]^\7q")
        buf.write("\2\2^_\7k\2\2_`\7f\2\2`\b\3\2\2\2ac\t\2\2\2ba\3\2\2\2")
        buf.write("cd\3\2\2\2db\3\2\2\2de\3\2\2\2e\n\3\2\2\2fh\t\3\2\2gf")
        buf.write("\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\f\3\2\2\2kl\7")
        buf.write("*\2\2l\16\3\2\2\2mn\7+\2\2n\20\3\2\2\2op\7}\2\2p\22\3")
        buf.write("\2\2\2qr\7\177\2\2r\24\3\2\2\2st\7=\2\2t\26\3\2\2\2uw")
        buf.write("\t\4\2\2vu\3\2\2\2wx\3\2\2\2xv\3\2\2\2xy\3\2\2\2yz\3\2")
        buf.write("\2\2z{\b\f\2\2{\30\3\2\2\2|}\13\2\2\2}\32\3\2\2\2~\177")
        buf.write("\13\2\2\2\177\34\3\2\2\2\u0080\u0081\13\2\2\2\u0081\36")
        buf.write("\3\2\2\2\u0082\u0083\t\5\2\2\u0083 \3\2\2\2\u0084\u0085")
        buf.write("\t\6\2\2\u0085\"\3\2\2\2\u0086\u0087\t\7\2\2\u0087$\3")
        buf.write("\2\2\2\u0088\u0089\t\b\2\2\u0089&\3\2\2\2\u008a\u008b")
        buf.write("\t\t\2\2\u008b(\3\2\2\2\u008c\u008d\t\n\2\2\u008d*\3\2")
        buf.write("\2\2\u008e\u008f\t\13\2\2\u008f,\3\2\2\2\u0090\u0091\t")
        buf.write("\f\2\2\u0091.\3\2\2\2\u0092\u0093\t\r\2\2\u0093\60\3\2")
        buf.write("\2\2\u0094\u0095\t\16\2\2\u0095\62\3\2\2\2\u0096\u0097")
        buf.write("\t\17\2\2\u0097\64\3\2\2\2\u0098\u0099\t\20\2\2\u0099")
        buf.write("\66\3\2\2\2\u009a\u009b\t\21\2\2\u009b8\3\2\2\2\u009c")
        buf.write("\u009d\t\22\2\2\u009d:\3\2\2\2\u009e\u009f\t\23\2\2\u009f")
        buf.write("<\3\2\2\2\u00a0\u00a1\t\24\2\2\u00a1>\3\2\2\2\u00a2\u00a3")
        buf.write("\t\25\2\2\u00a3@\3\2\2\2\u00a4\u00a5\t\26\2\2\u00a5B\3")
        buf.write("\2\2\2\u00a6\u00a7\t\27\2\2\u00a7D\3\2\2\2\u00a8\u00a9")
        buf.write("\t\30\2\2\u00a9F\3\2\2\2\u00aa\u00ab\t\31\2\2\u00abH\3")
        buf.write("\2\2\2\u00ac\u00ad\t\32\2\2\u00adJ\3\2\2\2\u00ae\u00af")
        buf.write("\t\33\2\2\u00afL\3\2\2\2\u00b0\u00b1\t\34\2\2\u00b1N\3")
        buf.write("\2\2\2\u00b2\u00b3\t\35\2\2\u00b3P\3\2\2\2\u00b4\u00b5")
        buf.write("\t\36\2\2\u00b5R\3\2\2\2\6\2dix\3\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    ID = 4
    INTLIT = 5
    LB = 6
    RB = 7
    LP = 8
    RP = 9
    SEMI = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'('", "')'", "'{'", "'}'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", "LP", "RP", 
            "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "ID", "INTLIT", "LB", "RB", 
                  "LP", "RP", "SEMI", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "A", "B", "C", "D", "E", "F", "G", "H", 
                  "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", 
                  "T", "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


