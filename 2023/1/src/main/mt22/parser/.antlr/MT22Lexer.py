# Generated from d:\Github\Principle-of-Programming-Languages\2023\1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\6")
        buf.write("\31\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\3\3")
        buf.write("\3\3\4\6\4\21\n\4\r\4\16\4\22\3\4\3\4\3\5\3\5\3\5\2\2")
        buf.write("\6\3\3\5\4\7\5\t\6\3\2\3\5\2\n\f\16\17\"\"\2\31\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\3\13\3\2\2")
        buf.write("\2\5\r\3\2\2\2\7\20\3\2\2\2\t\26\3\2\2\2\13\f\13\2\2\2")
        buf.write("\f\4\3\2\2\2\r\16\13\2\2\2\16\6\3\2\2\2\17\21\t\2\2\2")
        buf.write("\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3\2\2\2\22\23\3\2\2")
        buf.write("\2\23\24\3\2\2\2\24\25\b\4\2\2\25\b\3\2\2\2\26\27\13\2")
        buf.write("\2\2\27\30\b\5\3\2\30\n\3\2\2\2\4\2\22\4\b\2\2\3\5\2")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    UNCLOSE_STRING = 1
    ILLEGAL_ESCAPE = 2
    WS = 3
    ERROR_CHAR = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    ruleNames = [ "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", "ERROR_CHAR" ]

    grammarFileName = "MT22.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             raise ErrorToken(self.text) 
     


