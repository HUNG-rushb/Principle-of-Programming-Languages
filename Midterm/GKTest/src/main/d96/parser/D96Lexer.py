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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("\63\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write("\7\4\b\t\b\4\t\t\t\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\b\6\b,\n\b\r\b\16\b-\3\t\3\t\3\t\3\t\2\2\n\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\3\2\4\4\2C\\c|\5\2\f\f\17")
        buf.write("\17\"\"\2\63\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\3\23\3\2\2\2\5\27\3\2\2\2\7\35\3\2\2\2\t\37\3\2\2")
        buf.write("\2\13!\3\2\2\2\r(\3\2\2\2\17+\3\2\2\2\21/\3\2\2\2\23\24")
        buf.write("\7k\2\2\24\25\7p\2\2\25\26\7v\2\2\26\4\3\2\2\2\27\30\7")
        buf.write("h\2\2\30\31\7n\2\2\31\32\7q\2\2\32\33\7c\2\2\33\34\7v")
        buf.write("\2\2\34\6\3\2\2\2\35\36\7B\2\2\36\b\3\2\2\2\37 \7.\2\2")
        buf.write(" \n\3\2\2\2!\"\7u\2\2\"#\7v\2\2#$\7c\2\2$%\7v\2\2%&\7")
        buf.write("k\2\2&\'\7e\2\2\'\f\3\2\2\2()\7=\2\2)\16\3\2\2\2*,\t\2")
        buf.write("\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\20\3\2\2")
        buf.write("\2/\60\t\3\2\2\60\61\3\2\2\2\61\62\b\t\2\2\62\22\3\2\2")
        buf.write("\2\4\2-\3\b\2\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    FLOAT = 2
    AT = 3
    CM = 4
    STATIC = 5
    SM = 6
    ID = 7
    WS = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'@'", "','", "'static'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "FLOAT", "AT", "CM", "STATIC", "SM", "ID", "WS" ]

    ruleNames = [ "INT", "FLOAT", "AT", "CM", "STATIC", "SM", "ID", "WS" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


