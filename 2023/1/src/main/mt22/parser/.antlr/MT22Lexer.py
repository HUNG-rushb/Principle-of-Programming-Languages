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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u027d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!")
        buf.write("\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3/\3")
        buf.write("/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64")
        buf.write("\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3")
        buf.write(";\3<\3<\3=\3=\7=\u01d0\n=\f=\16=\u01d3\13=\3>\3>\5>\u01d7")
        buf.write("\n>\3?\3?\6?\u01db\n?\r?\16?\u01dc\3@\3@\3@\5@\u01e2\n")
        buf.write("@\3@\7@\u01e5\n@\f@\16@\u01e8\13@\3@\3@\7@\u01ec\n@\f")
        buf.write("@\16@\u01ef\13@\3@\6@\u01f2\n@\r@\16@\u01f3\5@\u01f6\n")
        buf.write("@\3A\3A\5A\u01fa\nA\3A\3A\3A\3A\3A\3A\3A\5A\u0203\nA\3")
        buf.write("A\3A\3A\3A\3A\3A\5A\u020b\nA\3A\3A\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\5A\u0216\nA\3A\3A\3B\3B\7B\u021c\nB\fB\16B\u021f\13")
        buf.write("B\3B\3B\7B\u0223\nB\fB\16B\u0226\13B\3C\3C\3C\3C\5C\u022c")
        buf.write("\nC\3D\3D\7D\u0230\nD\fD\16D\u0233\13D\3D\3D\3D\3E\3E")
        buf.write("\7E\u023a\nE\fE\16E\u023d\13E\3E\3E\3F\3F\7F\u0243\nF")
        buf.write("\fF\16F\u0246\13F\3F\3F\3F\3G\3G\3G\3G\5G\u024f\nG\3H")
        buf.write("\3H\3H\3I\3I\3I\5I\u0257\nI\3J\6J\u025a\nJ\rJ\16J\u025b")
        buf.write("\3J\3J\3K\3K\3K\3K\7K\u0264\nK\fK\16K\u0267\13K\3K\3K")
        buf.write("\3K\3K\3K\3L\3L\3L\3L\7L\u0272\nL\fL\16L\u0275\13L\3L")
        buf.write("\3L\3M\3M\3M\3N\3N\3\u0265\2O\3\3\5\4\7\5\t\6\13\7\r\b")
        buf.write("\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22")
        buf.write("#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\35")
        buf.write("9\36;\37= ?!A\"C\2E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61")
        buf.write("c\62e\63g\64i\65k\66m\67o8q9s:u;w<y={>}\2\177\2\u0081")
        buf.write("?\u0083\2\u0085@\u0087A\u0089B\u008bC\u008d\2\u008f\2")
        buf.write("\u0091\2\u0093D\u0095E\u0097F\u0099G\u009b\2\3\2\13\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\5\2\f\f$$^^\t")
        buf.write("\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\4\2\f\f\17\17\4\2G")
        buf.write("Ggg\2\u0290\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2")
        buf.write("\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2")
        buf.write("\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3")
        buf.write("\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g")
        buf.write("\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2")
        buf.write("q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2")
        buf.write("\2{\3\2\2\2\2\u0081\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3")
        buf.write("\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u0093\3\2\2\2")
        buf.write("\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u009d")
        buf.write("\3\2\2\2\5\u00a2\3\2\2\2\7\u00ab\3\2\2\2\t\u00b7\3\2\2")
        buf.write("\2\13\u00c4\3\2\2\2\r\u00ce\3\2\2\2\17\u00d9\3\2\2\2\21")
        buf.write("\u00e5\3\2\2\2\23\u00f2\3\2\2\2\25\u00fd\3\2\2\2\27\u0109")
        buf.write("\3\2\2\2\31\u010f\3\2\2\2\33\u011e\3\2\2\2\35\u0123\3")
        buf.write("\2\2\2\37\u0129\3\2\2\2!\u012c\3\2\2\2#\u0131\3\2\2\2")
        buf.write("%\u0135\3\2\2\2\'\u0138\3\2\2\2)\u013f\3\2\2\2+\u0145")
        buf.write("\3\2\2\2-\u0149\3\2\2\2/\u0152\3\2\2\2\61\u0155\3\2\2")
        buf.write("\2\63\u015d\3\2\2\2\65\u0163\3\2\2\2\67\u0168\3\2\2\2")
        buf.write("9\u016e\3\2\2\2;\u0176\3\2\2\2=\u017c\3\2\2\2?\u0184\3")
        buf.write("\2\2\2A\u018b\3\2\2\2C\u0190\3\2\2\2E\u0192\3\2\2\2G\u0194")
        buf.write("\3\2\2\2I\u0196\3\2\2\2K\u0198\3\2\2\2M\u019a\3\2\2\2")
        buf.write("O\u019c\3\2\2\2Q\u019e\3\2\2\2S\u01a1\3\2\2\2U\u01a4\3")
        buf.write("\2\2\2W\u01a7\3\2\2\2Y\u01aa\3\2\2\2[\u01ad\3\2\2\2]\u01b0")
        buf.write("\3\2\2\2_\u01b3\3\2\2\2a\u01b5\3\2\2\2c\u01b7\3\2\2\2")
        buf.write("e\u01b9\3\2\2\2g\u01bb\3\2\2\2i\u01bd\3\2\2\2k\u01bf\3")
        buf.write("\2\2\2m\u01c1\3\2\2\2o\u01c3\3\2\2\2q\u01c5\3\2\2\2s\u01c7")
        buf.write("\3\2\2\2u\u01c9\3\2\2\2w\u01cb\3\2\2\2y\u01cd\3\2\2\2")
        buf.write("{\u01d6\3\2\2\2}\u01d8\3\2\2\2\177\u01de\3\2\2\2\u0081")
        buf.write("\u0215\3\2\2\2\u0083\u0219\3\2\2\2\u0085\u022b\3\2\2\2")
        buf.write("\u0087\u022d\3\2\2\2\u0089\u0237\3\2\2\2\u008b\u0240\3")
        buf.write("\2\2\2\u008d\u024e\3\2\2\2\u008f\u0250\3\2\2\2\u0091\u0256")
        buf.write("\3\2\2\2\u0093\u0259\3\2\2\2\u0095\u025f\3\2\2\2\u0097")
        buf.write("\u026d\3\2\2\2\u0099\u0278\3\2\2\2\u009b\u027b\3\2\2\2")
        buf.write("\u009d\u009e\7o\2\2\u009e\u009f\7c\2\2\u009f\u00a0\7k")
        buf.write("\2\2\u00a0\u00a1\7p\2\2\u00a1\4\3\2\2\2\u00a2\u00a3\7")
        buf.write("h\2\2\u00a3\u00a4\7w\2\2\u00a4\u00a5\7p\2\2\u00a5\u00a6")
        buf.write("\7e\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9")
        buf.write("\7q\2\2\u00a9\u00aa\7p\2\2\u00aa\6\3\2\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7g\2\2\u00ad\u00ae\7c\2\2\u00ae\u00af")
        buf.write("\7f\2\2\u00af\u00b0\7K\2\2\u00b0\u00b1\7p\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7i\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\u00b6\7t\2\2\u00b6\b\3\2\2\2\u00b7\u00b8")
        buf.write("\7r\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb")
        buf.write("\7p\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7K\2\2\u00bd\u00be")
        buf.write("\7p\2\2\u00be\u00bf\7v\2\2\u00bf\u00c0\7g\2\2\u00c0\u00c1")
        buf.write("\7i\2\2\u00c1\u00c2\7g\2\2\u00c2\u00c3\7t\2\2\u00c3\n")
        buf.write("\3\2\2\2\u00c4\u00c5\7t\2\2\u00c5\u00c6\7g\2\2\u00c6\u00c7")
        buf.write("\7c\2\2\u00c7\u00c8\7f\2\2\u00c8\u00c9\7H\2\2\u00c9\u00ca")
        buf.write("\7n\2\2\u00ca\u00cb\7q\2\2\u00cb\u00cc\7c\2\2\u00cc\u00cd")
        buf.write("\7v\2\2\u00cd\f\3\2\2\2\u00ce\u00cf\7y\2\2\u00cf\u00d0")
        buf.write("\7t\2\2\u00d0\u00d1\7k\2\2\u00d1\u00d2\7v\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7H\2\2\u00d4\u00d5\7n\2\2\u00d5\u00d6")
        buf.write("\7q\2\2\u00d6\u00d7\7c\2\2\u00d7\u00d8\7v\2\2\u00d8\16")
        buf.write("\3\2\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7g\2\2\u00db\u00dc")
        buf.write("\7c\2\2\u00dc\u00dd\7f\2\2\u00dd\u00de\7D\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2")
        buf.write("\7g\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4\7p\2\2\u00e4\20")
        buf.write("\3\2\2\2\u00e5\u00e6\7r\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8")
        buf.write("\7k\2\2\u00e8\u00e9\7p\2\2\u00e9\u00ea\7v\2\2\u00ea\u00eb")
        buf.write("\7D\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u00f1")
        buf.write("\7p\2\2\u00f1\22\3\2\2\2\u00f2\u00f3\7t\2\2\u00f3\u00f4")
        buf.write("\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7f\2\2\u00f6\u00f7")
        buf.write("\7U\2\2\u00f7\u00f8\7v\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7k\2\2\u00fa\u00fb\7p\2\2\u00fb\u00fc\7i\2\2\u00fc\24")
        buf.write("\3\2\2\2\u00fd\u00fe\7r\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7U\2\2\u0103\u0104\7v\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108\7i\2\2\u0108\26")
        buf.write("\3\2\2\2\u0109\u010a\7u\2\2\u010a\u010b\7w\2\2\u010b\u010c")
        buf.write("\7r\2\2\u010c\u010d\7g\2\2\u010d\u010e\7t\2\2\u010e\30")
        buf.write("\3\2\2\2\u010f\u0110\7r\2\2\u0110\u0111\7t\2\2\u0111\u0112")
        buf.write("\7g\2\2\u0112\u0113\7x\2\2\u0113\u0114\7g\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7v\2\2\u0116\u0117\7F\2\2\u0117\u0118")
        buf.write("\7g\2\2\u0118\u0119\7h\2\2\u0119\u011a\7c\2\2\u011a\u011b")
        buf.write("\7w\2\2\u011b\u011c\7n\2\2\u011c\u011d\7v\2\2\u011d\32")
        buf.write("\3\2\2\2\u011e\u011f\7c\2\2\u011f\u0120\7w\2\2\u0120\u0121")
        buf.write("\7v\2\2\u0121\u0122\7q\2\2\u0122\34\3\2\2\2\u0123\u0124")
        buf.write("\7d\2\2\u0124\u0125\7t\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7c\2\2\u0127\u0128\7m\2\2\u0128\36\3\2\2\2\u0129\u012a")
        buf.write("\7f\2\2\u012a\u012b\7q\2\2\u012b \3\2\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d\u012e\7n\2\2\u012e\u012f\7u\2\2\u012f\u0130")
        buf.write("\7g\2\2\u0130\"\3\2\2\2\u0131\u0132\7h\2\2\u0132\u0133")
        buf.write("\7q\2\2\u0133\u0134\7t\2\2\u0134$\3\2\2\2\u0135\u0136")
        buf.write("\7k\2\2\u0136\u0137\7h\2\2\u0137&\3\2\2\2\u0138\u0139")
        buf.write("\7t\2\2\u0139\u013a\7g\2\2\u013a\u013b\7v\2\2\u013b\u013c")
        buf.write("\7w\2\2\u013c\u013d\7t\2\2\u013d\u013e\7p\2\2\u013e(\3")
        buf.write("\2\2\2\u013f\u0140\7y\2\2\u0140\u0141\7j\2\2\u0141\u0142")
        buf.write("\7k\2\2\u0142\u0143\7n\2\2\u0143\u0144\7g\2\2\u0144*\3")
        buf.write("\2\2\2\u0145\u0146\7q\2\2\u0146\u0147\7w\2\2\u0147\u0148")
        buf.write("\7v\2\2\u0148,\3\2\2\2\u0149\u014a\7e\2\2\u014a\u014b")
        buf.write("\7q\2\2\u014b\u014c\7p\2\2\u014c\u014d\7v\2\2\u014d\u014e")
        buf.write("\7k\2\2\u014e\u014f\7p\2\2\u014f\u0150\7w\2\2\u0150\u0151")
        buf.write("\7g\2\2\u0151.\3\2\2\2\u0152\u0153\7q\2\2\u0153\u0154")
        buf.write("\7h\2\2\u0154\60\3\2\2\2\u0155\u0156\7k\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157\u0158\7j\2\2\u0158\u0159\7g\2\2\u0159\u015a")
        buf.write("\7t\2\2\u015a\u015b\7k\2\2\u015b\u015c\7v\2\2\u015c\62")
        buf.write("\3\2\2\2\u015d\u015e\7c\2\2\u015e\u015f\7t\2\2\u015f\u0160")
        buf.write("\7t\2\2\u0160\u0161\7c\2\2\u0161\u0162\7{\2\2\u0162\64")
        buf.write("\3\2\2\2\u0163\u0164\7v\2\2\u0164\u0165\7t\2\2\u0165\u0166")
        buf.write("\7w\2\2\u0166\u0167\7g\2\2\u0167\66\3\2\2\2\u0168\u0169")
        buf.write("\7h\2\2\u0169\u016a\7c\2\2\u016a\u016b\7n\2\2\u016b\u016c")
        buf.write("\7u\2\2\u016c\u016d\7g\2\2\u016d8\3\2\2\2\u016e\u016f")
        buf.write("\7d\2\2\u016f\u0170\7q\2\2\u0170\u0171\7q\2\2\u0171\u0172")
        buf.write("\7n\2\2\u0172\u0173\7g\2\2\u0173\u0174\7c\2\2\u0174\u0175")
        buf.write("\7p\2\2\u0175:\3\2\2\2\u0176\u0177\7h\2\2\u0177\u0178")
        buf.write("\7n\2\2\u0178\u0179\7q\2\2\u0179\u017a\7c\2\2\u017a\u017b")
        buf.write("\7v\2\2\u017b<\3\2\2\2\u017c\u017d\7k\2\2\u017d\u017e")
        buf.write("\7p\2\2\u017e\u017f\7v\2\2\u017f\u0180\7g\2\2\u0180\u0181")
        buf.write("\7i\2\2\u0181\u0182\7g\2\2\u0182\u0183\7t\2\2\u0183>\3")
        buf.write("\2\2\2\u0184\u0185\7u\2\2\u0185\u0186\7v\2\2\u0186\u0187")
        buf.write("\7t\2\2\u0187\u0188\7k\2\2\u0188\u0189\7p\2\2\u0189\u018a")
        buf.write("\7i\2\2\u018a@\3\2\2\2\u018b\u018c\7x\2\2\u018c\u018d")
        buf.write("\7q\2\2\u018d\u018e\7k\2\2\u018e\u018f\7f\2\2\u018fB\3")
        buf.write("\2\2\2\u0190\u0191\7a\2\2\u0191D\3\2\2\2\u0192\u0193\7")
        buf.write("-\2\2\u0193F\3\2\2\2\u0194\u0195\7/\2\2\u0195H\3\2\2\2")
        buf.write("\u0196\u0197\7,\2\2\u0197J\3\2\2\2\u0198\u0199\7\61\2")
        buf.write("\2\u0199L\3\2\2\2\u019a\u019b\7\'\2\2\u019bN\3\2\2\2\u019c")
        buf.write("\u019d\7#\2\2\u019dP\3\2\2\2\u019e\u019f\7(\2\2\u019f")
        buf.write("\u01a0\7(\2\2\u01a0R\3\2\2\2\u01a1\u01a2\7~\2\2\u01a2")
        buf.write("\u01a3\7~\2\2\u01a3T\3\2\2\2\u01a4\u01a5\7?\2\2\u01a5")
        buf.write("\u01a6\7?\2\2\u01a6V\3\2\2\2\u01a7\u01a8\7#\2\2\u01a8")
        buf.write("\u01a9\7?\2\2\u01a9X\3\2\2\2\u01aa\u01ab\7<\2\2\u01ab")
        buf.write("\u01ac\7<\2\2\u01acZ\3\2\2\2\u01ad\u01ae\7@\2\2\u01ae")
        buf.write("\u01af\7?\2\2\u01af\\\3\2\2\2\u01b0\u01b1\7>\2\2\u01b1")
        buf.write("\u01b2\7?\2\2\u01b2^\3\2\2\2\u01b3\u01b4\7?\2\2\u01b4")
        buf.write("`\3\2\2\2\u01b5\u01b6\7@\2\2\u01b6b\3\2\2\2\u01b7\u01b8")
        buf.write("\7>\2\2\u01b8d\3\2\2\2\u01b9\u01ba\7*\2\2\u01baf\3\2\2")
        buf.write("\2\u01bb\u01bc\7+\2\2\u01bch\3\2\2\2\u01bd\u01be\7]\2")
        buf.write("\2\u01bej\3\2\2\2\u01bf\u01c0\7_\2\2\u01c0l\3\2\2\2\u01c1")
        buf.write("\u01c2\7}\2\2\u01c2n\3\2\2\2\u01c3\u01c4\7\177\2\2\u01c4")
        buf.write("p\3\2\2\2\u01c5\u01c6\7\60\2\2\u01c6r\3\2\2\2\u01c7\u01c8")
        buf.write("\7.\2\2\u01c8t\3\2\2\2\u01c9\u01ca\7<\2\2\u01cav\3\2\2")
        buf.write("\2\u01cb\u01cc\7=\2\2\u01ccx\3\2\2\2\u01cd\u01d1\t\2\2")
        buf.write("\2\u01ce\u01d0\t\3\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d3")
        buf.write("\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2")
        buf.write("z\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01d7\5\65\33\2\u01d5")
        buf.write("\u01d7\5\67\34\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2")
        buf.write("\2\u01d7|\3\2\2\2\u01d8\u01da\7\60\2\2\u01d9\u01db\t\4")
        buf.write("\2\2\u01da\u01d9\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd~\3\2\2\2\u01de\u01e1")
        buf.write("\5\u009bN\2\u01df\u01e2\5G$\2\u01e0\u01e2\5E#\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2\u01e1\u01e2\3\2\2\2")
        buf.write("\u01e2\u01f5\3\2\2\2\u01e3\u01e5\7\62\2\2\u01e4\u01e3")
        buf.write("\3\2\2\2\u01e5\u01e8\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e6")
        buf.write("\u01e7\3\2\2\2\u01e7\u01e9\3\2\2\2\u01e8\u01e6\3\2\2\2")
        buf.write("\u01e9\u01ed\t\5\2\2\u01ea\u01ec\t\4\2\2\u01eb\u01ea\3")
        buf.write("\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u01f6\3\2\2\2\u01ef\u01ed\3\2\2\2\u01f0")
        buf.write("\u01f2\7\62\2\2\u01f1\u01f0\3\2\2\2\u01f2\u01f3\3\2\2")
        buf.write("\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f6")
        buf.write("\3\2\2\2\u01f5\u01e6\3\2\2\2\u01f5\u01f1\3\2\2\2\u01f6")
        buf.write("\u0080\3\2\2\2\u01f7\u01fa\5\u0083B\2\u01f8\u01fa\7\62")
        buf.write("\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u01fc\5}?\2\u01fc\u01fd\5\177@\2\u01fd")
        buf.write("\u01fe\3\2\2\2\u01fe\u01ff\bA\2\2\u01ff\u0216\3\2\2\2")
        buf.write("\u0200\u0203\5\u0083B\2\u0201\u0203\7\62\2\2\u0202\u0200")
        buf.write("\3\2\2\2\u0202\u0201\3\2\2\2\u0203\u0204\3\2\2\2\u0204")
        buf.write("\u0205\5}?\2\u0205\u0206\3\2\2\2\u0206\u0207\bA\3\2\u0207")
        buf.write("\u0216\3\2\2\2\u0208\u020b\5\u0083B\2\u0209\u020b\7\62")
        buf.write("\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b\u020c")
        buf.write("\3\2\2\2\u020c\u020d\5\177@\2\u020d\u020e\3\2\2\2\u020e")
        buf.write("\u020f\bA\4\2\u020f\u0216\3\2\2\2\u0210\u0211\5}?\2\u0211")
        buf.write("\u0212\5\177@\2\u0212\u0213\3\2\2\2\u0213\u0214\bA\5\2")
        buf.write("\u0214\u0216\3\2\2\2\u0215\u01f9\3\2\2\2\u0215\u0202\3")
        buf.write("\2\2\2\u0215\u020a\3\2\2\2\u0215\u0210\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0218\bA\6\2\u0218\u0082\3\2\2\2\u0219")
        buf.write("\u0224\t\5\2\2\u021a\u021c\5C\"\2\u021b\u021a\3\2\2\2")
        buf.write("\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u0220\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0223")
        buf.write("\t\4\2\2\u0221\u0223\t\4\2\2\u0222\u021d\3\2\2\2\u0222")
        buf.write("\u0221\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0224\u0225\3\2\2\2\u0225\u0084\3\2\2\2\u0226\u0224\3")
        buf.write("\2\2\2\u0227\u0228\5\u0083B\2\u0228\u0229\bC\7\2\u0229")
        buf.write("\u022c\3\2\2\2\u022a\u022c\7\62\2\2\u022b\u0227\3\2\2")
        buf.write("\2\u022b\u022a\3\2\2\2\u022c\u0086\3\2\2\2\u022d\u0231")
        buf.write("\7$\2\2\u022e\u0230\5\u008dG\2\u022f\u022e\3\2\2\2\u0230")
        buf.write("\u0233\3\2\2\2\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2")
        buf.write("\u0232\u0234\3\2\2\2\u0233\u0231\3\2\2\2\u0234\u0235\7")
        buf.write("$\2\2\u0235\u0236\bD\b\2\u0236\u0088\3\2\2\2\u0237\u023b")
        buf.write("\7$\2\2\u0238\u023a\5\u008dG\2\u0239\u0238\3\2\2\2\u023a")
        buf.write("\u023d\3\2\2\2\u023b\u0239\3\2\2\2\u023b\u023c\3\2\2\2")
        buf.write("\u023c\u023e\3\2\2\2\u023d\u023b\3\2\2\2\u023e\u023f\b")
        buf.write("E\t\2\u023f\u008a\3\2\2\2\u0240\u0244\7$\2\2\u0241\u0243")
        buf.write("\5\u008dG\2\u0242\u0241\3\2\2\2\u0243\u0246\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0247\3\2\2\2")
        buf.write("\u0246\u0244\3\2\2\2\u0247\u0248\5\u0091I\2\u0248\u0249")
        buf.write("\bF\n\2\u0249\u008c\3\2\2\2\u024a\u024b\7^\2\2\u024b\u024f")
        buf.write("\7$\2\2\u024c\u024f\5\u008fH\2\u024d\u024f\n\6\2\2\u024e")
        buf.write("\u024a\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2")
        buf.write("\u024f\u008e\3\2\2\2\u0250\u0251\7^\2\2\u0251\u0252\t")
        buf.write("\7\2\2\u0252\u0090\3\2\2\2\u0253\u0254\7^\2\2\u0254\u0257")
        buf.write("\n\7\2\2\u0255\u0257\7^\2\2\u0256\u0253\3\2\2\2\u0256")
        buf.write("\u0255\3\2\2\2\u0257\u0092\3\2\2\2\u0258\u025a\t\b\2\2")
        buf.write("\u0259\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u0259\3")
        buf.write("\2\2\2\u025b\u025c\3\2\2\2\u025c\u025d\3\2\2\2\u025d\u025e")
        buf.write("\bJ\13\2\u025e\u0094\3\2\2\2\u025f\u0260\7\61\2\2\u0260")
        buf.write("\u0261\7,\2\2\u0261\u0265\3\2\2\2\u0262\u0264\13\2\2\2")
        buf.write("\u0263\u0262\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0266\3")
        buf.write("\2\2\2\u0265\u0263\3\2\2\2\u0266\u0268\3\2\2\2\u0267\u0265")
        buf.write("\3\2\2\2\u0268\u0269\7,\2\2\u0269\u026a\7\61\2\2\u026a")
        buf.write("\u026b\3\2\2\2\u026b\u026c\bK\13\2\u026c\u0096\3\2\2\2")
        buf.write("\u026d\u026e\7\61\2\2\u026e\u026f\7\61\2\2\u026f\u0273")
        buf.write("\3\2\2\2\u0270\u0272\n\t\2\2\u0271\u0270\3\2\2\2\u0272")
        buf.write("\u0275\3\2\2\2\u0273\u0271\3\2\2\2\u0273\u0274\3\2\2\2")
        buf.write("\u0274\u0276\3\2\2\2\u0275\u0273\3\2\2\2\u0276\u0277\b")
        buf.write("L\13\2\u0277\u0098\3\2\2\2\u0278\u0279\13\2\2\2\u0279")
        buf.write("\u027a\bM\f\2\u027a\u009a\3\2\2\2\u027b\u027c\t\n\2\2")
        buf.write("\u027c\u009c\3\2\2\2\33\2\u01d1\u01d6\u01dc\u01e1\u01e6")
        buf.write("\u01ed\u01f3\u01f5\u01f9\u0202\u020a\u0215\u021d\u0222")
        buf.write("\u0224\u022b\u0231\u023b\u0244\u024e\u0256\u025b\u0265")
        buf.write("\u0273\r\3A\2\3A\3\3A\4\3A\5\3A\6\3C\7\3D\b\3E\t\3F\n")
        buf.write("\b\2\2\3M\13")
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
    TRUE = 26
    FALSE = 27
    BOOLEAN = 28
    FLOAT = 29
    INTEGER = 30
    STRING = 31
    VOID = 32
    PLUSOP = 33
    MINUSOP = 34
    MULTIPLYOP = 35
    DIVIDEOP = 36
    MODULOOP = 37
    NOTOP = 38
    ANDOP = 39
    OROP = 40
    EQUALOP = 41
    NOTEQUALOP = 42
    DOUBLECOLONOP = 43
    GTE = 44
    LTE = 45
    EQUAL = 46
    GT = 47
    LT = 48
    LB = 49
    RB = 50
    LSB = 51
    RSB = 52
    LCB = 53
    RCB = 54
    DOT = 55
    COMMA = 56
    COLON = 57
    SEMICOLON = 58
    VARIABLE_IDENTIFIERS = 59
    BOOLLIT = 60
    FLOATLIT = 61
    INTLIT = 62
    STRINGLIT = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    WS = 66
    BLOCK_CMT = 67
    LINE_CMT = 68
    ERROR_CHAR = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'function'", "'readInteger'", "'printInteger'", "'readFloat'", 
            "'writeFloat'", "'readBoolean'", "'printBoolean'", "'readString'", 
            "'printString'", "'super'", "'preventDefault'", "'auto'", "'break'", 
            "'do'", "'else'", "'for'", "'if'", "'return'", "'while'", "'out'", 
            "'continue'", "'of'", "'inherit'", "'array'", "'true'", "'false'", 
            "'boolean'", "'float'", "'integer'", "'string'", "'void'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'!='", 
            "'::'", "'>='", "'<='", "'='", "'>'", "'<'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "MAIN", "FUNCTION", "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", 
            "WRITE_FLOAT", "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", 
            "PRINT_STRING", "SUPER", "PREVENT_DEFAULT", "AUTO", "BREAK", 
            "DO", "ELSE", "FOR", "IF", "RETURN", "WHILE", "OUT", "CONTINUE", 
            "OF", "INHERIT", "ARRAY", "TRUE", "FALSE", "BOOLEAN", "FLOAT", 
            "INTEGER", "STRING", "VOID", "PLUSOP", "MINUSOP", "MULTIPLYOP", 
            "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", 
            "NOTEQUALOP", "DOUBLECOLONOP", "GTE", "LTE", "EQUAL", "GT", 
            "LT", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
            "COLON", "SEMICOLON", "VARIABLE_IDENTIFIERS", "BOOLLIT", "FLOATLIT", 
            "INTLIT", "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
            "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR" ]

    ruleNames = [ "MAIN", "FUNCTION", "READ_INTEGER", "PRINT_INTEGER", "READ_FLOAT", 
                  "WRITE_FLOAT", "READ_BOOLEAN", "PRINT_BOOLEAN", "READ_STRING", 
                  "PRINT_STRING", "SUPER", "PREVENT_DEFAULT", "AUTO", "BREAK", 
                  "DO", "ELSE", "FOR", "IF", "RETURN", "WHILE", "OUT", "CONTINUE", 
                  "OF", "INHERIT", "ARRAY", "TRUE", "FALSE", "BOOLEAN", 
                  "FLOAT", "INTEGER", "STRING", "VOID", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "NOTEQUALOP", "DOUBLECOLONOP", 
                  "GTE", "LTE", "EQUAL", "GT", "LT", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
                  "VARIABLE_IDENTIFIERS", "BOOLLIT", "DECIMALPART", "EXPONENTPART", 
                  "FLOATLIT", "DEC", "INTLIT", "STRINGLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", 
                  "WS", "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR", "E" ]

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
            actions[63] = self.FLOATLIT_action 
            actions[65] = self.INTLIT_action 
            actions[66] = self.STRINGLIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.ERROR_CHAR_action 
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

            	if str(self.text)[-1] == '"' and str(self.text)[-2] == '\'': 
            		if not str(self.text)[-3] == '\\':
            			raise UncloseString(str(self.text)[1:])
            	
            	
            	current = self.text.find('\n')
            	if current != -1: 
            		raise UncloseString(str(self.text[:current - 1]))

            	
            	self.text = str(self.text)[1:-1].replace('\\"','"')

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	current = str(self.text)
            	raise UncloseString(current[0:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            	current = str(self.text)
            	raise IllegalEscape(current[0:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
             raise ErrorToken(self.text) 
     


