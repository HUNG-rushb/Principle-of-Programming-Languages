# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u02ba\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\5\b\u00c6\n\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write("-\3.\3.\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\3")
        buf.write("9\69\u017b\n9\r9\169\u017c\39\39\79\u0181\n9\f9\169\u0184")
        buf.write("\139\59\u0186\n9\3:\3:\3;\3;\7;\u018c\n;\f;\16;\u018f")
        buf.write("\13;\3;\3;\3;\3<\7<\u0195\n<\f<\16<\u0198\13<\3<\3<\7")
        buf.write("<\u019c\n<\f<\16<\u019f\13<\3<\6<\u01a2\n<\r<\16<\u01a3")
        buf.write("\3<\7<\u01a7\n<\f<\16<\u01aa\13<\3<\7<\u01ad\n<\f<\16")
        buf.write("<\u01b0\13<\3<\5<\u01b3\n<\3<\7<\u01b6\n<\f<\16<\u01b9")
        buf.write("\13<\3=\7=\u01bc\n=\f=\16=\u01bf\13=\3=\3=\7=\u01c3\n")
        buf.write("=\f=\16=\u01c6\13=\3=\3=\5=\u01ca\n=\3=\7=\u01cd\n=\f")
        buf.write("=\16=\u01d0\13=\3=\7=\u01d3\n=\f=\16=\u01d6\13=\3=\7=")
        buf.write("\u01d9\n=\f=\16=\u01dc\13=\3=\3=\6=\u01e0\n=\r=\16=\u01e1")
        buf.write("\5=\u01e4\n=\3=\7=\u01e7\n=\f=\16=\u01ea\13=\3>\7>\u01ed")
        buf.write("\n>\f>\16>\u01f0\13>\3>\3>\5>\u01f4\n>\3>\7>\u01f7\n>")
        buf.write("\f>\16>\u01fa\13>\3>\3>\7>\u01fe\n>\f>\16>\u0201\13>\3")
        buf.write(">\3>\3>\7>\u0206\n>\f>\16>\u0209\13>\3>\3>\5>\u020d\n")
        buf.write(">\3>\7>\u0210\n>\f>\16>\u0213\13>\3>\3>\7>\u0217\n>\f")
        buf.write(">\16>\u021a\13>\3>\3>\5>\u021e\n>\3>\7>\u0221\n>\f>\16")
        buf.write(">\u0224\13>\3>\5>\u0227\n>\3>\3>\3?\3?\3?\7?\u022e\n?")
        buf.write("\f?\16?\u0231\13?\3@\3@\3@\3@\6@\u0237\n@\r@\16@\u0238")
        buf.write("\5@\u023b\n@\3@\3@\6@\u023f\n@\r@\16@\u0240\7@\u0243\n")
        buf.write("@\f@\16@\u0246\13@\3A\3A\3A\6A\u024b\nA\rA\16A\u024c\5")
        buf.write("A\u024f\nA\3A\3A\6A\u0253\nA\rA\16A\u0254\7A\u0257\nA")
        buf.write("\fA\16A\u025a\13A\3B\3B\3B\3B\6B\u0260\nB\rB\16B\u0261")
        buf.write("\5B\u0264\nB\3B\3B\6B\u0268\nB\rB\16B\u0269\7B\u026c\n")
        buf.write("B\fB\16B\u026f\13B\3C\3C\3C\3C\5C\u0275\nC\3C\3C\3C\5")
        buf.write("C\u027a\nC\3D\3D\7D\u027e\nD\fD\16D\u0281\13D\3D\3D\3")
        buf.write("E\3E\7E\u0287\nE\fE\16E\u028a\13E\3E\3E\3E\3F\3F\3F\3")
        buf.write("F\5F\u0293\nF\3G\3G\3G\3H\3H\3H\5H\u029b\nH\3I\3I\3I\3")
        buf.write("I\7I\u02a1\nI\fI\16I\u02a4\13I\3I\3I\3I\3I\3I\3J\6J\u02ac")
        buf.write("\nJ\rJ\16J\u02ad\3J\3J\3K\3K\3K\3L\3L\3M\3M\3N\3N\3\u02a2")
        buf.write("\2O\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s\2u;w\2y\2{<}\2\177\2\u0081\2\u0083\2\u0085=\u0087>")
        buf.write("\u0089?\u008b\2\u008d\2\u008f\2\u0091@\u0093A\u0095B\u0097")
        buf.write("\2\u0099\2\u009b\2\3\2\21\6\2\62;C\\aac|\5\2C\\aac|\3")
        buf.write("\2\63;\3\2\62;\5\2\62;CHch\3\2\629\3\2\62\63\4\2$$^^\t")
        buf.write("\2))^^ddhhppttvv\n\2$$))^^ddhhppttvv\3\2^^\5\2\n\f\16")
        buf.write("\17\"\"\4\2DDdd\4\2GGgg\4\2ZZzz\2\u02e7\2\3\3\2\2\2\2")
        buf.write("\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3")
        buf.write("\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2")
        buf.write("\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2")
        buf.write("\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3")
        buf.write("\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61")
        buf.write("\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2")
        buf.write("\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3")
        buf.write("\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M")
        buf.write("\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2")
        buf.write("W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2")
        buf.write("\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2")
        buf.write("\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2u\3\2")
        buf.write("\2\2\2{\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\3\u009d\3\2\2\2\5\u00a3\3\2\2\2\7\u00ac\3\2\2\2\t\u00af")
        buf.write("\3\2\2\2\13\u00b6\3\2\2\2\r\u00bb\3\2\2\2\17\u00c5\3\2")
        buf.write("\2\2\21\u00c7\3\2\2\2\23\u00cc\3\2\2\2\25\u00d2\3\2\2")
        buf.write("\2\27\u00d8\3\2\2\2\31\u00db\3\2\2\2\33\u00df\3\2\2\2")
        buf.write("\35\u00e5\3\2\2\2\37\u00ed\3\2\2\2!\u00f4\3\2\2\2#\u00fb")
        buf.write("\3\2\2\2%\u0100\3\2\2\2\'\u0106\3\2\2\2)\u010a\3\2\2\2")
        buf.write("+\u010e\3\2\2\2-\u011a\3\2\2\2/\u0125\3\2\2\2\61\u0129")
        buf.write("\3\2\2\2\63\u012c\3\2\2\2\65\u0131\3\2\2\2\67\u0134\3")
        buf.write("\2\2\29\u0137\3\2\2\2;\u0139\3\2\2\2=\u013b\3\2\2\2?\u013d")
        buf.write("\3\2\2\2A\u013f\3\2\2\2C\u0141\3\2\2\2E\u0143\3\2\2\2")
        buf.write("G\u0145\3\2\2\2I\u0148\3\2\2\2K\u014b\3\2\2\2M\u014e\3")
        buf.write("\2\2\2O\u0150\3\2\2\2Q\u0153\3\2\2\2S\u0156\3\2\2\2U\u0159")
        buf.write("\3\2\2\2W\u015b\3\2\2\2Y\u015d\3\2\2\2[\u0161\3\2\2\2")
        buf.write("]\u0164\3\2\2\2_\u0166\3\2\2\2a\u0168\3\2\2\2c\u016a\3")
        buf.write("\2\2\2e\u016c\3\2\2\2g\u016e\3\2\2\2i\u0170\3\2\2\2k\u0172")
        buf.write("\3\2\2\2m\u0174\3\2\2\2o\u0176\3\2\2\2q\u0185\3\2\2\2")
        buf.write("s\u0187\3\2\2\2u\u0189\3\2\2\2w\u0196\3\2\2\2y\u01bd\3")
        buf.write("\2\2\2{\u0226\3\2\2\2}\u022a\3\2\2\2\177\u0232\3\2\2\2")
        buf.write("\u0081\u0247\3\2\2\2\u0083\u025b\3\2\2\2\u0085\u0279\3")
        buf.write("\2\2\2\u0087\u027b\3\2\2\2\u0089\u0284\3\2\2\2\u008b\u0292")
        buf.write("\3\2\2\2\u008d\u0294\3\2\2\2\u008f\u029a\3\2\2\2\u0091")
        buf.write("\u029c\3\2\2\2\u0093\u02ab\3\2\2\2\u0095\u02b1\3\2\2\2")
        buf.write("\u0097\u02b4\3\2\2\2\u0099\u02b6\3\2\2\2\u009b\u02b8\3")
        buf.write("\2\2\2\u009d\u009e\7D\2\2\u009e\u009f\7t\2\2\u009f\u00a0")
        buf.write("\7g\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7m\2\2\u00a2\4")
        buf.write("\3\2\2\2\u00a3\u00a4\7E\2\2\u00a4\u00a5\7q\2\2\u00a5\u00a6")
        buf.write("\7p\2\2\u00a6\u00a7\7v\2\2\u00a7\u00a8\7k\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7w\2\2\u00aa\u00ab\7g\2\2\u00ab\6")
        buf.write("\3\2\2\2\u00ac\u00ad\7K\2\2\u00ad\u00ae\7h\2\2\u00ae\b")
        buf.write("\3\2\2\2\u00af\u00b0\7G\2\2\u00b0\u00b1\7n\2\2\u00b1\u00b2")
        buf.write("\7u\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7k\2\2\u00b4\u00b5")
        buf.write("\7h\2\2\u00b5\n\3\2\2\2\u00b6\u00b7\7G\2\2\u00b7\u00b8")
        buf.write("\7n\2\2\u00b8\u00b9\7u\2\2\u00b9\u00ba\7g\2\2\u00ba\f")
        buf.write("\3\2\2\2\u00bb\u00bc\7H\2\2\u00bc\u00bd\7q\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7g\2\2\u00bf\u00c0\7c\2\2\u00c0\u00c1")
        buf.write("\7e\2\2\u00c1\u00c2\7j\2\2\u00c2\16\3\2\2\2\u00c3\u00c6")
        buf.write("\5\21\t\2\u00c4\u00c6\5\23\n\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c4\3\2\2\2\u00c6\20\3\2\2\2\u00c7\u00c8\7V\2\2\u00c8")
        buf.write("\u00c9\7t\2\2\u00c9\u00ca\7w\2\2\u00ca\u00cb\7g\2\2\u00cb")
        buf.write("\22\3\2\2\2\u00cc\u00cd\7H\2\2\u00cd\u00ce\7c\2\2\u00ce")
        buf.write("\u00cf\7n\2\2\u00cf\u00d0\7u\2\2\u00d0\u00d1\7g\2\2\u00d1")
        buf.write("\24\3\2\2\2\u00d2\u00d3\7C\2\2\u00d3\u00d4\7t\2\2\u00d4")
        buf.write("\u00d5\7t\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7{\2\2\u00d7")
        buf.write("\26\3\2\2\2\u00d8\u00d9\7K\2\2\u00d9\u00da\7p\2\2\u00da")
        buf.write("\30\3\2\2\2\u00db\u00dc\7K\2\2\u00dc\u00dd\7p\2\2\u00dd")
        buf.write("\u00de\7v\2\2\u00de\32\3\2\2\2\u00df\u00e0\7H\2\2\u00e0")
        buf.write("\u00e1\7n\2\2\u00e1\u00e2\7q\2\2\u00e2\u00e3\7c\2\2\u00e3")
        buf.write("\u00e4\7v\2\2\u00e4\34\3\2\2\2\u00e5\u00e6\7D\2\2\u00e6")
        buf.write("\u00e7\7q\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9\7n\2\2\u00e9")
        buf.write("\u00ea\7g\2\2\u00ea\u00eb\7c\2\2\u00eb\u00ec\7p\2\2\u00ec")
        buf.write("\36\3\2\2\2\u00ed\u00ee\7U\2\2\u00ee\u00ef\7v\2\2\u00ef")
        buf.write("\u00f0\7t\2\2\u00f0\u00f1\7k\2\2\u00f1\u00f2\7p\2\2\u00f2")
        buf.write("\u00f3\7i\2\2\u00f3 \3\2\2\2\u00f4\u00f5\7T\2\2\u00f5")
        buf.write("\u00f6\7g\2\2\u00f6\u00f7\7v\2\2\u00f7\u00f8\7w\2\2\u00f8")
        buf.write("\u00f9\7t\2\2\u00f9\u00fa\7p\2\2\u00fa\"\3\2\2\2\u00fb")
        buf.write("\u00fc\7P\2\2\u00fc\u00fd\7w\2\2\u00fd\u00fe\7n\2\2\u00fe")
        buf.write("\u00ff\7n\2\2\u00ff$\3\2\2\2\u0100\u0101\7E\2\2\u0101")
        buf.write("\u0102\7n\2\2\u0102\u0103\7c\2\2\u0103\u0104\7u\2\2\u0104")
        buf.write("\u0105\7u\2\2\u0105&\3\2\2\2\u0106\u0107\7X\2\2\u0107")
        buf.write("\u0108\7c\2\2\u0108\u0109\7n\2\2\u0109(\3\2\2\2\u010a")
        buf.write("\u010b\7X\2\2\u010b\u010c\7c\2\2\u010c\u010d\7t\2\2\u010d")
        buf.write("*\3\2\2\2\u010e\u010f\7E\2\2\u010f\u0110\7q\2\2\u0110")
        buf.write("\u0111\7p\2\2\u0111\u0112\7u\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\u0114\7t\2\2\u0114\u0115\7w\2\2\u0115\u0116\7e\2\2\u0116")
        buf.write("\u0117\7v\2\2\u0117\u0118\7q\2\2\u0118\u0119\7t\2\2\u0119")
        buf.write(",\3\2\2\2\u011a\u011b\7F\2\2\u011b\u011c\7g\2\2\u011c")
        buf.write("\u011d\7u\2\2\u011d\u011e\7v\2\2\u011e\u011f\7t\2\2\u011f")
        buf.write("\u0120\7w\2\2\u0120\u0121\7e\2\2\u0121\u0122\7v\2\2\u0122")
        buf.write("\u0123\7q\2\2\u0123\u0124\7t\2\2\u0124.\3\2\2\2\u0125")
        buf.write("\u0126\7P\2\2\u0126\u0127\7g\2\2\u0127\u0128\7y\2\2\u0128")
        buf.write("\60\3\2\2\2\u0129\u012a\7D\2\2\u012a\u012b\7{\2\2\u012b")
        buf.write("\62\3\2\2\2\u012c\u012d\7U\2\2\u012d\u012e\7g\2\2\u012e")
        buf.write("\u012f\7n\2\2\u012f\u0130\7h\2\2\u0130\64\3\2\2\2\u0131")
        buf.write("\u0132\7<\2\2\u0132\u0133\7<\2\2\u0133\66\3\2\2\2\u0134")
        buf.write("\u0135\7\60\2\2\u0135\u0136\7\60\2\2\u01368\3\2\2\2\u0137")
        buf.write("\u0138\7a\2\2\u0138:\3\2\2\2\u0139\u013a\7-\2\2\u013a")
        buf.write("<\3\2\2\2\u013b\u013c\7/\2\2\u013c>\3\2\2\2\u013d\u013e")
        buf.write("\7,\2\2\u013e@\3\2\2\2\u013f\u0140\7\61\2\2\u0140B\3\2")
        buf.write("\2\2\u0141\u0142\7\'\2\2\u0142D\3\2\2\2\u0143\u0144\7")
        buf.write("#\2\2\u0144F\3\2\2\2\u0145\u0146\7(\2\2\u0146\u0147\7")
        buf.write("(\2\2\u0147H\3\2\2\2\u0148\u0149\7~\2\2\u0149\u014a\7")
        buf.write("~\2\2\u014aJ\3\2\2\2\u014b\u014c\7?\2\2\u014c\u014d\7")
        buf.write("?\2\2\u014dL\3\2\2\2\u014e\u014f\7?\2\2\u014fN\3\2\2\2")
        buf.write("\u0150\u0151\7#\2\2\u0151\u0152\7?\2\2\u0152P\3\2\2\2")
        buf.write("\u0153\u0154\7@\2\2\u0154\u0155\7?\2\2\u0155R\3\2\2\2")
        buf.write("\u0156\u0157\7>\2\2\u0157\u0158\7?\2\2\u0158T\3\2\2\2")
        buf.write("\u0159\u015a\7@\2\2\u015aV\3\2\2\2\u015b\u015c\7>\2\2")
        buf.write("\u015cX\3\2\2\2\u015d\u015e\7?\2\2\u015e\u015f\7?\2\2")
        buf.write("\u015f\u0160\7\60\2\2\u0160Z\3\2\2\2\u0161\u0162\7-\2")
        buf.write("\2\u0162\u0163\7\60\2\2\u0163\\\3\2\2\2\u0164\u0165\7")
        buf.write("*\2\2\u0165^\3\2\2\2\u0166\u0167\7+\2\2\u0167`\3\2\2\2")
        buf.write("\u0168\u0169\7]\2\2\u0169b\3\2\2\2\u016a\u016b\7_\2\2")
        buf.write("\u016bd\3\2\2\2\u016c\u016d\7}\2\2\u016df\3\2\2\2\u016e")
        buf.write("\u016f\7\177\2\2\u016fh\3\2\2\2\u0170\u0171\7\60\2\2\u0171")
        buf.write("j\3\2\2\2\u0172\u0173\7.\2\2\u0173l\3\2\2\2\u0174\u0175")
        buf.write("\7<\2\2\u0175n\3\2\2\2\u0176\u0177\7=\2\2\u0177p\3\2\2")
        buf.write("\2\u0178\u017a\5s:\2\u0179\u017b\t\2\2\2\u017a\u0179\3")
        buf.write("\2\2\2\u017b\u017c\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017d")
        buf.write("\3\2\2\2\u017d\u0186\3\2\2\2\u017e\u0182\t\3\2\2\u017f")
        buf.write("\u0181\t\2\2\2\u0180\u017f\3\2\2\2\u0181\u0184\3\2\2\2")
        buf.write("\u0182\u0180\3\2\2\2\u0182\u0183\3\2\2\2\u0183\u0186\3")
        buf.write("\2\2\2\u0184\u0182\3\2\2\2\u0185\u0178\3\2\2\2\u0185\u017e")
        buf.write("\3\2\2\2\u0186r\3\2\2\2\u0187\u0188\7&\2\2\u0188t\3\2")
        buf.write("\2\2\u0189\u018d\7$\2\2\u018a\u018c\5\u008bF\2\u018b\u018a")
        buf.write("\3\2\2\2\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018d")
        buf.write("\u018e\3\2\2\2\u018e\u0190\3\2\2\2\u018f\u018d\3\2\2\2")
        buf.write("\u0190\u0191\7$\2\2\u0191\u0192\b;\2\2\u0192v\3\2\2\2")
        buf.write("\u0193\u0195\59\35\2\u0194\u0193\3\2\2\2\u0195\u0198\3")
        buf.write("\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197\3\2\2\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019d\7\60\2\2\u019a")
        buf.write("\u019c\59\35\2\u019b\u019a\3\2\2\2\u019c\u019f\3\2\2\2")
        buf.write("\u019d\u019b\3\2\2\2\u019d\u019e\3\2\2\2\u019e\u01b2\3")
        buf.write("\2\2\2\u019f\u019d\3\2\2\2\u01a0\u01a2\7\62\2\2\u01a1")
        buf.write("\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2")
        buf.write("\u01a3\u01a4\3\2\2\2\u01a4\u01b3\3\2\2\2\u01a5\u01a7\7")
        buf.write("\62\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8")
        buf.write("\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ae\3\2\2\2")
        buf.write("\u01aa\u01a8\3\2\2\2\u01ab\u01ad\59\35\2\u01ac\u01ab\3")
        buf.write("\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af")
        buf.write("\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1")
        buf.write("\u01b3\5}?\2\u01b2\u01a1\3\2\2\2\u01b2\u01a8\3\2\2\2\u01b3")
        buf.write("\u01b7\3\2\2\2\u01b4\u01b6\59\35\2\u01b5\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3")
        buf.write("\2\2\2\u01b8x\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba\u01bc")
        buf.write("\59\35\2\u01bb\u01ba\3\2\2\2\u01bc\u01bf\3\2\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01be\3\2\2\2\u01be\u01c0\3\2\2\2")
        buf.write("\u01bf\u01bd\3\2\2\2\u01c0\u01c4\5\u0099M\2\u01c1\u01c3")
        buf.write("\59\35\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01c9\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c7\u01ca\5=\37\2\u01c8\u01ca\5")
        buf.write(";\36\2\u01c9\u01c7\3\2\2\2\u01c9\u01c8\3\2\2\2\u01c9\u01ca")
        buf.write("\3\2\2\2\u01ca\u01ce\3\2\2\2\u01cb\u01cd\59\35\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2")
        buf.write("\u01ce\u01cf\3\2\2\2\u01cf\u01e3\3\2\2\2\u01d0\u01ce\3")
        buf.write("\2\2\2\u01d1\u01d3\7\62\2\2\u01d2\u01d1\3\2\2\2\u01d3")
        buf.write("\u01d6\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2")
        buf.write("\u01d5\u01da\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d7\u01d9\5")
        buf.write("9\35\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8")
        buf.write("\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd\3\2\2\2\u01dc")
        buf.write("\u01da\3\2\2\2\u01dd\u01e4\5}?\2\u01de\u01e0\7\62\2\2")
        buf.write("\u01df\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01df\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e4\3\2\2\2\u01e3\u01d4")
        buf.write("\3\2\2\2\u01e3\u01df\3\2\2\2\u01e4\u01e8\3\2\2\2\u01e5")
        buf.write("\u01e7\59\35\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9z\3\2\2")
        buf.write("\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\59\35\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f3\3\2\2\2\u01f0\u01ee\3\2\2\2")
        buf.write("\u01f1\u01f4\5}?\2\u01f2\u01f4\7\62\2\2\u01f3\u01f1\3")
        buf.write("\2\2\2\u01f3\u01f2\3\2\2\2\u01f4\u01f8\3\2\2\2\u01f5\u01f7")
        buf.write("\59\35\2\u01f6\u01f5\3\2\2\2\u01f7\u01fa\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9\u01fb\3\2\2\2")
        buf.write("\u01fa\u01f8\3\2\2\2\u01fb\u01ff\5w<\2\u01fc\u01fe\59")
        buf.write("\35\2\u01fd\u01fc\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd")
        buf.write("\3\2\2\2\u01ff\u0200\3\2\2\2\u0200\u0202\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0202\u0203\5y=\2\u0203\u0227\3\2\2\2\u0204")
        buf.write("\u0206\59\35\2\u0205\u0204\3\2\2\2\u0206\u0209\3\2\2\2")
        buf.write("\u0207\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020c\3")
        buf.write("\2\2\2\u0209\u0207\3\2\2\2\u020a\u020d\5}?\2\u020b\u020d")
        buf.write("\7\62\2\2\u020c\u020a\3\2\2\2\u020c\u020b\3\2\2\2\u020d")
        buf.write("\u0211\3\2\2\2\u020e\u0210\59\35\2\u020f\u020e\3\2\2\2")
        buf.write("\u0210\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3")
        buf.write("\2\2\2\u0212\u0214\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0227")
        buf.write("\5w<\2\u0215\u0217\59\35\2\u0216\u0215\3\2\2\2\u0217\u021a")
        buf.write("\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u021d\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u021e\5}?\2\u021c")
        buf.write("\u021e\7\62\2\2\u021d\u021b\3\2\2\2\u021d\u021c\3\2\2")
        buf.write("\2\u021e\u0222\3\2\2\2\u021f\u0221\59\35\2\u0220\u021f")
        buf.write("\3\2\2\2\u0221\u0224\3\2\2\2\u0222\u0220\3\2\2\2\u0222")
        buf.write("\u0223\3\2\2\2\u0223\u0225\3\2\2\2\u0224\u0222\3\2\2\2")
        buf.write("\u0225\u0227\5y=\2\u0226\u01ee\3\2\2\2\u0226\u0207\3\2")
        buf.write("\2\2\u0226\u0218\3\2\2\2\u0227\u0228\3\2\2\2\u0228\u0229")
        buf.write("\b>\3\2\u0229|\3\2\2\2\u022a\u022f\t\4\2\2\u022b\u022e")
        buf.write("\59\35\2\u022c\u022e\t\5\2\2\u022d\u022b\3\2\2\2\u022d")
        buf.write("\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230~\3\2\2\2\u0231\u022f\3\2\2")
        buf.write("\2\u0232\u0233\7\62\2\2\u0233\u023a\5\u009bN\2\u0234\u023b")
        buf.write("\59\35\2\u0235\u0237\t\6\2\2\u0236\u0235\3\2\2\2\u0237")
        buf.write("\u0238\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2")
        buf.write("\u0239\u023b\3\2\2\2\u023a\u0234\3\2\2\2\u023a\u0236\3")
        buf.write("\2\2\2\u023b\u0244\3\2\2\2\u023c\u023e\59\35\2\u023d\u023f")
        buf.write("\t\6\2\2\u023e\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240")
        buf.write("\u023e\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0243\3\2\2\2")
        buf.write("\u0242\u023c\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242\3")
        buf.write("\2\2\2\u0244\u0245\3\2\2\2\u0245\u0080\3\2\2\2\u0246\u0244")
        buf.write("\3\2\2\2\u0247\u024e\7\62\2\2\u0248\u024f\59\35\2\u0249")
        buf.write("\u024b\t\7\2\2\u024a\u0249\3\2\2\2\u024b\u024c\3\2\2\2")
        buf.write("\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024f\3")
        buf.write("\2\2\2\u024e\u0248\3\2\2\2\u024e\u024a\3\2\2\2\u024f\u0258")
        buf.write("\3\2\2\2\u0250\u0252\59\35\2\u0251\u0253\t\7\2\2\u0252")
        buf.write("\u0251\3\2\2\2\u0253\u0254\3\2\2\2\u0254\u0252\3\2\2\2")
        buf.write("\u0254\u0255\3\2\2\2\u0255\u0257\3\2\2\2\u0256\u0250\3")
        buf.write("\2\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u0082\3\2\2\2\u025a\u0258\3\2\2\2\u025b")
        buf.write("\u025c\7\62\2\2\u025c\u0263\5\u0097L\2\u025d\u0264\59")
        buf.write("\35\2\u025e\u0260\t\b\2\2\u025f\u025e\3\2\2\2\u0260\u0261")
        buf.write("\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262")
        buf.write("\u0264\3\2\2\2\u0263\u025d\3\2\2\2\u0263\u025f\3\2\2\2")
        buf.write("\u0264\u026d\3\2\2\2\u0265\u0267\59\35\2\u0266\u0268\t")
        buf.write("\b\2\2\u0267\u0266\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u0267")
        buf.write("\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026c\3\2\2\2\u026b")
        buf.write("\u0265\3\2\2\2\u026c\u026f\3\2\2\2\u026d\u026b\3\2\2\2")
        buf.write("\u026d\u026e\3\2\2\2\u026e\u0084\3\2\2\2\u026f\u026d\3")
        buf.write("\2\2\2\u0270\u0275\5}?\2\u0271\u0275\5\177@\2\u0272\u0275")
        buf.write("\5\u0081A\2\u0273\u0275\5\u0083B\2\u0274\u0270\3\2\2\2")
        buf.write("\u0274\u0271\3\2\2\2\u0274\u0272\3\2\2\2\u0274\u0273\3")
        buf.write("\2\2\2\u0275\u0276\3\2\2\2\u0276\u0277\bC\4\2\u0277\u027a")
        buf.write("\3\2\2\2\u0278\u027a\7\62\2\2\u0279\u0274\3\2\2\2\u0279")
        buf.write("\u0278\3\2\2\2\u027a\u0086\3\2\2\2\u027b\u027f\7$\2\2")
        buf.write("\u027c\u027e\5\u008bF\2\u027d\u027c\3\2\2\2\u027e\u0281")
        buf.write("\3\2\2\2\u027f\u027d\3\2\2\2\u027f\u0280\3\2\2\2\u0280")
        buf.write("\u0282\3\2\2\2\u0281\u027f\3\2\2\2\u0282\u0283\bD\5\2")
        buf.write("\u0283\u0088\3\2\2\2\u0284\u0288\7$\2\2\u0285\u0287\5")
        buf.write("\u008bF\2\u0286\u0285\3\2\2\2\u0287\u028a\3\2\2\2\u0288")
        buf.write("\u0286\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028b\3\2\2\2")
        buf.write("\u028a\u0288\3\2\2\2\u028b\u028c\5\u008fH\2\u028c\u028d")
        buf.write("\bE\6\2\u028d\u008a\3\2\2\2\u028e\u028f\7)\2\2\u028f\u0293")
        buf.write("\7$\2\2\u0290\u0293\5\u008dG\2\u0291\u0293\n\t\2\2\u0292")
        buf.write("\u028e\3\2\2\2\u0292\u0290\3\2\2\2\u0292\u0291\3\2\2\2")
        buf.write("\u0293\u008c\3\2\2\2\u0294\u0295\7^\2\2\u0295\u0296\t")
        buf.write("\n\2\2\u0296\u008e\3\2\2\2\u0297\u0298\7^\2\2\u0298\u029b")
        buf.write("\n\13\2\2\u0299\u029b\n\f\2\2\u029a\u0297\3\2\2\2\u029a")
        buf.write("\u0299\3\2\2\2\u029b\u0090\3\2\2\2\u029c\u029d\7%\2\2")
        buf.write("\u029d\u029e\7%\2\2\u029e\u02a2\3\2\2\2\u029f\u02a1\13")
        buf.write("\2\2\2\u02a0\u029f\3\2\2\2\u02a1\u02a4\3\2\2\2\u02a2\u02a3")
        buf.write("\3\2\2\2\u02a2\u02a0\3\2\2\2\u02a3\u02a5\3\2\2\2\u02a4")
        buf.write("\u02a2\3\2\2\2\u02a5\u02a6\7%\2\2\u02a6\u02a7\7%\2\2\u02a7")
        buf.write("\u02a8\3\2\2\2\u02a8\u02a9\bI\7\2\u02a9\u0092\3\2\2\2")
        buf.write("\u02aa\u02ac\t\r\2\2\u02ab\u02aa\3\2\2\2\u02ac\u02ad\3")
        buf.write("\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02af")
        buf.write("\3\2\2\2\u02af\u02b0\bJ\7\2\u02b0\u0094\3\2\2\2\u02b1")
        buf.write("\u02b2\13\2\2\2\u02b2\u02b3\bK\b\2\u02b3\u0096\3\2\2\2")
        buf.write("\u02b4\u02b5\t\16\2\2\u02b5\u0098\3\2\2\2\u02b6\u02b7")
        buf.write("\t\17\2\2\u02b7\u009a\3\2\2\2\u02b8\u02b9\t\20\2\2\u02b9")
        buf.write("\u009c\3\2\2\29\2\u00c5\u017c\u0182\u0185\u018d\u0196")
        buf.write("\u019d\u01a3\u01a8\u01ae\u01b2\u01b7\u01bd\u01c4\u01c9")
        buf.write("\u01ce\u01d4\u01da\u01e1\u01e3\u01e8\u01ee\u01f3\u01f8")
        buf.write("\u01ff\u0207\u020c\u0211\u0218\u021d\u0222\u0226\u022d")
        buf.write("\u022f\u0238\u023a\u0240\u0244\u024c\u024e\u0254\u0258")
        buf.write("\u0261\u0263\u0269\u026d\u0274\u0279\u027f\u0288\u0292")
        buf.write("\u029a\u02a2\u02ad\t\3;\2\3>\3\3C\4\3D\5\3E\6\b\2\2\3")
        buf.write("K\7")
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
            "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

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
            	raise UncloseString(current[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 5:
             raise ErrorToken(self.text) 
     


