# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2E")
        buf.write("\u0225\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\3\3\3\3\5\3")
        buf.write("\u00a8\n\3\3\4\3\4\3\4\5\4\u00ad\n\4\3\5\3\5\3\5\3\5\5")
        buf.write("\5\u00b3\n\5\3\6\3\6\7\6\u00b7\n\6\f\6\16\6\u00ba\13\6")
        buf.write("\3\6\3\6\6\6\u00be\n\6\r\6\16\6\u00bf\7\6\u00c2\n\6\f")
        buf.write("\6\16\6\u00c5\13\6\3\6\3\6\5\6\u00c9\n\6\3\7\3\7\3\7\6")
        buf.write("\7\u00ce\n\7\r\7\16\7\u00cf\3\b\3\b\6\b\u00d4\n\b\r\b")
        buf.write("\16\b\u00d5\3\t\3\t\3\t\6\t\u00db\n\t\r\t\16\t\u00dc\3")
        buf.write("\n\3\n\3\n\3\n\3\13\3\13\6\13\u00e5\n\13\r\13\16\13\u00e6")
        buf.write("\5\13\u00e9\n\13\3\f\7\f\u00ec\n\f\f\f\16\f\u00ef\13\f")
        buf.write("\3\f\3\f\3\f\5\f\u00f4\n\f\3\f\6\f\u00f7\n\f\r\f\16\f")
        buf.write("\u00f8\5\f\u00fb\n\f\3\r\3\r\5\r\u00ff\n\r\3\16\3\16\6")
        buf.write("\16\u0103\n\16\r\16\16\16\u0104\3\16\3\16\6\16\u0109\n")
        buf.write("\16\r\16\16\16\u010a\5\16\u010d\n\16\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3")
        buf.write("!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#")
        buf.write("\3#\3#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3")
        buf.write("&\3&\3&\3\'\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3")
        buf.write("-\3.\3.\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\3\67\38\38\38\39\39\39\39\3:\3:\3:\3;\3;\3<\3<\3")
        buf.write("=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("E\3E\7E\u01e6\nE\fE\16E\u01e9\13E\3E\3E\3E\3E\3E\3F\6")
        buf.write("F\u01f1\nF\rF\16F\u01f2\3F\3F\3G\3G\7G\u01f9\nG\fG\16")
        buf.write("G\u01fc\13G\3G\3G\3H\3H\7H\u0202\nH\fH\16H\u0205\13H\3")
        buf.write("H\3H\3H\3I\3I\3I\3I\5I\u020e\nI\3J\3J\3J\3K\3K\3K\5K\u0216")
        buf.write("\nK\3L\3L\3L\3M\6M\u021c\nM\rM\16M\u021d\3N\3N\3O\3O\3")
        buf.write("P\3P\4\u00ed\u01e7\2Q\3\3\5\4\7\5\t\6\13\2\r\2\17\2\21")
        buf.write("\2\23\7\25\2\27\2\31\b\33\t\35\n\37\13!\f#\r%\16\'\17")
        buf.write(")\20+\21-\22/\23\61\24\63\25\65\26\67\279\30;\31=\32?")
        buf.write("\33A\34C\35E\36G\37I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/")
        buf.write("i\60k\61m\62o\63q\64s\65u\66w\67y8{9}:\177;\u0081<\u0083")
        buf.write("=\u0085>\u0087?\u0089@\u008bA\u008dB\u008fC\u0091\2\u0093")
        buf.write("\2\u0095\2\u0097D\u0099E\u009b\2\u009d\2\u009f\2\3\2\17")
        buf.write("\3\2\63;\3\2\62;\5\2\62;CHch\3\2\62\63\6\2\62;C\\aac|")
        buf.write("\5\2C\\aac|\5\2\n\f\16\17\"\"\4\2$$^^\n\2$$))^^ddhhpp")
        buf.write("ttvv\3\2^^\4\2DDdd\4\2GGgg\4\2ZZzz\2\u023a\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\23\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3")
        buf.write("\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2")
        buf.write("\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\3\u00a1")
        buf.write("\3\2\2\2\5\u00a7\3\2\2\2\7\u00ac\3\2\2\2\t\u00b2\3\2\2")
        buf.write("\2\13\u00c8\3\2\2\2\r\u00ca\3\2\2\2\17\u00d1\3\2\2\2\21")
        buf.write("\u00d7\3\2\2\2\23\u00de\3\2\2\2\25\u00e8\3\2\2\2\27\u00ed")
        buf.write("\3\2\2\2\31\u00fe\3\2\2\2\33\u010c\3\2\2\2\35\u010e\3")
        buf.write("\2\2\2\37\u0110\3\2\2\2!\u0116\3\2\2\2#\u011f\3\2\2\2")
        buf.write("%\u0122\3\2\2\2\'\u0129\3\2\2\2)\u012e\3\2\2\2+\u0136")
        buf.write("\3\2\2\2-\u013b\3\2\2\2/\u0141\3\2\2\2\61\u0147\3\2\2")
        buf.write("\2\63\u014a\3\2\2\2\65\u014e\3\2\2\2\67\u0154\3\2\2\2")
        buf.write("9\u015c\3\2\2\2;\u0163\3\2\2\2=\u016a\3\2\2\2?\u016f\3")
        buf.write("\2\2\2A\u0175\3\2\2\2C\u0179\3\2\2\2E\u017d\3\2\2\2G\u0189")
        buf.write("\3\2\2\2I\u0194\3\2\2\2K\u0198\3\2\2\2M\u019b\3\2\2\2")
        buf.write("O\u019e\3\2\2\2Q\u01a0\3\2\2\2S\u01a2\3\2\2\2U\u01a4\3")
        buf.write("\2\2\2W\u01a6\3\2\2\2Y\u01a8\3\2\2\2[\u01aa\3\2\2\2]\u01ac")
        buf.write("\3\2\2\2_\u01ae\3\2\2\2a\u01b1\3\2\2\2c\u01b4\3\2\2\2")
        buf.write("e\u01b7\3\2\2\2g\u01b9\3\2\2\2i\u01bc\3\2\2\2k\u01be\3")
        buf.write("\2\2\2m\u01c0\3\2\2\2o\u01c3\3\2\2\2q\u01c6\3\2\2\2s\u01ca")
        buf.write("\3\2\2\2u\u01cd\3\2\2\2w\u01cf\3\2\2\2y\u01d1\3\2\2\2")
        buf.write("{\u01d3\3\2\2\2}\u01d5\3\2\2\2\177\u01d7\3\2\2\2\u0081")
        buf.write("\u01d9\3\2\2\2\u0083\u01db\3\2\2\2\u0085\u01dd\3\2\2\2")
        buf.write("\u0087\u01df\3\2\2\2\u0089\u01e1\3\2\2\2\u008b\u01f0\3")
        buf.write("\2\2\2\u008d\u01f6\3\2\2\2\u008f\u01ff\3\2\2\2\u0091\u020d")
        buf.write("\3\2\2\2\u0093\u020f\3\2\2\2\u0095\u0215\3\2\2\2\u0097")
        buf.write("\u0217\3\2\2\2\u0099\u021b\3\2\2\2\u009b\u021f\3\2\2\2")
        buf.write("\u009d\u0221\3\2\2\2\u009f\u0223\3\2\2\2\u00a1\u00a2\7")
        buf.write("$\2\2\u00a2\4\3\2\2\2\u00a3\u00a8\5\63\32\2\u00a4\u00a8")
        buf.write("\5\65\33\2\u00a5\u00a8\5\67\34\2\u00a6\u00a8\59\35\2\u00a7")
        buf.write("\u00a3\3\2\2\2\u00a7\u00a4\3\2\2\2\u00a7\u00a5\3\2\2\2")
        buf.write("\u00a7\u00a6\3\2\2\2\u00a8\6\3\2\2\2\u00a9\u00ad\5#\22")
        buf.write("\2\u00aa\u00ad\5%\23\2\u00ab\u00ad\5\'\24\2\u00ac\u00a9")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ab\3\2\2\2\u00ad")
        buf.write("\b\3\2\2\2\u00ae\u00b3\5\13\6\2\u00af\u00b3\5\r\7\2\u00b0")
        buf.write("\u00b3\5\17\b\2\u00b1\u00b3\5\21\t\2\u00b2\u00ae\3\2\2")
        buf.write("\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2\u00b1")
        buf.write("\3\2\2\2\u00b3\n\3\2\2\2\u00b4\u00b8\t\2\2\2\u00b5\u00b7")
        buf.write("\t\3\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00ba\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00c3\3\2\2\2")
        buf.write("\u00ba\u00b8\3\2\2\2\u00bb\u00bd\5Q)\2\u00bc\u00be\t\3")
        buf.write("\2\2\u00bd\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd")
        buf.write("\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1")
        buf.write("\u00bb\3\2\2\2\u00c2\u00c5\3\2\2\2\u00c3\u00c1\3\2\2\2")
        buf.write("\u00c3\u00c4\3\2\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00c3\3")
        buf.write("\2\2\2\u00c6\u00c9\b\6\2\2\u00c7\u00c9\7\62\2\2\u00c8")
        buf.write("\u00b4\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9\f\3\2\2\2\u00ca")
        buf.write("\u00cb\7\62\2\2\u00cb\u00cd\5\u009fP\2\u00cc\u00ce\t\2")
        buf.write("\2\2\u00cd\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00cd")
        buf.write("\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\16\3\2\2\2\u00d1\u00d3")
        buf.write("\7\62\2\2\u00d2\u00d4\t\4\2\2\u00d3\u00d2\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2")
        buf.write("\u00d6\20\3\2\2\2\u00d7\u00d8\7\62\2\2\u00d8\u00da\5\u009b")
        buf.write("N\2\u00d9\u00db\t\5\2\2\u00da\u00d9\3\2\2\2\u00db\u00dc")
        buf.write("\3\2\2\2\u00dc\u00da\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd")
        buf.write("\22\3\2\2\2\u00de\u00df\5\13\6\2\u00df\u00e0\5\25\13\2")
        buf.write("\u00e0\u00e1\5\27\f\2\u00e1\24\3\2\2\2\u00e2\u00e4\5\u0081")
        buf.write("A\2\u00e3\u00e5\t\3\2\2\u00e4\u00e3\3\2\2\2\u00e5\u00e6")
        buf.write("\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2\u00e7")
        buf.write("\u00e9\3\2\2\2\u00e8\u00e2\3\2\2\2\u00e8\u00e9\3\2\2\2")
        buf.write("\u00e9\26\3\2\2\2\u00ea\u00ec\t\3\2\2\u00eb\u00ea\3\2")
        buf.write("\2\2\u00ec\u00ef\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ed\u00eb")
        buf.write("\3\2\2\2\u00ee\u00fa\3\2\2\2\u00ef\u00ed\3\2\2\2\u00f0")
        buf.write("\u00f3\5\u009dO\2\u00f1\u00f4\5U+\2\u00f2\u00f4\5S*\2")
        buf.write("\u00f3\u00f1\3\2\2\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\u00f6\3\2\2\2\u00f5\u00f7\t\3\2\2\u00f6\u00f5")
        buf.write("\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6\3\2\2\2\u00f8")
        buf.write("\u00f9\3\2\2\2\u00f9\u00fb\3\2\2\2\u00fa\u00f0\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\30\3\2\2\2\u00fc\u00ff\5+\26")
        buf.write("\2\u00fd\u00ff\5-\27\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff\32\3\2\2\2\u0100\u0102\5\35\17\2\u0101")
        buf.write("\u0103\t\6\2\2\u0102\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0102\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u010d\3")
        buf.write("\2\2\2\u0106\u0108\t\7\2\2\u0107\u0109\t\6\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u0108\3\2\2\2\u010a")
        buf.write("\u010b\3\2\2\2\u010b\u010d\3\2\2\2\u010c\u0100\3\2\2\2")
        buf.write("\u010c\u0106\3\2\2\2\u010d\34\3\2\2\2\u010e\u010f\7&\2")
        buf.write("\2\u010f\36\3\2\2\2\u0110\u0111\7D\2\2\u0111\u0112\7t")
        buf.write("\2\2\u0112\u0113\7g\2\2\u0113\u0114\7c\2\2\u0114\u0115")
        buf.write("\7m\2\2\u0115 \3\2\2\2\u0116\u0117\7E\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118\u0119\7p\2\2\u0119\u011a\7v\2\2\u011a\u011b")
        buf.write("\7k\2\2\u011b\u011c\7p\2\2\u011c\u011d\7w\2\2\u011d\u011e")
        buf.write("\7g\2\2\u011e\"\3\2\2\2\u011f\u0120\7K\2\2\u0120\u0121")
        buf.write("\7h\2\2\u0121$\3\2\2\2\u0122\u0123\7G\2\2\u0123\u0124")
        buf.write("\7n\2\2\u0124\u0125\7u\2\2\u0125\u0126\7g\2\2\u0126\u0127")
        buf.write("\7k\2\2\u0127\u0128\7h\2\2\u0128&\3\2\2\2\u0129\u012a")
        buf.write("\7G\2\2\u012a\u012b\7n\2\2\u012b\u012c\7u\2\2\u012c\u012d")
        buf.write("\7g\2\2\u012d(\3\2\2\2\u012e\u012f\7H\2\2\u012f\u0130")
        buf.write("\7q\2\2\u0130\u0131\7t\2\2\u0131\u0132\7g\2\2\u0132\u0133")
        buf.write("\7c\2\2\u0133\u0134\7e\2\2\u0134\u0135\7j\2\2\u0135*\3")
        buf.write("\2\2\2\u0136\u0137\7V\2\2\u0137\u0138\7t\2\2\u0138\u0139")
        buf.write("\7w\2\2\u0139\u013a\7g\2\2\u013a,\3\2\2\2\u013b\u013c")
        buf.write("\7H\2\2\u013c\u013d\7c\2\2\u013d\u013e\7n\2\2\u013e\u013f")
        buf.write("\7u\2\2\u013f\u0140\7g\2\2\u0140.\3\2\2\2\u0141\u0142")
        buf.write("\7C\2\2\u0142\u0143\7t\2\2\u0143\u0144\7t\2\2\u0144\u0145")
        buf.write("\7c\2\2\u0145\u0146\7{\2\2\u0146\60\3\2\2\2\u0147\u0148")
        buf.write("\7K\2\2\u0148\u0149\7p\2\2\u0149\62\3\2\2\2\u014a\u014b")
        buf.write("\7K\2\2\u014b\u014c\7p\2\2\u014c\u014d\7v\2\2\u014d\64")
        buf.write("\3\2\2\2\u014e\u014f\7H\2\2\u014f\u0150\7n\2\2\u0150\u0151")
        buf.write("\7q\2\2\u0151\u0152\7c\2\2\u0152\u0153\7v\2\2\u0153\66")
        buf.write("\3\2\2\2\u0154\u0155\7D\2\2\u0155\u0156\7q\2\2\u0156\u0157")
        buf.write("\7q\2\2\u0157\u0158\7n\2\2\u0158\u0159\7g\2\2\u0159\u015a")
        buf.write("\7c\2\2\u015a\u015b\7p\2\2\u015b8\3\2\2\2\u015c\u015d")
        buf.write("\7U\2\2\u015d\u015e\7v\2\2\u015e\u015f\7t\2\2\u015f\u0160")
        buf.write("\7k\2\2\u0160\u0161\7p\2\2\u0161\u0162\7i\2\2\u0162:\3")
        buf.write("\2\2\2\u0163\u0164\7T\2\2\u0164\u0165\7g\2\2\u0165\u0166")
        buf.write("\7v\2\2\u0166\u0167\7w\2\2\u0167\u0168\7t\2\2\u0168\u0169")
        buf.write("\7p\2\2\u0169<\3\2\2\2\u016a\u016b\7P\2\2\u016b\u016c")
        buf.write("\7w\2\2\u016c\u016d\7n\2\2\u016d\u016e\7n\2\2\u016e>\3")
        buf.write("\2\2\2\u016f\u0170\7E\2\2\u0170\u0171\7n\2\2\u0171\u0172")
        buf.write("\7c\2\2\u0172\u0173\7u\2\2\u0173\u0174\7u\2\2\u0174@\3")
        buf.write("\2\2\2\u0175\u0176\7X\2\2\u0176\u0177\7c\2\2\u0177\u0178")
        buf.write("\7n\2\2\u0178B\3\2\2\2\u0179\u017a\7X\2\2\u017a\u017b")
        buf.write("\7c\2\2\u017b\u017c\7t\2\2\u017cD\3\2\2\2\u017d\u017e")
        buf.write("\7E\2\2\u017e\u017f\7q\2\2\u017f\u0180\7p\2\2\u0180\u0181")
        buf.write("\7u\2\2\u0181\u0182\7v\2\2\u0182\u0183\7t\2\2\u0183\u0184")
        buf.write("\7w\2\2\u0184\u0185\7e\2\2\u0185\u0186\7v\2\2\u0186\u0187")
        buf.write("\7q\2\2\u0187\u0188\7t\2\2\u0188F\3\2\2\2\u0189\u018a")
        buf.write("\7F\2\2\u018a\u018b\7g\2\2\u018b\u018c\7u\2\2\u018c\u018d")
        buf.write("\7v\2\2\u018d\u018e\7t\2\2\u018e\u018f\7w\2\2\u018f\u0190")
        buf.write("\7e\2\2\u0190\u0191\7v\2\2\u0191\u0192\7q\2\2\u0192\u0193")
        buf.write("\7t\2\2\u0193H\3\2\2\2\u0194\u0195\7P\2\2\u0195\u0196")
        buf.write("\7g\2\2\u0196\u0197\7y\2\2\u0197J\3\2\2\2\u0198\u0199")
        buf.write("\7D\2\2\u0199\u019a\7{\2\2\u019aL\3\2\2\2\u019b\u019c")
        buf.write("\7<\2\2\u019c\u019d\7<\2\2\u019dN\3\2\2\2\u019e\u019f")
        buf.write("\7\60\2\2\u019fP\3\2\2\2\u01a0\u01a1\7a\2\2\u01a1R\3\2")
        buf.write("\2\2\u01a2\u01a3\7-\2\2\u01a3T\3\2\2\2\u01a4\u01a5\7/")
        buf.write("\2\2\u01a5V\3\2\2\2\u01a6\u01a7\7,\2\2\u01a7X\3\2\2\2")
        buf.write("\u01a8\u01a9\7\61\2\2\u01a9Z\3\2\2\2\u01aa\u01ab\7\'\2")
        buf.write("\2\u01ab\\\3\2\2\2\u01ac\u01ad\7#\2\2\u01ad^\3\2\2\2\u01ae")
        buf.write("\u01af\7(\2\2\u01af\u01b0\7(\2\2\u01b0`\3\2\2\2\u01b1")
        buf.write("\u01b2\7~\2\2\u01b2\u01b3\7~\2\2\u01b3b\3\2\2\2\u01b4")
        buf.write("\u01b5\7?\2\2\u01b5\u01b6\7?\2\2\u01b6d\3\2\2\2\u01b7")
        buf.write("\u01b8\7?\2\2\u01b8f\3\2\2\2\u01b9\u01ba\7#\2\2\u01ba")
        buf.write("\u01bb\7?\2\2\u01bbh\3\2\2\2\u01bc\u01bd\7@\2\2\u01bd")
        buf.write("j\3\2\2\2\u01be\u01bf\7>\2\2\u01bfl\3\2\2\2\u01c0\u01c1")
        buf.write("\7@\2\2\u01c1\u01c2\7?\2\2\u01c2n\3\2\2\2\u01c3\u01c4")
        buf.write("\7>\2\2\u01c4\u01c5\7?\2\2\u01c5p\3\2\2\2\u01c6\u01c7")
        buf.write("\7?\2\2\u01c7\u01c8\7?\2\2\u01c8\u01c9\7\60\2\2\u01c9")
        buf.write("r\3\2\2\2\u01ca\u01cb\7-\2\2\u01cb\u01cc\7\60\2\2\u01cc")
        buf.write("t\3\2\2\2\u01cd\u01ce\7*\2\2\u01cev\3\2\2\2\u01cf\u01d0")
        buf.write("\7+\2\2\u01d0x\3\2\2\2\u01d1\u01d2\7]\2\2\u01d2z\3\2\2")
        buf.write("\2\u01d3\u01d4\7_\2\2\u01d4|\3\2\2\2\u01d5\u01d6\7}\2")
        buf.write("\2\u01d6~\3\2\2\2\u01d7\u01d8\7\177\2\2\u01d8\u0080\3")
        buf.write("\2\2\2\u01d9\u01da\7\60\2\2\u01da\u0082\3\2\2\2\u01db")
        buf.write("\u01dc\7.\2\2\u01dc\u0084\3\2\2\2\u01dd\u01de\7<\2\2\u01de")
        buf.write("\u0086\3\2\2\2\u01df\u01e0\7=\2\2\u01e0\u0088\3\2\2\2")
        buf.write("\u01e1\u01e2\7,\2\2\u01e2\u01e3\7,\2\2\u01e3\u01e7\3\2")
        buf.write("\2\2\u01e4\u01e6\13\2\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e9")
        buf.write("\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e8")
        buf.write("\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01eb\7,\2\2")
        buf.write("\u01eb\u01ec\7,\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ee\b")
        buf.write("E\3\2\u01ee\u008a\3\2\2\2\u01ef\u01f1\t\b\2\2\u01f0\u01ef")
        buf.write("\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2")
        buf.write("\u01f3\3\2\2\2\u01f3\u01f4\3\2\2\2\u01f4\u01f5\bF\3\2")
        buf.write("\u01f5\u008c\3\2\2\2\u01f6\u01fa\7$\2\2\u01f7\u01f9\5")
        buf.write("\u0091I\2\u01f8\u01f7\3\2\2\2\u01f9\u01fc\3\2\2\2\u01fa")
        buf.write("\u01f8\3\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2")
        buf.write("\u01fc\u01fa\3\2\2\2\u01fd\u01fe\bG\4\2\u01fe\u008e\3")
        buf.write("\2\2\2\u01ff\u0203\7$\2\2\u0200\u0202\5\u0091I\2\u0201")
        buf.write("\u0200\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0206\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0206\u0207\5\u0095K\2\u0207\u0208\bH\5\2\u0208")
        buf.write("\u0090\3\2\2\2\u0209\u020e\n\t\2\2\u020a\u020e\5\u0093")
        buf.write("J\2\u020b\u020c\7)\2\2\u020c\u020e\7$\2\2\u020d\u0209")
        buf.write("\3\2\2\2\u020d\u020a\3\2\2\2\u020d\u020b\3\2\2\2\u020e")
        buf.write("\u0092\3\2\2\2\u020f\u0210\7^\2\2\u0210\u0211\t\n\2\2")
        buf.write("\u0211\u0094\3\2\2\2\u0212\u0213\7^\2\2\u0213\u0216\n")
        buf.write("\n\2\2\u0214\u0216\n\13\2\2\u0215\u0212\3\2\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216\u0096\3\2\2\2\u0217\u0218\13\2\2")
        buf.write("\2\u0218\u0219\bL\6\2\u0219\u0098\3\2\2\2\u021a\u021c")
        buf.write("\t\7\2\2\u021b\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d")
        buf.write("\u021b\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u009a\3\2\2\2")
        buf.write("\u021f\u0220\t\f\2\2\u0220\u009c\3\2\2\2\u0221\u0222\t")
        buf.write("\r\2\2\u0222\u009e\3\2\2\2\u0223\u0224\t\16\2\2\u0224")
        buf.write("\u00a0\3\2\2\2\36\2\u00a7\u00ac\u00b2\u00b8\u00bf\u00c3")
        buf.write("\u00c8\u00cf\u00d5\u00dc\u00e6\u00e8\u00ed\u00f3\u00f8")
        buf.write("\u00fa\u00fe\u0104\u010a\u010c\u01e7\u01f2\u01fa\u0203")
        buf.write("\u020d\u0215\u021d\7\3\6\2\b\2\2\3G\3\3H\4\3L\5")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    TYPE = 2
    CONDITION = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLLIT = 6
    IDENTIFIERS = 7
    DOLLAR = 8
    BREAK = 9
    CONTINUE = 10
    IF = 11
    ELSEIF = 12
    ELSE = 13
    FOREACH = 14
    TRUE = 15
    FALSE = 16
    ARRAY = 17
    IN = 18
    INT = 19
    FLOAT = 20
    BOOLEAN = 21
    STRING = 22
    RETURN = 23
    NULL = 24
    CLASS = 25
    VAL = 26
    VAR = 27
    CONSTRUCTOR = 28
    DESTRUCTOR = 29
    NEW = 30
    BY = 31
    DOUBLECOLONOP = 32
    DOUBLEDOTOP = 33
    UNDERSCORE = 34
    PLUSOP = 35
    MINUSOP = 36
    MULTIPLYOP = 37
    DIVIDEOP = 38
    MODULOOP = 39
    NOTOP = 40
    ANDOP = 41
    OROP = 42
    EQUALOP = 43
    ASSIGNOP = 44
    NOTEQUAL = 45
    GT = 46
    LT = 47
    GTE = 48
    LTE = 49
    STREQUALOP = 50
    STRCONCATOP = 51
    LB = 52
    RB = 53
    LSB = 54
    RSB = 55
    LCB = 56
    RCB = 57
    DOT = 58
    COMMA = 59
    COLON = 60
    SEMICOLON = 61
    BLOCK_COMMENT = 62
    WS = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ERROR_CHAR = 66
    ID = 67

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\"'", "'$'", "'Break'", "'Continue'", "'If'", "'Elseif'", 
            "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", "'In'", 
            "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", 
            "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'::'", "'_'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", "'!='", "'>'", 
            "'<'", "'>='", "'<='", "'==.'", "'+.'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE", "CONDITION", "INTLIT", "FLOATLIT", "BOOLLIT", "IDENTIFIERS", 
            "DOLLAR", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
            "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", 
            "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GT", "LT", "GTE", 
            "LTE", "STREQUALOP", "STRCONCATOP", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", "BLOCK_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "ID" ]

    ruleNames = [ "T__0", "TYPE", "CONDITION", "INTLIT", "DEC", "HEX", "OCT", 
                  "BIN", "FLOATLIT", "DECIMALPART", "EXPONENTPART", "BOOLLIT", 
                  "IDENTIFIERS", "DOLLAR", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GT", 
                  "LT", "GTE", "LTE", "STREQUALOP", "STRCONCATOP", "LB", 
                  "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", 
                  "SEMICOLON", "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", 
                  "ERROR_CHAR", "ID", "B", "E", "X" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[4] = self.DEC_action 
            actions[69] = self.UNCLOSE_STRING_action 
            actions[70] = self.ILLEGAL_ESCAPE_action 
            actions[74] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def DEC_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	current = str(self.text)
            	raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:
             raise ErrorToken(self.text) 
     


