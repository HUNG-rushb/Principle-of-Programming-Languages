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
        buf.write("\u02e8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00b2\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\5\3\5\3\5\5\5\u00bc\n\5\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\5\n\u00df\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\5\r\u00f7\n\r\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\5\20\u010f\n\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0127\n\23\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\5\27\u013b\n\27\3")
        buf.write("\27\3\27\3\27\5\27\u0140\n\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\5\30\u0147\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5")
        buf.write("\31\u0150\n\31\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\5\34\u0160\n\34\3\34\3")
        buf.write("\34\5\34\u0164\n\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\5\37\u0174\n\37\3")
        buf.write(" \3 \3 \3 \3 \3!\3!\5!\u017d\n!\3\"\3\"\3\"\3#\3#\3#\5")
        buf.write("#\u0185\n#\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3$\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\3)\3)\5)\u01aa\n)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3")
        buf.write("-\3-\5-\u01b7\n-\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u01ca\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u01d1\n\62\3\63\3\63\3\63\3\63")
        buf.write("\3\63\3\63\3\63\5\63\u01da\n\63\3\64\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\5\64")
        buf.write("\u01ea\n\64\3\65\3\65\3\65\3\65\3\65\5\65\u01f1\n\65\3")
        buf.write("\66\3\66\3\66\3\66\3\66\5\66\u01f8\n\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\7\67\u0200\n\67\f\67\16\67\u0203\13\67")
        buf.write("\38\38\38\38\38\38\78\u020b\n8\f8\168\u020e\138\39\39")
        buf.write("\39\39\39\39\79\u0216\n9\f9\169\u0219\139\3:\3:\3:\5:")
        buf.write("\u021e\n:\3;\3;\3;\5;\u0223\n;\3<\3<\3<\3<\3<\7<\u022a")
        buf.write("\n<\f<\16<\u022d\13<\3=\3=\3=\3=\3=\7=\u0234\n=\f=\16")
        buf.write("=\u0237\13=\3>\3>\3>\5>\u023c\n>\3?\3?\3?\3?\3?\3?\3?")
        buf.write("\5?\u0245\n?\3@\3@\3@\3@\5@\u024b\n@\3A\3A\3A\3A\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\7B\u025b\nB\fB\16B\u025e\13")
        buf.write("B\3C\3C\3C\3C\5C\u0264\nC\3D\3D\3D\3D\3D\3D\5D\u026c\n")
        buf.write("D\3E\3E\3E\3E\5E\u0272\nE\3F\3F\3F\3F\3F\3F\3F\3F\5F\u027c")
        buf.write("\nF\3G\3G\3G\3G\5G\u0282\nG\3H\3H\3H\3H\3H\3H\3H\3H\5")
        buf.write("H\u028c\nH\3I\3I\3I\3I\3I\3I\5I\u0294\nI\3J\3J\3J\3J\3")
        buf.write("J\3K\3K\3K\3K\3K\3K\5K\u02a1\nK\3L\3L\3L\3L\3L\3L\5L\u02a9")
        buf.write("\nL\3M\3M\3M\3M\3M\3M\5M\u02b1\nM\3N\3N\3N\3N\3O\3O\3")
        buf.write("O\3O\3O\5O\u02bc\nO\3P\3P\3P\3P\3P\5P\u02c3\nP\3Q\3Q\5")
        buf.write("Q\u02c7\nQ\3Q\3Q\3Q\3Q\3Q\5Q\u02ce\nQ\3Q\5Q\u02d1\nQ\3")
        buf.write("R\3R\3R\3R\3R\3R\3R\3S\3S\3S\3S\3S\5S\u02df\nS\3T\3T\3")
        buf.write("U\3U\3U\5U\u02e6\nU\3U\2\blnpvx\u0082V\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\2\t\3")
        buf.write("\29:\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2\16\21\2")
        buf.write("\u02ed\2\u00aa\3\2\2\2\4\u00b1\3\2\2\2\6\u00b3\3\2\2\2")
        buf.write("\b\u00bb\3\2\2\2\n\u00bd\3\2\2\2\f\u00c3\3\2\2\2\16\u00c8")
        buf.write("\3\2\2\2\20\u00ce\3\2\2\2\22\u00de\3\2\2\2\24\u00e0\3")
        buf.write("\2\2\2\26\u00e6\3\2\2\2\30\u00f6\3\2\2\2\32\u00f8\3\2")
        buf.write("\2\2\34\u00fe\3\2\2\2\36\u010e\3\2\2\2 \u0110\3\2\2\2")
        buf.write("\"\u0116\3\2\2\2$\u0126\3\2\2\2&\u0128\3\2\2\2(\u012e")
        buf.write("\3\2\2\2*\u0133\3\2\2\2,\u0137\3\2\2\2.\u0146\3\2\2\2")
        buf.write("\60\u0148\3\2\2\2\62\u0151\3\2\2\2\64\u0157\3\2\2\2\66")
        buf.write("\u015f\3\2\2\28\u0165\3\2\2\2:\u0169\3\2\2\2<\u0173\3")
        buf.write("\2\2\2>\u0175\3\2\2\2@\u017c\3\2\2\2B\u017e\3\2\2\2D\u0184")
        buf.write("\3\2\2\2F\u0186\3\2\2\2H\u0191\3\2\2\2J\u0195\3\2\2\2")
        buf.write("L\u019c\3\2\2\2N\u01a0\3\2\2\2P\u01a9\3\2\2\2R\u01ab\3")
        buf.write("\2\2\2T\u01ae\3\2\2\2V\u01b1\3\2\2\2X\u01b6\3\2\2\2Z\u01b8")
        buf.write("\3\2\2\2\\\u01bc\3\2\2\2^\u01c0\3\2\2\2`\u01c9\3\2\2\2")
        buf.write("b\u01d0\3\2\2\2d\u01d9\3\2\2\2f\u01e9\3\2\2\2h\u01f0\3")
        buf.write("\2\2\2j\u01f7\3\2\2\2l\u01f9\3\2\2\2n\u0204\3\2\2\2p\u020f")
        buf.write("\3\2\2\2r\u021d\3\2\2\2t\u0222\3\2\2\2v\u0224\3\2\2\2")
        buf.write("x\u022e\3\2\2\2z\u023b\3\2\2\2|\u0244\3\2\2\2~\u024a\3")
        buf.write("\2\2\2\u0080\u024c\3\2\2\2\u0082\u0250\3\2\2\2\u0084\u0263")
        buf.write("\3\2\2\2\u0086\u026b\3\2\2\2\u0088\u0271\3\2\2\2\u008a")
        buf.write("\u027b\3\2\2\2\u008c\u0281\3\2\2\2\u008e\u028b\3\2\2\2")
        buf.write("\u0090\u0293\3\2\2\2\u0092\u0295\3\2\2\2\u0094\u02a0\3")
        buf.write("\2\2\2\u0096\u02a8\3\2\2\2\u0098\u02b0\3\2\2\2\u009a\u02b2")
        buf.write("\3\2\2\2\u009c\u02bb\3\2\2\2\u009e\u02c2\3\2\2\2\u00a0")
        buf.write("\u02d0\3\2\2\2\u00a2\u02d2\3\2\2\2\u00a4\u02de\3\2\2\2")
        buf.write("\u00a6\u02e0\3\2\2\2\u00a8\u02e5\3\2\2\2\u00aa\u00ab\5")
        buf.write("\4\3\2\u00ab\u00ac\7\2\2\3\u00ac\3\3\2\2\2\u00ad\u00ae")
        buf.write("\5\6\4\2\u00ae\u00af\5\4\3\2\u00af\u00b2\3\2\2\2\u00b0")
        buf.write("\u00b2\5\6\4\2\u00b1\u00ad\3\2\2\2\u00b1\u00b0\3\2\2\2")
        buf.write("\u00b2\5\3\2\2\2\u00b3\u00b4\7\24\2\2\u00b4\u00b5\79\2")
        buf.write("\2\u00b5\u00b6\5\b\5\2\u00b6\u00b7\5\\/\2\u00b7\7\3\2")
        buf.write("\2\2\u00b8\u00b9\7\67\2\2\u00b9\u00bc\79\2\2\u00ba\u00bc")
        buf.write("\3\2\2\2\u00bb\u00b8\3\2\2\2\u00bb\u00ba\3\2\2\2\u00bc")
        buf.write("\t\3\2\2\2\u00bd\u00be\7\27\2\2\u00be\u00bf\7/\2\2\u00bf")
        buf.write("\u00c0\5\u0098M\2\u00c0\u00c1\7\60\2\2\u00c1\u00c2\5^")
        buf.write("\60\2\u00c2\13\3\2\2\2\u00c3\u00c4\7\30\2\2\u00c4\u00c5")
        buf.write("\7/\2\2\u00c5\u00c6\7\60\2\2\u00c6\u00c7\5^\60\2\u00c7")
        buf.write("\r\3\2\2\2\u00c8\u00c9\7\26\2\2\u00c9\u00ca\5\u009eP\2")
        buf.write("\u00ca\u00cb\7\67\2\2\u00cb\u00cc\5\u00a8U\2\u00cc\u00cd")
        buf.write("\78\2\2\u00cd\17\3\2\2\2\u00ce\u00cf\7\26\2\2\u00cf\u00d0")
        buf.write("\79\2\2\u00d0\u00d1\5\22\n\2\u00d1\u00d2\5h\65\2\u00d2")
        buf.write("\u00d3\78\2\2\u00d3\21\3\2\2\2\u00d4\u00d5\7\66\2\2\u00d5")
        buf.write("\u00d6\79\2\2\u00d6\u00d7\5\22\n\2\u00d7\u00d8\5h\65\2")
        buf.write("\u00d8\u00d9\7\66\2\2\u00d9\u00df\3\2\2\2\u00da\u00db")
        buf.write("\7\67\2\2\u00db\u00dc\5\u00a8U\2\u00dc\u00dd\7\'\2\2\u00dd")
        buf.write("\u00df\3\2\2\2\u00de\u00d4\3\2\2\2\u00de\u00da\3\2\2\2")
        buf.write("\u00df\23\3\2\2\2\u00e0\u00e1\7\25\2\2\u00e1\u00e2\5\u009e")
        buf.write("P\2\u00e2\u00e3\7\67\2\2\u00e3\u00e4\5\u00a8U\2\u00e4")
        buf.write("\u00e5\78\2\2\u00e5\25\3\2\2\2\u00e6\u00e7\7\25\2\2\u00e7")
        buf.write("\u00e8\79\2\2\u00e8\u00e9\5\30\r\2\u00e9\u00ea\5h\65\2")
        buf.write("\u00ea\u00eb\78\2\2\u00eb\27\3\2\2\2\u00ec\u00ed\7\66")
        buf.write("\2\2\u00ed\u00ee\79\2\2\u00ee\u00ef\5\30\r\2\u00ef\u00f0")
        buf.write("\5h\65\2\u00f0\u00f1\7\66\2\2\u00f1\u00f7\3\2\2\2\u00f2")
        buf.write("\u00f3\7\67\2\2\u00f3\u00f4\5\u00a8U\2\u00f4\u00f5\7\'")
        buf.write("\2\2\u00f5\u00f7\3\2\2\2\u00f6\u00ec\3\2\2\2\u00f6\u00f2")
        buf.write("\3\2\2\2\u00f7\31\3\2\2\2\u00f8\u00f9\7\26\2\2\u00f9\u00fa")
        buf.write("\5\u009cO\2\u00fa\u00fb\7\67\2\2\u00fb\u00fc\5\u00a8U")
        buf.write("\2\u00fc\u00fd\78\2\2\u00fd\33\3\2\2\2\u00fe\u00ff\7\26")
        buf.write("\2\2\u00ff\u0100\t\2\2\2\u0100\u0101\5\36\20\2\u0101\u0102")
        buf.write("\5h\65\2\u0102\u0103\78\2\2\u0103\35\3\2\2\2\u0104\u0105")
        buf.write("\7\66\2\2\u0105\u0106\t\2\2\2\u0106\u0107\5\36\20\2\u0107")
        buf.write("\u0108\5h\65\2\u0108\u0109\7\66\2\2\u0109\u010f\3\2\2")
        buf.write("\2\u010a\u010b\7\67\2\2\u010b\u010c\5\u00a8U\2\u010c\u010d")
        buf.write("\7\'\2\2\u010d\u010f\3\2\2\2\u010e\u0104\3\2\2\2\u010e")
        buf.write("\u010a\3\2\2\2\u010f\37\3\2\2\2\u0110\u0111\7\25\2\2\u0111")
        buf.write("\u0112\5\u009cO\2\u0112\u0113\7\67\2\2\u0113\u0114\5\u00a8")
        buf.write("U\2\u0114\u0115\78\2\2\u0115!\3\2\2\2\u0116\u0117\7\25")
        buf.write("\2\2\u0117\u0118\t\2\2\2\u0118\u0119\5$\23\2\u0119\u011a")
        buf.write("\5h\65\2\u011a\u011b\78\2\2\u011b#\3\2\2\2\u011c\u011d")
        buf.write("\7\66\2\2\u011d\u011e\t\2\2\2\u011e\u011f\5$\23\2\u011f")
        buf.write("\u0120\5h\65\2\u0120\u0121\7\66\2\2\u0121\u0127\3\2\2")
        buf.write("\2\u0122\u0123\7\67\2\2\u0123\u0124\5\u00a8U\2\u0124\u0125")
        buf.write("\7\'\2\2\u0125\u0127\3\2\2\2\u0126\u011c\3\2\2\2\u0126")
        buf.write("\u0122\3\2\2\2\u0127%\3\2\2\2\u0128\u0129\t\2\2\2\u0129")
        buf.write("\u012a\7/\2\2\u012a\u012b\5\u0098M\2\u012b\u012c\7\60")
        buf.write("\2\2\u012c\u012d\5^\60\2\u012d\'\3\2\2\2\u012e\u012f\5")
        buf.write(",\27\2\u012f\u0130\5.\30\2\u0130\u0131\5\62\32\2\u0131")
        buf.write("\u0132\78\2\2\u0132)\3\2\2\2\u0133\u0134\5,\27\2\u0134")
        buf.write("\u0135\5.\30\2\u0135\u0136\5\62\32\2\u0136+\3\2\2\2\u0137")
        buf.write("\u013a\t\2\2\2\u0138\u013b\5\u0082B\2\u0139\u013b\3\2")
        buf.write("\2\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2\2\2\u013b\u013f")
        buf.write("\3\2\2\2\u013c\u013d\7\34\2\2\u013d\u0140\7:\2\2\u013e")
        buf.write("\u0140\3\2\2\2\u013f\u013c\3\2\2\2\u013f\u013e\3\2\2\2")
        buf.write("\u0140-\3\2\2\2\u0141\u0142\5\60\31\2\u0142\u0143\5.\30")
        buf.write("\2\u0143\u0147\3\2\2\2\u0144\u0147\5\60\31\2\u0145\u0147")
        buf.write("\3\2\2\2\u0146\u0141\3\2\2\2\u0146\u0144\3\2\2\2\u0146")
        buf.write("\u0145\3\2\2\2\u0147/\3\2\2\2\u0148\u014f\7\65\2\2\u0149")
        buf.write("\u0150\79\2\2\u014a\u014b\79\2\2\u014b\u014c\7/\2\2\u014c")
        buf.write("\u014d\5\u00a0Q\2\u014d\u014e\7\60\2\2\u014e\u0150\3\2")
        buf.write("\2\2\u014f\u0149\3\2\2\2\u014f\u014a\3\2\2\2\u0150\61")
        buf.write("\3\2\2\2\u0151\u0152\7\65\2\2\u0152\u0153\79\2\2\u0153")
        buf.write("\u0154\7/\2\2\u0154\u0155\5\u00a0Q\2\u0155\u0156\7\60")
        buf.write("\2\2\u0156\63\3\2\2\2\u0157\u0158\5\66\34\2\u0158\u0159")
        buf.write("\7\'\2\2\u0159\u015a\5h\65\2\u015a\u015b\78\2\2\u015b")
        buf.write("\65\3\2\2\2\u015c\u0160\79\2\2\u015d\u0160\5H%\2\u015e")
        buf.write("\u0160\5L\'\2\u015f\u015c\3\2\2\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u015e\3\2\2\2\u0160\u0163\3\2\2\2\u0161\u0164\5")
        buf.write("\u0082B\2\u0162\u0164\3\2\2\2\u0163\u0161\3\2\2\2\u0163")
        buf.write("\u0162\3\2\2\2\u0164\67\3\2\2\2\u0165\u0166\7/\2\2\u0166")
        buf.write("\u0167\5h\65\2\u0167\u0168\7\60\2\2\u01689\3\2\2\2\u0169")
        buf.write("\u016a\7\5\2\2\u016a\u016b\58\35\2\u016b\u016c\5^\60\2")
        buf.write("\u016c\u016d\5<\37\2\u016d;\3\2\2\2\u016e\u016f\5> \2")
        buf.write("\u016f\u0170\5<\37\2\u0170\u0174\3\2\2\2\u0171\u0174\5")
        buf.write("> \2\u0172\u0174\5@!\2\u0173\u016e\3\2\2\2\u0173\u0171")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174=\3\2\2\2\u0175\u0176")
        buf.write("\7\6\2\2\u0176\u0177\58\35\2\u0177\u0178\5^\60\2\u0178")
        buf.write("\u0179\5@!\2\u0179?\3\2\2\2\u017a\u017d\5B\"\2\u017b\u017d")
        buf.write("\3\2\2\2\u017c\u017a\3\2\2\2\u017c\u017b\3\2\2\2\u017d")
        buf.write("A\3\2\2\2\u017e\u017f\7\7\2\2\u017f\u0180\5^\60\2\u0180")
        buf.write("C\3\2\2\2\u0181\u0182\7\32\2\2\u0182\u0185\5h\65\2\u0183")
        buf.write("\u0185\3\2\2\2\u0184\u0181\3\2\2\2\u0184\u0183\3\2\2\2")
        buf.write("\u0185E\3\2\2\2\u0186\u0187\7\b\2\2\u0187\u0188\7/\2\2")
        buf.write("\u0188\u0189\t\2\2\2\u0189\u018a\7\r\2\2\u018a\u018b\5")
        buf.write("h\65\2\u018b\u018c\7\35\2\2\u018c\u018d\5h\65\2\u018d")
        buf.write("\u018e\5D#\2\u018e\u018f\7\60\2\2\u018f\u0190\5^\60\2")
        buf.write("\u0190G\3\2\2\2\u0191\u0192\5h\65\2\u0192\u0193\7\65\2")
        buf.write("\2\u0193\u0194\79\2\2\u0194I\3\2\2\2\u0195\u0196\5h\65")
        buf.write("\2\u0196\u0197\7\65\2\2\u0197\u0198\79\2\2\u0198\u0199")
        buf.write("\7/\2\2\u0199\u019a\5\u0090I\2\u019a\u019b\7\60\2\2\u019b")
        buf.write("K\3\2\2\2\u019c\u019d\t\2\2\2\u019d\u019e\7\34\2\2\u019e")
        buf.write("\u019f\7:\2\2\u019fM\3\2\2\2\u01a0\u01a1\t\2\2\2\u01a1")
        buf.write("\u01a2\7\34\2\2\u01a2\u01a3\7:\2\2\u01a3\u01a4\7/\2\2")
        buf.write("\u01a4\u01a5\5\u0090I\2\u01a5\u01a6\7\60\2\2\u01a6O\3")
        buf.write("\2\2\2\u01a7\u01aa\5J&\2\u01a8\u01aa\5N(\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01a8\3\2\2\2\u01aaQ\3\2\2\2\u01ab\u01ac")
        buf.write("\5P)\2\u01ac\u01ad\78\2\2\u01adS\3\2\2\2\u01ae\u01af\7")
        buf.write("\3\2\2\u01af\u01b0\78\2\2\u01b0U\3\2\2\2\u01b1\u01b2\7")
        buf.write("\4\2\2\u01b2\u01b3\78\2\2\u01b3W\3\2\2\2\u01b4\u01b7\5")
        buf.write("h\65\2\u01b5\u01b7\3\2\2\2\u01b6\u01b4\3\2\2\2\u01b6\u01b5")
        buf.write("\3\2\2\2\u01b7Y\3\2\2\2\u01b8\u01b9\7\22\2\2\u01b9\u01ba")
        buf.write("\5X-\2\u01ba\u01bb\78\2\2\u01bb[\3\2\2\2\u01bc\u01bd\7")
        buf.write("\63\2\2\u01bd\u01be\5`\61\2\u01be\u01bf\7\64\2\2\u01bf")
        buf.write("]\3\2\2\2\u01c0\u01c1\7\63\2\2\u01c1\u01c2\5b\62\2\u01c2")
        buf.write("\u01c3\7\64\2\2\u01c3_\3\2\2\2\u01c4\u01c5\5d\63\2\u01c5")
        buf.write("\u01c6\5`\61\2\u01c6\u01ca\3\2\2\2\u01c7\u01ca\5d\63\2")
        buf.write("\u01c8\u01ca\3\2\2\2\u01c9\u01c4\3\2\2\2\u01c9\u01c7\3")
        buf.write("\2\2\2\u01c9\u01c8\3\2\2\2\u01caa\3\2\2\2\u01cb\u01cc")
        buf.write("\5f\64\2\u01cc\u01cd\5b\62\2\u01cd\u01d1\3\2\2\2\u01ce")
        buf.write("\u01d1\5f\64\2\u01cf\u01d1\3\2\2\2\u01d0\u01cb\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d0\u01cf\3\2\2\2\u01d1c\3\2\2")
        buf.write("\2\u01d2\u01da\5\34\17\2\u01d3\u01da\5\"\22\2\u01d4\u01da")
        buf.write("\5\32\16\2\u01d5\u01da\5 \21\2\u01d6\u01da\5&\24\2\u01d7")
        buf.write("\u01da\5\n\6\2\u01d8\u01da\5\f\7\2\u01d9\u01d2\3\2\2\2")
        buf.write("\u01d9\u01d3\3\2\2\2\u01d9\u01d4\3\2\2\2\u01d9\u01d5\3")
        buf.write("\2\2\2\u01d9\u01d6\3\2\2\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8")
        buf.write("\3\2\2\2\u01dae\3\2\2\2\u01db\u01ea\5\20\t\2\u01dc\u01ea")
        buf.write("\5\26\f\2\u01dd\u01ea\5\16\b\2\u01de\u01ea\5\24\13\2\u01df")
        buf.write("\u01ea\5\64\33\2\u01e0\u01ea\5\26\f\2\u01e1\u01ea\5\64")
        buf.write("\33\2\u01e2\u01ea\5:\36\2\u01e3\u01ea\5F$\2\u01e4\u01ea")
        buf.write("\5(\25\2\u01e5\u01ea\5R*\2\u01e6\u01ea\5T+\2\u01e7\u01ea")
        buf.write("\5V,\2\u01e8\u01ea\5Z.\2\u01e9\u01db\3\2\2\2\u01e9\u01dc")
        buf.write("\3\2\2\2\u01e9\u01dd\3\2\2\2\u01e9\u01de\3\2\2\2\u01e9")
        buf.write("\u01df\3\2\2\2\u01e9\u01e0\3\2\2\2\u01e9\u01e1\3\2\2\2")
        buf.write("\u01e9\u01e2\3\2\2\2\u01e9\u01e3\3\2\2\2\u01e9\u01e4\3")
        buf.write("\2\2\2\u01e9\u01e5\3\2\2\2\u01e9\u01e6\3\2\2\2\u01e9\u01e7")
        buf.write("\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eag\3\2\2\2\u01eb\u01ec")
        buf.write("\5j\66\2\u01ec\u01ed\t\3\2\2\u01ed\u01ee\5j\66\2\u01ee")
        buf.write("\u01f1\3\2\2\2\u01ef\u01f1\5j\66\2\u01f0\u01eb\3\2\2\2")
        buf.write("\u01f0\u01ef\3\2\2\2\u01f1i\3\2\2\2\u01f2\u01f3\5l\67")
        buf.write("\2\u01f3\u01f4\t\4\2\2\u01f4\u01f5\5l\67\2\u01f5\u01f8")
        buf.write("\3\2\2\2\u01f6\u01f8\5l\67\2\u01f7\u01f2\3\2\2\2\u01f7")
        buf.write("\u01f6\3\2\2\2\u01f8k\3\2\2\2\u01f9\u01fa\b\67\1\2\u01fa")
        buf.write("\u01fb\5n8\2\u01fb\u0201\3\2\2\2\u01fc\u01fd\f\4\2\2\u01fd")
        buf.write("\u01fe\t\5\2\2\u01fe\u0200\5n8\2\u01ff\u01fc\3\2\2\2\u0200")
        buf.write("\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2")
        buf.write("\u0202m\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\b8\1\2")
        buf.write("\u0205\u0206\5p9\2\u0206\u020c\3\2\2\2\u0207\u0208\f\4")
        buf.write("\2\2\u0208\u0209\t\6\2\2\u0209\u020b\5p9\2\u020a\u0207")
        buf.write("\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020do\3\2\2\2\u020e\u020c\3\2\2\2\u020f")
        buf.write("\u0210\b9\1\2\u0210\u0211\5r:\2\u0211\u0217\3\2\2\2\u0212")
        buf.write("\u0213\f\4\2\2\u0213\u0214\t\7\2\2\u0214\u0216\5r:\2\u0215")
        buf.write("\u0212\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3\2\2\2")
        buf.write("\u0217\u0218\3\2\2\2\u0218q\3\2\2\2\u0219\u0217\3\2\2")
        buf.write("\2\u021a\u021b\7#\2\2\u021b\u021e\5r:\2\u021c\u021e\5")
        buf.write("t;\2\u021d\u021a\3\2\2\2\u021d\u021c\3\2\2\2\u021es\3")
        buf.write("\2\2\2\u021f\u0220\7\37\2\2\u0220\u0223\5t;\2\u0221\u0223")
        buf.write("\5v<\2\u0222\u021f\3\2\2\2\u0222\u0221\3\2\2\2\u0223u")
        buf.write("\3\2\2\2\u0224\u0225\b<\1\2\u0225\u0226\5x=\2\u0226\u022b")
        buf.write("\3\2\2\2\u0227\u0228\f\4\2\2\u0228\u022a\5\u0082B\2\u0229")
        buf.write("\u0227\3\2\2\2\u022a\u022d\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022cw\3\2\2\2\u022d\u022b\3\2\2")
        buf.write("\2\u022e\u022f\b=\1\2\u022f\u0230\5z>\2\u0230\u0235\3")
        buf.write("\2\2\2\u0231\u0232\f\4\2\2\u0232\u0234\5\u0088E\2\u0233")
        buf.write("\u0231\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236y\3\2\2\2\u0237\u0235\3\2\2")
        buf.write("\2\u0238\u0239\79\2\2\u0239\u023c\5\u008cG\2\u023a\u023c")
        buf.write("\5|?\2\u023b\u0238\3\2\2\2\u023b\u023a\3\2\2\2\u023c{")
        buf.write("\3\2\2\2\u023d\u023e\7\31\2\2\u023e\u023f\5h\65\2\u023f")
        buf.write("\u0240\7/\2\2\u0240\u0241\5\u0090I\2\u0241\u0242\7\60")
        buf.write("\2\2\u0242\u0245\3\2\2\2\u0243\u0245\5~@\2\u0244\u023d")
        buf.write("\3\2\2\2\u0244\u0243\3\2\2\2\u0245}\3\2\2\2\u0246\u024b")
        buf.write("\5\u0096L\2\u0247\u024b\79\2\2\u0248\u024b\7\33\2\2\u0249")
        buf.write("\u024b\5\u0080A\2\u024a\u0246\3\2\2\2\u024a\u0247\3\2")
        buf.write("\2\2\u024a\u0248\3\2\2\2\u024a\u0249\3\2\2\2\u024b\177")
        buf.write("\3\2\2\2\u024c\u024d\7/\2\2\u024d\u024e\5h\65\2\u024e")
        buf.write("\u024f\7\60\2\2\u024f\u0081\3\2\2\2\u0250\u0251\bB\1\2")
        buf.write("\u0251\u0252\7\61\2\2\u0252\u0253\5h\65\2\u0253\u0254")
        buf.write("\7\62\2\2\u0254\u025c\3\2\2\2\u0255\u0256\f\4\2\2\u0256")
        buf.write("\u0257\7\61\2\2\u0257\u0258\5h\65\2\u0258\u0259\7\62\2")
        buf.write("\2\u0259\u025b\3\2\2\2\u025a\u0255\3\2\2\2\u025b\u025e")
        buf.write("\3\2\2\2\u025c\u025a\3\2\2\2\u025c\u025d\3\2\2\2\u025d")
        buf.write("\u0083\3\2\2\2\u025e\u025c\3\2\2\2\u025f\u0264\5\u0086")
        buf.write("D\2\u0260\u0261\5\u0086D\2\u0261\u0262\5\u0082B\2\u0262")
        buf.write("\u0264\3\2\2\2\u0263\u025f\3\2\2\2\u0263\u0260\3\2\2\2")
        buf.write("\u0264\u0085\3\2\2\2\u0265\u026c\t\2\2\2\u0266\u0267\5")
        buf.write("h\65\2\u0267\u0268\5H%\2\u0268\u0269\t\2\2\2\u0269\u026c")
        buf.write("\3\2\2\2\u026a\u026c\3\2\2\2\u026b\u0265\3\2\2\2\u026b")
        buf.write("\u0266\3\2\2\2\u026b\u026a\3\2\2\2\u026c\u0087\3\2\2\2")
        buf.write("\u026d\u026e\5\u008aF\2\u026e\u026f\5\u0088E\2\u026f\u0272")
        buf.write("\3\2\2\2\u0270\u0272\5\u008aF\2\u0271\u026d\3\2\2\2\u0271")
        buf.write("\u0270\3\2\2\2\u0272\u0089\3\2\2\2\u0273\u0274\7\65\2")
        buf.write("\2\u0274\u027c\79\2\2\u0275\u0276\7\65\2\2\u0276\u0277")
        buf.write("\79\2\2\u0277\u0278\7/\2\2\u0278\u0279\5\u0090I\2\u0279")
        buf.write("\u027a\7\60\2\2\u027a\u027c\3\2\2\2\u027b\u0273\3\2\2")
        buf.write("\2\u027b\u0275\3\2\2\2\u027c\u008b\3\2\2\2\u027d\u027e")
        buf.write("\5\u008eH\2\u027e\u027f\5\u008cG\2\u027f\u0282\3\2\2\2")
        buf.write("\u0280\u0282\5\u008eH\2\u0281\u027d\3\2\2\2\u0281\u0280")
        buf.write("\3\2\2\2\u0282\u008d\3\2\2\2\u0283\u0284\7\34\2\2\u0284")
        buf.write("\u028c\7:\2\2\u0285\u0286\7\34\2\2\u0286\u0287\7:\2\2")
        buf.write("\u0287\u0288\7/\2\2\u0288\u0289\5\u0090I\2\u0289\u028a")
        buf.write("\7\60\2\2\u028a\u028c\3\2\2\2\u028b\u0283\3\2\2\2\u028b")
        buf.write("\u0285\3\2\2\2\u028c\u008f\3\2\2\2\u028d\u028e\5h\65\2")
        buf.write("\u028e\u028f\7\66\2\2\u028f\u0290\5\u0090I\2\u0290\u0294")
        buf.write("\3\2\2\2\u0291\u0294\5h\65\2\u0292\u0294\3\2\2\2\u0293")
        buf.write("\u028d\3\2\2\2\u0293\u0291\3\2\2\2\u0293\u0292\3\2\2\2")
        buf.write("\u0294\u0091\3\2\2\2\u0295\u0296\7\f\2\2\u0296\u0297\7")
        buf.write("/\2\2\u0297\u0298\5\u0094K\2\u0298\u0299\7\60\2\2\u0299")
        buf.write("\u0093\3\2\2\2\u029a\u029b\5h\65\2\u029b\u029c\7\66\2")
        buf.write("\2\u029c\u029d\5\u0094K\2\u029d\u02a1\3\2\2\2\u029e\u02a1")
        buf.write("\5h\65\2\u029f\u02a1\3\2\2\2\u02a0\u029a\3\2\2\2\u02a0")
        buf.write("\u029e\3\2\2\2\u02a0\u029f\3\2\2\2\u02a1\u0095\3\2\2\2")
        buf.write("\u02a2\u02a9\7=\2\2\u02a3\u02a9\7>\2\2\u02a4\u02a9\7<")
        buf.write("\2\2\u02a5\u02a9\7\t\2\2\u02a6\u02a9\7;\2\2\u02a7\u02a9")
        buf.write("\5\u0092J\2\u02a8\u02a2\3\2\2\2\u02a8\u02a3\3\2\2\2\u02a8")
        buf.write("\u02a4\3\2\2\2\u02a8\u02a5\3\2\2\2\u02a8\u02a6\3\2\2\2")
        buf.write("\u02a8\u02a7\3\2\2\2\u02a9\u0097\3\2\2\2\u02aa\u02ab\5")
        buf.write("\u009aN\2\u02ab\u02ac\78\2\2\u02ac\u02ad\5\u0098M\2\u02ad")
        buf.write("\u02b1\3\2\2\2\u02ae\u02b1\5\u009aN\2\u02af\u02b1\3\2")
        buf.write("\2\2\u02b0\u02aa\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b0\u02af")
        buf.write("\3\2\2\2\u02b1\u0099\3\2\2\2\u02b2\u02b3\5\u009cO\2\u02b3")
        buf.write("\u02b4\7\67\2\2\u02b4\u02b5\5\u00a8U\2\u02b5\u009b\3\2")
        buf.write("\2\2\u02b6\u02b7\t\2\2\2\u02b7\u02b8\7\66\2\2\u02b8\u02bc")
        buf.write("\5\u009cO\2\u02b9\u02bc\t\2\2\2\u02ba\u02bc\3\2\2\2\u02bb")
        buf.write("\u02b6\3\2\2\2\u02bb\u02b9\3\2\2\2\u02bb\u02ba\3\2\2\2")
        buf.write("\u02bc\u009d\3\2\2\2\u02bd\u02be\79\2\2\u02be\u02bf\7")
        buf.write("\66\2\2\u02bf\u02c3\5\u009eP\2\u02c0\u02c3\79\2\2\u02c1")
        buf.write("\u02c3\3\2\2\2\u02c2\u02bd\3\2\2\2\u02c2\u02c0\3\2\2\2")
        buf.write("\u02c2\u02c1\3\2\2\2\u02c3\u009f\3\2\2\2\u02c4\u02c7\5")
        buf.write("\u0096L\2\u02c5\u02c7\5h\65\2\u02c6\u02c4\3\2\2\2\u02c6")
        buf.write("\u02c5\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02c9\7\66\2")
        buf.write("\2\u02c9\u02ca\5\u00a0Q\2\u02ca\u02d1\3\2\2\2\u02cb\u02ce")
        buf.write("\5\u0096L\2\u02cc\u02ce\5h\65\2\u02cd\u02cb\3\2\2\2\u02cd")
        buf.write("\u02cc\3\2\2\2\u02ce\u02d1\3\2\2\2\u02cf\u02d1\3\2\2\2")
        buf.write("\u02d0\u02c6\3\2\2\2\u02d0\u02cd\3\2\2\2\u02d0\u02cf\3")
        buf.write("\2\2\2\u02d1\u00a1\3\2\2\2\u02d2\u02d3\7\f\2\2\u02d3\u02d4")
        buf.write("\7\61\2\2\u02d4\u02d5\5\u00a4S\2\u02d5\u02d6\7\66\2\2")
        buf.write("\u02d6\u02d7\7=\2\2\u02d7\u02d8\7\62\2\2\u02d8\u00a3\3")
        buf.write("\2\2\2\u02d9\u02df\5\u00a2R\2\u02da\u02df\7\16\2\2\u02db")
        buf.write("\u02df\7\17\2\2\u02dc\u02df\7\20\2\2\u02dd\u02df\7\21")
        buf.write("\2\2\u02de\u02d9\3\2\2\2\u02de\u02da\3\2\2\2\u02de\u02db")
        buf.write("\3\2\2\2\u02de\u02dc\3\2\2\2\u02de\u02dd\3\2\2\2\u02df")
        buf.write("\u00a5\3\2\2\2\u02e0\u02e1\t\b\2\2\u02e1\u00a7\3\2\2\2")
        buf.write("\u02e2\u02e6\5\u00a6T\2\u02e3\u02e6\5\u00a2R\2\u02e4\u02e6")
        buf.write("\79\2\2\u02e5\u02e2\3\2\2\2\u02e5\u02e3\3\2\2\2\u02e5")
        buf.write("\u02e4\3\2\2\2\u02e6\u00a9\3\2\2\2\65\u00b1\u00bb\u00de")
        buf.write("\u00f6\u010e\u0126\u013a\u013f\u0146\u014f\u015f\u0163")
        buf.write("\u0173\u017c\u0184\u01a9\u01b6\u01c9\u01d0\u01d9\u01e9")
        buf.write("\u01f0\u01f7\u0201\u020c\u0217\u021d\u0222\u022b\u0235")
        buf.write("\u023b\u0244\u024a\u025c\u0263\u026b\u0271\u027b\u0281")
        buf.write("\u028b\u0293\u02a0\u02a8\u02b0\u02bb\u02c2\u02c6\u02cd")
        buf.write("\u02d0\u02de\u02e5")
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
    RULE_call_func_statement = 19
    RULE_call_func = 20
    RULE_call_func_header = 21
    RULE_call_func_attr_list = 22
    RULE_call_func_attr = 23
    RULE_call_func_end = 24
    RULE_assignment_statements = 25
    RULE_lhs = 26
    RULE_if_condition = 27
    RULE_if_statements = 28
    RULE_elseif_list_statements = 29
    RULE_elseif_statement = 30
    RULE_else_statement_or_none = 31
    RULE_else_statement = 32
    RULE_by_expr = 33
    RULE_forin_statements = 34
    RULE_instance_attr_access = 35
    RULE_instance_method_access = 36
    RULE_static_attr_access = 37
    RULE_static_method_access = 38
    RULE_method_invocation = 39
    RULE_method_invocation_statement = 40
    RULE_break_statements = 41
    RULE_continue_statements = 42
    RULE_return_expr = 43
    RULE_return_statements = 44
    RULE_block_class_statements = 45
    RULE_block_statements = 46
    RULE_statements_class = 47
    RULE_statements = 48
    RULE_statement_class = 49
    RULE_statement = 50
    RULE_expr = 51
    RULE_expr1 = 52
    RULE_expr2 = 53
    RULE_expr3 = 54
    RULE_expr4 = 55
    RULE_expr5 = 56
    RULE_expr6 = 57
    RULE_expr7 = 58
    RULE_expr8 = 59
    RULE_expr9 = 60
    RULE_expr10 = 61
    RULE_expr11 = 62
    RULE_expr12 = 63
    RULE_index_operators = 64
    RULE_index_expr = 65
    RULE_index = 66
    RULE_instance_accesses = 67
    RULE_instance_access = 68
    RULE_static_accesses = 69
    RULE_static_access = 70
    RULE_list_expr = 71
    RULE_array_lit = 72
    RULE_array_val = 73
    RULE_literal = 74
    RULE_list_parameters = 75
    RULE_param = 76
    RULE_identifier_list = 77
    RULE_variable_in_func_identifier_list = 78
    RULE_value_list = 79
    RULE_array_type = 80
    RULE_array_element_type = 81
    RULE_primitive_type = 82
    RULE_variable_type = 83

    ruleNames =  [ "program", "class_declarations", "class_declaration", 
                   "class_inheritance", "constructor_dclr", "destructor_dclr", 
                   "var_variable_declaration_noinit", "var_variable_declaration", 
                   "var_declare_initiate_list", "val_variable_declaration_noinit", 
                   "val_variable_declaration", "val_declare_initiate_list", 
                   "var_both_variable_declaration_noinnit", "var_both_variable_declaration", 
                   "var_both_declare_initiate_list", "val_both_variable_declaration_noinnit", 
                   "val_both_variable_declaration", "val_both_declare_initiate_list", 
                   "function_declaration", "call_func_statement", "call_func", 
                   "call_func_header", "call_func_attr_list", "call_func_attr", 
                   "call_func_end", "assignment_statements", "lhs", "if_condition", 
                   "if_statements", "elseif_list_statements", "elseif_statement", 
                   "else_statement_or_none", "else_statement", "by_expr", 
                   "forin_statements", "instance_attr_access", "instance_method_access", 
                   "static_attr_access", "static_method_access", "method_invocation", 
                   "method_invocation_statement", "break_statements", "continue_statements", 
                   "return_expr", "return_statements", "block_class_statements", 
                   "block_statements", "statements_class", "statements", 
                   "statement_class", "statement", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "expr9", "expr10", "expr11", "expr12", "index_operators", 
                   "index_expr", "index", "instance_accesses", "instance_access", 
                   "static_accesses", "static_access", "list_expr", "array_lit", 
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
            self.state = 168
            self.class_declarations()
            self.state = 169
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
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.class_declaration()
                self.state = 172
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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
            self.state = 177
            self.match(D96Parser.CLASS)
            self.state = 178
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 179
            self.class_inheritance()
            self.state = 180
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
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(D96Parser.COLON)
                self.state = 183
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
            self.state = 187
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 188
            self.match(D96Parser.LB)
            self.state = 189
            self.list_parameters()
            self.state = 190
            self.match(D96Parser.RB)
            self.state = 191
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
            self.state = 193
            self.match(D96Parser.DESTRUCTOR)
            self.state = 194
            self.match(D96Parser.LB)
            self.state = 195
            self.match(D96Parser.RB)
            self.state = 196
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
            self.state = 198
            self.match(D96Parser.VAR)
            self.state = 199
            self.variable_in_func_identifier_list()
            self.state = 200
            self.match(D96Parser.COLON)
            self.state = 201
            self.variable_type()
            self.state = 202
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
            self.state = 204
            self.match(D96Parser.VAR)
            self.state = 205
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 206
            self.var_declare_initiate_list()
            self.state = 207
            self.expr()
            self.state = 208
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
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.match(D96Parser.COMMA)
                self.state = 211
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 212
                self.var_declare_initiate_list()
                self.state = 213
                self.expr()
                self.state = 214
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(D96Parser.COLON)
                self.state = 217
                self.variable_type()
                self.state = 218
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
            self.state = 222
            self.match(D96Parser.VAL)
            self.state = 223
            self.variable_in_func_identifier_list()
            self.state = 224
            self.match(D96Parser.COLON)
            self.state = 225
            self.variable_type()
            self.state = 226
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
            self.state = 228
            self.match(D96Parser.VAL)
            self.state = 229
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 230
            self.val_declare_initiate_list()
            self.state = 231
            self.expr()
            self.state = 232
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
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(D96Parser.COMMA)
                self.state = 235
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 236
                self.val_declare_initiate_list()
                self.state = 237
                self.expr()
                self.state = 238
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(D96Parser.COLON)
                self.state = 241
                self.variable_type()
                self.state = 242
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
            self.state = 246
            self.match(D96Parser.VAR)
            self.state = 247
            self.identifier_list()
            self.state = 248
            self.match(D96Parser.COLON)
            self.state = 249
            self.variable_type()
            self.state = 250
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
            self.state = 252
            self.match(D96Parser.VAR)
            self.state = 253
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 254
            self.var_both_declare_initiate_list()
            self.state = 255
            self.expr()
            self.state = 256
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
            self.state = 268
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(D96Parser.COMMA)
                self.state = 259
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 260
                self.var_both_declare_initiate_list()
                self.state = 261
                self.expr()
                self.state = 262
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(D96Parser.COLON)
                self.state = 265
                self.variable_type()
                self.state = 266
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
            self.state = 270
            self.match(D96Parser.VAL)
            self.state = 271
            self.identifier_list()
            self.state = 272
            self.match(D96Parser.COLON)
            self.state = 273
            self.variable_type()
            self.state = 274
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
            self.state = 276
            self.match(D96Parser.VAL)
            self.state = 277
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 278
            self.val_both_declare_initiate_list()
            self.state = 279
            self.expr()
            self.state = 280
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
            self.state = 292
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 282
                self.match(D96Parser.COMMA)
                self.state = 283
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self.val_both_declare_initiate_list()
                self.state = 285
                self.expr()
                self.state = 286
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
                self.match(D96Parser.COLON)
                self.state = 289
                self.variable_type()
                self.state = 290
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
            self.state = 294
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 295
            self.match(D96Parser.LB)
            self.state = 296
            self.list_parameters()
            self.state = 297
            self.match(D96Parser.RB)
            self.state = 298
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_statementContext(ParserRuleContext):

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




    def call_func_statement(self):

        localctx = D96Parser.Call_func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.call_func_header()
            self.state = 301
            self.call_func_attr_list()
            self.state = 302
            self.call_func_end()
            self.state = 303
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_funcContext(ParserRuleContext):

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




    def call_func(self):

        localctx = D96Parser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_call_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            self.call_func_header()
            self.state = 306
            self.call_func_attr_list()
            self.state = 307
            self.call_func_end()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_func_headerContext(ParserRuleContext):

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




    def call_func_header(self):

        localctx = D96Parser.Call_func_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_call_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 310
                self.index_operators(0)
                pass
            elif token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOUBLECOLONOP]:
                self.state = 314
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 315
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func_attr(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attrContext,0)


        def call_func_attr_list(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attr_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_func_attr_list




    def call_func_attr_list(self):

        localctx = D96Parser.Call_func_attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_call_func_attr_list)
        try:
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.call_func_attr()
                self.state = 320
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
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




    def call_func_attr(self):

        localctx = D96Parser.Call_func_attrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_call_func_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.DOT)
            self.state = 333
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 327
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 328
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 329
                self.match(D96Parser.LB)
                self.state = 330
                self.value_list()
                self.state = 331
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




    def call_func_end(self):

        localctx = D96Parser.Call_func_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call_func_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(D96Parser.DOT)
            self.state = 336
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 337
            self.match(D96Parser.LB)
            self.state = 338
            self.value_list()
            self.state = 339
            self.match(D96Parser.RB)
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
        self.enterRule(localctx, 50, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.lhs()
            self.state = 342
            self.match(D96Parser.ASSIGNOP)
            self.state = 343
            self.expr()
            self.state = 344
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
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 346
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 347
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.state = 348
                self.static_attr_access()
                pass


            self.state = 353
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 351
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




    def if_condition(self):

        localctx = D96Parser.If_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(D96Parser.LB)
            self.state = 356
            self.expr()
            self.state = 357
            self.match(D96Parser.RB)
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

        def if_condition(self):
            return self.getTypedRuleContext(D96Parser.If_conditionContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(D96Parser.IF)
            self.state = 360
            self.if_condition()
            self.state = 361
            self.block_statements()
            self.state = 362
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


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def else_statement_or_none(self):
            return self.getTypedRuleContext(D96Parser.Else_statement_or_noneContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_statements




    def elseif_list_statements(self):

        localctx = D96Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elseif_list_statements)
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.elseif_statement()
                self.state = 365
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 367
                self.elseif_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 368
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




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(D96Parser.ELSEIF)
            self.state = 372
            self.if_condition()
            self.state = 373
            self.block_statements()
            self.state = 374
            self.else_statement_or_none()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_statement_or_noneContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_else_statement_or_none




    def else_statement_or_none(self):

        localctx = D96Parser.Else_statement_or_noneContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_else_statement_or_none)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
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
        self.enterRule(localctx, 64, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(D96Parser.ELSE)
            self.state = 381
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
        self.enterRule(localctx, 66, self.RULE_by_expr)
        try:
            self.state = 386
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.match(D96Parser.BY)
                self.state = 384
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
        self.enterRule(localctx, 68, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(D96Parser.FOREACH)
            self.state = 389
            self.match(D96Parser.LB)
            self.state = 390
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 391
            self.match(D96Parser.IN)
            self.state = 392
            self.expr()
            self.state = 393
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 394
            self.expr()
            self.state = 395
            self.by_expr()
            self.state = 396
            self.match(D96Parser.RB)
            self.state = 397
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
        self.enterRule(localctx, 70, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.expr()
            self.state = 400
            self.match(D96Parser.DOT)
            self.state = 401
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
        self.enterRule(localctx, 72, self.RULE_instance_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.expr()
            self.state = 404
            self.match(D96Parser.DOT)
            self.state = 405
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 406
            self.match(D96Parser.LB)
            self.state = 407
            self.list_expr()
            self.state = 408
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
        self.enterRule(localctx, 74, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 411
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 412
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
        self.enterRule(localctx, 76, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 415
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 416
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 417
            self.match(D96Parser.LB)
            self.state = 418
            self.list_expr()
            self.state = 419
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
        self.enterRule(localctx, 78, self.RULE_method_invocation)
        try:
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
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
        self.enterRule(localctx, 80, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.method_invocation()
            self.state = 426
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
        self.enterRule(localctx, 82, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.BREAK)
            self.state = 429
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
        self.enterRule(localctx, 84, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(D96Parser.CONTINUE)
            self.state = 432
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
        self.enterRule(localctx, 86, self.RULE_return_expr)
        try:
            self.state = 436
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
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
        self.enterRule(localctx, 88, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(D96Parser.RETURN)
            self.state = 439
            self.return_expr()
            self.state = 440
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
        self.enterRule(localctx, 90, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(D96Parser.LCB)
            self.state = 443
            self.statements_class()
            self.state = 444
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
        self.enterRule(localctx, 92, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(D96Parser.LCB)
            self.state = 447
            self.statements()
            self.state = 448
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
        self.enterRule(localctx, 94, self.RULE_statements_class)
        try:
            self.state = 455
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.statement_class()
                self.state = 451
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
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
        self.enterRule(localctx, 96, self.RULE_statements)
        try:
            self.state = 462
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.statement()
                self.state = 458
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
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
        self.enterRule(localctx, 98, self.RULE_statement_class)
        try:
            self.state = 471
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.var_both_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 465
                self.val_both_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 466
                self.var_both_variable_declaration_noinnit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 467
                self.val_both_variable_declaration_noinnit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 468
                self.function_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 469
                self.constructor_dclr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 470
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




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_statement)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 473
                self.var_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 474
                self.val_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 475
                self.var_variable_declaration_noinit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 476
                self.val_variable_declaration_noinit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 477
                self.assignment_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 478
                self.val_variable_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 479
                self.assignment_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 480
                self.if_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 481
                self.forin_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 482
                self.call_func_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 483
                self.method_invocation_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 484
                self.break_statements()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 485
                self.continue_statements()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 486
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
        self.enterRule(localctx, 102, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 494
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.expr1()
                self.state = 490
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 491
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
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
        self.enterRule(localctx, 104, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.expr2(0)
                self.state = 497
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 498
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 506
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 507
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 508
                    self.expr3(0) 
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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
        _startState = 108
        self.enterRecursionRule(localctx, 108, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 522
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 517
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 518
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 519
                    self.expr4(0) 
                self.state = 524
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 533
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 528
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 529
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 530
                    self.expr5() 
                self.state = 535
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 112, self.RULE_expr5)
        try:
            self.state = 539
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 536
                self.match(D96Parser.NOTOP)
                self.state = 537
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 538
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
        self.enterRule(localctx, 114, self.RULE_expr6)
        try:
            self.state = 544
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.match(D96Parser.MINUSOP)
                self.state = 542
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 553
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 549
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 550
                    self.index_operators(0) 
                self.state = 555
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 563
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 559
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 560
                    self.instance_accesses() 
                self.state = 565
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def static_accesses(self):
            return self.getTypedRuleContext(D96Parser.Static_accessesContext,0)


        def expr10(self):
            return self.getTypedRuleContext(D96Parser.Expr10Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr9




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_expr9)
        try:
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 567
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
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
        self.enterRule(localctx, 122, self.RULE_expr10)
        try:
            self.state = 578
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.match(D96Parser.NEW)
                self.state = 572
                self.expr()
                self.state = 573
                self.match(D96Parser.LB)
                self.state = 574
                self.list_expr()
                self.state = 575
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 577
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
        self.enterRule(localctx, 124, self.RULE_expr11)
        try:
            self.state = 584
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 580
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 582
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 583
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
        self.enterRule(localctx, 126, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(D96Parser.LB)
            self.state = 587
            self.expr()
            self.state = 588
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



    def index_operators(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Index_operatorsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 591
            self.match(D96Parser.LSB)
            self.state = 592
            self.expr()
            self.state = 593
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 602
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 595
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 596
                    self.match(D96Parser.LSB)
                    self.state = 597
                    self.expr()
                    self.state = 598
                    self.match(D96Parser.RSB) 
                self.state = 604
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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
        self.enterRule(localctx, 130, self.RULE_index_expr)
        try:
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 605
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 606
                self.index()
                self.state = 607
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
        self.enterRule(localctx, 132, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 611
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 612
                self.expr()
                self.state = 613
                self.instance_attr_access()
                self.state = 614
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
        self.enterRule(localctx, 134, self.RULE_instance_accesses)
        try:
            self.state = 623
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.instance_access()
                self.state = 620
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
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
        self.enterRule(localctx, 136, self.RULE_instance_access)
        try:
            self.state = 633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 625
                self.match(D96Parser.DOT)
                self.state = 626
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
                self.match(D96Parser.DOT)
                self.state = 628
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 629
                self.match(D96Parser.LB)
                self.state = 630
                self.list_expr()
                self.state = 631
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
        self.enterRule(localctx, 138, self.RULE_static_accesses)
        try:
            self.state = 639
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 635
                self.static_access()
                self.state = 636
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 638
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
        self.enterRule(localctx, 140, self.RULE_static_access)
        try:
            self.state = 649
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 641
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 642
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 644
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 645
                self.match(D96Parser.LB)
                self.state = 646
                self.list_expr()
                self.state = 647
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
        self.enterRule(localctx, 142, self.RULE_list_expr)
        try:
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 651
                self.expr()
                self.state = 652
                self.match(D96Parser.COMMA)
                self.state = 653
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 655
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
        self.enterRule(localctx, 144, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 659
            self.match(D96Parser.ARRAY)
            self.state = 660
            self.match(D96Parser.LB)
            self.state = 661
            self.array_val()
            self.state = 662
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
        self.enterRule(localctx, 146, self.RULE_array_val)
        try:
            self.state = 670
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 664
                self.expr()
                self.state = 665
                self.match(D96Parser.COMMA)
                self.state = 666
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
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
        self.enterRule(localctx, 148, self.RULE_literal)
        try:
            self.state = 678
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 672
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 673
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 674
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 675
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 676
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 677
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
        self.enterRule(localctx, 150, self.RULE_list_parameters)
        try:
            self.state = 686
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.param()
                self.state = 681
                self.match(D96Parser.SEMICOLON)
                self.state = 682
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 684
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
        self.enterRule(localctx, 152, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.identifier_list()
            self.state = 689
            self.match(D96Parser.COLON)
            self.state = 690
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
        self.enterRule(localctx, 154, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 697
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 693
                self.match(D96Parser.COMMA)
                self.state = 694
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 695
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
        self.enterRule(localctx, 156, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 704
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 699
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 700
                self.match(D96Parser.COMMA)
                self.state = 701
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 702
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
        self.enterRule(localctx, 158, self.RULE_value_list)
        try:
            self.state = 718
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 708
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                if la_ == 1:
                    self.state = 706
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 707
                    self.expr()
                    pass


                self.state = 710
                self.match(D96Parser.COMMA)
                self.state = 711
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 715
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 713
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 714
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
        self.enterRule(localctx, 160, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 720
            self.match(D96Parser.ARRAY)
            self.state = 721
            self.match(D96Parser.LSB)
            self.state = 722
            self.array_element_type()
            self.state = 723
            self.match(D96Parser.COMMA)
            self.state = 724
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 725
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
        self.enterRule(localctx, 162, self.RULE_array_element_type)
        try:
            self.state = 732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 727
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 728
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 729
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 730
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 731
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
        self.enterRule(localctx, 164, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
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
        self.enterRule(localctx, 166, self.RULE_variable_type)
        try:
            self.state = 739
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 736
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 737
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 738
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
        self._predicates[53] = self.expr2_sempred
        self._predicates[54] = self.expr3_sempred
        self._predicates[55] = self.expr4_sempred
        self._predicates[58] = self.expr7_sempred
        self._predicates[59] = self.expr8_sempred
        self._predicates[64] = self.index_operators_sempred
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
         




