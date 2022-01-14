# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u021e\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\7\2\u00a2\n\2\f\2\16\2\u00a5")
        buf.write("\13\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00ae\n\3\3\4\3")
        buf.write("\4\3\4\5\4\u00b3\n\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00bb")
        buf.write("\n\5\3\6\6\6\u00be\n\6\r\6\16\6\u00bf\3\6\3\6\7\6\u00c4")
        buf.write("\n\6\f\6\16\6\u00c7\13\6\3\7\3\7\3\7\6\7\u00cc\n\7\r\7")
        buf.write("\16\7\u00cd\3\b\3\b\6\b\u00d2\n\b\r\b\16\b\u00d3\3\t\3")
        buf.write("\t\3\t\6\t\u00d9\n\t\r\t\16\t\u00da\3\n\6\n\u00de\n\n")
        buf.write("\r\n\16\n\u00df\3\n\3\n\5\n\u00e4\n\n\3\n\5\n\u00e7\n")
        buf.write("\n\3\13\3\13\6\13\u00eb\n\13\r\13\16\13\u00ec\3\f\3\f")
        buf.write("\3\f\5\f\u00f2\n\f\3\f\6\f\u00f5\n\f\r\f\16\f\u00f6\3")
        buf.write("\r\3\r\5\r\u00fb\n\r\3\16\3\16\6\16\u00ff\n\16\r\16\16")
        buf.write("\16\u0100\3\16\3\16\7\16\u0105\n\16\f\16\16\16\u0108\13")
        buf.write("\16\5\16\u010a\n\16\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$")
        buf.write("\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3")
        buf.write("\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\38\38\3")
        buf.write("8\39\39\39\39\3:\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3")
        buf.write("@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3D\3D\7D\u01e1\nD\fD\16D")
        buf.write("\u01e4\13D\3D\3D\3D\3D\3D\3E\6E\u01ec\nE\rE\16E\u01ed")
        buf.write("\3E\3E\3F\3F\7F\u01f4\nF\fF\16F\u01f7\13F\3F\3F\3G\3G")
        buf.write("\7G\u01fd\nG\fG\16G\u0200\13G\3G\3G\3G\3H\3H\5H\u0207")
        buf.write("\nH\3I\3I\3I\3J\3J\3J\5J\u020f\nJ\3K\3K\3K\3L\6L\u0215")
        buf.write("\nL\rL\16L\u0216\3M\3M\3N\3N\3O\3O\3\u01e2\2P\3\3\5\4")
        buf.write("\7\5\t\6\13\2\r\2\17\2\21\2\23\7\25\2\27\2\31\b\33\t\35")
        buf.write("\2\37\n!\13#\f%\r\'\16)\17+\20-\21/\22\61\23\63\24\65")
        buf.write("\25\67\269\27;\30=\31?\32A\33C\34E\35G\36I\37K M!O\"Q")
        buf.write("#S$U%W&Y\'[(])_*a+c,e-g.i/k\60m\61o\62q\63s\64u\65w\66")
        buf.write("y\67{8}9\177:\u0081;\u0083<\u0085=\u0087>\u0089?\u008b")
        buf.write("@\u008dA\u008f\2\u0091\2\u0093\2\u0095B\u0097C\u0099\2")
        buf.write("\u009b\2\u009d\2\3\2\20\3\2\63;\3\2\62;\5\2\62;CHch\3")
        buf.write("\2\629\3\2\62\63\6\2\62;C\\aac|\5\2C\\aac|\5\2\n\f\16")
        buf.write("\17\"\"\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttvv\3\2^^")
        buf.write("\4\2DDdd\4\2GGgg\4\2ZZzz\2\u0231\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\23\3\2\2\2\2\31\3\2\2\2\2")
        buf.write("\33\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2")
        buf.write("\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3")
        buf.write("\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2")
        buf.write("\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3")
        buf.write("\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K")
        buf.write("\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2")
        buf.write("U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2")
        buf.write("\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2")
        buf.write("\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2")
        buf.write("\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00ad\3\2\2\2\7\u00b2\3\2\2")
        buf.write("\2\t\u00ba\3\2\2\2\13\u00bd\3\2\2\2\r\u00c8\3\2\2\2\17")
        buf.write("\u00cf\3\2\2\2\21\u00d5\3\2\2\2\23\u00dd\3\2\2\2\25\u00e8")
        buf.write("\3\2\2\2\27\u00ee\3\2\2\2\31\u00fa\3\2\2\2\33\u0109\3")
        buf.write("\2\2\2\35\u010b\3\2\2\2\37\u010d\3\2\2\2!\u0113\3\2\2")
        buf.write("\2#\u011c\3\2\2\2%\u011f\3\2\2\2\'\u0126\3\2\2\2)\u012b")
        buf.write("\3\2\2\2+\u0133\3\2\2\2-\u0138\3\2\2\2/\u013e\3\2\2\2")
        buf.write("\61\u0144\3\2\2\2\63\u0147\3\2\2\2\65\u014b\3\2\2\2\67")
        buf.write("\u0151\3\2\2\29\u0159\3\2\2\2;\u0160\3\2\2\2=\u0167\3")
        buf.write("\2\2\2?\u016c\3\2\2\2A\u0172\3\2\2\2C\u0176\3\2\2\2E\u017a")
        buf.write("\3\2\2\2G\u0186\3\2\2\2I\u0191\3\2\2\2K\u0195\3\2\2\2")
        buf.write("M\u0198\3\2\2\2O\u019b\3\2\2\2Q\u019d\3\2\2\2S\u019f\3")
        buf.write("\2\2\2U\u01a1\3\2\2\2W\u01a3\3\2\2\2Y\u01a5\3\2\2\2[\u01a7")
        buf.write("\3\2\2\2]\u01a9\3\2\2\2_\u01ab\3\2\2\2a\u01ae\3\2\2\2")
        buf.write("c\u01b1\3\2\2\2e\u01b4\3\2\2\2g\u01b6\3\2\2\2i\u01b9\3")
        buf.write("\2\2\2k\u01bb\3\2\2\2m\u01bd\3\2\2\2o\u01c0\3\2\2\2q\u01c3")
        buf.write("\3\2\2\2s\u01c7\3\2\2\2u\u01ca\3\2\2\2w\u01cc\3\2\2\2")
        buf.write("y\u01ce\3\2\2\2{\u01d0\3\2\2\2}\u01d2\3\2\2\2\177\u01d4")
        buf.write("\3\2\2\2\u0081\u01d6\3\2\2\2\u0083\u01d8\3\2\2\2\u0085")
        buf.write("\u01da\3\2\2\2\u0087\u01dc\3\2\2\2\u0089\u01eb\3\2\2\2")
        buf.write("\u008b\u01f1\3\2\2\2\u008d\u01fa\3\2\2\2\u008f\u0206\3")
        buf.write("\2\2\2\u0091\u0208\3\2\2\2\u0093\u020e\3\2\2\2\u0095\u0210")
        buf.write("\3\2\2\2\u0097\u0214\3\2\2\2\u0099\u0218\3\2\2\2\u009b")
        buf.write("\u021a\3\2\2\2\u009d\u021c\3\2\2\2\u009f\u00a3\7$\2\2")
        buf.write("\u00a0\u00a2\5\u008fH\2\u00a1\u00a0\3\2\2\2\u00a2\u00a5")
        buf.write("\3\2\2\2\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4")
        buf.write("\u00a6\3\2\2\2\u00a5\u00a3\3\2\2\2\u00a6\u00a7\7$\2\2")
        buf.write("\u00a7\u00a8\b\2\2\2\u00a8\4\3\2\2\2\u00a9\u00ae\5\63")
        buf.write("\32\2\u00aa\u00ae\5\65\33\2\u00ab\u00ae\5\67\34\2\u00ac")
        buf.write("\u00ae\59\35\2\u00ad\u00a9\3\2\2\2\u00ad\u00aa\3\2\2\2")
        buf.write("\u00ad\u00ab\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\6\3\2\2")
        buf.write("\2\u00af\u00b3\5#\22\2\u00b0\u00b3\5%\23\2\u00b1\u00b3")
        buf.write("\5\'\24\2\u00b2\u00af\3\2\2\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\b\3\2\2\2\u00b4\u00b5\5\13\6\2\u00b5")
        buf.write("\u00b6\b\5\3\2\u00b6\u00bb\3\2\2\2\u00b7\u00bb\5\r\7\2")
        buf.write("\u00b8\u00bb\5\17\b\2\u00b9\u00bb\5\21\t\2\u00ba\u00b4")
        buf.write("\3\2\2\2\u00ba\u00b7\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00b9\3\2\2\2\u00bb\n\3\2\2\2\u00bc\u00be\t\2\2\2\u00bd")
        buf.write("\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c0\3\2\2\2\u00c0\u00c5\3\2\2\2\u00c1\u00c4\5")
        buf.write("Q)\2\u00c2\u00c4\t\3\2\2\u00c3\u00c1\3\2\2\2\u00c3\u00c2")
        buf.write("\3\2\2\2\u00c4\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write("\u00c6\3\2\2\2\u00c6\f\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8")
        buf.write("\u00c9\7\62\2\2\u00c9\u00cb\5\u009dO\2\u00ca\u00cc\t\4")
        buf.write("\2\2\u00cb\u00ca\3\2\2\2\u00cc\u00cd\3\2\2\2\u00cd\u00cb")
        buf.write("\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\16\3\2\2\2\u00cf\u00d1")
        buf.write("\7\62\2\2\u00d0\u00d2\t\5\2\2\u00d1\u00d0\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d3\u00d4\3\2\2\2")
        buf.write("\u00d4\20\3\2\2\2\u00d5\u00d6\7\62\2\2\u00d6\u00d8\5\u0099")
        buf.write("M\2\u00d7\u00d9\t\6\2\2\u00d8\u00d7\3\2\2\2\u00d9\u00da")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00da\u00db\3\2\2\2\u00db")
        buf.write("\22\3\2\2\2\u00dc\u00de\t\3\2\2\u00dd\u00dc\3\2\2\2\u00de")
        buf.write("\u00df\3\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2")
        buf.write("\u00e0\u00e6\3\2\2\2\u00e1\u00e3\5\25\13\2\u00e2\u00e4")
        buf.write("\5\27\f\2\u00e3\u00e2\3\2\2\2\u00e3\u00e4\3\2\2\2\u00e4")
        buf.write("\u00e7\3\2\2\2\u00e5\u00e7\5\27\f\2\u00e6\u00e1\3\2\2")
        buf.write("\2\u00e6\u00e5\3\2\2\2\u00e7\24\3\2\2\2\u00e8\u00ea\7")
        buf.write("\60\2\2\u00e9\u00eb\t\3\2\2\u00ea\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ec\3\2\2\2\u00ec\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2")
        buf.write("\u00ed\26\3\2\2\2\u00ee\u00f1\5\u009bN\2\u00ef\u00f2\5")
        buf.write("U+\2\u00f0\u00f2\5S*\2\u00f1\u00ef\3\2\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3\2\2\2\u00f3")
        buf.write("\u00f5\t\3\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2")
        buf.write("\u00f6\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\30\3\2")
        buf.write("\2\2\u00f8\u00fb\5+\26\2\u00f9\u00fb\5-\27\2\u00fa\u00f8")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb\32\3\2\2\2\u00fc\u00fe")
        buf.write("\5\35\17\2\u00fd\u00ff\t\7\2\2\u00fe\u00fd\3\2\2\2\u00ff")
        buf.write("\u0100\3\2\2\2\u0100\u00fe\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101\u010a\3\2\2\2\u0102\u0106\t\b\2\2\u0103\u0105\t")
        buf.write("\7\2\2\u0104\u0103\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0104")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u010a\3\2\2\2\u0108")
        buf.write("\u0106\3\2\2\2\u0109\u00fc\3\2\2\2\u0109\u0102\3\2\2\2")
        buf.write("\u010a\34\3\2\2\2\u010b\u010c\7&\2\2\u010c\36\3\2\2\2")
        buf.write("\u010d\u010e\7D\2\2\u010e\u010f\7t\2\2\u010f\u0110\7g")
        buf.write("\2\2\u0110\u0111\7c\2\2\u0111\u0112\7m\2\2\u0112 \3\2")
        buf.write("\2\2\u0113\u0114\7E\2\2\u0114\u0115\7q\2\2\u0115\u0116")
        buf.write("\7p\2\2\u0116\u0117\7v\2\2\u0117\u0118\7k\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7w\2\2\u011a\u011b\7g\2\2\u011b\"")
        buf.write("\3\2\2\2\u011c\u011d\7K\2\2\u011d\u011e\7h\2\2\u011e$")
        buf.write("\3\2\2\2\u011f\u0120\7G\2\2\u0120\u0121\7n\2\2\u0121\u0122")
        buf.write("\7u\2\2\u0122\u0123\7g\2\2\u0123\u0124\7k\2\2\u0124\u0125")
        buf.write("\7h\2\2\u0125&\3\2\2\2\u0126\u0127\7G\2\2\u0127\u0128")
        buf.write("\7n\2\2\u0128\u0129\7u\2\2\u0129\u012a\7g\2\2\u012a(\3")
        buf.write("\2\2\2\u012b\u012c\7H\2\2\u012c\u012d\7q\2\2\u012d\u012e")
        buf.write("\7t\2\2\u012e\u012f\7g\2\2\u012f\u0130\7c\2\2\u0130\u0131")
        buf.write("\7e\2\2\u0131\u0132\7j\2\2\u0132*\3\2\2\2\u0133\u0134")
        buf.write("\7V\2\2\u0134\u0135\7t\2\2\u0135\u0136\7w\2\2\u0136\u0137")
        buf.write("\7g\2\2\u0137,\3\2\2\2\u0138\u0139\7H\2\2\u0139\u013a")
        buf.write("\7c\2\2\u013a\u013b\7n\2\2\u013b\u013c\7u\2\2\u013c\u013d")
        buf.write("\7g\2\2\u013d.\3\2\2\2\u013e\u013f\7C\2\2\u013f\u0140")
        buf.write("\7t\2\2\u0140\u0141\7t\2\2\u0141\u0142\7c\2\2\u0142\u0143")
        buf.write("\7{\2\2\u0143\60\3\2\2\2\u0144\u0145\7K\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\62\3\2\2\2\u0147\u0148\7K\2\2\u0148\u0149")
        buf.write("\7p\2\2\u0149\u014a\7v\2\2\u014a\64\3\2\2\2\u014b\u014c")
        buf.write("\7H\2\2\u014c\u014d\7n\2\2\u014d\u014e\7q\2\2\u014e\u014f")
        buf.write("\7c\2\2\u014f\u0150\7v\2\2\u0150\66\3\2\2\2\u0151\u0152")
        buf.write("\7D\2\2\u0152\u0153\7q\2\2\u0153\u0154\7q\2\2\u0154\u0155")
        buf.write("\7n\2\2\u0155\u0156\7g\2\2\u0156\u0157\7c\2\2\u0157\u0158")
        buf.write("\7p\2\2\u01588\3\2\2\2\u0159\u015a\7U\2\2\u015a\u015b")
        buf.write("\7v\2\2\u015b\u015c\7t\2\2\u015c\u015d\7k\2\2\u015d\u015e")
        buf.write("\7p\2\2\u015e\u015f\7i\2\2\u015f:\3\2\2\2\u0160\u0161")
        buf.write("\7T\2\2\u0161\u0162\7g\2\2\u0162\u0163\7v\2\2\u0163\u0164")
        buf.write("\7w\2\2\u0164\u0165\7t\2\2\u0165\u0166\7p\2\2\u0166<\3")
        buf.write("\2\2\2\u0167\u0168\7P\2\2\u0168\u0169\7w\2\2\u0169\u016a")
        buf.write("\7n\2\2\u016a\u016b\7n\2\2\u016b>\3\2\2\2\u016c\u016d")
        buf.write("\7E\2\2\u016d\u016e\7n\2\2\u016e\u016f\7c\2\2\u016f\u0170")
        buf.write("\7u\2\2\u0170\u0171\7u\2\2\u0171@\3\2\2\2\u0172\u0173")
        buf.write("\7X\2\2\u0173\u0174\7c\2\2\u0174\u0175\7n\2\2\u0175B\3")
        buf.write("\2\2\2\u0176\u0177\7X\2\2\u0177\u0178\7c\2\2\u0178\u0179")
        buf.write("\7t\2\2\u0179D\3\2\2\2\u017a\u017b\7E\2\2\u017b\u017c")
        buf.write("\7q\2\2\u017c\u017d\7p\2\2\u017d\u017e\7u\2\2\u017e\u017f")
        buf.write("\7v\2\2\u017f\u0180\7t\2\2\u0180\u0181\7w\2\2\u0181\u0182")
        buf.write("\7e\2\2\u0182\u0183\7v\2\2\u0183\u0184\7q\2\2\u0184\u0185")
        buf.write("\7t\2\2\u0185F\3\2\2\2\u0186\u0187\7F\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188\u0189\7u\2\2\u0189\u018a\7v\2\2\u018a\u018b")
        buf.write("\7t\2\2\u018b\u018c\7w\2\2\u018c\u018d\7e\2\2\u018d\u018e")
        buf.write("\7v\2\2\u018e\u018f\7q\2\2\u018f\u0190\7t\2\2\u0190H\3")
        buf.write("\2\2\2\u0191\u0192\7P\2\2\u0192\u0193\7g\2\2\u0193\u0194")
        buf.write("\7y\2\2\u0194J\3\2\2\2\u0195\u0196\7D\2\2\u0196\u0197")
        buf.write("\7{\2\2\u0197L\3\2\2\2\u0198\u0199\7<\2\2\u0199\u019a")
        buf.write("\7<\2\2\u019aN\3\2\2\2\u019b\u019c\7\60\2\2\u019cP\3\2")
        buf.write("\2\2\u019d\u019e\7a\2\2\u019eR\3\2\2\2\u019f\u01a0\7-")
        buf.write("\2\2\u01a0T\3\2\2\2\u01a1\u01a2\7/\2\2\u01a2V\3\2\2\2")
        buf.write("\u01a3\u01a4\7,\2\2\u01a4X\3\2\2\2\u01a5\u01a6\7\61\2")
        buf.write("\2\u01a6Z\3\2\2\2\u01a7\u01a8\7\'\2\2\u01a8\\\3\2\2\2")
        buf.write("\u01a9\u01aa\7#\2\2\u01aa^\3\2\2\2\u01ab\u01ac\7(\2\2")
        buf.write("\u01ac\u01ad\7(\2\2\u01ad`\3\2\2\2\u01ae\u01af\7~\2\2")
        buf.write("\u01af\u01b0\7~\2\2\u01b0b\3\2\2\2\u01b1\u01b2\7?\2\2")
        buf.write("\u01b2\u01b3\7?\2\2\u01b3d\3\2\2\2\u01b4\u01b5\7?\2\2")
        buf.write("\u01b5f\3\2\2\2\u01b6\u01b7\7#\2\2\u01b7\u01b8\7?\2\2")
        buf.write("\u01b8h\3\2\2\2\u01b9\u01ba\7@\2\2\u01baj\3\2\2\2\u01bb")
        buf.write("\u01bc\7>\2\2\u01bcl\3\2\2\2\u01bd\u01be\7@\2\2\u01be")
        buf.write("\u01bf\7?\2\2\u01bfn\3\2\2\2\u01c0\u01c1\7>\2\2\u01c1")
        buf.write("\u01c2\7?\2\2\u01c2p\3\2\2\2\u01c3\u01c4\7?\2\2\u01c4")
        buf.write("\u01c5\7?\2\2\u01c5\u01c6\7\60\2\2\u01c6r\3\2\2\2\u01c7")
        buf.write("\u01c8\7-\2\2\u01c8\u01c9\7\60\2\2\u01c9t\3\2\2\2\u01ca")
        buf.write("\u01cb\7*\2\2\u01cbv\3\2\2\2\u01cc\u01cd\7+\2\2\u01cd")
        buf.write("x\3\2\2\2\u01ce\u01cf\7]\2\2\u01cfz\3\2\2\2\u01d0\u01d1")
        buf.write("\7_\2\2\u01d1|\3\2\2\2\u01d2\u01d3\7}\2\2\u01d3~\3\2\2")
        buf.write("\2\u01d4\u01d5\7\177\2\2\u01d5\u0080\3\2\2\2\u01d6\u01d7")
        buf.write("\7.\2\2\u01d7\u0082\3\2\2\2\u01d8\u01d9\7<\2\2\u01d9\u0084")
        buf.write("\3\2\2\2\u01da\u01db\7=\2\2\u01db\u0086\3\2\2\2\u01dc")
        buf.write("\u01dd\7%\2\2\u01dd\u01de\7%\2\2\u01de\u01e2\3\2\2\2\u01df")
        buf.write("\u01e1\13\2\2\2\u01e0\u01df\3\2\2\2\u01e1\u01e4\3\2\2")
        buf.write("\2\u01e2\u01e3\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e5")
        buf.write("\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e5\u01e6\7%\2\2\u01e6")
        buf.write("\u01e7\7%\2\2\u01e7\u01e8\3\2\2\2\u01e8\u01e9\bD\4\2\u01e9")
        buf.write("\u0088\3\2\2\2\u01ea\u01ec\t\t\2\2\u01eb\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ed\u01ee\3")
        buf.write("\2\2\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\bE\4\2\u01f0\u008a")
        buf.write("\3\2\2\2\u01f1\u01f5\7$\2\2\u01f2\u01f4\5\u008fH\2\u01f3")
        buf.write("\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3")
        buf.write("\2\2\2\u01f8\u01f9\bF\5\2\u01f9\u008c\3\2\2\2\u01fa\u01fe")
        buf.write("\7$\2\2\u01fb\u01fd\5\u008fH\2\u01fc\u01fb\3\2\2\2\u01fd")
        buf.write("\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2")
        buf.write("\u01ff\u0201\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0202\5")
        buf.write("\u0093J\2\u0202\u0203\bG\6\2\u0203\u008e\3\2\2\2\u0204")
        buf.write("\u0207\n\n\2\2\u0205\u0207\5\u0091I\2\u0206\u0204\3\2")
        buf.write("\2\2\u0206\u0205\3\2\2\2\u0207\u0090\3\2\2\2\u0208\u0209")
        buf.write("\7^\2\2\u0209\u020a\t\13\2\2\u020a\u0092\3\2\2\2\u020b")
        buf.write("\u020c\7^\2\2\u020c\u020f\n\13\2\2\u020d\u020f\n\f\2\2")
        buf.write("\u020e\u020b\3\2\2\2\u020e\u020d\3\2\2\2\u020f\u0094\3")
        buf.write("\2\2\2\u0210\u0211\13\2\2\2\u0211\u0212\bK\7\2\u0212\u0096")
        buf.write("\3\2\2\2\u0213\u0215\t\b\2\2\u0214\u0213\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216\u0214\3\2\2\2\u0216\u0217\3\2\2\2")
        buf.write("\u0217\u0098\3\2\2\2\u0218\u0219\t\r\2\2\u0219\u009a\3")
        buf.write("\2\2\2\u021a\u021b\t\16\2\2\u021b\u009c\3\2\2\2\u021c")
        buf.write("\u021d\t\17\2\2\u021d\u009e\3\2\2\2\36\2\u00a3\u00ad\u00b2")
        buf.write("\u00ba\u00bf\u00c3\u00c5\u00cd\u00d3\u00da\u00df\u00e3")
        buf.write("\u00e6\u00ec\u00f1\u00f6\u00fa\u0100\u0106\u0109\u01e2")
        buf.write("\u01ed\u01f5\u01fe\u0206\u020e\u0216\b\3\2\2\3\5\3\b\2")
        buf.write("\2\3F\4\3G\5\3K\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    STRINGLIT = 1
    TYPE = 2
    CONDITION = 3
    INTLIT = 4
    FLOATLIT = 5
    BOOLLIT = 6
    IDENTIFIERS = 7
    BREAK = 8
    CONTINUE = 9
    IF = 10
    ELSEIF = 11
    ELSE = 12
    FOREACH = 13
    TRUE = 14
    FALSE = 15
    ARRAY = 16
    IN = 17
    INT = 18
    FLOAT = 19
    BOOLEAN = 20
    STRING = 21
    RETURN = 22
    NULL = 23
    CLASS = 24
    VAL = 25
    VAR = 26
    CONSTRUCTOR = 27
    DESTRUCTOR = 28
    NEW = 29
    BY = 30
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
    COMMA = 57
    COLON = 58
    SEMICOLON = 59
    BLOCK_COMMENT = 60
    WS = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    ERROR_CHAR = 64
    ID = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'::'", 
            "'.'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>'", "'<'", "'>='", "'<='", 
            "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "','", 
            "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "STRINGLIT", "TYPE", "CONDITION", "INTLIT", "FLOATLIT", "BOOLLIT", 
            "IDENTIFIERS", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", 
            "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
            "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
            "DESTRUCTOR", "NEW", "BY", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
            "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
            "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GT", "LT", 
            "GTE", "LTE", "STREQUALOP", "STRCONCATOP", "LB", "RB", "LSB", 
            "RSB", "LCB", "RCB", "COMMA", "COLON", "SEMICOLON", "BLOCK_COMMENT", 
            "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ERROR_CHAR", "ID" ]

    ruleNames = [ "STRINGLIT", "TYPE", "CONDITION", "INTLIT", "DEC", "HEX", 
                  "OCT", "BIN", "FLOATLIT", "DECIMALPART", "EXPONENTPART", 
                  "BOOLLIT", "IDENTIFIERS", "DOLLAR", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUAL", "GT", 
                  "LT", "GTE", "LTE", "STREQUALOP", "STRCONCATOP", "LB", 
                  "RB", "LSB", "RSB", "LCB", "RCB", "COMMA", "COLON", "SEMICOLON", 
                  "BLOCK_COMMENT", "WS", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", "ERROR_CHAR", 
                  "ID", "B", "E", "X" ]

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
            actions[0] = self.STRINGLIT_action 
            actions[3] = self.INTLIT_action 
            actions[68] = self.UNCLOSE_STRING_action 
            actions[69] = self.ILLEGAL_ESCAPE_action 
            actions[73] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	self.text = str(self.text)[1:-1].replace('\"','')

     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
             
            	self.text = self.text.replace("_", "")
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            	current = str(self.text)
            	raise UncloseString(y[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
             raise ErrorToken(self.text) 
     


