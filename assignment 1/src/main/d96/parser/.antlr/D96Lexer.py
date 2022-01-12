# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2G")
        buf.write("\u01fb\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\5\2\u00a4\n\2\3\3")
        buf.write("\3\3\7\3\u00a8\n\3\f\3\16\3\u00ab\13\3\3\3\3\3\6\3\u00af")
        buf.write("\n\3\r\3\16\3\u00b0\7\3\u00b3\n\3\f\3\16\3\u00b6\13\3")
        buf.write("\3\3\3\3\5\3\u00ba\n\3\3\4\3\4\3\4\6\4\u00bf\n\4\r\4\16")
        buf.write("\4\u00c0\3\5\3\5\6\5\u00c5\n\5\r\5\16\5\u00c6\3\6\3\6")
        buf.write("\3\6\6\6\u00cc\n\6\r\6\16\6\u00cd\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\6\b\u00d6\n\b\r\b\16\b\u00d7\5\b\u00da\n\b\3\t\7")
        buf.write("\t\u00dd\n\t\f\t\16\t\u00e0\13\t\3\t\3\t\3\t\5\t\u00e5")
        buf.write("\n\t\3\t\6\t\u00e8\n\t\r\t\16\t\u00e9\5\t\u00ec\n\t\3")
        buf.write("\n\3\n\5\n\u00f0\n\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3")
        buf.write("&\3\'\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3")
        buf.write("/\3/\3/\3\60\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\38\39\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>")
        buf.write("\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3E\7")
        buf.write("E\u01d4\nE\fE\16E\u01d7\13E\3E\3E\3E\3E\3E\3F\6F\u01df")
        buf.write("\nF\rF\16F\u01e0\3F\3F\3G\3G\3H\3H\3I\3I\3I\3J\3J\3J\5")
        buf.write("J\u01ef\nJ\3K\3K\3K\3L\3L\3M\3M\3N\3N\3O\3O\4\u00de\u01d5")
        buf.write("\2P\3\3\5\2\7\2\t\2\13\2\r\4\17\2\21\2\23\5\25\6\27\7")
        buf.write("\31\b\33\t\35\n\37\13!\f#\r%\16\'\17)\20+\21-\22/\23\61")
        buf.write("\24\63\25\65\26\67\279\30;\31=\32?\33A\34C\35E\36G\37")
        buf.write("I K!M\"O#Q$S%U&W\'Y([)]*_+a,c-e.g/i\60k\61m\62o\63q\64")
        buf.write("s\65u\66w\67y8{9}:\177;\u0081<\u0083=\u0085>\u0087?\u0089")
        buf.write("@\u008bA\u008dB\u008fC\u0091D\u0093E\u0095F\u0097G\u0099")
        buf.write("\2\u009b\2\u009d\2\3\2\r\3\2\63;\3\2\62;\5\2\62;CHch\3")
        buf.write("\2\62\63\5\2\n\f\16\17\"\"\n\2$$))^^ddhhppttvv\3\2^^\5")
        buf.write("\2C\\aac|\4\2DDdd\4\2GGgg\4\2ZZzz\2\u0206\2\3\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\3\u00a3\3\2\2\2\5\u00b9")
        buf.write("\3\2\2\2\7\u00bb\3\2\2\2\t\u00c2\3\2\2\2\13\u00c8\3\2")
        buf.write("\2\2\r\u00cf\3\2\2\2\17\u00d9\3\2\2\2\21\u00de\3\2\2\2")
        buf.write("\23\u00ef\3\2\2\2\25\u00f1\3\2\2\2\27\u00f3\3\2\2\2\31")
        buf.write("\u00f5\3\2\2\2\33\u00f7\3\2\2\2\35\u00fd\3\2\2\2\37\u0106")
        buf.write("\3\2\2\2!\u0109\3\2\2\2#\u0110\3\2\2\2%\u0115\3\2\2\2")
        buf.write("\'\u011d\3\2\2\2)\u0122\3\2\2\2+\u0128\3\2\2\2-\u012e")
        buf.write("\3\2\2\2/\u0131\3\2\2\2\61\u0135\3\2\2\2\63\u013b\3\2")
        buf.write("\2\2\65\u0143\3\2\2\2\67\u014a\3\2\2\29\u0151\3\2\2\2")
        buf.write(";\u0156\3\2\2\2=\u015c\3\2\2\2?\u0160\3\2\2\2A\u0164\3")
        buf.write("\2\2\2C\u0170\3\2\2\2E\u017b\3\2\2\2G\u017f\3\2\2\2I\u0182")
        buf.write("\3\2\2\2K\u0187\3\2\2\2M\u018a\3\2\2\2O\u018c\3\2\2\2")
        buf.write("Q\u018e\3\2\2\2S\u0190\3\2\2\2U\u0192\3\2\2\2W\u0194\3")
        buf.write("\2\2\2Y\u0196\3\2\2\2[\u0198\3\2\2\2]\u019a\3\2\2\2_\u019d")
        buf.write("\3\2\2\2a\u01a0\3\2\2\2c\u01a3\3\2\2\2e\u01a5\3\2\2\2")
        buf.write("g\u01a8\3\2\2\2i\u01aa\3\2\2\2k\u01ac\3\2\2\2m\u01af\3")
        buf.write("\2\2\2o\u01b2\3\2\2\2q\u01b6\3\2\2\2s\u01b9\3\2\2\2u\u01bb")
        buf.write("\3\2\2\2w\u01bd\3\2\2\2y\u01bf\3\2\2\2{\u01c1\3\2\2\2")
        buf.write("}\u01c3\3\2\2\2\177\u01c5\3\2\2\2\u0081\u01c7\3\2\2\2")
        buf.write("\u0083\u01c9\3\2\2\2\u0085\u01cb\3\2\2\2\u0087\u01cd\3")
        buf.write("\2\2\2\u0089\u01cf\3\2\2\2\u008b\u01de\3\2\2\2\u008d\u01e4")
        buf.write("\3\2\2\2\u008f\u01e6\3\2\2\2\u0091\u01e8\3\2\2\2\u0093")
        buf.write("\u01ee\3\2\2\2\u0095\u01f0\3\2\2\2\u0097\u01f3\3\2\2\2")
        buf.write("\u0099\u01f5\3\2\2\2\u009b\u01f7\3\2\2\2\u009d\u01f9\3")
        buf.write("\2\2\2\u009f\u00a4\5\5\3\2\u00a0\u00a4\5\7\4\2\u00a1\u00a4")
        buf.write("\5\t\5\2\u00a2\u00a4\5\13\6\2\u00a3\u009f\3\2\2\2\u00a3")
        buf.write("\u00a0\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a2\3\2\2\2")
        buf.write("\u00a4\4\3\2\2\2\u00a5\u00a9\t\2\2\2\u00a6\u00a8\t\3\2")
        buf.write("\2\u00a7\u00a6\3\2\2\2\u00a8\u00ab\3\2\2\2\u00a9\u00a7")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b4\3\2\2\2\u00ab")
        buf.write("\u00a9\3\2\2\2\u00ac\u00ae\5O(\2\u00ad\u00af\t\3\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\u00b3\3\2\2\2\u00b2\u00ac\3")
        buf.write("\2\2\2\u00b3\u00b6\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5")
        buf.write("\3\2\2\2\u00b5\u00b7\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b7")
        buf.write("\u00ba\b\3\2\2\u00b8\u00ba\7\62\2\2\u00b9\u00a5\3\2\2")
        buf.write("\2\u00b9\u00b8\3\2\2\2\u00ba\6\3\2\2\2\u00bb\u00bc\7\62")
        buf.write("\2\2\u00bc\u00be\5\u009dO\2\u00bd\u00bf\t\2\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\b\3\2\2\2\u00c2\u00c4\7\62")
        buf.write("\2\2\u00c3\u00c5\t\4\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c6")
        buf.write("\3\2\2\2\u00c6\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7")
        buf.write("\n\3\2\2\2\u00c8\u00c9\7\62\2\2\u00c9\u00cb\5\u0099M\2")
        buf.write("\u00ca\u00cc\t\5\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3")
        buf.write("\2\2\2\u00cd\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\f")
        buf.write("\3\2\2\2\u00cf\u00d0\5\5\3\2\u00d0\u00d1\5\17\b\2\u00d1")
        buf.write("\u00d2\5\21\t\2\u00d2\16\3\2\2\2\u00d3\u00d5\5\177@\2")
        buf.write("\u00d4\u00d6\t\3\2\2\u00d5\u00d4\3\2\2\2\u00d6\u00d7\3")
        buf.write("\2\2\2\u00d7\u00d5\3\2\2\2\u00d7\u00d8\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d3\3\2\2\2\u00d9\u00da\3\2\2\2\u00da")
        buf.write("\20\3\2\2\2\u00db\u00dd\t\3\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("\u00e0\3\2\2\2\u00de\u00df\3\2\2\2\u00de\u00dc\3\2\2\2")
        buf.write("\u00df\u00eb\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e4\5")
        buf.write("\u009bN\2\u00e2\u00e5\5S*\2\u00e3\u00e5\5Q)\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e3\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5")
        buf.write("\u00e7\3\2\2\2\u00e6\u00e8\t\2\2\2\u00e7\u00e6\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea\3")
        buf.write("\2\2\2\u00ea\u00ec\3\2\2\2\u00eb\u00e1\3\2\2\2\u00eb\u00ec")
        buf.write("\3\2\2\2\u00ec\22\3\2\2\2\u00ed\u00f0\5\'\24\2\u00ee\u00f0")
        buf.write("\5)\25\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2\u00f0")
        buf.write("\24\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\26\3\2\2\2\u00f3")
        buf.write("\u00f4\3\2\2\2\u00f4\30\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6")
        buf.write("\32\3\2\2\2\u00f7\u00f8\7D\2\2\u00f8\u00f9\7t\2\2\u00f9")
        buf.write("\u00fa\7g\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7m\2\2\u00fc")
        buf.write("\34\3\2\2\2\u00fd\u00fe\7E\2\2\u00fe\u00ff\7q\2\2\u00ff")
        buf.write("\u0100\7p\2\2\u0100\u0101\7v\2\2\u0101\u0102\7k\2\2\u0102")
        buf.write("\u0103\7p\2\2\u0103\u0104\7w\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("\36\3\2\2\2\u0106\u0107\7K\2\2\u0107\u0108\7h\2\2\u0108")
        buf.write(" \3\2\2\2\u0109\u010a\7G\2\2\u010a\u010b\7n\2\2\u010b")
        buf.write("\u010c\7u\2\2\u010c\u010d\7g\2\2\u010d\u010e\7k\2\2\u010e")
        buf.write("\u010f\7h\2\2\u010f\"\3\2\2\2\u0110\u0111\7G\2\2\u0111")
        buf.write("\u0112\7n\2\2\u0112\u0113\7u\2\2\u0113\u0114\7g\2\2\u0114")
        buf.write("$\3\2\2\2\u0115\u0116\7H\2\2\u0116\u0117\7q\2\2\u0117")
        buf.write("\u0118\7t\2\2\u0118\u0119\7g\2\2\u0119\u011a\7c\2\2\u011a")
        buf.write("\u011b\7e\2\2\u011b\u011c\7j\2\2\u011c&\3\2\2\2\u011d")
        buf.write("\u011e\7V\2\2\u011e\u011f\7t\2\2\u011f\u0120\7w\2\2\u0120")
        buf.write("\u0121\7g\2\2\u0121(\3\2\2\2\u0122\u0123\7H\2\2\u0123")
        buf.write("\u0124\7c\2\2\u0124\u0125\7n\2\2\u0125\u0126\7u\2\2\u0126")
        buf.write("\u0127\7g\2\2\u0127*\3\2\2\2\u0128\u0129\7C\2\2\u0129")
        buf.write("\u012a\7t\2\2\u012a\u012b\7t\2\2\u012b\u012c\7c\2\2\u012c")
        buf.write("\u012d\7{\2\2\u012d,\3\2\2\2\u012e\u012f\7K\2\2\u012f")
        buf.write("\u0130\7p\2\2\u0130.\3\2\2\2\u0131\u0132\7K\2\2\u0132")
        buf.write("\u0133\7p\2\2\u0133\u0134\7v\2\2\u0134\60\3\2\2\2\u0135")
        buf.write("\u0136\7H\2\2\u0136\u0137\7n\2\2\u0137\u0138\7q\2\2\u0138")
        buf.write("\u0139\7c\2\2\u0139\u013a\7v\2\2\u013a\62\3\2\2\2\u013b")
        buf.write("\u013c\7D\2\2\u013c\u013d\7q\2\2\u013d\u013e\7q\2\2\u013e")
        buf.write("\u013f\7n\2\2\u013f\u0140\7g\2\2\u0140\u0141\7c\2\2\u0141")
        buf.write("\u0142\7p\2\2\u0142\64\3\2\2\2\u0143\u0144\7U\2\2\u0144")
        buf.write("\u0145\7v\2\2\u0145\u0146\7t\2\2\u0146\u0147\7k\2\2\u0147")
        buf.write("\u0148\7p\2\2\u0148\u0149\7i\2\2\u0149\66\3\2\2\2\u014a")
        buf.write("\u014b\7T\2\2\u014b\u014c\7g\2\2\u014c\u014d\7v\2\2\u014d")
        buf.write("\u014e\7w\2\2\u014e\u014f\7t\2\2\u014f\u0150\7p\2\2\u0150")
        buf.write("8\3\2\2\2\u0151\u0152\7P\2\2\u0152\u0153\7w\2\2\u0153")
        buf.write("\u0154\7n\2\2\u0154\u0155\7n\2\2\u0155:\3\2\2\2\u0156")
        buf.write("\u0157\7E\2\2\u0157\u0158\7n\2\2\u0158\u0159\7c\2\2\u0159")
        buf.write("\u015a\7u\2\2\u015a\u015b\7u\2\2\u015b<\3\2\2\2\u015c")
        buf.write("\u015d\7X\2\2\u015d\u015e\7c\2\2\u015e\u015f\7n\2\2\u015f")
        buf.write(">\3\2\2\2\u0160\u0161\7X\2\2\u0161\u0162\7c\2\2\u0162")
        buf.write("\u0163\7t\2\2\u0163@\3\2\2\2\u0164\u0165\7E\2\2\u0165")
        buf.write("\u0166\7q\2\2\u0166\u0167\7p\2\2\u0167\u0168\7u\2\2\u0168")
        buf.write("\u0169\7v\2\2\u0169\u016a\7t\2\2\u016a\u016b\7w\2\2\u016b")
        buf.write("\u016c\7e\2\2\u016c\u016d\7v\2\2\u016d\u016e\7q\2\2\u016e")
        buf.write("\u016f\7t\2\2\u016fB\3\2\2\2\u0170\u0171\7F\2\2\u0171")
        buf.write("\u0172\7g\2\2\u0172\u0173\7u\2\2\u0173\u0174\7v\2\2\u0174")
        buf.write("\u0175\7t\2\2\u0175\u0176\7w\2\2\u0176\u0177\7e\2\2\u0177")
        buf.write("\u0178\7v\2\2\u0178\u0179\7q\2\2\u0179\u017a\7t\2\2\u017a")
        buf.write("D\3\2\2\2\u017b\u017c\7P\2\2\u017c\u017d\7g\2\2\u017d")
        buf.write("\u017e\7y\2\2\u017eF\3\2\2\2\u017f\u0180\7D\2\2\u0180")
        buf.write("\u0181\7{\2\2\u0181H\3\2\2\2\u0182\u0183\7U\2\2\u0183")
        buf.write("\u0184\7g\2\2\u0184\u0185\7n\2\2\u0185\u0186\7h\2\2\u0186")
        buf.write("J\3\2\2\2\u0187\u0188\7<\2\2\u0188\u0189\7<\2\2\u0189")
        buf.write("L\3\2\2\2\u018a\u018b\7\60\2\2\u018bN\3\2\2\2\u018c\u018d")
        buf.write("\7a\2\2\u018dP\3\2\2\2\u018e\u018f\7-\2\2\u018fR\3\2\2")
        buf.write("\2\u0190\u0191\7/\2\2\u0191T\3\2\2\2\u0192\u0193\7,\2")
        buf.write("\2\u0193V\3\2\2\2\u0194\u0195\7\61\2\2\u0195X\3\2\2\2")
        buf.write("\u0196\u0197\7\'\2\2\u0197Z\3\2\2\2\u0198\u0199\7#\2\2")
        buf.write("\u0199\\\3\2\2\2\u019a\u019b\7(\2\2\u019b\u019c\7(\2\2")
        buf.write("\u019c^\3\2\2\2\u019d\u019e\7~\2\2\u019e\u019f\7~\2\2")
        buf.write("\u019f`\3\2\2\2\u01a0\u01a1\7?\2\2\u01a1\u01a2\7?\2\2")
        buf.write("\u01a2b\3\2\2\2\u01a3\u01a4\7?\2\2\u01a4d\3\2\2\2\u01a5")
        buf.write("\u01a6\7#\2\2\u01a6\u01a7\7?\2\2\u01a7f\3\2\2\2\u01a8")
        buf.write("\u01a9\7@\2\2\u01a9h\3\2\2\2\u01aa\u01ab\7>\2\2\u01ab")
        buf.write("j\3\2\2\2\u01ac\u01ad\7@\2\2\u01ad\u01ae\7?\2\2\u01ae")
        buf.write("l\3\2\2\2\u01af\u01b0\7>\2\2\u01b0\u01b1\7?\2\2\u01b1")
        buf.write("n\3\2\2\2\u01b2\u01b3\7?\2\2\u01b3\u01b4\7?\2\2\u01b4")
        buf.write("\u01b5\7\60\2\2\u01b5p\3\2\2\2\u01b6\u01b7\7-\2\2\u01b7")
        buf.write("\u01b8\7\60\2\2\u01b8r\3\2\2\2\u01b9\u01ba\7*\2\2\u01ba")
        buf.write("t\3\2\2\2\u01bb\u01bc\7+\2\2\u01bcv\3\2\2\2\u01bd\u01be")
        buf.write("\7]\2\2\u01bex\3\2\2\2\u01bf\u01c0\7_\2\2\u01c0z\3\2\2")
        buf.write("\2\u01c1\u01c2\7}\2\2\u01c2|\3\2\2\2\u01c3\u01c4\7\177")
        buf.write("\2\2\u01c4~\3\2\2\2\u01c5\u01c6\7\60\2\2\u01c6\u0080\3")
        buf.write("\2\2\2\u01c7\u01c8\7.\2\2\u01c8\u0082\3\2\2\2\u01c9\u01ca")
        buf.write("\7<\2\2\u01ca\u0084\3\2\2\2\u01cb\u01cc\7=\2\2\u01cc\u0086")
        buf.write("\3\2\2\2\u01cd\u01ce\7&\2\2\u01ce\u0088\3\2\2\2\u01cf")
        buf.write("\u01d0\7,\2\2\u01d0\u01d1\7,\2\2\u01d1\u01d5\3\2\2\2\u01d2")
        buf.write("\u01d4\13\2\2\2\u01d3\u01d2\3\2\2\2\u01d4\u01d7\3\2\2")
        buf.write("\2\u01d5\u01d6\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01d8")
        buf.write("\3\2\2\2\u01d7\u01d5\3\2\2\2\u01d8\u01d9\7,\2\2\u01d9")
        buf.write("\u01da\7,\2\2\u01da\u01db\3\2\2\2\u01db\u01dc\bE\3\2\u01dc")
        buf.write("\u008a\3\2\2\2\u01dd\u01df\t\6\2\2\u01de\u01dd\3\2\2\2")
        buf.write("\u01df\u01e0\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1\3")
        buf.write("\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e3\bF\3\2\u01e3\u008c")
        buf.write("\3\2\2\2\u01e4\u01e5\13\2\2\2\u01e5\u008e\3\2\2\2\u01e6")
        buf.write("\u01e7\13\2\2\2\u01e7\u0090\3\2\2\2\u01e8\u01e9\7^\2\2")
        buf.write("\u01e9\u01ea\t\7\2\2\u01ea\u0092\3\2\2\2\u01eb\u01ec\7")
        buf.write("^\2\2\u01ec\u01ef\n\7\2\2\u01ed\u01ef\n\b\2\2\u01ee\u01eb")
        buf.write("\3\2\2\2\u01ee\u01ed\3\2\2\2\u01ef\u0094\3\2\2\2\u01f0")
        buf.write("\u01f1\13\2\2\2\u01f1\u01f2\bK\4\2\u01f2\u0096\3\2\2\2")
        buf.write("\u01f3\u01f4\t\t\2\2\u01f4\u0098\3\2\2\2\u01f5\u01f6\t")
        buf.write("\n\2\2\u01f6\u009a\3\2\2\2\u01f7\u01f8\t\13\2\2\u01f8")
        buf.write("\u009c\3\2\2\2\u01f9\u01fa\t\f\2\2\u01fa\u009e\3\2\2\2")
        buf.write("\25\2\u00a3\u00a9\u00b0\u00b4\u00b9\u00c0\u00c6\u00cd")
        buf.write("\u00d7\u00d9\u00de\u00e4\u00e9\u00eb\u00ef\u01d5\u01e0")
        buf.write("\u01ee\5\3\3\2\b\2\2\3K\3")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLLIT = 3
    STRINGLIT = 4
    INDEXEDARRAYLIT = 5
    MULTIDIMENSIONALARRAYLIT = 6
    BREAK = 7
    CONTINUE = 8
    IF = 9
    ELSEIF = 10
    ELSE = 11
    FOREACH = 12
    TRUE = 13
    FALSE = 14
    ARRAY = 15
    IN = 16
    INT = 17
    FLOAT = 18
    BOOLEAN = 19
    STRING = 20
    RETURN = 21
    NULL = 22
    CLASS = 23
    VAL = 24
    VAR = 25
    CONSTRUCTOR = 26
    DESTRUCTOR = 27
    NEW = 28
    BY = 29
    SELF = 30
    DOUBLECOLONOP = 31
    DOUBLEDOTOP = 32
    UNDERSCORE = 33
    PLUSOP = 34
    MINUSOP = 35
    MULTIPLYOP = 36
    DIVIDEOP = 37
    MODULOOP = 38
    NOTOP = 39
    ANDOP = 40
    OROP = 41
    EQUALOP = 42
    ASSIGNOP = 43
    NOTEQUAL = 44
    GT = 45
    LT = 46
    GTE = 47
    LTE = 48
    STREQUALOP = 49
    STRCONCATOP = 50
    LB = 51
    RB = 52
    LSB = 53
    RSB = 54
    LCB = 55
    RCB = 56
    DOT = 57
    COMMA = 58
    COLON = 59
    SEMICOLON = 60
    DOLLARD = 61
    BLOCK_COMMENT = 62
    WS = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    ESC_SEQ = 66
    ESC_ILLEGAL = 67
    ERROR_CHAR = 68
    ID = 69

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'::'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
            "':'", "';'", "'$'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "INDEXEDARRAYLIT", 
            "MULTIDIMENSIONALARRAYLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
            "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
            "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", 
            "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", "DOUBLECOLONOP", 
            "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", 
            "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", 
            "ASSIGNOP", "NOTEQUAL", "GT", "LT", "GTE", "LTE", "STREQUALOP", 
            "STRCONCATOP", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", 
            "COMMA", "COLON", "SEMICOLON", "DOLLARD", "BLOCK_COMMENT", "WS", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_SEQ", "ESC_ILLEGAL", 
            "ERROR_CHAR", "ID" ]

    ruleNames = [ "INTLIT", "DEC", "HEX", "OCT", "BIN", "FLOATLIT", "DECIMALPART", 
                  "EXPONENTPART", "BOOLLIT", "STRINGLIT", "INDEXEDARRAYLIT", 
                  "MULTIDIMENSIONALARRAYLIT", "BREAK", "CONTINUE", "IF", 
                  "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
                  "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", 
                  "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", 
                  "GT", "LT", "GTE", "LTE", "STREQUALOP", "STRCONCATOP", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                  "COLON", "SEMICOLON", "DOLLARD", "BLOCK_COMMENT", "WS", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ESC_SEQ", "ESC_ILLEGAL", 
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
            actions[1] = self.DEC_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def DEC_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             self.text = self.text.replace("_", "")
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             raise ErrorToken(self.text) 
     


