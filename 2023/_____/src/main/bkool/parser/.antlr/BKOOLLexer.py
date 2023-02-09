# Generated from d:\Github\Principle-of-Programming-Languages\2023\_____\src\main\bkool\parser\BKOOL.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\13")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\6\3\33")
        buf.write("\n\3\r\3\16\3\34\3\3\3\3\6\3!\n\3\r\3\16\3\"\3\3\3\3\3")
        buf.write("\3\5\3(\n\3\3\3\6\3+\n\3\r\3\16\3,\3\3\3\3\6\3\61\n\3")
        buf.write("\r\3\16\3\62\3\3\3\3\3\3\5\38\n\3\3\3\6\3;\n\3\r\3\16")
        buf.write("\3<\5\3?\n\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\6\3\7\6\7J")
        buf.write("\n\7\r\7\16\7K\3\7\3\7\3\b\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\2\2\f\3\2\5\3\7\4\t\5\13\6\r\7\17\b\21\t\23\n\25")
        buf.write("\13\3\2\5\3\2\62;\4\2--//\5\2\13\f\17\17\"\"\2`\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\3\27\3\2\2\2\5\32\3\2\2\2\7@\3\2\2\2\tB\3\2\2\2\13D\3")
        buf.write("\2\2\2\rI\3\2\2\2\17O\3\2\2\2\21R\3\2\2\2\23T\3\2\2\2")
        buf.write("\25V\3\2\2\2\27\30\t\2\2\2\30\4\3\2\2\2\31\33\t\2\2\2")
        buf.write("\32\31\3\2\2\2\33\34\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2")
        buf.write("\2\35>\3\2\2\2\36 \7\60\2\2\37!\5\3\2\2 \37\3\2\2\2!\"")
        buf.write("\3\2\2\2\" \3\2\2\2\"#\3\2\2\2#?\3\2\2\2$\'\7g\2\2%(\t")
        buf.write("\3\2\2&(\3\2\2\2\'%\3\2\2\2\'&\3\2\2\2(*\3\2\2\2)+\5\3")
        buf.write("\2\2*)\3\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-?\3\2\2\2")
        buf.write(".\60\7\60\2\2/\61\5\3\2\2\60/\3\2\2\2\61\62\3\2\2\2\62")
        buf.write("\60\3\2\2\2\62\63\3\2\2\2\63\64\3\2\2\2\64\67\7g\2\2\65")
        buf.write("8\t\3\2\2\668\3\2\2\2\67\65\3\2\2\2\67\66\3\2\2\28:\3")
        buf.write("\2\2\29;\5\3\2\2:9\3\2\2\2;<\3\2\2\2<:\3\2\2\2<=\3\2\2")
        buf.write("\2=?\3\2\2\2>\36\3\2\2\2>$\3\2\2\2>.\3\2\2\2?\6\3\2\2")
        buf.write("\2@A\7=\2\2A\b\3\2\2\2BC\7<\2\2C\n\3\2\2\2DE\7X\2\2EF")
        buf.write("\7c\2\2FG\7t\2\2G\f\3\2\2\2HJ\t\4\2\2IH\3\2\2\2JK\3\2")
        buf.write("\2\2KI\3\2\2\2KL\3\2\2\2LM\3\2\2\2MN\b\7\2\2N\16\3\2\2")
        buf.write("\2OP\13\2\2\2PQ\b\b\3\2Q\20\3\2\2\2RS\13\2\2\2S\22\3\2")
        buf.write("\2\2TU\13\2\2\2U\24\3\2\2\2VW\13\2\2\2W\26\3\2\2\2\f\2")
        buf.write("\34\"\',\62\67<>K\4\b\2\2\3\b\2")
        return buf.getvalue()


class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    SEMI = 2
    COLON = 3
    VAR = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8
    UNTERMINATED_COMMENT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "':'", "'Var'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DIGIT", "ID", "SEMI", "COLON", "VAR", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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
     


