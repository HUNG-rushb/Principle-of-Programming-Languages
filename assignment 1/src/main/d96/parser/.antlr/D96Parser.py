# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 1\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0285\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\u009b\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\5\5\u00a5\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\5\t\u00be\n\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\n\u00ca\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00d6\n\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\r\3\r\3\r\5\r\u00e4\n\r\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00f0\n\16\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u0101\n\21\3\21\3\21\5\21\u0105\n")
        buf.write("\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\5\22\u0111\n\22\3\23\3\23\3\23\3\23\5\23\u0117\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\5\26\u0125\n\26\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\34\3\34\5\34\u014a\n\34\3")
        buf.write("\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \5 \u0157")
        buf.write("\n \3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("$\3$\3$\3%\3%\3%\3%\3%\5%\u0170\n%\3&\3&\3&\3&\3&\5&\u0177")
        buf.write("\n&\3\'\3\'\3\'\3\'\5\'\u017d\n\'\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u0187\n(\3)\3)\3)\3)\3)\5)\u018e\n)\3*\3*\3*\3")
        buf.write("*\3*\5*\u0195\n*\3+\3+\3+\3+\3+\3+\7+\u019d\n+\f+\16+")
        buf.write("\u01a0\13+\3,\3,\3,\3,\3,\3,\7,\u01a8\n,\f,\16,\u01ab")
        buf.write("\13,\3-\3-\3-\3-\3-\3-\7-\u01b3\n-\f-\16-\u01b6\13-\3")
        buf.write(".\3.\3.\5.\u01bb\n.\3/\3/\3/\5/\u01c0\n/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\7\60\u01c7\n\60\f\60\16\60\u01ca\13\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\5\61\u01d2\n\61\3\61\7\61\u01d5")
        buf.write("\n\61\f\61\16\61\u01d8\13\61\3\62\3\62\3\62\5\62\u01dd")
        buf.write("\n\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\5\63\u01e6\n")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\5\64\u01ed\n\64\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\5\66\u01fc\n\66\3\67\3\67\3\67\3\67\5\67\u0202\n\67\3")
        buf.write("8\38\38\38\38\38\58\u020a\n8\39\39\39\39\59\u0210\n9\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\5:\u021a\n:\3;\3;\3;\3;\5;\u0220")
        buf.write("\n;\3<\3<\3<\3<\3<\3<\3<\3<\5<\u022a\n<\3=\3=\3=\3=\3")
        buf.write("=\3=\5=\u0232\n=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\5?\u023f")
        buf.write("\n?\3@\3@\3@\3@\3@\3@\5@\u0247\n@\3A\3A\3A\3A\3A\3A\5")
        buf.write("A\u024f\nA\3B\3B\3B\3B\3C\3C\3C\3C\3C\5C\u025a\nC\3D\3")
        buf.write("D\3D\3D\3D\5D\u0261\nD\3E\3E\5E\u0265\nE\3E\3E\3E\3E\3")
        buf.write("E\5E\u026c\nE\3E\5E\u026f\nE\3F\3F\3F\3F\3F\3F\3F\3G\3")
        buf.write("G\3G\3G\3G\5G\u027d\nG\3H\3H\3I\3I\5I\u0283\nI\3I\2\7")
        buf.write("TVX^`J\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,")
        buf.write(".\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\2\n\3")
        buf.write("\2:;\3\2\25\26\3\2./\4\2\'\')-\3\2%&\3\2\37 \3\2!#\3\2")
        buf.write("\16\21\2\u028c\2\u0092\3\2\2\2\4\u009a\3\2\2\2\6\u009c")
        buf.write("\3\2\2\2\b\u00a4\3\2\2\2\n\u00a6\3\2\2\2\f\u00ac\3\2\2")
        buf.write("\2\16\u00b1\3\2\2\2\20\u00b7\3\2\2\2\22\u00c9\3\2\2\2")
        buf.write("\24\u00d5\3\2\2\2\26\u00d7\3\2\2\2\30\u00e3\3\2\2\2\32")
        buf.write("\u00ef\3\2\2\2\34\u00f1\3\2\2\2\36\u00f7\3\2\2\2 \u0100")
        buf.write("\3\2\2\2\"\u0106\3\2\2\2$\u0116\3\2\2\2&\u0118\3\2\2\2")
        buf.write("(\u011e\3\2\2\2*\u0124\3\2\2\2,\u0126\3\2\2\2.\u0131\3")
        buf.write("\2\2\2\60\u0135\3\2\2\2\62\u013c\3\2\2\2\64\u0140\3\2")
        buf.write("\2\2\66\u0149\3\2\2\28\u014b\3\2\2\2:\u014e\3\2\2\2<\u0151")
        buf.write("\3\2\2\2>\u0156\3\2\2\2@\u0158\3\2\2\2B\u015c\3\2\2\2")
        buf.write("D\u0160\3\2\2\2F\u0164\3\2\2\2H\u016f\3\2\2\2J\u0176\3")
        buf.write("\2\2\2L\u017c\3\2\2\2N\u0186\3\2\2\2P\u018d\3\2\2\2R\u0194")
        buf.write("\3\2\2\2T\u0196\3\2\2\2V\u01a1\3\2\2\2X\u01ac\3\2\2\2")
        buf.write("Z\u01ba\3\2\2\2\\\u01bf\3\2\2\2^\u01c1\3\2\2\2`\u01cb")
        buf.write("\3\2\2\2b\u01dc\3\2\2\2d\u01e5\3\2\2\2f\u01ec\3\2\2\2")
        buf.write("h\u01ee\3\2\2\2j\u01fb\3\2\2\2l\u0201\3\2\2\2n\u0209\3")
        buf.write("\2\2\2p\u020f\3\2\2\2r\u0219\3\2\2\2t\u021f\3\2\2\2v\u0229")
        buf.write("\3\2\2\2x\u0231\3\2\2\2z\u0233\3\2\2\2|\u023e\3\2\2\2")
        buf.write("~\u0246\3\2\2\2\u0080\u024e\3\2\2\2\u0082\u0250\3\2\2")
        buf.write("\2\u0084\u0259\3\2\2\2\u0086\u0260\3\2\2\2\u0088\u026e")
        buf.write("\3\2\2\2\u008a\u0270\3\2\2\2\u008c\u027c\3\2\2\2\u008e")
        buf.write("\u027e\3\2\2\2\u0090\u0282\3\2\2\2\u0092\u0093\5\4\3\2")
        buf.write("\u0093\u0094\7\2\2\3\u0094\3\3\2\2\2\u0095\u0096\5\6\4")
        buf.write("\2\u0096\u0097\5\4\3\2\u0097\u009b\3\2\2\2\u0098\u009b")
        buf.write("\5\6\4\2\u0099\u009b\3\2\2\2\u009a\u0095\3\2\2\2\u009a")
        buf.write("\u0098\3\2\2\2\u009a\u0099\3\2\2\2\u009b\5\3\2\2\2\u009c")
        buf.write("\u009d\7\24\2\2\u009d\u009e\7:\2\2\u009e\u009f\5\b\5\2")
        buf.write("\u009f\u00a0\5B\"\2\u00a0\7\3\2\2\2\u00a1\u00a2\78\2\2")
        buf.write("\u00a2\u00a5\7:\2\2\u00a3\u00a5\3\2\2\2\u00a4\u00a1\3")
        buf.write("\2\2\2\u00a4\u00a3\3\2\2\2\u00a5\t\3\2\2\2\u00a6\u00a7")
        buf.write("\7\27\2\2\u00a7\u00a8\7\60\2\2\u00a8\u00a9\5\u0080A\2")
        buf.write("\u00a9\u00aa\7\61\2\2\u00aa\u00ab\5D#\2\u00ab\13\3\2\2")
        buf.write("\2\u00ac\u00ad\7\30\2\2\u00ad\u00ae\7\60\2\2\u00ae\u00af")
        buf.write("\7\61\2\2\u00af\u00b0\5D#\2\u00b0\r\3\2\2\2\u00b1\u00b2")
        buf.write("\t\2\2\2\u00b2\u00b3\7\60\2\2\u00b3\u00b4\5\u0080A\2\u00b4")
        buf.write("\u00b5\7\61\2\2\u00b5\u00b6\5D#\2\u00b6\17\3\2\2\2\u00b7")
        buf.write("\u00bd\t\3\2\2\u00b8\u00be\5\22\n\2\u00b9\u00ba\5\u0084")
        buf.write("C\2\u00ba\u00bb\78\2\2\u00bb\u00bc\5\u0090I\2\u00bc\u00be")
        buf.write("\3\2\2\2\u00bd\u00b8\3\2\2\2\u00bd\u00b9\3\2\2\2\u00be")
        buf.write("\u00bf\3\2\2\2\u00bf\u00c0\79\2\2\u00c0\21\3\2\2\2\u00c1")
        buf.write("\u00c2\t\2\2\2\u00c2\u00c3\5\24\13\2\u00c3\u00c4\5P)\2")
        buf.write("\u00c4\u00ca\3\2\2\2\u00c5\u00c6\5\u0084C\2\u00c6\u00c7")
        buf.write("\78\2\2\u00c7\u00c8\5\u0090I\2\u00c8\u00ca\3\2\2\2\u00c9")
        buf.write("\u00c1\3\2\2\2\u00c9\u00c5\3\2\2\2\u00ca\23\3\2\2\2\u00cb")
        buf.write("\u00cc\7\67\2\2\u00cc\u00cd\t\2\2\2\u00cd\u00ce\5\24\13")
        buf.write("\2\u00ce\u00cf\5P)\2\u00cf\u00d0\7\67\2\2\u00d0\u00d6")
        buf.write("\3\2\2\2\u00d1\u00d2\78\2\2\u00d2\u00d3\5\u0090I\2\u00d3")
        buf.write("\u00d4\7(\2\2\u00d4\u00d6\3\2\2\2\u00d5\u00cb\3\2\2\2")
        buf.write("\u00d5\u00d1\3\2\2\2\u00d6\25\3\2\2\2\u00d7\u00d8\t\3")
        buf.write("\2\2\u00d8\u00d9\5\30\r\2\u00d9\u00da\79\2\2\u00da\27")
        buf.write("\3\2\2\2\u00db\u00dc\7:\2\2\u00dc\u00dd\5\32\16\2\u00dd")
        buf.write("\u00de\5P)\2\u00de\u00e4\3\2\2\2\u00df\u00e0\5\u0086D")
        buf.write("\2\u00e0\u00e1\78\2\2\u00e1\u00e2\5\u0090I\2\u00e2\u00e4")
        buf.write("\3\2\2\2\u00e3\u00db\3\2\2\2\u00e3\u00df\3\2\2\2\u00e4")
        buf.write("\31\3\2\2\2\u00e5\u00e6\7\67\2\2\u00e6\u00e7\7:\2\2\u00e7")
        buf.write("\u00e8\5\32\16\2\u00e8\u00e9\5P)\2\u00e9\u00ea\7\67\2")
        buf.write("\2\u00ea\u00f0\3\2\2\2\u00eb\u00ec\78\2\2\u00ec\u00ed")
        buf.write("\5\u0090I\2\u00ed\u00ee\7(\2\2\u00ee\u00f0\3\2\2\2\u00ef")
        buf.write("\u00e5\3\2\2\2\u00ef\u00eb\3\2\2\2\u00f0\33\3\2\2\2\u00f1")
        buf.write("\u00f2\t\2\2\2\u00f2\u00f3\7\60\2\2\u00f3\u00f4\5\u0080")
        buf.write("A\2\u00f4\u00f5\7\61\2\2\u00f5\u00f6\5D#\2\u00f6\35\3")
        buf.write("\2\2\2\u00f7\u00f8\5 \21\2\u00f8\u00f9\7(\2\2\u00f9\u00fa")
        buf.write("\5P)\2\u00fa\u00fb\79\2\2\u00fb\37\3\2\2\2\u00fc\u0101")
        buf.write("\7:\2\2\u00fd\u0101\7;\2\2\u00fe\u0101\5.\30\2\u00ff\u0101")
        buf.write("\5\62\32\2\u0100\u00fc\3\2\2\2\u0100\u00fd\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0100\u00ff\3\2\2\2\u0101\u0104\3\2\2\2")
        buf.write("\u0102\u0105\5j\66\2\u0103\u0105\3\2\2\2\u0104\u0102\3")
        buf.write("\2\2\2\u0104\u0103\3\2\2\2\u0105!\3\2\2\2\u0106\u0107")
        buf.write("\7\5\2\2\u0107\u0108\7\60\2\2\u0108\u0109\5P)\2\u0109")
        buf.write("\u010a\7\61\2\2\u010a\u0110\5D#\2\u010b\u010c\5$\23\2")
        buf.write("\u010c\u010d\5(\25\2\u010d\u0111\3\2\2\2\u010e\u0111\5")
        buf.write("(\25\2\u010f\u0111\3\2\2\2\u0110\u010b\3\2\2\2\u0110\u010e")
        buf.write("\3\2\2\2\u0110\u010f\3\2\2\2\u0111#\3\2\2\2\u0112\u0113")
        buf.write("\5&\24\2\u0113\u0114\5$\23\2\u0114\u0117\3\2\2\2\u0115")
        buf.write("\u0117\5&\24\2\u0116\u0112\3\2\2\2\u0116\u0115\3\2\2\2")
        buf.write("\u0117%\3\2\2\2\u0118\u0119\7\6\2\2\u0119\u011a\7\60\2")
        buf.write("\2\u011a\u011b\5P)\2\u011b\u011c\7\61\2\2\u011c\u011d")
        buf.write("\5D#\2\u011d\'\3\2\2\2\u011e\u011f\7\7\2\2\u011f\u0120")
        buf.write("\5D#\2\u0120)\3\2\2\2\u0121\u0122\7\32\2\2\u0122\u0125")
        buf.write("\5P)\2\u0123\u0125\3\2\2\2\u0124\u0121\3\2\2\2\u0124\u0123")
        buf.write("\3\2\2\2\u0125+\3\2\2\2\u0126\u0127\7\b\2\2\u0127\u0128")
        buf.write("\7\60\2\2\u0128\u0129\t\2\2\2\u0129\u012a\7\r\2\2\u012a")
        buf.write("\u012b\5P)\2\u012b\u012c\7\35\2\2\u012c\u012d\5P)\2\u012d")
        buf.write("\u012e\5*\26\2\u012e\u012f\7\61\2\2\u012f\u0130\5D#\2")
        buf.write("\u0130-\3\2\2\2\u0131\u0132\5P)\2\u0132\u0133\7\66\2\2")
        buf.write("\u0133\u0134\t\2\2\2\u0134/\3\2\2\2\u0135\u0136\5P)\2")
        buf.write("\u0136\u0137\7\66\2\2\u0137\u0138\t\2\2\2\u0138\u0139")
        buf.write("\7\60\2\2\u0139\u013a\5x=\2\u013a\u013b\7\61\2\2\u013b")
        buf.write("\61\3\2\2\2\u013c\u013d\5P)\2\u013d\u013e\7\34\2\2\u013e")
        buf.write("\u013f\7;\2\2\u013f\63\3\2\2\2\u0140\u0141\5P)\2\u0141")
        buf.write("\u0142\7\34\2\2\u0142\u0143\7;\2\2\u0143\u0144\7\60\2")
        buf.write("\2\u0144\u0145\5x=\2\u0145\u0146\7\61\2\2\u0146\65\3\2")
        buf.write("\2\2\u0147\u014a\5\60\31\2\u0148\u014a\5\64\33\2\u0149")
        buf.write("\u0147\3\2\2\2\u0149\u0148\3\2\2\2\u014a\67\3\2\2\2\u014b")
        buf.write("\u014c\5\66\34\2\u014c\u014d\79\2\2\u014d9\3\2\2\2\u014e")
        buf.write("\u014f\7\3\2\2\u014f\u0150\79\2\2\u0150;\3\2\2\2\u0151")
        buf.write("\u0152\7\4\2\2\u0152\u0153\79\2\2\u0153=\3\2\2\2\u0154")
        buf.write("\u0157\5P)\2\u0155\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0156")
        buf.write("\u0155\3\2\2\2\u0157?\3\2\2\2\u0158\u0159\7\22\2\2\u0159")
        buf.write("\u015a\5> \2\u015a\u015b\79\2\2\u015bA\3\2\2\2\u015c\u015d")
        buf.write("\7\64\2\2\u015d\u015e\5H%\2\u015e\u015f\7\65\2\2\u015f")
        buf.write("C\3\2\2\2\u0160\u0161\7\64\2\2\u0161\u0162\5J&\2\u0162")
        buf.write("\u0163\7\65\2\2\u0163E\3\2\2\2\u0164\u0165\7\64\2\2\u0165")
        buf.write("\u0166\5J&\2\u0166\u0167\7\22\2\2\u0167\u0168\79\2\2\u0168")
        buf.write("\u0169\7\65\2\2\u0169G\3\2\2\2\u016a\u016b\5L\'\2\u016b")
        buf.write("\u016c\5H%\2\u016c\u0170\3\2\2\2\u016d\u0170\5L\'\2\u016e")
        buf.write("\u0170\3\2\2\2\u016f\u016a\3\2\2\2\u016f\u016d\3\2\2\2")
        buf.write("\u016f\u016e\3\2\2\2\u0170I\3\2\2\2\u0171\u0172\5N(\2")
        buf.write("\u0172\u0173\5J&\2\u0173\u0177\3\2\2\2\u0174\u0177\5N")
        buf.write("(\2\u0175\u0177\3\2\2\2\u0176\u0171\3\2\2\2\u0176\u0174")
        buf.write("\3\2\2\2\u0176\u0175\3\2\2\2\u0177K\3\2\2\2\u0178\u017d")
        buf.write("\5\20\t\2\u0179\u017d\5\34\17\2\u017a\u017d\5\n\6\2\u017b")
        buf.write("\u017d\5\f\7\2\u017c\u0178\3\2\2\2\u017c\u0179\3\2\2\2")
        buf.write("\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017dM\3\2\2")
        buf.write("\2\u017e\u0187\5\26\f\2\u017f\u0187\5\36\20\2\u0180\u0187")
        buf.write("\5\"\22\2\u0181\u0187\5,\27\2\u0182\u0187\58\35\2\u0183")
        buf.write("\u0187\5:\36\2\u0184\u0187\5<\37\2\u0185\u0187\5@!\2\u0186")
        buf.write("\u017e\3\2\2\2\u0186\u017f\3\2\2\2\u0186\u0180\3\2\2\2")
        buf.write("\u0186\u0181\3\2\2\2\u0186\u0182\3\2\2\2\u0186\u0183\3")
        buf.write("\2\2\2\u0186\u0184\3\2\2\2\u0186\u0185\3\2\2\2\u0187O")
        buf.write("\3\2\2\2\u0188\u0189\5R*\2\u0189\u018a\t\4\2\2\u018a\u018b")
        buf.write("\5R*\2\u018b\u018e\3\2\2\2\u018c\u018e\5R*\2\u018d\u0188")
        buf.write("\3\2\2\2\u018d\u018c\3\2\2\2\u018eQ\3\2\2\2\u018f\u0190")
        buf.write("\5T+\2\u0190\u0191\t\5\2\2\u0191\u0192\5T+\2\u0192\u0195")
        buf.write("\3\2\2\2\u0193\u0195\5T+\2\u0194\u018f\3\2\2\2\u0194\u0193")
        buf.write("\3\2\2\2\u0195S\3\2\2\2\u0196\u0197\b+\1\2\u0197\u0198")
        buf.write("\5V,\2\u0198\u019e\3\2\2\2\u0199\u019a\f\4\2\2\u019a\u019b")
        buf.write("\t\6\2\2\u019b\u019d\5V,\2\u019c\u0199\3\2\2\2\u019d\u01a0")
        buf.write("\3\2\2\2\u019e\u019c\3\2\2\2\u019e\u019f\3\2\2\2\u019f")
        buf.write("U\3\2\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a2\b,\1\2\u01a2")
        buf.write("\u01a3\5X-\2\u01a3\u01a9\3\2\2\2\u01a4\u01a5\f\4\2\2\u01a5")
        buf.write("\u01a6\t\7\2\2\u01a6\u01a8\5X-\2\u01a7\u01a4\3\2\2\2\u01a8")
        buf.write("\u01ab\3\2\2\2\u01a9\u01a7\3\2\2\2\u01a9\u01aa\3\2\2\2")
        buf.write("\u01aaW\3\2\2\2\u01ab\u01a9\3\2\2\2\u01ac\u01ad\b-\1\2")
        buf.write("\u01ad\u01ae\5Z.\2\u01ae\u01b4\3\2\2\2\u01af\u01b0\f\4")
        buf.write("\2\2\u01b0\u01b1\t\b\2\2\u01b1\u01b3\5Z.\2\u01b2\u01af")
        buf.write("\3\2\2\2\u01b3\u01b6\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4")
        buf.write("\u01b5\3\2\2\2\u01b5Y\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b7")
        buf.write("\u01b8\7$\2\2\u01b8\u01bb\5Z.\2\u01b9\u01bb\5\\/\2\u01ba")
        buf.write("\u01b7\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb[\3\2\2\2\u01bc")
        buf.write("\u01bd\7 \2\2\u01bd\u01c0\5\\/\2\u01be\u01c0\5^\60\2\u01bf")
        buf.write("\u01bc\3\2\2\2\u01bf\u01be\3\2\2\2\u01c0]\3\2\2\2\u01c1")
        buf.write("\u01c2\b\60\1\2\u01c2\u01c3\5`\61\2\u01c3\u01c8\3\2\2")
        buf.write("\2\u01c4\u01c5\f\4\2\2\u01c5\u01c7\5j\66\2\u01c6\u01c4")
        buf.write("\3\2\2\2\u01c7\u01ca\3\2\2\2\u01c8\u01c6\3\2\2\2\u01c8")
        buf.write("\u01c9\3\2\2\2\u01c9_\3\2\2\2\u01ca\u01c8\3\2\2\2\u01cb")
        buf.write("\u01cc\b\61\1\2\u01cc\u01cd\5b\62\2\u01cd\u01d6\3\2\2")
        buf.write("\2\u01ce\u01d1\f\4\2\2\u01cf\u01d2\5j\66\2\u01d0\u01d2")
        buf.write("\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u01d5\5p9\2\u01d4\u01ce\3\2\2\2\u01d5")
        buf.write("\u01d8\3\2\2\2\u01d6\u01d4\3\2\2\2\u01d6\u01d7\3\2\2\2")
        buf.write("\u01d7a\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d9\u01da\t\2\2")
        buf.write("\2\u01da\u01dd\5t;\2\u01db\u01dd\5d\63\2\u01dc\u01d9\3")
        buf.write("\2\2\2\u01dc\u01db\3\2\2\2\u01ddc\3\2\2\2\u01de\u01df")
        buf.write("\7\31\2\2\u01df\u01e0\5P)\2\u01e0\u01e1\7\60\2\2\u01e1")
        buf.write("\u01e2\5x=\2\u01e2\u01e3\7\61\2\2\u01e3\u01e6\3\2\2\2")
        buf.write("\u01e4\u01e6\5f\64\2\u01e5\u01de\3\2\2\2\u01e5\u01e4\3")
        buf.write("\2\2\2\u01e6e\3\2\2\2\u01e7\u01ed\5~@\2\u01e8\u01ed\7")
        buf.write(":\2\2\u01e9\u01ed\7;\2\2\u01ea\u01ed\7\33\2\2\u01eb\u01ed")
        buf.write("\5h\65\2\u01ec\u01e7\3\2\2\2\u01ec\u01e8\3\2\2\2\u01ec")
        buf.write("\u01e9\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01eb\3\2\2\2")
        buf.write("\u01edg\3\2\2\2\u01ee\u01ef\7\60\2\2\u01ef\u01f0\5P)\2")
        buf.write("\u01f0\u01f1\7\61\2\2\u01f1i\3\2\2\2\u01f2\u01f3\7\62")
        buf.write("\2\2\u01f3\u01f4\5P)\2\u01f4\u01f5\7\63\2\2\u01f5\u01f6")
        buf.write("\5j\66\2\u01f6\u01fc\3\2\2\2\u01f7\u01f8\7\62\2\2\u01f8")
        buf.write("\u01f9\5P)\2\u01f9\u01fa\7\63\2\2\u01fa\u01fc\3\2\2\2")
        buf.write("\u01fb\u01f2\3\2\2\2\u01fb\u01f7\3\2\2\2\u01fck\3\2\2")
        buf.write("\2\u01fd\u0202\5n8\2\u01fe\u01ff\5n8\2\u01ff\u0200\5j")
        buf.write("\66\2\u0200\u0202\3\2\2\2\u0201\u01fd\3\2\2\2\u0201\u01fe")
        buf.write("\3\2\2\2\u0202m\3\2\2\2\u0203\u020a\t\2\2\2\u0204\u0205")
        buf.write("\5P)\2\u0205\u0206\5.\30\2\u0206\u0207\t\2\2\2\u0207\u020a")
        buf.write("\3\2\2\2\u0208\u020a\3\2\2\2\u0209\u0203\3\2\2\2\u0209")
        buf.write("\u0204\3\2\2\2\u0209\u0208\3\2\2\2\u020ao\3\2\2\2\u020b")
        buf.write("\u020c\5r:\2\u020c\u020d\5p9\2\u020d\u0210\3\2\2\2\u020e")
        buf.write("\u0210\5r:\2\u020f\u020b\3\2\2\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("q\3\2\2\2\u0211\u0212\7\66\2\2\u0212\u021a\t\2\2\2\u0213")
        buf.write("\u0214\7\66\2\2\u0214\u0215\t\2\2\2\u0215\u0216\7\60\2")
        buf.write("\2\u0216\u0217\5x=\2\u0217\u0218\7\61\2\2\u0218\u021a")
        buf.write("\3\2\2\2\u0219\u0211\3\2\2\2\u0219\u0213\3\2\2\2\u021a")
        buf.write("s\3\2\2\2\u021b\u021c\5v<\2\u021c\u021d\5t;\2\u021d\u0220")
        buf.write("\3\2\2\2\u021e\u0220\5v<\2\u021f\u021b\3\2\2\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220u\3\2\2\2\u0221\u0222\7\34\2\2\u0222\u022a")
        buf.write("\7;\2\2\u0223\u0224\7\34\2\2\u0224\u0225\7;\2\2\u0225")
        buf.write("\u0226\7\60\2\2\u0226\u0227\5x=\2\u0227\u0228\7\61\2\2")
        buf.write("\u0228\u022a\3\2\2\2\u0229\u0221\3\2\2\2\u0229\u0223\3")
        buf.write("\2\2\2\u022aw\3\2\2\2\u022b\u022c\5P)\2\u022c\u022d\7")
        buf.write("\67\2\2\u022d\u022e\5x=\2\u022e\u0232\3\2\2\2\u022f\u0232")
        buf.write("\5P)\2\u0230\u0232\3\2\2\2\u0231\u022b\3\2\2\2\u0231\u022f")
        buf.write("\3\2\2\2\u0231\u0230\3\2\2\2\u0232y\3\2\2\2\u0233\u0234")
        buf.write("\7\f\2\2\u0234\u0235\7\60\2\2\u0235\u0236\5|?\2\u0236")
        buf.write("\u0237\7\61\2\2\u0237{\3\2\2\2\u0238\u0239\5P)\2\u0239")
        buf.write("\u023a\7\67\2\2\u023a\u023b\5|?\2\u023b\u023f\3\2\2\2")
        buf.write("\u023c\u023f\5P)\2\u023d\u023f\3\2\2\2\u023e\u0238\3\2")
        buf.write("\2\2\u023e\u023c\3\2\2\2\u023e\u023d\3\2\2\2\u023f}\3")
        buf.write("\2\2\2\u0240\u0247\7>\2\2\u0241\u0247\7?\2\2\u0242\u0247")
        buf.write("\7=\2\2\u0243\u0247\7\t\2\2\u0244\u0247\7<\2\2\u0245\u0247")
        buf.write("\5z>\2\u0246\u0240\3\2\2\2\u0246\u0241\3\2\2\2\u0246\u0242")
        buf.write("\3\2\2\2\u0246\u0243\3\2\2\2\u0246\u0244\3\2\2\2\u0246")
        buf.write("\u0245\3\2\2\2\u0247\177\3\2\2\2\u0248\u0249\5\u0082B")
        buf.write("\2\u0249\u024a\79\2\2\u024a\u024b\5\u0080A\2\u024b\u024f")
        buf.write("\3\2\2\2\u024c\u024f\5\u0082B\2\u024d\u024f\3\2\2\2\u024e")
        buf.write("\u0248\3\2\2\2\u024e\u024c\3\2\2\2\u024e\u024d\3\2\2\2")
        buf.write("\u024f\u0081\3\2\2\2\u0250\u0251\5\u0084C\2\u0251\u0252")
        buf.write("\78\2\2\u0252\u0253\5\u0090I\2\u0253\u0083\3\2\2\2\u0254")
        buf.write("\u0255\t\2\2\2\u0255\u0256\7\67\2\2\u0256\u025a\5\u0084")
        buf.write("C\2\u0257\u025a\t\2\2\2\u0258\u025a\3\2\2\2\u0259\u0254")
        buf.write("\3\2\2\2\u0259\u0257\3\2\2\2\u0259\u0258\3\2\2\2\u025a")
        buf.write("\u0085\3\2\2\2\u025b\u025c\7:\2\2\u025c\u025d\7\67\2\2")
        buf.write("\u025d\u0261\5\u0086D\2\u025e\u0261\7:\2\2\u025f\u0261")
        buf.write("\3\2\2\2\u0260\u025b\3\2\2\2\u0260\u025e\3\2\2\2\u0260")
        buf.write("\u025f\3\2\2\2\u0261\u0087\3\2\2\2\u0262\u0265\5~@\2\u0263")
        buf.write("\u0265\5P)\2\u0264\u0262\3\2\2\2\u0264\u0263\3\2\2\2\u0265")
        buf.write("\u0266\3\2\2\2\u0266\u0267\7\67\2\2\u0267\u0268\5\u0088")
        buf.write("E\2\u0268\u026f\3\2\2\2\u0269\u026c\5~@\2\u026a\u026c")
        buf.write("\5P)\2\u026b\u0269\3\2\2\2\u026b\u026a\3\2\2\2\u026c\u026f")
        buf.write("\3\2\2\2\u026d\u026f\3\2\2\2\u026e\u0264\3\2\2\2\u026e")
        buf.write("\u026b\3\2\2\2\u026e\u026d\3\2\2\2\u026f\u0089\3\2\2\2")
        buf.write("\u0270\u0271\7\f\2\2\u0271\u0272\7\62\2\2\u0272\u0273")
        buf.write("\5\u008cG\2\u0273\u0274\7\67\2\2\u0274\u0275\7>\2\2\u0275")
        buf.write("\u0276\7\63\2\2\u0276\u008b\3\2\2\2\u0277\u027d\5\u008a")
        buf.write("F\2\u0278\u027d\7\16\2\2\u0279\u027d\7\17\2\2\u027a\u027d")
        buf.write("\7\20\2\2\u027b\u027d\7\21\2\2\u027c\u0277\3\2\2\2\u027c")
        buf.write("\u0278\3\2\2\2\u027c\u0279\3\2\2\2\u027c\u027a\3\2\2\2")
        buf.write("\u027c\u027b\3\2\2\2\u027d\u008d\3\2\2\2\u027e\u027f\t")
        buf.write("\t\2\2\u027f\u008f\3\2\2\2\u0280\u0283\5\u008eH\2\u0281")
        buf.write("\u0283\5\u008aF\2\u0282\u0280\3\2\2\2\u0282\u0281\3\2")
        buf.write("\2\2\u0283\u0091\3\2\2\2\63\u009a\u00a4\u00bd\u00c9\u00d5")
        buf.write("\u00e3\u00ef\u0100\u0104\u0110\u0116\u0124\u0149\u0156")
        buf.write("\u016f\u0176\u017c\u0186\u018d\u0194\u019e\u01a9\u01b4")
        buf.write("\u01ba\u01bf\u01c8\u01d1\u01d6\u01dc\u01e5\u01ec\u01fb")
        buf.write("\u0201\u0209\u020f\u0219\u021f\u0229\u0231\u023e\u0246")
        buf.write("\u024e\u0259\u0260\u0264\u026b\u026e\u027c\u0282")
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
                     "'By'", "'Self'", "'::'", "'..'", "'_'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'>='", "'<='", "'>'", "'<'", "'==.'", 
                     "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
                     "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "BOOLLIT", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", 
                      "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                      "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", 
                      "NOTEQUALOP", "GTE", "LTE", "GT", "LT", "STREQUALOP", 
                      "STRCONCATOP", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                      "DOT", "COMMA", "COLON", "SEMICOLON", "VARIABLE_IN_FUNC_IDENTIFIERS", 
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
    RULE_variable_declaration = 7
    RULE_declare_initiate_list = 8
    RULE_type_and_assign = 9
    RULE_variable_in_func_declaration = 10
    RULE_declare_initiate_in_func_list = 11
    RULE_type_and_assign_in_func = 12
    RULE_function_declaration = 13
    RULE_assignment_statements = 14
    RULE_lhs = 15
    RULE_if_statements = 16
    RULE_elseif_list_statements = 17
    RULE_elseif_statement = 18
    RULE_else_statement = 19
    RULE_by_expr = 20
    RULE_forin_statements = 21
    RULE_instance_attr_access = 22
    RULE_instance_method_access = 23
    RULE_static_attr_access = 24
    RULE_static_method_access = 25
    RULE_method_invocation = 26
    RULE_method_invocation_statement = 27
    RULE_break_statements = 28
    RULE_continue_statements = 29
    RULE_return_expr = 30
    RULE_return_statements = 31
    RULE_block_class_statements = 32
    RULE_block_statements = 33
    RULE_block_statements_in_main = 34
    RULE_statements_class = 35
    RULE_statements = 36
    RULE_statement_class = 37
    RULE_statement = 38
    RULE_expr = 39
    RULE_expr1 = 40
    RULE_expr2 = 41
    RULE_expr3 = 42
    RULE_expr4 = 43
    RULE_expr5 = 44
    RULE_expr6 = 45
    RULE_expr7 = 46
    RULE_expr8 = 47
    RULE_expr9 = 48
    RULE_expr10 = 49
    RULE_expr11 = 50
    RULE_expr12 = 51
    RULE_index_operators = 52
    RULE_index_expr = 53
    RULE_index = 54
    RULE_instance_accesses = 55
    RULE_instance_access = 56
    RULE_static_accesses = 57
    RULE_static_access = 58
    RULE_list_expr = 59
    RULE_array_lit = 60
    RULE_array_val = 61
    RULE_literal = 62
    RULE_list_parameters = 63
    RULE_param = 64
    RULE_identifier_list = 65
    RULE_variable_in_func_identifier_list = 66
    RULE_value_list = 67
    RULE_array_type = 68
    RULE_array_element_type = 69
    RULE_primitive_type = 70
    RULE_variable_type = 71

    ruleNames =  [ "program", "class_declarations", "class_declaration", 
                   "class_inheritance", "constructor_dclr", "destructor_dclr", 
                   "method_declaration", "variable_declaration", "declare_initiate_list", 
                   "type_and_assign", "variable_in_func_declaration", "declare_initiate_in_func_list", 
                   "type_and_assign_in_func", "function_declaration", "assignment_statements", 
                   "lhs", "if_statements", "elseif_list_statements", "elseif_statement", 
                   "else_statement", "by_expr", "forin_statements", "instance_attr_access", 
                   "instance_method_access", "static_attr_access", "static_method_access", 
                   "method_invocation", "method_invocation_statement", "break_statements", 
                   "continue_statements", "return_expr", "return_statements", 
                   "block_class_statements", "block_statements", "block_statements_in_main", 
                   "statements_class", "statements", "statement_class", 
                   "statement", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "expr12", "index_operators", "index_expr", 
                   "index", "instance_accesses", "instance_access", "static_accesses", 
                   "static_access", "list_expr", "array_lit", "array_val", 
                   "literal", "list_parameters", "param", "identifier_list", 
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
    UNDERSCORE=28
    PLUSOP=29
    MINUSOP=30
    MULTIPLYOP=31
    DIVIDEOP=32
    MODULOOP=33
    NOTOP=34
    ANDOP=35
    OROP=36
    EQUALOP=37
    ASSIGNOP=38
    NOTEQUALOP=39
    GTE=40
    LTE=41
    GT=42
    LT=43
    STREQUALOP=44
    STRCONCATOP=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    LCB=50
    RCB=51
    DOT=52
    COMMA=53
    COLON=54
    SEMICOLON=55
    VARIABLE_IN_FUNC_IDENTIFIERS=56
    DOLLAR_IDENTIFIERS=57
    STRINGLIT=58
    FLOATLIT=59
    INTLIT_IN_ARRAY=60
    INTLIT=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    BLOCK_COMMENT=64
    WS=65
    ERROR_CHAR=66

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

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
            self.state = 144
            self.class_declarations()
            self.state = 145
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_declarationsContext(ParserRuleContext):

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
            self.state = 152
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.class_declaration()
                self.state = 148
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.class_declaration()
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


    class Class_declarationContext(ParserRuleContext):

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
            self.state = 154
            self.match(D96Parser.CLASS)
            self.state = 155
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 156
            self.class_inheritance()
            self.state = 157
            self.block_class_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_inheritanceContext(ParserRuleContext):

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
            self.state = 162
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(D96Parser.COLON)
                self.state = 160
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
            self.state = 164
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 165
            self.match(D96Parser.LB)
            self.state = 166
            self.list_parameters()
            self.state = 167
            self.match(D96Parser.RB)
            self.state = 168
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Destructor_dclrContext(ParserRuleContext):

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




    def destructor_dclr(self):

        localctx = D96Parser.Destructor_dclrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_destructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(D96Parser.DESTRUCTOR)
            self.state = 171
            self.match(D96Parser.LB)
            self.state = 172
            self.match(D96Parser.RB)
            self.state = 173
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_declarationContext(ParserRuleContext):

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




    def method_declaration(self):

        localctx = D96Parser.Method_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 176
            self.match(D96Parser.LB)
            self.state = 177
            self.list_parameters()
            self.state = 178
            self.match(D96Parser.RB)
            self.state = 179
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Declare_initiate_listContext,0)


        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_declaration




    def variable_declaration(self):

        localctx = D96Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 182
                self.declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 183
                self.identifier_list()
                self.state = 184
                self.match(D96Parser.COLON)
                self.state = 185
                self.variable_type()
                pass


            self.state = 189
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_initiate_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declare_initiate_list




    def declare_initiate_list(self):

        localctx = D96Parser.Declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.type_and_assign()
                self.state = 193
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
                self.identifier_list()
                self.state = 196
                self.match(D96Parser.COLON)
                self.state = 197
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_and_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assignContext,0)


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
            return D96Parser.RULE_type_and_assign




    def type_and_assign(self):

        localctx = D96Parser.Type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 211
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.match(D96Parser.COMMA)
                self.state = 202
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 203
                self.type_and_assign()
                self.state = 204
                self.expr()
                self.state = 205
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(D96Parser.COLON)
                self.state = 208
                self.variable_type()
                self.state = 209
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


    class Variable_in_func_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declare_initiate_in_func_list(self):
            return self.getTypedRuleContext(D96Parser.Declare_initiate_in_func_listContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_in_func_declaration




    def variable_in_func_declaration(self):

        localctx = D96Parser.Variable_in_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_in_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 214
            self.declare_initiate_in_func_list()
            self.state = 215
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_initiate_in_func_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def type_and_assign_in_func(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assign_in_funcContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declare_initiate_in_func_list




    def declare_initiate_in_func_list(self):

        localctx = D96Parser.Declare_initiate_in_func_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_declare_initiate_in_func_list)
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 218
                self.type_and_assign_in_func()
                self.state = 219
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.variable_in_func_identifier_list()
                self.state = 222
                self.match(D96Parser.COLON)
                self.state = 223
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_and_assign_in_funcContext(ParserRuleContext):

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

        def type_and_assign_in_func(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assign_in_funcContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_type_and_assign_in_func




    def type_and_assign_in_func(self):

        localctx = D96Parser.Type_and_assign_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_type_and_assign_in_func)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(D96Parser.COMMA)
                self.state = 228
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 229
                self.type_and_assign_in_func()
                self.state = 230
                self.expr()
                self.state = 231
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(D96Parser.COLON)
                self.state = 234
                self.variable_type()
                self.state = 235
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
        self.enterRule(localctx, 26, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 240
            self.match(D96Parser.LB)
            self.state = 241
            self.list_parameters()
            self.state = 242
            self.match(D96Parser.RB)
            self.state = 243
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_statementsContext(ParserRuleContext):

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
        self.enterRule(localctx, 28, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.lhs()
            self.state = 246
            self.match(D96Parser.ASSIGNOP)
            self.state = 247
            self.expr()
            self.state = 248
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def instance_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_accessContext,0)


        def static_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_accessContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 250
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 251
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.state = 252
                self.instance_attr_access()
                pass

            elif la_ == 4:
                self.state = 253
                self.static_attr_access()
                pass


            self.state = 258
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 256
                self.index_operators()
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


    class If_statementsContext(ParserRuleContext):

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


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(D96Parser.IF)
            self.state = 261
            self.match(D96Parser.LB)
            self.state = 262
            self.expr()
            self.state = 263
            self.match(D96Parser.RB)
            self.state = 264
            self.block_statements()
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 265
                self.elseif_list_statements()
                self.state = 266
                self.else_statement()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 268
                self.else_statement()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.RCB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
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


    class Elseif_list_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_statement(self):
            return self.getTypedRuleContext(D96Parser.Elseif_statementContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_statements




    def elseif_list_statements(self):

        localctx = D96Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_elseif_list_statements)
        try:
            self.state = 276
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.elseif_statement()
                self.state = 273
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 275
                self.elseif_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Elseif_statementContext(ParserRuleContext):

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


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(D96Parser.ELSEIF)
            self.state = 279
            self.match(D96Parser.LB)
            self.state = 280
            self.expr()
            self.state = 281
            self.match(D96Parser.RB)
            self.state = 282
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statementContext(ParserRuleContext):

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
        self.enterRule(localctx, 38, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(D96Parser.ELSE)
            self.state = 285
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class By_exprContext(ParserRuleContext):

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
        self.enterRule(localctx, 40, self.RULE_by_expr)
        try:
            self.state = 290
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(D96Parser.BY)
                self.state = 288
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
        self.enterRule(localctx, 42, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.FOREACH)
            self.state = 293
            self.match(D96Parser.LB)
            self.state = 294
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 295
            self.match(D96Parser.IN)
            self.state = 296
            self.expr()
            self.state = 297
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 298
            self.expr()
            self.state = 299
            self.by_expr()
            self.state = 300
            self.match(D96Parser.RB)
            self.state = 301
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instance_attr_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_access




    def instance_attr_access(self):

        localctx = D96Parser.Instance_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_instance_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.expr()
            self.state = 304
            self.match(D96Parser.DOT)
            self.state = 305
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
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


    class Instance_method_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_expr(self):
            return self.getTypedRuleContext(D96Parser.List_exprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_access




    def instance_method_access(self):

        localctx = D96Parser.Instance_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_instance_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expr()
            self.state = 308
            self.match(D96Parser.DOT)
            self.state = 309
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 310
            self.match(D96Parser.LB)
            self.state = 311
            self.list_expr()
            self.state = 312
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_attr_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr_access




    def static_attr_access(self):

        localctx = D96Parser.Static_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_static_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.expr()
            self.state = 315
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 316
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Static_method_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


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
            return D96Parser.RULE_static_method_access




    def static_method_access(self):

        localctx = D96Parser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_static_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 318
            self.expr()
            self.state = 319
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 320
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 321
            self.match(D96Parser.LB)
            self.state = 322
            self.list_expr()
            self.state = 323
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocationContext(ParserRuleContext):

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
        self.enterRule(localctx, 52, self.RULE_method_invocation)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
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
        self.enterRule(localctx, 54, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.method_invocation()
            self.state = 330
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementsContext(ParserRuleContext):

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
        self.enterRule(localctx, 56, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(D96Parser.BREAK)
            self.state = 333
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementsContext(ParserRuleContext):

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
        self.enterRule(localctx, 58, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(D96Parser.CONTINUE)
            self.state = 336
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_return_expr




    def return_expr(self):

        localctx = D96Parser.Return_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_expr)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
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
        self.enterRule(localctx, 62, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.match(D96Parser.RETURN)
            self.state = 343
            self.return_expr()
            self.state = 344
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_class_statementsContext(ParserRuleContext):

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
        self.enterRule(localctx, 64, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(D96Parser.LCB)
            self.state = 347
            self.statements_class()
            self.state = 348
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementsContext(ParserRuleContext):

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
        self.enterRule(localctx, 66, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(D96Parser.LCB)
            self.state = 351
            self.statements()
            self.state = 352
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statements_in_mainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statements(self):
            return self.getTypedRuleContext(D96Parser.StatementsContext,0)


        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_block_statements_in_main




    def block_statements_in_main(self):

        localctx = D96Parser.Block_statements_in_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_block_statements_in_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.match(D96Parser.LCB)
            self.state = 355
            self.statements()
            self.state = 356
            self.match(D96Parser.RETURN)
            self.state = 357
            self.match(D96Parser.SEMICOLON)
            self.state = 358
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Statements_classContext(ParserRuleContext):

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
        self.enterRule(localctx, 70, self.RULE_statements_class)
        try:
            self.state = 365
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 360
                self.statement_class()
                self.state = 361
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
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
        self.enterRule(localctx, 72, self.RULE_statements)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.statement()
                self.state = 368
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_declarationContext,0)


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
        self.enterRule(localctx, 74, self.RULE_statement_class)
        try:
            self.state = 378
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.variable_declaration()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.function_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 376
                self.constructor_dclr()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 377
                self.destructor_dclr()
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


    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_in_func_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_declarationContext,0)


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
        self.enterRule(localctx, 76, self.RULE_statement)
        try:
            self.state = 388
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 380
                self.variable_in_func_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 382
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 383
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 384
                self.method_invocation_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 385
                self.break_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 386
                self.continue_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 387
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
        self.enterRule(localctx, 78, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.expr1()
                self.state = 391
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 392
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 394
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
        self.enterRule(localctx, 80, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.expr2(0)
                self.state = 398
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 399
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 401
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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 412
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 407
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 408
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 409
                    self.expr3(0) 
                self.state = 414
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 423
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 418
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 419
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 420
                    self.expr4(0) 
                self.state = 425
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):

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
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 434
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 429
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 430
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 431
                    self.expr5() 
                self.state = 436
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):

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
        self.enterRule(localctx, 88, self.RULE_expr5)
        try:
            self.state = 440
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 437
                self.match(D96Parser.NOTOP)
                self.state = 438
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
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
        self.enterRule(localctx, 90, self.RULE_expr6)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 442
                self.match(D96Parser.MINUSOP)
                self.state = 443
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 454
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 450
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 451
                    self.index_operators() 
                self.state = 456
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr9(self):
            return self.getTypedRuleContext(D96Parser.Expr9Context,0)


        def expr8(self):
            return self.getTypedRuleContext(D96Parser.Expr8Context,0)


        def instance_accesses(self):
            return self.getTypedRuleContext(D96Parser.Instance_accessesContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr8



    def expr8(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Expr8Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 468
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 460
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 463
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.LSB]:
                        self.state = 461
                        self.index_operators()
                        pass
                    elif token in [D96Parser.DOT]:
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 465
                    self.instance_accesses() 
                self.state = 470
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_accesses(self):
            return self.getTypedRuleContext(D96Parser.Static_accessesContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 471
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 472
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
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




    def expr10(self):

        localctx = D96Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr10)
        try:
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.match(D96Parser.NEW)
                self.state = 477
                self.expr()
                self.state = 478
                self.match(D96Parser.LB)
                self.state = 479
                self.list_expr()
                self.state = 480
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def expr12(self):
            return self.getTypedRuleContext(D96Parser.Expr12Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr11




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr11)
        try:
            self.state = 490
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 487
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 488
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 489
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
        self.enterRule(localctx, 102, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.match(D96Parser.LB)
            self.state = 493
            self.expr()
            self.state = 494
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_operatorsContext(ParserRuleContext):

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
        self.enterRule(localctx, 104, self.RULE_index_operators)
        try:
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.match(D96Parser.LSB)
                self.state = 497
                self.expr()
                self.state = 498
                self.match(D96Parser.RSB)
                self.state = 499
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 501
                self.match(D96Parser.LSB)
                self.state = 502
                self.expr()
                self.state = 503
                self.match(D96Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Index_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def index(self):
            return self.getTypedRuleContext(D96Parser.IndexContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_index_expr




    def index_expr(self):

        localctx = D96Parser.Index_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_index_expr)
        try:
            self.state = 511
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.index()
                self.state = 509
                self.index_operators()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):

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




    def index(self):

        localctx = D96Parser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 514
                self.expr()
                self.state = 515
                self.instance_attr_access()
                self.state = 516
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
        self.enterRule(localctx, 110, self.RULE_instance_accesses)
        try:
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.instance_access()
                self.state = 522
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

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
        self.enterRule(localctx, 112, self.RULE_instance_access)
        self._la = 0 # Token type
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(D96Parser.DOT)
                self.state = 528
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.match(D96Parser.DOT)
                self.state = 530
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 531
                self.match(D96Parser.LB)
                self.state = 532
                self.list_expr()
                self.state = 533
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def static_access(self):
            return self.getTypedRuleContext(D96Parser.Static_accessContext,0)


        def static_accesses(self):
            return self.getTypedRuleContext(D96Parser.Static_accessesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_static_accesses




    def static_accesses(self):

        localctx = D96Parser.Static_accessesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_static_accesses)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.static_access()
                self.state = 538
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
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




    def static_access(self):

        localctx = D96Parser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_static_access)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 544
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 546
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 547
                self.match(D96Parser.LB)
                self.state = 548
                self.list_expr()
                self.state = 549
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
        self.enterRule(localctx, 118, self.RULE_list_expr)
        try:
            self.state = 559
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.expr()
                self.state = 554
                self.match(D96Parser.COMMA)
                self.state = 555
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
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
        self.enterRule(localctx, 120, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.match(D96Parser.ARRAY)
            self.state = 562
            self.match(D96Parser.LB)
            self.state = 563
            self.array_val()
            self.state = 564
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_valContext(ParserRuleContext):

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
        self.enterRule(localctx, 122, self.RULE_array_val)
        try:
            self.state = 572
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.expr()
                self.state = 567
                self.match(D96Parser.COMMA)
                self.state = 568
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
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
        self.enterRule(localctx, 124, self.RULE_literal)
        try:
            self.state = 580
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 574
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 575
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 576
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 577
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 578
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 579
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
        self.enterRule(localctx, 126, self.RULE_list_parameters)
        try:
            self.state = 588
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.param()
                self.state = 583
                self.match(D96Parser.SEMICOLON)
                self.state = 584
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 586
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
        self.enterRule(localctx, 128, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 590
            self.identifier_list()
            self.state = 591
            self.match(D96Parser.COLON)
            self.state = 592
            self.variable_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Identifier_listContext(ParserRuleContext):

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
        self.enterRule(localctx, 130, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 599
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 595
                self.match(D96Parser.COMMA)
                self.state = 596
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
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
        self.enterRule(localctx, 132, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 606
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 601
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 602
                self.match(D96Parser.COMMA)
                self.state = 603
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 604
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
        self.enterRule(localctx, 134, self.RULE_value_list)
        try:
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 610
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 608
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 609
                    self.expr()
                    pass


                self.state = 612
                self.match(D96Parser.COMMA)
                self.state = 613
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 617
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 615
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 616
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
        self.enterRule(localctx, 136, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 622
            self.match(D96Parser.ARRAY)
            self.state = 623
            self.match(D96Parser.LSB)
            self.state = 624
            self.array_element_type()
            self.state = 625
            self.match(D96Parser.COMMA)
            self.state = 626
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 627
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_element_typeContext(ParserRuleContext):

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
        self.enterRule(localctx, 138, self.RULE_array_element_type)
        try:
            self.state = 634
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 630
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 631
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 632
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 633
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
        self.enterRule(localctx, 140, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 636
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(D96Parser.Primitive_typeContext,0)


        def array_type(self):
            return self.getTypedRuleContext(D96Parser.Array_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_type




    def variable_type(self):

        localctx = D96Parser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_variable_type)
        try:
            self.state = 640
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 638
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 639
                self.array_type()
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
        self._predicates[41] = self.expr2_sempred
        self._predicates[42] = self.expr3_sempred
        self._predicates[43] = self.expr4_sempred
        self._predicates[46] = self.expr7_sempred
        self._predicates[47] = self.expr8_sempred
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
         




