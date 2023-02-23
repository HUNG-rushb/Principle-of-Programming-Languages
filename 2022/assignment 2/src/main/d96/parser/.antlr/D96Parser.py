# Generated from d:\Github\Principle-of-Programming-Languages\2022\assignment 2\src\main\d96\parser\D96.g4 by ANTLR 4.9.2
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
        buf.write("\u028d\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\5\3\u009e\n\3\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\5\3\5\3\5\5\5\u00a8\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00cc\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00e4\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u00fc\n\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0114\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\5\26\u0123\n\26\3\27\3\27\3\27\5\27\u0128\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\5\31\u0134\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\5\33\u0140\n\33\3\34\3\34\3\34\5\34\u0145")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\5\"\u016a")
        buf.write("\n\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\5&\u0177\n&\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\5")
        buf.write("*\u018a\n*\3+\3+\3+\3+\3+\5+\u0191\n+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u019a\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01a7")
        buf.write("\n-\3.\3.\3.\3.\3.\5.\u01ae\n.\3/\3/\3/\3/\3/\5/\u01b5")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01bd\n\60\f\60")
        buf.write("\16\60\u01c0\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u01c8\n\61\f\61\16\61\u01cb\13\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u01d3\n\62\f\62\16\62\u01d6\13\62\3\63")
        buf.write("\3\63\3\63\5\63\u01db\n\63\3\64\3\64\3\64\5\64\u01e0\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\7\65\u01e7\n\65\f\65\16\65")
        buf.write("\u01ea\13\65\3\66\3\66\3\66\3\66\3\66\7\66\u01f1\n\66")
        buf.write("\f\66\16\66\u01f4\13\66\3\67\3\67\5\67\u01f8\n\67\38\3")
        buf.write("8\38\38\38\38\38\58\u0201\n8\39\39\39\39\59\u0207\n9\3")
        buf.write(":\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u0216\n;\3<\3")
        buf.write("<\3<\3<\5<\u021c\n<\3=\3=\3=\3=\3=\3=\3=\3=\5=\u0226\n")
        buf.write("=\3>\3>\3>\3>\3>\3>\3>\3>\3>\5>\u0231\n>\3?\3?\3?\3?\3")
        buf.write("?\3?\5?\u0239\n?\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\5A\u0246")
        buf.write("\nA\3B\3B\3B\3B\3B\3B\5B\u024e\nB\3C\3C\3C\3C\3C\3C\5")
        buf.write("C\u0256\nC\3D\3D\3D\3D\3E\3E\3E\3E\3E\5E\u0261\nE\3F\3")
        buf.write("F\3F\3F\3F\5F\u0268\nF\3G\3G\5G\u026c\nG\3G\3G\3G\3G\3")
        buf.write("G\5G\u0273\nG\3G\5G\u0276\nG\3H\3H\3H\3H\3H\3H\3H\3I\3")
        buf.write("I\3I\3I\3I\5I\u0284\nI\3J\3J\3K\3K\3K\5K\u028b\nK\3K\2")
        buf.write("\7^`bhjL\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\2\t\3\29:\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"")
        buf.write("\3\2\16\21\2\u0290\2\u0096\3\2\2\2\4\u009d\3\2\2\2\6\u009f")
        buf.write("\3\2\2\2\b\u00a7\3\2\2\2\n\u00a9\3\2\2\2\f\u00af\3\2\2")
        buf.write("\2\16\u00b5\3\2\2\2\20\u00bb\3\2\2\2\22\u00cb\3\2\2\2")
        buf.write("\24\u00cd\3\2\2\2\26\u00d3\3\2\2\2\30\u00e3\3\2\2\2\32")
        buf.write("\u00e5\3\2\2\2\34\u00eb\3\2\2\2\36\u00fb\3\2\2\2 \u00fd")
        buf.write("\3\2\2\2\"\u0103\3\2\2\2$\u0113\3\2\2\2&\u0115\3\2\2\2")
        buf.write("(\u011b\3\2\2\2*\u0122\3\2\2\2,\u0127\3\2\2\2.\u0129\3")
        buf.write("\2\2\2\60\u0133\3\2\2\2\62\u0135\3\2\2\2\64\u013f\3\2")
        buf.write("\2\2\66\u0144\3\2\2\28\u0146\3\2\2\2:\u0151\3\2\2\2<\u0155")
        buf.write("\3\2\2\2>\u015c\3\2\2\2@\u0160\3\2\2\2B\u0169\3\2\2\2")
        buf.write("D\u016b\3\2\2\2F\u016e\3\2\2\2H\u0171\3\2\2\2J\u0176\3")
        buf.write("\2\2\2L\u0178\3\2\2\2N\u017c\3\2\2\2P\u0180\3\2\2\2R\u0189")
        buf.write("\3\2\2\2T\u0190\3\2\2\2V\u0199\3\2\2\2X\u01a6\3\2\2\2")
        buf.write("Z\u01ad\3\2\2\2\\\u01b4\3\2\2\2^\u01b6\3\2\2\2`\u01c1")
        buf.write("\3\2\2\2b\u01cc\3\2\2\2d\u01da\3\2\2\2f\u01df\3\2\2\2")
        buf.write("h\u01e1\3\2\2\2j\u01eb\3\2\2\2l\u01f7\3\2\2\2n\u0200\3")
        buf.write("\2\2\2p\u0206\3\2\2\2r\u0208\3\2\2\2t\u0215\3\2\2\2v\u021b")
        buf.write("\3\2\2\2x\u0225\3\2\2\2z\u0227\3\2\2\2|\u0238\3\2\2\2")
        buf.write("~\u023a\3\2\2\2\u0080\u0245\3\2\2\2\u0082\u024d\3\2\2")
        buf.write("\2\u0084\u0255\3\2\2\2\u0086\u0257\3\2\2\2\u0088\u0260")
        buf.write("\3\2\2\2\u008a\u0267\3\2\2\2\u008c\u0275\3\2\2\2\u008e")
        buf.write("\u0277\3\2\2\2\u0090\u0283\3\2\2\2\u0092\u0285\3\2\2\2")
        buf.write("\u0094\u028a\3\2\2\2\u0096\u0097\5\4\3\2\u0097\u0098\7")
        buf.write("\2\2\3\u0098\3\3\2\2\2\u0099\u009a\5\6\4\2\u009a\u009b")
        buf.write("\5\4\3\2\u009b\u009e\3\2\2\2\u009c\u009e\5\6\4\2\u009d")
        buf.write("\u0099\3\2\2\2\u009d\u009c\3\2\2\2\u009e\5\3\2\2\2\u009f")
        buf.write("\u00a0\7\24\2\2\u00a0\u00a1\79\2\2\u00a1\u00a2\5\b\5\2")
        buf.write("\u00a2\u00a3\5N(\2\u00a3\7\3\2\2\2\u00a4\u00a5\7\67\2")
        buf.write("\2\u00a5\u00a8\79\2\2\u00a6\u00a8\3\2\2\2\u00a7\u00a4")
        buf.write("\3\2\2\2\u00a7\u00a6\3\2\2\2\u00a8\t\3\2\2\2\u00a9\u00aa")
        buf.write("\7\27\2\2\u00aa\u00ab\7/\2\2\u00ab\u00ac\5\u0084C\2\u00ac")
        buf.write("\u00ad\7\60\2\2\u00ad\u00ae\5P)\2\u00ae\13\3\2\2\2\u00af")
        buf.write("\u00b0\7\30\2\2\u00b0\u00b1\7/\2\2\u00b1\u00b2\5\u0084")
        buf.write("C\2\u00b2\u00b3\7\60\2\2\u00b3\u00b4\5P)\2\u00b4\r\3\2")
        buf.write("\2\2\u00b5\u00b6\7\26\2\2\u00b6\u00b7\5\u008aF\2\u00b7")
        buf.write("\u00b8\7\67\2\2\u00b8\u00b9\5\u0094K\2\u00b9\u00ba\78")
        buf.write("\2\2\u00ba\17\3\2\2\2\u00bb\u00bc\7\26\2\2\u00bc\u00bd")
        buf.write("\79\2\2\u00bd\u00be\5\22\n\2\u00be\u00bf\5Z.\2\u00bf\u00c0")
        buf.write("\78\2\2\u00c0\21\3\2\2\2\u00c1\u00c2\7\66\2\2\u00c2\u00c3")
        buf.write("\79\2\2\u00c3\u00c4\5\22\n\2\u00c4\u00c5\5Z.\2\u00c5\u00c6")
        buf.write("\7\66\2\2\u00c6\u00cc\3\2\2\2\u00c7\u00c8\7\67\2\2\u00c8")
        buf.write("\u00c9\5\u0094K\2\u00c9\u00ca\7\'\2\2\u00ca\u00cc\3\2")
        buf.write("\2\2\u00cb\u00c1\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc\23")
        buf.write("\3\2\2\2\u00cd\u00ce\7\25\2\2\u00ce\u00cf\5\u008aF\2\u00cf")
        buf.write("\u00d0\7\67\2\2\u00d0\u00d1\5\u0094K\2\u00d1\u00d2\78")
        buf.write("\2\2\u00d2\25\3\2\2\2\u00d3\u00d4\7\25\2\2\u00d4\u00d5")
        buf.write("\79\2\2\u00d5\u00d6\5\30\r\2\u00d6\u00d7\5Z.\2\u00d7\u00d8")
        buf.write("\78\2\2\u00d8\27\3\2\2\2\u00d9\u00da\7\66\2\2\u00da\u00db")
        buf.write("\79\2\2\u00db\u00dc\5\30\r\2\u00dc\u00dd\5Z.\2\u00dd\u00de")
        buf.write("\7\66\2\2\u00de\u00e4\3\2\2\2\u00df\u00e0\7\67\2\2\u00e0")
        buf.write("\u00e1\5\u0094K\2\u00e1\u00e2\7\'\2\2\u00e2\u00e4\3\2")
        buf.write("\2\2\u00e3\u00d9\3\2\2\2\u00e3\u00df\3\2\2\2\u00e4\31")
        buf.write("\3\2\2\2\u00e5\u00e6\7\26\2\2\u00e6\u00e7\5\u0088E\2\u00e7")
        buf.write("\u00e8\7\67\2\2\u00e8\u00e9\5\u0094K\2\u00e9\u00ea\78")
        buf.write("\2\2\u00ea\33\3\2\2\2\u00eb\u00ec\7\26\2\2\u00ec\u00ed")
        buf.write("\t\2\2\2\u00ed\u00ee\5\36\20\2\u00ee\u00ef\5Z.\2\u00ef")
        buf.write("\u00f0\78\2\2\u00f0\35\3\2\2\2\u00f1\u00f2\7\66\2\2\u00f2")
        buf.write("\u00f3\t\2\2\2\u00f3\u00f4\5\36\20\2\u00f4\u00f5\5Z.\2")
        buf.write("\u00f5\u00f6\7\66\2\2\u00f6\u00fc\3\2\2\2\u00f7\u00f8")
        buf.write("\7\67\2\2\u00f8\u00f9\5\u0094K\2\u00f9\u00fa\7\'\2\2\u00fa")
        buf.write("\u00fc\3\2\2\2\u00fb\u00f1\3\2\2\2\u00fb\u00f7\3\2\2\2")
        buf.write("\u00fc\37\3\2\2\2\u00fd\u00fe\7\25\2\2\u00fe\u00ff\5\u0088")
        buf.write("E\2\u00ff\u0100\7\67\2\2\u0100\u0101\5\u0094K\2\u0101")
        buf.write("\u0102\78\2\2\u0102!\3\2\2\2\u0103\u0104\7\25\2\2\u0104")
        buf.write("\u0105\t\2\2\2\u0105\u0106\5$\23\2\u0106\u0107\5Z.\2\u0107")
        buf.write("\u0108\78\2\2\u0108#\3\2\2\2\u0109\u010a\7\66\2\2\u010a")
        buf.write("\u010b\t\2\2\2\u010b\u010c\5$\23\2\u010c\u010d\5Z.\2\u010d")
        buf.write("\u010e\7\66\2\2\u010e\u0114\3\2\2\2\u010f\u0110\7\67\2")
        buf.write("\2\u0110\u0111\5\u0094K\2\u0111\u0112\7\'\2\2\u0112\u0114")
        buf.write("\3\2\2\2\u0113\u0109\3\2\2\2\u0113\u010f\3\2\2\2\u0114")
        buf.write("%\3\2\2\2\u0115\u0116\t\2\2\2\u0116\u0117\7/\2\2\u0117")
        buf.write("\u0118\5\u0084C\2\u0118\u0119\7\60\2\2\u0119\u011a\5P")
        buf.write(")\2\u011a\'\3\2\2\2\u011b\u011c\5*\26\2\u011c\u011d\7")
        buf.write("\'\2\2\u011d\u011e\5Z.\2\u011e\u011f\78\2\2\u011f)\3\2")
        buf.write("\2\2\u0120\u0123\5,\27\2\u0121\u0123\5h\65\2\u0122\u0120")
        buf.write("\3\2\2\2\u0122\u0121\3\2\2\2\u0123+\3\2\2\2\u0124\u0128")
        buf.write("\79\2\2\u0125\u0128\5:\36\2\u0126\u0128\5> \2\u0127\u0124")
        buf.write("\3\2\2\2\u0127\u0125\3\2\2\2\u0127\u0126\3\2\2\2\u0128")
        buf.write("-\3\2\2\2\u0129\u012a\7\5\2\2\u012a\u012b\7/\2\2\u012b")
        buf.write("\u012c\5Z.\2\u012c\u012d\7\60\2\2\u012d\u012e\5P)\2\u012e")
        buf.write("\u012f\5\60\31\2\u012f/\3\2\2\2\u0130\u0134\5\62\32\2")
        buf.write("\u0131\u0134\5\64\33\2\u0132\u0134\3\2\2\2\u0133\u0130")
        buf.write("\3\2\2\2\u0133\u0131\3\2\2\2\u0133\u0132\3\2\2\2\u0134")
        buf.write("\61\3\2\2\2\u0135\u0136\7\6\2\2\u0136\u0137\7/\2\2\u0137")
        buf.write("\u0138\5Z.\2\u0138\u0139\7\60\2\2\u0139\u013a\5P)\2\u013a")
        buf.write("\u013b\5\60\31\2\u013b\63\3\2\2\2\u013c\u013d\7\7\2\2")
        buf.write("\u013d\u0140\5P)\2\u013e\u0140\3\2\2\2\u013f\u013c\3\2")
        buf.write("\2\2\u013f\u013e\3\2\2\2\u0140\65\3\2\2\2\u0141\u0142")
        buf.write("\7\32\2\2\u0142\u0145\5Z.\2\u0143\u0145\3\2\2\2\u0144")
        buf.write("\u0141\3\2\2\2\u0144\u0143\3\2\2\2\u0145\67\3\2\2\2\u0146")
        buf.write("\u0147\7\b\2\2\u0147\u0148\7/\2\2\u0148\u0149\t\2\2\2")
        buf.write("\u0149\u014a\7\r\2\2\u014a\u014b\5Z.\2\u014b\u014c\7\35")
        buf.write("\2\2\u014c\u014d\5Z.\2\u014d\u014e\5\66\34\2\u014e\u014f")
        buf.write("\7\60\2\2\u014f\u0150\5P)\2\u01509\3\2\2\2\u0151\u0152")
        buf.write("\5Z.\2\u0152\u0153\7\65\2\2\u0153\u0154\79\2\2\u0154;")
        buf.write("\3\2\2\2\u0155\u0156\5Z.\2\u0156\u0157\7\65\2\2\u0157")
        buf.write("\u0158\79\2\2\u0158\u0159\7/\2\2\u0159\u015a\5|?\2\u015a")
        buf.write("\u015b\7\60\2\2\u015b=\3\2\2\2\u015c\u015d\t\2\2\2\u015d")
        buf.write("\u015e\7\34\2\2\u015e\u015f\7:\2\2\u015f?\3\2\2\2\u0160")
        buf.write("\u0161\t\2\2\2\u0161\u0162\7\34\2\2\u0162\u0163\7:\2\2")
        buf.write("\u0163\u0164\7/\2\2\u0164\u0165\5|?\2\u0165\u0166\7\60")
        buf.write("\2\2\u0166A\3\2\2\2\u0167\u016a\5<\37\2\u0168\u016a\5")
        buf.write("@!\2\u0169\u0167\3\2\2\2\u0169\u0168\3\2\2\2\u016aC\3")
        buf.write("\2\2\2\u016b\u016c\5B\"\2\u016c\u016d\78\2\2\u016dE\3")
        buf.write("\2\2\2\u016e\u016f\7\3\2\2\u016f\u0170\78\2\2\u0170G\3")
        buf.write("\2\2\2\u0171\u0172\7\4\2\2\u0172\u0173\78\2\2\u0173I\3")
        buf.write("\2\2\2\u0174\u0177\5Z.\2\u0175\u0177\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177K\3\2\2\2\u0178\u0179")
        buf.write("\7\22\2\2\u0179\u017a\5J&\2\u017a\u017b\78\2\2\u017bM")
        buf.write("\3\2\2\2\u017c\u017d\7\63\2\2\u017d\u017e\5R*\2\u017e")
        buf.write("\u017f\7\64\2\2\u017fO\3\2\2\2\u0180\u0181\7\63\2\2\u0181")
        buf.write("\u0182\5T+\2\u0182\u0183\7\64\2\2\u0183Q\3\2\2\2\u0184")
        buf.write("\u0185\5V,\2\u0185\u0186\5R*\2\u0186\u018a\3\2\2\2\u0187")
        buf.write("\u018a\5V,\2\u0188\u018a\3\2\2\2\u0189\u0184\3\2\2\2\u0189")
        buf.write("\u0187\3\2\2\2\u0189\u0188\3\2\2\2\u018aS\3\2\2\2\u018b")
        buf.write("\u018c\5X-\2\u018c\u018d\5T+\2\u018d\u0191\3\2\2\2\u018e")
        buf.write("\u0191\5X-\2\u018f\u0191\3\2\2\2\u0190\u018b\3\2\2\2\u0190")
        buf.write("\u018e\3\2\2\2\u0190\u018f\3\2\2\2\u0191U\3\2\2\2\u0192")
        buf.write("\u019a\5\34\17\2\u0193\u019a\5\"\22\2\u0194\u019a\5\32")
        buf.write("\16\2\u0195\u019a\5 \21\2\u0196\u019a\5&\24\2\u0197\u019a")
        buf.write("\5\n\6\2\u0198\u019a\5\f\7\2\u0199\u0192\3\2\2\2\u0199")
        buf.write("\u0193\3\2\2\2\u0199\u0194\3\2\2\2\u0199\u0195\3\2\2\2")
        buf.write("\u0199\u0196\3\2\2\2\u0199\u0197\3\2\2\2\u0199\u0198\3")
        buf.write("\2\2\2\u019aW\3\2\2\2\u019b\u01a7\5\20\t\2\u019c\u01a7")
        buf.write("\5\26\f\2\u019d\u01a7\5\16\b\2\u019e\u01a7\5\24\13\2\u019f")
        buf.write("\u01a7\5(\25\2\u01a0\u01a7\5.\30\2\u01a1\u01a7\58\35\2")
        buf.write("\u01a2\u01a7\5D#\2\u01a3\u01a7\5F$\2\u01a4\u01a7\5H%\2")
        buf.write("\u01a5\u01a7\5L\'\2\u01a6\u019b\3\2\2\2\u01a6\u019c\3")
        buf.write("\2\2\2\u01a6\u019d\3\2\2\2\u01a6\u019e\3\2\2\2\u01a6\u019f")
        buf.write("\3\2\2\2\u01a6\u01a0\3\2\2\2\u01a6\u01a1\3\2\2\2\u01a6")
        buf.write("\u01a2\3\2\2\2\u01a6\u01a3\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a5\3\2\2\2\u01a7Y\3\2\2\2\u01a8\u01a9\5\\/\2")
        buf.write("\u01a9\u01aa\t\3\2\2\u01aa\u01ab\5\\/\2\u01ab\u01ae\3")
        buf.write("\2\2\2\u01ac\u01ae\5\\/\2\u01ad\u01a8\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01ae[\3\2\2\2\u01af\u01b0\5^\60\2\u01b0\u01b1")
        buf.write("\t\4\2\2\u01b1\u01b2\5^\60\2\u01b2\u01b5\3\2\2\2\u01b3")
        buf.write("\u01b5\5^\60\2\u01b4\u01af\3\2\2\2\u01b4\u01b3\3\2\2\2")
        buf.write("\u01b5]\3\2\2\2\u01b6\u01b7\b\60\1\2\u01b7\u01b8\5`\61")
        buf.write("\2\u01b8\u01be\3\2\2\2\u01b9\u01ba\f\4\2\2\u01ba\u01bb")
        buf.write("\t\5\2\2\u01bb\u01bd\5`\61\2\u01bc\u01b9\3\2\2\2\u01bd")
        buf.write("\u01c0\3\2\2\2\u01be\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf_\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c2\b\61\1")
        buf.write("\2\u01c2\u01c3\5b\62\2\u01c3\u01c9\3\2\2\2\u01c4\u01c5")
        buf.write("\f\4\2\2\u01c5\u01c6\t\6\2\2\u01c6\u01c8\5b\62\2\u01c7")
        buf.write("\u01c4\3\2\2\2\u01c8\u01cb\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01ca\3\2\2\2\u01caa\3\2\2\2\u01cb\u01c9\3\2\2")
        buf.write("\2\u01cc\u01cd\b\62\1\2\u01cd\u01ce\5d\63\2\u01ce\u01d4")
        buf.write("\3\2\2\2\u01cf\u01d0\f\4\2\2\u01d0\u01d1\t\7\2\2\u01d1")
        buf.write("\u01d3\5d\63\2\u01d2\u01cf\3\2\2\2\u01d3\u01d6\3\2\2\2")
        buf.write("\u01d4\u01d2\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5c\3\2\2")
        buf.write("\2\u01d6\u01d4\3\2\2\2\u01d7\u01d8\7#\2\2\u01d8\u01db")
        buf.write("\5d\63\2\u01d9\u01db\5f\64\2\u01da\u01d7\3\2\2\2\u01da")
        buf.write("\u01d9\3\2\2\2\u01dbe\3\2\2\2\u01dc\u01dd\7\37\2\2\u01dd")
        buf.write("\u01e0\5f\64\2\u01de\u01e0\5h\65\2\u01df\u01dc\3\2\2\2")
        buf.write("\u01df\u01de\3\2\2\2\u01e0g\3\2\2\2\u01e1\u01e2\b\65\1")
        buf.write("\2\u01e2\u01e3\5j\66\2\u01e3\u01e8\3\2\2\2\u01e4\u01e5")
        buf.write("\f\4\2\2\u01e5\u01e7\5t;\2\u01e6\u01e4\3\2\2\2\u01e7\u01ea")
        buf.write("\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9")
        buf.write("i\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ec\b\66\1\2\u01ec")
        buf.write("\u01ed\5l\67\2\u01ed\u01f2\3\2\2\2\u01ee\u01ef\f\4\2\2")
        buf.write("\u01ef\u01f1\5v<\2\u01f0\u01ee\3\2\2\2\u01f1\u01f4\3\2")
        buf.write("\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3k\3")
        buf.write("\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01f8\5z>\2\u01f6\u01f8")
        buf.write("\5n8\2\u01f7\u01f5\3\2\2\2\u01f7\u01f6\3\2\2\2\u01f8m")
        buf.write("\3\2\2\2\u01f9\u01fa\7\31\2\2\u01fa\u01fb\79\2\2\u01fb")
        buf.write("\u01fc\7/\2\2\u01fc\u01fd\5|?\2\u01fd\u01fe\7\60\2\2\u01fe")
        buf.write("\u0201\3\2\2\2\u01ff\u0201\5p9\2\u0200\u01f9\3\2\2\2\u0200")
        buf.write("\u01ff\3\2\2\2\u0201o\3\2\2\2\u0202\u0207\5\u0082B\2\u0203")
        buf.write("\u0207\79\2\2\u0204\u0207\7\33\2\2\u0205\u0207\5r:\2\u0206")
        buf.write("\u0202\3\2\2\2\u0206\u0203\3\2\2\2\u0206\u0204\3\2\2\2")
        buf.write("\u0206\u0205\3\2\2\2\u0207q\3\2\2\2\u0208\u0209\7/\2\2")
        buf.write("\u0209\u020a\5Z.\2\u020a\u020b\7\60\2\2\u020bs\3\2\2\2")
        buf.write("\u020c\u020d\7\61\2\2\u020d\u020e\5Z.\2\u020e\u020f\7")
        buf.write("\62\2\2\u020f\u0210\5t;\2\u0210\u0216\3\2\2\2\u0211\u0212")
        buf.write("\7\61\2\2\u0212\u0213\5Z.\2\u0213\u0214\7\62\2\2\u0214")
        buf.write("\u0216\3\2\2\2\u0215\u020c\3\2\2\2\u0215\u0211\3\2\2\2")
        buf.write("\u0216u\3\2\2\2\u0217\u0218\5x=\2\u0218\u0219\5v<\2\u0219")
        buf.write("\u021c\3\2\2\2\u021a\u021c\5x=\2\u021b\u0217\3\2\2\2\u021b")
        buf.write("\u021a\3\2\2\2\u021cw\3\2\2\2\u021d\u021e\7\65\2\2\u021e")
        buf.write("\u0226\79\2\2\u021f\u0220\7\65\2\2\u0220\u0221\79\2\2")
        buf.write("\u0221\u0222\7/\2\2\u0222\u0223\5|?\2\u0223\u0224\7\60")
        buf.write("\2\2\u0224\u0226\3\2\2\2\u0225\u021d\3\2\2\2\u0225\u021f")
        buf.write("\3\2\2\2\u0226y\3\2\2\2\u0227\u0230\79\2\2\u0228\u0229")
        buf.write("\7\34\2\2\u0229\u0231\7:\2\2\u022a\u022b\7\34\2\2\u022b")
        buf.write("\u022c\7:\2\2\u022c\u022d\7/\2\2\u022d\u022e\5|?\2\u022e")
        buf.write("\u022f\7\60\2\2\u022f\u0231\3\2\2\2\u0230\u0228\3\2\2")
        buf.write("\2\u0230\u022a\3\2\2\2\u0231{\3\2\2\2\u0232\u0233\5Z.")
        buf.write("\2\u0233\u0234\7\66\2\2\u0234\u0235\5|?\2\u0235\u0239")
        buf.write("\3\2\2\2\u0236\u0239\5Z.\2\u0237\u0239\3\2\2\2\u0238\u0232")
        buf.write("\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0237\3\2\2\2\u0239")
        buf.write("}\3\2\2\2\u023a\u023b\7\f\2\2\u023b\u023c\7/\2\2\u023c")
        buf.write("\u023d\5\u0080A\2\u023d\u023e\7\60\2\2\u023e\177\3\2\2")
        buf.write("\2\u023f\u0240\5Z.\2\u0240\u0241\7\66\2\2\u0241\u0242")
        buf.write("\5\u0080A\2\u0242\u0246\3\2\2\2\u0243\u0246\5Z.\2\u0244")
        buf.write("\u0246\3\2\2\2\u0245\u023f\3\2\2\2\u0245\u0243\3\2\2\2")
        buf.write("\u0245\u0244\3\2\2\2\u0246\u0081\3\2\2\2\u0247\u024e\7")
        buf.write("=\2\2\u0248\u024e\7>\2\2\u0249\u024e\7<\2\2\u024a\u024e")
        buf.write("\7\t\2\2\u024b\u024e\7;\2\2\u024c\u024e\5~@\2\u024d\u0247")
        buf.write("\3\2\2\2\u024d\u0248\3\2\2\2\u024d\u0249\3\2\2\2\u024d")
        buf.write("\u024a\3\2\2\2\u024d\u024b\3\2\2\2\u024d\u024c\3\2\2\2")
        buf.write("\u024e\u0083\3\2\2\2\u024f\u0250\5\u0086D\2\u0250\u0251")
        buf.write("\78\2\2\u0251\u0252\5\u0084C\2\u0252\u0256\3\2\2\2\u0253")
        buf.write("\u0256\5\u0086D\2\u0254\u0256\3\2\2\2\u0255\u024f\3\2")
        buf.write("\2\2\u0255\u0253\3\2\2\2\u0255\u0254\3\2\2\2\u0256\u0085")
        buf.write("\3\2\2\2\u0257\u0258\5\u0088E\2\u0258\u0259\7\67\2\2\u0259")
        buf.write("\u025a\5\u0094K\2\u025a\u0087\3\2\2\2\u025b\u025c\t\2")
        buf.write("\2\2\u025c\u025d\7\66\2\2\u025d\u0261\5\u0088E\2\u025e")
        buf.write("\u0261\t\2\2\2\u025f\u0261\3\2\2\2\u0260\u025b\3\2\2\2")
        buf.write("\u0260\u025e\3\2\2\2\u0260\u025f\3\2\2\2\u0261\u0089\3")
        buf.write("\2\2\2\u0262\u0263\79\2\2\u0263\u0264\7\66\2\2\u0264\u0268")
        buf.write("\5\u008aF\2\u0265\u0268\79\2\2\u0266\u0268\3\2\2\2\u0267")
        buf.write("\u0262\3\2\2\2\u0267\u0265\3\2\2\2\u0267\u0266\3\2\2\2")
        buf.write("\u0268\u008b\3\2\2\2\u0269\u026c\5\u0082B\2\u026a\u026c")
        buf.write("\5Z.\2\u026b\u0269\3\2\2\2\u026b\u026a\3\2\2\2\u026c\u026d")
        buf.write("\3\2\2\2\u026d\u026e\7\66\2\2\u026e\u026f\5\u008cG\2\u026f")
        buf.write("\u0276\3\2\2\2\u0270\u0273\5\u0082B\2\u0271\u0273\5Z.")
        buf.write("\2\u0272\u0270\3\2\2\2\u0272\u0271\3\2\2\2\u0273\u0276")
        buf.write("\3\2\2\2\u0274\u0276\3\2\2\2\u0275\u026b\3\2\2\2\u0275")
        buf.write("\u0272\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u008d\3\2\2\2")
        buf.write("\u0277\u0278\7\f\2\2\u0278\u0279\7\61\2\2\u0279\u027a")
        buf.write("\5\u0090I\2\u027a\u027b\7\66\2\2\u027b\u027c\7=\2\2\u027c")
        buf.write("\u027d\7\62\2\2\u027d\u008f\3\2\2\2\u027e\u0284\5\u008e")
        buf.write("H\2\u027f\u0284\7\16\2\2\u0280\u0284\7\17\2\2\u0281\u0284")
        buf.write("\7\20\2\2\u0282\u0284\7\21\2\2\u0283\u027e\3\2\2\2\u0283")
        buf.write("\u027f\3\2\2\2\u0283\u0280\3\2\2\2\u0283\u0281\3\2\2\2")
        buf.write("\u0283\u0282\3\2\2\2\u0284\u0091\3\2\2\2\u0285\u0286\t")
        buf.write("\b\2\2\u0286\u0093\3\2\2\2\u0287\u028b\5\u0092J\2\u0288")
        buf.write("\u028b\5\u008eH\2\u0289\u028b\79\2\2\u028a\u0287\3\2\2")
        buf.write("\2\u028a\u0288\3\2\2\2\u028a\u0289\3\2\2\2\u028b\u0095")
        buf.write("\3\2\2\2.\u009d\u00a7\u00cb\u00e3\u00fb\u0113\u0122\u0127")
        buf.write("\u0133\u013f\u0144\u0169\u0176\u0189\u0190\u0199\u01a6")
        buf.write("\u01ad\u01b4\u01be\u01c9\u01d4\u01da\u01df\u01e8\u01f2")
        buf.write("\u01f7\u0200\u0206\u0215\u021b\u0225\u0230\u0238\u0245")
        buf.write("\u024d\u0255\u0260\u0267\u026b\u0272\u0275\u0283\u028a")
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
    RULE_var_variable_declaration_noinit = 6
    RULE_var_variable_declaration = 7
    RULE_var_declare_initiate_list = 8
    RULE_val_variable_declaration_noinit = 9
    RULE_val_variable_declaration = 10
    RULE_val_declare_initiate_list = 11
    RULE_var_both_variable_declaration_noinnit = 12
    RULE_var_both_variable_declaration = 13
    RULE_var_both_declare_initiate_list = 14
    RULE_val_both_variable_declaration_noinnit = 15
    RULE_val_both_variable_declaration = 16
    RULE_val_both_declare_initiate_list = 17
    RULE_function_declaration = 18
    RULE_assignment_statements = 19
    RULE_lhs = 20
    RULE_scalar_variable = 21
    RULE_if_statements = 22
    RULE_elseif_list_statements = 23
    RULE_elseif_statement = 24
    RULE_else_statement = 25
    RULE_by_expr = 26
    RULE_forin_statements = 27
    RULE_instance_attr_access = 28
    RULE_instance_method_access = 29
    RULE_static_attr_access = 30
    RULE_static_method_access = 31
    RULE_method_invocation = 32
    RULE_method_invocation_statement = 33
    RULE_break_statements = 34
    RULE_continue_statements = 35
    RULE_return_expr = 36
    RULE_return_statements = 37
    RULE_block_class_statements = 38
    RULE_block_statements = 39
    RULE_statements_class = 40
    RULE_statements = 41
    RULE_statement_class = 42
    RULE_statement = 43
    RULE_expr = 44
    RULE_expr1 = 45
    RULE_expr2 = 46
    RULE_expr3 = 47
    RULE_expr4 = 48
    RULE_expr5 = 49
    RULE_expr6 = 50
    RULE_expr7 = 51
    RULE_expr8 = 52
    RULE_expr9 = 53
    RULE_expr10 = 54
    RULE_expr11 = 55
    RULE_expr12 = 56
    RULE_index_operators = 57
    RULE_instance_accesses = 58
    RULE_instance_access = 59
    RULE_static_access = 60
    RULE_list_expr = 61
    RULE_array_lit = 62
    RULE_array_val = 63
    RULE_literal = 64
    RULE_list_parameters = 65
    RULE_param = 66
    RULE_identifier_list = 67
    RULE_variable_in_func_identifier_list = 68
    RULE_value_list = 69
    RULE_array_type = 70
    RULE_array_element_type = 71
    RULE_primitive_type = 72
    RULE_variable_type = 73

    ruleNames =  [ "program", "class_declarations", "class_declaration", 
                   "class_inheritance", "constructor_dclr", "destructor_dclr", 
                   "var_variable_declaration_noinit", "var_variable_declaration", 
                   "var_declare_initiate_list", "val_variable_declaration_noinit", 
                   "val_variable_declaration", "val_declare_initiate_list", 
                   "var_both_variable_declaration_noinnit", "var_both_variable_declaration", 
                   "var_both_declare_initiate_list", "val_both_variable_declaration_noinnit", 
                   "val_both_variable_declaration", "val_both_declare_initiate_list", 
                   "function_declaration", "assignment_statements", "lhs", 
                   "scalar_variable", "if_statements", "elseif_list_statements", 
                   "elseif_statement", "else_statement", "by_expr", "forin_statements", 
                   "instance_attr_access", "instance_method_access", "static_attr_access", 
                   "static_method_access", "method_invocation", "method_invocation_statement", 
                   "break_statements", "continue_statements", "return_expr", 
                   "return_statements", "block_class_statements", "block_statements", 
                   "statements_class", "statements", "statement_class", 
                   "statement", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "expr12", "index_operators", "instance_accesses", 
                   "instance_access", "static_access", "list_expr", "array_lit", 
                   "array_val", "literal", "list_parameters", "param", "identifier_list", 
                   "variable_in_func_identifier_list", "value_list", "array_type", 
                   "array_element_type", "primitive_type", "variable_type" ]

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




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.class_declarations()
            self.state = 149
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




    def class_declarations(self):

        localctx = D96Parser.Class_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_declarations)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 151
                self.class_declaration()
                self.state = 152
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
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




    def class_declaration(self):

        localctx = D96Parser.Class_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(D96Parser.CLASS)
            self.state = 158
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 159
            self.class_inheritance()
            self.state = 160
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




    def class_inheritance(self):

        localctx = D96Parser.Class_inheritanceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_class_inheritance)
        try:
            self.state = 165
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(D96Parser.COLON)
                self.state = 163
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




    def constructor_dclr(self):

        localctx = D96Parser.Constructor_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_constructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 168
            self.match(D96Parser.LB)
            self.state = 169
            self.list_parameters()
            self.state = 170
            self.match(D96Parser.RB)
            self.state = 171
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

        def list_parameters(self):
            return self.getTypedRuleContext(D96Parser.List_parametersContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_destructor_dclr




    def destructor_dclr(self):

        localctx = D96Parser.Destructor_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_destructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(D96Parser.DESTRUCTOR)
            self.state = 174
            self.match(D96Parser.LB)
            self.state = 175
            self.list_parameters()
            self.state = 176
            self.match(D96Parser.RB)
            self.state = 177
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




    def var_variable_declaration_noinit(self):

        localctx = D96Parser.Var_variable_declaration_noinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_variable_declaration_noinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(D96Parser.VAR)
            self.state = 180
            self.variable_in_func_identifier_list()
            self.state = 181
            self.match(D96Parser.COLON)
            self.state = 182
            self.variable_type()
            self.state = 183
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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def var_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Var_declare_initiate_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_variable_declaration




    def var_variable_declaration(self):

        localctx = D96Parser.Var_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_var_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(D96Parser.VAR)
            self.state = 186
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 187
            self.var_declare_initiate_list()
            self.state = 188
            self.expr()
            self.state = 189
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def var_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Var_declare_initiate_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_declare_initiate_list




    def var_declare_initiate_list(self):

        localctx = D96Parser.Var_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_var_declare_initiate_list)
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(D96Parser.COMMA)
                self.state = 192
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 193
                self.var_declare_initiate_list()
                self.state = 194
                self.expr()
                self.state = 195
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
                self.match(D96Parser.COLON)
                self.state = 198
                self.variable_type()
                self.state = 199
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




    def val_variable_declaration_noinit(self):

        localctx = D96Parser.Val_variable_declaration_noinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_val_variable_declaration_noinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(D96Parser.VAL)
            self.state = 204
            self.variable_in_func_identifier_list()
            self.state = 205
            self.match(D96Parser.COLON)
            self.state = 206
            self.variable_type()
            self.state = 207
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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def val_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Val_declare_initiate_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_variable_declaration




    def val_variable_declaration(self):

        localctx = D96Parser.Val_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_val_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(D96Parser.VAL)
            self.state = 210
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 211
            self.val_declare_initiate_list()
            self.state = 212
            self.expr()
            self.state = 213
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def val_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Val_declare_initiate_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_declare_initiate_list




    def val_declare_initiate_list(self):

        localctx = D96Parser.Val_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_val_declare_initiate_list)
        try:
            self.state = 225
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.match(D96Parser.COMMA)
                self.state = 216
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 217
                self.val_declare_initiate_list()
                self.state = 218
                self.expr()
                self.state = 219
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.match(D96Parser.COLON)
                self.state = 222
                self.variable_type()
                self.state = 223
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




    def var_both_variable_declaration_noinnit(self):

        localctx = D96Parser.Var_both_variable_declaration_noinnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_var_both_variable_declaration_noinnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(D96Parser.VAR)
            self.state = 228
            self.identifier_list()
            self.state = 229
            self.match(D96Parser.COLON)
            self.state = 230
            self.variable_type()
            self.state = 231
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


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_var_both_variable_declaration




    def var_both_variable_declaration(self):

        localctx = D96Parser.Var_both_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_var_both_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(D96Parser.VAR)
            self.state = 234
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 235
            self.var_both_declare_initiate_list()
            self.state = 236
            self.expr()
            self.state = 237
            self.match(D96Parser.SEMICOLON)
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def var_both_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Var_both_declare_initiate_listContext,0)


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
            return D96Parser.RULE_var_both_declare_initiate_list




    def var_both_declare_initiate_list(self):

        localctx = D96Parser.Var_both_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(D96Parser.COMMA)
                self.state = 240
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 241
                self.var_both_declare_initiate_list()
                self.state = 242
                self.expr()
                self.state = 243
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.match(D96Parser.COLON)
                self.state = 246
                self.variable_type()
                self.state = 247
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




    def val_both_variable_declaration_noinnit(self):

        localctx = D96Parser.Val_both_variable_declaration_noinnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_val_both_variable_declaration_noinnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(D96Parser.VAL)
            self.state = 252
            self.identifier_list()
            self.state = 253
            self.match(D96Parser.COLON)
            self.state = 254
            self.variable_type()
            self.state = 255
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


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_val_both_variable_declaration




    def val_both_variable_declaration(self):

        localctx = D96Parser.Val_both_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_val_both_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(D96Parser.VAL)
            self.state = 258
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 259
            self.val_both_declare_initiate_list()
            self.state = 260
            self.expr()
            self.state = 261
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

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def val_both_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Val_both_declare_initiate_listContext,0)


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
            return D96Parser.RULE_val_both_declare_initiate_list




    def val_both_declare_initiate_list(self):

        localctx = D96Parser.Val_both_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_val_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(D96Parser.COMMA)
                self.state = 264
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 265
                self.val_both_declare_initiate_list()
                self.state = 266
                self.expr()
                self.state = 267
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.match(D96Parser.COLON)
                self.state = 270
                self.variable_type()
                self.state = 271
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




    def function_declaration(self):

        localctx = D96Parser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 276
            self.match(D96Parser.LB)
            self.state = 277
            self.list_parameters()
            self.state = 278
            self.match(D96Parser.RB)
            self.state = 279
            self.block_statements()
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




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.lhs()
            self.state = 282
            self.match(D96Parser.ASSIGNOP)
            self.state = 283
            self.expr()
            self.state = 284
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

        def scalar_variable(self):
            return self.getTypedRuleContext(D96Parser.Scalar_variableContext,0)


        def expr7(self):
            return self.getTypedRuleContext(D96Parser.Expr7Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_lhs)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.scalar_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
                self.expr7(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_variableContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return D96Parser.RULE_scalar_variable




    def scalar_variable(self):

        localctx = D96Parser.Scalar_variableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_scalar_variable)
        try:
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 292
                self.static_attr_access()
                pass


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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(D96Parser.IF)
            self.state = 296
            self.match(D96Parser.LB)
            self.state = 297
            self.expr()
            self.state = 298
            self.match(D96Parser.RB)
            self.state = 299
            self.block_statements()
            self.state = 300
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


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_statements




    def elseif_list_statements(self):

        localctx = D96Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elseif_list_statements)
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.elseif_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.else_statement()
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


    class Elseif_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(D96Parser.ELSEIF, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.match(D96Parser.ELSEIF)
            self.state = 308
            self.match(D96Parser.LB)
            self.state = 309
            self.expr()
            self.state = 310
            self.match(D96Parser.RB)
            self.state = 311
            self.block_statements()
            self.state = 312
            self.elseif_list_statements()
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




    def else_statement(self):

        localctx = D96Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_else_statement)
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.match(D96Parser.ELSE)
                self.state = 315
                self.block_statements()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.RCB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
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




    def by_expr(self):

        localctx = D96Parser.By_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_by_expr)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(D96Parser.BY)
                self.state = 320
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




    def forin_statements(self):

        localctx = D96Parser.Forin_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.match(D96Parser.FOREACH)
            self.state = 325
            self.match(D96Parser.LB)
            self.state = 326
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 327
            self.match(D96Parser.IN)
            self.state = 328
            self.expr()
            self.state = 329
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 330
            self.expr()
            self.state = 331
            self.by_expr()
            self.state = 332
            self.match(D96Parser.RB)
            self.state = 333
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




    def instance_attr_access(self):

        localctx = D96Parser.Instance_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.expr()
            self.state = 336
            self.match(D96Parser.DOT)
            self.state = 337
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




    def instance_method_access(self):

        localctx = D96Parser.Instance_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_instance_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr()
            self.state = 340
            self.match(D96Parser.DOT)
            self.state = 341
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 342
            self.match(D96Parser.LB)
            self.state = 343
            self.list_expr()
            self.state = 344
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




    def static_attr_access(self):

        localctx = D96Parser.Static_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 347
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 348
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




    def static_method_access(self):

        localctx = D96Parser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 351
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 352
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 353
            self.match(D96Parser.LB)
            self.state = 354
            self.list_expr()
            self.state = 355
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




    def method_invocation(self):

        localctx = D96Parser.Method_invocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_method_invocation)
        try:
            self.state = 359
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
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




    def method_invocation_statement(self):

        localctx = D96Parser.Method_invocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.method_invocation()
            self.state = 362
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




    def break_statements(self):

        localctx = D96Parser.Break_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(D96Parser.BREAK)
            self.state = 365
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




    def continue_statements(self):

        localctx = D96Parser.Continue_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(D96Parser.CONTINUE)
            self.state = 368
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




    def return_expr(self):

        localctx = D96Parser.Return_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_return_expr)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 370
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




    def return_statements(self):

        localctx = D96Parser.Return_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.match(D96Parser.RETURN)
            self.state = 375
            self.return_expr()
            self.state = 376
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




    def block_class_statements(self):

        localctx = D96Parser.Block_class_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.LCB)
            self.state = 379
            self.statements_class()
            self.state = 380
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




    def block_statements(self):

        localctx = D96Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(D96Parser.LCB)
            self.state = 383
            self.statements()
            self.state = 384
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




    def statements_class(self):

        localctx = D96Parser.Statements_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_statements_class)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.statement_class()
                self.state = 387
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 389
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




    def statements(self):

        localctx = D96Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_statements)
        try:
            self.state = 398
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 393
                self.statement()
                self.state = 394
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 396
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




    def statement_class(self):

        localctx = D96Parser.Statement_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_statement_class)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                self.var_both_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
                self.val_both_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 402
                self.var_both_variable_declaration_noinnit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 403
                self.val_both_variable_declaration_noinnit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 404
                self.function_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 405
                self.constructor_dclr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 406
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




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_statement)
        try:
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.var_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.val_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 411
                self.var_variable_declaration_noinit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 412
                self.val_variable_declaration_noinit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 413
                self.assignment_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 414
                self.if_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 415
                self.forin_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 416
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 417
                self.break_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 418
                self.continue_statements()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 419
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




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 427
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.expr1()
                self.state = 423
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 424
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
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




    def expr1(self):

        localctx = D96Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.expr2(0)
                self.state = 430
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 431
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 433
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



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 444
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 439
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 440
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 441
                    self.expr3(0) 
                self.state = 446
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 455
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 450
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 451
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 452
                    self.expr4(0) 
                self.state = 457
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 96
        self.enterRecursionRule(localctx, 96, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 466
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 461
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 462
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 463
                    self.expr5() 
                self.state = 468
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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




    def expr5(self):

        localctx = D96Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr5)
        try:
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(D96Parser.NOTOP)
                self.state = 470
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 471
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




    def expr6(self):

        localctx = D96Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr6)
        try:
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.match(D96Parser.MINUSOP)
                self.state = 475
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 476
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



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 482
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 483
                    self.index_operators() 
                self.state = 488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 496
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 492
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 493
                    self.instance_accesses() 
                self.state = 498
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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

        def static_access(self):
            return self.getTypedRuleContext(D96Parser.Static_accessContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr9)
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.static_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

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




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_expr10)
        try:
            self.state = 510
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.match(D96Parser.NEW)
                self.state = 504
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 505
                self.match(D96Parser.LB)
                self.state = 506
                self.list_expr()
                self.state = 507
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 509
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




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_expr11)
        try:
            self.state = 516
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 512
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 514
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 515
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




    def expr12(self):

        localctx = D96Parser.Expr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(D96Parser.LB)
            self.state = 519
            self.expr()
            self.state = 520
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




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_index_operators)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                self.match(D96Parser.LSB)
                self.state = 523
                self.expr()
                self.state = 524
                self.match(D96Parser.RSB)
                self.state = 525
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(D96Parser.LSB)
                self.state = 528
                self.expr()
                self.state = 529
                self.match(D96Parser.RSB)
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




    def instance_accesses(self):

        localctx = D96Parser.Instance_accessesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_instance_accesses)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.instance_access()
                self.state = 534
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 536
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




    def instance_access(self):

        localctx = D96Parser.Instance_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_instance_access)
        try:
            self.state = 547
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.match(D96Parser.DOT)
                self.state = 540
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 541
                self.match(D96Parser.DOT)
                self.state = 542
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 543
                self.match(D96Parser.LB)
                self.state = 544
                self.list_expr()
                self.state = 545
                self.match(D96Parser.RB)
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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

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




    def static_access(self):

        localctx = D96Parser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_static_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 550
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 551
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 552
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 553
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 554
                self.match(D96Parser.LB)
                self.state = 555
                self.list_expr()
                self.state = 556
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




    def list_expr(self):

        localctx = D96Parser.List_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_list_expr)
        try:
            self.state = 566
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 560
                self.expr()
                self.state = 561
                self.match(D96Parser.COMMA)
                self.state = 562
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
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




    def array_lit(self):

        localctx = D96Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.match(D96Parser.ARRAY)
            self.state = 569
            self.match(D96Parser.LB)
            self.state = 570
            self.array_val()
            self.state = 571
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




    def array_val(self):

        localctx = D96Parser.Array_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_array_val)
        try:
            self.state = 579
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.expr()
                self.state = 574
                self.match(D96Parser.COMMA)
                self.state = 575
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
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




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_literal)
        try:
            self.state = 587
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 583
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 584
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 585
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 586
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




    def list_parameters(self):

        localctx = D96Parser.List_parametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_list_parameters)
        try:
            self.state = 595
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.param()
                self.state = 590
                self.match(D96Parser.SEMICOLON)
                self.state = 591
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 593
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




    def param(self):

        localctx = D96Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 597
            self.identifier_list()
            self.state = 598
            self.match(D96Parser.COLON)
            self.state = 599
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




    def identifier_list(self):

        localctx = D96Parser.Identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 602
                self.match(D96Parser.COMMA)
                self.state = 603
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
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




    def variable_in_func_identifier_list(self):

        localctx = D96Parser.Variable_in_func_identifier_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 608
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 609
                self.match(D96Parser.COMMA)
                self.state = 610
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
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




    def value_list(self):

        localctx = D96Parser.Value_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_value_list)
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
                if la_ == 1:
                    self.state = 615
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 616
                    self.expr()
                    pass


                self.state = 619
                self.match(D96Parser.COMMA)
                self.state = 620
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 624
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 622
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 623
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




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629
            self.match(D96Parser.ARRAY)
            self.state = 630
            self.match(D96Parser.LSB)
            self.state = 631
            self.array_element_type()
            self.state = 632
            self.match(D96Parser.COMMA)
            self.state = 633
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 634
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




    def array_element_type(self):

        localctx = D96Parser.Array_element_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_array_element_type)
        try:
            self.state = 641
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 638
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 639
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 640
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




    def primitive_type(self):

        localctx = D96Parser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
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




    def variable_type(self):

        localctx = D96Parser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_variable_type)
        try:
            self.state = 648
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 645
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 647
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
        self._predicates[46] = self.expr2_sempred
        self._predicates[47] = self.expr3_sempred
        self._predicates[48] = self.expr4_sempred
        self._predicates[51] = self.expr7_sempred
        self._predicates[52] = self.expr8_sempred
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
         




