# Generated from d:\Github\Principle-of-Programming-Languages\2022\Midterm\midterm.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\3")
        buf.write("\27\b\1\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\5\2\16")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\2\2\4\3\2\5\3\3\2")
        buf.write("\4\3\2\62;\3\2\63;\2\27\2\5\3\2\2\2\3\r\3\2\2\2\5\17\3")
        buf.write("\2\2\2\7\16\t\2\2\2\b\t\t\3\2\2\t\16\t\2\2\2\n\13\t\3")
        buf.write("\2\2\13\f\t\2\2\2\f\16\t\2\2\2\r\7\3\2\2\2\r\b\3\2\2\2")
        buf.write("\r\n\3\2\2\2\16\4\3\2\2\2\17\20\5\3\2\2\20\21\7\60\2\2")
        buf.write("\21\22\5\3\2\2\22\23\7\60\2\2\23\24\5\3\2\2\24\25\7\60")
        buf.write("\2\2\25\26\5\3\2\2\26\6\3\2\2\2\4\2\r\2")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IP = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "IP" ]

    ruleNames = [ "M", "IP" ]

    grammarFileName = "midterm.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


