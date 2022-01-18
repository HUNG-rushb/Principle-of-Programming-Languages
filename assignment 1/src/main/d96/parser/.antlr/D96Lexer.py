# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u0267\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\5\n\u00d8\n\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\62\3\62\3\63")
        buf.write("\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\3")
        buf.write("9\39\3:\3:\3;\3;\6;\u018d\n;\r;\16;\u018e\3;\3;\7;\u0193")
        buf.write("\n;\f;\16;\u0196\13;\5;\u0198\n;\3<\3<\3=\3=\7=\u019e")
        buf.write("\n=\f=\16=\u01a1\13=\3=\3=\3=\3>\3>\7>\u01a8\n>\f>\16")
        buf.write(">\u01ab\13>\3>\5>\u01ae\n>\3?\3?\3?\5?\u01b3\n?\3?\7?")
        buf.write("\u01b6\n?\f?\16?\u01b9\13?\3?\3?\6?\u01bd\n?\r?\16?\u01be")
        buf.write("\5?\u01c1\n?\3@\3@\5@\u01c5\n@\3@\3@\3@\3@\3@\5@\u01cc")
        buf.write("\n@\3@\3@\3@\5@\u01d1\n@\3@\5@\u01d4\n@\3@\3@\3A\3A\3")
        buf.write("A\7A\u01db\nA\fA\16A\u01de\13A\3B\3B\3B\3B\6B\u01e4\n")
        buf.write("B\rB\16B\u01e5\5B\u01e8\nB\3B\3B\6B\u01ec\nB\rB\16B\u01ed")
        buf.write("\7B\u01f0\nB\fB\16B\u01f3\13B\3C\3C\3C\6C\u01f8\nC\rC")
        buf.write("\16C\u01f9\5C\u01fc\nC\3C\3C\6C\u0200\nC\rC\16C\u0201")
        buf.write("\7C\u0204\nC\fC\16C\u0207\13C\3D\3D\3D\3D\6D\u020d\nD")
        buf.write("\rD\16D\u020e\5D\u0211\nD\3D\3D\6D\u0215\nD\rD\16D\u0216")
        buf.write("\7D\u0219\nD\fD\16D\u021c\13D\3E\3E\3E\3E\5E\u0222\nE")
        buf.write("\3E\3E\3E\5E\u0227\nE\3F\3F\7F\u022b\nF\fF\16F\u022e\13")
        buf.write("F\3F\3F\3G\3G\7G\u0234\nG\fG\16G\u0237\13G\3G\3G\3G\3")
        buf.write("H\3H\3H\3H\5H\u0240\nH\3I\3I\3I\3J\3J\3J\5J\u0248\nJ\3")
        buf.write("K\3K\3K\3K\7K\u024e\nK\fK\16K\u0251\13K\3K\3K\3K\3K\3")
        buf.write("K\3L\6L\u0259\nL\rL\16L\u025a\3L\3L\3M\3M\3M\3N\3N\3O")
        buf.write("\3O\3P\3P\3\u024f\2Q\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write("\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37")
        buf.write("= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64")
        buf.write("g\65i\66k\67m8o9q:s;u<w\2y={\2}\2\177>\u0081\2\u0083\2")
        buf.write("\u0085\2\u0087\2\u0089?\u008b@\u008dA\u008f\2\u0091\2")
        buf.write("\u0093\2\u0095B\u0097C\u0099D\u009b\2\u009d\2\u009f\2")
        buf.write("\3\2\17\6\2\62;C\\aac|\5\2C\\aac|\3\2\63;\3\2\62;\5\2")
        buf.write("\62;CHch\3\2\629\3\2\62\63\4\2$$^^\t\2))^^ddhhppttvv\5")
        buf.write("\2\n\f\16\17\"\"\4\2DDdd\4\2GGgg\4\2ZZzz\2\u0283\2\3\3")
        buf.write("\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2")
        buf.write("\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2")
        buf.write("\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2")
        buf.write("\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2y\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u00a1\3\2\2")
        buf.write("\2\5\u00a6\3\2\2\2\7\u00af\3\2\2\2\t\u00b5\3\2\2\2\13")
        buf.write("\u00be\3\2\2\2\r\u00c1\3\2\2\2\17\u00c8\3\2\2\2\21\u00cd")
        buf.write("\3\2\2\2\23\u00d7\3\2\2\2\25\u00d9\3\2\2\2\27\u00de\3")
        buf.write("\2\2\2\31\u00e4\3\2\2\2\33\u00ea\3\2\2\2\35\u00ed\3\2")
        buf.write("\2\2\37\u00f1\3\2\2\2!\u00f7\3\2\2\2#\u00ff\3\2\2\2%\u0106")
        buf.write("\3\2\2\2\'\u010d\3\2\2\2)\u0112\3\2\2\2+\u0118\3\2\2\2")
        buf.write("-\u011c\3\2\2\2/\u0120\3\2\2\2\61\u012c\3\2\2\2\63\u0137")
        buf.write("\3\2\2\2\65\u013b\3\2\2\2\67\u013e\3\2\2\29\u0143\3\2")
        buf.write("\2\2;\u0146\3\2\2\2=\u0149\3\2\2\2?\u014b\3\2\2\2A\u014d")
        buf.write("\3\2\2\2C\u014f\3\2\2\2E\u0151\3\2\2\2G\u0153\3\2\2\2")
        buf.write("I\u0155\3\2\2\2K\u0157\3\2\2\2M\u015a\3\2\2\2O\u015d\3")
        buf.write("\2\2\2Q\u0160\3\2\2\2S\u0162\3\2\2\2U\u0165\3\2\2\2W\u0168")
        buf.write("\3\2\2\2Y\u016b\3\2\2\2[\u016d\3\2\2\2]\u016f\3\2\2\2")
        buf.write("_\u0173\3\2\2\2a\u0176\3\2\2\2c\u0178\3\2\2\2e\u017a\3")
        buf.write("\2\2\2g\u017c\3\2\2\2i\u017e\3\2\2\2k\u0180\3\2\2\2m\u0182")
        buf.write("\3\2\2\2o\u0184\3\2\2\2q\u0186\3\2\2\2s\u0188\3\2\2\2")
        buf.write("u\u0197\3\2\2\2w\u0199\3\2\2\2y\u019b\3\2\2\2{\u01a5\3")
        buf.write("\2\2\2}\u01af\3\2\2\2\177\u01d3\3\2\2\2\u0081\u01d7\3")
        buf.write("\2\2\2\u0083\u01df\3\2\2\2\u0085\u01f4\3\2\2\2\u0087\u0208")
        buf.write("\3\2\2\2\u0089\u0226\3\2\2\2\u008b\u0228\3\2\2\2\u008d")
        buf.write("\u0231\3\2\2\2\u008f\u023f\3\2\2\2\u0091\u0241\3\2\2\2")
        buf.write("\u0093\u0247\3\2\2\2\u0095\u0249\3\2\2\2\u0097\u0258\3")
        buf.write("\2\2\2\u0099\u025e\3\2\2\2\u009b\u0261\3\2\2\2\u009d\u0263")
        buf.write("\3\2\2\2\u009f\u0265\3\2\2\2\u00a1\u00a2\7c\2\2\u00a2")
        buf.write("\u00a3\7h\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7h\2\2\u00a5")
        buf.write("\4\3\2\2\2\u00a6\u00a7\7u\2\2\u00a7\u00a8\7f\2\2\u00a8")
        buf.write("\u00a9\7h\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7f\2\2\u00ab")
        buf.write("\u00ac\7h\2\2\u00ac\u00ad\7u\2\2\u00ad\u00ae\7c\2\2\u00ae")
        buf.write("\6\3\2\2\2\u00af\u00b0\7D\2\2\u00b0\u00b1\7t\2\2\u00b1")
        buf.write("\u00b2\7g\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7m\2\2\u00b4")
        buf.write("\b\3\2\2\2\u00b5\u00b6\7E\2\2\u00b6\u00b7\7q\2\2\u00b7")
        buf.write("\u00b8\7p\2\2\u00b8\u00b9\7v\2\2\u00b9\u00ba\7k\2\2\u00ba")
        buf.write("\u00bb\7p\2\2\u00bb\u00bc\7w\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\n\3\2\2\2\u00be\u00bf\7K\2\2\u00bf\u00c0\7h\2\2\u00c0")
        buf.write("\f\3\2\2\2\u00c1\u00c2\7G\2\2\u00c2\u00c3\7n\2\2\u00c3")
        buf.write("\u00c4\7u\2\2\u00c4\u00c5\7g\2\2\u00c5\u00c6\7k\2\2\u00c6")
        buf.write("\u00c7\7h\2\2\u00c7\16\3\2\2\2\u00c8\u00c9\7G\2\2\u00c9")
        buf.write("\u00ca\7n\2\2\u00ca\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc")
        buf.write("\20\3\2\2\2\u00cd\u00ce\7H\2\2\u00ce\u00cf\7q\2\2\u00cf")
        buf.write("\u00d0\7t\2\2\u00d0\u00d1\7g\2\2\u00d1\u00d2\7c\2\2\u00d2")
        buf.write("\u00d3\7e\2\2\u00d3\u00d4\7j\2\2\u00d4\22\3\2\2\2\u00d5")
        buf.write("\u00d8\5\25\13\2\u00d6\u00d8\5\27\f\2\u00d7\u00d5\3\2")
        buf.write("\2\2\u00d7\u00d6\3\2\2\2\u00d8\24\3\2\2\2\u00d9\u00da")
        buf.write("\7V\2\2\u00da\u00db\7t\2\2\u00db\u00dc\7w\2\2\u00dc\u00dd")
        buf.write("\7g\2\2\u00dd\26\3\2\2\2\u00de\u00df\7H\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7n\2\2\u00e1\u00e2\7u\2\2\u00e2\u00e3")
        buf.write("\7g\2\2\u00e3\30\3\2\2\2\u00e4\u00e5\7C\2\2\u00e5\u00e6")
        buf.write("\7t\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9")
        buf.write("\7{\2\2\u00e9\32\3\2\2\2\u00ea\u00eb\7K\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\34\3\2\2\2\u00ed\u00ee\7K\2\2\u00ee\u00ef")
        buf.write("\7p\2\2\u00ef\u00f0\7v\2\2\u00f0\36\3\2\2\2\u00f1\u00f2")
        buf.write("\7H\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7q\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7v\2\2\u00f6 \3\2\2\2\u00f7\u00f8")
        buf.write("\7D\2\2\u00f8\u00f9\7q\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb")
        buf.write("\7n\2\2\u00fb\u00fc\7g\2\2\u00fc\u00fd\7c\2\2\u00fd\u00fe")
        buf.write("\7p\2\2\u00fe\"\3\2\2\2\u00ff\u0100\7U\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7t\2\2\u0102\u0103\7k\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\u0105\7i\2\2\u0105$\3\2\2\2\u0106\u0107")
        buf.write("\7T\2\2\u0107\u0108\7g\2\2\u0108\u0109\7v\2\2\u0109\u010a")
        buf.write("\7w\2\2\u010a\u010b\7t\2\2\u010b\u010c\7p\2\2\u010c&\3")
        buf.write("\2\2\2\u010d\u010e\7P\2\2\u010e\u010f\7w\2\2\u010f\u0110")
        buf.write("\7n\2\2\u0110\u0111\7n\2\2\u0111(\3\2\2\2\u0112\u0113")
        buf.write("\7E\2\2\u0113\u0114\7n\2\2\u0114\u0115\7c\2\2\u0115\u0116")
        buf.write("\7u\2\2\u0116\u0117\7u\2\2\u0117*\3\2\2\2\u0118\u0119")
        buf.write("\7X\2\2\u0119\u011a\7c\2\2\u011a\u011b\7n\2\2\u011b,\3")
        buf.write("\2\2\2\u011c\u011d\7X\2\2\u011d\u011e\7c\2\2\u011e\u011f")
        buf.write("\7t\2\2\u011f.\3\2\2\2\u0120\u0121\7E\2\2\u0121\u0122")
        buf.write("\7q\2\2\u0122\u0123\7p\2\2\u0123\u0124\7u\2\2\u0124\u0125")
        buf.write("\7v\2\2\u0125\u0126\7t\2\2\u0126\u0127\7w\2\2\u0127\u0128")
        buf.write("\7e\2\2\u0128\u0129\7v\2\2\u0129\u012a\7q\2\2\u012a\u012b")
        buf.write("\7t\2\2\u012b\60\3\2\2\2\u012c\u012d\7F\2\2\u012d\u012e")
        buf.write("\7g\2\2\u012e\u012f\7u\2\2\u012f\u0130\7v\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131\u0132\7w\2\2\u0132\u0133\7e\2\2\u0133\u0134")
        buf.write("\7v\2\2\u0134\u0135\7q\2\2\u0135\u0136\7t\2\2\u0136\62")
        buf.write("\3\2\2\2\u0137\u0138\7P\2\2\u0138\u0139\7g\2\2\u0139\u013a")
        buf.write("\7y\2\2\u013a\64\3\2\2\2\u013b\u013c\7D\2\2\u013c\u013d")
        buf.write("\7{\2\2\u013d\66\3\2\2\2\u013e\u013f\7U\2\2\u013f\u0140")
        buf.write("\7g\2\2\u0140\u0141\7n\2\2\u0141\u0142\7h\2\2\u01428\3")
        buf.write("\2\2\2\u0143\u0144\7<\2\2\u0144\u0145\7<\2\2\u0145:\3")
        buf.write("\2\2\2\u0146\u0147\7\60\2\2\u0147\u0148\7\60\2\2\u0148")
        buf.write("<\3\2\2\2\u0149\u014a\7a\2\2\u014a>\3\2\2\2\u014b\u014c")
        buf.write("\7-\2\2\u014c@\3\2\2\2\u014d\u014e\7/\2\2\u014eB\3\2\2")
        buf.write("\2\u014f\u0150\7,\2\2\u0150D\3\2\2\2\u0151\u0152\7\61")
        buf.write("\2\2\u0152F\3\2\2\2\u0153\u0154\7\'\2\2\u0154H\3\2\2\2")
        buf.write("\u0155\u0156\7#\2\2\u0156J\3\2\2\2\u0157\u0158\7(\2\2")
        buf.write("\u0158\u0159\7(\2\2\u0159L\3\2\2\2\u015a\u015b\7~\2\2")
        buf.write("\u015b\u015c\7~\2\2\u015cN\3\2\2\2\u015d\u015e\7?\2\2")
        buf.write("\u015e\u015f\7?\2\2\u015fP\3\2\2\2\u0160\u0161\7?\2\2")
        buf.write("\u0161R\3\2\2\2\u0162\u0163\7#\2\2\u0163\u0164\7?\2\2")
        buf.write("\u0164T\3\2\2\2\u0165\u0166\7@\2\2\u0166\u0167\7?\2\2")
        buf.write("\u0167V\3\2\2\2\u0168\u0169\7>\2\2\u0169\u016a\7?\2\2")
        buf.write("\u016aX\3\2\2\2\u016b\u016c\7@\2\2\u016cZ\3\2\2\2\u016d")
        buf.write("\u016e\7>\2\2\u016e\\\3\2\2\2\u016f\u0170\7?\2\2\u0170")
        buf.write("\u0171\7?\2\2\u0171\u0172\7\60\2\2\u0172^\3\2\2\2\u0173")
        buf.write("\u0174\7-\2\2\u0174\u0175\7\60\2\2\u0175`\3\2\2\2\u0176")
        buf.write("\u0177\7*\2\2\u0177b\3\2\2\2\u0178\u0179\7+\2\2\u0179")
        buf.write("d\3\2\2\2\u017a\u017b\7]\2\2\u017bf\3\2\2\2\u017c\u017d")
        buf.write("\7_\2\2\u017dh\3\2\2\2\u017e\u017f\7}\2\2\u017fj\3\2\2")
        buf.write("\2\u0180\u0181\7\177\2\2\u0181l\3\2\2\2\u0182\u0183\7")
        buf.write("\60\2\2\u0183n\3\2\2\2\u0184\u0185\7.\2\2\u0185p\3\2\2")
        buf.write("\2\u0186\u0187\7<\2\2\u0187r\3\2\2\2\u0188\u0189\7=\2")
        buf.write("\2\u0189t\3\2\2\2\u018a\u018c\5w<\2\u018b\u018d\t\2\2")
        buf.write("\2\u018c\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0198\3\2\2\2\u0190")
        buf.write("\u0194\t\3\2\2\u0191\u0193\t\2\2\2\u0192\u0191\3\2\2\2")
        buf.write("\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2\u0194\u0195\3")
        buf.write("\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0197\u018a")
        buf.write("\3\2\2\2\u0197\u0190\3\2\2\2\u0198v\3\2\2\2\u0199\u019a")
        buf.write("\7&\2\2\u019ax\3\2\2\2\u019b\u019f\7$\2\2\u019c\u019e")
        buf.write("\5\u008fH\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3\2\2\2")
        buf.write("\u01a1\u019f\3\2\2\2\u01a2\u01a3\7$\2\2\u01a3\u01a4\b")
        buf.write("=\2\2\u01a4z\3\2\2\2\u01a5\u01a9\7\60\2\2\u01a6\u01a8")
        buf.write("\7\62\2\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9")
        buf.write("\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ad\3\2\2\2")
        buf.write("\u01ab\u01a9\3\2\2\2\u01ac\u01ae\5\u0081A\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae|\3\2\2\2\u01af\u01b2")
        buf.write("\5\u009dO\2\u01b0\u01b3\5A!\2\u01b1\u01b3\5? \2\u01b2")
        buf.write("\u01b0\3\2\2\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2")
        buf.write("\u01b3\u01c0\3\2\2\2\u01b4\u01b6\7\62\2\2\u01b5\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7")
        buf.write("\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3\2\2\2")
        buf.write("\u01ba\u01c1\5\u0081A\2\u01bb\u01bd\7\62\2\2\u01bc\u01bb")
        buf.write("\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01bc\3\2\2\2\u01be")
        buf.write("\u01bf\3\2\2\2\u01bf\u01c1\3\2\2\2\u01c0\u01b7\3\2\2\2")
        buf.write("\u01c0\u01bc\3\2\2\2\u01c1~\3\2\2\2\u01c2\u01c5\5\u0081")
        buf.write("A\2\u01c3\u01c5\7\62\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3")
        buf.write("\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\5{>\2\u01c7\u01c8")
        buf.write("\5}?\2\u01c8\u01d4\3\2\2\2\u01c9\u01cc\5\u0081A\2\u01ca")
        buf.write("\u01cc\7\62\2\2\u01cb\u01c9\3\2\2\2\u01cb\u01ca\3\2\2")
        buf.write("\2\u01cc\u01cd\3\2\2\2\u01cd\u01d4\5{>\2\u01ce\u01d1\5")
        buf.write("\u0081A\2\u01cf\u01d1\7\62\2\2\u01d0\u01ce\3\2\2\2\u01d0")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d4\5}?\2\u01d3")
        buf.write("\u01c4\3\2\2\2\u01d3\u01cb\3\2\2\2\u01d3\u01d0\3\2\2\2")
        buf.write("\u01d4\u01d5\3\2\2\2\u01d5\u01d6\b@\3\2\u01d6\u0080\3")
        buf.write("\2\2\2\u01d7\u01dc\t\4\2\2\u01d8\u01db\5=\37\2\u01d9\u01db")
        buf.write("\t\5\2\2\u01da\u01d8\3\2\2\2\u01da\u01d9\3\2\2\2\u01db")
        buf.write("\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u0082\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\7")
        buf.write("\62\2\2\u01e0\u01e7\5\u009fP\2\u01e1\u01e8\5=\37\2\u01e2")
        buf.write("\u01e4\t\6\2\2\u01e3\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2")
        buf.write("\u01e5\u01e3\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e8\3")
        buf.write("\2\2\2\u01e7\u01e1\3\2\2\2\u01e7\u01e3\3\2\2\2\u01e8\u01f1")
        buf.write("\3\2\2\2\u01e9\u01eb\5=\37\2\u01ea\u01ec\t\6\2\2\u01eb")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2")
        buf.write("\u01ed\u01ee\3\2\2\2\u01ee\u01f0\3\2\2\2\u01ef\u01e9\3")
        buf.write("\2\2\2\u01f0\u01f3\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u0084\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4")
        buf.write("\u01fb\7\62\2\2\u01f5\u01fc\5=\37\2\u01f6\u01f8\t\7\2")
        buf.write("\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01f7")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fc\3\2\2\2\u01fb")
        buf.write("\u01f5\3\2\2\2\u01fb\u01f7\3\2\2\2\u01fc\u0205\3\2\2\2")
        buf.write("\u01fd\u01ff\5=\37\2\u01fe\u0200\t\7\2\2\u01ff\u01fe\3")
        buf.write("\2\2\2\u0200\u0201\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0204\3\2\2\2\u0203\u01fd\3\2\2\2\u0204")
        buf.write("\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0086\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u0209\7")
        buf.write("\62\2\2\u0209\u0210\5\u009bN\2\u020a\u0211\5=\37\2\u020b")
        buf.write("\u020d\t\b\2\2\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u020c\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3")
        buf.write("\2\2\2\u0210\u020a\3\2\2\2\u0210\u020c\3\2\2\2\u0211\u021a")
        buf.write("\3\2\2\2\u0212\u0214\5=\37\2\u0213\u0215\t\b\2\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215\u0216\3\2\2\2\u0216\u0214\3\2\2\2")
        buf.write("\u0216\u0217\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u0212\3")
        buf.write("\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u021b")
        buf.write("\3\2\2\2\u021b\u0088\3\2\2\2\u021c\u021a\3\2\2\2\u021d")
        buf.write("\u0222\5\u0081A\2\u021e\u0222\5\u0083B\2\u021f\u0222\5")
        buf.write("\u0085C\2\u0220\u0222\5\u0087D\2\u0221\u021d\3\2\2\2\u0221")
        buf.write("\u021e\3\2\2\2\u0221\u021f\3\2\2\2\u0221\u0220\3\2\2\2")
        buf.write("\u0222\u0223\3\2\2\2\u0223\u0224\bE\4\2\u0224\u0227\3")
        buf.write("\2\2\2\u0225\u0227\7\62\2\2\u0226\u0221\3\2\2\2\u0226")
        buf.write("\u0225\3\2\2\2\u0227\u008a\3\2\2\2\u0228\u022c\7$\2\2")
        buf.write("\u0229\u022b\5\u008fH\2\u022a\u0229\3\2\2\2\u022b\u022e")
        buf.write("\3\2\2\2\u022c\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022f\3\2\2\2\u022e\u022c\3\2\2\2\u022f\u0230\bF\5\2")
        buf.write("\u0230\u008c\3\2\2\2\u0231\u0235\7$\2\2\u0232\u0234\5")
        buf.write("\u008fH\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0238\3\2\2\2")
        buf.write("\u0237\u0235\3\2\2\2\u0238\u0239\5\u0093J\2\u0239\u023a")
        buf.write("\bG\6\2\u023a\u008e\3\2\2\2\u023b\u023c\7)\2\2\u023c\u0240")
        buf.write("\7$\2\2\u023d\u0240\5\u0091I\2\u023e\u0240\n\t\2\2\u023f")
        buf.write("\u023b\3\2\2\2\u023f\u023d\3\2\2\2\u023f\u023e\3\2\2\2")
        buf.write("\u0240\u0090\3\2\2\2\u0241\u0242\7^\2\2\u0242\u0243\t")
        buf.write("\n\2\2\u0243\u0092\3\2\2\2\u0244\u0245\7^\2\2\u0245\u0248")
        buf.write("\n\n\2\2\u0246\u0248\7^\2\2\u0247\u0244\3\2\2\2\u0247")
        buf.write("\u0246\3\2\2\2\u0248\u0094\3\2\2\2\u0249\u024a\7%\2\2")
        buf.write("\u024a\u024b\7%\2\2\u024b\u024f\3\2\2\2\u024c\u024e\13")
        buf.write("\2\2\2\u024d\u024c\3\2\2\2\u024e\u0251\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u024f\u024d\3\2\2\2\u0250\u0252\3\2\2\2\u0251")
        buf.write("\u024f\3\2\2\2\u0252\u0253\7%\2\2\u0253\u0254\7%\2\2\u0254")
        buf.write("\u0255\3\2\2\2\u0255\u0256\bK\7\2\u0256\u0096\3\2\2\2")
        buf.write("\u0257\u0259\t\13\2\2\u0258\u0257\3\2\2\2\u0259\u025a")
        buf.write("\3\2\2\2\u025a\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write("\u025c\3\2\2\2\u025c\u025d\bL\7\2\u025d\u0098\3\2\2\2")
        buf.write("\u025e\u025f\13\2\2\2\u025f\u0260\bM\b\2\u0260\u009a\3")
        buf.write("\2\2\2\u0261\u0262\t\f\2\2\u0262\u009c\3\2\2\2\u0263\u0264")
        buf.write("\t\r\2\2\u0264\u009e\3\2\2\2\u0265\u0266\t\16\2\2\u0266")
        buf.write("\u00a0\3\2\2\2(\2\u00d7\u018e\u0194\u0197\u019f\u01a9")
        buf.write("\u01ad\u01b2\u01b7\u01be\u01c0\u01c4\u01cb\u01d0\u01d3")
        buf.write("\u01da\u01dc\u01e5\u01e7\u01ed\u01f1\u01f9\u01fb\u0201")
        buf.write("\u0205\u020e\u0210\u0216\u021a\u0221\u0226\u022c\u0235")
        buf.write("\u023f\u0247\u024f\u025a\t\3=\2\3@\3\3E\4\3F\5\3G\6\b")
        buf.write("\2\2\3M\7")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSEIF = 6
    ELSE = 7
    FOREACH = 8
    BOOLLIT = 9
    TRUE = 10
    FALSE = 11
    ARRAY = 12
    IN = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    STRING = 17
    RETURN = 18
    NULL = 19
    CLASS = 20
    VAL = 21
    VAR = 22
    CONSTRUCTOR = 23
    DESTRUCTOR = 24
    NEW = 25
    BY = 26
    SELF = 27
    DOUBLECOLONOP = 28
    DOUBLEDOTOP = 29
    UNDERSCORE = 30
    PLUSOP = 31
    MINUSOP = 32
    MULTIPLYOP = 33
    DIVIDEOP = 34
    MODULOOP = 35
    NOTOP = 36
    ANDOP = 37
    OROP = 38
    EQUALOP = 39
    ASSIGNOP = 40
    NOTEQUALOP = 41
    GTE = 42
    LTE = 43
    GT = 44
    LT = 45
    STREQUALOP = 46
    STRCONCATOP = 47
    LB = 48
    RB = 49
    LSB = 50
    RSB = 51
    LCB = 52
    RCB = 53
    DOT = 54
    COMMA = 55
    COLON = 56
    SEMICOLON = 57
    IDENTIFIERS = 58
    STRINGLIT = 59
    FLOATLIT = 60
    INTLIT = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    BLOCK_COMMENT = 64
    WS = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'afef'", "'sdfsdfsa'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
            "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'Self'", "'::'", "'..'", "'_'", "'+'", "'-'", 
            "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", 
            "'>='", "'<='", "'>'", "'<'", "'==.'", "'+.'", "'('", "')'", 
            "'['", "']'", "'{'", "'}'", "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLLIT", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
            "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
            "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", "GTE", 
            "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", "LB", "RB", 
            "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
            "IDENTIFIERS", "STRINGLIT", "FLOATLIT", "INTLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "T__1", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
                  "FOREACH", "BOOLLIT", "TRUE", "FALSE", "ARRAY", "IN", 
                  "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
                  "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", 
                  "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", 
                  "GTE", "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                  "COLON", "SEMICOLON", "IDENTIFIERS", "DOLLAR", "STRINGLIT", 
                  "DECIMALPART", "EXPONENTPART", "FLOATLIT", "DEC", "HEX", 
                  "OCT", "BIN", "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", "BLOCK_COMMENT", 
                  "WS", "ERROR_CHAR", "B", "E", "X" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit() # result mean for input

        # delete later
        print('--------------------------------------------------------------------------------')
        attributes = inspect.getmembers(D96Lexer, lambda a:not(inspect.isroutine(a)))
        user_defined_attr = [a for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))]
        for i in user_defined_attr:
            if tk == i[1]:
                print ("{:<30} {:<30} {:<50}".format(result.text, '|', i[0]))
        print('--------------------------------------------------------------------------------')
        return result


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[59] = self.STRINGLIT_action 
            actions[62] = self.FLOATLIT_action 
            actions[67] = self.INTLIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = str(self.text)[1:-1].replace('\'"','"')
            	

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	current = str(self.text)
            	raise UncloseString(current[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             raise ErrorToken(self.text) 
     


