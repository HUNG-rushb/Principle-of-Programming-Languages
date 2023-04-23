# Generated from d:\Github\Principle-of-Programming-Languages\2023\3\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2;")
        buf.write("\u01f7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u0141")
        buf.write("\n\61\3\62\3\62\7\62\u0145\n\62\f\62\16\62\u0148\13\62")
        buf.write("\3\63\3\63\7\63\u014c\n\63\f\63\16\63\u014f\13\63\3\64")
        buf.write("\3\64\3\64\5\64\u0154\n\64\3\64\7\64\u0157\n\64\f\64\16")
        buf.write("\64\u015a\13\64\3\64\3\64\7\64\u015e\n\64\f\64\16\64\u0161")
        buf.write("\13\64\3\64\6\64\u0164\n\64\r\64\16\64\u0165\5\64\u0168")
        buf.write("\n\64\3\65\3\65\5\65\u016c\n\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u0175\n\65\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\5\65\u017d\n\65\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\5\65\u0188\n\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\7\66\u0191\n\66\f\66\16\66\u0194\13\66\3\67")
        buf.write("\3\67\3\67\3\67\5\67\u019a\n\67\38\38\78\u019e\n8\f8\16")
        buf.write("8\u01a1\138\38\38\38\39\39\79\u01a8\n9\f9\169\u01ab\13")
        buf.write("9\39\39\39\79\u01b0\n9\f9\169\u01b3\139\39\59\u01b6\n")
        buf.write("9\39\59\u01b9\n9\3:\3:\7:\u01bd\n:\f:\16:\u01c0\13:\3")
        buf.write(":\3:\3:\3;\3;\3;\3;\5;\u01c9\n;\3<\3<\3<\3=\3=\3=\5=\u01d1")
        buf.write("\n=\3>\6>\u01d4\n>\r>\16>\u01d5\3>\3>\3?\3?\3?\3?\7?\u01de")
        buf.write("\n?\f?\16?\u01e1\13?\3?\3?\3?\3?\3?\3@\3@\3@\3@\7@\u01ec")
        buf.write("\n@\f@\16@\u01ef\13@\3@\3@\3A\3A\3A\3B\3B\3\u01df\2C\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\2-\27/\30\61")
        buf.write("\31\63\32\65\33\67\349\35;\36=\37? A!C\"E#G$I%K&M\'O(")
        buf.write("Q)S*U+W,Y-[.]/_\60a\61c\62e\2g\2i\63k\2m\64o\65q\66s\67")
        buf.write("u\2w\2y\2{8}9\177:\u0081;\u0083\2\3\2\f\5\2C\\aac|\6\2")
        buf.write("\62;C\\aac|\3\2\62;\3\2\63;\3\3\f\f\6\2\f\f\16\17$$^^")
        buf.write("\t\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\4\2\f\f\17\17\4\2")
        buf.write("GGgg\2\u020b\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2i\3\2\2\2\2m\3")
        buf.write("\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2{\3\2\2\2\2}")
        buf.write("\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\3\u0085\3\2\2\2")
        buf.write("\5\u008a\3\2\2\2\7\u0093\3\2\2\2\t\u0098\3\2\2\2\13\u009e")
        buf.write("\3\2\2\2\r\u00a1\3\2\2\2\17\u00a6\3\2\2\2\21\u00aa\3\2")
        buf.write("\2\2\23\u00ad\3\2\2\2\25\u00b4\3\2\2\2\27\u00ba\3\2\2")
        buf.write("\2\31\u00be\3\2\2\2\33\u00c7\3\2\2\2\35\u00ca\3\2\2\2")
        buf.write("\37\u00d2\3\2\2\2!\u00d8\3\2\2\2#\u00e0\3\2\2\2%\u00e6")
        buf.write("\3\2\2\2\'\u00ee\3\2\2\2)\u00f5\3\2\2\2+\u00fa\3\2\2\2")
        buf.write("-\u00fc\3\2\2\2/\u00fe\3\2\2\2\61\u0100\3\2\2\2\63\u0102")
        buf.write("\3\2\2\2\65\u0104\3\2\2\2\67\u0106\3\2\2\29\u0108\3\2")
        buf.write("\2\2;\u010b\3\2\2\2=\u010e\3\2\2\2?\u0111\3\2\2\2A\u0114")
        buf.write("\3\2\2\2C\u0117\3\2\2\2E\u011a\3\2\2\2G\u011d\3\2\2\2")
        buf.write("I\u011f\3\2\2\2K\u0121\3\2\2\2M\u0123\3\2\2\2O\u0125\3")
        buf.write("\2\2\2Q\u0127\3\2\2\2S\u0129\3\2\2\2U\u012b\3\2\2\2W\u012d")
        buf.write("\3\2\2\2Y\u012f\3\2\2\2[\u0131\3\2\2\2]\u0133\3\2\2\2")
        buf.write("_\u0135\3\2\2\2a\u0140\3\2\2\2c\u0142\3\2\2\2e\u0149\3")
        buf.write("\2\2\2g\u0150\3\2\2\2i\u0187\3\2\2\2k\u018b\3\2\2\2m\u0199")
        buf.write("\3\2\2\2o\u019b\3\2\2\2q\u01b8\3\2\2\2s\u01ba\3\2\2\2")
        buf.write("u\u01c8\3\2\2\2w\u01ca\3\2\2\2y\u01d0\3\2\2\2{\u01d3\3")
        buf.write("\2\2\2}\u01d9\3\2\2\2\177\u01e7\3\2\2\2\u0081\u01f2\3")
        buf.write("\2\2\2\u0083\u01f5\3\2\2\2\u0085\u0086\7o\2\2\u0086\u0087")
        buf.write("\7c\2\2\u0087\u0088\7k\2\2\u0088\u0089\7p\2\2\u0089\4")
        buf.write("\3\2\2\2\u008a\u008b\7h\2\2\u008b\u008c\7w\2\2\u008c\u008d")
        buf.write("\7p\2\2\u008d\u008e\7e\2\2\u008e\u008f\7v\2\2\u008f\u0090")
        buf.write("\7k\2\2\u0090\u0091\7q\2\2\u0091\u0092\7p\2\2\u0092\6")
        buf.write("\3\2\2\2\u0093\u0094\7c\2\2\u0094\u0095\7w\2\2\u0095\u0096")
        buf.write("\7v\2\2\u0096\u0097\7q\2\2\u0097\b\3\2\2\2\u0098\u0099")
        buf.write("\7d\2\2\u0099\u009a\7t\2\2\u009a\u009b\7g\2\2\u009b\u009c")
        buf.write("\7c\2\2\u009c\u009d\7m\2\2\u009d\n\3\2\2\2\u009e\u009f")
        buf.write("\7f\2\2\u009f\u00a0\7q\2\2\u00a0\f\3\2\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7n\2\2\u00a3\u00a4\7u\2\2\u00a4\u00a5")
        buf.write("\7g\2\2\u00a5\16\3\2\2\2\u00a6\u00a7\7h\2\2\u00a7\u00a8")
        buf.write("\7q\2\2\u00a8\u00a9\7t\2\2\u00a9\20\3\2\2\2\u00aa\u00ab")
        buf.write("\7k\2\2\u00ab\u00ac\7h\2\2\u00ac\22\3\2\2\2\u00ad\u00ae")
        buf.write("\7t\2\2\u00ae\u00af\7g\2\2\u00af\u00b0\7v\2\2\u00b0\u00b1")
        buf.write("\7w\2\2\u00b1\u00b2\7t\2\2\u00b2\u00b3\7p\2\2\u00b3\24")
        buf.write("\3\2\2\2\u00b4\u00b5\7y\2\2\u00b5\u00b6\7j\2\2\u00b6\u00b7")
        buf.write("\7k\2\2\u00b7\u00b8\7n\2\2\u00b8\u00b9\7g\2\2\u00b9\26")
        buf.write("\3\2\2\2\u00ba\u00bb\7q\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd")
        buf.write("\7v\2\2\u00bd\30\3\2\2\2\u00be\u00bf\7e\2\2\u00bf\u00c0")
        buf.write("\7q\2\2\u00c0\u00c1\7p\2\2\u00c1\u00c2\7v\2\2\u00c2\u00c3")
        buf.write("\7k\2\2\u00c3\u00c4\7p\2\2\u00c4\u00c5\7w\2\2\u00c5\u00c6")
        buf.write("\7g\2\2\u00c6\32\3\2\2\2\u00c7\u00c8\7q\2\2\u00c8\u00c9")
        buf.write("\7h\2\2\u00c9\34\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc")
        buf.write("\7p\2\2\u00cc\u00cd\7j\2\2\u00cd\u00ce\7g\2\2\u00ce\u00cf")
        buf.write("\7t\2\2\u00cf\u00d0\7k\2\2\u00d0\u00d1\7v\2\2\u00d1\36")
        buf.write("\3\2\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7t\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7{\2\2\u00d7 \3")
        buf.write("\2\2\2\u00d8\u00d9\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db")
        buf.write("\7q\2\2\u00db\u00dc\7n\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7c\2\2\u00de\u00df\7p\2\2\u00df\"\3\2\2\2\u00e0\u00e1")
        buf.write("\7h\2\2\u00e1\u00e2\7n\2\2\u00e2\u00e3\7q\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7v\2\2\u00e5$\3\2\2\2\u00e6\u00e7")
        buf.write("\7k\2\2\u00e7\u00e8\7p\2\2\u00e8\u00e9\7v\2\2\u00e9\u00ea")
        buf.write("\7g\2\2\u00ea\u00eb\7i\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed")
        buf.write("\7t\2\2\u00ed&\3\2\2\2\u00ee\u00ef\7u\2\2\u00ef\u00f0")
        buf.write("\7v\2\2\u00f0\u00f1\7t\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3")
        buf.write("\7p\2\2\u00f3\u00f4\7i\2\2\u00f4(\3\2\2\2\u00f5\u00f6")
        buf.write("\7x\2\2\u00f6\u00f7\7q\2\2\u00f7\u00f8\7k\2\2\u00f8\u00f9")
        buf.write("\7f\2\2\u00f9*\3\2\2\2\u00fa\u00fb\7a\2\2\u00fb,\3\2\2")
        buf.write("\2\u00fc\u00fd\7-\2\2\u00fd.\3\2\2\2\u00fe\u00ff\7/\2")
        buf.write("\2\u00ff\60\3\2\2\2\u0100\u0101\7,\2\2\u0101\62\3\2\2")
        buf.write("\2\u0102\u0103\7\61\2\2\u0103\64\3\2\2\2\u0104\u0105\7")
        buf.write("\'\2\2\u0105\66\3\2\2\2\u0106\u0107\7#\2\2\u01078\3\2")
        buf.write("\2\2\u0108\u0109\7(\2\2\u0109\u010a\7(\2\2\u010a:\3\2")
        buf.write("\2\2\u010b\u010c\7~\2\2\u010c\u010d\7~\2\2\u010d<\3\2")
        buf.write("\2\2\u010e\u010f\7?\2\2\u010f\u0110\7?\2\2\u0110>\3\2")
        buf.write("\2\2\u0111\u0112\7#\2\2\u0112\u0113\7?\2\2\u0113@\3\2")
        buf.write("\2\2\u0114\u0115\7<\2\2\u0115\u0116\7<\2\2\u0116B\3\2")
        buf.write("\2\2\u0117\u0118\7@\2\2\u0118\u0119\7?\2\2\u0119D\3\2")
        buf.write("\2\2\u011a\u011b\7>\2\2\u011b\u011c\7?\2\2\u011cF\3\2")
        buf.write("\2\2\u011d\u011e\7?\2\2\u011eH\3\2\2\2\u011f\u0120\7@")
        buf.write("\2\2\u0120J\3\2\2\2\u0121\u0122\7>\2\2\u0122L\3\2\2\2")
        buf.write("\u0123\u0124\7*\2\2\u0124N\3\2\2\2\u0125\u0126\7+\2\2")
        buf.write("\u0126P\3\2\2\2\u0127\u0128\7]\2\2\u0128R\3\2\2\2\u0129")
        buf.write("\u012a\7_\2\2\u012aT\3\2\2\2\u012b\u012c\7}\2\2\u012c")
        buf.write("V\3\2\2\2\u012d\u012e\7\177\2\2\u012eX\3\2\2\2\u012f\u0130")
        buf.write("\7\60\2\2\u0130Z\3\2\2\2\u0131\u0132\7.\2\2\u0132\\\3")
        buf.write("\2\2\2\u0133\u0134\7<\2\2\u0134^\3\2\2\2\u0135\u0136\7")
        buf.write("=\2\2\u0136`\3\2\2\2\u0137\u0138\7v\2\2\u0138\u0139\7")
        buf.write("t\2\2\u0139\u013a\7w\2\2\u013a\u0141\7g\2\2\u013b\u013c")
        buf.write("\7h\2\2\u013c\u013d\7c\2\2\u013d\u013e\7n\2\2\u013e\u013f")
        buf.write("\7u\2\2\u013f\u0141\7g\2\2\u0140\u0137\3\2\2\2\u0140\u013b")
        buf.write("\3\2\2\2\u0141b\3\2\2\2\u0142\u0146\t\2\2\2\u0143\u0145")
        buf.write("\t\3\2\2\u0144\u0143\3\2\2\2\u0145\u0148\3\2\2\2\u0146")
        buf.write("\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147d\3\2\2\2\u0148")
        buf.write("\u0146\3\2\2\2\u0149\u014d\7\60\2\2\u014a\u014c\t\4\2")
        buf.write("\2\u014b\u014a\3\2\2\2\u014c\u014f\3\2\2\2\u014d\u014b")
        buf.write("\3\2\2\2\u014d\u014e\3\2\2\2\u014ef\3\2\2\2\u014f\u014d")
        buf.write("\3\2\2\2\u0150\u0153\5\u0083B\2\u0151\u0154\5/\30\2\u0152")
        buf.write("\u0154\5-\27\2\u0153\u0151\3\2\2\2\u0153\u0152\3\2\2\2")
        buf.write("\u0153\u0154\3\2\2\2\u0154\u0167\3\2\2\2\u0155\u0157\7")
        buf.write("\62\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2\u0158")
        buf.write("\u0156\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015b\3\2\2\2")
        buf.write("\u015a\u0158\3\2\2\2\u015b\u015f\t\5\2\2\u015c\u015e\t")
        buf.write("\4\2\2\u015d\u015c\3\2\2\2\u015e\u0161\3\2\2\2\u015f\u015d")
        buf.write("\3\2\2\2\u015f\u0160\3\2\2\2\u0160\u0168\3\2\2\2\u0161")
        buf.write("\u015f\3\2\2\2\u0162\u0164\7\62\2\2\u0163\u0162\3\2\2")
        buf.write("\2\u0164\u0165\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166")
        buf.write("\3\2\2\2\u0166\u0168\3\2\2\2\u0167\u0158\3\2\2\2\u0167")
        buf.write("\u0163\3\2\2\2\u0168h\3\2\2\2\u0169\u016c\5k\66\2\u016a")
        buf.write("\u016c\7\62\2\2\u016b\u0169\3\2\2\2\u016b\u016a\3\2\2")
        buf.write("\2\u016c\u016d\3\2\2\2\u016d\u016e\5e\63\2\u016e\u016f")
        buf.write("\5g\64\2\u016f\u0170\3\2\2\2\u0170\u0171\b\65\2\2\u0171")
        buf.write("\u0188\3\2\2\2\u0172\u0175\5k\66\2\u0173\u0175\7\62\2")
        buf.write("\2\u0174\u0172\3\2\2\2\u0174\u0173\3\2\2\2\u0175\u0176")
        buf.write("\3\2\2\2\u0176\u0177\5e\63\2\u0177\u0178\3\2\2\2\u0178")
        buf.write("\u0179\b\65\3\2\u0179\u0188\3\2\2\2\u017a\u017d\5k\66")
        buf.write("\2\u017b\u017d\7\62\2\2\u017c\u017a\3\2\2\2\u017c\u017b")
        buf.write("\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\5g\64\2\u017f")
        buf.write("\u0180\3\2\2\2\u0180\u0181\b\65\4\2\u0181\u0188\3\2\2")
        buf.write("\2\u0182\u0183\5e\63\2\u0183\u0184\5g\64\2\u0184\u0185")
        buf.write("\3\2\2\2\u0185\u0186\b\65\5\2\u0186\u0188\3\2\2\2\u0187")
        buf.write("\u016b\3\2\2\2\u0187\u0174\3\2\2\2\u0187\u017c\3\2\2\2")
        buf.write("\u0187\u0182\3\2\2\2\u0188\u0189\3\2\2\2\u0189\u018a\b")
        buf.write("\65\6\2\u018aj\3\2\2\2\u018b\u0192\t\5\2\2\u018c\u018d")
        buf.write("\5+\26\2\u018d\u018e\t\4\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u0191\t\4\2\2\u0190\u018c\3\2\2\2\u0190\u018f\3\2\2\2")
        buf.write("\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2\u0192\u0193\3")
        buf.write("\2\2\2\u0193l\3\2\2\2\u0194\u0192\3\2\2\2\u0195\u0196")
        buf.write("\5k\66\2\u0196\u0197\b\67\7\2\u0197\u019a\3\2\2\2\u0198")
        buf.write("\u019a\7\62\2\2\u0199\u0195\3\2\2\2\u0199\u0198\3\2\2")
        buf.write("\2\u019an\3\2\2\2\u019b\u019f\7$\2\2\u019c\u019e\5u;\2")
        buf.write("\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3")
        buf.write("\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2\u01a1\u019f")
        buf.write("\3\2\2\2\u01a2\u01a3\7$\2\2\u01a3\u01a4\b8\b\2\u01a4p")
        buf.write("\3\2\2\2\u01a5\u01a9\7$\2\2\u01a6\u01a8\5u;\2\u01a7\u01a6")
        buf.write("\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2\u01ab\u01a9\3\2\2\2")
        buf.write("\u01ac\u01b9\b9\t\2\u01ad\u01b1\7$\2\2\u01ae\u01b0\5u")
        buf.write(";\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af")
        buf.write("\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write("\u01b1\3\2\2\2\u01b4\u01b6\t\6\2\2\u01b5\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b7\3\2\2\2\u01b7\u01b9\b9\n\2\u01b8\u01a5\3")
        buf.write("\2\2\2\u01b8\u01ad\3\2\2\2\u01b9r\3\2\2\2\u01ba\u01be")
        buf.write("\7$\2\2\u01bb\u01bd\5u;\2\u01bc\u01bb\3\2\2\2\u01bd\u01c0")
        buf.write("\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf")
        buf.write("\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\5y=\2\u01c2")
        buf.write("\u01c3\b:\13\2\u01c3t\3\2\2\2\u01c4\u01c5\7^\2\2\u01c5")
        buf.write("\u01c9\7$\2\2\u01c6\u01c9\5w<\2\u01c7\u01c9\n\7\2\2\u01c8")
        buf.write("\u01c4\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2\2")
        buf.write("\u01c9v\3\2\2\2\u01ca\u01cb\7^\2\2\u01cb\u01cc\t\b\2\2")
        buf.write("\u01ccx\3\2\2\2\u01cd\u01ce\7^\2\2\u01ce\u01d1\n\b\2\2")
        buf.write("\u01cf\u01d1\7^\2\2\u01d0\u01cd\3\2\2\2\u01d0\u01cf\3")
        buf.write("\2\2\2\u01d1z\3\2\2\2\u01d2\u01d4\t\t\2\2\u01d3\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8\b>\f\2")
        buf.write("\u01d8|\3\2\2\2\u01d9\u01da\7\61\2\2\u01da\u01db\7,\2")
        buf.write("\2\u01db\u01df\3\2\2\2\u01dc\u01de\13\2\2\2\u01dd\u01dc")
        buf.write("\3\2\2\2\u01de\u01e1\3\2\2\2\u01df\u01e0\3\2\2\2\u01df")
        buf.write("\u01dd\3\2\2\2\u01e0\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2")
        buf.write("\u01e2\u01e3\7,\2\2\u01e3\u01e4\7\61\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01e6\b?\f\2\u01e6~\3\2\2\2\u01e7\u01e8\7")
        buf.write("\61\2\2\u01e8\u01e9\7\61\2\2\u01e9\u01ed\3\2\2\2\u01ea")
        buf.write("\u01ec\n\n\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2")
        buf.write("\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3")
        buf.write("\2\2\2\u01ef\u01ed\3\2\2\2\u01f0\u01f1\b@\f\2\u01f1\u0080")
        buf.write("\3\2\2\2\u01f2\u01f3\13\2\2\2\u01f3\u01f4\bA\r\2\u01f4")
        buf.write("\u0082\3\2\2\2\u01f5\u01f6\t\13\2\2\u01f6\u0084\3\2\2")
        buf.write("\2\35\2\u0140\u0146\u014d\u0153\u0158\u015f\u0165\u0167")
        buf.write("\u016b\u0174\u017c\u0187\u0190\u0192\u0199\u019f\u01a9")
        buf.write("\u01b1\u01b5\u01b8\u01be\u01c8\u01d0\u01d5\u01df\u01ed")
        buf.write("\16\3\65\2\3\65\3\3\65\4\3\65\5\3\65\6\3\67\7\38\b\39")
        buf.write("\t\39\n\3:\13\b\2\2\3A\f")
        return buf.getvalue()


class MT22Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MAIN = 1
    FUNCTION = 2
    AUTO = 3
    BREAK = 4
    DO = 5
    ELSE = 6
    FOR = 7
    IF = 8
    RETURN = 9
    WHILE = 10
    OUT = 11
    CONTINUE = 12
    OF = 13
    INHERIT = 14
    ARRAY = 15
    BOOLEAN = 16
    FLOAT = 17
    INTEGER = 18
    STRING = 19
    VOID = 20
    PLUSOP = 21
    MINUSOP = 22
    MULTIPLYOP = 23
    DIVIDEOP = 24
    MODULOOP = 25
    NOTOP = 26
    ANDOP = 27
    OROP = 28
    EQUALOP = 29
    NOTEQUALOP = 30
    DOUBLECOLONOP = 31
    GTE = 32
    LTE = 33
    EQUAL = 34
    GT = 35
    LT = 36
    LB = 37
    RB = 38
    LSB = 39
    RSB = 40
    LCB = 41
    RCB = 42
    DOT = 43
    COMMA = 44
    COLON = 45
    SEMICOLON = 46
    BOOLLIT = 47
    VARIABLE_IDENTIFIERS = 48
    FLOATLIT = 49
    INTLIT = 50
    STRINGLIT = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53
    WS = 54
    BLOCK_CMT = 55
    LINE_CMT = 56
    ERROR_CHAR = 57

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'function'", "'auto'", "'break'", "'do'", "'else'", 
            "'for'", "'if'", "'return'", "'while'", "'out'", "'continue'", 
            "'of'", "'inherit'", "'array'", "'boolean'", "'float'", "'integer'", 
            "'string'", "'void'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'!='", "'::'", "'>='", "'<='", "'='", 
            "'>'", "'<'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
            "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN", "FUNCTION", "AUTO", "BREAK", "DO", "ELSE", "FOR", "IF", 
            "RETURN", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
            "BOOLEAN", "FLOAT", "INTEGER", "STRING", "VOID", "PLUSOP", "MINUSOP", 
            "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", "OROP", 
            "EQUALOP", "NOTEQUALOP", "DOUBLECOLONOP", "GTE", "LTE", "EQUAL", 
            "GT", "LT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
            "COLON", "SEMICOLON", "BOOLLIT", "VARIABLE_IDENTIFIERS", "FLOATLIT", 
            "INTLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
            "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR" ]

    ruleNames = [ "MAIN", "FUNCTION", "AUTO", "BREAK", "DO", "ELSE", "FOR", 
                  "IF", "RETURN", "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", 
                  "ARRAY", "BOOLEAN", "FLOAT", "INTEGER", "STRING", "VOID", 
                  "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                  "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", "NOTEQUALOP", 
                  "DOUBLECOLONOP", "GTE", "LTE", "EQUAL", "GT", "LT", "LB", 
                  "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", 
                  "SEMICOLON", "BOOLLIT", "VARIABLE_IDENTIFIERS", "DECIMALPART", 
                  "EXPONENTPART", "FLOATLIT", "DEC", "INTLIT", "STRINGLIT", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_CHAR", "ESC_CHAR", 
                  "ESC_UNAVAILABLE", "WS", "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR", 
                  "E" ]

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
            actions[51] = self.FLOATLIT_action 
            actions[53] = self.INTLIT_action 
            actions[54] = self.STRINGLIT_action 
            actions[55] = self.UNCLOSE_STRING_action 
            actions[56] = self.ILLEGAL_ESCAPE_action 
            actions[63] = self.ERROR_CHAR_action 
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
     


