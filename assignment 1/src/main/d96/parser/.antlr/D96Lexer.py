# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2F")
        buf.write("\u029a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00ce\n\b\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35")
        buf.write("\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#\3#\3$\3$\3")
        buf.write("$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3")
        buf.write("*\3+\3+\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3\60\3\60\3\61")
        buf.write("\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\39\39\39\39\39\39\3:\3:\3:\3:\3")
        buf.write(":\3;\3;\7;\u0190\n;\f;\16;\u0193\13;\3<\3<\6<\u0197\n")
        buf.write("<\r<\16<\u0198\3=\3=\3>\3>\7>\u019f\n>\f>\16>\u01a2\13")
        buf.write(">\3>\3>\3>\3?\3?\7?\u01a9\n?\f?\16?\u01ac\13?\3@\3@\3")
        buf.write("@\5@\u01b1\n@\3@\7@\u01b4\n@\f@\16@\u01b7\13@\3@\3@\7")
        buf.write("@\u01bb\n@\f@\16@\u01be\13@\3@\6@\u01c1\n@\r@\16@\u01c2")
        buf.write("\5@\u01c5\n@\3A\3A\5A\u01c9\nA\3A\3A\3A\3A\3A\3A\3A\5")
        buf.write("A\u01d2\nA\3A\3A\3A\3A\3A\3A\5A\u01da\nA\3A\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\5A\u01e5\nA\3A\3A\3B\3B\3B\3B\3B\7B\u01ee")
        buf.write("\nB\fB\16B\u01f1\13B\3C\3C\3C\6C\u01f6\nC\rC\16C\u01f7")
        buf.write("\3C\3C\6C\u01fc\nC\rC\16C\u01fd\7C\u0200\nC\fC\16C\u0203")
        buf.write("\13C\3C\7C\u0206\nC\fC\16C\u0209\13C\5C\u020b\nC\3C\5")
        buf.write("C\u020e\nC\3D\3D\6D\u0212\nD\rD\16D\u0213\3D\3D\6D\u0218")
        buf.write("\nD\rD\16D\u0219\7D\u021c\nD\fD\16D\u021f\13D\3D\7D\u0222")
        buf.write("\nD\fD\16D\u0225\13D\5D\u0227\nD\3D\5D\u022a\nD\3E\3E")
        buf.write("\3E\6E\u022f\nE\rE\16E\u0230\3E\3E\6E\u0235\nE\rE\16E")
        buf.write("\u0236\7E\u0239\nE\fE\16E\u023c\13E\3E\7E\u023f\nE\fE")
        buf.write("\16E\u0242\13E\5E\u0244\nE\3E\5E\u0247\nE\3F\3F\3F\3F")
        buf.write("\5F\u024d\nF\3F\3F\3F\5F\u0252\nF\3G\3G\3G\3G\5G\u0258")
        buf.write("\nG\3G\3G\3H\3H\7H\u025e\nH\fH\16H\u0261\13H\3H\3H\3I")
        buf.write("\3I\7I\u0267\nI\fI\16I\u026a\13I\3I\3I\3I\3J\3J\3J\3J")
        buf.write("\5J\u0273\nJ\3K\3K\3K\3L\3L\3L\5L\u027b\nL\3M\3M\3M\3")
        buf.write("M\7M\u0281\nM\fM\16M\u0284\13M\3M\3M\3M\3M\3M\3N\6N\u028c")
        buf.write("\nN\rN\16N\u028d\3N\3N\3O\3O\3O\3P\3P\3Q\3Q\3R\3R\3\u0282")
        buf.write("\2S\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u<w=y\2{>}\2\177\2\u0081?\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\u008b@\u008dA\u008fB\u0091C\u0093\2\u0095\2\u0097\2")
        buf.write("\u0099D\u009bE\u009dF\u009f\2\u00a1\2\u00a3\2\3\2\21\5")
        buf.write("\2C\\aac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\5\2\63;CHch\5")
        buf.write("\2\62;CHch\3\2\639\3\2\629\3\2\62\63\4\2$$^^\t\2))^^d")
        buf.write("dhhppttvv\5\2\n\f\16\17\"\"\4\2DDdd\4\2GGgg\4\2ZZzz\2")
        buf.write("\u02bf\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33")
        buf.write("\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2")
        buf.write("\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2{\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2")
        buf.write("\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\3\u00a5\3\2\2\2\5\u00ab\3\2\2")
        buf.write("\2\7\u00b4\3\2\2\2\t\u00b7\3\2\2\2\13\u00be\3\2\2\2\r")
        buf.write("\u00c3\3\2\2\2\17\u00cd\3\2\2\2\21\u00cf\3\2\2\2\23\u00d4")
        buf.write("\3\2\2\2\25\u00da\3\2\2\2\27\u00e0\3\2\2\2\31\u00e3\3")
        buf.write("\2\2\2\33\u00e7\3\2\2\2\35\u00ed\3\2\2\2\37\u00f5\3\2")
        buf.write("\2\2!\u00fc\3\2\2\2#\u0103\3\2\2\2%\u0108\3\2\2\2\'\u010e")
        buf.write("\3\2\2\2)\u0112\3\2\2\2+\u0116\3\2\2\2-\u0122\3\2\2\2")
        buf.write("/\u012d\3\2\2\2\61\u0131\3\2\2\2\63\u0134\3\2\2\2\65\u0139")
        buf.write("\3\2\2\2\67\u013c\3\2\2\29\u013f\3\2\2\2;\u0141\3\2\2")
        buf.write("\2=\u0143\3\2\2\2?\u0145\3\2\2\2A\u0147\3\2\2\2C\u0149")
        buf.write("\3\2\2\2E\u014b\3\2\2\2G\u014d\3\2\2\2I\u0150\3\2\2\2")
        buf.write("K\u0153\3\2\2\2M\u0156\3\2\2\2O\u0158\3\2\2\2Q\u015b\3")
        buf.write("\2\2\2S\u015e\3\2\2\2U\u0161\3\2\2\2W\u0163\3\2\2\2Y\u0165")
        buf.write("\3\2\2\2[\u0169\3\2\2\2]\u016c\3\2\2\2_\u016e\3\2\2\2")
        buf.write("a\u0170\3\2\2\2c\u0172\3\2\2\2e\u0174\3\2\2\2g\u0176\3")
        buf.write("\2\2\2i\u0178\3\2\2\2k\u017a\3\2\2\2m\u017c\3\2\2\2o\u017e")
        buf.write("\3\2\2\2q\u0180\3\2\2\2s\u0188\3\2\2\2u\u018d\3\2\2\2")
        buf.write("w\u0194\3\2\2\2y\u019a\3\2\2\2{\u019c\3\2\2\2}\u01a6\3")
        buf.write("\2\2\2\177\u01ad\3\2\2\2\u0081\u01e4\3\2\2\2\u0083\u01e8")
        buf.write("\3\2\2\2\u0085\u01f2\3\2\2\2\u0087\u020f\3\2\2\2\u0089")
        buf.write("\u022b\3\2\2\2\u008b\u0251\3\2\2\2\u008d\u0257\3\2\2\2")
        buf.write("\u008f\u025b\3\2\2\2\u0091\u0264\3\2\2\2\u0093\u0272\3")
        buf.write("\2\2\2\u0095\u0274\3\2\2\2\u0097\u027a\3\2\2\2\u0099\u027c")
        buf.write("\3\2\2\2\u009b\u028b\3\2\2\2\u009d\u0291\3\2\2\2\u009f")
        buf.write("\u0294\3\2\2\2\u00a1\u0296\3\2\2\2\u00a3\u0298\3\2\2\2")
        buf.write("\u00a5\u00a6\7D\2\2\u00a6\u00a7\7t\2\2\u00a7\u00a8\7g")
        buf.write("\2\2\u00a8\u00a9\7c\2\2\u00a9\u00aa\7m\2\2\u00aa\4\3\2")
        buf.write("\2\2\u00ab\u00ac\7E\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae")
        buf.write("\7p\2\2\u00ae\u00af\7v\2\2\u00af\u00b0\7k\2\2\u00b0\u00b1")
        buf.write("\7p\2\2\u00b1\u00b2\7w\2\2\u00b2\u00b3\7g\2\2\u00b3\6")
        buf.write("\3\2\2\2\u00b4\u00b5\7K\2\2\u00b5\u00b6\7h\2\2\u00b6\b")
        buf.write("\3\2\2\2\u00b7\u00b8\7G\2\2\u00b8\u00b9\7n\2\2\u00b9\u00ba")
        buf.write("\7u\2\2\u00ba\u00bb\7g\2\2\u00bb\u00bc\7k\2\2\u00bc\u00bd")
        buf.write("\7h\2\2\u00bd\n\3\2\2\2\u00be\u00bf\7G\2\2\u00bf\u00c0")
        buf.write("\7n\2\2\u00c0\u00c1\7u\2\2\u00c1\u00c2\7g\2\2\u00c2\f")
        buf.write("\3\2\2\2\u00c3\u00c4\7H\2\2\u00c4\u00c5\7q\2\2\u00c5\u00c6")
        buf.write("\7t\2\2\u00c6\u00c7\7g\2\2\u00c7\u00c8\7c\2\2\u00c8\u00c9")
        buf.write("\7e\2\2\u00c9\u00ca\7j\2\2\u00ca\16\3\2\2\2\u00cb\u00ce")
        buf.write("\5\21\t\2\u00cc\u00ce\5\23\n\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\20\3\2\2\2\u00cf\u00d0\7V\2\2\u00d0")
        buf.write("\u00d1\7t\2\2\u00d1\u00d2\7w\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\22\3\2\2\2\u00d4\u00d5\7H\2\2\u00d5\u00d6\7c\2\2\u00d6")
        buf.write("\u00d7\7n\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9\7g\2\2\u00d9")
        buf.write("\24\3\2\2\2\u00da\u00db\7C\2\2\u00db\u00dc\7t\2\2\u00dc")
        buf.write("\u00dd\7t\2\2\u00dd\u00de\7c\2\2\u00de\u00df\7{\2\2\u00df")
        buf.write("\26\3\2\2\2\u00e0\u00e1\7K\2\2\u00e1\u00e2\7p\2\2\u00e2")
        buf.write("\30\3\2\2\2\u00e3\u00e4\7K\2\2\u00e4\u00e5\7p\2\2\u00e5")
        buf.write("\u00e6\7v\2\2\u00e6\32\3\2\2\2\u00e7\u00e8\7H\2\2\u00e8")
        buf.write("\u00e9\7n\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb\7c\2\2\u00eb")
        buf.write("\u00ec\7v\2\2\u00ec\34\3\2\2\2\u00ed\u00ee\7D\2\2\u00ee")
        buf.write("\u00ef\7q\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1\7n\2\2\u00f1")
        buf.write("\u00f2\7g\2\2\u00f2\u00f3\7c\2\2\u00f3\u00f4\7p\2\2\u00f4")
        buf.write("\36\3\2\2\2\u00f5\u00f6\7U\2\2\u00f6\u00f7\7v\2\2\u00f7")
        buf.write("\u00f8\7t\2\2\u00f8\u00f9\7k\2\2\u00f9\u00fa\7p\2\2\u00fa")
        buf.write("\u00fb\7i\2\2\u00fb \3\2\2\2\u00fc\u00fd\7T\2\2\u00fd")
        buf.write("\u00fe\7g\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7w\2\2\u0100")
        buf.write("\u0101\7t\2\2\u0101\u0102\7p\2\2\u0102\"\3\2\2\2\u0103")
        buf.write("\u0104\7P\2\2\u0104\u0105\7w\2\2\u0105\u0106\7n\2\2\u0106")
        buf.write("\u0107\7n\2\2\u0107$\3\2\2\2\u0108\u0109\7E\2\2\u0109")
        buf.write("\u010a\7n\2\2\u010a\u010b\7c\2\2\u010b\u010c\7u\2\2\u010c")
        buf.write("\u010d\7u\2\2\u010d&\3\2\2\2\u010e\u010f\7X\2\2\u010f")
        buf.write("\u0110\7c\2\2\u0110\u0111\7n\2\2\u0111(\3\2\2\2\u0112")
        buf.write("\u0113\7X\2\2\u0113\u0114\7c\2\2\u0114\u0115\7t\2\2\u0115")
        buf.write("*\3\2\2\2\u0116\u0117\7E\2\2\u0117\u0118\7q\2\2\u0118")
        buf.write("\u0119\7p\2\2\u0119\u011a\7u\2\2\u011a\u011b\7v\2\2\u011b")
        buf.write("\u011c\7t\2\2\u011c\u011d\7w\2\2\u011d\u011e\7e\2\2\u011e")
        buf.write("\u011f\7v\2\2\u011f\u0120\7q\2\2\u0120\u0121\7t\2\2\u0121")
        buf.write(",\3\2\2\2\u0122\u0123\7F\2\2\u0123\u0124\7g\2\2\u0124")
        buf.write("\u0125\7u\2\2\u0125\u0126\7v\2\2\u0126\u0127\7t\2\2\u0127")
        buf.write("\u0128\7w\2\2\u0128\u0129\7e\2\2\u0129\u012a\7v\2\2\u012a")
        buf.write("\u012b\7q\2\2\u012b\u012c\7t\2\2\u012c.\3\2\2\2\u012d")
        buf.write("\u012e\7P\2\2\u012e\u012f\7g\2\2\u012f\u0130\7y\2\2\u0130")
        buf.write("\60\3\2\2\2\u0131\u0132\7D\2\2\u0132\u0133\7{\2\2\u0133")
        buf.write("\62\3\2\2\2\u0134\u0135\7U\2\2\u0135\u0136\7g\2\2\u0136")
        buf.write("\u0137\7n\2\2\u0137\u0138\7h\2\2\u0138\64\3\2\2\2\u0139")
        buf.write("\u013a\7<\2\2\u013a\u013b\7<\2\2\u013b\66\3\2\2\2\u013c")
        buf.write("\u013d\7\60\2\2\u013d\u013e\7\60\2\2\u013e8\3\2\2\2\u013f")
        buf.write("\u0140\7a\2\2\u0140:\3\2\2\2\u0141\u0142\7-\2\2\u0142")
        buf.write("<\3\2\2\2\u0143\u0144\7/\2\2\u0144>\3\2\2\2\u0145\u0146")
        buf.write("\7,\2\2\u0146@\3\2\2\2\u0147\u0148\7\61\2\2\u0148B\3\2")
        buf.write("\2\2\u0149\u014a\7\'\2\2\u014aD\3\2\2\2\u014b\u014c\7")
        buf.write("#\2\2\u014cF\3\2\2\2\u014d\u014e\7(\2\2\u014e\u014f\7")
        buf.write("(\2\2\u014fH\3\2\2\2\u0150\u0151\7~\2\2\u0151\u0152\7")
        buf.write("~\2\2\u0152J\3\2\2\2\u0153\u0154\7?\2\2\u0154\u0155\7")
        buf.write("?\2\2\u0155L\3\2\2\2\u0156\u0157\7?\2\2\u0157N\3\2\2\2")
        buf.write("\u0158\u0159\7#\2\2\u0159\u015a\7?\2\2\u015aP\3\2\2\2")
        buf.write("\u015b\u015c\7@\2\2\u015c\u015d\7?\2\2\u015dR\3\2\2\2")
        buf.write("\u015e\u015f\7>\2\2\u015f\u0160\7?\2\2\u0160T\3\2\2\2")
        buf.write("\u0161\u0162\7@\2\2\u0162V\3\2\2\2\u0163\u0164\7>\2\2")
        buf.write("\u0164X\3\2\2\2\u0165\u0166\7?\2\2\u0166\u0167\7?\2\2")
        buf.write("\u0167\u0168\7\60\2\2\u0168Z\3\2\2\2\u0169\u016a\7-\2")
        buf.write("\2\u016a\u016b\7\60\2\2\u016b\\\3\2\2\2\u016c\u016d\7")
        buf.write("*\2\2\u016d^\3\2\2\2\u016e\u016f\7+\2\2\u016f`\3\2\2\2")
        buf.write("\u0170\u0171\7]\2\2\u0171b\3\2\2\2\u0172\u0173\7_\2\2")
        buf.write("\u0173d\3\2\2\2\u0174\u0175\7}\2\2\u0175f\3\2\2\2\u0176")
        buf.write("\u0177\7\177\2\2\u0177h\3\2\2\2\u0178\u0179\7\60\2\2\u0179")
        buf.write("j\3\2\2\2\u017a\u017b\7.\2\2\u017bl\3\2\2\2\u017c\u017d")
        buf.write("\7<\2\2\u017dn\3\2\2\2\u017e\u017f\7=\2\2\u017fp\3\2\2")
        buf.write("\2\u0180\u0181\7R\2\2\u0181\u0182\7t\2\2\u0182\u0183\7")
        buf.write("q\2\2\u0183\u0184\7i\2\2\u0184\u0185\7t\2\2\u0185\u0186")
        buf.write("\7c\2\2\u0186\u0187\7o\2\2\u0187r\3\2\2\2\u0188\u0189")
        buf.write("\7o\2\2\u0189\u018a\7c\2\2\u018a\u018b\7k\2\2\u018b\u018c")
        buf.write("\7p\2\2\u018ct\3\2\2\2\u018d\u0191\t\2\2\2\u018e\u0190")
        buf.write("\t\3\2\2\u018f\u018e\3\2\2\2\u0190\u0193\3\2\2\2\u0191")
        buf.write("\u018f\3\2\2\2\u0191\u0192\3\2\2\2\u0192v\3\2\2\2\u0193")
        buf.write("\u0191\3\2\2\2\u0194\u0196\5y=\2\u0195\u0197\t\3\2\2\u0196")
        buf.write("\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198\u0196\3\2\2\2")
        buf.write("\u0198\u0199\3\2\2\2\u0199x\3\2\2\2\u019a\u019b\7&\2\2")
        buf.write("\u019bz\3\2\2\2\u019c\u01a0\7$\2\2\u019d\u019f\5\u0093")
        buf.write("J\2\u019e\u019d\3\2\2\2\u019f\u01a2\3\2\2\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a3\3\2\2\2\u01a2")
        buf.write("\u01a0\3\2\2\2\u01a3\u01a4\7$\2\2\u01a4\u01a5\b>\2\2\u01a5")
        buf.write("|\3\2\2\2\u01a6\u01aa\7\60\2\2\u01a7\u01a9\t\4\2\2\u01a8")
        buf.write("\u01a7\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01ab\3\2\2\2\u01ab~\3\2\2\2\u01ac\u01aa\3\2\2")
        buf.write("\2\u01ad\u01b0\5\u00a1Q\2\u01ae\u01b1\5=\37\2\u01af\u01b1")
        buf.write("\5;\36\2\u01b0\u01ae\3\2\2\2\u01b0\u01af\3\2\2\2\u01b0")
        buf.write("\u01b1\3\2\2\2\u01b1\u01c4\3\2\2\2\u01b2\u01b4\7\62\2")
        buf.write("\2\u01b3\u01b2\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3")
        buf.write("\3\2\2\2\u01b5\u01b6\3\2\2\2\u01b6\u01b8\3\2\2\2\u01b7")
        buf.write("\u01b5\3\2\2\2\u01b8\u01bc\t\5\2\2\u01b9\u01bb\t\4\2\2")
        buf.write("\u01ba\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01c5\3\2\2\2\u01be\u01bc")
        buf.write("\3\2\2\2\u01bf\u01c1\7\62\2\2\u01c0\u01bf\3\2\2\2\u01c1")
        buf.write("\u01c2\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2")
        buf.write("\u01c3\u01c5\3\2\2\2\u01c4\u01b5\3\2\2\2\u01c4\u01c0\3")
        buf.write("\2\2\2\u01c5\u0080\3\2\2\2\u01c6\u01c9\5\u0083B\2\u01c7")
        buf.write("\u01c9\7\62\2\2\u01c8\u01c6\3\2\2\2\u01c8\u01c7\3\2\2")
        buf.write("\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb\5}?\2\u01cb\u01cc\5")
        buf.write("\177@\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\bA\3\2\u01ce\u01e5")
        buf.write("\3\2\2\2\u01cf\u01d2\5\u0083B\2\u01d0\u01d2\7\62\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2")
        buf.write("\u01d3\u01d4\5}?\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\bA")
        buf.write("\4\2\u01d6\u01e5\3\2\2\2\u01d7\u01da\5\u0083B\2\u01d8")
        buf.write("\u01da\7\62\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8\3\2\2")
        buf.write("\2\u01da\u01db\3\2\2\2\u01db\u01dc\5\177@\2\u01dc\u01dd")
        buf.write("\3\2\2\2\u01dd\u01de\bA\5\2\u01de\u01e5\3\2\2\2\u01df")
        buf.write("\u01e0\5}?\2\u01e0\u01e1\5\177@\2\u01e1\u01e2\3\2\2\2")
        buf.write("\u01e2\u01e3\bA\6\2\u01e3\u01e5\3\2\2\2\u01e4\u01c8\3")
        buf.write("\2\2\2\u01e4\u01d1\3\2\2\2\u01e4\u01d9\3\2\2\2\u01e4\u01df")
        buf.write("\3\2\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\bA\7\2\u01e7")
        buf.write("\u0082\3\2\2\2\u01e8\u01ef\t\5\2\2\u01e9\u01ea\59\35\2")
        buf.write("\u01ea\u01eb\t\4\2\2\u01eb\u01ee\3\2\2\2\u01ec\u01ee\t")
        buf.write("\4\2\2\u01ed\u01e9\3\2\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01f1")
        buf.write("\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0")
        buf.write("\u0084\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f3\7\62\2")
        buf.write("\2\u01f3\u020d\5\u00a3R\2\u01f4\u01f6\t\6\2\2\u01f5\u01f4")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7")
        buf.write("\u01f8\3\2\2\2\u01f8\u020a\3\2\2\2\u01f9\u01fb\59\35\2")
        buf.write("\u01fa\u01fc\t\7\2\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3")
        buf.write("\2\2\2\u01fd\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200")
        buf.write("\3\2\2\2\u01ff\u01f9\3\2\2\2\u0200\u0203\3\2\2\2\u0201")
        buf.write("\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u020b\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0204\u0206\t\7\2\2\u0205\u0204\3")
        buf.write("\2\2\2\u0206\u0209\3\2\2\2\u0207\u0205\3\2\2\2\u0207\u0208")
        buf.write("\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2\u020a")
        buf.write("\u0201\3\2\2\2\u020a\u0207\3\2\2\2\u020b\u020e\3\2\2\2")
        buf.write("\u020c\u020e\7\62\2\2\u020d\u01f5\3\2\2\2\u020d\u020c")
        buf.write("\3\2\2\2\u020e\u0086\3\2\2\2\u020f\u0229\7\62\2\2\u0210")
        buf.write("\u0212\t\b\2\2\u0211\u0210\3\2\2\2\u0212\u0213\3\2\2\2")
        buf.write("\u0213\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0226\3")
        buf.write("\2\2\2\u0215\u0217\59\35\2\u0216\u0218\t\t\2\2\u0217\u0216")
        buf.write("\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u0217\3\2\2\2\u0219")
        buf.write("\u021a\3\2\2\2\u021a\u021c\3\2\2\2\u021b\u0215\3\2\2\2")
        buf.write("\u021c\u021f\3\2\2\2\u021d\u021b\3\2\2\2\u021d\u021e\3")
        buf.write("\2\2\2\u021e\u0227\3\2\2\2\u021f\u021d\3\2\2\2\u0220\u0222")
        buf.write("\t\t\2\2\u0221\u0220\3\2\2\2\u0222\u0225\3\2\2\2\u0223")
        buf.write("\u0221\3\2\2\2\u0223\u0224\3\2\2\2\u0224\u0227\3\2\2\2")
        buf.write("\u0225\u0223\3\2\2\2\u0226\u021d\3\2\2\2\u0226\u0223\3")
        buf.write("\2\2\2\u0227\u022a\3\2\2\2\u0228\u022a\7\62\2\2\u0229")
        buf.write("\u0211\3\2\2\2\u0229\u0228\3\2\2\2\u022a\u0088\3\2\2\2")
        buf.write("\u022b\u022c\7\62\2\2\u022c\u0246\5\u009fP\2\u022d\u022f")
        buf.write("\7\63\2\2\u022e\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230")
        buf.write("\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u0243\3\2\2\2")
        buf.write("\u0232\u0234\59\35\2\u0233\u0235\t\n\2\2\u0234\u0233\3")
        buf.write("\2\2\2\u0235\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236\u0237")
        buf.write("\3\2\2\2\u0237\u0239\3\2\2\2\u0238\u0232\3\2\2\2\u0239")
        buf.write("\u023c\3\2\2\2\u023a\u0238\3\2\2\2\u023a\u023b\3\2\2\2")
        buf.write("\u023b\u0244\3\2\2\2\u023c\u023a\3\2\2\2\u023d\u023f\t")
        buf.write("\n\2\2\u023e\u023d\3\2\2\2\u023f\u0242\3\2\2\2\u0240\u023e")
        buf.write("\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0244\3\2\2\2\u0242")
        buf.write("\u0240\3\2\2\2\u0243\u023a\3\2\2\2\u0243\u0240\3\2\2\2")
        buf.write("\u0244\u0247\3\2\2\2\u0245\u0247\7\62\2\2\u0246\u022e")
        buf.write("\3\2\2\2\u0246\u0245\3\2\2\2\u0247\u008a\3\2\2\2\u0248")
        buf.write("\u024d\5\u0083B\2\u0249\u024d\5\u0085C\2\u024a\u024d\5")
        buf.write("\u0087D\2\u024b\u024d\5\u0089E\2\u024c\u0248\3\2\2\2\u024c")
        buf.write("\u0249\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024b\3\2\2\2")
        buf.write("\u024d\u024e\3\2\2\2\u024e\u024f\bF\b\2\u024f\u0252\3")
        buf.write("\2\2\2\u0250\u0252\7\62\2\2\u0251\u024c\3\2\2\2\u0251")
        buf.write("\u0250\3\2\2\2\u0252\u008c\3\2\2\2\u0253\u0258\5\u0083")
        buf.write("B\2\u0254\u0258\5\u0085C\2\u0255\u0258\5\u0087D\2\u0256")
        buf.write("\u0258\5\u0089E\2\u0257\u0253\3\2\2\2\u0257\u0254\3\2")
        buf.write("\2\2\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\u025a\bG\t\2\u025a\u008e\3\2\2\2\u025b")
        buf.write("\u025f\7$\2\2\u025c\u025e\5\u0093J\2\u025d\u025c\3\2\2")
        buf.write("\2\u025e\u0261\3\2\2\2\u025f\u025d\3\2\2\2\u025f\u0260")
        buf.write("\3\2\2\2\u0260\u0262\3\2\2\2\u0261\u025f\3\2\2\2\u0262")
        buf.write("\u0263\bH\n\2\u0263\u0090\3\2\2\2\u0264\u0268\7$\2\2\u0265")
        buf.write("\u0267\5\u0093J\2\u0266\u0265\3\2\2\2\u0267\u026a\3\2")
        buf.write("\2\2\u0268\u0266\3\2\2\2\u0268\u0269\3\2\2\2\u0269\u026b")
        buf.write("\3\2\2\2\u026a\u0268\3\2\2\2\u026b\u026c\5\u0097L\2\u026c")
        buf.write("\u026d\bI\13\2\u026d\u0092\3\2\2\2\u026e\u026f\7)\2\2")
        buf.write("\u026f\u0273\7$\2\2\u0270\u0273\5\u0095K\2\u0271\u0273")
        buf.write("\n\13\2\2\u0272\u026e\3\2\2\2\u0272\u0270\3\2\2\2\u0272")
        buf.write("\u0271\3\2\2\2\u0273\u0094\3\2\2\2\u0274\u0275\7^\2\2")
        buf.write("\u0275\u0276\t\f\2\2\u0276\u0096\3\2\2\2\u0277\u0278\7")
        buf.write("^\2\2\u0278\u027b\n\f\2\2\u0279\u027b\7^\2\2\u027a\u0277")
        buf.write("\3\2\2\2\u027a\u0279\3\2\2\2\u027b\u0098\3\2\2\2\u027c")
        buf.write("\u027d\7%\2\2\u027d\u027e\7%\2\2\u027e\u0282\3\2\2\2\u027f")
        buf.write("\u0281\13\2\2\2\u0280\u027f\3\2\2\2\u0281\u0284\3\2\2")
        buf.write("\2\u0282\u0283\3\2\2\2\u0282\u0280\3\2\2\2\u0283\u0285")
        buf.write("\3\2\2\2\u0284\u0282\3\2\2\2\u0285\u0286\7%\2\2\u0286")
        buf.write("\u0287\7%\2\2\u0287\u0288\3\2\2\2\u0288\u0289\bM\f\2\u0289")
        buf.write("\u009a\3\2\2\2\u028a\u028c\t\r\2\2\u028b\u028a\3\2\2\2")
        buf.write("\u028c\u028d\3\2\2\2\u028d\u028b\3\2\2\2\u028d\u028e\3")
        buf.write("\2\2\2\u028e\u028f\3\2\2\2\u028f\u0290\bN\f\2\u0290\u009c")
        buf.write("\3\2\2\2\u0291\u0292\13\2\2\2\u0292\u0293\bO\r\2\u0293")
        buf.write("\u009e\3\2\2\2\u0294\u0295\t\16\2\2\u0295\u00a0\3\2\2")
        buf.write("\2\u0296\u0297\t\17\2\2\u0297\u00a2\3\2\2\2\u0298\u0299")
        buf.write("\t\20\2\2\u0299\u00a4\3\2\2\2.\2\u00cd\u0191\u0198\u01a0")
        buf.write("\u01aa\u01b0\u01b5\u01bc\u01c2\u01c4\u01c8\u01d1\u01d9")
        buf.write("\u01e4\u01ed\u01ef\u01f7\u01fd\u0201\u0207\u020a\u020d")
        buf.write("\u0213\u0219\u021d\u0223\u0226\u0229\u0230\u0236\u023a")
        buf.write("\u0240\u0243\u0246\u024c\u0251\u0257\u025f\u0268\u0272")
        buf.write("\u027a\u0282\u028d\16\3>\2\3A\3\3A\4\3A\5\3A\6\3A\7\3")
        buf.write("F\b\3G\t\3H\n\3I\13\b\2\2\3O\f")
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
    INTLIT_IN_ARRAY = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65
    BLOCK_COMMENT = 66
    WS = 67
    ERROR_CHAR = 68

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
            "STRINGLIT", "FLOATLIT", "INTLIT", "INTLIT_IN_ARRAY", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

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
                  "INTLIT", "INTLIT_IN_ARRAY", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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
            actions[60] = self.STRINGLIT_action 
            actions[63] = self.FLOATLIT_action 
            actions[68] = self.INTLIT_action 
            actions[69] = self.INTLIT_IN_ARRAY_action 
            actions[70] = self.UNCLOSE_STRING_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[77] = self.ERROR_CHAR_action 
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
     

    def INTLIT_IN_ARRAY_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            	current = str(self.text)
            	raise UncloseString(current[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
             raise ErrorToken(self.text) 
     


