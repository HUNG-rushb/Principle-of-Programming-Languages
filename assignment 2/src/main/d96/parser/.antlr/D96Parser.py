# Generated from c:\Users\DELL\Documents\GitHub\Principle-of-Programming-Languages\assignment 2\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\u029f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00a2\n\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\5\3\5\3\5\5\5\u00ac\n\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u00d0\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00e8\n\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u0100\n\20\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0118")
        buf.write("\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\26\3\26\5\26\u0127\n\26\3\27\3\27\3\27\5\27\u012c")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\5\31\u0138\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\33\3\33\3\33\5\33\u0144\n\33\3\34\3\34\3\34\5\34\u0149")
        buf.write("\n\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\5\"\u016e")
        buf.write("\n\"\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\5&\u017b\n&\3\'")
        buf.write("\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\5")
        buf.write("*\u018e\n*\3+\3+\3+\3+\3+\5+\u0195\n+\3,\3,\3,\3,\3,\3")
        buf.write(",\3,\5,\u019e\n,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01ab")
        buf.write("\n-\3.\3.\3.\3.\3.\5.\u01b2\n.\3/\3/\3/\3/\3/\5/\u01b9")
        buf.write("\n/\3\60\3\60\3\60\3\60\3\60\3\60\7\60\u01c1\n\60\f\60")
        buf.write("\16\60\u01c4\13\60\3\61\3\61\3\61\3\61\3\61\3\61\7\61")
        buf.write("\u01cc\n\61\f\61\16\61\u01cf\13\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\7\62\u01d7\n\62\f\62\16\62\u01da\13\62\3\63")
        buf.write("\3\63\3\63\5\63\u01df\n\63\3\64\3\64\3\64\5\64\u01e4\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\7\65\u01eb\n\65\f\65\16\65")
        buf.write("\u01ee\13\65\3\66\3\66\3\66\3\66\3\66\7\66\u01f5\n\66")
        buf.write("\f\66\16\66\u01f8\13\66\3\67\3\67\5\67\u01fc\n\67\38\3")
        buf.write("8\38\38\38\38\38\58\u0205\n8\39\39\39\39\59\u020b\n9\3")
        buf.write(":\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3;\3;\5;\u021a\n;\3<\3")
        buf.write("<\3<\3<\5<\u0220\n<\3=\3=\3=\3=\3=\3=\5=\u0228\n=\3>\3")
        buf.write(">\3>\3>\5>\u022e\n>\3?\3?\3?\3?\3?\3?\3?\3?\5?\u0238\n")
        buf.write("?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u0243\n@\3A\3A\3A\3A\3")
        buf.write("A\3A\5A\u024b\nA\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\5C\u0258")
        buf.write("\nC\3D\3D\3D\3D\3D\3D\5D\u0260\nD\3E\3E\3E\3E\3E\3E\5")
        buf.write("E\u0268\nE\3F\3F\3F\3F\3G\3G\3G\3G\3G\5G\u0273\nG\3H\3")
        buf.write("H\3H\3H\3H\5H\u027a\nH\3I\3I\5I\u027e\nI\3I\3I\3I\3I\3")
        buf.write("I\5I\u0285\nI\3I\5I\u0288\nI\3J\3J\3J\3J\3J\3J\3J\3K\3")
        buf.write("K\3K\3K\3K\5K\u0296\nK\3L\3L\3M\3M\3M\5M\u029d\nM\3M\2")
        buf.write("\7^`bhjN\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(")
        buf.write("*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\u0096\u0098\2\t\3\29:\3\2-.\4\2&&(,\3\2$%\3\2\36")
        buf.write("\37\3\2 \"\3\2\16\21\2\u02a3\2\u009a\3\2\2\2\4\u00a1\3")
        buf.write("\2\2\2\6\u00a3\3\2\2\2\b\u00ab\3\2\2\2\n\u00ad\3\2\2\2")
        buf.write("\f\u00b3\3\2\2\2\16\u00b9\3\2\2\2\20\u00bf\3\2\2\2\22")
        buf.write("\u00cf\3\2\2\2\24\u00d1\3\2\2\2\26\u00d7\3\2\2\2\30\u00e7")
        buf.write("\3\2\2\2\32\u00e9\3\2\2\2\34\u00ef\3\2\2\2\36\u00ff\3")
        buf.write("\2\2\2 \u0101\3\2\2\2\"\u0107\3\2\2\2$\u0117\3\2\2\2&")
        buf.write("\u0119\3\2\2\2(\u011f\3\2\2\2*\u0126\3\2\2\2,\u012b\3")
        buf.write("\2\2\2.\u012d\3\2\2\2\60\u0137\3\2\2\2\62\u0139\3\2\2")
        buf.write("\2\64\u0143\3\2\2\2\66\u0148\3\2\2\28\u014a\3\2\2\2:\u0155")
        buf.write("\3\2\2\2<\u0159\3\2\2\2>\u0160\3\2\2\2@\u0164\3\2\2\2")
        buf.write("B\u016d\3\2\2\2D\u016f\3\2\2\2F\u0172\3\2\2\2H\u0175\3")
        buf.write("\2\2\2J\u017a\3\2\2\2L\u017c\3\2\2\2N\u0180\3\2\2\2P\u0184")
        buf.write("\3\2\2\2R\u018d\3\2\2\2T\u0194\3\2\2\2V\u019d\3\2\2\2")
        buf.write("X\u01aa\3\2\2\2Z\u01b1\3\2\2\2\\\u01b8\3\2\2\2^\u01ba")
        buf.write("\3\2\2\2`\u01c5\3\2\2\2b\u01d0\3\2\2\2d\u01de\3\2\2\2")
        buf.write("f\u01e3\3\2\2\2h\u01e5\3\2\2\2j\u01ef\3\2\2\2l\u01fb\3")
        buf.write("\2\2\2n\u0204\3\2\2\2p\u020a\3\2\2\2r\u020c\3\2\2\2t\u0219")
        buf.write("\3\2\2\2v\u021f\3\2\2\2x\u0227\3\2\2\2z\u022d\3\2\2\2")
        buf.write("|\u0237\3\2\2\2~\u0239\3\2\2\2\u0080\u024a\3\2\2\2\u0082")
        buf.write("\u024c\3\2\2\2\u0084\u0257\3\2\2\2\u0086\u025f\3\2\2\2")
        buf.write("\u0088\u0267\3\2\2\2\u008a\u0269\3\2\2\2\u008c\u0272\3")
        buf.write("\2\2\2\u008e\u0279\3\2\2\2\u0090\u0287\3\2\2\2\u0092\u0289")
        buf.write("\3\2\2\2\u0094\u0295\3\2\2\2\u0096\u0297\3\2\2\2\u0098")
        buf.write("\u029c\3\2\2\2\u009a\u009b\5\4\3\2\u009b\u009c\7\2\2\3")
        buf.write("\u009c\3\3\2\2\2\u009d\u009e\5\6\4\2\u009e\u009f\5\4\3")
        buf.write("\2\u009f\u00a2\3\2\2\2\u00a0\u00a2\5\6\4\2\u00a1\u009d")
        buf.write("\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\5\3\2\2\2\u00a3\u00a4")
        buf.write("\7\24\2\2\u00a4\u00a5\79\2\2\u00a5\u00a6\5\b\5\2\u00a6")
        buf.write("\u00a7\5N(\2\u00a7\7\3\2\2\2\u00a8\u00a9\7\67\2\2\u00a9")
        buf.write("\u00ac\79\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a8\3\2\2\2")
        buf.write("\u00ab\u00aa\3\2\2\2\u00ac\t\3\2\2\2\u00ad\u00ae\7\27")
        buf.write("\2\2\u00ae\u00af\7/\2\2\u00af\u00b0\5\u0088E\2\u00b0\u00b1")
        buf.write("\7\60\2\2\u00b1\u00b2\5P)\2\u00b2\13\3\2\2\2\u00b3\u00b4")
        buf.write("\7\30\2\2\u00b4\u00b5\7/\2\2\u00b5\u00b6\5\u0088E\2\u00b6")
        buf.write("\u00b7\7\60\2\2\u00b7\u00b8\5P)\2\u00b8\r\3\2\2\2\u00b9")
        buf.write("\u00ba\7\26\2\2\u00ba\u00bb\5\u008eH\2\u00bb\u00bc\7\67")
        buf.write("\2\2\u00bc\u00bd\5\u0098M\2\u00bd\u00be\78\2\2\u00be\17")
        buf.write("\3\2\2\2\u00bf\u00c0\7\26\2\2\u00c0\u00c1\79\2\2\u00c1")
        buf.write("\u00c2\5\22\n\2\u00c2\u00c3\5Z.\2\u00c3\u00c4\78\2\2\u00c4")
        buf.write("\21\3\2\2\2\u00c5\u00c6\7\66\2\2\u00c6\u00c7\79\2\2\u00c7")
        buf.write("\u00c8\5\22\n\2\u00c8\u00c9\5Z.\2\u00c9\u00ca\7\66\2\2")
        buf.write("\u00ca\u00d0\3\2\2\2\u00cb\u00cc\7\67\2\2\u00cc\u00cd")
        buf.write("\5\u0098M\2\u00cd\u00ce\7\'\2\2\u00ce\u00d0\3\2\2\2\u00cf")
        buf.write("\u00c5\3\2\2\2\u00cf\u00cb\3\2\2\2\u00d0\23\3\2\2\2\u00d1")
        buf.write("\u00d2\7\25\2\2\u00d2\u00d3\5\u008eH\2\u00d3\u00d4\7\67")
        buf.write("\2\2\u00d4\u00d5\5\u0098M\2\u00d5\u00d6\78\2\2\u00d6\25")
        buf.write("\3\2\2\2\u00d7\u00d8\7\25\2\2\u00d8\u00d9\79\2\2\u00d9")
        buf.write("\u00da\5\30\r\2\u00da\u00db\5Z.\2\u00db\u00dc\78\2\2\u00dc")
        buf.write("\27\3\2\2\2\u00dd\u00de\7\66\2\2\u00de\u00df\79\2\2\u00df")
        buf.write("\u00e0\5\30\r\2\u00e0\u00e1\5Z.\2\u00e1\u00e2\7\66\2\2")
        buf.write("\u00e2\u00e8\3\2\2\2\u00e3\u00e4\7\67\2\2\u00e4\u00e5")
        buf.write("\5\u0098M\2\u00e5\u00e6\7\'\2\2\u00e6\u00e8\3\2\2\2\u00e7")
        buf.write("\u00dd\3\2\2\2\u00e7\u00e3\3\2\2\2\u00e8\31\3\2\2\2\u00e9")
        buf.write("\u00ea\7\26\2\2\u00ea\u00eb\5\u008cG\2\u00eb\u00ec\7\67")
        buf.write("\2\2\u00ec\u00ed\5\u0098M\2\u00ed\u00ee\78\2\2\u00ee\33")
        buf.write("\3\2\2\2\u00ef\u00f0\7\26\2\2\u00f0\u00f1\t\2\2\2\u00f1")
        buf.write("\u00f2\5\36\20\2\u00f2\u00f3\5Z.\2\u00f3\u00f4\78\2\2")
        buf.write("\u00f4\35\3\2\2\2\u00f5\u00f6\7\66\2\2\u00f6\u00f7\t\2")
        buf.write("\2\2\u00f7\u00f8\5\36\20\2\u00f8\u00f9\5Z.\2\u00f9\u00fa")
        buf.write("\7\66\2\2\u00fa\u0100\3\2\2\2\u00fb\u00fc\7\67\2\2\u00fc")
        buf.write("\u00fd\5\u0098M\2\u00fd\u00fe\7\'\2\2\u00fe\u0100\3\2")
        buf.write("\2\2\u00ff\u00f5\3\2\2\2\u00ff\u00fb\3\2\2\2\u0100\37")
        buf.write("\3\2\2\2\u0101\u0102\7\25\2\2\u0102\u0103\5\u008cG\2\u0103")
        buf.write("\u0104\7\67\2\2\u0104\u0105\5\u0098M\2\u0105\u0106\78")
        buf.write("\2\2\u0106!\3\2\2\2\u0107\u0108\7\25\2\2\u0108\u0109\t")
        buf.write("\2\2\2\u0109\u010a\5$\23\2\u010a\u010b\5Z.\2\u010b\u010c")
        buf.write("\78\2\2\u010c#\3\2\2\2\u010d\u010e\7\66\2\2\u010e\u010f")
        buf.write("\t\2\2\2\u010f\u0110\5$\23\2\u0110\u0111\5Z.\2\u0111\u0112")
        buf.write("\7\66\2\2\u0112\u0118\3\2\2\2\u0113\u0114\7\67\2\2\u0114")
        buf.write("\u0115\5\u0098M\2\u0115\u0116\7\'\2\2\u0116\u0118\3\2")
        buf.write("\2\2\u0117\u010d\3\2\2\2\u0117\u0113\3\2\2\2\u0118%\3")
        buf.write("\2\2\2\u0119\u011a\t\2\2\2\u011a\u011b\7/\2\2\u011b\u011c")
        buf.write("\5\u0088E\2\u011c\u011d\7\60\2\2\u011d\u011e\5P)\2\u011e")
        buf.write("\'\3\2\2\2\u011f\u0120\5*\26\2\u0120\u0121\7\'\2\2\u0121")
        buf.write("\u0122\5Z.\2\u0122\u0123\78\2\2\u0123)\3\2\2\2\u0124\u0127")
        buf.write("\5,\27\2\u0125\u0127\5h\65\2\u0126\u0124\3\2\2\2\u0126")
        buf.write("\u0125\3\2\2\2\u0127+\3\2\2\2\u0128\u012c\79\2\2\u0129")
        buf.write("\u012c\5:\36\2\u012a\u012c\5> \2\u012b\u0128\3\2\2\2\u012b")
        buf.write("\u0129\3\2\2\2\u012b\u012a\3\2\2\2\u012c-\3\2\2\2\u012d")
        buf.write("\u012e\7\5\2\2\u012e\u012f\7/\2\2\u012f\u0130\5Z.\2\u0130")
        buf.write("\u0131\7\60\2\2\u0131\u0132\5P)\2\u0132\u0133\5\60\31")
        buf.write("\2\u0133/\3\2\2\2\u0134\u0138\5\62\32\2\u0135\u0138\5")
        buf.write("\64\33\2\u0136\u0138\3\2\2\2\u0137\u0134\3\2\2\2\u0137")
        buf.write("\u0135\3\2\2\2\u0137\u0136\3\2\2\2\u0138\61\3\2\2\2\u0139")
        buf.write("\u013a\7\6\2\2\u013a\u013b\7/\2\2\u013b\u013c\5Z.\2\u013c")
        buf.write("\u013d\7\60\2\2\u013d\u013e\5P)\2\u013e\u013f\5\60\31")
        buf.write("\2\u013f\63\3\2\2\2\u0140\u0141\7\7\2\2\u0141\u0144\5")
        buf.write("P)\2\u0142\u0144\3\2\2\2\u0143\u0140\3\2\2\2\u0143\u0142")
        buf.write("\3\2\2\2\u0144\65\3\2\2\2\u0145\u0146\7\32\2\2\u0146\u0149")
        buf.write("\5Z.\2\u0147\u0149\3\2\2\2\u0148\u0145\3\2\2\2\u0148\u0147")
        buf.write("\3\2\2\2\u0149\67\3\2\2\2\u014a\u014b\7\b\2\2\u014b\u014c")
        buf.write("\7/\2\2\u014c\u014d\t\2\2\2\u014d\u014e\7\r\2\2\u014e")
        buf.write("\u014f\5Z.\2\u014f\u0150\7\35\2\2\u0150\u0151\5Z.\2\u0151")
        buf.write("\u0152\5\66\34\2\u0152\u0153\7\60\2\2\u0153\u0154\5P)")
        buf.write("\2\u01549\3\2\2\2\u0155\u0156\5Z.\2\u0156\u0157\7\65\2")
        buf.write("\2\u0157\u0158\79\2\2\u0158;\3\2\2\2\u0159\u015a\5Z.\2")
        buf.write("\u015a\u015b\7\65\2\2\u015b\u015c\79\2\2\u015c\u015d\7")
        buf.write("/\2\2\u015d\u015e\5\u0080A\2\u015e\u015f\7\60\2\2\u015f")
        buf.write("=\3\2\2\2\u0160\u0161\t\2\2\2\u0161\u0162\7\34\2\2\u0162")
        buf.write("\u0163\7:\2\2\u0163?\3\2\2\2\u0164\u0165\t\2\2\2\u0165")
        buf.write("\u0166\7\34\2\2\u0166\u0167\7:\2\2\u0167\u0168\7/\2\2")
        buf.write("\u0168\u0169\5\u0080A\2\u0169\u016a\7\60\2\2\u016aA\3")
        buf.write("\2\2\2\u016b\u016e\5<\37\2\u016c\u016e\5@!\2\u016d\u016b")
        buf.write("\3\2\2\2\u016d\u016c\3\2\2\2\u016eC\3\2\2\2\u016f\u0170")
        buf.write("\5B\"\2\u0170\u0171\78\2\2\u0171E\3\2\2\2\u0172\u0173")
        buf.write("\7\3\2\2\u0173\u0174\78\2\2\u0174G\3\2\2\2\u0175\u0176")
        buf.write("\7\4\2\2\u0176\u0177\78\2\2\u0177I\3\2\2\2\u0178\u017b")
        buf.write("\5Z.\2\u0179\u017b\3\2\2\2\u017a\u0178\3\2\2\2\u017a\u0179")
        buf.write("\3\2\2\2\u017bK\3\2\2\2\u017c\u017d\7\22\2\2\u017d\u017e")
        buf.write("\5J&\2\u017e\u017f\78\2\2\u017fM\3\2\2\2\u0180\u0181\7")
        buf.write("\63\2\2\u0181\u0182\5R*\2\u0182\u0183\7\64\2\2\u0183O")
        buf.write("\3\2\2\2\u0184\u0185\7\63\2\2\u0185\u0186\5T+\2\u0186")
        buf.write("\u0187\7\64\2\2\u0187Q\3\2\2\2\u0188\u0189\5V,\2\u0189")
        buf.write("\u018a\5R*\2\u018a\u018e\3\2\2\2\u018b\u018e\5V,\2\u018c")
        buf.write("\u018e\3\2\2\2\u018d\u0188\3\2\2\2\u018d\u018b\3\2\2\2")
        buf.write("\u018d\u018c\3\2\2\2\u018eS\3\2\2\2\u018f\u0190\5X-\2")
        buf.write("\u0190\u0191\5T+\2\u0191\u0195\3\2\2\2\u0192\u0195\5X")
        buf.write("-\2\u0193\u0195\3\2\2\2\u0194\u018f\3\2\2\2\u0194\u0192")
        buf.write("\3\2\2\2\u0194\u0193\3\2\2\2\u0195U\3\2\2\2\u0196\u019e")
        buf.write("\5\34\17\2\u0197\u019e\5\"\22\2\u0198\u019e\5\32\16\2")
        buf.write("\u0199\u019e\5 \21\2\u019a\u019e\5&\24\2\u019b\u019e\5")
        buf.write("\n\6\2\u019c\u019e\5\f\7\2\u019d\u0196\3\2\2\2\u019d\u0197")
        buf.write("\3\2\2\2\u019d\u0198\3\2\2\2\u019d\u0199\3\2\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019b\3\2\2\2\u019d\u019c\3\2\2\2")
        buf.write("\u019eW\3\2\2\2\u019f\u01ab\5\20\t\2\u01a0\u01ab\5\26")
        buf.write("\f\2\u01a1\u01ab\5\16\b\2\u01a2\u01ab\5\24\13\2\u01a3")
        buf.write("\u01ab\5(\25\2\u01a4\u01ab\5.\30\2\u01a5\u01ab\58\35\2")
        buf.write("\u01a6\u01ab\5D#\2\u01a7\u01ab\5F$\2\u01a8\u01ab\5H%\2")
        buf.write("\u01a9\u01ab\5L\'\2\u01aa\u019f\3\2\2\2\u01aa\u01a0\3")
        buf.write("\2\2\2\u01aa\u01a1\3\2\2\2\u01aa\u01a2\3\2\2\2\u01aa\u01a3")
        buf.write("\3\2\2\2\u01aa\u01a4\3\2\2\2\u01aa\u01a5\3\2\2\2\u01aa")
        buf.write("\u01a6\3\2\2\2\u01aa\u01a7\3\2\2\2\u01aa\u01a8\3\2\2\2")
        buf.write("\u01aa\u01a9\3\2\2\2\u01abY\3\2\2\2\u01ac\u01ad\5\\/\2")
        buf.write("\u01ad\u01ae\t\3\2\2\u01ae\u01af\5\\/\2\u01af\u01b2\3")
        buf.write("\2\2\2\u01b0\u01b2\5\\/\2\u01b1\u01ac\3\2\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2[\3\2\2\2\u01b3\u01b4\5^\60\2\u01b4\u01b5")
        buf.write("\t\4\2\2\u01b5\u01b6\5^\60\2\u01b6\u01b9\3\2\2\2\u01b7")
        buf.write("\u01b9\5^\60\2\u01b8\u01b3\3\2\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9]\3\2\2\2\u01ba\u01bb\b\60\1\2\u01bb\u01bc\5`\61")
        buf.write("\2\u01bc\u01c2\3\2\2\2\u01bd\u01be\f\4\2\2\u01be\u01bf")
        buf.write("\t\5\2\2\u01bf\u01c1\5`\61\2\u01c0\u01bd\3\2\2\2\u01c1")
        buf.write("\u01c4\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2")
        buf.write("\u01c3_\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\b\61\1")
        buf.write("\2\u01c6\u01c7\5b\62\2\u01c7\u01cd\3\2\2\2\u01c8\u01c9")
        buf.write("\f\4\2\2\u01c9\u01ca\t\6\2\2\u01ca\u01cc\5b\62\2\u01cb")
        buf.write("\u01c8\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2")
        buf.write("\u01cd\u01ce\3\2\2\2\u01cea\3\2\2\2\u01cf\u01cd\3\2\2")
        buf.write("\2\u01d0\u01d1\b\62\1\2\u01d1\u01d2\5d\63\2\u01d2\u01d8")
        buf.write("\3\2\2\2\u01d3\u01d4\f\4\2\2\u01d4\u01d5\t\7\2\2\u01d5")
        buf.write("\u01d7\5d\63\2\u01d6\u01d3\3\2\2\2\u01d7\u01da\3\2\2\2")
        buf.write("\u01d8\u01d6\3\2\2\2\u01d8\u01d9\3\2\2\2\u01d9c\3\2\2")
        buf.write("\2\u01da\u01d8\3\2\2\2\u01db\u01dc\7#\2\2\u01dc\u01df")
        buf.write("\5d\63\2\u01dd\u01df\5f\64\2\u01de\u01db\3\2\2\2\u01de")
        buf.write("\u01dd\3\2\2\2\u01dfe\3\2\2\2\u01e0\u01e1\7\37\2\2\u01e1")
        buf.write("\u01e4\5f\64\2\u01e2\u01e4\5h\65\2\u01e3\u01e0\3\2\2\2")
        buf.write("\u01e3\u01e2\3\2\2\2\u01e4g\3\2\2\2\u01e5\u01e6\b\65\1")
        buf.write("\2\u01e6\u01e7\5j\66\2\u01e7\u01ec\3\2\2\2\u01e8\u01e9")
        buf.write("\f\4\2\2\u01e9\u01eb\5t;\2\u01ea\u01e8\3\2\2\2\u01eb\u01ee")
        buf.write("\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed")
        buf.write("i\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ef\u01f0\b\66\1\2\u01f0")
        buf.write("\u01f1\5l\67\2\u01f1\u01f6\3\2\2\2\u01f2\u01f3\f\4\2\2")
        buf.write("\u01f3\u01f5\5z>\2\u01f4\u01f2\3\2\2\2\u01f5\u01f8\3\2")
        buf.write("\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7k\3")
        buf.write("\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fc\5~@\2\u01fa\u01fc")
        buf.write("\5n8\2\u01fb\u01f9\3\2\2\2\u01fb\u01fa\3\2\2\2\u01fcm")
        buf.write("\3\2\2\2\u01fd\u01fe\7\31\2\2\u01fe\u01ff\79\2\2\u01ff")
        buf.write("\u0200\7/\2\2\u0200\u0201\5\u0080A\2\u0201\u0202\7\60")
        buf.write("\2\2\u0202\u0205\3\2\2\2\u0203\u0205\5p9\2\u0204\u01fd")
        buf.write("\3\2\2\2\u0204\u0203\3\2\2\2\u0205o\3\2\2\2\u0206\u020b")
        buf.write("\5\u0086D\2\u0207\u020b\79\2\2\u0208\u020b\7\33\2\2\u0209")
        buf.write("\u020b\5r:\2\u020a\u0206\3\2\2\2\u020a\u0207\3\2\2\2\u020a")
        buf.write("\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020bq\3\2\2\2\u020c")
        buf.write("\u020d\7/\2\2\u020d\u020e\5Z.\2\u020e\u020f\7\60\2\2\u020f")
        buf.write("s\3\2\2\2\u0210\u0211\7\61\2\2\u0211\u0212\5Z.\2\u0212")
        buf.write("\u0213\7\62\2\2\u0213\u0214\5t;\2\u0214\u021a\3\2\2\2")
        buf.write("\u0215\u0216\7\61\2\2\u0216\u0217\5Z.\2\u0217\u0218\7")
        buf.write("\62\2\2\u0218\u021a\3\2\2\2\u0219\u0210\3\2\2\2\u0219")
        buf.write("\u0215\3\2\2\2\u021au\3\2\2\2\u021b\u0220\5x=\2\u021c")
        buf.write("\u021d\5x=\2\u021d\u021e\5t;\2\u021e\u0220\3\2\2\2\u021f")
        buf.write("\u021b\3\2\2\2\u021f\u021c\3\2\2\2\u0220w\3\2\2\2\u0221")
        buf.write("\u0228\t\2\2\2\u0222\u0223\5Z.\2\u0223\u0224\5:\36\2\u0224")
        buf.write("\u0225\t\2\2\2\u0225\u0228\3\2\2\2\u0226\u0228\3\2\2\2")
        buf.write("\u0227\u0221\3\2\2\2\u0227\u0222\3\2\2\2\u0227\u0226\3")
        buf.write("\2\2\2\u0228y\3\2\2\2\u0229\u022a\5|?\2\u022a\u022b\5")
        buf.write("z>\2\u022b\u022e\3\2\2\2\u022c\u022e\5|?\2\u022d\u0229")
        buf.write("\3\2\2\2\u022d\u022c\3\2\2\2\u022e{\3\2\2\2\u022f\u0230")
        buf.write("\7\65\2\2\u0230\u0238\79\2\2\u0231\u0232\7\65\2\2\u0232")
        buf.write("\u0233\79\2\2\u0233\u0234\7/\2\2\u0234\u0235\5\u0080A")
        buf.write("\2\u0235\u0236\7\60\2\2\u0236\u0238\3\2\2\2\u0237\u022f")
        buf.write("\3\2\2\2\u0237\u0231\3\2\2\2\u0238}\3\2\2\2\u0239\u0242")
        buf.write("\79\2\2\u023a\u023b\7\34\2\2\u023b\u0243\7:\2\2\u023c")
        buf.write("\u023d\7\34\2\2\u023d\u023e\7:\2\2\u023e\u023f\7/\2\2")
        buf.write("\u023f\u0240\5\u0080A\2\u0240\u0241\7\60\2\2\u0241\u0243")
        buf.write("\3\2\2\2\u0242\u023a\3\2\2\2\u0242\u023c\3\2\2\2\u0243")
        buf.write("\177\3\2\2\2\u0244\u0245\5Z.\2\u0245\u0246\7\66\2\2\u0246")
        buf.write("\u0247\5\u0080A\2\u0247\u024b\3\2\2\2\u0248\u024b\5Z.")
        buf.write("\2\u0249\u024b\3\2\2\2\u024a\u0244\3\2\2\2\u024a\u0248")
        buf.write("\3\2\2\2\u024a\u0249\3\2\2\2\u024b\u0081\3\2\2\2\u024c")
        buf.write("\u024d\7\f\2\2\u024d\u024e\7/\2\2\u024e\u024f\5\u0084")
        buf.write("C\2\u024f\u0250\7\60\2\2\u0250\u0083\3\2\2\2\u0251\u0252")
        buf.write("\5Z.\2\u0252\u0253\7\66\2\2\u0253\u0254\5\u0084C\2\u0254")
        buf.write("\u0258\3\2\2\2\u0255\u0258\5Z.\2\u0256\u0258\3\2\2\2\u0257")
        buf.write("\u0251\3\2\2\2\u0257\u0255\3\2\2\2\u0257\u0256\3\2\2\2")
        buf.write("\u0258\u0085\3\2\2\2\u0259\u0260\7=\2\2\u025a\u0260\7")
        buf.write(">\2\2\u025b\u0260\7<\2\2\u025c\u0260\7\t\2\2\u025d\u0260")
        buf.write("\7;\2\2\u025e\u0260\5\u0082B\2\u025f\u0259\3\2\2\2\u025f")
        buf.write("\u025a\3\2\2\2\u025f\u025b\3\2\2\2\u025f\u025c\3\2\2\2")
        buf.write("\u025f\u025d\3\2\2\2\u025f\u025e\3\2\2\2\u0260\u0087\3")
        buf.write("\2\2\2\u0261\u0262\5\u008aF\2\u0262\u0263\78\2\2\u0263")
        buf.write("\u0264\5\u0088E\2\u0264\u0268\3\2\2\2\u0265\u0268\5\u008a")
        buf.write("F\2\u0266\u0268\3\2\2\2\u0267\u0261\3\2\2\2\u0267\u0265")
        buf.write("\3\2\2\2\u0267\u0266\3\2\2\2\u0268\u0089\3\2\2\2\u0269")
        buf.write("\u026a\5\u008cG\2\u026a\u026b\7\67\2\2\u026b\u026c\5\u0098")
        buf.write("M\2\u026c\u008b\3\2\2\2\u026d\u026e\t\2\2\2\u026e\u026f")
        buf.write("\7\66\2\2\u026f\u0273\5\u008cG\2\u0270\u0273\t\2\2\2\u0271")
        buf.write("\u0273\3\2\2\2\u0272\u026d\3\2\2\2\u0272\u0270\3\2\2\2")
        buf.write("\u0272\u0271\3\2\2\2\u0273\u008d\3\2\2\2\u0274\u0275\7")
        buf.write("9\2\2\u0275\u0276\7\66\2\2\u0276\u027a\5\u008eH\2\u0277")
        buf.write("\u027a\79\2\2\u0278\u027a\3\2\2\2\u0279\u0274\3\2\2\2")
        buf.write("\u0279\u0277\3\2\2\2\u0279\u0278\3\2\2\2\u027a\u008f\3")
        buf.write("\2\2\2\u027b\u027e\5\u0086D\2\u027c\u027e\5Z.\2\u027d")
        buf.write("\u027b\3\2\2\2\u027d\u027c\3\2\2\2\u027e\u027f\3\2\2\2")
        buf.write("\u027f\u0280\7\66\2\2\u0280\u0281\5\u0090I\2\u0281\u0288")
        buf.write("\3\2\2\2\u0282\u0285\5\u0086D\2\u0283\u0285\5Z.\2\u0284")
        buf.write("\u0282\3\2\2\2\u0284\u0283\3\2\2\2\u0285\u0288\3\2\2\2")
        buf.write("\u0286\u0288\3\2\2\2\u0287\u027d\3\2\2\2\u0287\u0284\3")
        buf.write("\2\2\2\u0287\u0286\3\2\2\2\u0288\u0091\3\2\2\2\u0289\u028a")
        buf.write("\7\f\2\2\u028a\u028b\7\61\2\2\u028b\u028c\5\u0094K\2\u028c")
        buf.write("\u028d\7\66\2\2\u028d\u028e\7=\2\2\u028e\u028f\7\62\2")
        buf.write("\2\u028f\u0093\3\2\2\2\u0290\u0296\5\u0092J\2\u0291\u0296")
        buf.write("\7\16\2\2\u0292\u0296\7\17\2\2\u0293\u0296\7\20\2\2\u0294")
        buf.write("\u0296\7\21\2\2\u0295\u0290\3\2\2\2\u0295\u0291\3\2\2")
        buf.write("\2\u0295\u0292\3\2\2\2\u0295\u0293\3\2\2\2\u0295\u0294")
        buf.write("\3\2\2\2\u0296\u0095\3\2\2\2\u0297\u0298\t\b\2\2\u0298")
        buf.write("\u0097\3\2\2\2\u0299\u029d\5\u0096L\2\u029a\u029d\5\u0092")
        buf.write("J\2\u029b\u029d\79\2\2\u029c\u0299\3\2\2\2\u029c\u029a")
        buf.write("\3\2\2\2\u029c\u029b\3\2\2\2\u029d\u0099\3\2\2\2\60\u00a1")
        buf.write("\u00ab\u00cf\u00e7\u00ff\u0117\u0126\u012b\u0137\u0143")
        buf.write("\u0148\u016d\u017a\u018d\u0194\u019d\u01aa\u01b1\u01b8")
        buf.write("\u01c2\u01cd\u01d8\u01de\u01e3\u01ec\u01f6\u01fb\u0204")
        buf.write("\u020a\u0219\u021f\u0227\u022d\u0237\u0242\u024a\u0257")
        buf.write("\u025f\u0267\u0272\u0279\u027d\u0284\u0287\u0295\u029c")
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
    RULE_index_expr = 58
    RULE_index = 59
    RULE_instance_accesses = 60
    RULE_instance_access = 61
    RULE_static_access = 62
    RULE_list_expr = 63
    RULE_array_lit = 64
    RULE_array_val = 65
    RULE_literal = 66
    RULE_list_parameters = 67
    RULE_param = 68
    RULE_identifier_list = 69
    RULE_variable_in_func_identifier_list = 70
    RULE_value_list = 71
    RULE_array_type = 72
    RULE_array_element_type = 73
    RULE_primitive_type = 74
    RULE_variable_type = 75

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
                   "expr11", "expr12", "index_operators", "index_expr", 
                   "index", "instance_accesses", "instance_access", "static_access", 
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
            self.state = 152
            self.class_declarations()
            self.state = 153
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
            self.state = 159
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.class_declaration()
                self.state = 156
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
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
            self.state = 161
            self.match(D96Parser.CLASS)
            self.state = 162
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 163
            self.class_inheritance()
            self.state = 164
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
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self.match(D96Parser.COLON)
                self.state = 167
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
            self.state = 171
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 172
            self.match(D96Parser.LB)
            self.state = 173
            self.list_parameters()
            self.state = 174
            self.match(D96Parser.RB)
            self.state = 175
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
            self.state = 177
            self.match(D96Parser.DESTRUCTOR)
            self.state = 178
            self.match(D96Parser.LB)
            self.state = 179
            self.list_parameters()
            self.state = 180
            self.match(D96Parser.RB)
            self.state = 181
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_variable_declaration_noinitContext(ParserRuleContext):

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
            self.state = 183
            self.match(D96Parser.VAR)
            self.state = 184
            self.variable_in_func_identifier_list()
            self.state = 185
            self.match(D96Parser.COLON)
            self.state = 186
            self.variable_type()
            self.state = 187
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_variable_declarationContext(ParserRuleContext):

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
            self.state = 189
            self.match(D96Parser.VAR)
            self.state = 190
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 191
            self.var_declare_initiate_list()
            self.state = 192
            self.expr()
            self.state = 193
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declare_initiate_listContext(ParserRuleContext):

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
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.match(D96Parser.COMMA)
                self.state = 196
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 197
                self.var_declare_initiate_list()
                self.state = 198
                self.expr()
                self.state = 199
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 201
                self.match(D96Parser.COLON)
                self.state = 202
                self.variable_type()
                self.state = 203
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
            self.state = 207
            self.match(D96Parser.VAL)
            self.state = 208
            self.variable_in_func_identifier_list()
            self.state = 209
            self.match(D96Parser.COLON)
            self.state = 210
            self.variable_type()
            self.state = 211
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_variable_declarationContext(ParserRuleContext):

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
            self.state = 213
            self.match(D96Parser.VAL)
            self.state = 214
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 215
            self.val_declare_initiate_list()
            self.state = 216
            self.expr()
            self.state = 217
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_declare_initiate_listContext(ParserRuleContext):

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
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 219
                self.match(D96Parser.COMMA)
                self.state = 220
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 221
                self.val_declare_initiate_list()
                self.state = 222
                self.expr()
                self.state = 223
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(D96Parser.COLON)
                self.state = 226
                self.variable_type()
                self.state = 227
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
            self.state = 231
            self.match(D96Parser.VAR)
            self.state = 232
            self.identifier_list()
            self.state = 233
            self.match(D96Parser.COLON)
            self.state = 234
            self.variable_type()
            self.state = 235
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_variable_declarationContext(ParserRuleContext):

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
            self.state = 237
            self.match(D96Parser.VAR)
            self.state = 238
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 239
            self.var_both_declare_initiate_list()
            self.state = 240
            self.expr()
            self.state = 241
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_both_declare_initiate_listContext(ParserRuleContext):

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
            self.state = 253
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(D96Parser.COMMA)
                self.state = 244
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 245
                self.var_both_declare_initiate_list()
                self.state = 246
                self.expr()
                self.state = 247
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(D96Parser.COLON)
                self.state = 250
                self.variable_type()
                self.state = 251
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
            self.state = 255
            self.match(D96Parser.VAL)
            self.state = 256
            self.identifier_list()
            self.state = 257
            self.match(D96Parser.COLON)
            self.state = 258
            self.variable_type()
            self.state = 259
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_both_variable_declarationContext(ParserRuleContext):

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
            self.state = 261
            self.match(D96Parser.VAL)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 263
            self.val_both_declare_initiate_list()
            self.state = 264
            self.expr()
            self.state = 265
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Val_both_declare_initiate_listContext(ParserRuleContext):

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
            self.state = 277
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 267
                self.match(D96Parser.COMMA)
                self.state = 268
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 269
                self.val_both_declare_initiate_list()
                self.state = 270
                self.expr()
                self.state = 271
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 273
                self.match(D96Parser.COLON)
                self.state = 274
                self.variable_type()
                self.state = 275
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
        self.enterRule(localctx, 36, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 280
            self.match(D96Parser.LB)
            self.state = 281
            self.list_parameters()
            self.state = 282
            self.match(D96Parser.RB)
            self.state = 283
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
        self.enterRule(localctx, 38, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.lhs()
            self.state = 286
            self.match(D96Parser.ASSIGNOP)
            self.state = 287
            self.expr()
            self.state = 288
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
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.scalar_variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
            self.state = 297
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 294
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 295
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 296
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
            self.state = 299
            self.match(D96Parser.IF)
            self.state = 300
            self.match(D96Parser.LB)
            self.state = 301
            self.expr()
            self.state = 302
            self.match(D96Parser.RB)
            self.state = 303
            self.block_statements()
            self.state = 304
            self.elseif_list_statements()
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


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_statements




    def elseif_list_statements(self):

        localctx = D96Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elseif_list_statements)
        try:
            self.state = 309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.elseif_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 307
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
            self.state = 311
            self.match(D96Parser.ELSEIF)
            self.state = 312
            self.match(D96Parser.LB)
            self.state = 313
            self.expr()
            self.state = 314
            self.match(D96Parser.RB)
            self.state = 315
            self.block_statements()
            self.state = 316
            self.elseif_list_statements()
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
        self.enterRule(localctx, 50, self.RULE_else_statement)
        try:
            self.state = 321
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(D96Parser.ELSE)
                self.state = 319
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
            self.state = 326
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.match(D96Parser.BY)
                self.state = 324
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
        self.enterRule(localctx, 54, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(D96Parser.FOREACH)
            self.state = 329
            self.match(D96Parser.LB)
            self.state = 330
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 331
            self.match(D96Parser.IN)
            self.state = 332
            self.expr()
            self.state = 333
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 334
            self.expr()
            self.state = 335
            self.by_expr()
            self.state = 336
            self.match(D96Parser.RB)
            self.state = 337
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

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_access




    def instance_attr_access(self):

        localctx = D96Parser.Instance_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.expr()
            self.state = 340
            self.match(D96Parser.DOT)
            self.state = 341
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
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
            self.state = 343
            self.expr()
            self.state = 344
            self.match(D96Parser.DOT)
            self.state = 345
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 346
            self.match(D96Parser.LB)
            self.state = 347
            self.list_expr()
            self.state = 348
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
            self.state = 354
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 355
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 356
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 357
            self.match(D96Parser.LB)
            self.state = 358
            self.list_expr()
            self.state = 359
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
        self.enterRule(localctx, 64, self.RULE_method_invocation)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
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
        self.enterRule(localctx, 66, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.method_invocation()
            self.state = 366
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
        self.enterRule(localctx, 68, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 368
            self.match(D96Parser.BREAK)
            self.state = 369
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
        self.enterRule(localctx, 70, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(D96Parser.CONTINUE)
            self.state = 372
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
        self.enterRule(localctx, 72, self.RULE_return_expr)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
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
        self.enterRule(localctx, 74, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.RETURN)
            self.state = 379
            self.return_expr()
            self.state = 380
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
        self.enterRule(localctx, 76, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(D96Parser.LCB)
            self.state = 383
            self.statements_class()
            self.state = 384
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
        self.enterRule(localctx, 78, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.match(D96Parser.LCB)
            self.state = 387
            self.statements()
            self.state = 388
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
        self.enterRule(localctx, 80, self.RULE_statements_class)
        try:
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                self.statement_class()
                self.state = 391
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 393
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
        self.enterRule(localctx, 82, self.RULE_statements)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.statement()
                self.state = 398
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
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
            self.state = 411
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.var_both_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.val_both_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.var_both_variable_declaration_noinnit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 407
                self.val_both_variable_declaration_noinnit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 408
                self.function_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 409
                self.constructor_dclr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 410
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
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.var_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 414
                self.val_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 415
                self.var_variable_declaration_noinit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 416
                self.val_variable_declaration_noinit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 417
                self.assignment_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 418
                self.if_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 419
                self.forin_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 420
                self.method_invocation_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 421
                self.break_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 422
                self.continue_statements()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 423
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
        self.enterRule(localctx, 88, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.expr1()
                self.state = 427
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 428
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
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
        self.enterRule(localctx, 90, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.expr2(0)
                self.state = 434
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 435
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
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
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 444
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 445
                    self.expr3(0) 
                self.state = 450
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
            self.state = 452
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 454
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 455
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 456
                    self.expr4(0) 
                self.state = 461
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
            self.state = 463
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 465
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 466
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 467
                    self.expr5() 
                self.state = 472
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
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.match(D96Parser.NOTOP)
                self.state = 474
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
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
        self.enterRule(localctx, 100, self.RULE_expr6)
        try:
            self.state = 481
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.match(D96Parser.MINUSOP)
                self.state = 479
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 484
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 490
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 486
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 487
                    self.index_operators() 
                self.state = 492
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
            self.state = 494
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 496
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 497
                    self.instance_accesses() 
                self.state = 502
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
            self.state = 505
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 503
                self.static_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 504
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
            self.state = 514
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.match(D96Parser.NEW)
                self.state = 508
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 509
                self.match(D96Parser.LB)
                self.state = 510
                self.list_expr()
                self.state = 511
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 513
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
            self.state = 520
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 516
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 518
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 519
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
        self.enterRule(localctx, 112, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 522
            self.match(D96Parser.LB)
            self.state = 523
            self.expr()
            self.state = 524
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
        self.enterRule(localctx, 114, self.RULE_index_operators)
        try:
            self.state = 535
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(D96Parser.LSB)
                self.state = 527
                self.expr()
                self.state = 528
                self.match(D96Parser.RSB)
                self.state = 529
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.match(D96Parser.LSB)
                self.state = 532
                self.expr()
                self.state = 533
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
        self.enterRule(localctx, 116, self.RULE_index_expr)
        try:
            self.state = 541
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 537
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
                self.index()
                self.state = 539
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
        self.enterRule(localctx, 118, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 549
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.expr()
                self.state = 545
                self.instance_attr_access()
                self.state = 546
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
        self.enterRule(localctx, 120, self.RULE_instance_accesses)
        try:
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 551
                self.instance_access()
                self.state = 552
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
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
        self.enterRule(localctx, 122, self.RULE_instance_access)
        try:
            self.state = 565
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.match(D96Parser.DOT)
                self.state = 558
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.match(D96Parser.DOT)
                self.state = 560
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 561
                self.match(D96Parser.LB)
                self.state = 562
                self.list_expr()
                self.state = 563
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
        self.enterRule(localctx, 124, self.RULE_static_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 568
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 569
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 570
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 571
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 572
                self.match(D96Parser.LB)
                self.state = 573
                self.list_expr()
                self.state = 574
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
        self.enterRule(localctx, 126, self.RULE_list_expr)
        try:
            self.state = 584
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.expr()
                self.state = 579
                self.match(D96Parser.COMMA)
                self.state = 580
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
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
        self.enterRule(localctx, 128, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(D96Parser.ARRAY)
            self.state = 587
            self.match(D96Parser.LB)
            self.state = 588
            self.array_val()
            self.state = 589
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
        self.enterRule(localctx, 130, self.RULE_array_val)
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.expr()
                self.state = 592
                self.match(D96Parser.COMMA)
                self.state = 593
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
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
        self.enterRule(localctx, 132, self.RULE_literal)
        try:
            self.state = 605
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 601
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 602
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 603
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 604
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
        self.enterRule(localctx, 134, self.RULE_list_parameters)
        try:
            self.state = 613
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.param()
                self.state = 608
                self.match(D96Parser.SEMICOLON)
                self.state = 609
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 611
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
        self.enterRule(localctx, 136, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.identifier_list()
            self.state = 616
            self.match(D96Parser.COLON)
            self.state = 617
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
        self.enterRule(localctx, 138, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 620
                self.match(D96Parser.COMMA)
                self.state = 621
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
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
        self.enterRule(localctx, 140, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 631
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 627
                self.match(D96Parser.COMMA)
                self.state = 628
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 629
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
        self.enterRule(localctx, 142, self.RULE_value_list)
        try:
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 633
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 634
                    self.expr()
                    pass


                self.state = 637
                self.match(D96Parser.COMMA)
                self.state = 638
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 642
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
                if la_ == 1:
                    self.state = 640
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 641
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
        self.enterRule(localctx, 144, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(D96Parser.ARRAY)
            self.state = 648
            self.match(D96Parser.LSB)
            self.state = 649
            self.array_element_type()
            self.state = 650
            self.match(D96Parser.COMMA)
            self.state = 651
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 652
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
        self.enterRule(localctx, 146, self.RULE_array_element_type)
        try:
            self.state = 659
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 654
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 655
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 656
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 657
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 658
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
        self.enterRule(localctx, 148, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 661
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


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_variable_type




    def variable_type(self):

        localctx = D96Parser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_variable_type)
        try:
            self.state = 666
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 664
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 665
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
         




