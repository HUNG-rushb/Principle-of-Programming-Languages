# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u024f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\5\b\u00c8\n\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3")
        buf.write("&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62")
        buf.write("\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38")
        buf.write("\38\39\39\69\u017d\n9\r9\169\u017e\39\39\79\u0183\n9\f")
        buf.write("9\169\u0186\139\59\u0188\n9\3:\3:\3;\3;\7;\u018e\n;\f")
        buf.write(";\16;\u0191\13;\3;\3;\3;\3<\3<\7<\u0198\n<\f<\16<\u019b")
        buf.write("\13<\3<\3<\3=\3=\3=\5=\u01a2\n=\3=\7=\u01a5\n=\f=\16=")
        buf.write("\u01a8\13=\3=\3=\3>\3>\3>\7>\u01af\n>\f>\16>\u01b2\13")
        buf.write(">\5>\u01b4\n>\3>\3>\5>\u01b8\n>\3>\5>\u01bb\n>\3>\3>\3")
        buf.write(">\5>\u01c0\n>\3>\3>\3?\3?\3?\7?\u01c7\n?\f?\16?\u01ca")
        buf.write("\13?\3@\3@\3@\6@\u01cf\n@\r@\16@\u01d0\3@\3@\6@\u01d5")
        buf.write("\n@\r@\16@\u01d6\7@\u01d9\n@\f@\16@\u01dc\13@\3A\3A\6")
        buf.write("A\u01e0\nA\rA\16A\u01e1\3A\3A\6A\u01e6\nA\rA\16A\u01e7")
        buf.write("\7A\u01ea\nA\fA\16A\u01ed\13A\3B\3B\3B\6B\u01f2\nB\rB")
        buf.write("\16B\u01f3\3B\3B\6B\u01f8\nB\rB\16B\u01f9\7B\u01fc\nB")
        buf.write("\fB\16B\u01ff\13B\3C\3C\3C\3C\5C\u0205\nC\3C\3C\3C\5C")
        buf.write("\u020a\nC\3D\3D\7D\u020e\nD\fD\16D\u0211\13D\3D\3D\3E")
        buf.write("\3E\7E\u0217\nE\fE\16E\u021a\13E\3E\3E\3E\3F\3F\3F\3F")
        buf.write("\5F\u0223\nF\3G\3G\3G\3H\3H\3H\5H\u022b\nH\3I\3I\3I\3")
        buf.write("I\7I\u0231\nI\fI\16I\u0234\13I\3I\3I\3I\3I\3I\3J\6J\u023c")
        buf.write("\nJ\rJ\16J\u023d\3J\3J\3K\3K\3K\3L\6L\u0246\nL\rL\16L")
        buf.write("\u0247\3M\3M\3N\3N\3O\3O\3\u0232\2P\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_")
        buf.write("\61a\62c\63e\64g\65i\66k\67m8o9q:s\2u;w\2y\2{<}\2\177")
        buf.write("\2\u0081\2\u0083\2\u0085=\u0087>\u0089?\u008b\2\u008d")
        buf.write("\2\u008f\2\u0091@\u0093A\u0095B\u0097C\u0099\2\u009b\2")
        buf.write("\u009d\2\3\2\20\6\2\62;C\\aac|\5\2C\\aac|\3\2\62;\3\2")
        buf.write("\63;\5\2\62;CHch\3\2\629\3\2\62\63\4\2$$^^\n\2$$))^^d")
        buf.write("dhhppttvv\3\2^^\5\2\n\f\16\17\"\"\4\2DDdd\4\2GGgg\4\2")
        buf.write("ZZzz\2\u0266\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3")
        buf.write("\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2")
        buf.write("\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2")
        buf.write("\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write("#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2u\3\2\2\2\2{\3\2\2\2\2\u0085\3\2")
        buf.write("\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u0091\3\2\2\2\2")
        buf.write("\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009f")
        buf.write("\3\2\2\2\5\u00a5\3\2\2\2\7\u00ae\3\2\2\2\t\u00b1\3\2\2")
        buf.write("\2\13\u00b8\3\2\2\2\r\u00bd\3\2\2\2\17\u00c7\3\2\2\2\21")
        buf.write("\u00c9\3\2\2\2\23\u00ce\3\2\2\2\25\u00d4\3\2\2\2\27\u00da")
        buf.write("\3\2\2\2\31\u00dd\3\2\2\2\33\u00e1\3\2\2\2\35\u00e7\3")
        buf.write("\2\2\2\37\u00ef\3\2\2\2!\u00f6\3\2\2\2#\u00fd\3\2\2\2")
        buf.write("%\u0102\3\2\2\2\'\u0108\3\2\2\2)\u010c\3\2\2\2+\u0110")
        buf.write("\3\2\2\2-\u011c\3\2\2\2/\u0127\3\2\2\2\61\u012b\3\2\2")
        buf.write("\2\63\u012e\3\2\2\2\65\u0133\3\2\2\2\67\u0136\3\2\2\2")
        buf.write("9\u0139\3\2\2\2;\u013b\3\2\2\2=\u013d\3\2\2\2?\u013f\3")
        buf.write("\2\2\2A\u0141\3\2\2\2C\u0143\3\2\2\2E\u0145\3\2\2\2G\u0147")
        buf.write("\3\2\2\2I\u014a\3\2\2\2K\u014d\3\2\2\2M\u0150\3\2\2\2")
        buf.write("O\u0152\3\2\2\2Q\u0155\3\2\2\2S\u0158\3\2\2\2U\u015b\3")
        buf.write("\2\2\2W\u015d\3\2\2\2Y\u015f\3\2\2\2[\u0163\3\2\2\2]\u0166")
        buf.write("\3\2\2\2_\u0168\3\2\2\2a\u016a\3\2\2\2c\u016c\3\2\2\2")
        buf.write("e\u016e\3\2\2\2g\u0170\3\2\2\2i\u0172\3\2\2\2k\u0174\3")
        buf.write("\2\2\2m\u0176\3\2\2\2o\u0178\3\2\2\2q\u0187\3\2\2\2s\u0189")
        buf.write("\3\2\2\2u\u018b\3\2\2\2w\u0195\3\2\2\2y\u019e\3\2\2\2")
        buf.write("{\u01bf\3\2\2\2}\u01c3\3\2\2\2\177\u01cb\3\2\2\2\u0081")
        buf.write("\u01dd\3\2\2\2\u0083\u01ee\3\2\2\2\u0085\u0209\3\2\2\2")
        buf.write("\u0087\u020b\3\2\2\2\u0089\u0214\3\2\2\2\u008b\u0222\3")
        buf.write("\2\2\2\u008d\u0224\3\2\2\2\u008f\u022a\3\2\2\2\u0091\u022c")
        buf.write("\3\2\2\2\u0093\u023b\3\2\2\2\u0095\u0241\3\2\2\2\u0097")
        buf.write("\u0245\3\2\2\2\u0099\u0249\3\2\2\2\u009b\u024b\3\2\2\2")
        buf.write("\u009d\u024d\3\2\2\2\u009f\u00a0\7D\2\2\u00a0\u00a1\7")
        buf.write("t\2\2\u00a1\u00a2\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7m\2\2\u00a4\4\3\2\2\2\u00a5\u00a6\7E\2\2\u00a6\u00a7")
        buf.write("\7q\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa")
        buf.write("\7k\2\2\u00aa\u00ab\7p\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad")
        buf.write("\7g\2\2\u00ad\6\3\2\2\2\u00ae\u00af\7K\2\2\u00af\u00b0")
        buf.write("\7h\2\2\u00b0\b\3\2\2\2\u00b1\u00b2\7G\2\2\u00b2\u00b3")
        buf.write("\7n\2\2\u00b3\u00b4\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6")
        buf.write("\7k\2\2\u00b6\u00b7\7h\2\2\u00b7\n\3\2\2\2\u00b8\u00b9")
        buf.write("\7G\2\2\u00b9\u00ba\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc")
        buf.write("\7g\2\2\u00bc\f\3\2\2\2\u00bd\u00be\7H\2\2\u00be\u00bf")
        buf.write("\7q\2\2\u00bf\u00c0\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2")
        buf.write("\7c\2\2\u00c2\u00c3\7e\2\2\u00c3\u00c4\7j\2\2\u00c4\16")
        buf.write("\3\2\2\2\u00c5\u00c8\5\21\t\2\u00c6\u00c8\5\23\n\2\u00c7")
        buf.write("\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\20\3\2\2\2\u00c9")
        buf.write("\u00ca\7V\2\2\u00ca\u00cb\7t\2\2\u00cb\u00cc\7w\2\2\u00cc")
        buf.write("\u00cd\7g\2\2\u00cd\22\3\2\2\2\u00ce\u00cf\7H\2\2\u00cf")
        buf.write("\u00d0\7c\2\2\u00d0\u00d1\7n\2\2\u00d1\u00d2\7u\2\2\u00d2")
        buf.write("\u00d3\7g\2\2\u00d3\24\3\2\2\2\u00d4\u00d5\7C\2\2\u00d5")
        buf.write("\u00d6\7t\2\2\u00d6\u00d7\7t\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write("\u00d9\7{\2\2\u00d9\26\3\2\2\2\u00da\u00db\7K\2\2\u00db")
        buf.write("\u00dc\7p\2\2\u00dc\30\3\2\2\2\u00dd\u00de\7K\2\2\u00de")
        buf.write("\u00df\7p\2\2\u00df\u00e0\7v\2\2\u00e0\32\3\2\2\2\u00e1")
        buf.write("\u00e2\7H\2\2\u00e2\u00e3\7n\2\2\u00e3\u00e4\7q\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e6\7v\2\2\u00e6\34\3\2\2\2\u00e7")
        buf.write("\u00e8\7D\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7q\2\2\u00ea")
        buf.write("\u00eb\7n\2\2\u00eb\u00ec\7g\2\2\u00ec\u00ed\7c\2\2\u00ed")
        buf.write("\u00ee\7p\2\2\u00ee\36\3\2\2\2\u00ef\u00f0\7U\2\2\u00f0")
        buf.write("\u00f1\7v\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7k\2\2\u00f3")
        buf.write("\u00f4\7p\2\2\u00f4\u00f5\7i\2\2\u00f5 \3\2\2\2\u00f6")
        buf.write("\u00f7\7T\2\2\u00f7\u00f8\7g\2\2\u00f8\u00f9\7v\2\2\u00f9")
        buf.write("\u00fa\7w\2\2\u00fa\u00fb\7t\2\2\u00fb\u00fc\7p\2\2\u00fc")
        buf.write("\"\3\2\2\2\u00fd\u00fe\7P\2\2\u00fe\u00ff\7w\2\2\u00ff")
        buf.write("\u0100\7n\2\2\u0100\u0101\7n\2\2\u0101$\3\2\2\2\u0102")
        buf.write("\u0103\7E\2\2\u0103\u0104\7n\2\2\u0104\u0105\7c\2\2\u0105")
        buf.write("\u0106\7u\2\2\u0106\u0107\7u\2\2\u0107&\3\2\2\2\u0108")
        buf.write("\u0109\7X\2\2\u0109\u010a\7c\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("(\3\2\2\2\u010c\u010d\7X\2\2\u010d\u010e\7c\2\2\u010e")
        buf.write("\u010f\7t\2\2\u010f*\3\2\2\2\u0110\u0111\7E\2\2\u0111")
        buf.write("\u0112\7q\2\2\u0112\u0113\7p\2\2\u0113\u0114\7u\2\2\u0114")
        buf.write("\u0115\7v\2\2\u0115\u0116\7t\2\2\u0116\u0117\7w\2\2\u0117")
        buf.write("\u0118\7e\2\2\u0118\u0119\7v\2\2\u0119\u011a\7q\2\2\u011a")
        buf.write("\u011b\7t\2\2\u011b,\3\2\2\2\u011c\u011d\7F\2\2\u011d")
        buf.write("\u011e\7g\2\2\u011e\u011f\7u\2\2\u011f\u0120\7v\2\2\u0120")
        buf.write("\u0121\7t\2\2\u0121\u0122\7w\2\2\u0122\u0123\7e\2\2\u0123")
        buf.write("\u0124\7v\2\2\u0124\u0125\7q\2\2\u0125\u0126\7t\2\2\u0126")
        buf.write(".\3\2\2\2\u0127\u0128\7P\2\2\u0128\u0129\7g\2\2\u0129")
        buf.write("\u012a\7y\2\2\u012a\60\3\2\2\2\u012b\u012c\7D\2\2\u012c")
        buf.write("\u012d\7{\2\2\u012d\62\3\2\2\2\u012e\u012f\7U\2\2\u012f")
        buf.write("\u0130\7g\2\2\u0130\u0131\7n\2\2\u0131\u0132\7h\2\2\u0132")
        buf.write("\64\3\2\2\2\u0133\u0134\7<\2\2\u0134\u0135\7<\2\2\u0135")
        buf.write("\66\3\2\2\2\u0136\u0137\7\60\2\2\u0137\u0138\7\60\2\2")
        buf.write("\u01388\3\2\2\2\u0139\u013a\7a\2\2\u013a:\3\2\2\2\u013b")
        buf.write("\u013c\7-\2\2\u013c<\3\2\2\2\u013d\u013e\7/\2\2\u013e")
        buf.write(">\3\2\2\2\u013f\u0140\7,\2\2\u0140@\3\2\2\2\u0141\u0142")
        buf.write("\7\61\2\2\u0142B\3\2\2\2\u0143\u0144\7\'\2\2\u0144D\3")
        buf.write("\2\2\2\u0145\u0146\7#\2\2\u0146F\3\2\2\2\u0147\u0148\7")
        buf.write("(\2\2\u0148\u0149\7(\2\2\u0149H\3\2\2\2\u014a\u014b\7")
        buf.write("~\2\2\u014b\u014c\7~\2\2\u014cJ\3\2\2\2\u014d\u014e\7")
        buf.write("?\2\2\u014e\u014f\7?\2\2\u014fL\3\2\2\2\u0150\u0151\7")
        buf.write("?\2\2\u0151N\3\2\2\2\u0152\u0153\7#\2\2\u0153\u0154\7")
        buf.write("?\2\2\u0154P\3\2\2\2\u0155\u0156\7@\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157R\3\2\2\2\u0158\u0159\7>\2\2\u0159\u015a\7")
        buf.write("?\2\2\u015aT\3\2\2\2\u015b\u015c\7@\2\2\u015cV\3\2\2\2")
        buf.write("\u015d\u015e\7>\2\2\u015eX\3\2\2\2\u015f\u0160\7?\2\2")
        buf.write("\u0160\u0161\7?\2\2\u0161\u0162\7\60\2\2\u0162Z\3\2\2")
        buf.write("\2\u0163\u0164\7-\2\2\u0164\u0165\7\60\2\2\u0165\\\3\2")
        buf.write("\2\2\u0166\u0167\7*\2\2\u0167^\3\2\2\2\u0168\u0169\7+")
        buf.write("\2\2\u0169`\3\2\2\2\u016a\u016b\7]\2\2\u016bb\3\2\2\2")
        buf.write("\u016c\u016d\7_\2\2\u016dd\3\2\2\2\u016e\u016f\7}\2\2")
        buf.write("\u016ff\3\2\2\2\u0170\u0171\7\177\2\2\u0171h\3\2\2\2\u0172")
        buf.write("\u0173\7\60\2\2\u0173j\3\2\2\2\u0174\u0175\7.\2\2\u0175")
        buf.write("l\3\2\2\2\u0176\u0177\7<\2\2\u0177n\3\2\2\2\u0178\u0179")
        buf.write("\7=\2\2\u0179p\3\2\2\2\u017a\u017c\5s:\2\u017b\u017d\t")
        buf.write("\2\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017f\3\2\2\2\u017f\u0188\3\2\2\2\u0180")
        buf.write("\u0184\t\3\2\2\u0181\u0183\t\2\2\2\u0182\u0181\3\2\2\2")
        buf.write("\u0183\u0186\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3")
        buf.write("\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0187\u017a")
        buf.write("\3\2\2\2\u0187\u0180\3\2\2\2\u0188r\3\2\2\2\u0189\u018a")
        buf.write("\7&\2\2\u018at\3\2\2\2\u018b\u018f\7$\2\2\u018c\u018e")
        buf.write("\5\u008bF\2\u018d\u018c\3\2\2\2\u018e\u0191\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192\3\2\2\2")
        buf.write("\u0191\u018f\3\2\2\2\u0192\u0193\7$\2\2\u0193\u0194\b")
        buf.write(";\2\2\u0194v\3\2\2\2\u0195\u0199\7\60\2\2\u0196\u0198")
        buf.write("\7\62\2\2\u0197\u0196\3\2\2\2\u0198\u019b\3\2\2\2\u0199")
        buf.write("\u0197\3\2\2\2\u0199\u019a\3\2\2\2\u019a\u019c\3\2\2\2")
        buf.write("\u019b\u0199\3\2\2\2\u019c\u019d\5}?\2\u019dx\3\2\2\2")
        buf.write("\u019e\u01a1\5\u009bN\2\u019f\u01a2\5=\37\2\u01a0\u01a2")
        buf.write("\5;\36\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u01a6\3\2\2\2\u01a3\u01a5\7\62\2")
        buf.write("\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4")
        buf.write("\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a9\u01aa\5}?\2\u01aaz\3\2\2\2\u01ab")
        buf.write("\u01b4\5}?\2\u01ac\u01b0\7\62\2\2\u01ad\u01af\t\4\2\2")
        buf.write("\u01ae\u01ad\3\2\2\2\u01af\u01b2\3\2\2\2\u01b0\u01ae\3")
        buf.write("\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b0")
        buf.write("\3\2\2\2\u01b3\u01ab\3\2\2\2\u01b3\u01ac\3\2\2\2\u01b4")
        buf.write("\u01ba\3\2\2\2\u01b5\u01b7\5w<\2\u01b6\u01b8\5y=\2\u01b7")
        buf.write("\u01b6\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01bb\3\2\2\2")
        buf.write("\u01b9\u01bb\5y=\2\u01ba\u01b5\3\2\2\2\u01ba\u01b9\3\2")
        buf.write("\2\2\u01bb\u01c0\3\2\2\2\u01bc\u01bd\5w<\2\u01bd\u01be")
        buf.write("\5y=\2\u01be\u01c0\3\2\2\2\u01bf\u01b3\3\2\2\2\u01bf\u01bc")
        buf.write("\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1\u01c2\b>\3\2\u01c2")
        buf.write("|\3\2\2\2\u01c3\u01c8\t\5\2\2\u01c4\u01c7\59\35\2\u01c5")
        buf.write("\u01c7\t\4\2\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2")
        buf.write("\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c9\3")
        buf.write("\2\2\2\u01c9~\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb\u01cc")
        buf.write("\7\62\2\2\u01cc\u01ce\5\u009dO\2\u01cd\u01cf\t\6\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01da\3\2\2\2\u01d2\u01d4\5")
        buf.write("9\35\2\u01d3\u01d5\t\6\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6")
        buf.write("\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01d9\3\2\2\2\u01d8\u01d2\3\2\2\2\u01d9\u01dc\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u0080\3")
        buf.write("\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01df\7\62\2\2\u01de")
        buf.write("\u01e0\t\7\2\2\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2")
        buf.write("\u01e1\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01eb\3")
        buf.write("\2\2\2\u01e3\u01e5\59\35\2\u01e4\u01e6\t\7\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e3\3\2\2\2")
        buf.write("\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec\3")
        buf.write("\2\2\2\u01ec\u0082\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee\u01ef")
        buf.write("\7\62\2\2\u01ef\u01f1\5\u0099M\2\u01f0\u01f2\t\b\2\2\u01f1")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f1\3\2\2\2")
        buf.write("\u01f3\u01f4\3\2\2\2\u01f4\u01fd\3\2\2\2\u01f5\u01f7\5")
        buf.write("9\35\2\u01f6\u01f8\t\b\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9")
        buf.write("\3\2\2\2\u01f9\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa")
        buf.write("\u01fc\3\2\2\2\u01fb\u01f5\3\2\2\2\u01fc\u01ff\3\2\2\2")
        buf.write("\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0084\3")
        buf.write("\2\2\2\u01ff\u01fd\3\2\2\2\u0200\u0205\5}?\2\u0201\u0205")
        buf.write("\5\177@\2\u0202\u0205\5\u0081A\2\u0203\u0205\5\u0083B")
        buf.write("\2\u0204\u0200\3\2\2\2\u0204\u0201\3\2\2\2\u0204\u0202")
        buf.write("\3\2\2\2\u0204\u0203\3\2\2\2\u0205\u0206\3\2\2\2\u0206")
        buf.write("\u0207\bC\4\2\u0207\u020a\3\2\2\2\u0208\u020a\7\62\2\2")
        buf.write("\u0209\u0204\3\2\2\2\u0209\u0208\3\2\2\2\u020a\u0086\3")
        buf.write("\2\2\2\u020b\u020f\7$\2\2\u020c\u020e\5\u008bF\2\u020d")
        buf.write("\u020c\3\2\2\2\u020e\u0211\3\2\2\2\u020f\u020d\3\2\2\2")
        buf.write("\u020f\u0210\3\2\2\2\u0210\u0212\3\2\2\2\u0211\u020f\3")
        buf.write("\2\2\2\u0212\u0213\bD\5\2\u0213\u0088\3\2\2\2\u0214\u0218")
        buf.write("\7$\2\2\u0215\u0217\5\u008bF\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u021a\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2")
        buf.write("\u0219\u021b\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021c\5")
        buf.write("\u008fH\2\u021c\u021d\bE\6\2\u021d\u008a\3\2\2\2\u021e")
        buf.write("\u0223\n\t\2\2\u021f\u0223\5\u008dG\2\u0220\u0221\7)\2")
        buf.write("\2\u0221\u0223\7$\2\2\u0222\u021e\3\2\2\2\u0222\u021f")
        buf.write("\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u008c\3\2\2\2\u0224")
        buf.write("\u0225\7^\2\2\u0225\u0226\t\n\2\2\u0226\u008e\3\2\2\2")
        buf.write("\u0227\u0228\7^\2\2\u0228\u022b\n\n\2\2\u0229\u022b\n")
        buf.write("\13\2\2\u022a\u0227\3\2\2\2\u022a\u0229\3\2\2\2\u022b")
        buf.write("\u0090\3\2\2\2\u022c\u022d\7%\2\2\u022d\u022e\7%\2\2\u022e")
        buf.write("\u0232\3\2\2\2\u022f\u0231\13\2\2\2\u0230\u022f\3\2\2")
        buf.write("\2\u0231\u0234\3\2\2\2\u0232\u0233\3\2\2\2\u0232\u0230")
        buf.write("\3\2\2\2\u0233\u0235\3\2\2\2\u0234\u0232\3\2\2\2\u0235")
        buf.write("\u0236\7%\2\2\u0236\u0237\7%\2\2\u0237\u0238\3\2\2\2\u0238")
        buf.write("\u0239\bI\7\2\u0239\u0092\3\2\2\2\u023a\u023c\t\f\2\2")
        buf.write("\u023b\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u023b\3")
        buf.write("\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\3\2\2\2\u023f\u0240")
        buf.write("\bJ\7\2\u0240\u0094\3\2\2\2\u0241\u0242\13\2\2\2\u0242")
        buf.write("\u0243\bK\b\2\u0243\u0096\3\2\2\2\u0244\u0246\t\3\2\2")
        buf.write("\u0245\u0244\3\2\2\2\u0246\u0247\3\2\2\2\u0247\u0245\3")
        buf.write("\2\2\2\u0247\u0248\3\2\2\2\u0248\u0098\3\2\2\2\u0249\u024a")
        buf.write("\t\r\2\2\u024a\u009a\3\2\2\2\u024b\u024c\t\16\2\2\u024c")
        buf.write("\u009c\3\2\2\2\u024d\u024e\t\17\2\2\u024e\u009e\3\2\2")
        buf.write("\2$\2\u00c7\u017e\u0184\u0187\u018f\u0199\u01a1\u01a6")
        buf.write("\u01b0\u01b3\u01b7\u01ba\u01bf\u01c6\u01c8\u01d0\u01d6")
        buf.write("\u01da\u01e1\u01e7\u01eb\u01f3\u01f9\u01fd\u0204\u0209")
        buf.write("\u020f\u0218\u0222\u022a\u0232\u023d\u0247\t\3;\2\3>\3")
        buf.write("\3C\4\3D\5\3E\6\b\2\2\3K\7")
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
    NOTEQUAL = 39
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
    IDENTIFIERS = 56
    STRINGLIT = 57
    FLOATLIT = 58
    INTLIT = 59
    UNCLOSE_STRING = 60
    ILLEGAL_ESCAPE = 61
    BLOCK_COMMENT = 62
    WS = 63
    ERROR_CHAR = 64
    ID = 65

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
            "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLLIT", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
            "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
            "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GTE", "LTE", 
            "GT", "LT", "STREQUALOP", "STRCONCATOP", "LB", "RB", "LSB", 
            "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", "IDENTIFIERS", 
            "STRINGLIT", "FLOATLIT", "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR", "ID" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "BOOLLIT", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GTE", 
                  "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", "LB", 
                  "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", 
                  "SEMICOLON", "IDENTIFIERS", "DOLLAR", "STRINGLIT", "DECIMALPART", 
                  "EXPONENTPART", "FLOATLIT", "DEC", "HEX", "OCT", "BIN", 
                  "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "STRING_CHAR", 
                  "ESC_CHAR", "ESC_UNAVAILABLE", "BLOCK_COMMENT", "WS", 
                  "ERROR_CHAR", "ID", "B", "E", "X" ]

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
            actions[57] = self.STRINGLIT_action 
            actions[60] = self.FLOATLIT_action 
            actions[65] = self.INTLIT_action 
            actions[66] = self.UNCLOSE_STRING_action 
            actions[67] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
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
            	raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             raise ErrorToken(self.text) 
     


