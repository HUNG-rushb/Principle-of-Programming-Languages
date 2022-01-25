# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0290\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00cc\n\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+")
        buf.write("\3+\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3;\3;\7;\u018e\n;\f;\16;\u0191\13;\3<\3<\6<\u0195\n")
        buf.write("<\r<\16<\u0196\3=\3=\3>\3>\7>\u019d\n>\f>\16>\u01a0\13")
        buf.write(">\3>\3>\3>\3?\3?\7?\u01a7\n?\f?\16?\u01aa\13?\3@\3@\3")
        buf.write("@\5@\u01af\n@\3@\7@\u01b2\n@\f@\16@\u01b5\13@\3@\3@\7")
        buf.write("@\u01b9\n@\f@\16@\u01bc\13@\3@\6@\u01bf\n@\r@\16@\u01c0")
        buf.write("\5@\u01c3\n@\3A\3A\5A\u01c7\nA\3A\3A\3A\3A\3A\3A\3A\5")
        buf.write("A\u01d0\nA\3A\3A\3A\3A\3A\3A\5A\u01d8\nA\3A\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\5A\u01e3\nA\3A\3A\3B\3B\3B\3B\3B\7B\u01ec")
        buf.write("\nB\fB\16B\u01ef\13B\3C\3C\3C\6C\u01f4\nC\rC\16C\u01f5")
        buf.write("\3C\3C\6C\u01fa\nC\rC\16C\u01fb\7C\u01fe\nC\fC\16C\u0201")
        buf.write("\13C\3C\7C\u0204\nC\fC\16C\u0207\13C\5C\u0209\nC\3C\5")
        buf.write("C\u020c\nC\3D\3D\6D\u0210\nD\rD\16D\u0211\3D\3D\6D\u0216")
        buf.write("\nD\rD\16D\u0217\7D\u021a\nD\fD\16D\u021d\13D\3D\7D\u0220")
        buf.write("\nD\fD\16D\u0223\13D\5D\u0225\nD\3D\5D\u0228\nD\3E\3E")
        buf.write("\3E\6E\u022d\nE\rE\16E\u022e\3E\3E\6E\u0233\nE\rE\16E")
        buf.write("\u0234\7E\u0237\nE\fE\16E\u023a\13E\3E\7E\u023d\nE\fE")
        buf.write("\16E\u0240\13E\5E\u0242\nE\3E\5E\u0245\nE\3F\3F\3F\3F")
        buf.write("\5F\u024b\nF\3F\3F\3F\5F\u0250\nF\3G\3G\7G\u0254\nG\f")
        buf.write("G\16G\u0257\13G\3G\3G\3H\3H\7H\u025d\nH\fH\16H\u0260\13")
        buf.write("H\3H\3H\3H\3I\3I\3I\3I\5I\u0269\nI\3J\3J\3J\3K\3K\3K\5")
        buf.write("K\u0271\nK\3L\3L\3L\3L\7L\u0277\nL\fL\16L\u027a\13L\3")
        buf.write("L\3L\3L\3L\3L\3M\6M\u0282\nM\rM\16M\u0283\3M\3M\3N\3N")
        buf.write("\3N\3O\3O\3P\3P\3Q\3Q\3\u0278\2R\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y\2{>}\2\177\2\u0081")
        buf.write("?\u0083\2\u0085\2\u0087\2\u0089\2\u008b@\u008dA\u008f")
        buf.write("B\u0091\2\u0093\2\u0095\2\u0097C\u0099D\u009bE\u009d\2")
        buf.write("\u009f\2\u00a1\2\3\2\21\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\3\2\63;\5\2\63;CHch\5\2\62;CHch\3\2\639\3\2\629\3")
        buf.write("\2\62\63\4\2$$^^\t\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\4")
        buf.write("\2DDdd\4\2GGgg\4\2ZZzz\2\u02b2\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2{\3\2\2\2\2\u0081\3\2\2\2\2\u008b\3")
        buf.write("\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0097\3\2\2\2")
        buf.write("\2\u0099\3\2\2\2\2\u009b\3\2\2\2\3\u00a3\3\2\2\2\5\u00a9")
        buf.write("\3\2\2\2\7\u00b2\3\2\2\2\t\u00b5\3\2\2\2\13\u00bc\3\2")
        buf.write("\2\2\r\u00c1\3\2\2\2\17\u00cb\3\2\2\2\21\u00cd\3\2\2\2")
        buf.write("\23\u00d2\3\2\2\2\25\u00d8\3\2\2\2\27\u00de\3\2\2\2\31")
        buf.write("\u00e1\3\2\2\2\33\u00e5\3\2\2\2\35\u00eb\3\2\2\2\37\u00f3")
        buf.write("\3\2\2\2!\u00fa\3\2\2\2#\u0101\3\2\2\2%\u0106\3\2\2\2")
        buf.write("\'\u010c\3\2\2\2)\u0110\3\2\2\2+\u0114\3\2\2\2-\u0120")
        buf.write("\3\2\2\2/\u012b\3\2\2\2\61\u012f\3\2\2\2\63\u0132\3\2")
        buf.write("\2\2\65\u0137\3\2\2\2\67\u013a\3\2\2\29\u013d\3\2\2\2")
        buf.write(";\u013f\3\2\2\2=\u0141\3\2\2\2?\u0143\3\2\2\2A\u0145\3")
        buf.write("\2\2\2C\u0147\3\2\2\2E\u0149\3\2\2\2G\u014b\3\2\2\2I\u014e")
        buf.write("\3\2\2\2K\u0151\3\2\2\2M\u0154\3\2\2\2O\u0156\3\2\2\2")
        buf.write("Q\u0159\3\2\2\2S\u015c\3\2\2\2U\u015f\3\2\2\2W\u0161\3")
        buf.write("\2\2\2Y\u0163\3\2\2\2[\u0167\3\2\2\2]\u016a\3\2\2\2_\u016c")
        buf.write("\3\2\2\2a\u016e\3\2\2\2c\u0170\3\2\2\2e\u0172\3\2\2\2")
        buf.write("g\u0174\3\2\2\2i\u0176\3\2\2\2k\u0178\3\2\2\2m\u017a\3")
        buf.write("\2\2\2o\u017c\3\2\2\2q\u017e\3\2\2\2s\u0186\3\2\2\2u\u018b")
        buf.write("\3\2\2\2w\u0192\3\2\2\2y\u0198\3\2\2\2{\u019a\3\2\2\2")
        buf.write("}\u01a4\3\2\2\2\177\u01ab\3\2\2\2\u0081\u01e2\3\2\2\2")
        buf.write("\u0083\u01e6\3\2\2\2\u0085\u01f0\3\2\2\2\u0087\u020d\3")
        buf.write("\2\2\2\u0089\u0229\3\2\2\2\u008b\u024f\3\2\2\2\u008d\u0251")
        buf.write("\3\2\2\2\u008f\u025a\3\2\2\2\u0091\u0268\3\2\2\2\u0093")
        buf.write("\u026a\3\2\2\2\u0095\u0270\3\2\2\2\u0097\u0272\3\2\2\2")
        buf.write("\u0099\u0281\3\2\2\2\u009b\u0287\3\2\2\2\u009d\u028a\3")
        buf.write("\2\2\2\u009f\u028c\3\2\2\2\u00a1\u028e\3\2\2\2\u00a3\u00a4")
        buf.write("\7D\2\2\u00a4\u00a5\7t\2\2\u00a5\u00a6\7g\2\2\u00a6\u00a7")
        buf.write("\7c\2\2\u00a7\u00a8\7m\2\2\u00a8\4\3\2\2\2\u00a9\u00aa")
        buf.write("\7E\2\2\u00aa\u00ab\7q\2\2\u00ab\u00ac\7p\2\2\u00ac\u00ad")
        buf.write("\7v\2\2\u00ad\u00ae\7k\2\2\u00ae\u00af\7p\2\2\u00af\u00b0")
        buf.write("\7w\2\2\u00b0\u00b1\7g\2\2\u00b1\6\3\2\2\2\u00b2\u00b3")
        buf.write("\7K\2\2\u00b3\u00b4\7h\2\2\u00b4\b\3\2\2\2\u00b5\u00b6")
        buf.write("\7G\2\2\u00b6\u00b7\7n\2\2\u00b7\u00b8\7u\2\2\u00b8\u00b9")
        buf.write("\7g\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7h\2\2\u00bb\n")
        buf.write("\3\2\2\2\u00bc\u00bd\7G\2\2\u00bd\u00be\7n\2\2\u00be\u00bf")
        buf.write("\7u\2\2\u00bf\u00c0\7g\2\2\u00c0\f\3\2\2\2\u00c1\u00c2")
        buf.write("\7H\2\2\u00c2\u00c3\7q\2\2\u00c3\u00c4\7t\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7c\2\2\u00c6\u00c7\7e\2\2\u00c7\u00c8")
        buf.write("\7j\2\2\u00c8\16\3\2\2\2\u00c9\u00cc\5\21\t\2\u00ca\u00cc")
        buf.write("\5\23\n\2\u00cb\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc")
        buf.write("\20\3\2\2\2\u00cd\u00ce\7V\2\2\u00ce\u00cf\7t\2\2\u00cf")
        buf.write("\u00d0\7w\2\2\u00d0\u00d1\7g\2\2\u00d1\22\3\2\2\2\u00d2")
        buf.write("\u00d3\7H\2\2\u00d3\u00d4\7c\2\2\u00d4\u00d5\7n\2\2\u00d5")
        buf.write("\u00d6\7u\2\2\u00d6\u00d7\7g\2\2\u00d7\24\3\2\2\2\u00d8")
        buf.write("\u00d9\7C\2\2\u00d9\u00da\7t\2\2\u00da\u00db\7t\2\2\u00db")
        buf.write("\u00dc\7c\2\2\u00dc\u00dd\7{\2\2\u00dd\26\3\2\2\2\u00de")
        buf.write("\u00df\7K\2\2\u00df\u00e0\7p\2\2\u00e0\30\3\2\2\2\u00e1")
        buf.write("\u00e2\7K\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7v\2\2\u00e4")
        buf.write("\32\3\2\2\2\u00e5\u00e6\7H\2\2\u00e6\u00e7\7n\2\2\u00e7")
        buf.write("\u00e8\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u00ea\7v\2\2\u00ea")
        buf.write("\34\3\2\2\2\u00eb\u00ec\7D\2\2\u00ec\u00ed\7q\2\2\u00ed")
        buf.write("\u00ee\7q\2\2\u00ee\u00ef\7n\2\2\u00ef\u00f0\7g\2\2\u00f0")
        buf.write("\u00f1\7c\2\2\u00f1\u00f2\7p\2\2\u00f2\36\3\2\2\2\u00f3")
        buf.write("\u00f4\7U\2\2\u00f4\u00f5\7v\2\2\u00f5\u00f6\7t\2\2\u00f6")
        buf.write("\u00f7\7k\2\2\u00f7\u00f8\7p\2\2\u00f8\u00f9\7i\2\2\u00f9")
        buf.write(" \3\2\2\2\u00fa\u00fb\7T\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("\u00fd\7v\2\2\u00fd\u00fe\7w\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7p\2\2\u0100\"\3\2\2\2\u0101\u0102\7P\2\2\u0102")
        buf.write("\u0103\7w\2\2\u0103\u0104\7n\2\2\u0104\u0105\7n\2\2\u0105")
        buf.write("$\3\2\2\2\u0106\u0107\7E\2\2\u0107\u0108\7n\2\2\u0108")
        buf.write("\u0109\7c\2\2\u0109\u010a\7u\2\2\u010a\u010b\7u\2\2\u010b")
        buf.write("&\3\2\2\2\u010c\u010d\7X\2\2\u010d\u010e\7c\2\2\u010e")
        buf.write("\u010f\7n\2\2\u010f(\3\2\2\2\u0110\u0111\7X\2\2\u0111")
        buf.write("\u0112\7c\2\2\u0112\u0113\7t\2\2\u0113*\3\2\2\2\u0114")
        buf.write("\u0115\7E\2\2\u0115\u0116\7q\2\2\u0116\u0117\7p\2\2\u0117")
        buf.write("\u0118\7u\2\2\u0118\u0119\7v\2\2\u0119\u011a\7t\2\2\u011a")
        buf.write("\u011b\7w\2\2\u011b\u011c\7e\2\2\u011c\u011d\7v\2\2\u011d")
        buf.write("\u011e\7q\2\2\u011e\u011f\7t\2\2\u011f,\3\2\2\2\u0120")
        buf.write("\u0121\7F\2\2\u0121\u0122\7g\2\2\u0122\u0123\7u\2\2\u0123")
        buf.write("\u0124\7v\2\2\u0124\u0125\7t\2\2\u0125\u0126\7w\2\2\u0126")
        buf.write("\u0127\7e\2\2\u0127\u0128\7v\2\2\u0128\u0129\7q\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a.\3\2\2\2\u012b\u012c\7P\2\2\u012c")
        buf.write("\u012d\7g\2\2\u012d\u012e\7y\2\2\u012e\60\3\2\2\2\u012f")
        buf.write("\u0130\7D\2\2\u0130\u0131\7{\2\2\u0131\62\3\2\2\2\u0132")
        buf.write("\u0133\7U\2\2\u0133\u0134\7g\2\2\u0134\u0135\7n\2\2\u0135")
        buf.write("\u0136\7h\2\2\u0136\64\3\2\2\2\u0137\u0138\7<\2\2\u0138")
        buf.write("\u0139\7<\2\2\u0139\66\3\2\2\2\u013a\u013b\7\60\2\2\u013b")
        buf.write("\u013c\7\60\2\2\u013c8\3\2\2\2\u013d\u013e\7a\2\2\u013e")
        buf.write(":\3\2\2\2\u013f\u0140\7-\2\2\u0140<\3\2\2\2\u0141\u0142")
        buf.write("\7/\2\2\u0142>\3\2\2\2\u0143\u0144\7,\2\2\u0144@\3\2\2")
        buf.write("\2\u0145\u0146\7\61\2\2\u0146B\3\2\2\2\u0147\u0148\7\'")
        buf.write("\2\2\u0148D\3\2\2\2\u0149\u014a\7#\2\2\u014aF\3\2\2\2")
        buf.write("\u014b\u014c\7(\2\2\u014c\u014d\7(\2\2\u014dH\3\2\2\2")
        buf.write("\u014e\u014f\7~\2\2\u014f\u0150\7~\2\2\u0150J\3\2\2\2")
        buf.write("\u0151\u0152\7?\2\2\u0152\u0153\7?\2\2\u0153L\3\2\2\2")
        buf.write("\u0154\u0155\7?\2\2\u0155N\3\2\2\2\u0156\u0157\7#\2\2")
        buf.write("\u0157\u0158\7?\2\2\u0158P\3\2\2\2\u0159\u015a\7@\2\2")
        buf.write("\u015a\u015b\7?\2\2\u015bR\3\2\2\2\u015c\u015d\7>\2\2")
        buf.write("\u015d\u015e\7?\2\2\u015eT\3\2\2\2\u015f\u0160\7@\2\2")
        buf.write("\u0160V\3\2\2\2\u0161\u0162\7>\2\2\u0162X\3\2\2\2\u0163")
        buf.write("\u0164\7?\2\2\u0164\u0165\7?\2\2\u0165\u0166\7\60\2\2")
        buf.write("\u0166Z\3\2\2\2\u0167\u0168\7-\2\2\u0168\u0169\7\60\2")
        buf.write("\2\u0169\\\3\2\2\2\u016a\u016b\7*\2\2\u016b^\3\2\2\2\u016c")
        buf.write("\u016d\7+\2\2\u016d`\3\2\2\2\u016e\u016f\7]\2\2\u016f")
        buf.write("b\3\2\2\2\u0170\u0171\7_\2\2\u0171d\3\2\2\2\u0172\u0173")
        buf.write("\7}\2\2\u0173f\3\2\2\2\u0174\u0175\7\177\2\2\u0175h\3")
        buf.write("\2\2\2\u0176\u0177\7\60\2\2\u0177j\3\2\2\2\u0178\u0179")
        buf.write("\7.\2\2\u0179l\3\2\2\2\u017a\u017b\7<\2\2\u017bn\3\2\2")
        buf.write("\2\u017c\u017d\7=\2\2\u017dp\3\2\2\2\u017e\u017f\7R\2")
        buf.write("\2\u017f\u0180\7t\2\2\u0180\u0181\7q\2\2\u0181\u0182\7")
        buf.write("i\2\2\u0182\u0183\7t\2\2\u0183\u0184\7c\2\2\u0184\u0185")
        buf.write("\7o\2\2\u0185r\3\2\2\2\u0186\u0187\7o\2\2\u0187\u0188")
        buf.write("\7c\2\2\u0188\u0189\7k\2\2\u0189\u018a\7p\2\2\u018at\3")
        buf.write("\2\2\2\u018b\u018f\t\2\2\2\u018c\u018e\t\3\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190v\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0194\5y=\2\u0193\u0195\t\3\2\2\u0194\u0193\3\2\2\2\u0195")
        buf.write("\u0196\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2")
        buf.write("\u0197x\3\2\2\2\u0198\u0199\7&\2\2\u0199z\3\2\2\2\u019a")
        buf.write("\u019e\7$\2\2\u019b\u019d\5\u0091I\2\u019c\u019b\3\2\2")
        buf.write("\2\u019d\u01a0\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f")
        buf.write("\3\2\2\2\u019f\u01a1\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1")
        buf.write("\u01a2\7$\2\2\u01a2\u01a3\b>\2\2\u01a3|\3\2\2\2\u01a4")
        buf.write("\u01a8\7\60\2\2\u01a5\u01a7\t\4\2\2\u01a6\u01a5\3\2\2")
        buf.write("\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9")
        buf.write("\3\2\2\2\u01a9~\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ae")
        buf.write("\5\u009fP\2\u01ac\u01af\5=\37\2\u01ad\u01af\5;\36\2\u01ae")
        buf.write("\u01ac\3\2\2\2\u01ae\u01ad\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01af\u01c2\3\2\2\2\u01b0\u01b2\7\62\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b3")
        buf.write("\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5\u01b3\3\2\2\2")
        buf.write("\u01b6\u01ba\t\5\2\2\u01b7\u01b9\t\4\2\2\u01b8\u01b7\3")
        buf.write("\2\2\2\u01b9\u01bc\3\2\2\2\u01ba\u01b8\3\2\2\2\u01ba\u01bb")
        buf.write("\3\2\2\2\u01bb\u01c3\3\2\2\2\u01bc\u01ba\3\2\2\2\u01bd")
        buf.write("\u01bf\7\62\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c0\3\2\2")
        buf.write("\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c3")
        buf.write("\3\2\2\2\u01c2\u01b3\3\2\2\2\u01c2\u01be\3\2\2\2\u01c3")
        buf.write("\u0080\3\2\2\2\u01c4\u01c7\5\u0083B\2\u01c5\u01c7\7\62")
        buf.write("\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\5}?\2\u01c9\u01ca\5\177@\2\u01ca")
        buf.write("\u01cb\3\2\2\2\u01cb\u01cc\bA\3\2\u01cc\u01e3\3\2\2\2")
        buf.write("\u01cd\u01d0\5\u0083B\2\u01ce\u01d0\7\62\2\2\u01cf\u01cd")
        buf.write("\3\2\2\2\u01cf\u01ce\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1")
        buf.write("\u01d2\5}?\2\u01d2\u01d3\3\2\2\2\u01d3\u01d4\bA\4\2\u01d4")
        buf.write("\u01e3\3\2\2\2\u01d5\u01d8\5\u0083B\2\u01d6\u01d8\7\62")
        buf.write("\2\2\u01d7\u01d5\3\2\2\2\u01d7\u01d6\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01da\5\177@\2\u01da\u01db\3\2\2\2\u01db")
        buf.write("\u01dc\bA\5\2\u01dc\u01e3\3\2\2\2\u01dd\u01de\5}?\2\u01de")
        buf.write("\u01df\5\177@\2\u01df\u01e0\3\2\2\2\u01e0\u01e1\bA\6\2")
        buf.write("\u01e1\u01e3\3\2\2\2\u01e2\u01c6\3\2\2\2\u01e2\u01cf\3")
        buf.write("\2\2\2\u01e2\u01d7\3\2\2\2\u01e2\u01dd\3\2\2\2\u01e3\u01e4")
        buf.write("\3\2\2\2\u01e4\u01e5\bA\7\2\u01e5\u0082\3\2\2\2\u01e6")
        buf.write("\u01ed\t\5\2\2\u01e7\u01e8\59\35\2\u01e8\u01e9\t\4\2\2")
        buf.write("\u01e9\u01ec\3\2\2\2\u01ea\u01ec\t\4\2\2\u01eb\u01e7\3")
        buf.write("\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u01ef\3\2\2\2\u01ed\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u0084\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01f0\u01f1\7\62\2\2\u01f1\u020b\5\u00a1")
        buf.write("Q\2\u01f2\u01f4\t\6\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f5")
        buf.write("\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u0208\3\2\2\2\u01f7\u01f9\59\35\2\u01f8\u01fa\t\7\2\2")
        buf.write("\u01f9\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01f9\3")
        buf.write("\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fe\3\2\2\2\u01fd\u01f7")
        buf.write("\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0209\3\2\2\2\u0201\u01ff\3\2\2\2")
        buf.write("\u0202\u0204\t\7\2\2\u0203\u0202\3\2\2\2\u0204\u0207\3")
        buf.write("\2\2\2\u0205\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0209")
        buf.write("\3\2\2\2\u0207\u0205\3\2\2\2\u0208\u01ff\3\2\2\2\u0208")
        buf.write("\u0205\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u020c\7\62\2")
        buf.write("\2\u020b\u01f3\3\2\2\2\u020b\u020a\3\2\2\2\u020c\u0086")
        buf.write("\3\2\2\2\u020d\u0227\7\62\2\2\u020e\u0210\t\b\2\2\u020f")
        buf.write("\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211\u020f\3\2\2\2")
        buf.write("\u0211\u0212\3\2\2\2\u0212\u0224\3\2\2\2\u0213\u0215\5")
        buf.write("9\35\2\u0214\u0216\t\t\2\2\u0215\u0214\3\2\2\2\u0216\u0217")
        buf.write("\3\2\2\2\u0217\u0215\3\2\2\2\u0217\u0218\3\2\2\2\u0218")
        buf.write("\u021a\3\2\2\2\u0219\u0213\3\2\2\2\u021a\u021d\3\2\2\2")
        buf.write("\u021b\u0219\3\2\2\2\u021b\u021c\3\2\2\2\u021c\u0225\3")
        buf.write("\2\2\2\u021d\u021b\3\2\2\2\u021e\u0220\t\t\2\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0224\u021b\3\2\2\2\u0224\u0221\3\2\2\2\u0225\u0228\3")
        buf.write("\2\2\2\u0226\u0228\7\62\2\2\u0227\u020f\3\2\2\2\u0227")
        buf.write("\u0226\3\2\2\2\u0228\u0088\3\2\2\2\u0229\u022a\7\62\2")
        buf.write("\2\u022a\u0244\5\u009dO\2\u022b\u022d\7\63\2\2\u022c\u022b")
        buf.write("\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022c\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022f\u0241\3\2\2\2\u0230\u0232\59\35\2")
        buf.write("\u0231\u0233\t\n\2\2\u0232\u0231\3\2\2\2\u0233\u0234\3")
        buf.write("\2\2\2\u0234\u0232\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237")
        buf.write("\3\2\2\2\u0236\u0230\3\2\2\2\u0237\u023a\3\2\2\2\u0238")
        buf.write("\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u0242\3\2\2\2")
        buf.write("\u023a\u0238\3\2\2\2\u023b\u023d\t\n\2\2\u023c\u023b\3")
        buf.write("\2\2\2\u023d\u0240\3\2\2\2\u023e\u023c\3\2\2\2\u023e\u023f")
        buf.write("\3\2\2\2\u023f\u0242\3\2\2\2\u0240\u023e\3\2\2\2\u0241")
        buf.write("\u0238\3\2\2\2\u0241\u023e\3\2\2\2\u0242\u0245\3\2\2\2")
        buf.write("\u0243\u0245\7\62\2\2\u0244\u022c\3\2\2\2\u0244\u0243")
        buf.write("\3\2\2\2\u0245\u008a\3\2\2\2\u0246\u024b\5\u0083B\2\u0247")
        buf.write("\u024b\5\u0085C\2\u0248\u024b\5\u0087D\2\u0249\u024b\5")
        buf.write("\u0089E\2\u024a\u0246\3\2\2\2\u024a\u0247\3\2\2\2\u024a")
        buf.write("\u0248\3\2\2\2\u024a\u0249\3\2\2\2\u024b\u024c\3\2\2\2")
        buf.write("\u024c\u024d\bF\b\2\u024d\u0250\3\2\2\2\u024e\u0250\7")
        buf.write("\62\2\2\u024f\u024a\3\2\2\2\u024f\u024e\3\2\2\2\u0250")
        buf.write("\u008c\3\2\2\2\u0251\u0255\7$\2\2\u0252\u0254\5\u0091")
        buf.write("I\2\u0253\u0252\3\2\2\2\u0254\u0257\3\2\2\2\u0255\u0253")
        buf.write("\3\2\2\2\u0255\u0256\3\2\2\2\u0256\u0258\3\2\2\2\u0257")
        buf.write("\u0255\3\2\2\2\u0258\u0259\bG\t\2\u0259\u008e\3\2\2\2")
        buf.write("\u025a\u025e\7$\2\2\u025b\u025d\5\u0091I\2\u025c\u025b")
        buf.write("\3\2\2\2\u025d\u0260\3\2\2\2\u025e\u025c\3\2\2\2\u025e")
        buf.write("\u025f\3\2\2\2\u025f\u0261\3\2\2\2\u0260\u025e\3\2\2\2")
        buf.write("\u0261\u0262\5\u0095K\2\u0262\u0263\bH\n\2\u0263\u0090")
        buf.write("\3\2\2\2\u0264\u0265\7)\2\2\u0265\u0269\7$\2\2\u0266\u0269")
        buf.write("\5\u0093J\2\u0267\u0269\n\13\2\2\u0268\u0264\3\2\2\2\u0268")
        buf.write("\u0266\3\2\2\2\u0268\u0267\3\2\2\2\u0269\u0092\3\2\2\2")
        buf.write("\u026a\u026b\7^\2\2\u026b\u026c\t\f\2\2\u026c\u0094\3")
        buf.write("\2\2\2\u026d\u026e\7^\2\2\u026e\u0271\n\f\2\2\u026f\u0271")
        buf.write("\7^\2\2\u0270\u026d\3\2\2\2\u0270\u026f\3\2\2\2\u0271")
        buf.write("\u0096\3\2\2\2\u0272\u0273\7%\2\2\u0273\u0274\7%\2\2\u0274")
        buf.write("\u0278\3\2\2\2\u0275\u0277\13\2\2\2\u0276\u0275\3\2\2")
        buf.write("\2\u0277\u027a\3\2\2\2\u0278\u0279\3\2\2\2\u0278\u0276")
        buf.write("\3\2\2\2\u0279\u027b\3\2\2\2\u027a\u0278\3\2\2\2\u027b")
        buf.write("\u027c\7%\2\2\u027c\u027d\7%\2\2\u027d\u027e\3\2\2\2\u027e")
        buf.write("\u027f\bL\13\2\u027f\u0098\3\2\2\2\u0280\u0282\t\r\2\2")
        buf.write("\u0281\u0280\3\2\2\2\u0282\u0283\3\2\2\2\u0283\u0281\3")
        buf.write("\2\2\2\u0283\u0284\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0286")
        buf.write("\bM\13\2\u0286\u009a\3\2\2\2\u0287\u0288\13\2\2\2\u0288")
        buf.write("\u0289\bN\f\2\u0289\u009c\3\2\2\2\u028a\u028b\t\16\2\2")
        buf.write("\u028b\u009e\3\2\2\2\u028c\u028d\t\17\2\2\u028d\u00a0")
        buf.write("\3\2\2\2\u028e\u028f\t\20\2\2\u028f\u00a2\3\2\2\2-\2\u00cb")
        buf.write("\u018f\u0196\u019e\u01a8\u01ae\u01b3\u01ba\u01c0\u01c2")
        buf.write("\u01c6\u01cf\u01d7\u01e2\u01eb\u01ed\u01f5\u01fb\u01ff")
        buf.write("\u0205\u0208\u020b\u0211\u0217\u021b\u0221\u0224\u0227")
        buf.write("\u022e\u0234\u0238\u023e\u0241\u0244\u024a\u024f\u0255")
        buf.write("\u025e\u0268\u0270\u0278\u0283\r\3>\2\3A\3\3A\4\3A\5\3")
        buf.write("A\6\3A\7\3F\b\3G\t\3H\n\b\2\2\3N\13")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOREACH = 6
    BOOLLIT = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    CONSTRUCTOR = 21
    DESTRUCTOR = 22
    NEW = 23
    BY = 24
    SELF = 25
    DOUBLECOLONOP = 26
    DOUBLEDOTOP = 27
    UNDERSCORE = 28
    PLUSOP = 29
    MINUSOP = 30
    MULTIPLYOP = 31
    DIVIDEOP = 32
    MODULOOP = 33
    NOTOP = 34
    ANDOP = 35
    OROP = 36
    EQUALOP = 37
    ASSIGNOP = 38
    NOTEQUALOP = 39
    GTE = 40
    LTE = 41
    GT = 42
    LT = 43
    STREQUALOP = 44
    STRCONCATOP = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    LCB = 50
    RCB = 51
    DOT = 52
    COMMA = 53
    COLON = 54
    SEMICOLON = 55
    PROGRAM = 56
    MAIN = 57
    VARIABLE_IN_FUNC_IDENTIFIERS = 58
    DOLLAR_IDENTIFIERS = 59
    STRINGLIT = 60
    FLOATLIT = 61
    INTLIT = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    BLOCK_COMMENT = 65
    WS = 66
    ERROR_CHAR = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'::'", "'..'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'='", "'!='", "'>='", "'<='", "'>'", 
            "'<'", "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "','", "':'", "';'", "'Program'", "'main'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLLIT", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
            "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
            "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", "GTE", 
            "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", "LB", "RB", 
            "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
            "PROGRAM", "MAIN", "VARIABLE_IN_FUNC_IDENTIFIERS", "DOLLAR_IDENTIFIERS", 
            "STRINGLIT", "FLOATLIT", "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "BOOLLIT", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", 
                  "GTE", "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                  "COLON", "SEMICOLON", "PROGRAM", "MAIN", "VARIABLE_IN_FUNC_IDENTIFIERS", 
                  "DOLLAR_IDENTIFIERS", "DOLLAR", "STRINGLIT", "DECIMALPART", 
                  "EXPONENTPART", "FLOATLIT", "DEC", "HEX", "OCT", "BIN", 
                  "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_CHAR", 
                  "ESC_CHAR", "ESC_UNAVAILABLE", "BLOCK_COMMENT", "WS", 
                  "ERROR_CHAR", "B", "E", "X" ]

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
            actions[60] = self.STRINGLIT_action 
            actions[63] = self.FLOATLIT_action 
            actions[68] = self.INTLIT_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[76] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    if str(self.text)[-1] == '"' and str(self.text)[-2] == '\'': 
                        raise UncloseString(str(self.text)[1:])
                    
                    current = self.text.find('\n')
                    if current != -1: 
                        raise UncloseString(str(self.text[:current - 1]))
                    self.text = str(self.text)[1:-1]

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 3:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 4:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 5:
            self.text = self.text.replace("_", "")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:

            	current = str(self.text)
            	raise UncloseString(current[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:
             raise ErrorToken(self.text) 
     


