# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u0329\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\3\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3\u00c0\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\5\5\u00ca\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00ef\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00fb\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u010f\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\20\3\20\5\20\u011b\n\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\5\23\u012b")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\5\24\u0132\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u013c\n\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0148")
        buf.write("\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u015c\n")
        buf.write("\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\5\32\u0168\n\32\3\33\3\33\3\33\3\33\3\33\3\33\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\5\36\u017c\n\36\3\36\3\36\3\36\5\36\u0181\n\36\3\37\3")
        buf.write("\37\3\37\3\37\3\37\5\37\u0188\n\37\3 \3 \3 \3 \3 \3 \3")
        buf.write(" \5 \u0191\n \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\5#\u01a1\n#\3#\3#\5#\u01a5\n#\3$\3$\3$\3$\3%\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\5&\u01b5\n&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\5(\u01be\n(\3)\3)\3)\3*\3*\3*\5*\u01c6\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3\60\3\60")
        buf.write("\5\60\u01eb\n\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3")
        buf.write("\63\3\63\3\64\3\64\5\64\u01f8\n\64\3\65\3\65\3\65\3\65")
        buf.write("\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\38\38\38\38\3")
        buf.write("8\58\u020b\n8\39\39\39\39\39\59\u0212\n9\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\5:\u021b\n:\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\5;\u022b\n;\3<\3<\3<\3<\3<\5<\u0232\n<\3=\3=\3")
        buf.write("=\3=\3=\5=\u0239\n=\3>\3>\3>\3>\3>\3>\7>\u0241\n>\f>\16")
        buf.write(">\u0244\13>\3?\3?\3?\3?\3?\3?\7?\u024c\n?\f?\16?\u024f")
        buf.write("\13?\3@\3@\3@\3@\3@\3@\7@\u0257\n@\f@\16@\u025a\13@\3")
        buf.write("A\3A\3A\5A\u025f\nA\3B\3B\3B\5B\u0264\nB\3C\3C\3C\3C\3")
        buf.write("C\7C\u026b\nC\fC\16C\u026e\13C\3D\3D\3D\3D\3D\7D\u0275")
        buf.write("\nD\fD\16D\u0278\13D\3E\3E\3E\5E\u027d\nE\3F\3F\3F\3F")
        buf.write("\3F\3F\3F\5F\u0286\nF\3G\3G\3G\3G\5G\u028c\nG\3H\3H\3")
        buf.write("H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3I\3I\7I\u029c\nI\fI\16I")
        buf.write("\u029f\13I\3J\3J\3J\3J\5J\u02a5\nJ\3K\3K\3K\3K\3K\3K\5")
        buf.write("K\u02ad\nK\3L\3L\3L\3L\5L\u02b3\nL\3M\3M\3M\3M\3M\3M\3")
        buf.write("M\3M\5M\u02bd\nM\3N\3N\3N\3N\5N\u02c3\nN\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\5O\u02cd\nO\3P\3P\3P\3P\3P\3P\5P\u02d5\nP\3")
        buf.write("Q\3Q\3Q\3Q\3Q\3R\3R\3R\3R\3R\3R\5R\u02e2\nR\3S\3S\3S\3")
        buf.write("S\3S\3S\5S\u02ea\nS\3T\3T\3T\3T\3T\3T\5T\u02f2\nT\3U\3")
        buf.write("U\3U\3U\3V\3V\3V\3V\3V\5V\u02fd\nV\3W\3W\3W\3W\3W\5W\u0304")
        buf.write("\nW\3X\3X\5X\u0308\nX\3X\3X\3X\3X\3X\5X\u030f\nX\3X\5")
        buf.write("X\u0312\nX\3Y\3Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\5Z\u0320")
        buf.write("\nZ\3[\3[\3\\\3\\\3\\\5\\\u0327\n\\\3\\\2\bz|~\u0084\u0086")
        buf.write("\u0090]\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write("\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6")
        buf.write("\2\t\3\29:\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2\16")
        buf.write("\21\2\u032e\2\u00b8\3\2\2\2\4\u00bf\3\2\2\2\6\u00c1\3")
        buf.write("\2\2\2\b\u00c9\3\2\2\2\n\u00cb\3\2\2\2\f\u00d1\3\2\2\2")
        buf.write("\16\u00d6\3\2\2\2\20\u00dc\3\2\2\2\22\u00e2\3\2\2\2\24")
        buf.write("\u00ee\3\2\2\2\26\u00fa\3\2\2\2\30\u00fc\3\2\2\2\32\u0102")
        buf.write("\3\2\2\2\34\u010e\3\2\2\2\36\u011a\3\2\2\2 \u011c\3\2")
        buf.write("\2\2\"\u0122\3\2\2\2$\u012a\3\2\2\2&\u0131\3\2\2\2(\u013b")
        buf.write("\3\2\2\2*\u0147\3\2\2\2,\u0149\3\2\2\2.\u014f\3\2\2\2")
        buf.write("\60\u015b\3\2\2\2\62\u0167\3\2\2\2\64\u0169\3\2\2\2\66")
        buf.write("\u016f\3\2\2\28\u0174\3\2\2\2:\u0178\3\2\2\2<\u0187\3")
        buf.write("\2\2\2>\u0189\3\2\2\2@\u0192\3\2\2\2B\u0198\3\2\2\2D\u01a0")
        buf.write("\3\2\2\2F\u01a6\3\2\2\2H\u01aa\3\2\2\2J\u01b4\3\2\2\2")
        buf.write("L\u01b6\3\2\2\2N\u01bd\3\2\2\2P\u01bf\3\2\2\2R\u01c5\3")
        buf.write("\2\2\2T\u01c7\3\2\2\2V\u01d2\3\2\2\2X\u01d6\3\2\2\2Z\u01dd")
        buf.write("\3\2\2\2\\\u01e1\3\2\2\2^\u01ea\3\2\2\2`\u01ec\3\2\2\2")
        buf.write("b\u01ef\3\2\2\2d\u01f2\3\2\2\2f\u01f7\3\2\2\2h\u01f9\3")
        buf.write("\2\2\2j\u01fd\3\2\2\2l\u0201\3\2\2\2n\u020a\3\2\2\2p\u0211")
        buf.write("\3\2\2\2r\u021a\3\2\2\2t\u022a\3\2\2\2v\u0231\3\2\2\2")
        buf.write("x\u0238\3\2\2\2z\u023a\3\2\2\2|\u0245\3\2\2\2~\u0250\3")
        buf.write("\2\2\2\u0080\u025e\3\2\2\2\u0082\u0263\3\2\2\2\u0084\u0265")
        buf.write("\3\2\2\2\u0086\u026f\3\2\2\2\u0088\u027c\3\2\2\2\u008a")
        buf.write("\u0285\3\2\2\2\u008c\u028b\3\2\2\2\u008e\u028d\3\2\2\2")
        buf.write("\u0090\u0291\3\2\2\2\u0092\u02a4\3\2\2\2\u0094\u02ac\3")
        buf.write("\2\2\2\u0096\u02b2\3\2\2\2\u0098\u02bc\3\2\2\2\u009a\u02c2")
        buf.write("\3\2\2\2\u009c\u02cc\3\2\2\2\u009e\u02d4\3\2\2\2\u00a0")
        buf.write("\u02d6\3\2\2\2\u00a2\u02e1\3\2\2\2\u00a4\u02e9\3\2\2\2")
        buf.write("\u00a6\u02f1\3\2\2\2\u00a8\u02f3\3\2\2\2\u00aa\u02fc\3")
        buf.write("\2\2\2\u00ac\u0303\3\2\2\2\u00ae\u0311\3\2\2\2\u00b0\u0313")
        buf.write("\3\2\2\2\u00b2\u031f\3\2\2\2\u00b4\u0321\3\2\2\2\u00b6")
        buf.write("\u0326\3\2\2\2\u00b8\u00b9\5\4\3\2\u00b9\u00ba\7\2\2\3")
        buf.write("\u00ba\3\3\2\2\2\u00bb\u00bc\5\6\4\2\u00bc\u00bd\5\4\3")
        buf.write("\2\u00bd\u00c0\3\2\2\2\u00be\u00c0\5\6\4\2\u00bf\u00bb")
        buf.write("\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0\5\3\2\2\2\u00c1\u00c2")
        buf.write("\7\24\2\2\u00c2\u00c3\79\2\2\u00c3\u00c4\5\b\5\2\u00c4")
        buf.write("\u00c5\5j\66\2\u00c5\7\3\2\2\2\u00c6\u00c7\7\67\2\2\u00c7")
        buf.write("\u00ca\79\2\2\u00c8\u00ca\3\2\2\2\u00c9\u00c6\3\2\2\2")
        buf.write("\u00c9\u00c8\3\2\2\2\u00ca\t\3\2\2\2\u00cb\u00cc\7\27")
        buf.write("\2\2\u00cc\u00cd\7/\2\2\u00cd\u00ce\5\u00a6T\2\u00ce\u00cf")
        buf.write("\7\60\2\2\u00cf\u00d0\5l\67\2\u00d0\13\3\2\2\2\u00d1\u00d2")
        buf.write("\7\30\2\2\u00d2\u00d3\7/\2\2\u00d3\u00d4\7\60\2\2\u00d4")
        buf.write("\u00d5\5l\67\2\u00d5\r\3\2\2\2\u00d6\u00d7\t\2\2\2\u00d7")
        buf.write("\u00d8\7/\2\2\u00d8\u00d9\5\u00a6T\2\u00d9\u00da\7\60")
        buf.write("\2\2\u00da\u00db\5l\67\2\u00db\17\3\2\2\2\u00dc\u00dd")
        buf.write("\7\26\2\2\u00dd\u00de\5\u00acW\2\u00de\u00df\7\67\2\2")
        buf.write("\u00df\u00e0\5\u00b6\\\2\u00e0\u00e1\78\2\2\u00e1\21\3")
        buf.write("\2\2\2\u00e2\u00e3\7\26\2\2\u00e3\u00e4\5\24\13\2\u00e4")
        buf.write("\u00e5\78\2\2\u00e5\23\3\2\2\2\u00e6\u00e7\79\2\2\u00e7")
        buf.write("\u00e8\5\26\f\2\u00e8\u00e9\5v<\2\u00e9\u00ef\3\2\2\2")
        buf.write("\u00ea\u00eb\5\u00acW\2\u00eb\u00ec\7\67\2\2\u00ec\u00ed")
        buf.write("\5\u00b6\\\2\u00ed\u00ef\3\2\2\2\u00ee\u00e6\3\2\2\2\u00ee")
        buf.write("\u00ea\3\2\2\2\u00ef\25\3\2\2\2\u00f0\u00f1\7\66\2\2\u00f1")
        buf.write("\u00f2\79\2\2\u00f2\u00f3\5\26\f\2\u00f3\u00f4\5v<\2\u00f4")
        buf.write("\u00f5\7\66\2\2\u00f5\u00fb\3\2\2\2\u00f6\u00f7\7\67\2")
        buf.write("\2\u00f7\u00f8\5\u00b6\\\2\u00f8\u00f9\7\'\2\2\u00f9\u00fb")
        buf.write("\3\2\2\2\u00fa\u00f0\3\2\2\2\u00fa\u00f6\3\2\2\2\u00fb")
        buf.write("\27\3\2\2\2\u00fc\u00fd\7\25\2\2\u00fd\u00fe\5\u00acW")
        buf.write("\2\u00fe\u00ff\7\67\2\2\u00ff\u0100\5\u00b6\\\2\u0100")
        buf.write("\u0101\78\2\2\u0101\31\3\2\2\2\u0102\u0103\7\25\2\2\u0103")
        buf.write("\u0104\5\34\17\2\u0104\u0105\78\2\2\u0105\33\3\2\2\2\u0106")
        buf.write("\u0107\79\2\2\u0107\u0108\5\36\20\2\u0108\u0109\5v<\2")
        buf.write("\u0109\u010f\3\2\2\2\u010a\u010b\5\u00acW\2\u010b\u010c")
        buf.write("\7\67\2\2\u010c\u010d\5\u00b6\\\2\u010d\u010f\3\2\2\2")
        buf.write("\u010e\u0106\3\2\2\2\u010e\u010a\3\2\2\2\u010f\35\3\2")
        buf.write("\2\2\u0110\u0111\7\66\2\2\u0111\u0112\79\2\2\u0112\u0113")
        buf.write("\5\36\20\2\u0113\u0114\5v<\2\u0114\u0115\7\66\2\2\u0115")
        buf.write("\u011b\3\2\2\2\u0116\u0117\7\67\2\2\u0117\u0118\5\u00b6")
        buf.write("\\\2\u0118\u0119\7\'\2\2\u0119\u011b\3\2\2\2\u011a\u0110")
        buf.write("\3\2\2\2\u011a\u0116\3\2\2\2\u011b\37\3\2\2\2\u011c\u011d")
        buf.write("\7\26\2\2\u011d\u011e\5\u00aaV\2\u011e\u011f\7\67\2\2")
        buf.write("\u011f\u0120\5\u00b6\\\2\u0120\u0121\78\2\2\u0121!\3\2")
        buf.write("\2\2\u0122\u0123\7\26\2\2\u0123\u0124\5(\25\2\u0124\u0125")
        buf.write("\78\2\2\u0125#\3\2\2\2\u0126\u0127\5&\24\2\u0127\u0128")
        buf.write("\5$\23\2\u0128\u012b\3\2\2\2\u0129\u012b\5&\24\2\u012a")
        buf.write("\u0126\3\2\2\2\u012a\u0129\3\2\2\2\u012b%\3\2\2\2\u012c")
        buf.write("\u012d\t\2\2\2\u012d\u0132\7\66\2\2\u012e\u0132\t\2\2")
        buf.write("\2\u012f\u0130\7\67\2\2\u0130\u0132\5\u00b6\\\2\u0131")
        buf.write("\u012c\3\2\2\2\u0131\u012e\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0132\'\3\2\2\2\u0133\u0134\t\2\2\2\u0134\u0135\5*\26")
        buf.write("\2\u0135\u0136\5v<\2\u0136\u013c\3\2\2\2\u0137\u0138\5")
        buf.write("\u00acW\2\u0138\u0139\7\67\2\2\u0139\u013a\5\u00b6\\\2")
        buf.write("\u013a\u013c\3\2\2\2\u013b\u0133\3\2\2\2\u013b\u0137\3")
        buf.write("\2\2\2\u013c)\3\2\2\2\u013d\u013e\7\66\2\2\u013e\u013f")
        buf.write("\t\2\2\2\u013f\u0140\5*\26\2\u0140\u0141\5v<\2\u0141\u0142")
        buf.write("\7\66\2\2\u0142\u0148\3\2\2\2\u0143\u0144\7\67\2\2\u0144")
        buf.write("\u0145\5\u00b6\\\2\u0145\u0146\7\'\2\2\u0146\u0148\3\2")
        buf.write("\2\2\u0147\u013d\3\2\2\2\u0147\u0143\3\2\2\2\u0148+\3")
        buf.write("\2\2\2\u0149\u014a\7\25\2\2\u014a\u014b\5\u00aaV\2\u014b")
        buf.write("\u014c\7\67\2\2\u014c\u014d\5\u00b6\\\2\u014d\u014e\7")
        buf.write("8\2\2\u014e-\3\2\2\2\u014f\u0150\7\25\2\2\u0150\u0151")
        buf.write("\5\60\31\2\u0151\u0152\78\2\2\u0152/\3\2\2\2\u0153\u0154")
        buf.write("\t\2\2\2\u0154\u0155\5\62\32\2\u0155\u0156\5v<\2\u0156")
        buf.write("\u015c\3\2\2\2\u0157\u0158\5\u00acW\2\u0158\u0159\7\67")
        buf.write("\2\2\u0159\u015a\5\u00b6\\\2\u015a\u015c\3\2\2\2\u015b")
        buf.write("\u0153\3\2\2\2\u015b\u0157\3\2\2\2\u015c\61\3\2\2\2\u015d")
        buf.write("\u015e\7\66\2\2\u015e\u015f\t\2\2\2\u015f\u0160\5\62\32")
        buf.write("\2\u0160\u0161\5v<\2\u0161\u0162\7\66\2\2\u0162\u0168")
        buf.write("\3\2\2\2\u0163\u0164\7\67\2\2\u0164\u0165\5\u00b6\\\2")
        buf.write("\u0165\u0166\7\'\2\2\u0166\u0168\3\2\2\2\u0167\u015d\3")
        buf.write("\2\2\2\u0167\u0163\3\2\2\2\u0168\63\3\2\2\2\u0169\u016a")
        buf.write("\t\2\2\2\u016a\u016b\7/\2\2\u016b\u016c\5\u00a6T\2\u016c")
        buf.write("\u016d\7\60\2\2\u016d\u016e\5l\67\2\u016e\65\3\2\2\2\u016f")
        buf.write("\u0170\5:\36\2\u0170\u0171\5<\37\2\u0171\u0172\5@!\2\u0172")
        buf.write("\u0173\78\2\2\u0173\67\3\2\2\2\u0174\u0175\5:\36\2\u0175")
        buf.write("\u0176\5<\37\2\u0176\u0177\5@!\2\u01779\3\2\2\2\u0178")
        buf.write("\u017b\t\2\2\2\u0179\u017c\5\u0090I\2\u017a\u017c\3\2")
        buf.write("\2\2\u017b\u0179\3\2\2\2\u017b\u017a\3\2\2\2\u017c\u0180")
        buf.write("\3\2\2\2\u017d\u017e\7\34\2\2\u017e\u0181\7:\2\2\u017f")
        buf.write("\u0181\3\2\2\2\u0180\u017d\3\2\2\2\u0180\u017f\3\2\2\2")
        buf.write("\u0181;\3\2\2\2\u0182\u0183\5> \2\u0183\u0184\5<\37\2")
        buf.write("\u0184\u0188\3\2\2\2\u0185\u0188\5> \2\u0186\u0188\3\2")
        buf.write("\2\2\u0187\u0182\3\2\2\2\u0187\u0185\3\2\2\2\u0187\u0186")
        buf.write("\3\2\2\2\u0188=\3\2\2\2\u0189\u0190\7\65\2\2\u018a\u0191")
        buf.write("\79\2\2\u018b\u018c\79\2\2\u018c\u018d\7/\2\2\u018d\u018e")
        buf.write("\5\u00aeX\2\u018e\u018f\7\60\2\2\u018f\u0191\3\2\2\2\u0190")
        buf.write("\u018a\3\2\2\2\u0190\u018b\3\2\2\2\u0191?\3\2\2\2\u0192")
        buf.write("\u0193\7\65\2\2\u0193\u0194\79\2\2\u0194\u0195\7/\2\2")
        buf.write("\u0195\u0196\5\u00aeX\2\u0196\u0197\7\60\2\2\u0197A\3")
        buf.write("\2\2\2\u0198\u0199\5D#\2\u0199\u019a\7\'\2\2\u019a\u019b")
        buf.write("\5v<\2\u019b\u019c\78\2\2\u019cC\3\2\2\2\u019d\u01a1\7")
        buf.write("9\2\2\u019e\u01a1\5V,\2\u019f\u01a1\5Z.\2\u01a0\u019d")
        buf.write("\3\2\2\2\u01a0\u019e\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1")
        buf.write("\u01a4\3\2\2\2\u01a2\u01a5\5\u0090I\2\u01a3\u01a5\3\2")
        buf.write("\2\2\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5E\3")
        buf.write("\2\2\2\u01a6\u01a7\7/\2\2\u01a7\u01a8\5v<\2\u01a8\u01a9")
        buf.write("\7\60\2\2\u01a9G\3\2\2\2\u01aa\u01ab\7\5\2\2\u01ab\u01ac")
        buf.write("\5F$\2\u01ac\u01ad\5l\67\2\u01ad\u01ae\5J&\2\u01aeI\3")
        buf.write("\2\2\2\u01af\u01b0\5L\'\2\u01b0\u01b1\5J&\2\u01b1\u01b5")
        buf.write("\3\2\2\2\u01b2\u01b5\5L\'\2\u01b3\u01b5\5N(\2\u01b4\u01af")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("K\3\2\2\2\u01b6\u01b7\7\6\2\2\u01b7\u01b8\5F$\2\u01b8")
        buf.write("\u01b9\5l\67\2\u01b9\u01ba\5N(\2\u01baM\3\2\2\2\u01bb")
        buf.write("\u01be\5P)\2\u01bc\u01be\3\2\2\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01beO\3\2\2\2\u01bf\u01c0\7\7\2\2\u01c0")
        buf.write("\u01c1\5l\67\2\u01c1Q\3\2\2\2\u01c2\u01c3\7\32\2\2\u01c3")
        buf.write("\u01c6\5v<\2\u01c4\u01c6\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6S\3\2\2\2\u01c7\u01c8\7\b\2\2\u01c8")
        buf.write("\u01c9\7/\2\2\u01c9\u01ca\t\2\2\2\u01ca\u01cb\7\r\2\2")
        buf.write("\u01cb\u01cc\5v<\2\u01cc\u01cd\7\35\2\2\u01cd\u01ce\5")
        buf.write("v<\2\u01ce\u01cf\5R*\2\u01cf\u01d0\7\60\2\2\u01d0\u01d1")
        buf.write("\5l\67\2\u01d1U\3\2\2\2\u01d2\u01d3\5v<\2\u01d3\u01d4")
        buf.write("\7\65\2\2\u01d4\u01d5\79\2\2\u01d5W\3\2\2\2\u01d6\u01d7")
        buf.write("\5v<\2\u01d7\u01d8\7\65\2\2\u01d8\u01d9\79\2\2\u01d9\u01da")
        buf.write("\7/\2\2\u01da\u01db\5\u009eP\2\u01db\u01dc\7\60\2\2\u01dc")
        buf.write("Y\3\2\2\2\u01dd\u01de\t\2\2\2\u01de\u01df\7\34\2\2\u01df")
        buf.write("\u01e0\7:\2\2\u01e0[\3\2\2\2\u01e1\u01e2\t\2\2\2\u01e2")
        buf.write("\u01e3\7\34\2\2\u01e3\u01e4\7:\2\2\u01e4\u01e5\7/\2\2")
        buf.write("\u01e5\u01e6\5\u009eP\2\u01e6\u01e7\7\60\2\2\u01e7]\3")
        buf.write("\2\2\2\u01e8\u01eb\5X-\2\u01e9\u01eb\5\\/\2\u01ea\u01e8")
        buf.write("\3\2\2\2\u01ea\u01e9\3\2\2\2\u01eb_\3\2\2\2\u01ec\u01ed")
        buf.write("\5^\60\2\u01ed\u01ee\78\2\2\u01eea\3\2\2\2\u01ef\u01f0")
        buf.write("\7\3\2\2\u01f0\u01f1\78\2\2\u01f1c\3\2\2\2\u01f2\u01f3")
        buf.write("\7\4\2\2\u01f3\u01f4\78\2\2\u01f4e\3\2\2\2\u01f5\u01f8")
        buf.write("\5v<\2\u01f6\u01f8\3\2\2\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6")
        buf.write("\3\2\2\2\u01f8g\3\2\2\2\u01f9\u01fa\7\22\2\2\u01fa\u01fb")
        buf.write("\5f\64\2\u01fb\u01fc\78\2\2\u01fci\3\2\2\2\u01fd\u01fe")
        buf.write("\7\63\2\2\u01fe\u01ff\5n8\2\u01ff\u0200\7\64\2\2\u0200")
        buf.write("k\3\2\2\2\u0201\u0202\7\63\2\2\u0202\u0203\5p9\2\u0203")
        buf.write("\u0204\7\64\2\2\u0204m\3\2\2\2\u0205\u0206\5r:\2\u0206")
        buf.write("\u0207\5n8\2\u0207\u020b\3\2\2\2\u0208\u020b\5r:\2\u0209")
        buf.write("\u020b\3\2\2\2\u020a\u0205\3\2\2\2\u020a\u0208\3\2\2\2")
        buf.write("\u020a\u0209\3\2\2\2\u020bo\3\2\2\2\u020c\u020d\5t;\2")
        buf.write("\u020d\u020e\5p9\2\u020e\u0212\3\2\2\2\u020f\u0212\5t")
        buf.write(";\2\u0210\u0212\3\2\2\2\u0211\u020c\3\2\2\2\u0211\u020f")
        buf.write("\3\2\2\2\u0211\u0210\3\2\2\2\u0212q\3\2\2\2\u0213\u021b")
        buf.write("\5\"\22\2\u0214\u021b\5.\30\2\u0215\u021b\5 \21\2\u0216")
        buf.write("\u021b\5,\27\2\u0217\u021b\5\64\33\2\u0218\u021b\5\n\6")
        buf.write("\2\u0219\u021b\5\f\7\2\u021a\u0213\3\2\2\2\u021a\u0214")
        buf.write("\3\2\2\2\u021a\u0215\3\2\2\2\u021a\u0216\3\2\2\2\u021a")
        buf.write("\u0217\3\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2\2")
        buf.write("\u021bs\3\2\2\2\u021c\u022b\5\22\n\2\u021d\u022b\5\32")
        buf.write("\16\2\u021e\u022b\5\20\t\2\u021f\u022b\5\30\r\2\u0220")
        buf.write("\u022b\5B\"\2\u0221\u022b\5\32\16\2\u0222\u022b\5B\"\2")
        buf.write("\u0223\u022b\5H%\2\u0224\u022b\5T+\2\u0225\u022b\5\66")
        buf.write("\34\2\u0226\u022b\5`\61\2\u0227\u022b\5b\62\2\u0228\u022b")
        buf.write("\5d\63\2\u0229\u022b\5h\65\2\u022a\u021c\3\2\2\2\u022a")
        buf.write("\u021d\3\2\2\2\u022a\u021e\3\2\2\2\u022a\u021f\3\2\2\2")
        buf.write("\u022a\u0220\3\2\2\2\u022a\u0221\3\2\2\2\u022a\u0222\3")
        buf.write("\2\2\2\u022a\u0223\3\2\2\2\u022a\u0224\3\2\2\2\u022a\u0225")
        buf.write("\3\2\2\2\u022a\u0226\3\2\2\2\u022a\u0227\3\2\2\2\u022a")
        buf.write("\u0228\3\2\2\2\u022a\u0229\3\2\2\2\u022bu\3\2\2\2\u022c")
        buf.write("\u022d\5x=\2\u022d\u022e\t\3\2\2\u022e\u022f\5x=\2\u022f")
        buf.write("\u0232\3\2\2\2\u0230\u0232\5x=\2\u0231\u022c\3\2\2\2\u0231")
        buf.write("\u0230\3\2\2\2\u0232w\3\2\2\2\u0233\u0234\5z>\2\u0234")
        buf.write("\u0235\t\4\2\2\u0235\u0236\5z>\2\u0236\u0239\3\2\2\2\u0237")
        buf.write("\u0239\5z>\2\u0238\u0233\3\2\2\2\u0238\u0237\3\2\2\2\u0239")
        buf.write("y\3\2\2\2\u023a\u023b\b>\1\2\u023b\u023c\5|?\2\u023c\u0242")
        buf.write("\3\2\2\2\u023d\u023e\f\4\2\2\u023e\u023f\t\5\2\2\u023f")
        buf.write("\u0241\5|?\2\u0240\u023d\3\2\2\2\u0241\u0244\3\2\2\2\u0242")
        buf.write("\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243{\3\2\2\2\u0244")
        buf.write("\u0242\3\2\2\2\u0245\u0246\b?\1\2\u0246\u0247\5~@\2\u0247")
        buf.write("\u024d\3\2\2\2\u0248\u0249\f\4\2\2\u0249\u024a\t\6\2\2")
        buf.write("\u024a\u024c\5~@\2\u024b\u0248\3\2\2\2\u024c\u024f\3\2")
        buf.write("\2\2\u024d\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e}\3")
        buf.write("\2\2\2\u024f\u024d\3\2\2\2\u0250\u0251\b@\1\2\u0251\u0252")
        buf.write("\5\u0080A\2\u0252\u0258\3\2\2\2\u0253\u0254\f\4\2\2\u0254")
        buf.write("\u0255\t\7\2\2\u0255\u0257\5\u0080A\2\u0256\u0253\3\2")
        buf.write("\2\2\u0257\u025a\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259")
        buf.write("\3\2\2\2\u0259\177\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c")
        buf.write("\7#\2\2\u025c\u025f\5\u0080A\2\u025d\u025f\5\u0082B\2")
        buf.write("\u025e\u025b\3\2\2\2\u025e\u025d\3\2\2\2\u025f\u0081\3")
        buf.write("\2\2\2\u0260\u0261\7\37\2\2\u0261\u0264\5\u0082B\2\u0262")
        buf.write("\u0264\5\u0084C\2\u0263\u0260\3\2\2\2\u0263\u0262\3\2")
        buf.write("\2\2\u0264\u0083\3\2\2\2\u0265\u0266\bC\1\2\u0266\u0267")
        buf.write("\5\u0086D\2\u0267\u026c\3\2\2\2\u0268\u0269\f\4\2\2\u0269")
        buf.write("\u026b\5\u0090I\2\u026a\u0268\3\2\2\2\u026b\u026e\3\2")
        buf.write("\2\2\u026c\u026a\3\2\2\2\u026c\u026d\3\2\2\2\u026d\u0085")
        buf.write("\3\2\2\2\u026e\u026c\3\2\2\2\u026f\u0270\bD\1\2\u0270")
        buf.write("\u0271\5\u0088E\2\u0271\u0276\3\2\2\2\u0272\u0273\f\4")
        buf.write("\2\2\u0273\u0275\5\u0096L\2\u0274\u0272\3\2\2\2\u0275")
        buf.write("\u0278\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0087\3\2\2\2\u0278\u0276\3\2\2\2\u0279\u027a\7")
        buf.write("9\2\2\u027a\u027d\5\u009aN\2\u027b\u027d\5\u008aF\2\u027c")
        buf.write("\u0279\3\2\2\2\u027c\u027b\3\2\2\2\u027d\u0089\3\2\2\2")
        buf.write("\u027e\u027f\7\31\2\2\u027f\u0280\5v<\2\u0280\u0281\7")
        buf.write("/\2\2\u0281\u0282\5\u009eP\2\u0282\u0283\7\60\2\2\u0283")
        buf.write("\u0286\3\2\2\2\u0284\u0286\5\u008cG\2\u0285\u027e\3\2")
        buf.write("\2\2\u0285\u0284\3\2\2\2\u0286\u008b\3\2\2\2\u0287\u028c")
        buf.write("\5\u00a4S\2\u0288\u028c\79\2\2\u0289\u028c\7\33\2\2\u028a")
        buf.write("\u028c\5\u008eH\2\u028b\u0287\3\2\2\2\u028b\u0288\3\2")
        buf.write("\2\2\u028b\u0289\3\2\2\2\u028b\u028a\3\2\2\2\u028c\u008d")
        buf.write("\3\2\2\2\u028d\u028e\7/\2\2\u028e\u028f\5v<\2\u028f\u0290")
        buf.write("\7\60\2\2\u0290\u008f\3\2\2\2\u0291\u0292\bI\1\2\u0292")
        buf.write("\u0293\7\61\2\2\u0293\u0294\5v<\2\u0294\u0295\7\62\2\2")
        buf.write("\u0295\u029d\3\2\2\2\u0296\u0297\f\4\2\2\u0297\u0298\7")
        buf.write("\61\2\2\u0298\u0299\5v<\2\u0299\u029a\7\62\2\2\u029a\u029c")
        buf.write("\3\2\2\2\u029b\u0296\3\2\2\2\u029c\u029f\3\2\2\2\u029d")
        buf.write("\u029b\3\2\2\2\u029d\u029e\3\2\2\2\u029e\u0091\3\2\2\2")
        buf.write("\u029f\u029d\3\2\2\2\u02a0\u02a5\5\u0094K\2\u02a1\u02a2")
        buf.write("\5\u0094K\2\u02a2\u02a3\5\u0090I\2\u02a3\u02a5\3\2\2\2")
        buf.write("\u02a4\u02a0\3\2\2\2\u02a4\u02a1\3\2\2\2\u02a5\u0093\3")
        buf.write("\2\2\2\u02a6\u02ad\t\2\2\2\u02a7\u02a8\5v<\2\u02a8\u02a9")
        buf.write("\5V,\2\u02a9\u02aa\t\2\2\2\u02aa\u02ad\3\2\2\2\u02ab\u02ad")
        buf.write("\3\2\2\2\u02ac\u02a6\3\2\2\2\u02ac\u02a7\3\2\2\2\u02ac")
        buf.write("\u02ab\3\2\2\2\u02ad\u0095\3\2\2\2\u02ae\u02af\5\u0098")
        buf.write("M\2\u02af\u02b0\5\u0096L\2\u02b0\u02b3\3\2\2\2\u02b1\u02b3")
        buf.write("\5\u0098M\2\u02b2\u02ae\3\2\2\2\u02b2\u02b1\3\2\2\2\u02b3")
        buf.write("\u0097\3\2\2\2\u02b4\u02b5\7\65\2\2\u02b5\u02bd\79\2\2")
        buf.write("\u02b6\u02b7\7\65\2\2\u02b7\u02b8\79\2\2\u02b8\u02b9\7")
        buf.write("/\2\2\u02b9\u02ba\5\u009eP\2\u02ba\u02bb\7\60\2\2\u02bb")
        buf.write("\u02bd\3\2\2\2\u02bc\u02b4\3\2\2\2\u02bc\u02b6\3\2\2\2")
        buf.write("\u02bd\u0099\3\2\2\2\u02be\u02bf\5\u009cO\2\u02bf\u02c0")
        buf.write("\5\u009aN\2\u02c0\u02c3\3\2\2\2\u02c1\u02c3\5\u009cO\2")
        buf.write("\u02c2\u02be\3\2\2\2\u02c2\u02c1\3\2\2\2\u02c3\u009b\3")
        buf.write("\2\2\2\u02c4\u02c5\7\34\2\2\u02c5\u02cd\7:\2\2\u02c6\u02c7")
        buf.write("\7\34\2\2\u02c7\u02c8\7:\2\2\u02c8\u02c9\7/\2\2\u02c9")
        buf.write("\u02ca\5\u009eP\2\u02ca\u02cb\7\60\2\2\u02cb\u02cd\3\2")
        buf.write("\2\2\u02cc\u02c4\3\2\2\2\u02cc\u02c6\3\2\2\2\u02cd\u009d")
        buf.write("\3\2\2\2\u02ce\u02cf\5v<\2\u02cf\u02d0\7\66\2\2\u02d0")
        buf.write("\u02d1\5\u009eP\2\u02d1\u02d5\3\2\2\2\u02d2\u02d5\5v<")
        buf.write("\2\u02d3\u02d5\3\2\2\2\u02d4\u02ce\3\2\2\2\u02d4\u02d2")
        buf.write("\3\2\2\2\u02d4\u02d3\3\2\2\2\u02d5\u009f\3\2\2\2\u02d6")
        buf.write("\u02d7\7\f\2\2\u02d7\u02d8\7/\2\2\u02d8\u02d9\5\u00a2")
        buf.write("R\2\u02d9\u02da\7\60\2\2\u02da\u00a1\3\2\2\2\u02db\u02dc")
        buf.write("\5v<\2\u02dc\u02dd\7\66\2\2\u02dd\u02de\5\u00a2R\2\u02de")
        buf.write("\u02e2\3\2\2\2\u02df\u02e2\5v<\2\u02e0\u02e2\3\2\2\2\u02e1")
        buf.write("\u02db\3\2\2\2\u02e1\u02df\3\2\2\2\u02e1\u02e0\3\2\2\2")
        buf.write("\u02e2\u00a3\3\2\2\2\u02e3\u02ea\7=\2\2\u02e4\u02ea\7")
        buf.write(">\2\2\u02e5\u02ea\7<\2\2\u02e6\u02ea\7\t\2\2\u02e7\u02ea")
        buf.write("\7;\2\2\u02e8\u02ea\5\u00a0Q\2\u02e9\u02e3\3\2\2\2\u02e9")
        buf.write("\u02e4\3\2\2\2\u02e9\u02e5\3\2\2\2\u02e9\u02e6\3\2\2\2")
        buf.write("\u02e9\u02e7\3\2\2\2\u02e9\u02e8\3\2\2\2\u02ea\u00a5\3")
        buf.write("\2\2\2\u02eb\u02ec\5\u00a8U\2\u02ec\u02ed\78\2\2\u02ed")
        buf.write("\u02ee\5\u00a6T\2\u02ee\u02f2\3\2\2\2\u02ef\u02f2\5\u00a8")
        buf.write("U\2\u02f0\u02f2\3\2\2\2\u02f1\u02eb\3\2\2\2\u02f1\u02ef")
        buf.write("\3\2\2\2\u02f1\u02f0\3\2\2\2\u02f2\u00a7\3\2\2\2\u02f3")
        buf.write("\u02f4\5\u00aaV\2\u02f4\u02f5\7\67\2\2\u02f5\u02f6\5\u00b6")
        buf.write("\\\2\u02f6\u00a9\3\2\2\2\u02f7\u02f8\t\2\2\2\u02f8\u02f9")
        buf.write("\7\66\2\2\u02f9\u02fd\5\u00aaV\2\u02fa\u02fd\t\2\2\2\u02fb")
        buf.write("\u02fd\3\2\2\2\u02fc\u02f7\3\2\2\2\u02fc\u02fa\3\2\2\2")
        buf.write("\u02fc\u02fb\3\2\2\2\u02fd\u00ab\3\2\2\2\u02fe\u02ff\7")
        buf.write("9\2\2\u02ff\u0300\7\66\2\2\u0300\u0304\5\u00acW\2\u0301")
        buf.write("\u0304\79\2\2\u0302\u0304\3\2\2\2\u0303\u02fe\3\2\2\2")
        buf.write("\u0303\u0301\3\2\2\2\u0303\u0302\3\2\2\2\u0304\u00ad\3")
        buf.write("\2\2\2\u0305\u0308\5\u00a4S\2\u0306\u0308\5v<\2\u0307")
        buf.write("\u0305\3\2\2\2\u0307\u0306\3\2\2\2\u0308\u0309\3\2\2\2")
        buf.write("\u0309\u030a\7\66\2\2\u030a\u030b\5\u00aeX\2\u030b\u0312")
        buf.write("\3\2\2\2\u030c\u030f\5\u00a4S\2\u030d\u030f\5v<\2\u030e")
        buf.write("\u030c\3\2\2\2\u030e\u030d\3\2\2\2\u030f\u0312\3\2\2\2")
        buf.write("\u0310\u0312\3\2\2\2\u0311\u0307\3\2\2\2\u0311\u030e\3")
        buf.write("\2\2\2\u0311\u0310\3\2\2\2\u0312\u00af\3\2\2\2\u0313\u0314")
        buf.write("\7\f\2\2\u0314\u0315\7\61\2\2\u0315\u0316\5\u00b2Z\2\u0316")
        buf.write("\u0317\7\66\2\2\u0317\u0318\7=\2\2\u0318\u0319\7\62\2")
        buf.write("\2\u0319\u00b1\3\2\2\2\u031a\u0320\5\u00b0Y\2\u031b\u0320")
        buf.write("\7\16\2\2\u031c\u0320\7\17\2\2\u031d\u0320\7\20\2\2\u031e")
        buf.write("\u0320\7\21\2\2\u031f\u031a\3\2\2\2\u031f\u031b\3\2\2")
        buf.write("\2\u031f\u031c\3\2\2\2\u031f\u031d\3\2\2\2\u031f\u031e")
        buf.write("\3\2\2\2\u0320\u00b3\3\2\2\2\u0321\u0322\t\b\2\2\u0322")
        buf.write("\u00b5\3\2\2\2\u0323\u0327\5\u00b4[\2\u0324\u0327\5\u00b0")
        buf.write("Y\2\u0325\u0327\79\2\2\u0326\u0323\3\2\2\2\u0326\u0324")
        buf.write("\3\2\2\2\u0326\u0325\3\2\2\2\u0327\u00b7\3\2\2\2;\u00bf")
        buf.write("\u00c9\u00ee\u00fa\u010e\u011a\u012a\u0131\u013b\u0147")
        buf.write("\u015b\u0167\u017b\u0180\u0187\u0190\u01a0\u01a4\u01b4")
        buf.write("\u01bd\u01c5\u01ea\u01f7\u020a\u0211\u021a\u022a\u0231")
        buf.write("\u0238\u0242\u024d\u0258\u025e\u0263\u026c\u0276\u027c")
        buf.write("\u0285\u028b\u029d\u02a4\u02ac\u02b2\u02bc\u02c2\u02cc")
        buf.write("\u02d4\u02e1\u02e9\u02f1\u02fc\u0303\u0307\u030e\u0311")
        buf.write("\u031f\u0326")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Break'", "'Continue'", "'If'", "'Elseif'", 
                     "'Else'", "'Foreach'", "<INVALID>", "'True'", "'False'", 
                     "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'::'", "'..'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", "'='", 
                     "'!='", "'>='", "'<='", "'>'", "'<'", "'==.'", "'+.'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", "','", 
                     "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "BOOLLIT", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", 
                      "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", 
                      "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", 
                      "GTE", "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", 
                      "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                      "COLON", "SEMICOLON", "VARIABLE_IN_FUNC_IDENTIFIERS", 
                      "DOLLAR_IDENTIFIERS", "STRINGLIT", "FLOATLIT", "INTLIT_IN_ARRAY", 
                      "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "BLOCK_COMMENT", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_declarations = 1
    RULE_class_declaration = 2
    RULE_class_inheritance = 3
    RULE_constructor_dclr = 4
    RULE_destructor_dclr = 5
    RULE_method_declaration = 6
    RULE_var_variable_declaration_noinit = 7
    RULE_var_variable_declaration = 8
    RULE_var_declare_initiate_list = 9
    RULE_var_type_and_assign = 10
    RULE_val_variable_declaration_noinit = 11
    RULE_val_variable_declaration = 12
    RULE_val_declare_initiate_list = 13
    RULE_val_type_and_assign = 14
    RULE_var_both_variable_declaration_noinnit = 15
    RULE_var_both_variable_declaration = 16
    RULE_var_both_no_value_assign_declare_list = 17
    RULE_var_both_no_value_assign_declare = 18
    RULE_var_both_declare_initiate_list = 19
    RULE_var_both_type_and_assign = 20
    RULE_val_both_variable_declaration_noinnit = 21
    RULE_val_both_variable_declaration = 22
    RULE_val_both_declare_initiate_list = 23
    RULE_val_both_type_and_assign = 24
    RULE_function_declaration = 25
    RULE_call_func_statement = 26
    RULE_call_func = 27
    RULE_call_func_header = 28
    RULE_call_func_attr_list = 29
    RULE_call_func_attr = 30
    RULE_call_func_end = 31
    RULE_assignment_statements = 32
    RULE_lhs = 33
    RULE_if_condition = 34
    RULE_if_statements = 35
    RULE_elseif_list_statements = 36
    RULE_elseif_statement = 37
    RULE_else_statement_or_none = 38
    RULE_else_statement = 39
    RULE_by_expr = 40
    RULE_forin_statements = 41
    RULE_instance_attr_access = 42
    RULE_instance_method_access = 43
    RULE_static_attr_access = 44
    RULE_static_method_access = 45
    RULE_method_invocation = 46
    RULE_method_invocation_statement = 47
    RULE_break_statements = 48
    RULE_continue_statements = 49
    RULE_return_expr = 50
    RULE_return_statements = 51
    RULE_block_class_statements = 52
    RULE_block_statements = 53
    RULE_statements_class = 54
    RULE_statements = 55
    RULE_statement_class = 56
    RULE_statement = 57
    RULE_expr = 58
    RULE_expr1 = 59
    RULE_expr2 = 60
    RULE_expr3 = 61
    RULE_expr4 = 62
    RULE_expr5 = 63
    RULE_expr6 = 64
    RULE_expr7 = 65
    RULE_expr8 = 66
    RULE_expr9 = 67
    RULE_expr10 = 68
    RULE_expr11 = 69
    RULE_expr12 = 70
    RULE_index_operators = 71
    RULE_index_expr = 72
    RULE_index = 73
    RULE_instance_accesses = 74
    RULE_instance_access = 75
    RULE_static_accesses = 76
    RULE_static_access = 77
    RULE_list_expr = 78
    RULE_array_lit = 79
    RULE_array_val = 80
    RULE_literal = 81
    RULE_list_parameters = 82
    RULE_param = 83
    RULE_identifier_list = 84
    RULE_variable_in_func_identifier_list = 85
    RULE_value_list = 86
    RULE_array_type = 87
    RULE_array_element_type = 88
    RULE_primitive_type = 89
    RULE_variable_type = 90

    ruleNames =  [ "program", "class_declarations", "class_declaration", 
                   "class_inheritance", "constructor_dclr", "destructor_dclr", 
                   "method_declaration", "var_variable_declaration_noinit", 
                   "var_variable_declaration", "var_declare_initiate_list", 
                   "var_type_and_assign", "val_variable_declaration_noinit", 
                   "val_variable_declaration", "val_declare_initiate_list", 
                   "val_type_and_assign", "var_both_variable_declaration_noinnit", 
                   "var_both_variable_declaration", "var_both_no_value_assign_declare_list", 
                   "var_both_no_value_assign_declare", "var_both_declare_initiate_list", 
                   "var_both_type_and_assign", "val_both_variable_declaration_noinnit", 
                   "val_both_variable_declaration", "val_both_declare_initiate_list", 
                   "val_both_type_and_assign", "function_declaration", "call_func_statement", 
                   "call_func", "call_func_header", "call_func_attr_list", 
                   "call_func_attr", "call_func_end", "assignment_statements", 
                   "lhs", "if_condition", "if_statements", "elseif_list_statements", 
                   "elseif_statement", "else_statement_or_none", "else_statement", 
                   "by_expr", "forin_statements", "instance_attr_access", 
                   "instance_method_access", "static_attr_access", "static_method_access", 
                   "method_invocation", "method_invocation_statement", "break_statements", 
                   "continue_statements", "return_expr", "return_statements", 
                   "block_class_statements", "block_statements", "statements_class", 
                   "statements", "statement_class", "statement", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "expr10", "expr11", "expr12", 
                   "index_operators", "index_expr", "index", "instance_accesses", 
                   "instance_access", "static_accesses", "static_access", 
                   "list_expr", "array_lit", "array_val", "literal", "list_parameters", 
                   "param", "identifier_list", "variable_in_func_identifier_list", 
                   "value_list", "array_type", "array_element_type", "primitive_type", 
                   "variable_type" ]

    EOF = Token.EOF
    BREAK=1
    CONTINUE=2
    IF=3
    ELSEIF=4
    ELSE=5
    FOREACH=6
    BOOLLIT=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    STRING=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    SELF=25
    DOUBLECOLONOP=26
    DOUBLEDOTOP=27
    PLUSOP=28
    MINUSOP=29
    MULTIPLYOP=30
    DIVIDEOP=31
    MODULOOP=32
    NOTOP=33
    ANDOP=34
    OROP=35
    EQUALOP=36
    ASSIGNOP=37
    NOTEQUALOP=38
    GTE=39
    LTE=40
    GT=41
    LT=42
    STREQUALOP=43
    STRCONCATOP=44
    LB=45
    RB=46
    LSB=47
    RSB=48
    LCB=49
    RCB=50
    DOT=51
    COMMA=52
    COLON=53
    SEMICOLON=54
    VARIABLE_IN_FUNC_IDENTIFIERS=55
    DOLLAR_IDENTIFIERS=56
    STRINGLIT=57
    FLOATLIT=58
    INTLIT_IN_ARRAY=59
    INTLIT=60
    UNCLOSE_STRING=61
    ILLEGAL_ESCAPE=62
    BLOCK_COMMENT=63
    WS=64
    ERROR_CHAR=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declarations(self):
            return self.getTypedRuleContext(D96Parser.Class_declarationsContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.class_declarations()
            self.state = 183
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_declaration(self):
            return self.getTypedRuleContext(D96Parser.Class_declarationContext,0)


        def class_declarations(self):
            return self.getTypedRuleContext(D96Parser.Class_declarationsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declarations" ):
                return visitor.visitClass_declarations(self)
            else:
                return visitor.visitChildren(self)




    def class_declarations(self):

        localctx = D96Parser.Class_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declarations)
        try:
            self.state = 189
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.class_declaration()
                self.state = 186
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.class_declaration()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def class_inheritance(self):
            return self.getTypedRuleContext(D96Parser.Class_inheritanceContext,0)


        def block_class_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_class_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_declaration" ):
                return visitor.visitClass_declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(D96Parser.CLASS)
            self.state = 192
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 193
            self.class_inheritance()
            self.state = 194
            self.block_class_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_inheritanceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_inheritance

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_inheritance" ):
                return visitor.visitClass_inheritance(self)
            else:
                return visitor.visitChildren(self)




    def class_inheritance(self):

        localctx = D96Parser.Class_inheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_inheritance)
        try:
            self.state = 199
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(D96Parser.COLON)
                self.state = 197
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.LCB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constructor_dclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_constructor_dclr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstructor_dclr" ):
                return visitor.visitConstructor_dclr(self)
            else:
                return visitor.visitChildren(self)




    def constructor_dclr(self):

        localctx = D96Parser.Constructor_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 202
            self.match(D96Parser.LB)
            self.state = 203
            self.list_parameters()
            self.state = 204
            self.match(D96Parser.RB)
            self.state = 205
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_dclrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_dclr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestructor_dclr" ):
                return visitor.visitDestructor_dclr(self)
            else:
                return visitor.visitChildren(self)




    def destructor_dclr(self):

        localctx = D96Parser.Destructor_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_destructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(D96Parser.DESTRUCTOR)
            self.state = 208
            self.match(D96Parser.LB)
            self.state = 209
            self.match(D96Parser.RB)
            self.state = 210
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_declaration" ):
                return visitor.visitMethod_declaration(self)
            else:
                return visitor.visitChildren(self)




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 213
            self.match(D96Parser.LB)
            self.state = 214
            self.list_parameters()
            self.state = 215
            self.match(D96Parser.RB)
            self.state = 216
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_variable_declaration_noinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_variable_declaration_noinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_variable_declaration_noinit" ):
                return visitor.visitVar_variable_declaration_noinit(self)
            else:
                return visitor.visitChildren(self)




    def var_variable_declaration_noinit(self):

        localctx = D96Parser.Var_variable_declaration_noinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_variable_declaration_noinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(D96Parser.VAR)
            self.state = 219
            self.variable_in_func_identifier_list()
            self.state = 220
            self.match(D96Parser.COLON)
            self.state = 221
            self.variable_type()
            self.state = 222
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def var_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Var_declare_initiate_listContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_variable_declaration" ):
                return visitor.visitVar_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_variable_declaration(self):

        localctx = D96Parser.Var_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(D96Parser.VAR)
            self.state = 225
            self.var_declare_initiate_list()
            self.state = 226
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_initiate_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def var_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Var_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_declare_initiate_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare_initiate_list" ):
                return visitor.visitVar_declare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def var_declare_initiate_list(self):

        localctx = D96Parser.Var_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_var_declare_initiate_list)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 229
                self.var_type_and_assign()
                self.state = 230
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.variable_in_func_identifier_list()
                self.state = 233
                self.match(D96Parser.COLON)
                self.state = 234
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_type_and_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def var_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Var_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_type_and_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type_and_assign" ):
                return visitor.visitVar_type_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_type_and_assign(self):

        localctx = D96Parser.Var_type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_type_and_assign)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(D96Parser.COMMA)
                self.state = 239
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 240
                self.var_type_and_assign()
                self.state = 241
                self.expr()
                self.state = 242
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(D96Parser.COLON)
                self.state = 245
                self.variable_type()
                self.state = 246
                self.match(D96Parser.ASSIGNOP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_variable_declaration_noinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_variable_declaration_noinit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_variable_declaration_noinit" ):
                return visitor.visitVal_variable_declaration_noinit(self)
            else:
                return visitor.visitChildren(self)




    def val_variable_declaration_noinit(self):

        localctx = D96Parser.Val_variable_declaration_noinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_val_variable_declaration_noinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(D96Parser.VAL)
            self.state = 251
            self.variable_in_func_identifier_list()
            self.state = 252
            self.match(D96Parser.COLON)
            self.state = 253
            self.variable_type()
            self.state = 254
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def val_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Val_declare_initiate_listContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_variable_declaration" ):
                return visitor.visitVal_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def val_variable_declaration(self):

        localctx = D96Parser.Val_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_val_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(D96Parser.VAL)
            self.state = 257
            self.val_declare_initiate_list()
            self.state = 258
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_declare_initiate_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def val_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Val_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_val_declare_initiate_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_declare_initiate_list" ):
                return visitor.visitVal_declare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def val_declare_initiate_list(self):

        localctx = D96Parser.Val_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_val_declare_initiate_list)
        try:
            self.state = 268
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 260
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 261
                self.val_type_and_assign()
                self.state = 262
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.variable_in_func_identifier_list()
                self.state = 265
                self.match(D96Parser.COLON)
                self.state = 266
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_type_and_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def val_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Val_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_type_and_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_type_and_assign" ):
                return visitor.visitVal_type_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def val_type_and_assign(self):

        localctx = D96Parser.Val_type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_val_type_and_assign)
        try:
            self.state = 280
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.match(D96Parser.COMMA)
                self.state = 271
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 272
                self.val_type_and_assign()
                self.state = 273
                self.expr()
                self.state = 274
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.match(D96Parser.COLON)
                self.state = 277
                self.variable_type()
                self.state = 278
                self.match(D96Parser.ASSIGNOP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_variable_declaration_noinnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_both_variable_declaration_noinnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_both_variable_declaration_noinnit" ):
                return visitor.visitVar_both_variable_declaration_noinnit(self)
            else:
                return visitor.visitChildren(self)




    def var_both_variable_declaration_noinnit(self):

        localctx = D96Parser.Var_both_variable_declaration_noinnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_var_both_variable_declaration_noinnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(D96Parser.VAR)
            self.state = 283
            self.identifier_list()
            self.state = 284
            self.match(D96Parser.COLON)
            self.state = 285
            self.variable_type()
            self.state = 286
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def var_both_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Var_both_declare_initiate_listContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_both_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_both_variable_declaration" ):
                return visitor.visitVar_both_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_both_variable_declaration(self):

        localctx = D96Parser.Var_both_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_var_both_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.match(D96Parser.VAR)
            self.state = 289
            self.var_both_declare_initiate_list()
            self.state = 290
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_no_value_assign_declare_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_both_no_value_assign_declare(self):
            return self.getTypedRuleContext(D96Parser.Var_both_no_value_assign_declareContext,0)


        def var_both_no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.Var_both_no_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_both_no_value_assign_declare_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_both_no_value_assign_declare_list" ):
                return visitor.visitVar_both_no_value_assign_declare_list(self)
            else:
                return visitor.visitChildren(self)




    def var_both_no_value_assign_declare_list(self):

        localctx = D96Parser.Var_both_no_value_assign_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_var_both_no_value_assign_declare_list)
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.var_both_no_value_assign_declare()
                self.state = 293
                self.var_both_no_value_assign_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.var_both_no_value_assign_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_no_value_assign_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_both_no_value_assign_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_both_no_value_assign_declare" ):
                return visitor.visitVar_both_no_value_assign_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_both_no_value_assign_declare(self):

        localctx = D96Parser.Var_both_no_value_assign_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_var_both_no_value_assign_declare)
        self._la = 0 # Token type
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 299
                self.match(D96Parser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
                self.match(D96Parser.COLON)
                self.state = 302
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_declare_initiate_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_both_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Var_both_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_var_both_declare_initiate_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_both_declare_initiate_list" ):
                return visitor.visitVar_both_declare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def var_both_declare_initiate_list(self):

        localctx = D96Parser.Var_both_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 306
                self.var_both_type_and_assign()
                self.state = 307
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.variable_in_func_identifier_list()
                self.state = 310
                self.match(D96Parser.COLON)
                self.state = 311
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_type_and_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def var_both_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Var_both_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_both_type_and_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_both_type_and_assign" ):
                return visitor.visitVar_both_type_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_both_type_and_assign(self):

        localctx = D96Parser.Var_both_type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_var_both_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 325
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.match(D96Parser.COMMA)
                self.state = 316
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 317
                self.var_both_type_and_assign()
                self.state = 318
                self.expr()
                self.state = 319
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.match(D96Parser.COLON)
                self.state = 322
                self.variable_type()
                self.state = 323
                self.match(D96Parser.ASSIGNOP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_both_variable_declaration_noinnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_both_variable_declaration_noinnit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_both_variable_declaration_noinnit" ):
                return visitor.visitVal_both_variable_declaration_noinnit(self)
            else:
                return visitor.visitChildren(self)




    def val_both_variable_declaration_noinnit(self):

        localctx = D96Parser.Val_both_variable_declaration_noinnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_val_both_variable_declaration_noinnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.match(D96Parser.VAL)
            self.state = 328
            self.identifier_list()
            self.state = 329
            self.match(D96Parser.COLON)
            self.state = 330
            self.variable_type()
            self.state = 331
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_both_variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def val_both_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Val_both_declare_initiate_listContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_both_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_both_variable_declaration" ):
                return visitor.visitVal_both_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def val_both_variable_declaration(self):

        localctx = D96Parser.Val_both_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_val_both_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(D96Parser.VAL)
            self.state = 334
            self.val_both_declare_initiate_list()
            self.state = 335
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_both_declare_initiate_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def val_both_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Val_both_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_val_both_declare_initiate_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_both_declare_initiate_list" ):
                return visitor.visitVal_both_declare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def val_both_declare_initiate_list(self):

        localctx = D96Parser.Val_both_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_val_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 345
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 338
                self.val_both_type_and_assign()
                self.state = 339
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.variable_in_func_identifier_list()
                self.state = 342
                self.match(D96Parser.COLON)
                self.state = 343
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_both_type_and_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def val_both_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Val_both_type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_both_type_and_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVal_both_type_and_assign" ):
                return visitor.visitVal_both_type_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def val_both_type_and_assign(self):

        localctx = D96Parser.Val_both_type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_val_both_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 357
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.match(D96Parser.COMMA)
                self.state = 348
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 349
                self.val_both_type_and_assign()
                self.state = 350
                self.expr()
                self.state = 351
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(D96Parser.COLON)
                self.state = 354
                self.variable_type()
                self.state = 355
                self.match(D96Parser.ASSIGNOP)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_declaration" ):
                return visitor.visitFunction_declaration(self)
            else:
                return visitor.visitChildren(self)




    def function_declaration(self):

        localctx = D96Parser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 360
            self.match(D96Parser.LB)
            self.state = 361
            self.list_parameters()
            self.state = 362
            self.match(D96Parser.RB)
            self.state = 363
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func_header(self):
            return self.getTypedRuleContext(D96Parser.Call_func_headerContext,0)


        def call_func_attr_list(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attr_listContext,0)


        def call_func_end(self):
            return self.getTypedRuleContext(D96Parser.Call_func_endContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func_statement" ):
                return visitor.visitCall_func_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_func_statement(self):

        localctx = D96Parser.Call_func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.call_func_header()
            self.state = 366
            self.call_func_attr_list()
            self.state = 367
            self.call_func_end()
            self.state = 368
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func_header(self):
            return self.getTypedRuleContext(D96Parser.Call_func_headerContext,0)


        def call_func_attr_list(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attr_listContext,0)


        def call_func_end(self):
            return self.getTypedRuleContext(D96Parser.Call_func_endContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = D96Parser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_call_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.call_func_header()
            self.state = 371
            self.call_func_attr_list()
            self.state = 372
            self.call_func_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_IDENTIFIERS)
            else:
                return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, i)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func_header

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func_header" ):
                return visitor.visitCall_func_header(self)
            else:
                return visitor.visitChildren(self)




    def call_func_header(self):

        localctx = D96Parser.Call_func_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_call_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 375
                self.index_operators(0)
                pass
            elif token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOUBLECOLONOP]:
                self.state = 379
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 380
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass
            elif token in [D96Parser.DOT]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_attr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func_attr(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attrContext,0)


        def call_func_attr_list(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_func_attr_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func_attr_list" ):
                return visitor.visitCall_func_attr_list(self)
            else:
                return visitor.visitChildren(self)




    def call_func_attr_list(self):

        localctx = D96Parser.Call_func_attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_call_func_attr_list)
        try:
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.call_func_attr()
                self.state = 385
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.call_func_attr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_attrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func_attr" ):
                return visitor.visitCall_func_attr(self)
            else:
                return visitor.visitChildren(self)




    def call_func_attr(self):

        localctx = D96Parser.Call_func_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_call_func_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(D96Parser.DOT)
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 392
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 393
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 394
                self.match(D96Parser.LB)
                self.state = 395
                self.value_list()
                self.state = 396
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_endContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func_end

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func_end" ):
                return visitor.visitCall_func_end(self)
            else:
                return visitor.visitChildren(self)




    def call_func_end(self):

        localctx = D96Parser.Call_func_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_call_func_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.match(D96Parser.DOT)
            self.state = 401
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 402
            self.match(D96Parser.LB)
            self.state = 403
            self.value_list()
            self.state = 404
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statements" ):
                return visitor.visitAssignment_statements(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self.lhs()
            self.state = 407
            self.match(D96Parser.ASSIGNOP)
            self.state = 408
            self.expr()
            self.state = 409
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def instance_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_accessContext,0)


        def static_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_accessContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 411
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 412
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.state = 413
                self.static_attr_access()
                pass


            self.state = 418
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 416
                self.index_operators(0)
                pass
            elif token in [D96Parser.ASSIGNOP]:
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_if_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_condition" ):
                return visitor.visitIf_condition(self)
            else:
                return visitor.visitChildren(self)




    def if_condition(self):

        localctx = D96Parser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self.match(D96Parser.LB)
            self.state = 421
            self.expr()
            self.state = 422
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(D96Parser.If_conditionContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statements" ):
                return visitor.visitIf_statements(self)
            else:
                return visitor.visitChildren(self)




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self.match(D96Parser.IF)
            self.state = 425
            self.if_condition()
            self.state = 426
            self.block_statements()
            self.state = 427
            self.elseif_list_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_list_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_statement(self):
            return self.getTypedRuleContext(D96Parser.Elseif_statementContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def else_statement_or_none(self):
            return self.getTypedRuleContext(D96Parser.Else_statement_or_noneContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list_statements" ):
                return visitor.visitElseif_list_statements(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list_statements(self):

        localctx = D96Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_elseif_list_statements)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.elseif_statement()
                self.state = 430
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.elseif_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.else_statement_or_none()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def if_condition(self):
            return self.getTypedRuleContext(D96Parser.If_conditionContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def else_statement_or_none(self):
            return self.getTypedRuleContext(D96Parser.Else_statement_or_noneContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(D96Parser.ELSEIF)
            self.state = 437
            self.if_condition()
            self.state = 438
            self.block_statements()
            self.state = 439
            self.else_statement_or_none()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statement_or_noneContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement_or_none

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement_or_none" ):
                return visitor.visitElse_statement_or_none(self)
            else:
                return visitor.visitChildren(self)




    def else_statement_or_none(self):

        localctx = D96Parser.Else_statement_or_noneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_else_statement_or_none)
        try:
            self.state = 443
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.else_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElse_statement" ):
                return visitor.visitElse_statement(self)
            else:
                return visitor.visitChildren(self)




    def else_statement(self):

        localctx = D96Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.ELSE)
            self.state = 446
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class By_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_by_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBy_expr" ):
                return visitor.visitBy_expr(self)
            else:
                return visitor.visitChildren(self)




    def by_expr(self):

        localctx = D96Parser.By_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_by_expr)
        try:
            self.state = 451
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(D96Parser.BY)
                self.state = 449
                self.expr()
                pass
            elif token in [D96Parser.RB]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forin_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def DOUBLEDOTOP(self):
            return self.getToken(D96Parser.DOUBLEDOTOP, 0)

        def by_expr(self):
            return self.getTypedRuleContext(D96Parser.By_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_forin_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForin_statements" ):
                return visitor.visitForin_statements(self)
            else:
                return visitor.visitChildren(self)




    def forin_statements(self):

        localctx = D96Parser.Forin_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(D96Parser.FOREACH)
            self.state = 454
            self.match(D96Parser.LB)
            self.state = 455
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 456
            self.match(D96Parser.IN)
            self.state = 457
            self.expr()
            self.state = 458
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 459
            self.expr()
            self.state = 460
            self.by_expr()
            self.state = 461
            self.match(D96Parser.RB)
            self.state = 462
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attr_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr_access" ):
                return visitor.visitInstance_attr_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr_access(self):

        localctx = D96Parser.Instance_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 464
            self.expr()
            self.state = 465
            self.match(D96Parser.DOT)
            self.state = 466
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_method_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_access" ):
                return visitor.visitInstance_method_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_access(self):

        localctx = D96Parser.Instance_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_instance_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.expr()
            self.state = 469
            self.match(D96Parser.DOT)
            self.state = 470
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 471
            self.match(D96Parser.LB)
            self.state = 472
            self.list_expr()
            self.state = 473
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attr_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def DOLLAR_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_IDENTIFIERS)
            else:
                return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, i)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr_access" ):
                return visitor.visitStatic_attr_access(self)
            else:
                return visitor.visitChildren(self)




    def static_attr_access(self):

        localctx = D96Parser.Static_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 476
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 477
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def DOLLAR_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.DOLLAR_IDENTIFIERS)
            else:
                return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, i)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_access" ):
                return visitor.visitStatic_method_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_access(self):

        localctx = D96Parser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 480
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 481
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 482
            self.match(D96Parser.LB)
            self.state = 483
            self.list_expr()
            self.state = 484
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_method_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_accessContext,0)


        def static_method_access(self):
            return self.getTypedRuleContext(D96Parser.Static_method_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation" ):
                return visitor.visitMethod_invocation(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation(self):

        localctx = D96Parser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_method_invocation)
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
                self.static_method_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method_invocation(self):
            return self.getTypedRuleContext(D96Parser.Method_invocationContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_method_invocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod_invocation_statement" ):
                return visitor.visitMethod_invocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.method_invocation()
            self.state = 491
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_break_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statements" ):
                return visitor.visitBreak_statements(self)
            else:
                return visitor.visitChildren(self)




    def break_statements(self):

        localctx = D96Parser.Break_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(D96Parser.BREAK)
            self.state = 494
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_continue_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statements" ):
                return visitor.visitContinue_statements(self)
            else:
                return visitor.visitChildren(self)




    def continue_statements(self):

        localctx = D96Parser.Continue_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.match(D96Parser.CONTINUE)
            self.state = 497
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_expr" ):
                return visitor.visitReturn_expr(self)
            else:
                return visitor.visitChildren(self)




    def return_expr(self):

        localctx = D96Parser.Return_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_return_expr)
        try:
            self.state = 501
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.expr()
                pass
            elif token in [D96Parser.SEMICOLON]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def return_expr(self):
            return self.getTypedRuleContext(D96Parser.Return_exprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_return_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statements" ):
                return visitor.visitReturn_statements(self)
            else:
                return visitor.visitChildren(self)




    def return_statements(self):

        localctx = D96Parser.Return_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.RETURN)
            self.state = 504
            self.return_expr()
            self.state = 505
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_class_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statements_class(self):
            return self.getTypedRuleContext(D96Parser.Statements_classContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_class_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_class_statements" ):
                return visitor.visitBlock_class_statements(self)
            else:
                return visitor.visitChildren(self)




    def block_class_statements(self):

        localctx = D96Parser.Block_class_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(D96Parser.LCB)
            self.state = 508
            self.statements_class()
            self.state = 509
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statements" ):
                return visitor.visitBlock_statements(self)
            else:
                return visitor.visitChildren(self)




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(D96Parser.LCB)
            self.state = 512
            self.statements()
            self.state = 513
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement_class(self):
            return self.getTypedRuleContext(D96Parser.Statement_classContext,0)


        def statements_class(self):
            return self.getTypedRuleContext(D96Parser.Statements_classContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements_class" ):
                return visitor.visitStatements_class(self)
            else:
                return visitor.visitChildren(self)




    def statements_class(self):

        localctx = D96Parser.Statements_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_statements_class)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.statement_class()
                self.state = 516
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.statement_class()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(D96Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatements" ):
                return visitor.visitStatements(self)
            else:
                return visitor.visitChildren(self)




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_statements)
        try:
            self.state = 527
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.statement()
                self.state = 523
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
                self.statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statement_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_both_variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Var_both_variable_declarationContext,0)


        def val_both_variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Val_both_variable_declarationContext,0)


        def var_both_variable_declaration_noinnit(self):
            return self.getTypedRuleContext(D96Parser.Var_both_variable_declaration_noinnitContext,0)


        def val_both_variable_declaration_noinnit(self):
            return self.getTypedRuleContext(D96Parser.Val_both_variable_declaration_noinnitContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(D96Parser.Function_declarationContext,0)


        def constructor_dclr(self):
            return self.getTypedRuleContext(D96Parser.Constructor_dclrContext,0)


        def destructor_dclr(self):
            return self.getTypedRuleContext(D96Parser.Destructor_dclrContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_class" ):
                return visitor.visitStatement_class(self)
            else:
                return visitor.visitChildren(self)




    def statement_class(self):

        localctx = D96Parser.Statement_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_statement_class)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.var_both_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
                self.val_both_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 531
                self.var_both_variable_declaration_noinnit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 532
                self.val_both_variable_declaration_noinnit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 533
                self.function_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 534
                self.constructor_dclr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 535
                self.destructor_dclr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Var_variable_declarationContext,0)


        def val_variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Val_variable_declarationContext,0)


        def var_variable_declaration_noinit(self):
            return self.getTypedRuleContext(D96Parser.Var_variable_declaration_noinitContext,0)


        def val_variable_declaration_noinit(self):
            return self.getTypedRuleContext(D96Parser.Val_variable_declaration_noinitContext,0)


        def assignment_statements(self):
            return self.getTypedRuleContext(D96Parser.Assignment_statementsContext,0)


        def if_statements(self):
            return self.getTypedRuleContext(D96Parser.If_statementsContext,0)


        def forin_statements(self):
            return self.getTypedRuleContext(D96Parser.Forin_statementsContext,0)


        def call_func_statement(self):
            return self.getTypedRuleContext(D96Parser.Call_func_statementContext,0)


        def method_invocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Method_invocation_statementContext,0)


        def break_statements(self):
            return self.getTypedRuleContext(D96Parser.Break_statementsContext,0)


        def continue_statements(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementsContext,0)


        def return_statements(self):
            return self.getTypedRuleContext(D96Parser.Return_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_statement)
        try:
            self.state = 552
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 538
                self.var_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 539
                self.val_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 540
                self.var_variable_declaration_noinit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 541
                self.val_variable_declaration_noinit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 542
                self.assignment_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 543
                self.val_variable_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 544
                self.assignment_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 545
                self.if_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 546
                self.forin_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 547
                self.call_func_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 548
                self.method_invocation_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 549
                self.break_statements()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 550
                self.continue_statements()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 551
                self.return_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr1Context,i)


        def STRCONCATOP(self):
            return self.getToken(D96Parser.STRCONCATOP, 0)

        def STREQUALOP(self):
            return self.getToken(D96Parser.STREQUALOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.expr1()
                self.state = 555
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 556
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 558
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(D96Parser.Expr2Context,i)


        def EQUALOP(self):
            return self.getToken(D96Parser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(D96Parser.NOTEQUALOP, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
                self.expr2(0)
                self.state = 562
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 563
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
                self.expr2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(D96Parser.Expr2Context,0)


        def ANDOP(self):
            return self.getToken(D96Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(D96Parser.OROP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 576
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 571
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 572
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 573
                    self.expr3(0) 
                self.state = 578
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(D96Parser.Expr3Context,0)


        def PLUSOP(self):
            return self.getToken(D96Parser.PLUSOP, 0)

        def MINUSOP(self):
            return self.getToken(D96Parser.MINUSOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 587
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 582
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 583
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 584
                    self.expr4(0) 
                self.state = 589
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(D96Parser.Expr4Context,0)


        def MULTIPLYOP(self):
            return self.getToken(D96Parser.MULTIPLYOP, 0)

        def DIVIDEOP(self):
            return self.getToken(D96Parser.DIVIDEOP, 0)

        def MODULOOP(self):
            return self.getToken(D96Parser.MODULOOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 598
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 593
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 594
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 595
                    self.expr5() 
                self.state = 600
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOTOP(self):
            return self.getToken(D96Parser.NOTOP, 0)

        def expr5(self):
            return self.getTypedRuleContext(D96Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_expr5)
        try:
            self.state = 604
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                self.match(D96Parser.NOTOP)
                self.state = 602
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 603
                self.expr6()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUSOP(self):
            return self.getToken(D96Parser.MINUSOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(D96Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_expr6)
        try:
            self.state = 609
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 606
                self.match(D96Parser.MINUSOP)
                self.state = 607
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
                self.expr7(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 618
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 614
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 615
                    self.index_operators(0) 
                self.state = 620
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def instance_accesses(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr8" ):
                return visitor.visitExpr8(self)
            else:
                return visitor.visitChildren(self)



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 628
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 624
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 625
                    self.instance_accesses() 
                self.state = 630
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def static_accesses(self):
            return self.getTypedRuleContext(D96Parser.Static_accessesContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_expr9)
        try:
            self.state = 634
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 631
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 632
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 633
                self.expr10()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expr11(self):
            return self.getTypedRuleContext(D96Parser.Expr11Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr10" ):
                return visitor.visitExpr10(self)
            else:
                return visitor.visitChildren(self)




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_expr10)
        try:
            self.state = 643
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.match(D96Parser.NEW)
                self.state = 637
                self.expr()
                self.state = 638
                self.match(D96Parser.LB)
                self.state = 639
                self.list_expr()
                self.state = 640
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self.expr11()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def expr12(self):
            return self.getTypedRuleContext(D96Parser.Expr12Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_expr11)
        try:
            self.state = 649
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 645
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 647
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 648
                self.expr12()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr12Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr12

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr12" ):
                return visitor.visitExpr12(self)
            else:
                return visitor.visitChildren(self)




    def expr12(self):

        localctx = D96Parser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 651
            self.match(D96Parser.LB)
            self.state = 652
            self.expr()
            self.state = 653
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_operators

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_operators" ):
                return visitor.visitIndex_operators(self)
            else:
                return visitor.visitChildren(self)



    def index_operators(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operatorsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 142
        self.enterRecursionRule(localctx, 142, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 656
            self.match(D96Parser.LSB)
            self.state = 657
            self.expr()
            self.state = 658
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 667
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 660
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 661
                    self.match(D96Parser.LSB)
                    self.state = 662
                    self.expr()
                    self.state = 663
                    self.match(D96Parser.RSB) 
                self.state = 669
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Index_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex_expr" ):
                return visitor.visitIndex_expr(self)
            else:
                return visitor.visitChildren(self)




    def index_expr(self):

        localctx = D96Parser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_index_expr)
        try:
            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 670
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.index()
                self.state = 672
                self.index_operators(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def instance_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIndex" ):
                return visitor.visitIndex(self)
            else:
                return visitor.visitChildren(self)




    def index(self):

        localctx = D96Parser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 682
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 676
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 677
                self.expr()
                self.state = 678
                self.instance_attr_access()
                self.state = 679
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_accessesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instance_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessContext,0)


        def instance_accesses(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_instance_accesses

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_accesses" ):
                return visitor.visitInstance_accesses(self)
            else:
                return visitor.visitChildren(self)




    def instance_accesses(self):

        localctx = D96Parser.Instance_accessesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_instance_accesses)
        try:
            self.state = 688
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 684
                self.instance_access()
                self.state = 685
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 687
                self.instance_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_access" ):
                return visitor.visitInstance_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_access(self):

        localctx = D96Parser.Instance_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_instance_access)
        try:
            self.state = 698
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 690
                self.match(D96Parser.DOT)
                self.state = 691
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 692
                self.match(D96Parser.DOT)
                self.state = 693
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 694
                self.match(D96Parser.LB)
                self.state = 695
                self.list_expr()
                self.state = 696
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_accessesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access(self):
            return self.getTypedRuleContext(D96Parser.Static_accessContext,0)


        def static_accesses(self):
            return self.getTypedRuleContext(D96Parser.Static_accessesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_accesses

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_accesses" ):
                return visitor.visitStatic_accesses(self)
            else:
                return visitor.visitChildren(self)




    def static_accesses(self):

        localctx = D96Parser.Static_accessesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_static_accesses)
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 700
                self.static_access()
                self.state = 701
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 703
                self.static_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_access" ):
                return visitor.visitStatic_access(self)
            else:
                return visitor.visitChildren(self)




    def static_access(self):

        localctx = D96Parser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_static_access)
        try:
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 706
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 707
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 708
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 709
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 710
                self.match(D96Parser.LB)
                self.state = 711
                self.list_expr()
                self.state = 712
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expr" ):
                return visitor.visitList_expr(self)
            else:
                return visitor.visitChildren(self)




    def list_expr(self):

        localctx = D96Parser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_list_expr)
        try:
            self.state = 722
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.expr()
                self.state = 717
                self.match(D96Parser.COMMA)
                self.state = 718
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 720
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def array_val(self):
            return self.getTypedRuleContext(D96Parser.Array_valContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_lit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_lit" ):
                return visitor.visitArray_lit(self)
            else:
                return visitor.visitChildren(self)




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 724
            self.match(D96Parser.ARRAY)
            self.state = 725
            self.match(D96Parser.LB)
            self.state = 726
            self.array_val()
            self.state = 727
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def array_val(self):
            return self.getTypedRuleContext(D96Parser.Array_valContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_array_val

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_val" ):
                return visitor.visitArray_val(self)
            else:
                return visitor.visitChildren(self)




    def array_val(self):

        localctx = D96Parser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_array_val)
        try:
            self.state = 735
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.expr()
                self.state = 730
                self.match(D96Parser.COMMA)
                self.state = 731
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 733
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT_IN_ARRAY(self):
            return self.getToken(D96Parser.INTLIT_IN_ARRAY, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(D96Parser.STRINGLIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(D96Parser.Array_litContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_literal)
        try:
            self.state = 743
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 737
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 738
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 739
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 740
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 741
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 742
                self.array_lit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_parametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(D96Parser.ParamContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_parameters

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_parameters" ):
                return visitor.visitList_parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_parameters(self):

        localctx = D96Parser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_list_parameters)
        try:
            self.state = 751
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 745
                self.param()
                self.state = 746
                self.match(D96Parser.SEMICOLON)
                self.state = 747
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 749
                self.param()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 753
            self.identifier_list()
            self.state = 754
            self.match(D96Parser.COLON)
            self.state = 755
            self.variable_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier_list" ):
                return visitor.visitIdentifier_list(self)
            else:
                return visitor.visitChildren(self)




    def identifier_list(self):

        localctx = D96Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 762
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 757
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 758
                self.match(D96Parser.COMMA)
                self.state = 759
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 760
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_in_func_identifier_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_in_func_identifier_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_in_func_identifier_list" ):
                return visitor.visitVariable_in_func_identifier_list(self)
            else:
                return visitor.visitChildren(self)




    def variable_in_func_identifier_list(self):

        localctx = D96Parser.Variable_in_func_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 769
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 764
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 765
                self.match(D96Parser.COMMA)
                self.state = 766
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 767
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Value_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_value_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_list" ):
                return visitor.visitValue_list(self)
            else:
                return visitor.visitChildren(self)




    def value_list(self):

        localctx = D96Parser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_value_list)
        try:
            self.state = 783
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 773
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 771
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 772
                    self.expr()
                    pass


                self.state = 775
                self.match(D96Parser.COMMA)
                self.state = 776
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 780
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 778
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 779
                    self.expr()
                    pass


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def array_element_type(self):
            return self.getTypedRuleContext(D96Parser.Array_element_typeContext,0)


        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def INTLIT_IN_ARRAY(self):
            return self.getToken(D96Parser.INTLIT_IN_ARRAY, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_type" ):
                return visitor.visitArray_type(self)
            else:
                return visitor.visitChildren(self)




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 785
            self.match(D96Parser.ARRAY)
            self.state = 786
            self.match(D96Parser.LSB)
            self.state = 787
            self.array_element_type()
            self.state = 788
            self.match(D96Parser.COMMA)
            self.state = 789
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 790
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_element_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_element_type" ):
                return visitor.visitArray_element_type(self)
            else:
                return visitor.visitChildren(self)




    def array_element_type(self):

        localctx = D96Parser.Array_element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_array_element_type)
        try:
            self.state = 797
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 792
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 793
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 794
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 795
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 796
                self.match(D96Parser.STRING)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 799
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INT) | (1 << D96Parser.FLOAT) | (1 << D96Parser.BOOLEAN) | (1 << D96Parser.STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_type" ):
                return visitor.visitVariable_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_type(self):

        localctx = D96Parser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_variable_type)
        try:
            self.state = 804
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 801
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 802
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 803
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[60] = self.expr2_sempred
        self._predicates[61] = self.expr3_sempred
        self._predicates[62] = self.expr4_sempred
        self._predicates[65] = self.expr7_sempred
        self._predicates[66] = self.expr8_sempred
        self._predicates[71] = self.index_operators_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr8_sempred(self, localctx:Expr8Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def index_operators_sempred(self, localctx:Index_operatorsContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




