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
        buf.write("\u02be\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("9\169\u0186\139\59\u0188\n9\3:\3:\7:\u018c\n:\f:\16:\u018f")
        buf.write("\13:\3;\3;\3<\3<\7<\u0195\n<\f<\16<\u0198\13<\3<\3<\3")
        buf.write("<\3=\7=\u019e\n=\f=\16=\u01a1\13=\3=\3=\7=\u01a5\n=\f")
        buf.write("=\16=\u01a8\13=\3=\7=\u01ab\n=\f=\16=\u01ae\13=\3=\7=")
        buf.write("\u01b1\n=\f=\16=\u01b4\13=\3=\5=\u01b7\n=\3=\7=\u01ba")
        buf.write("\n=\f=\16=\u01bd\13=\3>\7>\u01c0\n>\f>\16>\u01c3\13>\3")
        buf.write(">\3>\7>\u01c7\n>\f>\16>\u01ca\13>\3>\3>\5>\u01ce\n>\3")
        buf.write(">\7>\u01d1\n>\f>\16>\u01d4\13>\3>\7>\u01d7\n>\f>\16>\u01da")
        buf.write("\13>\3>\7>\u01dd\n>\f>\16>\u01e0\13>\3>\3>\6>\u01e4\n")
        buf.write(">\r>\16>\u01e5\5>\u01e8\n>\3>\7>\u01eb\n>\f>\16>\u01ee")
        buf.write("\13>\3?\7?\u01f1\n?\f?\16?\u01f4\13?\3?\3?\5?\u01f8\n")
        buf.write("?\3?\7?\u01fb\n?\f?\16?\u01fe\13?\3?\3?\7?\u0202\n?\f")
        buf.write("?\16?\u0205\13?\3?\3?\3?\7?\u020a\n?\f?\16?\u020d\13?")
        buf.write("\3?\3?\5?\u0211\n?\3?\7?\u0214\n?\f?\16?\u0217\13?\3?")
        buf.write("\3?\7?\u021b\n?\f?\16?\u021e\13?\3?\3?\5?\u0222\n?\3?")
        buf.write("\7?\u0225\n?\f?\16?\u0228\13?\3?\5?\u022b\n?\3?\3?\3@")
        buf.write("\3@\3@\7@\u0232\n@\f@\16@\u0235\13@\3A\3A\3A\3A\6A\u023b")
        buf.write("\nA\rA\16A\u023c\5A\u023f\nA\3A\3A\6A\u0243\nA\rA\16A")
        buf.write("\u0244\7A\u0247\nA\fA\16A\u024a\13A\3B\3B\3B\6B\u024f")
        buf.write("\nB\rB\16B\u0250\5B\u0253\nB\3B\3B\6B\u0257\nB\rB\16B")
        buf.write("\u0258\7B\u025b\nB\fB\16B\u025e\13B\3C\3C\3C\3C\6C\u0264")
        buf.write("\nC\rC\16C\u0265\5C\u0268\nC\3C\3C\6C\u026c\nC\rC\16C")
        buf.write("\u026d\7C\u0270\nC\fC\16C\u0273\13C\3D\3D\3D\3D\5D\u0279")
        buf.write("\nD\3D\3D\3D\5D\u027e\nD\3E\3E\7E\u0282\nE\fE\16E\u0285")
        buf.write("\13E\3E\3E\3F\3F\7F\u028b\nF\fF\16F\u028e\13F\3F\3F\3")
        buf.write("F\3G\3G\3G\3G\5G\u0297\nG\3H\3H\3H\3I\3I\3I\5I\u029f\n")
        buf.write("I\3J\3J\3J\3J\7J\u02a5\nJ\fJ\16J\u02a8\13J\3J\3J\3J\3")
        buf.write("J\3J\3K\6K\u02b0\nK\rK\16K\u02b1\3K\3K\3L\3L\3L\3M\3M")
        buf.write("\3N\3N\3O\3O\3\u02a6\2P\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63")
        buf.write("e\64g\65i\66k\67m8o9q:s;u\2w<y\2{\2}=\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087>\u0089?\u008b@\u008d\2\u008f\2\u0091")
        buf.write("\2\u0093A\u0095B\u0097C\u0099\2\u009b\2\u009d\2\3\2\21")
        buf.write("\6\2\62;C\\aac|\5\2C\\aac|\3\2\63;\3\2\62;\5\2\62;CHc")
        buf.write("h\3\2\629\3\2\62\63\4\2$$^^\t\2))^^ddhhppttvv\n\2$$))")
        buf.write("^^ddhhppttvv\3\2^^\5\2\n\f\16\17\"\"\4\2DDdd\4\2GGgg\4")
        buf.write("\2ZZzz\2\u02eb\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write("\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3")
        buf.write("\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2")
        buf.write("\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u009f\3\2\2")
        buf.write("\2\5\u00a5\3\2\2\2\7\u00ae\3\2\2\2\t\u00b1\3\2\2\2\13")
        buf.write("\u00b8\3\2\2\2\r\u00bd\3\2\2\2\17\u00c7\3\2\2\2\21\u00c9")
        buf.write("\3\2\2\2\23\u00ce\3\2\2\2\25\u00d4\3\2\2\2\27\u00da\3")
        buf.write("\2\2\2\31\u00dd\3\2\2\2\33\u00e1\3\2\2\2\35\u00e7\3\2")
        buf.write("\2\2\37\u00ef\3\2\2\2!\u00f6\3\2\2\2#\u00fd\3\2\2\2%\u0102")
        buf.write("\3\2\2\2\'\u0108\3\2\2\2)\u010c\3\2\2\2+\u0110\3\2\2\2")
        buf.write("-\u011c\3\2\2\2/\u0127\3\2\2\2\61\u012b\3\2\2\2\63\u012e")
        buf.write("\3\2\2\2\65\u0133\3\2\2\2\67\u0136\3\2\2\29\u0139\3\2")
        buf.write("\2\2;\u013b\3\2\2\2=\u013d\3\2\2\2?\u013f\3\2\2\2A\u0141")
        buf.write("\3\2\2\2C\u0143\3\2\2\2E\u0145\3\2\2\2G\u0147\3\2\2\2")
        buf.write("I\u014a\3\2\2\2K\u014d\3\2\2\2M\u0150\3\2\2\2O\u0152\3")
        buf.write("\2\2\2Q\u0155\3\2\2\2S\u0158\3\2\2\2U\u015b\3\2\2\2W\u015d")
        buf.write("\3\2\2\2Y\u015f\3\2\2\2[\u0163\3\2\2\2]\u0166\3\2\2\2")
        buf.write("_\u0168\3\2\2\2a\u016a\3\2\2\2c\u016c\3\2\2\2e\u016e\3")
        buf.write("\2\2\2g\u0170\3\2\2\2i\u0172\3\2\2\2k\u0174\3\2\2\2m\u0176")
        buf.write("\3\2\2\2o\u0178\3\2\2\2q\u0187\3\2\2\2s\u0189\3\2\2\2")
        buf.write("u\u0190\3\2\2\2w\u0192\3\2\2\2y\u019f\3\2\2\2{\u01c1\3")
        buf.write("\2\2\2}\u022a\3\2\2\2\177\u022e\3\2\2\2\u0081\u0236\3")
        buf.write("\2\2\2\u0083\u024b\3\2\2\2\u0085\u025f\3\2\2\2\u0087\u027d")
        buf.write("\3\2\2\2\u0089\u027f\3\2\2\2\u008b\u0288\3\2\2\2\u008d")
        buf.write("\u0296\3\2\2\2\u008f\u0298\3\2\2\2\u0091\u029e\3\2\2\2")
        buf.write("\u0093\u02a0\3\2\2\2\u0095\u02af\3\2\2\2\u0097\u02b5\3")
        buf.write("\2\2\2\u0099\u02b8\3\2\2\2\u009b\u02ba\3\2\2\2\u009d\u02bc")
        buf.write("\3\2\2\2\u009f\u00a0\7D\2\2\u00a0\u00a1\7t\2\2\u00a1\u00a2")
        buf.write("\7g\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4\7m\2\2\u00a4\4")
        buf.write("\3\2\2\2\u00a5\u00a6\7E\2\2\u00a6\u00a7\7q\2\2\u00a7\u00a8")
        buf.write("\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\u00aa\7k\2\2\u00aa\u00ab")
        buf.write("\7p\2\2\u00ab\u00ac\7w\2\2\u00ac\u00ad\7g\2\2\u00ad\6")
        buf.write("\3\2\2\2\u00ae\u00af\7K\2\2\u00af\u00b0\7h\2\2\u00b0\b")
        buf.write("\3\2\2\2\u00b1\u00b2\7G\2\2\u00b2\u00b3\7n\2\2\u00b3\u00b4")
        buf.write("\7u\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7k\2\2\u00b6\u00b7")
        buf.write("\7h\2\2\u00b7\n\3\2\2\2\u00b8\u00b9\7G\2\2\u00b9\u00ba")
        buf.write("\7n\2\2\u00ba\u00bb\7u\2\2\u00bb\u00bc\7g\2\2\u00bc\f")
        buf.write("\3\2\2\2\u00bd\u00be\7H\2\2\u00be\u00bf\7q\2\2\u00bf\u00c0")
        buf.write("\7t\2\2\u00c0\u00c1\7g\2\2\u00c1\u00c2\7c\2\2\u00c2\u00c3")
        buf.write("\7e\2\2\u00c3\u00c4\7j\2\2\u00c4\16\3\2\2\2\u00c5\u00c8")
        buf.write("\5\21\t\2\u00c6\u00c8\5\23\n\2\u00c7\u00c5\3\2\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\20\3\2\2\2\u00c9\u00ca\7V\2\2\u00ca")
        buf.write("\u00cb\7t\2\2\u00cb\u00cc\7w\2\2\u00cc\u00cd\7g\2\2\u00cd")
        buf.write("\22\3\2\2\2\u00ce\u00cf\7H\2\2\u00cf\u00d0\7c\2\2\u00d0")
        buf.write("\u00d1\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\24\3\2\2\2\u00d4\u00d5\7C\2\2\u00d5\u00d6\7t\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7{\2\2\u00d9")
        buf.write("\26\3\2\2\2\u00da\u00db\7K\2\2\u00db\u00dc\7p\2\2\u00dc")
        buf.write("\30\3\2\2\2\u00dd\u00de\7K\2\2\u00de\u00df\7p\2\2\u00df")
        buf.write("\u00e0\7v\2\2\u00e0\32\3\2\2\2\u00e1\u00e2\7H\2\2\u00e2")
        buf.write("\u00e3\7n\2\2\u00e3\u00e4\7q\2\2\u00e4\u00e5\7c\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\34\3\2\2\2\u00e7\u00e8\7D\2\2\u00e8")
        buf.write("\u00e9\7q\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7n\2\2\u00eb")
        buf.write("\u00ec\7g\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7p\2\2\u00ee")
        buf.write("\36\3\2\2\2\u00ef\u00f0\7U\2\2\u00f0\u00f1\7v\2\2\u00f1")
        buf.write("\u00f2\7t\2\2\u00f2\u00f3\7k\2\2\u00f3\u00f4\7p\2\2\u00f4")
        buf.write("\u00f5\7i\2\2\u00f5 \3\2\2\2\u00f6\u00f7\7T\2\2\u00f7")
        buf.write("\u00f8\7g\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7w\2\2\u00fa")
        buf.write("\u00fb\7t\2\2\u00fb\u00fc\7p\2\2\u00fc\"\3\2\2\2\u00fd")
        buf.write("\u00fe\7P\2\2\u00fe\u00ff\7w\2\2\u00ff\u0100\7n\2\2\u0100")
        buf.write("\u0101\7n\2\2\u0101$\3\2\2\2\u0102\u0103\7E\2\2\u0103")
        buf.write("\u0104\7n\2\2\u0104\u0105\7c\2\2\u0105\u0106\7u\2\2\u0106")
        buf.write("\u0107\7u\2\2\u0107&\3\2\2\2\u0108\u0109\7X\2\2\u0109")
        buf.write("\u010a\7c\2\2\u010a\u010b\7n\2\2\u010b(\3\2\2\2\u010c")
        buf.write("\u010d\7X\2\2\u010d\u010e\7c\2\2\u010e\u010f\7t\2\2\u010f")
        buf.write("*\3\2\2\2\u0110\u0111\7E\2\2\u0111\u0112\7q\2\2\u0112")
        buf.write("\u0113\7p\2\2\u0113\u0114\7u\2\2\u0114\u0115\7v\2\2\u0115")
        buf.write("\u0116\7t\2\2\u0116\u0117\7w\2\2\u0117\u0118\7e\2\2\u0118")
        buf.write("\u0119\7v\2\2\u0119\u011a\7q\2\2\u011a\u011b\7t\2\2\u011b")
        buf.write(",\3\2\2\2\u011c\u011d\7F\2\2\u011d\u011e\7g\2\2\u011e")
        buf.write("\u011f\7u\2\2\u011f\u0120\7v\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write("\u0122\7w\2\2\u0122\u0123\7e\2\2\u0123\u0124\7v\2\2\u0124")
        buf.write("\u0125\7q\2\2\u0125\u0126\7t\2\2\u0126.\3\2\2\2\u0127")
        buf.write("\u0128\7P\2\2\u0128\u0129\7g\2\2\u0129\u012a\7y\2\2\u012a")
        buf.write("\60\3\2\2\2\u012b\u012c\7D\2\2\u012c\u012d\7{\2\2\u012d")
        buf.write("\62\3\2\2\2\u012e\u012f\7U\2\2\u012f\u0130\7g\2\2\u0130")
        buf.write("\u0131\7n\2\2\u0131\u0132\7h\2\2\u0132\64\3\2\2\2\u0133")
        buf.write("\u0134\7<\2\2\u0134\u0135\7<\2\2\u0135\66\3\2\2\2\u0136")
        buf.write("\u0137\7\60\2\2\u0137\u0138\7\60\2\2\u01388\3\2\2\2\u0139")
        buf.write("\u013a\7a\2\2\u013a:\3\2\2\2\u013b\u013c\7-\2\2\u013c")
        buf.write("<\3\2\2\2\u013d\u013e\7/\2\2\u013e>\3\2\2\2\u013f\u0140")
        buf.write("\7,\2\2\u0140@\3\2\2\2\u0141\u0142\7\61\2\2\u0142B\3\2")
        buf.write("\2\2\u0143\u0144\7\'\2\2\u0144D\3\2\2\2\u0145\u0146\7")
        buf.write("#\2\2\u0146F\3\2\2\2\u0147\u0148\7(\2\2\u0148\u0149\7")
        buf.write("(\2\2\u0149H\3\2\2\2\u014a\u014b\7~\2\2\u014b\u014c\7")
        buf.write("~\2\2\u014cJ\3\2\2\2\u014d\u014e\7?\2\2\u014e\u014f\7")
        buf.write("?\2\2\u014fL\3\2\2\2\u0150\u0151\7?\2\2\u0151N\3\2\2\2")
        buf.write("\u0152\u0153\7#\2\2\u0153\u0154\7?\2\2\u0154P\3\2\2\2")
        buf.write("\u0155\u0156\7@\2\2\u0156\u0157\7?\2\2\u0157R\3\2\2\2")
        buf.write("\u0158\u0159\7>\2\2\u0159\u015a\7?\2\2\u015aT\3\2\2\2")
        buf.write("\u015b\u015c\7@\2\2\u015cV\3\2\2\2\u015d\u015e\7>\2\2")
        buf.write("\u015eX\3\2\2\2\u015f\u0160\7?\2\2\u0160\u0161\7?\2\2")
        buf.write("\u0161\u0162\7\60\2\2\u0162Z\3\2\2\2\u0163\u0164\7-\2")
        buf.write("\2\u0164\u0165\7\60\2\2\u0165\\\3\2\2\2\u0166\u0167\7")
        buf.write("*\2\2\u0167^\3\2\2\2\u0168\u0169\7+\2\2\u0169`\3\2\2\2")
        buf.write("\u016a\u016b\7]\2\2\u016bb\3\2\2\2\u016c\u016d\7_\2\2")
        buf.write("\u016dd\3\2\2\2\u016e\u016f\7}\2\2\u016ff\3\2\2\2\u0170")
        buf.write("\u0171\7\177\2\2\u0171h\3\2\2\2\u0172\u0173\7\60\2\2\u0173")
        buf.write("j\3\2\2\2\u0174\u0175\7.\2\2\u0175l\3\2\2\2\u0176\u0177")
        buf.write("\7<\2\2\u0177n\3\2\2\2\u0178\u0179\7=\2\2\u0179p\3\2\2")
        buf.write("\2\u017a\u017c\5u;\2\u017b\u017d\t\2\2\2\u017c\u017b\3")
        buf.write("\2\2\2\u017d\u017e\3\2\2\2\u017e\u017c\3\2\2\2\u017e\u017f")
        buf.write("\3\2\2\2\u017f\u0188\3\2\2\2\u0180\u0184\t\3\2\2\u0181")
        buf.write("\u0183\t\2\2\2\u0182\u0181\3\2\2\2\u0183\u0186\3\2\2\2")
        buf.write("\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185\u0188\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0187\u017a\3\2\2\2\u0187\u0180")
        buf.write("\3\2\2\2\u0188r\3\2\2\2\u0189\u018d\t\3\2\2\u018a\u018c")
        buf.write("\t\2\2\2\u018b\u018a\3\2\2\2\u018c\u018f\3\2\2\2\u018d")
        buf.write("\u018b\3\2\2\2\u018d\u018e\3\2\2\2\u018et\3\2\2\2\u018f")
        buf.write("\u018d\3\2\2\2\u0190\u0191\7&\2\2\u0191v\3\2\2\2\u0192")
        buf.write("\u0196\7$\2\2\u0193\u0195\5\u008dG\2\u0194\u0193\3\2\2")
        buf.write("\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197\u0199\3\2\2\2\u0198\u0196\3\2\2\2\u0199")
        buf.write("\u019a\7$\2\2\u019a\u019b\b<\2\2\u019bx\3\2\2\2\u019c")
        buf.write("\u019e\59\35\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2")
        buf.write("\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a2\3")
        buf.write("\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a6\7\60\2\2\u01a3")
        buf.write("\u01a5\59\35\2\u01a4\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2")
        buf.write("\u01a6\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01ac\3")
        buf.write("\2\2\2\u01a8\u01a6\3\2\2\2\u01a9\u01ab\7\62\2\2\u01aa")
        buf.write("\u01a9\3\2\2\2\u01ab\u01ae\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ac\u01ad\3\2\2\2\u01ad\u01b2\3\2\2\2\u01ae\u01ac\3")
        buf.write("\2\2\2\u01af\u01b1\59\35\2\u01b0\u01af\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b7\5\177@")
        buf.write("\2\u01b6\u01b5\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01bb")
        buf.write("\3\2\2\2\u01b8\u01ba\59\35\2\u01b9\u01b8\3\2\2\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bcz\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c0\59\35")
        buf.write("\2\u01bf\u01be\3\2\2\2\u01c0\u01c3\3\2\2\2\u01c1\u01bf")
        buf.write("\3\2\2\2\u01c1\u01c2\3\2\2\2\u01c2\u01c4\3\2\2\2\u01c3")
        buf.write("\u01c1\3\2\2\2\u01c4\u01c8\5\u009bN\2\u01c5\u01c7\59\35")
        buf.write("\2\u01c6\u01c5\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01cd\3\2\2\2\u01ca")
        buf.write("\u01c8\3\2\2\2\u01cb\u01ce\5=\37\2\u01cc\u01ce\5;\36\2")
        buf.write("\u01cd\u01cb\3\2\2\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01d2\3\2\2\2\u01cf\u01d1\59\35\2\u01d0\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01e7\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d5\u01d7\7\62\2\2\u01d6\u01d5\3\2\2\2\u01d7\u01da")
        buf.write("\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9")
        buf.write("\u01de\3\2\2\2\u01da\u01d8\3\2\2\2\u01db\u01dd\59\35\2")
        buf.write("\u01dc\u01db\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3")
        buf.write("\2\2\2\u01de\u01df\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01de")
        buf.write("\3\2\2\2\u01e1\u01e8\5\177@\2\u01e2\u01e4\7\62\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u01e3\3\2\2\2")
        buf.write("\u01e5\u01e6\3\2\2\2\u01e6\u01e8\3\2\2\2\u01e7\u01d8\3")
        buf.write("\2\2\2\u01e7\u01e3\3\2\2\2\u01e8\u01ec\3\2\2\2\u01e9\u01eb")
        buf.write("\59\35\2\u01ea\u01e9\3\2\2\2\u01eb\u01ee\3\2\2\2\u01ec")
        buf.write("\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed|\3\2\2\2\u01ee")
        buf.write("\u01ec\3\2\2\2\u01ef\u01f1\59\35\2\u01f0\u01ef\3\2\2\2")
        buf.write("\u01f1\u01f4\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3")
        buf.write("\2\2\2\u01f3\u01f7\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f8")
        buf.write("\5\177@\2\u01f6\u01f8\7\62\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8\u01fc\3\2\2\2\u01f9\u01fb\59\35\2")
        buf.write("\u01fa\u01f9\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\3\2\2\2\u01fe\u01fc")
        buf.write("\3\2\2\2\u01ff\u0203\5y=\2\u0200\u0202\59\35\2\u0201\u0200")
        buf.write("\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0203")
        buf.write("\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3\2\2\2")
        buf.write("\u0206\u0207\5{>\2\u0207\u022b\3\2\2\2\u0208\u020a\59")
        buf.write("\35\2\u0209\u0208\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u0210\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020e\u0211\5\177@\2\u020f\u0211\7\62\2")
        buf.write("\2\u0210\u020e\3\2\2\2\u0210\u020f\3\2\2\2\u0211\u0215")
        buf.write("\3\2\2\2\u0212\u0214\59\35\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u022b\5")
        buf.write("y=\2\u0219\u021b\59\35\2\u021a\u0219\3\2\2\2\u021b\u021e")
        buf.write("\3\2\2\2\u021c\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\u0221\3\2\2\2\u021e\u021c\3\2\2\2\u021f\u0222\5\177@")
        buf.write("\2\u0220\u0222\7\62\2\2\u0221\u021f\3\2\2\2\u0221\u0220")
        buf.write("\3\2\2\2\u0222\u0226\3\2\2\2\u0223\u0225\59\35\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225\u0228\3\2\2\2\u0226\u0224\3\2\2\2")
        buf.write("\u0226\u0227\3\2\2\2\u0227\u0229\3\2\2\2\u0228\u0226\3")
        buf.write("\2\2\2\u0229\u022b\5{>\2\u022a\u01f2\3\2\2\2\u022a\u020b")
        buf.write("\3\2\2\2\u022a\u021c\3\2\2\2\u022b\u022c\3\2\2\2\u022c")
        buf.write("\u022d\b?\3\2\u022d~\3\2\2\2\u022e\u0233\t\4\2\2\u022f")
        buf.write("\u0232\59\35\2\u0230\u0232\t\5\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0230\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0231\3")
        buf.write("\2\2\2\u0233\u0234\3\2\2\2\u0234\u0080\3\2\2\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u0237\7\62\2\2\u0237\u023e\5\u009dO\2\u0238")
        buf.write("\u023f\59\35\2\u0239\u023b\t\6\2\2\u023a\u0239\3\2\2\2")
        buf.write("\u023b\u023c\3\2\2\2\u023c\u023a\3\2\2\2\u023c\u023d\3")
        buf.write("\2\2\2\u023d\u023f\3\2\2\2\u023e\u0238\3\2\2\2\u023e\u023a")
        buf.write("\3\2\2\2\u023f\u0248\3\2\2\2\u0240\u0242\59\35\2\u0241")
        buf.write("\u0243\t\6\2\2\u0242\u0241\3\2\2\2\u0243\u0244\3\2\2\2")
        buf.write("\u0244\u0242\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0247\3")
        buf.write("\2\2\2\u0246\u0240\3\2\2\2\u0247\u024a\3\2\2\2\u0248\u0246")
        buf.write("\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u0082\3\2\2\2\u024a")
        buf.write("\u0248\3\2\2\2\u024b\u0252\7\62\2\2\u024c\u0253\59\35")
        buf.write("\2\u024d\u024f\t\7\2\2\u024e\u024d\3\2\2\2\u024f\u0250")
        buf.write("\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251")
        buf.write("\u0253\3\2\2\2\u0252\u024c\3\2\2\2\u0252\u024e\3\2\2\2")
        buf.write("\u0253\u025c\3\2\2\2\u0254\u0256\59\35\2\u0255\u0257\t")
        buf.write("\7\2\2\u0256\u0255\3\2\2\2\u0257\u0258\3\2\2\2\u0258\u0256")
        buf.write("\3\2\2\2\u0258\u0259\3\2\2\2\u0259\u025b\3\2\2\2\u025a")
        buf.write("\u0254\3\2\2\2\u025b\u025e\3\2\2\2\u025c\u025a\3\2\2\2")
        buf.write("\u025c\u025d\3\2\2\2\u025d\u0084\3\2\2\2\u025e\u025c\3")
        buf.write("\2\2\2\u025f\u0260\7\62\2\2\u0260\u0267\5\u0099M\2\u0261")
        buf.write("\u0268\59\35\2\u0262\u0264\t\b\2\2\u0263\u0262\3\2\2\2")
        buf.write("\u0264\u0265\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3")
        buf.write("\2\2\2\u0266\u0268\3\2\2\2\u0267\u0261\3\2\2\2\u0267\u0263")
        buf.write("\3\2\2\2\u0268\u0271\3\2\2\2\u0269\u026b\59\35\2\u026a")
        buf.write("\u026c\t\b\2\2\u026b\u026a\3\2\2\2\u026c\u026d\3\2\2\2")
        buf.write("\u026d\u026b\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u0270\3")
        buf.write("\2\2\2\u026f\u0269\3\2\2\2\u0270\u0273\3\2\2\2\u0271\u026f")
        buf.write("\3\2\2\2\u0271\u0272\3\2\2\2\u0272\u0086\3\2\2\2\u0273")
        buf.write("\u0271\3\2\2\2\u0274\u0279\5\177@\2\u0275\u0279\5\u0081")
        buf.write("A\2\u0276\u0279\5\u0083B\2\u0277\u0279\5\u0085C\2\u0278")
        buf.write("\u0274\3\2\2\2\u0278\u0275\3\2\2\2\u0278\u0276\3\2\2\2")
        buf.write("\u0278\u0277\3\2\2\2\u0279\u027a\3\2\2\2\u027a\u027b\b")
        buf.write("D\4\2\u027b\u027e\3\2\2\2\u027c\u027e\7\62\2\2\u027d\u0278")
        buf.write("\3\2\2\2\u027d\u027c\3\2\2\2\u027e\u0088\3\2\2\2\u027f")
        buf.write("\u0283\7$\2\2\u0280\u0282\5\u008dG\2\u0281\u0280\3\2\2")
        buf.write("\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2\u0283\u0284")
        buf.write("\3\2\2\2\u0284\u0286\3\2\2\2\u0285\u0283\3\2\2\2\u0286")
        buf.write("\u0287\bE\5\2\u0287\u008a\3\2\2\2\u0288\u028c\7$\2\2\u0289")
        buf.write("\u028b\5\u008dG\2\u028a\u0289\3\2\2\2\u028b\u028e\3\2")
        buf.write("\2\2\u028c\u028a\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028f")
        buf.write("\3\2\2\2\u028e\u028c\3\2\2\2\u028f\u0290\5\u0091I\2\u0290")
        buf.write("\u0291\bF\6\2\u0291\u008c\3\2\2\2\u0292\u0293\7)\2\2\u0293")
        buf.write("\u0297\7$\2\2\u0294\u0297\5\u008fH\2\u0295\u0297\n\t\2")
        buf.write("\2\u0296\u0292\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0295")
        buf.write("\3\2\2\2\u0297\u008e\3\2\2\2\u0298\u0299\7^\2\2\u0299")
        buf.write("\u029a\t\n\2\2\u029a\u0090\3\2\2\2\u029b\u029c\7^\2\2")
        buf.write("\u029c\u029f\n\13\2\2\u029d\u029f\n\f\2\2\u029e\u029b")
        buf.write("\3\2\2\2\u029e\u029d\3\2\2\2\u029f\u0092\3\2\2\2\u02a0")
        buf.write("\u02a1\7%\2\2\u02a1\u02a2\7%\2\2\u02a2\u02a6\3\2\2\2\u02a3")
        buf.write("\u02a5\13\2\2\2\u02a4\u02a3\3\2\2\2\u02a5\u02a8\3\2\2")
        buf.write("\2\u02a6\u02a7\3\2\2\2\u02a6\u02a4\3\2\2\2\u02a7\u02a9")
        buf.write("\3\2\2\2\u02a8\u02a6\3\2\2\2\u02a9\u02aa\7%\2\2\u02aa")
        buf.write("\u02ab\7%\2\2\u02ab\u02ac\3\2\2\2\u02ac\u02ad\bJ\7\2\u02ad")
        buf.write("\u0094\3\2\2\2\u02ae\u02b0\t\r\2\2\u02af\u02ae\3\2\2\2")
        buf.write("\u02b0\u02b1\3\2\2\2\u02b1\u02af\3\2\2\2\u02b1\u02b2\3")
        buf.write("\2\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b4\bK\7\2\u02b4\u0096")
        buf.write("\3\2\2\2\u02b5\u02b6\13\2\2\2\u02b6\u02b7\bL\b\2\u02b7")
        buf.write("\u0098\3\2\2\2\u02b8\u02b9\t\16\2\2\u02b9\u009a\3\2\2")
        buf.write("\2\u02ba\u02bb\t\17\2\2\u02bb\u009c\3\2\2\2\u02bc\u02bd")
        buf.write("\t\20\2\2\u02bd\u009e\3\2\2\29\2\u00c7\u017e\u0184\u0187")
        buf.write("\u018d\u0196\u019f\u01a6\u01ac\u01b2\u01b6\u01bb\u01c1")
        buf.write("\u01c8\u01cd\u01d2\u01d8\u01de\u01e5\u01e7\u01ec\u01f2")
        buf.write("\u01f7\u01fc\u0203\u020b\u0210\u0215\u021c\u0221\u0226")
        buf.write("\u022a\u0231\u0233\u023c\u023e\u0244\u0248\u0250\u0252")
        buf.write("\u0258\u025c\u0265\u0267\u026d\u0271\u0278\u027d\u0283")
        buf.write("\u028c\u0296\u029e\u02a6\u02b1\t\3<\2\3?\3\3D\4\3E\5\3")
        buf.write("F\6\b\2\2\3L\7")
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
    VARIABLE_IDENTIFIERS = 57
    STRINGLIT = 58
    FLOATLIT = 59
    INTLIT = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    BLOCK_COMMENT = 63
    WS = 64
    ERROR_CHAR = 65

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
            "VARIABLE_IDENTIFIERS", "STRINGLIT", "FLOATLIT", "INTLIT", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "BOOLLIT", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GTE", 
                  "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", "LB", 
                  "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", 
                  "SEMICOLON", "IDENTIFIERS", "VARIABLE_IDENTIFIERS", "DOLLAR", 
                  "STRINGLIT", "DECIMALPART", "EXPONENTPART", "FLOATLIT", 
                  "DEC", "HEX", "OCT", "BIN", "INTLIT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", 
                  "BLOCK_COMMENT", "WS", "ERROR_CHAR", "B", "E", "X" ]

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
            actions[58] = self.STRINGLIT_action 
            actions[61] = self.FLOATLIT_action 
            actions[66] = self.INTLIT_action 
            actions[67] = self.UNCLOSE_STRING_action 
            actions[68] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
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
     


