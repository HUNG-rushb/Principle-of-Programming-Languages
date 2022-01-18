# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u02c7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\n=\f=\16=\u01a1\13=\3=\3=\3=\3>\7>\u01a7\n>\f>\16>\u01aa")
        buf.write("\13>\3>\3>\7>\u01ae\n>\f>\16>\u01b1\13>\3>\7>\u01b4\n")
        buf.write(">\f>\16>\u01b7\13>\3>\7>\u01ba\n>\f>\16>\u01bd\13>\3>")
        buf.write("\5>\u01c0\n>\3>\7>\u01c3\n>\f>\16>\u01c6\13>\3?\7?\u01c9")
        buf.write("\n?\f?\16?\u01cc\13?\3?\3?\7?\u01d0\n?\f?\16?\u01d3\13")
        buf.write("?\3?\3?\5?\u01d7\n?\3?\7?\u01da\n?\f?\16?\u01dd\13?\3")
        buf.write("?\7?\u01e0\n?\f?\16?\u01e3\13?\3?\7?\u01e6\n?\f?\16?\u01e9")
        buf.write("\13?\3?\3?\6?\u01ed\n?\r?\16?\u01ee\5?\u01f1\n?\3?\7?")
        buf.write("\u01f4\n?\f?\16?\u01f7\13?\3@\7@\u01fa\n@\f@\16@\u01fd")
        buf.write("\13@\3@\3@\5@\u0201\n@\3@\7@\u0204\n@\f@\16@\u0207\13")
        buf.write("@\3@\3@\7@\u020b\n@\f@\16@\u020e\13@\3@\3@\3@\7@\u0213")
        buf.write("\n@\f@\16@\u0216\13@\3@\3@\5@\u021a\n@\3@\7@\u021d\n@")
        buf.write("\f@\16@\u0220\13@\3@\3@\7@\u0224\n@\f@\16@\u0227\13@\3")
        buf.write("@\3@\5@\u022b\n@\3@\7@\u022e\n@\f@\16@\u0231\13@\3@\5")
        buf.write("@\u0234\n@\3@\3@\3A\3A\3A\7A\u023b\nA\fA\16A\u023e\13")
        buf.write("A\3B\3B\3B\3B\6B\u0244\nB\rB\16B\u0245\5B\u0248\nB\3B")
        buf.write("\3B\6B\u024c\nB\rB\16B\u024d\7B\u0250\nB\fB\16B\u0253")
        buf.write("\13B\3C\3C\3C\6C\u0258\nC\rC\16C\u0259\5C\u025c\nC\3C")
        buf.write("\3C\6C\u0260\nC\rC\16C\u0261\7C\u0264\nC\fC\16C\u0267")
        buf.write("\13C\3D\3D\3D\3D\6D\u026d\nD\rD\16D\u026e\5D\u0271\nD")
        buf.write("\3D\3D\6D\u0275\nD\rD\16D\u0276\7D\u0279\nD\fD\16D\u027c")
        buf.write("\13D\3E\3E\3E\3E\5E\u0282\nE\3E\3E\3E\5E\u0287\nE\3F\3")
        buf.write("F\7F\u028b\nF\fF\16F\u028e\13F\3F\3F\3G\3G\7G\u0294\n")
        buf.write("G\fG\16G\u0297\13G\3G\3G\3G\3H\3H\3H\3H\5H\u02a0\nH\3")
        buf.write("I\3I\3I\3J\3J\3J\5J\u02a8\nJ\3K\3K\3K\3K\7K\u02ae\nK\f")
        buf.write("K\16K\u02b1\13K\3K\3K\3K\3K\3K\3L\6L\u02b9\nL\rL\16L\u02ba")
        buf.write("\3L\3L\3M\3M\3M\3N\3N\3O\3O\3P\3P\3\u02af\2Q\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63")
        buf.write("\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-")
        buf.write("Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w\2y={\2")
        buf.write("}\2\177>\u0081\2\u0083\2\u0085\2\u0087\2\u0089?\u008b")
        buf.write("@\u008dA\u008f\2\u0091\2\u0093\2\u0095B\u0097C\u0099D")
        buf.write("\u009b\2\u009d\2\u009f\2\3\2\17\6\2\62;C\\aac|\5\2C\\")
        buf.write("aac|\3\2\63;\3\2\62;\5\2\62;CHch\3\2\629\3\2\62\63\4\2")
        buf.write("$$^^\t\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\4\2DDdd\4\2G")
        buf.write("Ggg\4\2ZZzz\2\u02f3\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3")
        buf.write("\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2")
        buf.write("\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3")
        buf.write("\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G")
        buf.write("\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2")
        buf.write("Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2")
        buf.write("\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2")
        buf.write("\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2")
        buf.write("\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2y\3")
        buf.write("\2\2\2\2\177\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2")
        buf.write("\u008d\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099")
        buf.write("\3\2\2\2\3\u00a1\3\2\2\2\5\u00a6\3\2\2\2\7\u00af\3\2\2")
        buf.write("\2\t\u00b5\3\2\2\2\13\u00be\3\2\2\2\r\u00c1\3\2\2\2\17")
        buf.write("\u00c8\3\2\2\2\21\u00cd\3\2\2\2\23\u00d7\3\2\2\2\25\u00d9")
        buf.write("\3\2\2\2\27\u00de\3\2\2\2\31\u00e4\3\2\2\2\33\u00ea\3")
        buf.write("\2\2\2\35\u00ed\3\2\2\2\37\u00f1\3\2\2\2!\u00f7\3\2\2")
        buf.write("\2#\u00ff\3\2\2\2%\u0106\3\2\2\2\'\u010d\3\2\2\2)\u0112")
        buf.write("\3\2\2\2+\u0118\3\2\2\2-\u011c\3\2\2\2/\u0120\3\2\2\2")
        buf.write("\61\u012c\3\2\2\2\63\u0137\3\2\2\2\65\u013b\3\2\2\2\67")
        buf.write("\u013e\3\2\2\29\u0143\3\2\2\2;\u0146\3\2\2\2=\u0149\3")
        buf.write("\2\2\2?\u014b\3\2\2\2A\u014d\3\2\2\2C\u014f\3\2\2\2E\u0151")
        buf.write("\3\2\2\2G\u0153\3\2\2\2I\u0155\3\2\2\2K\u0157\3\2\2\2")
        buf.write("M\u015a\3\2\2\2O\u015d\3\2\2\2Q\u0160\3\2\2\2S\u0162\3")
        buf.write("\2\2\2U\u0165\3\2\2\2W\u0168\3\2\2\2Y\u016b\3\2\2\2[\u016d")
        buf.write("\3\2\2\2]\u016f\3\2\2\2_\u0173\3\2\2\2a\u0176\3\2\2\2")
        buf.write("c\u0178\3\2\2\2e\u017a\3\2\2\2g\u017c\3\2\2\2i\u017e\3")
        buf.write("\2\2\2k\u0180\3\2\2\2m\u0182\3\2\2\2o\u0184\3\2\2\2q\u0186")
        buf.write("\3\2\2\2s\u0188\3\2\2\2u\u0197\3\2\2\2w\u0199\3\2\2\2")
        buf.write("y\u019b\3\2\2\2{\u01a8\3\2\2\2}\u01ca\3\2\2\2\177\u0233")
        buf.write("\3\2\2\2\u0081\u0237\3\2\2\2\u0083\u023f\3\2\2\2\u0085")
        buf.write("\u0254\3\2\2\2\u0087\u0268\3\2\2\2\u0089\u0286\3\2\2\2")
        buf.write("\u008b\u0288\3\2\2\2\u008d\u0291\3\2\2\2\u008f\u029f\3")
        buf.write("\2\2\2\u0091\u02a1\3\2\2\2\u0093\u02a7\3\2\2\2\u0095\u02a9")
        buf.write("\3\2\2\2\u0097\u02b8\3\2\2\2\u0099\u02be\3\2\2\2\u009b")
        buf.write("\u02c1\3\2\2\2\u009d\u02c3\3\2\2\2\u009f\u02c5\3\2\2\2")
        buf.write("\u00a1\u00a2\7c\2\2\u00a2\u00a3\7h\2\2\u00a3\u00a4\7g")
        buf.write("\2\2\u00a4\u00a5\7h\2\2\u00a5\4\3\2\2\2\u00a6\u00a7\7")
        buf.write("u\2\2\u00a7\u00a8\7f\2\2\u00a8\u00a9\7h\2\2\u00a9\u00aa")
        buf.write("\7u\2\2\u00aa\u00ab\7f\2\2\u00ab\u00ac\7h\2\2\u00ac\u00ad")
        buf.write("\7u\2\2\u00ad\u00ae\7c\2\2\u00ae\6\3\2\2\2\u00af\u00b0")
        buf.write("\7D\2\2\u00b0\u00b1\7t\2\2\u00b1\u00b2\7g\2\2\u00b2\u00b3")
        buf.write("\7c\2\2\u00b3\u00b4\7m\2\2\u00b4\b\3\2\2\2\u00b5\u00b6")
        buf.write("\7E\2\2\u00b6\u00b7\7q\2\2\u00b7\u00b8\7p\2\2\u00b8\u00b9")
        buf.write("\7v\2\2\u00b9\u00ba\7k\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc")
        buf.write("\7w\2\2\u00bc\u00bd\7g\2\2\u00bd\n\3\2\2\2\u00be\u00bf")
        buf.write("\7K\2\2\u00bf\u00c0\7h\2\2\u00c0\f\3\2\2\2\u00c1\u00c2")
        buf.write("\7G\2\2\u00c2\u00c3\7n\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5")
        buf.write("\7g\2\2\u00c5\u00c6\7k\2\2\u00c6\u00c7\7h\2\2\u00c7\16")
        buf.write("\3\2\2\2\u00c8\u00c9\7G\2\2\u00c9\u00ca\7n\2\2\u00ca\u00cb")
        buf.write("\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\20\3\2\2\2\u00cd\u00ce")
        buf.write("\7H\2\2\u00ce\u00cf\7q\2\2\u00cf\u00d0\7t\2\2\u00d0\u00d1")
        buf.write("\7g\2\2\u00d1\u00d2\7c\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4")
        buf.write("\7j\2\2\u00d4\22\3\2\2\2\u00d5\u00d8\5\25\13\2\u00d6\u00d8")
        buf.write("\5\27\f\2\u00d7\u00d5\3\2\2\2\u00d7\u00d6\3\2\2\2\u00d8")
        buf.write("\24\3\2\2\2\u00d9\u00da\7V\2\2\u00da\u00db\7t\2\2\u00db")
        buf.write("\u00dc\7w\2\2\u00dc\u00dd\7g\2\2\u00dd\26\3\2\2\2\u00de")
        buf.write("\u00df\7H\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7n\2\2\u00e1")
        buf.write("\u00e2\7u\2\2\u00e2\u00e3\7g\2\2\u00e3\30\3\2\2\2\u00e4")
        buf.write("\u00e5\7C\2\2\u00e5\u00e6\7t\2\2\u00e6\u00e7\7t\2\2\u00e7")
        buf.write("\u00e8\7c\2\2\u00e8\u00e9\7{\2\2\u00e9\32\3\2\2\2\u00ea")
        buf.write("\u00eb\7K\2\2\u00eb\u00ec\7p\2\2\u00ec\34\3\2\2\2\u00ed")
        buf.write("\u00ee\7K\2\2\u00ee\u00ef\7p\2\2\u00ef\u00f0\7v\2\2\u00f0")
        buf.write("\36\3\2\2\2\u00f1\u00f2\7H\2\2\u00f2\u00f3\7n\2\2\u00f3")
        buf.write("\u00f4\7q\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7v\2\2\u00f6")
        buf.write(" \3\2\2\2\u00f7\u00f8\7D\2\2\u00f8\u00f9\7q\2\2\u00f9")
        buf.write("\u00fa\7q\2\2\u00fa\u00fb\7n\2\2\u00fb\u00fc\7g\2\2\u00fc")
        buf.write("\u00fd\7c\2\2\u00fd\u00fe\7p\2\2\u00fe\"\3\2\2\2\u00ff")
        buf.write("\u0100\7U\2\2\u0100\u0101\7v\2\2\u0101\u0102\7t\2\2\u0102")
        buf.write("\u0103\7k\2\2\u0103\u0104\7p\2\2\u0104\u0105\7i\2\2\u0105")
        buf.write("$\3\2\2\2\u0106\u0107\7T\2\2\u0107\u0108\7g\2\2\u0108")
        buf.write("\u0109\7v\2\2\u0109\u010a\7w\2\2\u010a\u010b\7t\2\2\u010b")
        buf.write("\u010c\7p\2\2\u010c&\3\2\2\2\u010d\u010e\7P\2\2\u010e")
        buf.write("\u010f\7w\2\2\u010f\u0110\7n\2\2\u0110\u0111\7n\2\2\u0111")
        buf.write("(\3\2\2\2\u0112\u0113\7E\2\2\u0113\u0114\7n\2\2\u0114")
        buf.write("\u0115\7c\2\2\u0115\u0116\7u\2\2\u0116\u0117\7u\2\2\u0117")
        buf.write("*\3\2\2\2\u0118\u0119\7X\2\2\u0119\u011a\7c\2\2\u011a")
        buf.write("\u011b\7n\2\2\u011b,\3\2\2\2\u011c\u011d\7X\2\2\u011d")
        buf.write("\u011e\7c\2\2\u011e\u011f\7t\2\2\u011f.\3\2\2\2\u0120")
        buf.write("\u0121\7E\2\2\u0121\u0122\7q\2\2\u0122\u0123\7p\2\2\u0123")
        buf.write("\u0124\7u\2\2\u0124\u0125\7v\2\2\u0125\u0126\7t\2\2\u0126")
        buf.write("\u0127\7w\2\2\u0127\u0128\7e\2\2\u0128\u0129\7v\2\2\u0129")
        buf.write("\u012a\7q\2\2\u012a\u012b\7t\2\2\u012b\60\3\2\2\2\u012c")
        buf.write("\u012d\7F\2\2\u012d\u012e\7g\2\2\u012e\u012f\7u\2\2\u012f")
        buf.write("\u0130\7v\2\2\u0130\u0131\7t\2\2\u0131\u0132\7w\2\2\u0132")
        buf.write("\u0133\7e\2\2\u0133\u0134\7v\2\2\u0134\u0135\7q\2\2\u0135")
        buf.write("\u0136\7t\2\2\u0136\62\3\2\2\2\u0137\u0138\7P\2\2\u0138")
        buf.write("\u0139\7g\2\2\u0139\u013a\7y\2\2\u013a\64\3\2\2\2\u013b")
        buf.write("\u013c\7D\2\2\u013c\u013d\7{\2\2\u013d\66\3\2\2\2\u013e")
        buf.write("\u013f\7U\2\2\u013f\u0140\7g\2\2\u0140\u0141\7n\2\2\u0141")
        buf.write("\u0142\7h\2\2\u01428\3\2\2\2\u0143\u0144\7<\2\2\u0144")
        buf.write("\u0145\7<\2\2\u0145:\3\2\2\2\u0146\u0147\7\60\2\2\u0147")
        buf.write("\u0148\7\60\2\2\u0148<\3\2\2\2\u0149\u014a\7a\2\2\u014a")
        buf.write(">\3\2\2\2\u014b\u014c\7-\2\2\u014c@\3\2\2\2\u014d\u014e")
        buf.write("\7/\2\2\u014eB\3\2\2\2\u014f\u0150\7,\2\2\u0150D\3\2\2")
        buf.write("\2\u0151\u0152\7\61\2\2\u0152F\3\2\2\2\u0153\u0154\7\'")
        buf.write("\2\2\u0154H\3\2\2\2\u0155\u0156\7#\2\2\u0156J\3\2\2\2")
        buf.write("\u0157\u0158\7(\2\2\u0158\u0159\7(\2\2\u0159L\3\2\2\2")
        buf.write("\u015a\u015b\7~\2\2\u015b\u015c\7~\2\2\u015cN\3\2\2\2")
        buf.write("\u015d\u015e\7?\2\2\u015e\u015f\7?\2\2\u015fP\3\2\2\2")
        buf.write("\u0160\u0161\7?\2\2\u0161R\3\2\2\2\u0162\u0163\7#\2\2")
        buf.write("\u0163\u0164\7?\2\2\u0164T\3\2\2\2\u0165\u0166\7@\2\2")
        buf.write("\u0166\u0167\7?\2\2\u0167V\3\2\2\2\u0168\u0169\7>\2\2")
        buf.write("\u0169\u016a\7?\2\2\u016aX\3\2\2\2\u016b\u016c\7@\2\2")
        buf.write("\u016cZ\3\2\2\2\u016d\u016e\7>\2\2\u016e\\\3\2\2\2\u016f")
        buf.write("\u0170\7?\2\2\u0170\u0171\7?\2\2\u0171\u0172\7\60\2\2")
        buf.write("\u0172^\3\2\2\2\u0173\u0174\7-\2\2\u0174\u0175\7\60\2")
        buf.write("\2\u0175`\3\2\2\2\u0176\u0177\7*\2\2\u0177b\3\2\2\2\u0178")
        buf.write("\u0179\7+\2\2\u0179d\3\2\2\2\u017a\u017b\7]\2\2\u017b")
        buf.write("f\3\2\2\2\u017c\u017d\7_\2\2\u017dh\3\2\2\2\u017e\u017f")
        buf.write("\7}\2\2\u017fj\3\2\2\2\u0180\u0181\7\177\2\2\u0181l\3")
        buf.write("\2\2\2\u0182\u0183\7\60\2\2\u0183n\3\2\2\2\u0184\u0185")
        buf.write("\7.\2\2\u0185p\3\2\2\2\u0186\u0187\7<\2\2\u0187r\3\2\2")
        buf.write("\2\u0188\u0189\7=\2\2\u0189t\3\2\2\2\u018a\u018c\5w<\2")
        buf.write("\u018b\u018d\t\2\2\2\u018c\u018b\3\2\2\2\u018d\u018e\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0198")
        buf.write("\3\2\2\2\u0190\u0194\t\3\2\2\u0191\u0193\t\2\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0193\u0196\3\2\2\2\u0194\u0192\3\2\2\2")
        buf.write("\u0194\u0195\3\2\2\2\u0195\u0198\3\2\2\2\u0196\u0194\3")
        buf.write("\2\2\2\u0197\u018a\3\2\2\2\u0197\u0190\3\2\2\2\u0198v")
        buf.write("\3\2\2\2\u0199\u019a\7&\2\2\u019ax\3\2\2\2\u019b\u019f")
        buf.write("\7$\2\2\u019c\u019e\5\u008fH\2\u019d\u019c\3\2\2\2\u019e")
        buf.write("\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u01a2\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a3\7")
        buf.write("$\2\2\u01a3\u01a4\b=\2\2\u01a4z\3\2\2\2\u01a5\u01a7\5")
        buf.write("=\37\2\u01a6\u01a5\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6")
        buf.write("\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9\u01ab\3\2\2\2\u01aa")
        buf.write("\u01a8\3\2\2\2\u01ab\u01af\7\60\2\2\u01ac\u01ae\5=\37")
        buf.write("\2\u01ad\u01ac\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af\u01ad")
        buf.write("\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b5\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b2\u01b4\7\62\2\2\u01b3\u01b2\3\2\2")
        buf.write("\2\u01b4\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6")
        buf.write("\3\2\2\2\u01b6\u01bb\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8")
        buf.write("\u01ba\5=\37\2\u01b9\u01b8\3\2\2\2\u01ba\u01bd\3\2\2\2")
        buf.write("\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc\u01bf\3")
        buf.write("\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01c0\5\u0081A\2\u01bf")
        buf.write("\u01be\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c4\3\2\2\2")
        buf.write("\u01c1\u01c3\5=\37\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3")
        buf.write("\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5|")
        buf.write("\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c9\5=\37\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01d1\5\u009dO\2\u01ce\u01d0\5=\37\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d6\3\2\2\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d4\u01d7\5A!\2\u01d5\u01d7\5? \2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d6\u01d7\3\2\2\2\u01d7")
        buf.write("\u01db\3\2\2\2\u01d8\u01da\5=\37\2\u01d9\u01d8\3\2\2\2")
        buf.write("\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc\3")
        buf.write("\2\2\2\u01dc\u01f0\3\2\2\2\u01dd\u01db\3\2\2\2\u01de\u01e0")
        buf.write("\7\62\2\2\u01df\u01de\3\2\2\2\u01e0\u01e3\3\2\2\2\u01e1")
        buf.write("\u01df\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01e7\3\2\2\2")
        buf.write("\u01e3\u01e1\3\2\2\2\u01e4\u01e6\5=\37\2\u01e5\u01e4\3")
        buf.write("\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8")
        buf.write("\3\2\2\2\u01e8\u01ea\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea")
        buf.write("\u01f1\5\u0081A\2\u01eb\u01ed\7\62\2\2\u01ec\u01eb\3\2")
        buf.write("\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef")
        buf.write("\3\2\2\2\u01ef\u01f1\3\2\2\2\u01f0\u01e1\3\2\2\2\u01f0")
        buf.write("\u01ec\3\2\2\2\u01f1\u01f5\3\2\2\2\u01f2\u01f4\5=\37\2")
        buf.write("\u01f3\u01f2\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5\u01f3\3")
        buf.write("\2\2\2\u01f5\u01f6\3\2\2\2\u01f6~\3\2\2\2\u01f7\u01f5")
        buf.write("\3\2\2\2\u01f8\u01fa\5=\37\2\u01f9\u01f8\3\2\2\2\u01fa")
        buf.write("\u01fd\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2")
        buf.write("\u01fc\u0200\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fe\u0201\5")
        buf.write("\u0081A\2\u01ff\u0201\7\62\2\2\u0200\u01fe\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201\u0205\3\2\2\2\u0202\u0204\5=\37\2")
        buf.write("\u0203\u0202\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3")
        buf.write("\2\2\2\u0205\u0206\3\2\2\2\u0206\u0208\3\2\2\2\u0207\u0205")
        buf.write("\3\2\2\2\u0208\u020c\5{>\2\u0209\u020b\5=\37\2\u020a\u0209")
        buf.write("\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020d\u020f\3\2\2\2\u020e\u020c\3\2\2\2")
        buf.write("\u020f\u0210\5}?\2\u0210\u0234\3\2\2\2\u0211\u0213\5=")
        buf.write("\37\2\u0212\u0211\3\2\2\2\u0213\u0216\3\2\2\2\u0214\u0212")
        buf.write("\3\2\2\2\u0214\u0215\3\2\2\2\u0215\u0219\3\2\2\2\u0216")
        buf.write("\u0214\3\2\2\2\u0217\u021a\5\u0081A\2\u0218\u021a\7\62")
        buf.write("\2\2\u0219\u0217\3\2\2\2\u0219\u0218\3\2\2\2\u021a\u021e")
        buf.write("\3\2\2\2\u021b\u021d\5=\37\2\u021c\u021b\3\2\2\2\u021d")
        buf.write("\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e\u021f\3\2\2\2")
        buf.write("\u021f\u0221\3\2\2\2\u0220\u021e\3\2\2\2\u0221\u0234\5")
        buf.write("{>\2\u0222\u0224\5=\37\2\u0223\u0222\3\2\2\2\u0224\u0227")
        buf.write("\3\2\2\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226")
        buf.write("\u022a\3\2\2\2\u0227\u0225\3\2\2\2\u0228\u022b\5\u0081")
        buf.write("A\2\u0229\u022b\7\62\2\2\u022a\u0228\3\2\2\2\u022a\u0229")
        buf.write("\3\2\2\2\u022b\u022f\3\2\2\2\u022c\u022e\5=\37\2\u022d")
        buf.write("\u022c\3\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2")
        buf.write("\u022f\u0230\3\2\2\2\u0230\u0232\3\2\2\2\u0231\u022f\3")
        buf.write("\2\2\2\u0232\u0234\5}?\2\u0233\u01fb\3\2\2\2\u0233\u0214")
        buf.write("\3\2\2\2\u0233\u0225\3\2\2\2\u0234\u0235\3\2\2\2\u0235")
        buf.write("\u0236\b@\3\2\u0236\u0080\3\2\2\2\u0237\u023c\t\4\2\2")
        buf.write("\u0238\u023b\5=\37\2\u0239\u023b\t\5\2\2\u023a\u0238\3")
        buf.write("\2\2\2\u023a\u0239\3\2\2\2\u023b\u023e\3\2\2\2\u023c\u023a")
        buf.write("\3\2\2\2\u023c\u023d\3\2\2\2\u023d\u0082\3\2\2\2\u023e")
        buf.write("\u023c\3\2\2\2\u023f\u0240\7\62\2\2\u0240\u0247\5\u009f")
        buf.write("P\2\u0241\u0248\5=\37\2\u0242\u0244\t\6\2\2\u0243\u0242")
        buf.write("\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0243\3\2\2\2\u0245")
        buf.write("\u0246\3\2\2\2\u0246\u0248\3\2\2\2\u0247\u0241\3\2\2\2")
        buf.write("\u0247\u0243\3\2\2\2\u0248\u0251\3\2\2\2\u0249\u024b\5")
        buf.write("=\37\2\u024a\u024c\t\6\2\2\u024b\u024a\3\2\2\2\u024c\u024d")
        buf.write("\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("\u0250\3\2\2\2\u024f\u0249\3\2\2\2\u0250\u0253\3\2\2\2")
        buf.write("\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0084\3")
        buf.write("\2\2\2\u0253\u0251\3\2\2\2\u0254\u025b\7\62\2\2\u0255")
        buf.write("\u025c\5=\37\2\u0256\u0258\t\7\2\2\u0257\u0256\3\2\2\2")
        buf.write("\u0258\u0259\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u025a\3")
        buf.write("\2\2\2\u025a\u025c\3\2\2\2\u025b\u0255\3\2\2\2\u025b\u0257")
        buf.write("\3\2\2\2\u025c\u0265\3\2\2\2\u025d\u025f\5=\37\2\u025e")
        buf.write("\u0260\t\7\2\2\u025f\u025e\3\2\2\2\u0260\u0261\3\2\2\2")
        buf.write("\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0264\3")
        buf.write("\2\2\2\u0263\u025d\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263")
        buf.write("\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u0086\3\2\2\2\u0267")
        buf.write("\u0265\3\2\2\2\u0268\u0269\7\62\2\2\u0269\u0270\5\u009b")
        buf.write("N\2\u026a\u0271\5=\37\2\u026b\u026d\t\b\2\2\u026c\u026b")
        buf.write("\3\2\2\2\u026d\u026e\3\2\2\2\u026e\u026c\3\2\2\2\u026e")
        buf.write("\u026f\3\2\2\2\u026f\u0271\3\2\2\2\u0270\u026a\3\2\2\2")
        buf.write("\u0270\u026c\3\2\2\2\u0271\u027a\3\2\2\2\u0272\u0274\5")
        buf.write("=\37\2\u0273\u0275\t\b\2\2\u0274\u0273\3\2\2\2\u0275\u0276")
        buf.write("\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2\u0277")
        buf.write("\u0279\3\2\2\2\u0278\u0272\3\2\2\2\u0279\u027c\3\2\2\2")
        buf.write("\u027a\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u0088\3")
        buf.write("\2\2\2\u027c\u027a\3\2\2\2\u027d\u0282\5\u0081A\2\u027e")
        buf.write("\u0282\5\u0083B\2\u027f\u0282\5\u0085C\2\u0280\u0282\5")
        buf.write("\u0087D\2\u0281\u027d\3\2\2\2\u0281\u027e\3\2\2\2\u0281")
        buf.write("\u027f\3\2\2\2\u0281\u0280\3\2\2\2\u0282\u0283\3\2\2\2")
        buf.write("\u0283\u0284\bE\4\2\u0284\u0287\3\2\2\2\u0285\u0287\7")
        buf.write("\62\2\2\u0286\u0281\3\2\2\2\u0286\u0285\3\2\2\2\u0287")
        buf.write("\u008a\3\2\2\2\u0288\u028c\7$\2\2\u0289\u028b\5\u008f")
        buf.write("H\2\u028a\u0289\3\2\2\2\u028b\u028e\3\2\2\2\u028c\u028a")
        buf.write("\3\2\2\2\u028c\u028d\3\2\2\2\u028d\u028f\3\2\2\2\u028e")
        buf.write("\u028c\3\2\2\2\u028f\u0290\bF\5\2\u0290\u008c\3\2\2\2")
        buf.write("\u0291\u0295\7$\2\2\u0292\u0294\5\u008fH\2\u0293\u0292")
        buf.write("\3\2\2\2\u0294\u0297\3\2\2\2\u0295\u0293\3\2\2\2\u0295")
        buf.write("\u0296\3\2\2\2\u0296\u0298\3\2\2\2\u0297\u0295\3\2\2\2")
        buf.write("\u0298\u0299\5\u0093J\2\u0299\u029a\bG\6\2\u029a\u008e")
        buf.write("\3\2\2\2\u029b\u029c\7)\2\2\u029c\u02a0\7$\2\2\u029d\u02a0")
        buf.write("\5\u0091I\2\u029e\u02a0\n\t\2\2\u029f\u029b\3\2\2\2\u029f")
        buf.write("\u029d\3\2\2\2\u029f\u029e\3\2\2\2\u02a0\u0090\3\2\2\2")
        buf.write("\u02a1\u02a2\7^\2\2\u02a2\u02a3\t\n\2\2\u02a3\u0092\3")
        buf.write("\2\2\2\u02a4\u02a5\7^\2\2\u02a5\u02a8\n\n\2\2\u02a6\u02a8")
        buf.write("\7^\2\2\u02a7\u02a4\3\2\2\2\u02a7\u02a6\3\2\2\2\u02a8")
        buf.write("\u0094\3\2\2\2\u02a9\u02aa\7%\2\2\u02aa\u02ab\7%\2\2\u02ab")
        buf.write("\u02af\3\2\2\2\u02ac\u02ae\13\2\2\2\u02ad\u02ac\3\2\2")
        buf.write("\2\u02ae\u02b1\3\2\2\2\u02af\u02b0\3\2\2\2\u02af\u02ad")
        buf.write("\3\2\2\2\u02b0\u02b2\3\2\2\2\u02b1\u02af\3\2\2\2\u02b2")
        buf.write("\u02b3\7%\2\2\u02b3\u02b4\7%\2\2\u02b4\u02b5\3\2\2\2\u02b5")
        buf.write("\u02b6\bK\7\2\u02b6\u0096\3\2\2\2\u02b7\u02b9\t\13\2\2")
        buf.write("\u02b8\u02b7\3\2\2\2\u02b9\u02ba\3\2\2\2\u02ba\u02b8\3")
        buf.write("\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd")
        buf.write("\bL\7\2\u02bd\u0098\3\2\2\2\u02be\u02bf\13\2\2\2\u02bf")
        buf.write("\u02c0\bM\b\2\u02c0\u009a\3\2\2\2\u02c1\u02c2\t\f\2\2")
        buf.write("\u02c2\u009c\3\2\2\2\u02c3\u02c4\t\r\2\2\u02c4\u009e\3")
        buf.write("\2\2\2\u02c5\u02c6\t\16\2\2\u02c6\u00a0\3\2\2\28\2\u00d7")
        buf.write("\u018e\u0194\u0197\u019f\u01a8\u01af\u01b5\u01bb\u01bf")
        buf.write("\u01c4\u01ca\u01d1\u01d6\u01db\u01e1\u01e7\u01ee\u01f0")
        buf.write("\u01f5\u01fb\u0200\u0205\u020c\u0214\u0219\u021e\u0225")
        buf.write("\u022a\u022f\u0233\u023a\u023c\u0245\u0247\u024d\u0251")
        buf.write("\u0259\u025b\u0261\u0265\u026e\u0270\u0276\u027a\u0281")
        buf.write("\u0286\u028c\u0295\u029f\u02a7\u02af\u02ba\t\3=\2\3@\3")
        buf.write("\3E\4\3F\5\3G\6\b\2\2\3M\7")
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
        self.checkVersion("4.9.2")
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
     


