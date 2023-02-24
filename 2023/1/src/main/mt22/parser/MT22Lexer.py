# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0282\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%")
        buf.write("\3&\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3")
        buf.write("+\3,\3,\3,\3-\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3")
        buf.write("\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\39\39\3:\3:\3;\3;\7;\u01c1\n;\f;\16;\u01c4")
        buf.write("\13;\3<\3<\3<\3<\3<\3<\3<\3<\3<\5<\u01cf\n<\3=\3=\7=\u01d3")
        buf.write("\n=\f=\16=\u01d6\13=\3>\3>\3>\5>\u01db\n>\3>\7>\u01de")
        buf.write("\n>\f>\16>\u01e1\13>\3>\3>\7>\u01e5\n>\f>\16>\u01e8\13")
        buf.write(">\3>\6>\u01eb\n>\r>\16>\u01ec\5>\u01ef\n>\3?\3?\5?\u01f3")
        buf.write("\n?\3?\3?\3?\3?\3?\3?\3?\5?\u01fc\n?\3?\3?\3?\3?\3?\3")
        buf.write("?\5?\u0204\n?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u020f\n?\3")
        buf.write("?\3?\3@\3@\7@\u0215\n@\f@\16@\u0218\13@\3@\3@\7@\u021c")
        buf.write("\n@\f@\16@\u021f\13@\3A\3A\3A\3A\5A\u0225\nA\3B\3B\7B")
        buf.write("\u0229\nB\fB\16B\u022c\13B\3B\3B\3B\3C\3C\7C\u0233\nC")
        buf.write("\fC\16C\u0236\13C\3C\3C\3C\7C\u023b\nC\fC\16C\u023e\13")
        buf.write("C\3C\5C\u0241\nC\3C\5C\u0244\nC\3D\3D\7D\u0248\nD\fD\16")
        buf.write("D\u024b\13D\3D\3D\3D\3E\3E\3E\3E\5E\u0254\nE\3F\3F\3F")
        buf.write("\3G\3G\3G\5G\u025c\nG\3H\6H\u025f\nH\rH\16H\u0260\3H\3")
        buf.write("H\3I\3I\3I\3I\7I\u0269\nI\fI\16I\u026c\13I\3I\3I\3I\3")
        buf.write("I\3I\3J\3J\3J\3J\7J\u0277\nJ\fJ\16J\u027a\13J\3J\3J\3")
        buf.write("K\3K\3K\3L\3L\3\u026a\2M\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?\2A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62")
        buf.write("e\63g\64i\65k\66m\67o8q9s:u;w<y\2{\2}=\177\2\u0081>\u0083")
        buf.write("?\u0085@\u0087A\u0089\2\u008b\2\u008d\2\u008fB\u0091C")
        buf.write("\u0093D\u0095E\u0097\2\3\2\f\5\2C\\aac|\6\2\62;C\\aac")
        buf.write("|\3\2\62;\3\2\63;\3\3\f\f\6\2\f\f\16\17$$^^\t\2))^^dd")
        buf.write("hhppttvv\5\2\n\f\16\17\"\"\4\2\f\f\17\17\4\2GGgg\2\u0297")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2\2\u0081\3\2")
        buf.write("\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2")
        buf.write("\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u0099\3\2\2\2\5\u009e\3\2\2\2\7\u00a7\3\2\2")
        buf.write("\2\t\u00b3\3\2\2\2\13\u00c0\3\2\2\2\r\u00ca\3\2\2\2\17")
        buf.write("\u00d5\3\2\2\2\21\u00e1\3\2\2\2\23\u00ee\3\2\2\2\25\u00f9")
        buf.write("\3\2\2\2\27\u0105\3\2\2\2\31\u010b\3\2\2\2\33\u011a\3")
        buf.write("\2\2\2\35\u011f\3\2\2\2\37\u0125\3\2\2\2!\u0128\3\2\2")
        buf.write("\2#\u012d\3\2\2\2%\u0131\3\2\2\2\'\u0134\3\2\2\2)\u013b")
        buf.write("\3\2\2\2+\u0141\3\2\2\2-\u0145\3\2\2\2/\u014e\3\2\2\2")
        buf.write("\61\u0151\3\2\2\2\63\u0159\3\2\2\2\65\u015f\3\2\2\2\67")
        buf.write("\u0167\3\2\2\29\u016d\3\2\2\2;\u0175\3\2\2\2=\u017c\3")
        buf.write("\2\2\2?\u0181\3\2\2\2A\u0183\3\2\2\2C\u0185\3\2\2\2E\u0187")
        buf.write("\3\2\2\2G\u0189\3\2\2\2I\u018b\3\2\2\2K\u018d\3\2\2\2")
        buf.write("M\u018f\3\2\2\2O\u0192\3\2\2\2Q\u0195\3\2\2\2S\u0198\3")
        buf.write("\2\2\2U\u019b\3\2\2\2W\u019e\3\2\2\2Y\u01a1\3\2\2\2[\u01a4")
        buf.write("\3\2\2\2]\u01a6\3\2\2\2_\u01a8\3\2\2\2a\u01aa\3\2\2\2")
        buf.write("c\u01ac\3\2\2\2e\u01ae\3\2\2\2g\u01b0\3\2\2\2i\u01b2\3")
        buf.write("\2\2\2k\u01b4\3\2\2\2m\u01b6\3\2\2\2o\u01b8\3\2\2\2q\u01ba")
        buf.write("\3\2\2\2s\u01bc\3\2\2\2u\u01be\3\2\2\2w\u01ce\3\2\2\2")
        buf.write("y\u01d0\3\2\2\2{\u01d7\3\2\2\2}\u020e\3\2\2\2\177\u0212")
        buf.write("\3\2\2\2\u0081\u0224\3\2\2\2\u0083\u0226\3\2\2\2\u0085")
        buf.write("\u0243\3\2\2\2\u0087\u0245\3\2\2\2\u0089\u0253\3\2\2\2")
        buf.write("\u008b\u0255\3\2\2\2\u008d\u025b\3\2\2\2\u008f\u025e\3")
        buf.write("\2\2\2\u0091\u0264\3\2\2\2\u0093\u0272\3\2\2\2\u0095\u027d")
        buf.write("\3\2\2\2\u0097\u0280\3\2\2\2\u0099\u009a\7o\2\2\u009a")
        buf.write("\u009b\7c\2\2\u009b\u009c\7k\2\2\u009c\u009d\7p\2\2\u009d")
        buf.write("\4\3\2\2\2\u009e\u009f\7h\2\2\u009f\u00a0\7w\2\2\u00a0")
        buf.write("\u00a1\7p\2\2\u00a1\u00a2\7e\2\2\u00a2\u00a3\7v\2\2\u00a3")
        buf.write("\u00a4\7k\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6\7p\2\2\u00a6")
        buf.write("\6\3\2\2\2\u00a7\u00a8\7t\2\2\u00a8\u00a9\7g\2\2\u00a9")
        buf.write("\u00aa\7c\2\2\u00aa\u00ab\7f\2\2\u00ab\u00ac\7K\2\2\u00ac")
        buf.write("\u00ad\7p\2\2\u00ad\u00ae\7v\2\2\u00ae\u00af\7g\2\2\u00af")
        buf.write("\u00b0\7i\2\2\u00b0\u00b1\7g\2\2\u00b1\u00b2\7t\2\2\u00b2")
        buf.write("\b\3\2\2\2\u00b3\u00b4\7r\2\2\u00b4\u00b5\7t\2\2\u00b5")
        buf.write("\u00b6\7k\2\2\u00b6\u00b7\7p\2\2\u00b7\u00b8\7v\2\2\u00b8")
        buf.write("\u00b9\7K\2\2\u00b9\u00ba\7p\2\2\u00ba\u00bb\7v\2\2\u00bb")
        buf.write("\u00bc\7g\2\2\u00bc\u00bd\7i\2\2\u00bd\u00be\7g\2\2\u00be")
        buf.write("\u00bf\7t\2\2\u00bf\n\3\2\2\2\u00c0\u00c1\7t\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\u00c3\7c\2\2\u00c3\u00c4\7f\2\2\u00c4")
        buf.write("\u00c5\7H\2\2\u00c5\u00c6\7n\2\2\u00c6\u00c7\7q\2\2\u00c7")
        buf.write("\u00c8\7c\2\2\u00c8\u00c9\7v\2\2\u00c9\f\3\2\2\2\u00ca")
        buf.write("\u00cb\7y\2\2\u00cb\u00cc\7t\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7v\2\2\u00ce\u00cf\7g\2\2\u00cf\u00d0\7H\2\2\u00d0")
        buf.write("\u00d1\7n\2\2\u00d1\u00d2\7q\2\2\u00d2\u00d3\7c\2\2\u00d3")
        buf.write("\u00d4\7v\2\2\u00d4\16\3\2\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\u00d7\7g\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7f\2\2\u00d9")
        buf.write("\u00da\7D\2\2\u00da\u00db\7q\2\2\u00db\u00dc\7q\2\2\u00dc")
        buf.write("\u00dd\7n\2\2\u00dd\u00de\7g\2\2\u00de\u00df\7c\2\2\u00df")
        buf.write("\u00e0\7p\2\2\u00e0\20\3\2\2\2\u00e1\u00e2\7r\2\2\u00e2")
        buf.write("\u00e3\7t\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\u00e7\7D\2\2\u00e7\u00e8\7q\2\2\u00e8")
        buf.write("\u00e9\7q\2\2\u00e9\u00ea\7n\2\2\u00ea\u00eb\7g\2\2\u00eb")
        buf.write("\u00ec\7c\2\2\u00ec\u00ed\7p\2\2\u00ed\22\3\2\2\2\u00ee")
        buf.write("\u00ef\7t\2\2\u00ef\u00f0\7g\2\2\u00f0\u00f1\7c\2\2\u00f1")
        buf.write("\u00f2\7f\2\2\u00f2\u00f3\7U\2\2\u00f3\u00f4\7v\2\2\u00f4")
        buf.write("\u00f5\7t\2\2\u00f5\u00f6\7k\2\2\u00f6\u00f7\7p\2\2\u00f7")
        buf.write("\u00f8\7i\2\2\u00f8\24\3\2\2\2\u00f9\u00fa\7r\2\2\u00fa")
        buf.write("\u00fb\7t\2\2\u00fb\u00fc\7k\2\2\u00fc\u00fd\7p\2\2\u00fd")
        buf.write("\u00fe\7v\2\2\u00fe\u00ff\7U\2\2\u00ff\u0100\7v\2\2\u0100")
        buf.write("\u0101\7t\2\2\u0101\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103")
        buf.write("\u0104\7i\2\2\u0104\26\3\2\2\2\u0105\u0106\7u\2\2\u0106")
        buf.write("\u0107\7w\2\2\u0107\u0108\7r\2\2\u0108\u0109\7g\2\2\u0109")
        buf.write("\u010a\7t\2\2\u010a\30\3\2\2\2\u010b\u010c\7r\2\2\u010c")
        buf.write("\u010d\7t\2\2\u010d\u010e\7g\2\2\u010e\u010f\7x\2\2\u010f")
        buf.write("\u0110\7g\2\2\u0110\u0111\7p\2\2\u0111\u0112\7v\2\2\u0112")
        buf.write("\u0113\7F\2\2\u0113\u0114\7g\2\2\u0114\u0115\7h\2\2\u0115")
        buf.write("\u0116\7c\2\2\u0116\u0117\7w\2\2\u0117\u0118\7n\2\2\u0118")
        buf.write("\u0119\7v\2\2\u0119\32\3\2\2\2\u011a\u011b\7c\2\2\u011b")
        buf.write("\u011c\7w\2\2\u011c\u011d\7v\2\2\u011d\u011e\7q\2\2\u011e")
        buf.write("\34\3\2\2\2\u011f\u0120\7d\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7g\2\2\u0122\u0123\7c\2\2\u0123\u0124\7m\2\2\u0124")
        buf.write("\36\3\2\2\2\u0125\u0126\7f\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write(" \3\2\2\2\u0128\u0129\7g\2\2\u0129\u012a\7n\2\2\u012a")
        buf.write("\u012b\7u\2\2\u012b\u012c\7g\2\2\u012c\"\3\2\2\2\u012d")
        buf.write("\u012e\7h\2\2\u012e\u012f\7q\2\2\u012f\u0130\7t\2\2\u0130")
        buf.write("$\3\2\2\2\u0131\u0132\7k\2\2\u0132\u0133\7h\2\2\u0133")
        buf.write("&\3\2\2\2\u0134\u0135\7t\2\2\u0135\u0136\7g\2\2\u0136")
        buf.write("\u0137\7v\2\2\u0137\u0138\7w\2\2\u0138\u0139\7t\2\2\u0139")
        buf.write("\u013a\7p\2\2\u013a(\3\2\2\2\u013b\u013c\7y\2\2\u013c")
        buf.write("\u013d\7j\2\2\u013d\u013e\7k\2\2\u013e\u013f\7n\2\2\u013f")
        buf.write("\u0140\7g\2\2\u0140*\3\2\2\2\u0141\u0142\7q\2\2\u0142")
        buf.write("\u0143\7w\2\2\u0143\u0144\7v\2\2\u0144,\3\2\2\2\u0145")
        buf.write("\u0146\7e\2\2\u0146\u0147\7q\2\2\u0147\u0148\7p\2\2\u0148")
        buf.write("\u0149\7v\2\2\u0149\u014a\7k\2\2\u014a\u014b\7p\2\2\u014b")
        buf.write("\u014c\7w\2\2\u014c\u014d\7g\2\2\u014d.\3\2\2\2\u014e")
        buf.write("\u014f\7q\2\2\u014f\u0150\7h\2\2\u0150\60\3\2\2\2\u0151")
        buf.write("\u0152\7k\2\2\u0152\u0153\7p\2\2\u0153\u0154\7j\2\2\u0154")
        buf.write("\u0155\7g\2\2\u0155\u0156\7t\2\2\u0156\u0157\7k\2\2\u0157")
        buf.write("\u0158\7v\2\2\u0158\62\3\2\2\2\u0159\u015a\7c\2\2\u015a")
        buf.write("\u015b\7t\2\2\u015b\u015c\7t\2\2\u015c\u015d\7c\2\2\u015d")
        buf.write("\u015e\7{\2\2\u015e\64\3\2\2\2\u015f\u0160\7d\2\2\u0160")
        buf.write("\u0161\7q\2\2\u0161\u0162\7q\2\2\u0162\u0163\7n\2\2\u0163")
        buf.write("\u0164\7g\2\2\u0164\u0165\7c\2\2\u0165\u0166\7p\2\2\u0166")
        buf.write("\66\3\2\2\2\u0167\u0168\7h\2\2\u0168\u0169\7n\2\2\u0169")
        buf.write("\u016a\7q\2\2\u016a\u016b\7c\2\2\u016b\u016c\7v\2\2\u016c")
        buf.write("8\3\2\2\2\u016d\u016e\7k\2\2\u016e\u016f\7p\2\2\u016f")
        buf.write("\u0170\7v\2\2\u0170\u0171\7g\2\2\u0171\u0172\7i\2\2\u0172")
        buf.write("\u0173\7g\2\2\u0173\u0174\7t\2\2\u0174:\3\2\2\2\u0175")
        buf.write("\u0176\7u\2\2\u0176\u0177\7v\2\2\u0177\u0178\7t\2\2\u0178")
        buf.write("\u0179\7k\2\2\u0179\u017a\7p\2\2\u017a\u017b\7i\2\2\u017b")
        buf.write("<\3\2\2\2\u017c\u017d\7x\2\2\u017d\u017e\7q\2\2\u017e")
        buf.write("\u017f\7k\2\2\u017f\u0180\7f\2\2\u0180>\3\2\2\2\u0181")
        buf.write("\u0182\7a\2\2\u0182@\3\2\2\2\u0183\u0184\7-\2\2\u0184")
        buf.write("B\3\2\2\2\u0185\u0186\7/\2\2\u0186D\3\2\2\2\u0187\u0188")
        buf.write("\7,\2\2\u0188F\3\2\2\2\u0189\u018a\7\61\2\2\u018aH\3\2")
        buf.write("\2\2\u018b\u018c\7\'\2\2\u018cJ\3\2\2\2\u018d\u018e\7")
        buf.write("#\2\2\u018eL\3\2\2\2\u018f\u0190\7(\2\2\u0190\u0191\7")
        buf.write("(\2\2\u0191N\3\2\2\2\u0192\u0193\7~\2\2\u0193\u0194\7")
        buf.write("~\2\2\u0194P\3\2\2\2\u0195\u0196\7?\2\2\u0196\u0197\7")
        buf.write("?\2\2\u0197R\3\2\2\2\u0198\u0199\7#\2\2\u0199\u019a\7")
        buf.write("?\2\2\u019aT\3\2\2\2\u019b\u019c\7<\2\2\u019c\u019d\7")
        buf.write("<\2\2\u019dV\3\2\2\2\u019e\u019f\7@\2\2\u019f\u01a0\7")
        buf.write("?\2\2\u01a0X\3\2\2\2\u01a1\u01a2\7>\2\2\u01a2\u01a3\7")
        buf.write("?\2\2\u01a3Z\3\2\2\2\u01a4\u01a5\7?\2\2\u01a5\\\3\2\2")
        buf.write("\2\u01a6\u01a7\7@\2\2\u01a7^\3\2\2\2\u01a8\u01a9\7>\2")
        buf.write("\2\u01a9`\3\2\2\2\u01aa\u01ab\7*\2\2\u01abb\3\2\2\2\u01ac")
        buf.write("\u01ad\7+\2\2\u01add\3\2\2\2\u01ae\u01af\7]\2\2\u01af")
        buf.write("f\3\2\2\2\u01b0\u01b1\7_\2\2\u01b1h\3\2\2\2\u01b2\u01b3")
        buf.write("\7}\2\2\u01b3j\3\2\2\2\u01b4\u01b5\7\177\2\2\u01b5l\3")
        buf.write("\2\2\2\u01b6\u01b7\7\60\2\2\u01b7n\3\2\2\2\u01b8\u01b9")
        buf.write("\7.\2\2\u01b9p\3\2\2\2\u01ba\u01bb\7<\2\2\u01bbr\3\2\2")
        buf.write("\2\u01bc\u01bd\7=\2\2\u01bdt\3\2\2\2\u01be\u01c2\t\2\2")
        buf.write("\2\u01bf\u01c1\t\3\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("v\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7v\2\2\u01c6")
        buf.write("\u01c7\7t\2\2\u01c7\u01c8\7w\2\2\u01c8\u01cf\7g\2\2\u01c9")
        buf.write("\u01ca\7h\2\2\u01ca\u01cb\7c\2\2\u01cb\u01cc\7n\2\2\u01cc")
        buf.write("\u01cd\7u\2\2\u01cd\u01cf\7g\2\2\u01ce\u01c5\3\2\2\2\u01ce")
        buf.write("\u01c9\3\2\2\2\u01cfx\3\2\2\2\u01d0\u01d4\7\60\2\2\u01d1")
        buf.write("\u01d3\t\4\2\2\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2")
        buf.write("\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5z\3\2\2")
        buf.write("\2\u01d6\u01d4\3\2\2\2\u01d7\u01da\5\u0097L\2\u01d8\u01db")
        buf.write("\5C\"\2\u01d9\u01db\5A!\2\u01da\u01d8\3\2\2\2\u01da\u01d9")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01ee\3\2\2\2\u01dc")
        buf.write("\u01de\7\62\2\2\u01dd\u01dc\3\2\2\2\u01de\u01e1\3\2\2")
        buf.write("\2\u01df\u01dd\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e2")
        buf.write("\3\2\2\2\u01e1\u01df\3\2\2\2\u01e2\u01e6\t\5\2\2\u01e3")
        buf.write("\u01e5\t\4\2\2\u01e4\u01e3\3\2\2\2\u01e5\u01e8\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01ef\3")
        buf.write("\2\2\2\u01e8\u01e6\3\2\2\2\u01e9\u01eb\7\62\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u01ef\3\2\2\2\u01ee\u01df\3")
        buf.write("\2\2\2\u01ee\u01ea\3\2\2\2\u01ef|\3\2\2\2\u01f0\u01f3")
        buf.write("\5\177@\2\u01f1\u01f3\7\62\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\5y=\2\u01f5")
        buf.write("\u01f6\5{>\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\b?\2\2\u01f8")
        buf.write("\u020f\3\2\2\2\u01f9\u01fc\5\177@\2\u01fa\u01fc\7\62\2")
        buf.write("\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd")
        buf.write("\3\2\2\2\u01fd\u01fe\5y=\2\u01fe\u01ff\3\2\2\2\u01ff\u0200")
        buf.write("\b?\3\2\u0200\u020f\3\2\2\2\u0201\u0204\5\177@\2\u0202")
        buf.write("\u0204\7\62\2\2\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2")
        buf.write("\2\u0204\u0205\3\2\2\2\u0205\u0206\5{>\2\u0206\u0207\3")
        buf.write("\2\2\2\u0207\u0208\b?\4\2\u0208\u020f\3\2\2\2\u0209\u020a")
        buf.write("\5y=\2\u020a\u020b\5{>\2\u020b\u020c\3\2\2\2\u020c\u020d")
        buf.write("\b?\5\2\u020d\u020f\3\2\2\2\u020e\u01f2\3\2\2\2\u020e")
        buf.write("\u01fb\3\2\2\2\u020e\u0203\3\2\2\2\u020e\u0209\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0211\b?\6\2\u0211~\3\2\2\2")
        buf.write("\u0212\u021d\t\5\2\2\u0213\u0215\5? \2\u0214\u0213\3\2")
        buf.write("\2\2\u0215\u0218\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0216\3\2\2\2\u0219")
        buf.write("\u021c\t\4\2\2\u021a\u021c\t\4\2\2\u021b\u0216\3\2\2\2")
        buf.write("\u021b\u021a\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021d\u021e\3\2\2\2\u021e\u0080\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u0220\u0221\5\177@\2\u0221\u0222\bA\7\2\u0222")
        buf.write("\u0225\3\2\2\2\u0223\u0225\7\62\2\2\u0224\u0220\3\2\2")
        buf.write("\2\u0224\u0223\3\2\2\2\u0225\u0082\3\2\2\2\u0226\u022a")
        buf.write("\7$\2\2\u0227\u0229\5\u0089E\2\u0228\u0227\3\2\2\2\u0229")
        buf.write("\u022c\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2")
        buf.write("\u022b\u022d\3\2\2\2\u022c\u022a\3\2\2\2\u022d\u022e\7")
        buf.write("$\2\2\u022e\u022f\bB\b\2\u022f\u0084\3\2\2\2\u0230\u0234")
        buf.write("\7$\2\2\u0231\u0233\5\u0089E\2\u0232\u0231\3\2\2\2\u0233")
        buf.write("\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2")
        buf.write("\u0235\u0237\3\2\2\2\u0236\u0234\3\2\2\2\u0237\u0244\b")
        buf.write("C\t\2\u0238\u023c\7$\2\2\u0239\u023b\5\u0089E\2\u023a")
        buf.write("\u0239\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a\3\2\2\2")
        buf.write("\u023c\u023d\3\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023f\u0241\t\6\2\2\u0240\u023f\3\2\2\2\u0241\u0242")
        buf.write("\3\2\2\2\u0242\u0244\bC\n\2\u0243\u0230\3\2\2\2\u0243")
        buf.write("\u0238\3\2\2\2\u0244\u0086\3\2\2\2\u0245\u0249\7$\2\2")
        buf.write("\u0246\u0248\5\u0089E\2\u0247\u0246\3\2\2\2\u0248\u024b")
        buf.write("\3\2\2\2\u0249\u0247\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("\u024c\3\2\2\2\u024b\u0249\3\2\2\2\u024c\u024d\5\u008d")
        buf.write("G\2\u024d\u024e\bD\13\2\u024e\u0088\3\2\2\2\u024f\u0250")
        buf.write("\7^\2\2\u0250\u0254\7$\2\2\u0251\u0254\5\u008bF\2\u0252")
        buf.write("\u0254\n\7\2\2\u0253\u024f\3\2\2\2\u0253\u0251\3\2\2\2")
        buf.write("\u0253\u0252\3\2\2\2\u0254\u008a\3\2\2\2\u0255\u0256\7")
        buf.write("^\2\2\u0256\u0257\t\b\2\2\u0257\u008c\3\2\2\2\u0258\u0259")
        buf.write("\7^\2\2\u0259\u025c\n\b\2\2\u025a\u025c\7^\2\2\u025b\u0258")
        buf.write("\3\2\2\2\u025b\u025a\3\2\2\2\u025c\u008e\3\2\2\2\u025d")
        buf.write("\u025f\t\t\2\2\u025e\u025d\3\2\2\2\u025f\u0260\3\2\2\2")
        buf.write("\u0260\u025e\3\2\2\2\u0260\u0261\3\2\2\2\u0261\u0262\3")
        buf.write("\2\2\2\u0262\u0263\bH\f\2\u0263\u0090\3\2\2\2\u0264\u0265")
        buf.write("\7\61\2\2\u0265\u0266\7,\2\2\u0266\u026a\3\2\2\2\u0267")
        buf.write("\u0269\13\2\2\2\u0268\u0267\3\2\2\2\u0269\u026c\3\2\2")
        buf.write("\2\u026a\u026b\3\2\2\2\u026a\u0268\3\2\2\2\u026b\u026d")
        buf.write("\3\2\2\2\u026c\u026a\3\2\2\2\u026d\u026e\7,\2\2\u026e")
        buf.write("\u026f\7\61\2\2\u026f\u0270\3\2\2\2\u0270\u0271\bI\f\2")
        buf.write("\u0271\u0092\3\2\2\2\u0272\u0273\7\61\2\2\u0273\u0274")
        buf.write("\7\61\2\2\u0274\u0278\3\2\2\2\u0275\u0277\n\n\2\2\u0276")
        buf.write("\u0275\3\2\2\2\u0277\u027a\3\2\2\2\u0278\u0276\3\2\2\2")
        buf.write("\u0278\u0279\3\2\2\2\u0279\u027b\3\2\2\2\u027a\u0278\3")
        buf.write("\2\2\2\u027b\u027c\bJ\f\2\u027c\u0094\3\2\2\2\u027d\u027e")
        buf.write("\13\2\2\2\u027e\u027f\bK\r\2\u027f\u0096\3\2\2\2\u0280")
        buf.write("\u0281\t\13\2\2\u0281\u0098\3\2\2\2\36\2\u01c2\u01ce\u01d4")
        buf.write("\u01da\u01df\u01e6\u01ec\u01ee\u01f2\u01fb\u0203\u020e")
        buf.write("\u0216\u021b\u021d\u0224\u022a\u0234\u023c\u0240\u0243")
        buf.write("\u0249\u0253\u025b\u0260\u026a\u0278\16\3?\2\3?\3\3?\4")
        buf.write("\3?\5\3?\6\3A\7\3B\b\3C\t\3C\n\3D\13\b\2\2\3K\f")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN = 1
    FUNCTION = 2
    READ_INTEGER = 3
    PRINT_INTEGER = 4
    READ_FLOAT = 5
    WRITE_FLOAT = 6
    READ_BOOLEAN = 7
    PRINT_BOOLEAN = 8
    READ_STRING = 9
    PRINT_STRING = 10
    SUPER = 11
    PREVENT_DEFAULT = 12
    AUTO = 13
    BREAK = 14
    DO = 15
    ELSE = 16
    FOR = 17
    IF = 18
    RETURN = 19
    WHILE = 20
    OUT = 21
    CONTINUE = 22
    OF = 23
    INHERIT = 24
    ARRAY = 25
    BOOLEAN = 26
    FLOAT = 27
    INTEGER = 28
    STRING = 29
    VOID = 30
    PLUSOP = 31
    MINUSOP = 32
    MULTIPLYOP = 33
    DIVIDEOP = 34
    MODULOOP = 35
    NOTOP = 36
    ANDOP = 37
    OROP = 38
    EQUALOP = 39
    NOTEQUALOP = 40
    DOUBLECOLONOP = 41
    GTE = 42
    LTE = 43
    EQUAL = 44
    GT = 45
    LT = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    DOT = 53
    COMMA = 54
    COLON = 55
    SEMICOLON = 56
    VARIABLE_IDENTIFIERS = 57
    BOOLLIT = 58
    FLOATLIT = 59
    INTLIT = 60
    STRINGLIT = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    WS = 64
    BLOCK_CMT = 65
    LINE_CMT = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'function'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'writeFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'", "'auto'", "'break'", 
            "'do'", "'else'", "'for'", "'if'", "'return'", "'while'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'boolean'", "'float'", 
            "'integer'", "'string'", "'void'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", "'::'", "'>='", 
            "'<='", "'='", "'>'", "'<'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN", "FUNCTION", "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", 
            "WRITE_FLOAT", "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", 
            "PRINT_STRING", "SUPER", "PREVENT_DEFAULT", "AUTO", "BREAK", 
            "DO", "ELSE", "FOR", "IF", "RETURN", "WHILE", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "BOOLEAN", "FLOAT", "INTEGER", "STRING", 
            "VOID", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", 
            "NOTOP", "ANDOP", "OROP", "EQUALOP", "NOTEQUALOP", "DOUBLECOLONOP", 
            "GTE", "LTE", "EQUAL", "GT", "LT", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", "VARIABLE_IDENTIFIERS", 
            "BOOLLIT", "FLOATLIT", "INTLIT", "STRINGLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "WS", "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR" ]

    ruleNames = [ "MAIN", "FUNCTION", "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", 
                  "WRITE_FLOAT", "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", 
                  "PRINT_STRING", "SUPER", "PREVENT_DEFAULT", "AUTO", "BREAK", 
                  "DO", "ELSE", "FOR", "IF", "RETURN", "WHILE", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "BOOLEAN", "FLOAT", "INTEGER", 
                  "STRING", "VOID", "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", 
                  "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", 
                  "NOTEQUALOP", "DOUBLECOLONOP", "GTE", "LTE", "EQUAL", 
                  "GT", "LT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", 
                  "COMMA", "COLON", "SEMICOLON", "VARIABLE_IDENTIFIERS", 
                  "BOOLLIT", "DECIMALPART", "EXPONENTPART", "FLOATLIT", 
                  "DEC", "INTLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", "WS", "BLOCK_CMT", 
                  "LINE_CMT", "ERROR_CHAR", "E" ]

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
            actions[61] = self.FLOATLIT_action 
            actions[63] = self.INTLIT_action 
            actions[64] = self.STRINGLIT_action 
            actions[65] = self.UNCLOSE_STRING_action 
            actions[66] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 3:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 4:
            self.text = self.text.replace("_", "")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
            self.text = self.text.replace("_", "")
     

    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            	
            	self.text = str(self.text)[1:-1].replace('\"','"')

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	current = str(self.text)
            	raise UncloseString(current[1:])

     

        if actionIndex == 8:

            	Quynh = str(self.text)
            	index = Quynh.find('\n')
            	if index != -1:
            		raise UncloseString(Quynh[1:index - 1])
            	self.text = Quynh
            	raise UncloseString(self.text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
             raise ErrorToken(self.text) 
     


