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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("I\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\6\6\60\n\6\r\6\16\6\61\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\t\6\t<\n\t\r\t\16\t=\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\2\2\17\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\3\2\5\4\2C\\c|\5\2\13\f\17\17\"\"\3\2\62;\2J\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35")
        buf.write("\3\2\2\2\5\"\3\2\2\2\7$\3\2\2\2\t(\3\2\2\2\13/\3\2\2\2")
        buf.write("\r\63\3\2\2\2\17\67\3\2\2\2\21;\3\2\2\2\23?\3\2\2\2\25")
        buf.write("A\3\2\2\2\27C\3\2\2\2\31E\3\2\2\2\33G\3\2\2\2\35\36\7")
        buf.write("d\2\2\36\37\7q\2\2\37 \7f\2\2 !\7{\2\2!\4\3\2\2\2\"#\7")
        buf.write(".\2\2#\6\3\2\2\2$%\7k\2\2%&\7p\2\2&\'\7v\2\2\'\b\3\2\2")
        buf.write("\2()\7h\2\2)*\7n\2\2*+\7q\2\2+,\7c\2\2,-\7v\2\2-\n\3\2")
        buf.write("\2\2.\60\t\2\2\2/.\3\2\2\2\60\61\3\2\2\2\61/\3\2\2\2\61")
        buf.write("\62\3\2\2\2\62\f\3\2\2\2\63\64\t\3\2\2\64\65\3\2\2\2\65")
        buf.write("\66\b\7\2\2\66\16\3\2\2\2\678\13\2\2\289\b\b\3\29\20\3")
        buf.write("\2\2\2:<\t\4\2\2;:\3\2\2\2<=\3\2\2\2=;\3\2\2\2=>\3\2\2")
        buf.write("\2>\22\3\2\2\2?@\7*\2\2@\24\3\2\2\2AB\7+\2\2B\26\3\2\2")
        buf.write("\2CD\7}\2\2D\30\3\2\2\2EF\7\177\2\2F\32\3\2\2\2GH\7=\2")
        buf.write("\2H\34\3\2\2\2\5\2\61=\4\b\2\2\3\b\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    COM = 2
    INT = 3
    FLOAT = 4
    ID = 5
    WS = 6
    ERROR_CHAR = 7
    INTLIT = 8
    LB = 9
    RB = 10
    LP = 11
    RP = 12
    SEMI = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'body'", "','", "'int'", "'float'", "'('", "')'", "'{'", "'}'", 
            "';'" ]

    symbolicNames = [ "<INVALID>",
            "COM", "INT", "FLOAT", "ID", "WS", "ERROR_CHAR", "INTLIT", "LB", 
            "RB", "LP", "RP", "SEMI" ]

    ruleNames = [ "T__0", "COM", "INT", "FLOAT", "ID", "WS", "ERROR_CHAR", 
                  "INTLIT", "LB", "RB", "LP", "RP", "SEMI" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[6] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


