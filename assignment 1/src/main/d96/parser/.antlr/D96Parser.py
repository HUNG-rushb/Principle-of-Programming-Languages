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
        buf.write("\u0289\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\3\2\3\2\3\2\6\2\u0096")
        buf.write("\n\2\r\2\16\2\u0097\3\3\3\3\3\3\3\3\3\3\5\3\u009f\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5\5\u00a9\n\5\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00c2\n\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00ce\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00da\n")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\5")
        buf.write("\r\u00e8\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\5\16\u00f4\n\16\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\5\21\u0105")
        buf.write("\n\21\3\21\3\21\5\21\u0109\n\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\5\22\u0115\n\22\3\23\3\23")
        buf.write("\3\23\3\23\5\23\u011b\n\23\3\24\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0129\n\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\5\34\u014e\n\34\3\35\3\35\3\35\3\36\3\36\3\36\3")
        buf.write("\37\3\37\3\37\3 \3 \5 \u015b\n \3!\3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3\"\3#\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\5")
        buf.write("%\u0174\n%\3&\3&\3&\3&\3&\5&\u017b\n&\3\'\3\'\3\'\3\'")
        buf.write("\5\'\u0181\n\'\3(\3(\3(\3(\3(\3(\3(\3(\5(\u018b\n(\3)")
        buf.write("\3)\3)\3)\3)\5)\u0192\n)\3*\3*\3*\3*\3*\5*\u0199\n*\3")
        buf.write("+\3+\3+\3+\3+\3+\7+\u01a1\n+\f+\16+\u01a4\13+\3,\3,\3")
        buf.write(",\3,\3,\3,\7,\u01ac\n,\f,\16,\u01af\13,\3-\3-\3-\3-\3")
        buf.write("-\3-\7-\u01b7\n-\f-\16-\u01ba\13-\3.\3.\3.\5.\u01bf\n")
        buf.write(".\3/\3/\3/\5/\u01c4\n/\3\60\3\60\3\60\3\60\3\60\7\60\u01cb")
        buf.write("\n\60\f\60\16\60\u01ce\13\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u01d6\n\61\3\61\7\61\u01d9\n\61\f\61\16\61")
        buf.write("\u01dc\13\61\3\62\3\62\3\62\5\62\u01e1\n\62\3\63\3\63")
        buf.write("\3\63\3\63\3\63\3\63\3\63\5\63\u01ea\n\63\3\64\3\64\3")
        buf.write("\64\3\64\3\64\5\64\u01f1\n\64\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0200\n")
        buf.write("\66\3\67\3\67\3\67\3\67\5\67\u0206\n\67\38\38\38\38\3")
        buf.write("8\38\58\u020e\n8\39\39\39\39\59\u0214\n9\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\5:\u021e\n:\3;\3;\3;\3;\5;\u0224\n;\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\5<\u022e\n<\3=\3=\3=\3=\3=\3=\5=\u0236")
        buf.write("\n=\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\5?\u0243\n?\3@\3")
        buf.write("@\3@\3@\3@\3@\5@\u024b\n@\3A\3A\3A\3A\3A\3A\5A\u0253\n")
        buf.write("A\3B\3B\3B\3B\3C\3C\3C\3C\3C\5C\u025e\nC\3D\3D\3D\3D\3")
        buf.write("D\5D\u0265\nD\3E\3E\5E\u0269\nE\3E\3E\3E\3E\3E\5E\u0270")
        buf.write("\nE\3E\5E\u0273\nE\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3")
        buf.write("G\5G\u0281\nG\3H\3H\3I\3I\5I\u0287\nI\3I\2\7TVX^`J\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\2\n\3\2:;\3\2\25")
        buf.write("\26\3\2./\4\2\'\')-\3\2%&\3\2\37 \3\2!#\3\2\16\21\2\u0291")
        buf.write("\2\u0095\3\2\2\2\4\u009e\3\2\2\2\6\u00a0\3\2\2\2\b\u00a8")
        buf.write("\3\2\2\2\n\u00aa\3\2\2\2\f\u00b0\3\2\2\2\16\u00b5\3\2")
        buf.write("\2\2\20\u00bb\3\2\2\2\22\u00cd\3\2\2\2\24\u00d9\3\2\2")
        buf.write("\2\26\u00db\3\2\2\2\30\u00e7\3\2\2\2\32\u00f3\3\2\2\2")
        buf.write("\34\u00f5\3\2\2\2\36\u00fb\3\2\2\2 \u0104\3\2\2\2\"\u010a")
        buf.write("\3\2\2\2$\u011a\3\2\2\2&\u011c\3\2\2\2(\u0122\3\2\2\2")
        buf.write("*\u0128\3\2\2\2,\u012a\3\2\2\2.\u0135\3\2\2\2\60\u0139")
        buf.write("\3\2\2\2\62\u0140\3\2\2\2\64\u0144\3\2\2\2\66\u014d\3")
        buf.write("\2\2\28\u014f\3\2\2\2:\u0152\3\2\2\2<\u0155\3\2\2\2>\u015a")
        buf.write("\3\2\2\2@\u015c\3\2\2\2B\u0160\3\2\2\2D\u0164\3\2\2\2")
        buf.write("F\u0168\3\2\2\2H\u0173\3\2\2\2J\u017a\3\2\2\2L\u0180\3")
        buf.write("\2\2\2N\u018a\3\2\2\2P\u0191\3\2\2\2R\u0198\3\2\2\2T\u019a")
        buf.write("\3\2\2\2V\u01a5\3\2\2\2X\u01b0\3\2\2\2Z\u01be\3\2\2\2")
        buf.write("\\\u01c3\3\2\2\2^\u01c5\3\2\2\2`\u01cf\3\2\2\2b\u01e0")
        buf.write("\3\2\2\2d\u01e9\3\2\2\2f\u01f0\3\2\2\2h\u01f2\3\2\2\2")
        buf.write("j\u01ff\3\2\2\2l\u0205\3\2\2\2n\u020d\3\2\2\2p\u0213\3")
        buf.write("\2\2\2r\u021d\3\2\2\2t\u0223\3\2\2\2v\u022d\3\2\2\2x\u0235")
        buf.write("\3\2\2\2z\u0237\3\2\2\2|\u0242\3\2\2\2~\u024a\3\2\2\2")
        buf.write("\u0080\u0252\3\2\2\2\u0082\u0254\3\2\2\2\u0084\u025d\3")
        buf.write("\2\2\2\u0086\u0264\3\2\2\2\u0088\u0272\3\2\2\2\u008a\u0274")
        buf.write("\3\2\2\2\u008c\u0280\3\2\2\2\u008e\u0282\3\2\2\2\u0090")
        buf.write("\u0286\3\2\2\2\u0092\u0093\5P)\2\u0093\u0094\7\67\2\2")
        buf.write("\u0094\u0096\3\2\2\2\u0095\u0092\3\2\2\2\u0096\u0097\3")
        buf.write("\2\2\2\u0097\u0095\3\2\2\2\u0097\u0098\3\2\2\2\u0098\3")
        buf.write("\3\2\2\2\u0099\u009a\5\6\4\2\u009a\u009b\5\4\3\2\u009b")
        buf.write("\u009f\3\2\2\2\u009c\u009f\5\6\4\2\u009d\u009f\3\2\2\2")
        buf.write("\u009e\u0099\3\2\2\2\u009e\u009c\3\2\2\2\u009e\u009d\3")
        buf.write("\2\2\2\u009f\5\3\2\2\2\u00a0\u00a1\7\24\2\2\u00a1\u00a2")
        buf.write("\7:\2\2\u00a2\u00a3\5\b\5\2\u00a3\u00a4\5B\"\2\u00a4\7")
        buf.write("\3\2\2\2\u00a5\u00a6\78\2\2\u00a6\u00a9\7:\2\2\u00a7\u00a9")
        buf.write("\3\2\2\2\u00a8\u00a5\3\2\2\2\u00a8\u00a7\3\2\2\2\u00a9")
        buf.write("\t\3\2\2\2\u00aa\u00ab\7\27\2\2\u00ab\u00ac\7\60\2\2\u00ac")
        buf.write("\u00ad\5\u0080A\2\u00ad\u00ae\7\61\2\2\u00ae\u00af\5D")
        buf.write("#\2\u00af\13\3\2\2\2\u00b0\u00b1\7\30\2\2\u00b1\u00b2")
        buf.write("\7\60\2\2\u00b2\u00b3\7\61\2\2\u00b3\u00b4\5D#\2\u00b4")
        buf.write("\r\3\2\2\2\u00b5\u00b6\t\2\2\2\u00b6\u00b7\7\60\2\2\u00b7")
        buf.write("\u00b8\5\u0080A\2\u00b8\u00b9\7\61\2\2\u00b9\u00ba\5D")
        buf.write("#\2\u00ba\17\3\2\2\2\u00bb\u00c1\t\3\2\2\u00bc\u00c2\5")
        buf.write("\22\n\2\u00bd\u00be\5\u0084C\2\u00be\u00bf\78\2\2\u00bf")
        buf.write("\u00c0\5\u0090I\2\u00c0\u00c2\3\2\2\2\u00c1\u00bc\3\2")
        buf.write("\2\2\u00c1\u00bd\3\2\2\2\u00c2\u00c3\3\2\2\2\u00c3\u00c4")
        buf.write("\79\2\2\u00c4\21\3\2\2\2\u00c5\u00c6\t\2\2\2\u00c6\u00c7")
        buf.write("\5\24\13\2\u00c7\u00c8\5P)\2\u00c8\u00ce\3\2\2\2\u00c9")
        buf.write("\u00ca\5\u0084C\2\u00ca\u00cb\78\2\2\u00cb\u00cc\5\u0090")
        buf.write("I\2\u00cc\u00ce\3\2\2\2\u00cd\u00c5\3\2\2\2\u00cd\u00c9")
        buf.write("\3\2\2\2\u00ce\23\3\2\2\2\u00cf\u00d0\7\67\2\2\u00d0\u00d1")
        buf.write("\t\2\2\2\u00d1\u00d2\5\24\13\2\u00d2\u00d3\5P)\2\u00d3")
        buf.write("\u00d4\7\67\2\2\u00d4\u00da\3\2\2\2\u00d5\u00d6\78\2\2")
        buf.write("\u00d6\u00d7\5\u0090I\2\u00d7\u00d8\7(\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00cf\3\2\2\2\u00d9\u00d5\3\2\2\2\u00da")
        buf.write("\25\3\2\2\2\u00db\u00dc\t\3\2\2\u00dc\u00dd\5\30\r\2\u00dd")
        buf.write("\u00de\79\2\2\u00de\27\3\2\2\2\u00df\u00e0\7:\2\2\u00e0")
        buf.write("\u00e1\5\32\16\2\u00e1\u00e2\5P)\2\u00e2\u00e8\3\2\2\2")
        buf.write("\u00e3\u00e4\5\u0086D\2\u00e4\u00e5\78\2\2\u00e5\u00e6")
        buf.write("\5\u0090I\2\u00e6\u00e8\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7")
        buf.write("\u00e3\3\2\2\2\u00e8\31\3\2\2\2\u00e9\u00ea\7\67\2\2\u00ea")
        buf.write("\u00eb\7:\2\2\u00eb\u00ec\5\32\16\2\u00ec\u00ed\5P)\2")
        buf.write("\u00ed\u00ee\7\67\2\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0")
        buf.write("\78\2\2\u00f0\u00f1\5\u0090I\2\u00f1\u00f2\7(\2\2\u00f2")
        buf.write("\u00f4\3\2\2\2\u00f3\u00e9\3\2\2\2\u00f3\u00ef\3\2\2\2")
        buf.write("\u00f4\33\3\2\2\2\u00f5\u00f6\t\2\2\2\u00f6\u00f7\7\60")
        buf.write("\2\2\u00f7\u00f8\5\u0080A\2\u00f8\u00f9\7\61\2\2\u00f9")
        buf.write("\u00fa\5D#\2\u00fa\35\3\2\2\2\u00fb\u00fc\5 \21\2\u00fc")
        buf.write("\u00fd\7(\2\2\u00fd\u00fe\5P)\2\u00fe\u00ff\79\2\2\u00ff")
        buf.write("\37\3\2\2\2\u0100\u0105\7:\2\2\u0101\u0105\7;\2\2\u0102")
        buf.write("\u0105\5.\30\2\u0103\u0105\5\62\32\2\u0104\u0100\3\2\2")
        buf.write("\2\u0104\u0101\3\2\2\2\u0104\u0102\3\2\2\2\u0104\u0103")
        buf.write("\3\2\2\2\u0105\u0108\3\2\2\2\u0106\u0109\5j\66\2\u0107")
        buf.write("\u0109\3\2\2\2\u0108\u0106\3\2\2\2\u0108\u0107\3\2\2\2")
        buf.write("\u0109!\3\2\2\2\u010a\u010b\7\5\2\2\u010b\u010c\7\60\2")
        buf.write("\2\u010c\u010d\5P)\2\u010d\u010e\7\61\2\2\u010e\u0114")
        buf.write("\5D#\2\u010f\u0110\5$\23\2\u0110\u0111\5(\25\2\u0111\u0115")
        buf.write("\3\2\2\2\u0112\u0115\5(\25\2\u0113\u0115\3\2\2\2\u0114")
        buf.write("\u010f\3\2\2\2\u0114\u0112\3\2\2\2\u0114\u0113\3\2\2\2")
        buf.write("\u0115#\3\2\2\2\u0116\u0117\5&\24\2\u0117\u0118\5$\23")
        buf.write("\2\u0118\u011b\3\2\2\2\u0119\u011b\5&\24\2\u011a\u0116")
        buf.write("\3\2\2\2\u011a\u0119\3\2\2\2\u011b%\3\2\2\2\u011c\u011d")
        buf.write("\7\6\2\2\u011d\u011e\7\60\2\2\u011e\u011f\5P)\2\u011f")
        buf.write("\u0120\7\61\2\2\u0120\u0121\5D#\2\u0121\'\3\2\2\2\u0122")
        buf.write("\u0123\7\7\2\2\u0123\u0124\5D#\2\u0124)\3\2\2\2\u0125")
        buf.write("\u0126\7\32\2\2\u0126\u0129\5P)\2\u0127\u0129\3\2\2\2")
        buf.write("\u0128\u0125\3\2\2\2\u0128\u0127\3\2\2\2\u0129+\3\2\2")
        buf.write("\2\u012a\u012b\7\b\2\2\u012b\u012c\7\60\2\2\u012c\u012d")
        buf.write("\t\2\2\2\u012d\u012e\7\r\2\2\u012e\u012f\5P)\2\u012f\u0130")
        buf.write("\7\35\2\2\u0130\u0131\5P)\2\u0131\u0132\5*\26\2\u0132")
        buf.write("\u0133\7\61\2\2\u0133\u0134\5D#\2\u0134-\3\2\2\2\u0135")
        buf.write("\u0136\5P)\2\u0136\u0137\7\66\2\2\u0137\u0138\t\2\2\2")
        buf.write("\u0138/\3\2\2\2\u0139\u013a\5P)\2\u013a\u013b\7\66\2\2")
        buf.write("\u013b\u013c\t\2\2\2\u013c\u013d\7\60\2\2\u013d\u013e")
        buf.write("\5x=\2\u013e\u013f\7\61\2\2\u013f\61\3\2\2\2\u0140\u0141")
        buf.write("\5P)\2\u0141\u0142\7\34\2\2\u0142\u0143\7;\2\2\u0143\63")
        buf.write("\3\2\2\2\u0144\u0145\5P)\2\u0145\u0146\7\34\2\2\u0146")
        buf.write("\u0147\7;\2\2\u0147\u0148\7\60\2\2\u0148\u0149\5x=\2\u0149")
        buf.write("\u014a\7\61\2\2\u014a\65\3\2\2\2\u014b\u014e\5\60\31\2")
        buf.write("\u014c\u014e\5\64\33\2\u014d\u014b\3\2\2\2\u014d\u014c")
        buf.write("\3\2\2\2\u014e\67\3\2\2\2\u014f\u0150\5\66\34\2\u0150")
        buf.write("\u0151\79\2\2\u01519\3\2\2\2\u0152\u0153\7\3\2\2\u0153")
        buf.write("\u0154\79\2\2\u0154;\3\2\2\2\u0155\u0156\7\4\2\2\u0156")
        buf.write("\u0157\79\2\2\u0157=\3\2\2\2\u0158\u015b\5P)\2\u0159\u015b")
        buf.write("\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u0159\3\2\2\2\u015b")
        buf.write("?\3\2\2\2\u015c\u015d\7\22\2\2\u015d\u015e\5> \2\u015e")
        buf.write("\u015f\79\2\2\u015fA\3\2\2\2\u0160\u0161\7\64\2\2\u0161")
        buf.write("\u0162\5H%\2\u0162\u0163\7\65\2\2\u0163C\3\2\2\2\u0164")
        buf.write("\u0165\7\64\2\2\u0165\u0166\5J&\2\u0166\u0167\7\65\2\2")
        buf.write("\u0167E\3\2\2\2\u0168\u0169\7\64\2\2\u0169\u016a\5J&\2")
        buf.write("\u016a\u016b\7\22\2\2\u016b\u016c\79\2\2\u016c\u016d\7")
        buf.write("\65\2\2\u016dG\3\2\2\2\u016e\u016f\5L\'\2\u016f\u0170")
        buf.write("\5H%\2\u0170\u0174\3\2\2\2\u0171\u0174\5L\'\2\u0172\u0174")
        buf.write("\3\2\2\2\u0173\u016e\3\2\2\2\u0173\u0171\3\2\2\2\u0173")
        buf.write("\u0172\3\2\2\2\u0174I\3\2\2\2\u0175\u0176\5N(\2\u0176")
        buf.write("\u0177\5J&\2\u0177\u017b\3\2\2\2\u0178\u017b\5N(\2\u0179")
        buf.write("\u017b\3\2\2\2\u017a\u0175\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u0179\3\2\2\2\u017bK\3\2\2\2\u017c\u0181\5\20\t")
        buf.write("\2\u017d\u0181\5\34\17\2\u017e\u0181\5\n\6\2\u017f\u0181")
        buf.write("\5\f\7\2\u0180\u017c\3\2\2\2\u0180\u017d\3\2\2\2\u0180")
        buf.write("\u017e\3\2\2\2\u0180\u017f\3\2\2\2\u0181M\3\2\2\2\u0182")
        buf.write("\u018b\5\26\f\2\u0183\u018b\5\36\20\2\u0184\u018b\5\"")
        buf.write("\22\2\u0185\u018b\5,\27\2\u0186\u018b\58\35\2\u0187\u018b")
        buf.write("\5:\36\2\u0188\u018b\5<\37\2\u0189\u018b\5@!\2\u018a\u0182")
        buf.write("\3\2\2\2\u018a\u0183\3\2\2\2\u018a\u0184\3\2\2\2\u018a")
        buf.write("\u0185\3\2\2\2\u018a\u0186\3\2\2\2\u018a\u0187\3\2\2\2")
        buf.write("\u018a\u0188\3\2\2\2\u018a\u0189\3\2\2\2\u018bO\3\2\2")
        buf.write("\2\u018c\u018d\5R*\2\u018d\u018e\t\4\2\2\u018e\u018f\5")
        buf.write("R*\2\u018f\u0192\3\2\2\2\u0190\u0192\5R*\2\u0191\u018c")
        buf.write("\3\2\2\2\u0191\u0190\3\2\2\2\u0192Q\3\2\2\2\u0193\u0194")
        buf.write("\5T+\2\u0194\u0195\t\5\2\2\u0195\u0196\5T+\2\u0196\u0199")
        buf.write("\3\2\2\2\u0197\u0199\5T+\2\u0198\u0193\3\2\2\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199S\3\2\2\2\u019a\u019b\b+\1\2\u019b\u019c")
        buf.write("\5V,\2\u019c\u01a2\3\2\2\2\u019d\u019e\f\4\2\2\u019e\u019f")
        buf.write("\t\6\2\2\u019f\u01a1\5V,\2\u01a0\u019d\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("U\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\b,\1\2\u01a6")
        buf.write("\u01a7\5X-\2\u01a7\u01ad\3\2\2\2\u01a8\u01a9\f\4\2\2\u01a9")
        buf.write("\u01aa\t\7\2\2\u01aa\u01ac\5X-\2\u01ab\u01a8\3\2\2\2\u01ac")
        buf.write("\u01af\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2")
        buf.write("\u01aeW\3\2\2\2\u01af\u01ad\3\2\2\2\u01b0\u01b1\b-\1\2")
        buf.write("\u01b1\u01b2\5Z.\2\u01b2\u01b8\3\2\2\2\u01b3\u01b4\f\4")
        buf.write("\2\2\u01b4\u01b5\t\b\2\2\u01b5\u01b7\5Z.\2\u01b6\u01b3")
        buf.write("\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6\3\2\2\2\u01b8")
        buf.write("\u01b9\3\2\2\2\u01b9Y\3\2\2\2\u01ba\u01b8\3\2\2\2\u01bb")
        buf.write("\u01bc\7$\2\2\u01bc\u01bf\5Z.\2\u01bd\u01bf\5\\/\2\u01be")
        buf.write("\u01bb\3\2\2\2\u01be\u01bd\3\2\2\2\u01bf[\3\2\2\2\u01c0")
        buf.write("\u01c1\7 \2\2\u01c1\u01c4\5\\/\2\u01c2\u01c4\5^\60\2\u01c3")
        buf.write("\u01c0\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4]\3\2\2\2\u01c5")
        buf.write("\u01c6\b\60\1\2\u01c6\u01c7\5`\61\2\u01c7\u01cc\3\2\2")
        buf.write("\2\u01c8\u01c9\f\4\2\2\u01c9\u01cb\5j\66\2\u01ca\u01c8")
        buf.write("\3\2\2\2\u01cb\u01ce\3\2\2\2\u01cc\u01ca\3\2\2\2\u01cc")
        buf.write("\u01cd\3\2\2\2\u01cd_\3\2\2\2\u01ce\u01cc\3\2\2\2\u01cf")
        buf.write("\u01d0\b\61\1\2\u01d0\u01d1\5b\62\2\u01d1\u01da\3\2\2")
        buf.write("\2\u01d2\u01d5\f\4\2\2\u01d3\u01d6\5j\66\2\u01d4\u01d6")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d9\5p9\2\u01d8\u01d2\3\2\2\2\u01d9")
        buf.write("\u01dc\3\2\2\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2")
        buf.write("\u01dba\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01de\t\2\2")
        buf.write("\2\u01de\u01e1\5t;\2\u01df\u01e1\5d\63\2\u01e0\u01dd\3")
        buf.write("\2\2\2\u01e0\u01df\3\2\2\2\u01e1c\3\2\2\2\u01e2\u01e3")
        buf.write("\7\31\2\2\u01e3\u01e4\5P)\2\u01e4\u01e5\7\60\2\2\u01e5")
        buf.write("\u01e6\5x=\2\u01e6\u01e7\7\61\2\2\u01e7\u01ea\3\2\2\2")
        buf.write("\u01e8\u01ea\5f\64\2\u01e9\u01e2\3\2\2\2\u01e9\u01e8\3")
        buf.write("\2\2\2\u01eae\3\2\2\2\u01eb\u01f1\5~@\2\u01ec\u01f1\7")
        buf.write(":\2\2\u01ed\u01f1\7;\2\2\u01ee\u01f1\7\33\2\2\u01ef\u01f1")
        buf.write("\5h\65\2\u01f0\u01eb\3\2\2\2\u01f0\u01ec\3\2\2\2\u01f0")
        buf.write("\u01ed\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2")
        buf.write("\u01f1g\3\2\2\2\u01f2\u01f3\7\60\2\2\u01f3\u01f4\5P)\2")
        buf.write("\u01f4\u01f5\7\61\2\2\u01f5i\3\2\2\2\u01f6\u01f7\7\62")
        buf.write("\2\2\u01f7\u01f8\5P)\2\u01f8\u01f9\7\63\2\2\u01f9\u01fa")
        buf.write("\5j\66\2\u01fa\u0200\3\2\2\2\u01fb\u01fc\7\62\2\2\u01fc")
        buf.write("\u01fd\5P)\2\u01fd\u01fe\7\63\2\2\u01fe\u0200\3\2\2\2")
        buf.write("\u01ff\u01f6\3\2\2\2\u01ff\u01fb\3\2\2\2\u0200k\3\2\2")
        buf.write("\2\u0201\u0206\5n8\2\u0202\u0203\5n8\2\u0203\u0204\5j")
        buf.write("\66\2\u0204\u0206\3\2\2\2\u0205\u0201\3\2\2\2\u0205\u0202")
        buf.write("\3\2\2\2\u0206m\3\2\2\2\u0207\u020e\t\2\2\2\u0208\u0209")
        buf.write("\5P)\2\u0209\u020a\5.\30\2\u020a\u020b\t\2\2\2\u020b\u020e")
        buf.write("\3\2\2\2\u020c\u020e\3\2\2\2\u020d\u0207\3\2\2\2\u020d")
        buf.write("\u0208\3\2\2\2\u020d\u020c\3\2\2\2\u020eo\3\2\2\2\u020f")
        buf.write("\u0210\5r:\2\u0210\u0211\5p9\2\u0211\u0214\3\2\2\2\u0212")
        buf.write("\u0214\5r:\2\u0213\u020f\3\2\2\2\u0213\u0212\3\2\2\2\u0214")
        buf.write("q\3\2\2\2\u0215\u0216\7\66\2\2\u0216\u021e\t\2\2\2\u0217")
        buf.write("\u0218\7\66\2\2\u0218\u0219\t\2\2\2\u0219\u021a\7\60\2")
        buf.write("\2\u021a\u021b\5x=\2\u021b\u021c\7\61\2\2\u021c\u021e")
        buf.write("\3\2\2\2\u021d\u0215\3\2\2\2\u021d\u0217\3\2\2\2\u021e")
        buf.write("s\3\2\2\2\u021f\u0220\5v<\2\u0220\u0221\5t;\2\u0221\u0224")
        buf.write("\3\2\2\2\u0222\u0224\5v<\2\u0223\u021f\3\2\2\2\u0223\u0222")
        buf.write("\3\2\2\2\u0224u\3\2\2\2\u0225\u0226\7\34\2\2\u0226\u022e")
        buf.write("\7;\2\2\u0227\u0228\7\34\2\2\u0228\u0229\7;\2\2\u0229")
        buf.write("\u022a\7\60\2\2\u022a\u022b\5x=\2\u022b\u022c\7\61\2\2")
        buf.write("\u022c\u022e\3\2\2\2\u022d\u0225\3\2\2\2\u022d\u0227\3")
        buf.write("\2\2\2\u022ew\3\2\2\2\u022f\u0230\5P)\2\u0230\u0231\7")
        buf.write("\67\2\2\u0231\u0232\5x=\2\u0232\u0236\3\2\2\2\u0233\u0236")
        buf.write("\5P)\2\u0234\u0236\3\2\2\2\u0235\u022f\3\2\2\2\u0235\u0233")
        buf.write("\3\2\2\2\u0235\u0234\3\2\2\2\u0236y\3\2\2\2\u0237\u0238")
        buf.write("\7\f\2\2\u0238\u0239\7\60\2\2\u0239\u023a\5|?\2\u023a")
        buf.write("\u023b\7\61\2\2\u023b{\3\2\2\2\u023c\u023d\5P)\2\u023d")
        buf.write("\u023e\7\67\2\2\u023e\u023f\5|?\2\u023f\u0243\3\2\2\2")
        buf.write("\u0240\u0243\5P)\2\u0241\u0243\3\2\2\2\u0242\u023c\3\2")
        buf.write("\2\2\u0242\u0240\3\2\2\2\u0242\u0241\3\2\2\2\u0243}\3")
        buf.write("\2\2\2\u0244\u024b\7>\2\2\u0245\u024b\7?\2\2\u0246\u024b")
        buf.write("\7=\2\2\u0247\u024b\7\t\2\2\u0248\u024b\7<\2\2\u0249\u024b")
        buf.write("\5z>\2\u024a\u0244\3\2\2\2\u024a\u0245\3\2\2\2\u024a\u0246")
        buf.write("\3\2\2\2\u024a\u0247\3\2\2\2\u024a\u0248\3\2\2\2\u024a")
        buf.write("\u0249\3\2\2\2\u024b\177\3\2\2\2\u024c\u024d\5\u0082B")
        buf.write("\2\u024d\u024e\79\2\2\u024e\u024f\5\u0080A\2\u024f\u0253")
        buf.write("\3\2\2\2\u0250\u0253\5\u0082B\2\u0251\u0253\3\2\2\2\u0252")
        buf.write("\u024c\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0251\3\2\2\2")
        buf.write("\u0253\u0081\3\2\2\2\u0254\u0255\5\u0084C\2\u0255\u0256")
        buf.write("\78\2\2\u0256\u0257\5\u0090I\2\u0257\u0083\3\2\2\2\u0258")
        buf.write("\u0259\t\2\2\2\u0259\u025a\7\67\2\2\u025a\u025e\5\u0084")
        buf.write("C\2\u025b\u025e\t\2\2\2\u025c\u025e\3\2\2\2\u025d\u0258")
        buf.write("\3\2\2\2\u025d\u025b\3\2\2\2\u025d\u025c\3\2\2\2\u025e")
        buf.write("\u0085\3\2\2\2\u025f\u0260\7:\2\2\u0260\u0261\7\67\2\2")
        buf.write("\u0261\u0265\5\u0086D\2\u0262\u0265\7:\2\2\u0263\u0265")
        buf.write("\3\2\2\2\u0264\u025f\3\2\2\2\u0264\u0262\3\2\2\2\u0264")
        buf.write("\u0263\3\2\2\2\u0265\u0087\3\2\2\2\u0266\u0269\5~@\2\u0267")
        buf.write("\u0269\5P)\2\u0268\u0266\3\2\2\2\u0268\u0267\3\2\2\2\u0269")
        buf.write("\u026a\3\2\2\2\u026a\u026b\7\67\2\2\u026b\u026c\5\u0088")
        buf.write("E\2\u026c\u0273\3\2\2\2\u026d\u0270\5~@\2\u026e\u0270")
        buf.write("\5P)\2\u026f\u026d\3\2\2\2\u026f\u026e\3\2\2\2\u0270\u0273")
        buf.write("\3\2\2\2\u0271\u0273\3\2\2\2\u0272\u0268\3\2\2\2\u0272")
        buf.write("\u026f\3\2\2\2\u0272\u0271\3\2\2\2\u0273\u0089\3\2\2\2")
        buf.write("\u0274\u0275\7\f\2\2\u0275\u0276\7\62\2\2\u0276\u0277")
        buf.write("\5\u008cG\2\u0277\u0278\7\67\2\2\u0278\u0279\7>\2\2\u0279")
        buf.write("\u027a\7\63\2\2\u027a\u008b\3\2\2\2\u027b\u0281\5\u008a")
        buf.write("F\2\u027c\u0281\7\16\2\2\u027d\u0281\7\17\2\2\u027e\u0281")
        buf.write("\7\20\2\2\u027f\u0281\7\21\2\2\u0280\u027b\3\2\2\2\u0280")
        buf.write("\u027c\3\2\2\2\u0280\u027d\3\2\2\2\u0280\u027e\3\2\2\2")
        buf.write("\u0280\u027f\3\2\2\2\u0281\u008d\3\2\2\2\u0282\u0283\t")
        buf.write("\t\2\2\u0283\u008f\3\2\2\2\u0284\u0287\5\u008eH\2\u0285")
        buf.write("\u0287\5\u008aF\2\u0286\u0284\3\2\2\2\u0286\u0285\3\2")
        buf.write("\2\2\u0287\u0091\3\2\2\2\64\u0097\u009e\u00a8\u00c1\u00cd")
        buf.write("\u00d9\u00e7\u00f3\u0104\u0108\u0114\u011a\u0128\u014d")
        buf.write("\u015a\u0173\u017a\u0180\u018a\u0191\u0198\u01a2\u01ad")
        buf.write("\u01b8\u01be\u01c3\u01cc\u01d5\u01da\u01e0\u01e9\u01f0")
        buf.write("\u01ff\u0205\u020d\u0213\u021d\u0223\u022d\u0235\u0242")
        buf.write("\u024a\u0252\u025d\u0264\u0268\u026f\u0272\u0280\u0286")
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 144
                self.expr()
                self.state = 145
                self.match(D96Parser.COMMA)
                self.state = 149 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUSOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT_IN_ARRAY) | (1 << D96Parser.INTLIT))) != 0)):
                    break

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
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
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
            self.state = 158
            self.match(D96Parser.CLASS)
            self.state = 159
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 160
            self.class_inheritance()
            self.state = 161
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
            self.state = 166
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(D96Parser.COLON)
                self.state = 164
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
            self.state = 168
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 169
            self.match(D96Parser.LB)
            self.state = 170
            self.list_parameters()
            self.state = 171
            self.match(D96Parser.RB)
            self.state = 172
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
            self.state = 174
            self.match(D96Parser.DESTRUCTOR)
            self.state = 175
            self.match(D96Parser.LB)
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
            self.state = 179
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 180
            self.match(D96Parser.LB)
            self.state = 181
            self.list_parameters()
            self.state = 182
            self.match(D96Parser.RB)
            self.state = 183
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
            self.state = 185
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 186
                self.declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 187
                self.identifier_list()
                self.state = 188
                self.match(D96Parser.COLON)
                self.state = 189
                self.variable_type()
                pass


            self.state = 193
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
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.type_and_assign()
                self.state = 197
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.identifier_list()
                self.state = 200
                self.match(D96Parser.COLON)
                self.state = 201
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
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(D96Parser.COMMA)
                self.state = 206
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 207
                self.type_and_assign()
                self.state = 208
                self.expr()
                self.state = 209
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.match(D96Parser.COLON)
                self.state = 212
                self.variable_type()
                self.state = 213
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
            self.state = 217
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 218
            self.declare_initiate_in_func_list()
            self.state = 219
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
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 222
                self.type_and_assign_in_func()
                self.state = 223
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.variable_in_func_identifier_list()
                self.state = 226
                self.match(D96Parser.COLON)
                self.state = 227
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
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(D96Parser.COMMA)
                self.state = 232
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 233
                self.type_and_assign_in_func()
                self.state = 234
                self.expr()
                self.state = 235
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.match(D96Parser.COLON)
                self.state = 238
                self.variable_type()
                self.state = 239
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
            self.state = 243
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 244
            self.match(D96Parser.LB)
            self.state = 245
            self.list_parameters()
            self.state = 246
            self.match(D96Parser.RB)
            self.state = 247
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
            self.state = 249
            self.lhs()
            self.state = 250
            self.match(D96Parser.ASSIGNOP)
            self.state = 251
            self.expr()
            self.state = 252
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
            self.state = 258
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 254
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 255
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.state = 256
                self.instance_attr_access()
                pass

            elif la_ == 4:
                self.state = 257
                self.static_attr_access()
                pass


            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 260
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
            self.state = 264
            self.match(D96Parser.IF)
            self.state = 265
            self.match(D96Parser.LB)
            self.state = 266
            self.expr()
            self.state = 267
            self.match(D96Parser.RB)
            self.state = 268
            self.block_statements()
            self.state = 274
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 269
                self.elseif_list_statements()
                self.state = 270
                self.else_statement()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 272
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
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.elseif_statement()
                self.state = 277
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
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
            self.state = 282
            self.match(D96Parser.ELSEIF)
            self.state = 283
            self.match(D96Parser.LB)
            self.state = 284
            self.expr()
            self.state = 285
            self.match(D96Parser.RB)
            self.state = 286
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
            self.state = 288
            self.match(D96Parser.ELSE)
            self.state = 289
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
            self.state = 294
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(D96Parser.BY)
                self.state = 292
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
            self.state = 296
            self.match(D96Parser.FOREACH)
            self.state = 297
            self.match(D96Parser.LB)
            self.state = 298
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 299
            self.match(D96Parser.IN)
            self.state = 300
            self.expr()
            self.state = 301
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 302
            self.expr()
            self.state = 303
            self.by_expr()
            self.state = 304
            self.match(D96Parser.RB)
            self.state = 305
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
            self.state = 311
            self.expr()
            self.state = 312
            self.match(D96Parser.DOT)
            self.state = 313
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 314
            self.match(D96Parser.LB)
            self.state = 315
            self.list_expr()
            self.state = 316
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
            self.state = 318
            self.expr()
            self.state = 319
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 320
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
            self.state = 322
            self.expr()
            self.state = 323
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 324
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 325
            self.match(D96Parser.LB)
            self.state = 326
            self.list_expr()
            self.state = 327
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
            self.state = 331
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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
            self.state = 333
            self.method_invocation()
            self.state = 334
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
            self.state = 336
            self.match(D96Parser.BREAK)
            self.state = 337
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
            self.state = 339
            self.match(D96Parser.CONTINUE)
            self.state = 340
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
            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
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
            self.state = 346
            self.match(D96Parser.RETURN)
            self.state = 347
            self.return_expr()
            self.state = 348
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
            self.state = 350
            self.match(D96Parser.LCB)
            self.state = 351
            self.statements_class()
            self.state = 352
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
            self.state = 354
            self.match(D96Parser.LCB)
            self.state = 355
            self.statements()
            self.state = 356
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
            self.state = 358
            self.match(D96Parser.LCB)
            self.state = 359
            self.statements()
            self.state = 360
            self.match(D96Parser.RETURN)
            self.state = 361
            self.match(D96Parser.SEMICOLON)
            self.state = 362
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
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.statement_class()
                self.state = 365
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
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
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 371
                self.statement()
                self.state = 372
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
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
            self.state = 382
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.variable_declaration()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
                self.function_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 380
                self.constructor_dclr()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 381
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
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.variable_in_func_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 386
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 387
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 388
                self.method_invocation_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 389
                self.break_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 390
                self.continue_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 391
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
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.expr1()
                self.state = 395
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 396
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
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
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.expr2(0)
                self.state = 402
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 403
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
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
            self.state = 409
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.expr3(0) 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
            self.state = 420
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 427
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 422
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 423
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 424
                    self.expr4(0) 
                self.state = 429
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 431
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 438
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 433
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 434
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 435
                    self.expr5() 
                self.state = 440
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
            self.state = 444
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.match(D96Parser.NOTOP)
                self.state = 442
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 443
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
            self.state = 449
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(D96Parser.MINUSOP)
                self.state = 447
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
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
            self.state = 452
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 458
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 454
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 455
                    self.index_operators() 
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
            self.state = 462
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 464
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 467
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.LSB]:
                        self.state = 465
                        self.index_operators()
                        pass
                    elif token in [D96Parser.DOT]:
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 469
                    self.instance_accesses() 
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
            self.state = 478
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 476
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
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
            self.state = 487
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(D96Parser.NEW)
                self.state = 481
                self.expr()
                self.state = 482
                self.match(D96Parser.LB)
                self.state = 483
                self.list_expr()
                self.state = 484
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 486
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
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 492
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 493
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
            self.state = 496
            self.match(D96Parser.LB)
            self.state = 497
            self.expr()
            self.state = 498
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
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 500
                self.match(D96Parser.LSB)
                self.state = 501
                self.expr()
                self.state = 502
                self.match(D96Parser.RSB)
                self.state = 503
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 505
                self.match(D96Parser.LSB)
                self.state = 506
                self.expr()
                self.state = 507
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
            self.state = 515
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.index()
                self.state = 513
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
            self.state = 523
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 517
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
                self.expr()
                self.state = 519
                self.instance_attr_access()
                self.state = 520
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
            self.state = 529
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.instance_access()
                self.state = 526
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
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
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 531
                self.match(D96Parser.DOT)
                self.state = 532
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 533
                self.match(D96Parser.DOT)
                self.state = 534
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 535
                self.match(D96Parser.LB)
                self.state = 536
                self.list_expr()
                self.state = 537
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
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.static_access()
                self.state = 542
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
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
            self.state = 555
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 548
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 550
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 551
                self.match(D96Parser.LB)
                self.state = 552
                self.list_expr()
                self.state = 553
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
            self.state = 563
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                self.expr()
                self.state = 558
                self.match(D96Parser.COMMA)
                self.state = 559
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
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
            self.state = 565
            self.match(D96Parser.ARRAY)
            self.state = 566
            self.match(D96Parser.LB)
            self.state = 567
            self.array_val()
            self.state = 568
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
            self.state = 576
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 570
                self.expr()
                self.state = 571
                self.match(D96Parser.COMMA)
                self.state = 572
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
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
            self.state = 584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 579
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 580
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 581
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 582
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 583
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
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 586
                self.param()
                self.state = 587
                self.match(D96Parser.SEMICOLON)
                self.state = 588
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
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
            self.state = 594
            self.identifier_list()
            self.state = 595
            self.match(D96Parser.COLON)
            self.state = 596
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
            self.state = 603
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 599
                self.match(D96Parser.COMMA)
                self.state = 600
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
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
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 606
                self.match(D96Parser.COMMA)
                self.state = 607
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 608
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
            self.state = 624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 612
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 613
                    self.expr()
                    pass


                self.state = 616
                self.match(D96Parser.COMMA)
                self.state = 617
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 619
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 620
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
            self.state = 626
            self.match(D96Parser.ARRAY)
            self.state = 627
            self.match(D96Parser.LSB)
            self.state = 628
            self.array_element_type()
            self.state = 629
            self.match(D96Parser.COMMA)
            self.state = 630
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 631
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
            self.state = 638
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 633
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 634
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 635
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 636
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 637
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
            self.state = 640
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
            self.state = 644
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 642
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
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
         




