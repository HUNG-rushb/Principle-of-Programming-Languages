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
        buf.write("\u0321\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\3\2\3\2\3\2\3\3\3\3\3")
        buf.write("\3\3\3\5\3\u00be\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\5")
        buf.write("\5\u00c8\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\5\n\u00e7\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00f3\n\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\5\16\u0107\n\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u0113\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\5\22\u0123\n\22\3\23\3\23\3\23\3\23\3\23\5")
        buf.write("\23\u012a\n\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u0134\n\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\3\25\3\25\5\25\u0140\n\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0154\n\30\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u0160\n\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\5\35\u0174\n\35\3\35\3\35\3\35\5")
        buf.write("\35\u0179\n\35\3\36\3\36\3\36\3\36\3\36\5\36\u0180\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u0189\n\37\3")
        buf.write(" \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\3\"\5\"\u0199")
        buf.write("\n\"\3\"\3\"\5\"\u019d\n\"\3#\3#\3#\3#\3$\3$\3$\3$\3$")
        buf.write("\3%\3%\3%\3%\3%\5%\u01ad\n%\3&\3&\3&\3&\3&\3\'\3\'\5\'")
        buf.write("\u01b6\n\'\3(\3(\3(\3)\3)\3)\5)\u01be\n)\3*\3*\3*\3*\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3/\3/\5/\u01e3\n/\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\62\3\62\3\62\3\63\3\63\5\63")
        buf.write("\u01f0\n\63\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3")
        buf.write("\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\5\67\u0203")
        buf.write("\n\67\38\38\38\38\38\58\u020a\n8\39\39\39\39\39\39\39")
        buf.write("\59\u0213\n9\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\5:\u0223\n:\3;\3;\3;\3;\3;\5;\u022a\n;\3<\3<\3<\3<\3")
        buf.write("<\5<\u0231\n<\3=\3=\3=\3=\3=\3=\7=\u0239\n=\f=\16=\u023c")
        buf.write("\13=\3>\3>\3>\3>\3>\3>\7>\u0244\n>\f>\16>\u0247\13>\3")
        buf.write("?\3?\3?\3?\3?\3?\7?\u024f\n?\f?\16?\u0252\13?\3@\3@\3")
        buf.write("@\5@\u0257\n@\3A\3A\3A\5A\u025c\nA\3B\3B\3B\3B\3B\7B\u0263")
        buf.write("\nB\fB\16B\u0266\13B\3C\3C\3C\3C\3C\7C\u026d\nC\fC\16")
        buf.write("C\u0270\13C\3D\3D\3D\5D\u0275\nD\3E\3E\3E\3E\3E\3E\3E")
        buf.write("\5E\u027e\nE\3F\3F\3F\3F\5F\u0284\nF\3G\3G\3G\3G\3H\3")
        buf.write("H\3H\3H\3H\3H\3H\3H\3H\3H\7H\u0294\nH\fH\16H\u0297\13")
        buf.write("H\3I\3I\3I\3I\5I\u029d\nI\3J\3J\3J\3J\3J\3J\5J\u02a5\n")
        buf.write("J\3K\3K\3K\3K\5K\u02ab\nK\3L\3L\3L\3L\3L\3L\3L\3L\5L\u02b5")
        buf.write("\nL\3M\3M\3M\3M\5M\u02bb\nM\3N\3N\3N\3N\3N\3N\3N\3N\5")
        buf.write("N\u02c5\nN\3O\3O\3O\3O\3O\3O\5O\u02cd\nO\3P\3P\3P\3P\3")
        buf.write("P\3Q\3Q\3Q\3Q\3Q\3Q\5Q\u02da\nQ\3R\3R\3R\3R\3R\3R\5R\u02e2")
        buf.write("\nR\3S\3S\3S\3S\3S\3S\5S\u02ea\nS\3T\3T\3T\3T\3U\3U\3")
        buf.write("U\3U\3U\5U\u02f5\nU\3V\3V\3V\3V\3V\5V\u02fc\nV\3W\3W\5")
        buf.write("W\u0300\nW\3W\3W\3W\3W\3W\5W\u0307\nW\3W\5W\u030a\nW\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3Y\3Y\3Y\3Y\3Y\5Y\u0318\nY\3Z\3Z\3")
        buf.write("[\3[\3[\5[\u031f\n[\3[\2\bxz|\u0082\u0084\u008e\\\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096")
        buf.write("\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8")
        buf.write("\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\2\t\3\29:\3\2-.\4")
        buf.write("\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2\16\21\2\u0327\2\u00b6")
        buf.write("\3\2\2\2\4\u00bd\3\2\2\2\6\u00bf\3\2\2\2\b\u00c7\3\2\2")
        buf.write("\2\n\u00c9\3\2\2\2\f\u00cf\3\2\2\2\16\u00d4\3\2\2\2\20")
        buf.write("\u00da\3\2\2\2\22\u00e6\3\2\2\2\24\u00f2\3\2\2\2\26\u00f4")
        buf.write("\3\2\2\2\30\u00fa\3\2\2\2\32\u0106\3\2\2\2\34\u0112\3")
        buf.write("\2\2\2\36\u0114\3\2\2\2 \u011a\3\2\2\2\"\u0122\3\2\2\2")
        buf.write("$\u0129\3\2\2\2&\u0133\3\2\2\2(\u013f\3\2\2\2*\u0141\3")
        buf.write("\2\2\2,\u0147\3\2\2\2.\u0153\3\2\2\2\60\u015f\3\2\2\2")
        buf.write("\62\u0161\3\2\2\2\64\u0167\3\2\2\2\66\u016c\3\2\2\28\u0170")
        buf.write("\3\2\2\2:\u017f\3\2\2\2<\u0181\3\2\2\2>\u018a\3\2\2\2")
        buf.write("@\u0190\3\2\2\2B\u0198\3\2\2\2D\u019e\3\2\2\2F\u01a2\3")
        buf.write("\2\2\2H\u01ac\3\2\2\2J\u01ae\3\2\2\2L\u01b5\3\2\2\2N\u01b7")
        buf.write("\3\2\2\2P\u01bd\3\2\2\2R\u01bf\3\2\2\2T\u01ca\3\2\2\2")
        buf.write("V\u01ce\3\2\2\2X\u01d5\3\2\2\2Z\u01d9\3\2\2\2\\\u01e2")
        buf.write("\3\2\2\2^\u01e4\3\2\2\2`\u01e7\3\2\2\2b\u01ea\3\2\2\2")
        buf.write("d\u01ef\3\2\2\2f\u01f1\3\2\2\2h\u01f5\3\2\2\2j\u01f9\3")
        buf.write("\2\2\2l\u0202\3\2\2\2n\u0209\3\2\2\2p\u0212\3\2\2\2r\u0222")
        buf.write("\3\2\2\2t\u0229\3\2\2\2v\u0230\3\2\2\2x\u0232\3\2\2\2")
        buf.write("z\u023d\3\2\2\2|\u0248\3\2\2\2~\u0256\3\2\2\2\u0080\u025b")
        buf.write("\3\2\2\2\u0082\u025d\3\2\2\2\u0084\u0267\3\2\2\2\u0086")
        buf.write("\u0274\3\2\2\2\u0088\u027d\3\2\2\2\u008a\u0283\3\2\2\2")
        buf.write("\u008c\u0285\3\2\2\2\u008e\u0289\3\2\2\2\u0090\u029c\3")
        buf.write("\2\2\2\u0092\u02a4\3\2\2\2\u0094\u02aa\3\2\2\2\u0096\u02b4")
        buf.write("\3\2\2\2\u0098\u02ba\3\2\2\2\u009a\u02c4\3\2\2\2\u009c")
        buf.write("\u02cc\3\2\2\2\u009e\u02ce\3\2\2\2\u00a0\u02d9\3\2\2\2")
        buf.write("\u00a2\u02e1\3\2\2\2\u00a4\u02e9\3\2\2\2\u00a6\u02eb\3")
        buf.write("\2\2\2\u00a8\u02f4\3\2\2\2\u00aa\u02fb\3\2\2\2\u00ac\u0309")
        buf.write("\3\2\2\2\u00ae\u030b\3\2\2\2\u00b0\u0317\3\2\2\2\u00b2")
        buf.write("\u0319\3\2\2\2\u00b4\u031e\3\2\2\2\u00b6\u00b7\5\4\3\2")
        buf.write("\u00b7\u00b8\7\2\2\3\u00b8\3\3\2\2\2\u00b9\u00ba\5\6\4")
        buf.write("\2\u00ba\u00bb\5\4\3\2\u00bb\u00be\3\2\2\2\u00bc\u00be")
        buf.write("\5\6\4\2\u00bd\u00b9\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be")
        buf.write("\5\3\2\2\2\u00bf\u00c0\7\24\2\2\u00c0\u00c1\79\2\2\u00c1")
        buf.write("\u00c2\5\b\5\2\u00c2\u00c3\5h\65\2\u00c3\7\3\2\2\2\u00c4")
        buf.write("\u00c5\7\67\2\2\u00c5\u00c8\79\2\2\u00c6\u00c8\3\2\2\2")
        buf.write("\u00c7\u00c4\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\t\3\2\2")
        buf.write("\2\u00c9\u00ca\7\27\2\2\u00ca\u00cb\7/\2\2\u00cb\u00cc")
        buf.write("\5\u00a4S\2\u00cc\u00cd\7\60\2\2\u00cd\u00ce\5j\66\2\u00ce")
        buf.write("\13\3\2\2\2\u00cf\u00d0\7\30\2\2\u00d0\u00d1\7/\2\2\u00d1")
        buf.write("\u00d2\7\60\2\2\u00d2\u00d3\5j\66\2\u00d3\r\3\2\2\2\u00d4")
        buf.write("\u00d5\7\26\2\2\u00d5\u00d6\5\u00aaV\2\u00d6\u00d7\7\67")
        buf.write("\2\2\u00d7\u00d8\5\u00b4[\2\u00d8\u00d9\78\2\2\u00d9\17")
        buf.write("\3\2\2\2\u00da\u00db\7\26\2\2\u00db\u00dc\5\22\n\2\u00dc")
        buf.write("\u00dd\78\2\2\u00dd\21\3\2\2\2\u00de\u00df\79\2\2\u00df")
        buf.write("\u00e0\5\24\13\2\u00e0\u00e1\5t;\2\u00e1\u00e7\3\2\2\2")
        buf.write("\u00e2\u00e3\5\u00aaV\2\u00e3\u00e4\7\67\2\2\u00e4\u00e5")
        buf.write("\5\u00b4[\2\u00e5\u00e7\3\2\2\2\u00e6\u00de\3\2\2\2\u00e6")
        buf.write("\u00e2\3\2\2\2\u00e7\23\3\2\2\2\u00e8\u00e9\7\66\2\2\u00e9")
        buf.write("\u00ea\79\2\2\u00ea\u00eb\5\24\13\2\u00eb\u00ec\5t;\2")
        buf.write("\u00ec\u00ed\7\66\2\2\u00ed\u00f3\3\2\2\2\u00ee\u00ef")
        buf.write("\7\67\2\2\u00ef\u00f0\5\u00b4[\2\u00f0\u00f1\7\'\2\2\u00f1")
        buf.write("\u00f3\3\2\2\2\u00f2\u00e8\3\2\2\2\u00f2\u00ee\3\2\2\2")
        buf.write("\u00f3\25\3\2\2\2\u00f4\u00f5\7\25\2\2\u00f5\u00f6\5\u00aa")
        buf.write("V\2\u00f6\u00f7\7\67\2\2\u00f7\u00f8\5\u00b4[\2\u00f8")
        buf.write("\u00f9\78\2\2\u00f9\27\3\2\2\2\u00fa\u00fb\7\25\2\2\u00fb")
        buf.write("\u00fc\5\32\16\2\u00fc\u00fd\78\2\2\u00fd\31\3\2\2\2\u00fe")
        buf.write("\u00ff\79\2\2\u00ff\u0100\5\34\17\2\u0100\u0101\5t;\2")
        buf.write("\u0101\u0107\3\2\2\2\u0102\u0103\5\u00aaV\2\u0103\u0104")
        buf.write("\7\67\2\2\u0104\u0105\5\u00b4[\2\u0105\u0107\3\2\2\2\u0106")
        buf.write("\u00fe\3\2\2\2\u0106\u0102\3\2\2\2\u0107\33\3\2\2\2\u0108")
        buf.write("\u0109\7\66\2\2\u0109\u010a\79\2\2\u010a\u010b\5\34\17")
        buf.write("\2\u010b\u010c\5t;\2\u010c\u010d\7\66\2\2\u010d\u0113")
        buf.write("\3\2\2\2\u010e\u010f\7\67\2\2\u010f\u0110\5\u00b4[\2\u0110")
        buf.write("\u0111\7\'\2\2\u0111\u0113\3\2\2\2\u0112\u0108\3\2\2\2")
        buf.write("\u0112\u010e\3\2\2\2\u0113\35\3\2\2\2\u0114\u0115\7\26")
        buf.write("\2\2\u0115\u0116\5\u00a8U\2\u0116\u0117\7\67\2\2\u0117")
        buf.write("\u0118\5\u00b4[\2\u0118\u0119\78\2\2\u0119\37\3\2\2\2")
        buf.write("\u011a\u011b\7\26\2\2\u011b\u011c\5&\24\2\u011c\u011d")
        buf.write("\78\2\2\u011d!\3\2\2\2\u011e\u011f\5$\23\2\u011f\u0120")
        buf.write("\5\"\22\2\u0120\u0123\3\2\2\2\u0121\u0123\5$\23\2\u0122")
        buf.write("\u011e\3\2\2\2\u0122\u0121\3\2\2\2\u0123#\3\2\2\2\u0124")
        buf.write("\u0125\t\2\2\2\u0125\u012a\7\66\2\2\u0126\u012a\t\2\2")
        buf.write("\2\u0127\u0128\7\67\2\2\u0128\u012a\5\u00b4[\2\u0129\u0124")
        buf.write("\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0127\3\2\2\2\u012a")
        buf.write("%\3\2\2\2\u012b\u012c\t\2\2\2\u012c\u012d\5(\25\2\u012d")
        buf.write("\u012e\5t;\2\u012e\u0134\3\2\2\2\u012f\u0130\5\u00aaV")
        buf.write("\2\u0130\u0131\7\67\2\2\u0131\u0132\5\u00b4[\2\u0132\u0134")
        buf.write("\3\2\2\2\u0133\u012b\3\2\2\2\u0133\u012f\3\2\2\2\u0134")
        buf.write("\'\3\2\2\2\u0135\u0136\7\66\2\2\u0136\u0137\t\2\2\2\u0137")
        buf.write("\u0138\5(\25\2\u0138\u0139\5t;\2\u0139\u013a\7\66\2\2")
        buf.write("\u013a\u0140\3\2\2\2\u013b\u013c\7\67\2\2\u013c\u013d")
        buf.write("\5\u00b4[\2\u013d\u013e\7\'\2\2\u013e\u0140\3\2\2\2\u013f")
        buf.write("\u0135\3\2\2\2\u013f\u013b\3\2\2\2\u0140)\3\2\2\2\u0141")
        buf.write("\u0142\7\25\2\2\u0142\u0143\5\u00a8U\2\u0143\u0144\7\67")
        buf.write("\2\2\u0144\u0145\5\u00b4[\2\u0145\u0146\78\2\2\u0146+")
        buf.write("\3\2\2\2\u0147\u0148\7\25\2\2\u0148\u0149\5.\30\2\u0149")
        buf.write("\u014a\78\2\2\u014a-\3\2\2\2\u014b\u014c\t\2\2\2\u014c")
        buf.write("\u014d\5\60\31\2\u014d\u014e\5t;\2\u014e\u0154\3\2\2\2")
        buf.write("\u014f\u0150\5\u00aaV\2\u0150\u0151\7\67\2\2\u0151\u0152")
        buf.write("\5\u00b4[\2\u0152\u0154\3\2\2\2\u0153\u014b\3\2\2\2\u0153")
        buf.write("\u014f\3\2\2\2\u0154/\3\2\2\2\u0155\u0156\7\66\2\2\u0156")
        buf.write("\u0157\t\2\2\2\u0157\u0158\5\60\31\2\u0158\u0159\5t;\2")
        buf.write("\u0159\u015a\7\66\2\2\u015a\u0160\3\2\2\2\u015b\u015c")
        buf.write("\7\67\2\2\u015c\u015d\5\u00b4[\2\u015d\u015e\7\'\2\2\u015e")
        buf.write("\u0160\3\2\2\2\u015f\u0155\3\2\2\2\u015f\u015b\3\2\2\2")
        buf.write("\u0160\61\3\2\2\2\u0161\u0162\t\2\2\2\u0162\u0163\7/\2")
        buf.write("\2\u0163\u0164\5\u00a4S\2\u0164\u0165\7\60\2\2\u0165\u0166")
        buf.write("\5j\66\2\u0166\63\3\2\2\2\u0167\u0168\58\35\2\u0168\u0169")
        buf.write("\5:\36\2\u0169\u016a\5> \2\u016a\u016b\78\2\2\u016b\65")
        buf.write("\3\2\2\2\u016c\u016d\58\35\2\u016d\u016e\5:\36\2\u016e")
        buf.write("\u016f\5> \2\u016f\67\3\2\2\2\u0170\u0173\t\2\2\2\u0171")
        buf.write("\u0174\5\u008eH\2\u0172\u0174\3\2\2\2\u0173\u0171\3\2")
        buf.write("\2\2\u0173\u0172\3\2\2\2\u0174\u0178\3\2\2\2\u0175\u0176")
        buf.write("\7\34\2\2\u0176\u0179\7:\2\2\u0177\u0179\3\2\2\2\u0178")
        buf.write("\u0175\3\2\2\2\u0178\u0177\3\2\2\2\u01799\3\2\2\2\u017a")
        buf.write("\u017b\5<\37\2\u017b\u017c\5:\36\2\u017c\u0180\3\2\2\2")
        buf.write("\u017d\u0180\5<\37\2\u017e\u0180\3\2\2\2\u017f\u017a\3")
        buf.write("\2\2\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180;")
        buf.write("\3\2\2\2\u0181\u0188\7\65\2\2\u0182\u0189\79\2\2\u0183")
        buf.write("\u0184\79\2\2\u0184\u0185\7/\2\2\u0185\u0186\5\u00acW")
        buf.write("\2\u0186\u0187\7\60\2\2\u0187\u0189\3\2\2\2\u0188\u0182")
        buf.write("\3\2\2\2\u0188\u0183\3\2\2\2\u0189=\3\2\2\2\u018a\u018b")
        buf.write("\7\65\2\2\u018b\u018c\79\2\2\u018c\u018d\7/\2\2\u018d")
        buf.write("\u018e\5\u00acW\2\u018e\u018f\7\60\2\2\u018f?\3\2\2\2")
        buf.write("\u0190\u0191\5B\"\2\u0191\u0192\7\'\2\2\u0192\u0193\5")
        buf.write("t;\2\u0193\u0194\78\2\2\u0194A\3\2\2\2\u0195\u0199\79")
        buf.write("\2\2\u0196\u0199\5T+\2\u0197\u0199\5X-\2\u0198\u0195\3")
        buf.write("\2\2\2\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2\u0199\u019c")
        buf.write("\3\2\2\2\u019a\u019d\5\u008eH\2\u019b\u019d\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019dC\3\2\2\2\u019e")
        buf.write("\u019f\7/\2\2\u019f\u01a0\5t;\2\u01a0\u01a1\7\60\2\2\u01a1")
        buf.write("E\3\2\2\2\u01a2\u01a3\7\5\2\2\u01a3\u01a4\5D#\2\u01a4")
        buf.write("\u01a5\5j\66\2\u01a5\u01a6\5H%\2\u01a6G\3\2\2\2\u01a7")
        buf.write("\u01a8\5J&\2\u01a8\u01a9\5H%\2\u01a9\u01ad\3\2\2\2\u01aa")
        buf.write("\u01ad\5J&\2\u01ab\u01ad\5L\'\2\u01ac\u01a7\3\2\2\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adI\3\2\2\2\u01ae")
        buf.write("\u01af\7\6\2\2\u01af\u01b0\5D#\2\u01b0\u01b1\5j\66\2\u01b1")
        buf.write("\u01b2\5L\'\2\u01b2K\3\2\2\2\u01b3\u01b6\5N(\2\u01b4\u01b6")
        buf.write("\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("M\3\2\2\2\u01b7\u01b8\7\7\2\2\u01b8\u01b9\5j\66\2\u01b9")
        buf.write("O\3\2\2\2\u01ba\u01bb\7\32\2\2\u01bb\u01be\5t;\2\u01bc")
        buf.write("\u01be\3\2\2\2\u01bd\u01ba\3\2\2\2\u01bd\u01bc\3\2\2\2")
        buf.write("\u01beQ\3\2\2\2\u01bf\u01c0\7\b\2\2\u01c0\u01c1\7/\2\2")
        buf.write("\u01c1\u01c2\t\2\2\2\u01c2\u01c3\7\r\2\2\u01c3\u01c4\5")
        buf.write("t;\2\u01c4\u01c5\7\35\2\2\u01c5\u01c6\5t;\2\u01c6\u01c7")
        buf.write("\5P)\2\u01c7\u01c8\7\60\2\2\u01c8\u01c9\5j\66\2\u01c9")
        buf.write("S\3\2\2\2\u01ca\u01cb\5t;\2\u01cb\u01cc\7\65\2\2\u01cc")
        buf.write("\u01cd\79\2\2\u01cdU\3\2\2\2\u01ce\u01cf\5t;\2\u01cf\u01d0")
        buf.write("\7\65\2\2\u01d0\u01d1\79\2\2\u01d1\u01d2\7/\2\2\u01d2")
        buf.write("\u01d3\5\u009cO\2\u01d3\u01d4\7\60\2\2\u01d4W\3\2\2\2")
        buf.write("\u01d5\u01d6\t\2\2\2\u01d6\u01d7\7\34\2\2\u01d7\u01d8")
        buf.write("\7:\2\2\u01d8Y\3\2\2\2\u01d9\u01da\t\2\2\2\u01da\u01db")
        buf.write("\7\34\2\2\u01db\u01dc\7:\2\2\u01dc\u01dd\7/\2\2\u01dd")
        buf.write("\u01de\5\u009cO\2\u01de\u01df\7\60\2\2\u01df[\3\2\2\2")
        buf.write("\u01e0\u01e3\5V,\2\u01e1\u01e3\5Z.\2\u01e2\u01e0\3\2\2")
        buf.write("\2\u01e2\u01e1\3\2\2\2\u01e3]\3\2\2\2\u01e4\u01e5\5\\")
        buf.write("/\2\u01e5\u01e6\78\2\2\u01e6_\3\2\2\2\u01e7\u01e8\7\3")
        buf.write("\2\2\u01e8\u01e9\78\2\2\u01e9a\3\2\2\2\u01ea\u01eb\7\4")
        buf.write("\2\2\u01eb\u01ec\78\2\2\u01ecc\3\2\2\2\u01ed\u01f0\5t")
        buf.write(";\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0e\3\2\2\2\u01f1\u01f2\7\22\2\2\u01f2\u01f3")
        buf.write("\5d\63\2\u01f3\u01f4\78\2\2\u01f4g\3\2\2\2\u01f5\u01f6")
        buf.write("\7\63\2\2\u01f6\u01f7\5l\67\2\u01f7\u01f8\7\64\2\2\u01f8")
        buf.write("i\3\2\2\2\u01f9\u01fa\7\63\2\2\u01fa\u01fb\5n8\2\u01fb")
        buf.write("\u01fc\7\64\2\2\u01fck\3\2\2\2\u01fd\u01fe\5p9\2\u01fe")
        buf.write("\u01ff\5l\67\2\u01ff\u0203\3\2\2\2\u0200\u0203\5p9\2\u0201")
        buf.write("\u0203\3\2\2\2\u0202\u01fd\3\2\2\2\u0202\u0200\3\2\2\2")
        buf.write("\u0202\u0201\3\2\2\2\u0203m\3\2\2\2\u0204\u0205\5r:\2")
        buf.write("\u0205\u0206\5n8\2\u0206\u020a\3\2\2\2\u0207\u020a\5r")
        buf.write(":\2\u0208\u020a\3\2\2\2\u0209\u0204\3\2\2\2\u0209\u0207")
        buf.write("\3\2\2\2\u0209\u0208\3\2\2\2\u020ao\3\2\2\2\u020b\u0213")
        buf.write("\5 \21\2\u020c\u0213\5,\27\2\u020d\u0213\5\36\20\2\u020e")
        buf.write("\u0213\5*\26\2\u020f\u0213\5\62\32\2\u0210\u0213\5\n\6")
        buf.write("\2\u0211\u0213\5\f\7\2\u0212\u020b\3\2\2\2\u0212\u020c")
        buf.write("\3\2\2\2\u0212\u020d\3\2\2\2\u0212\u020e\3\2\2\2\u0212")
        buf.write("\u020f\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0211\3\2\2\2")
        buf.write("\u0213q\3\2\2\2\u0214\u0223\5\20\t\2\u0215\u0223\5\30")
        buf.write("\r\2\u0216\u0223\5\16\b\2\u0217\u0223\5\26\f\2\u0218\u0223")
        buf.write("\5@!\2\u0219\u0223\5\30\r\2\u021a\u0223\5@!\2\u021b\u0223")
        buf.write("\5F$\2\u021c\u0223\5R*\2\u021d\u0223\5\64\33\2\u021e\u0223")
        buf.write("\5^\60\2\u021f\u0223\5`\61\2\u0220\u0223\5b\62\2\u0221")
        buf.write("\u0223\5f\64\2\u0222\u0214\3\2\2\2\u0222\u0215\3\2\2\2")
        buf.write("\u0222\u0216\3\2\2\2\u0222\u0217\3\2\2\2\u0222\u0218\3")
        buf.write("\2\2\2\u0222\u0219\3\2\2\2\u0222\u021a\3\2\2\2\u0222\u021b")
        buf.write("\3\2\2\2\u0222\u021c\3\2\2\2\u0222\u021d\3\2\2\2\u0222")
        buf.write("\u021e\3\2\2\2\u0222\u021f\3\2\2\2\u0222\u0220\3\2\2\2")
        buf.write("\u0222\u0221\3\2\2\2\u0223s\3\2\2\2\u0224\u0225\5v<\2")
        buf.write("\u0225\u0226\t\3\2\2\u0226\u0227\5v<\2\u0227\u022a\3\2")
        buf.write("\2\2\u0228\u022a\5v<\2\u0229\u0224\3\2\2\2\u0229\u0228")
        buf.write("\3\2\2\2\u022au\3\2\2\2\u022b\u022c\5x=\2\u022c\u022d")
        buf.write("\t\4\2\2\u022d\u022e\5x=\2\u022e\u0231\3\2\2\2\u022f\u0231")
        buf.write("\5x=\2\u0230\u022b\3\2\2\2\u0230\u022f\3\2\2\2\u0231w")
        buf.write("\3\2\2\2\u0232\u0233\b=\1\2\u0233\u0234\5z>\2\u0234\u023a")
        buf.write("\3\2\2\2\u0235\u0236\f\4\2\2\u0236\u0237\t\5\2\2\u0237")
        buf.write("\u0239\5z>\2\u0238\u0235\3\2\2\2\u0239\u023c\3\2\2\2\u023a")
        buf.write("\u0238\3\2\2\2\u023a\u023b\3\2\2\2\u023by\3\2\2\2\u023c")
        buf.write("\u023a\3\2\2\2\u023d\u023e\b>\1\2\u023e\u023f\5|?\2\u023f")
        buf.write("\u0245\3\2\2\2\u0240\u0241\f\4\2\2\u0241\u0242\t\6\2\2")
        buf.write("\u0242\u0244\5|?\2\u0243\u0240\3\2\2\2\u0244\u0247\3\2")
        buf.write("\2\2\u0245\u0243\3\2\2\2\u0245\u0246\3\2\2\2\u0246{\3")
        buf.write("\2\2\2\u0247\u0245\3\2\2\2\u0248\u0249\b?\1\2\u0249\u024a")
        buf.write("\5~@\2\u024a\u0250\3\2\2\2\u024b\u024c\f\4\2\2\u024c\u024d")
        buf.write("\t\7\2\2\u024d\u024f\5~@\2\u024e\u024b\3\2\2\2\u024f\u0252")
        buf.write("\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251\3\2\2\2\u0251")
        buf.write("}\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0254\7#\2\2\u0254")
        buf.write("\u0257\5~@\2\u0255\u0257\5\u0080A\2\u0256\u0253\3\2\2")
        buf.write("\2\u0256\u0255\3\2\2\2\u0257\177\3\2\2\2\u0258\u0259\7")
        buf.write("\37\2\2\u0259\u025c\5\u0080A\2\u025a\u025c\5\u0082B\2")
        buf.write("\u025b\u0258\3\2\2\2\u025b\u025a\3\2\2\2\u025c\u0081\3")
        buf.write("\2\2\2\u025d\u025e\bB\1\2\u025e\u025f\5\u0084C\2\u025f")
        buf.write("\u0264\3\2\2\2\u0260\u0261\f\4\2\2\u0261\u0263\5\u008e")
        buf.write("H\2\u0262\u0260\3\2\2\2\u0263\u0266\3\2\2\2\u0264\u0262")
        buf.write("\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0083\3\2\2\2\u0266")
        buf.write("\u0264\3\2\2\2\u0267\u0268\bC\1\2\u0268\u0269\5\u0086")
        buf.write("D\2\u0269\u026e\3\2\2\2\u026a\u026b\f\4\2\2\u026b\u026d")
        buf.write("\5\u0094K\2\u026c\u026a\3\2\2\2\u026d\u0270\3\2\2\2\u026e")
        buf.write("\u026c\3\2\2\2\u026e\u026f\3\2\2\2\u026f\u0085\3\2\2\2")
        buf.write("\u0270\u026e\3\2\2\2\u0271\u0272\79\2\2\u0272\u0275\5")
        buf.write("\u0098M\2\u0273\u0275\5\u0088E\2\u0274\u0271\3\2\2\2\u0274")
        buf.write("\u0273\3\2\2\2\u0275\u0087\3\2\2\2\u0276\u0277\7\31\2")
        buf.write("\2\u0277\u0278\5t;\2\u0278\u0279\7/\2\2\u0279\u027a\5")
        buf.write("\u009cO\2\u027a\u027b\7\60\2\2\u027b\u027e\3\2\2\2\u027c")
        buf.write("\u027e\5\u008aF\2\u027d\u0276\3\2\2\2\u027d\u027c\3\2")
        buf.write("\2\2\u027e\u0089\3\2\2\2\u027f\u0284\5\u00a2R\2\u0280")
        buf.write("\u0284\79\2\2\u0281\u0284\7\33\2\2\u0282\u0284\5\u008c")
        buf.write("G\2\u0283\u027f\3\2\2\2\u0283\u0280\3\2\2\2\u0283\u0281")
        buf.write("\3\2\2\2\u0283\u0282\3\2\2\2\u0284\u008b\3\2\2\2\u0285")
        buf.write("\u0286\7/\2\2\u0286\u0287\5t;\2\u0287\u0288\7\60\2\2\u0288")
        buf.write("\u008d\3\2\2\2\u0289\u028a\bH\1\2\u028a\u028b\7\61\2\2")
        buf.write("\u028b\u028c\5t;\2\u028c\u028d\7\62\2\2\u028d\u0295\3")
        buf.write("\2\2\2\u028e\u028f\f\4\2\2\u028f\u0290\7\61\2\2\u0290")
        buf.write("\u0291\5t;\2\u0291\u0292\7\62\2\2\u0292\u0294\3\2\2\2")
        buf.write("\u0293\u028e\3\2\2\2\u0294\u0297\3\2\2\2\u0295\u0293\3")
        buf.write("\2\2\2\u0295\u0296\3\2\2\2\u0296\u008f\3\2\2\2\u0297\u0295")
        buf.write("\3\2\2\2\u0298\u029d\5\u0092J\2\u0299\u029a\5\u0092J\2")
        buf.write("\u029a\u029b\5\u008eH\2\u029b\u029d\3\2\2\2\u029c\u0298")
        buf.write("\3\2\2\2\u029c\u0299\3\2\2\2\u029d\u0091\3\2\2\2\u029e")
        buf.write("\u02a5\t\2\2\2\u029f\u02a0\5t;\2\u02a0\u02a1\5T+\2\u02a1")
        buf.write("\u02a2\t\2\2\2\u02a2\u02a5\3\2\2\2\u02a3\u02a5\3\2\2\2")
        buf.write("\u02a4\u029e\3\2\2\2\u02a4\u029f\3\2\2\2\u02a4\u02a3\3")
        buf.write("\2\2\2\u02a5\u0093\3\2\2\2\u02a6\u02a7\5\u0096L\2\u02a7")
        buf.write("\u02a8\5\u0094K\2\u02a8\u02ab\3\2\2\2\u02a9\u02ab\5\u0096")
        buf.write("L\2\u02aa\u02a6\3\2\2\2\u02aa\u02a9\3\2\2\2\u02ab\u0095")
        buf.write("\3\2\2\2\u02ac\u02ad\7\65\2\2\u02ad\u02b5\79\2\2\u02ae")
        buf.write("\u02af\7\65\2\2\u02af\u02b0\79\2\2\u02b0\u02b1\7/\2\2")
        buf.write("\u02b1\u02b2\5\u009cO\2\u02b2\u02b3\7\60\2\2\u02b3\u02b5")
        buf.write("\3\2\2\2\u02b4\u02ac\3\2\2\2\u02b4\u02ae\3\2\2\2\u02b5")
        buf.write("\u0097\3\2\2\2\u02b6\u02b7\5\u009aN\2\u02b7\u02b8\5\u0098")
        buf.write("M\2\u02b8\u02bb\3\2\2\2\u02b9\u02bb\5\u009aN\2\u02ba\u02b6")
        buf.write("\3\2\2\2\u02ba\u02b9\3\2\2\2\u02bb\u0099\3\2\2\2\u02bc")
        buf.write("\u02bd\7\34\2\2\u02bd\u02c5\7:\2\2\u02be\u02bf\7\34\2")
        buf.write("\2\u02bf\u02c0\7:\2\2\u02c0\u02c1\7/\2\2\u02c1\u02c2\5")
        buf.write("\u009cO\2\u02c2\u02c3\7\60\2\2\u02c3\u02c5\3\2\2\2\u02c4")
        buf.write("\u02bc\3\2\2\2\u02c4\u02be\3\2\2\2\u02c5\u009b\3\2\2\2")
        buf.write("\u02c6\u02c7\5t;\2\u02c7\u02c8\7\66\2\2\u02c8\u02c9\5")
        buf.write("\u009cO\2\u02c9\u02cd\3\2\2\2\u02ca\u02cd\5t;\2\u02cb")
        buf.write("\u02cd\3\2\2\2\u02cc\u02c6\3\2\2\2\u02cc\u02ca\3\2\2\2")
        buf.write("\u02cc\u02cb\3\2\2\2\u02cd\u009d\3\2\2\2\u02ce\u02cf\7")
        buf.write("\f\2\2\u02cf\u02d0\7/\2\2\u02d0\u02d1\5\u00a0Q\2\u02d1")
        buf.write("\u02d2\7\60\2\2\u02d2\u009f\3\2\2\2\u02d3\u02d4\5t;\2")
        buf.write("\u02d4\u02d5\7\66\2\2\u02d5\u02d6\5\u00a0Q\2\u02d6\u02da")
        buf.write("\3\2\2\2\u02d7\u02da\5t;\2\u02d8\u02da\3\2\2\2\u02d9\u02d3")
        buf.write("\3\2\2\2\u02d9\u02d7\3\2\2\2\u02d9\u02d8\3\2\2\2\u02da")
        buf.write("\u00a1\3\2\2\2\u02db\u02e2\7=\2\2\u02dc\u02e2\7>\2\2\u02dd")
        buf.write("\u02e2\7<\2\2\u02de\u02e2\7\t\2\2\u02df\u02e2\7;\2\2\u02e0")
        buf.write("\u02e2\5\u009eP\2\u02e1\u02db\3\2\2\2\u02e1\u02dc\3\2")
        buf.write("\2\2\u02e1\u02dd\3\2\2\2\u02e1\u02de\3\2\2\2\u02e1\u02df")
        buf.write("\3\2\2\2\u02e1\u02e0\3\2\2\2\u02e2\u00a3\3\2\2\2\u02e3")
        buf.write("\u02e4\5\u00a6T\2\u02e4\u02e5\78\2\2\u02e5\u02e6\5\u00a4")
        buf.write("S\2\u02e6\u02ea\3\2\2\2\u02e7\u02ea\5\u00a6T\2\u02e8\u02ea")
        buf.write("\3\2\2\2\u02e9\u02e3\3\2\2\2\u02e9\u02e7\3\2\2\2\u02e9")
        buf.write("\u02e8\3\2\2\2\u02ea\u00a5\3\2\2\2\u02eb\u02ec\5\u00a8")
        buf.write("U\2\u02ec\u02ed\7\67\2\2\u02ed\u02ee\5\u00b4[\2\u02ee")
        buf.write("\u00a7\3\2\2\2\u02ef\u02f0\t\2\2\2\u02f0\u02f1\7\66\2")
        buf.write("\2\u02f1\u02f5\5\u00a8U\2\u02f2\u02f5\t\2\2\2\u02f3\u02f5")
        buf.write("\3\2\2\2\u02f4\u02ef\3\2\2\2\u02f4\u02f2\3\2\2\2\u02f4")
        buf.write("\u02f3\3\2\2\2\u02f5\u00a9\3\2\2\2\u02f6\u02f7\79\2\2")
        buf.write("\u02f7\u02f8\7\66\2\2\u02f8\u02fc\5\u00aaV\2\u02f9\u02fc")
        buf.write("\79\2\2\u02fa\u02fc\3\2\2\2\u02fb\u02f6\3\2\2\2\u02fb")
        buf.write("\u02f9\3\2\2\2\u02fb\u02fa\3\2\2\2\u02fc\u00ab\3\2\2\2")
        buf.write("\u02fd\u0300\5\u00a2R\2\u02fe\u0300\5t;\2\u02ff\u02fd")
        buf.write("\3\2\2\2\u02ff\u02fe\3\2\2\2\u0300\u0301\3\2\2\2\u0301")
        buf.write("\u0302\7\66\2\2\u0302\u0303\5\u00acW\2\u0303\u030a\3\2")
        buf.write("\2\2\u0304\u0307\5\u00a2R\2\u0305\u0307\5t;\2\u0306\u0304")
        buf.write("\3\2\2\2\u0306\u0305\3\2\2\2\u0307\u030a\3\2\2\2\u0308")
        buf.write("\u030a\3\2\2\2\u0309\u02ff\3\2\2\2\u0309\u0306\3\2\2\2")
        buf.write("\u0309\u0308\3\2\2\2\u030a\u00ad\3\2\2\2\u030b\u030c\7")
        buf.write("\f\2\2\u030c\u030d\7\61\2\2\u030d\u030e\5\u00b0Y\2\u030e")
        buf.write("\u030f\7\66\2\2\u030f\u0310\7=\2\2\u0310\u0311\7\62\2")
        buf.write("\2\u0311\u00af\3\2\2\2\u0312\u0318\5\u00aeX\2\u0313\u0318")
        buf.write("\7\16\2\2\u0314\u0318\7\17\2\2\u0315\u0318\7\20\2\2\u0316")
        buf.write("\u0318\7\21\2\2\u0317\u0312\3\2\2\2\u0317\u0313\3\2\2")
        buf.write("\2\u0317\u0314\3\2\2\2\u0317\u0315\3\2\2\2\u0317\u0316")
        buf.write("\3\2\2\2\u0318\u00b1\3\2\2\2\u0319\u031a\t\b\2\2\u031a")
        buf.write("\u00b3\3\2\2\2\u031b\u031f\5\u00b2Z\2\u031c\u031f\5\u00ae")
        buf.write("X\2\u031d\u031f\79\2\2\u031e\u031b\3\2\2\2\u031e\u031c")
        buf.write("\3\2\2\2\u031e\u031d\3\2\2\2\u031f\u00b5\3\2\2\2;\u00bd")
        buf.write("\u00c7\u00e6\u00f2\u0106\u0112\u0122\u0129\u0133\u013f")
        buf.write("\u0153\u015f\u0173\u0178\u017f\u0188\u0198\u019c\u01ac")
        buf.write("\u01b5\u01bd\u01e2\u01ef\u0202\u0209\u0212\u0222\u0229")
        buf.write("\u0230\u023a\u0245\u0250\u0256\u025b\u0264\u026e\u0274")
        buf.write("\u027d\u0283\u0295\u029c\u02a4\u02aa\u02b4\u02ba\u02c4")
        buf.write("\u02cc\u02d9\u02e1\u02e9\u02f4\u02fb\u02ff\u0306\u0309")
        buf.write("\u0317\u031e")
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
    RULE_var_type_and_assign = 9
    RULE_val_variable_declaration_noinit = 10
    RULE_val_variable_declaration = 11
    RULE_val_declare_initiate_list = 12
    RULE_val_type_and_assign = 13
    RULE_var_both_variable_declaration_noinnit = 14
    RULE_var_both_variable_declaration = 15
    RULE_var_both_no_value_assign_declare_list = 16
    RULE_var_both_no_value_assign_declare = 17
    RULE_var_both_declare_initiate_list = 18
    RULE_var_both_type_and_assign = 19
    RULE_val_both_variable_declaration_noinnit = 20
    RULE_val_both_variable_declaration = 21
    RULE_val_both_declare_initiate_list = 22
    RULE_val_both_type_and_assign = 23
    RULE_function_declaration = 24
    RULE_call_func_statement = 25
    RULE_call_func = 26
    RULE_call_func_header = 27
    RULE_call_func_attr_list = 28
    RULE_call_func_attr = 29
    RULE_call_func_end = 30
    RULE_assignment_statements = 31
    RULE_lhs = 32
    RULE_if_condition = 33
    RULE_if_statements = 34
    RULE_elseif_list_statements = 35
    RULE_elseif_statement = 36
    RULE_else_statement_or_none = 37
    RULE_else_statement = 38
    RULE_by_expr = 39
    RULE_forin_statements = 40
    RULE_instance_attr_access = 41
    RULE_instance_method_access = 42
    RULE_static_attr_access = 43
    RULE_static_method_access = 44
    RULE_method_invocation = 45
    RULE_method_invocation_statement = 46
    RULE_break_statements = 47
    RULE_continue_statements = 48
    RULE_return_expr = 49
    RULE_return_statements = 50
    RULE_block_class_statements = 51
    RULE_block_statements = 52
    RULE_statements_class = 53
    RULE_statements = 54
    RULE_statement_class = 55
    RULE_statement = 56
    RULE_expr = 57
    RULE_expr1 = 58
    RULE_expr2 = 59
    RULE_expr3 = 60
    RULE_expr4 = 61
    RULE_expr5 = 62
    RULE_expr6 = 63
    RULE_expr7 = 64
    RULE_expr8 = 65
    RULE_expr9 = 66
    RULE_expr10 = 67
    RULE_expr11 = 68
    RULE_expr12 = 69
    RULE_index_operators = 70
    RULE_index_expr = 71
    RULE_index = 72
    RULE_instance_accesses = 73
    RULE_instance_access = 74
    RULE_static_accesses = 75
    RULE_static_access = 76
    RULE_list_expr = 77
    RULE_array_lit = 78
    RULE_array_val = 79
    RULE_literal = 80
    RULE_list_parameters = 81
    RULE_param = 82
    RULE_identifier_list = 83
    RULE_variable_in_func_identifier_list = 84
    RULE_value_list = 85
    RULE_array_type = 86
    RULE_array_element_type = 87
    RULE_primitive_type = 88
    RULE_variable_type = 89

    ruleNames =  [ "program", "class_declarations", "class_declaration", 
                   "class_inheritance", "constructor_dclr", "destructor_dclr", 
                   "var_variable_declaration_noinit", "var_variable_declaration", 
                   "var_declare_initiate_list", "var_type_and_assign", "val_variable_declaration_noinit", 
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
            self.state = 180
            self.class_declarations()
            self.state = 181
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
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.class_declaration()
                self.state = 184
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
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
            self.state = 189
            self.match(D96Parser.CLASS)
            self.state = 190
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 191
            self.class_inheritance()
            self.state = 192
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
            self.state = 197
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(D96Parser.COLON)
                self.state = 195
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
            self.state = 199
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 200
            self.match(D96Parser.LB)
            self.state = 201
            self.list_parameters()
            self.state = 202
            self.match(D96Parser.RB)
            self.state = 203
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
            self.state = 205
            self.match(D96Parser.DESTRUCTOR)
            self.state = 206
            self.match(D96Parser.LB)
            self.state = 207
            self.match(D96Parser.RB)
            self.state = 208
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
        self.enterRule(localctx, 12, self.RULE_var_variable_declaration_noinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(D96Parser.VAR)
            self.state = 211
            self.variable_in_func_identifier_list()
            self.state = 212
            self.match(D96Parser.COLON)
            self.state = 213
            self.variable_type()
            self.state = 214
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
        self.enterRule(localctx, 14, self.RULE_var_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(D96Parser.VAR)
            self.state = 217
            self.var_declare_initiate_list()
            self.state = 218
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
        self.enterRule(localctx, 16, self.RULE_var_declare_initiate_list)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 221
                self.var_type_and_assign()
                self.state = 222
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.variable_in_func_identifier_list()
                self.state = 225
                self.match(D96Parser.COLON)
                self.state = 226
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
        self.enterRule(localctx, 18, self.RULE_var_type_and_assign)
        try:
            self.state = 240
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                self.match(D96Parser.COMMA)
                self.state = 231
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 232
                self.var_type_and_assign()
                self.state = 233
                self.expr()
                self.state = 234
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(D96Parser.COLON)
                self.state = 237
                self.variable_type()
                self.state = 238
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
        self.enterRule(localctx, 20, self.RULE_val_variable_declaration_noinit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(D96Parser.VAL)
            self.state = 243
            self.variable_in_func_identifier_list()
            self.state = 244
            self.match(D96Parser.COLON)
            self.state = 245
            self.variable_type()
            self.state = 246
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
        self.enterRule(localctx, 22, self.RULE_val_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(D96Parser.VAL)
            self.state = 249
            self.val_declare_initiate_list()
            self.state = 250
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
        self.enterRule(localctx, 24, self.RULE_val_declare_initiate_list)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 253
                self.val_type_and_assign()
                self.state = 254
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.variable_in_func_identifier_list()
                self.state = 257
                self.match(D96Parser.COLON)
                self.state = 258
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
        self.enterRule(localctx, 26, self.RULE_val_type_and_assign)
        try:
            self.state = 272
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(D96Parser.COMMA)
                self.state = 263
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 264
                self.val_type_and_assign()
                self.state = 265
                self.expr()
                self.state = 266
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(D96Parser.COLON)
                self.state = 269
                self.variable_type()
                self.state = 270
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
        self.enterRule(localctx, 28, self.RULE_var_both_variable_declaration_noinnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(D96Parser.VAR)
            self.state = 275
            self.identifier_list()
            self.state = 276
            self.match(D96Parser.COLON)
            self.state = 277
            self.variable_type()
            self.state = 278
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
        self.enterRule(localctx, 30, self.RULE_var_both_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(D96Parser.VAR)
            self.state = 281
            self.var_both_declare_initiate_list()
            self.state = 282
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
        self.enterRule(localctx, 32, self.RULE_var_both_no_value_assign_declare_list)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.var_both_no_value_assign_declare()
                self.state = 285
                self.var_both_no_value_assign_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 287
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
        self.enterRule(localctx, 34, self.RULE_var_both_no_value_assign_declare)
        self._la = 0 # Token type
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 291
                self.match(D96Parser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 292
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 293
                self.match(D96Parser.COLON)
                self.state = 294
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
        self.enterRule(localctx, 36, self.RULE_var_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 298
                self.var_both_type_and_assign()
                self.state = 299
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.variable_in_func_identifier_list()
                self.state = 302
                self.match(D96Parser.COLON)
                self.state = 303
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
        self.enterRule(localctx, 38, self.RULE_var_both_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 317
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.match(D96Parser.COMMA)
                self.state = 308
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 309
                self.var_both_type_and_assign()
                self.state = 310
                self.expr()
                self.state = 311
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
                self.match(D96Parser.COLON)
                self.state = 314
                self.variable_type()
                self.state = 315
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
        self.enterRule(localctx, 40, self.RULE_val_both_variable_declaration_noinnit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(D96Parser.VAL)
            self.state = 320
            self.identifier_list()
            self.state = 321
            self.match(D96Parser.COLON)
            self.state = 322
            self.variable_type()
            self.state = 323
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
        self.enterRule(localctx, 42, self.RULE_val_both_variable_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(D96Parser.VAL)
            self.state = 326
            self.val_both_declare_initiate_list()
            self.state = 327
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
        self.enterRule(localctx, 44, self.RULE_val_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 330
                self.val_both_type_and_assign()
                self.state = 331
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 333
                self.variable_in_func_identifier_list()
                self.state = 334
                self.match(D96Parser.COLON)
                self.state = 335
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
        self.enterRule(localctx, 46, self.RULE_val_both_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 339
                self.match(D96Parser.COMMA)
                self.state = 340
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 341
                self.val_both_type_and_assign()
                self.state = 342
                self.expr()
                self.state = 343
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.match(D96Parser.COLON)
                self.state = 346
                self.variable_type()
                self.state = 347
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
        self.enterRule(localctx, 48, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 352
            self.match(D96Parser.LB)
            self.state = 353
            self.list_parameters()
            self.state = 354
            self.match(D96Parser.RB)
            self.state = 355
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
        self.enterRule(localctx, 50, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.call_func_header()
            self.state = 358
            self.call_func_attr_list()
            self.state = 359
            self.call_func_end()
            self.state = 360
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
        self.enterRule(localctx, 52, self.RULE_call_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 362
            self.call_func_header()
            self.state = 363
            self.call_func_attr_list()
            self.state = 364
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
        self.enterRule(localctx, 54, self.RULE_call_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 367
                self.index_operators(0)
                pass
            elif token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOUBLECOLONOP]:
                self.state = 371
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 372
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
        self.enterRule(localctx, 56, self.RULE_call_func_attr_list)
        try:
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.call_func_attr()
                self.state = 377
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
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
        self.enterRule(localctx, 58, self.RULE_call_func_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.match(D96Parser.DOT)
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 384
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 385
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 386
                self.match(D96Parser.LB)
                self.state = 387
                self.value_list()
                self.state = 388
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
        self.enterRule(localctx, 60, self.RULE_call_func_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.match(D96Parser.DOT)
            self.state = 393
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 394
            self.match(D96Parser.LB)
            self.state = 395
            self.value_list()
            self.state = 396
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
        self.enterRule(localctx, 62, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.lhs()
            self.state = 399
            self.match(D96Parser.ASSIGNOP)
            self.state = 400
            self.expr()
            self.state = 401
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
        self.enterRule(localctx, 64, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 403
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 404
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.state = 405
                self.static_attr_access()
                pass


            self.state = 410
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 408
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
        self.enterRule(localctx, 66, self.RULE_if_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(D96Parser.LB)
            self.state = 413
            self.expr()
            self.state = 414
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
        self.enterRule(localctx, 68, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(D96Parser.IF)
            self.state = 417
            self.if_condition()
            self.state = 418
            self.block_statements()
            self.state = 419
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
        self.enterRule(localctx, 70, self.RULE_elseif_list_statements)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.elseif_statement()
                self.state = 422
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.elseif_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 425
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
        self.enterRule(localctx, 72, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.ELSEIF)
            self.state = 429
            self.if_condition()
            self.state = 430
            self.block_statements()
            self.state = 431
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
        self.enterRule(localctx, 74, self.RULE_else_statement_or_none)
        try:
            self.state = 435
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
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
        self.enterRule(localctx, 76, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(D96Parser.ELSE)
            self.state = 438
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
        self.enterRule(localctx, 78, self.RULE_by_expr)
        try:
            self.state = 443
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(D96Parser.BY)
                self.state = 441
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
        self.enterRule(localctx, 80, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(D96Parser.FOREACH)
            self.state = 446
            self.match(D96Parser.LB)
            self.state = 447
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 448
            self.match(D96Parser.IN)
            self.state = 449
            self.expr()
            self.state = 450
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 451
            self.expr()
            self.state = 452
            self.by_expr()
            self.state = 453
            self.match(D96Parser.RB)
            self.state = 454
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
        self.enterRule(localctx, 82, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 456
            self.expr()
            self.state = 457
            self.match(D96Parser.DOT)
            self.state = 458
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
        self.enterRule(localctx, 84, self.RULE_instance_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.expr()
            self.state = 461
            self.match(D96Parser.DOT)
            self.state = 462
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 463
            self.match(D96Parser.LB)
            self.state = 464
            self.list_expr()
            self.state = 465
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
        self.enterRule(localctx, 86, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 468
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 469
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
        self.enterRule(localctx, 88, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 472
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 473
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 474
            self.match(D96Parser.LB)
            self.state = 475
            self.list_expr()
            self.state = 476
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
        self.enterRule(localctx, 90, self.RULE_method_invocation)
        try:
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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
        self.enterRule(localctx, 92, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.method_invocation()
            self.state = 483
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
        self.enterRule(localctx, 94, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(D96Parser.BREAK)
            self.state = 486
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
        self.enterRule(localctx, 96, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 488
            self.match(D96Parser.CONTINUE)
            self.state = 489
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
        self.enterRule(localctx, 98, self.RULE_return_expr)
        try:
            self.state = 493
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
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
        self.enterRule(localctx, 100, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.match(D96Parser.RETURN)
            self.state = 496
            self.return_expr()
            self.state = 497
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
        self.enterRule(localctx, 102, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(D96Parser.LCB)
            self.state = 500
            self.statements_class()
            self.state = 501
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
        self.enterRule(localctx, 104, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(D96Parser.LCB)
            self.state = 504
            self.statements()
            self.state = 505
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
        self.enterRule(localctx, 106, self.RULE_statements_class)
        try:
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 507
                self.statement_class()
                self.state = 508
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
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
        self.enterRule(localctx, 108, self.RULE_statements)
        try:
            self.state = 519
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 514
                self.statement()
                self.state = 515
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
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
        self.enterRule(localctx, 110, self.RULE_statement_class)
        try:
            self.state = 528
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.var_both_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.val_both_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
                self.var_both_variable_declaration_noinnit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 524
                self.val_both_variable_declaration_noinnit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 525
                self.function_declaration()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 526
                self.constructor_dclr()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 527
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
        self.enterRule(localctx, 112, self.RULE_statement)
        try:
            self.state = 544
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.var_variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self.val_variable_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 532
                self.var_variable_declaration_noinit()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 533
                self.val_variable_declaration_noinit()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 534
                self.assignment_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 535
                self.val_variable_declaration()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 536
                self.assignment_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 537
                self.if_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 538
                self.forin_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 539
                self.call_func_statement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 540
                self.method_invocation_statement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 541
                self.break_statements()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 542
                self.continue_statements()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 543
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
        self.enterRule(localctx, 114, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.expr1()
                self.state = 547
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 548
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 550
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
        self.enterRule(localctx, 116, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 558
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                self.expr2(0)
                self.state = 554
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 555
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 557
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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 568
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 563
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 564
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 565
                    self.expr3(0) 
                self.state = 570
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
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 579
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 574
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 575
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 576
                    self.expr4(0) 
                self.state = 581
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
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 585
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 586
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 587
                    self.expr5() 
                self.state = 592
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
        self.enterRule(localctx, 124, self.RULE_expr5)
        try:
            self.state = 596
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.match(D96Parser.NOTOP)
                self.state = 594
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
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
        self.enterRule(localctx, 126, self.RULE_expr6)
        try:
            self.state = 601
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.match(D96Parser.MINUSOP)
                self.state = 599
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
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
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 610
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 606
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 607
                    self.index_operators(0) 
                self.state = 612
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
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 620
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 616
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 617
                    self.instance_accesses() 
                self.state = 622
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
        self.enterRule(localctx, 132, self.RULE_expr9)
        try:
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 623
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 624
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
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
        self.enterRule(localctx, 134, self.RULE_expr10)
        try:
            self.state = 635
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 628
                self.match(D96Parser.NEW)
                self.state = 629
                self.expr()
                self.state = 630
                self.match(D96Parser.LB)
                self.state = 631
                self.list_expr()
                self.state = 632
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 634
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
        self.enterRule(localctx, 136, self.RULE_expr11)
        try:
            self.state = 641
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 637
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 638
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 639
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 640
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
        self.enterRule(localctx, 138, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 643
            self.match(D96Parser.LB)
            self.state = 644
            self.expr()
            self.state = 645
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
        _startState = 140
        self.enterRecursionRule(localctx, 140, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            self.match(D96Parser.LSB)
            self.state = 649
            self.expr()
            self.state = 650
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 659
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 652
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 653
                    self.match(D96Parser.LSB)
                    self.state = 654
                    self.expr()
                    self.state = 655
                    self.match(D96Parser.RSB) 
                self.state = 661
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
        self.enterRule(localctx, 142, self.RULE_index_expr)
        try:
            self.state = 666
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 662
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 663
                self.index()
                self.state = 664
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
        self.enterRule(localctx, 144, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 668
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 669
                self.expr()
                self.state = 670
                self.instance_attr_access()
                self.state = 671
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
        self.enterRule(localctx, 146, self.RULE_instance_accesses)
        try:
            self.state = 680
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 676
                self.instance_access()
                self.state = 677
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 679
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
        self.enterRule(localctx, 148, self.RULE_instance_access)
        try:
            self.state = 690
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 682
                self.match(D96Parser.DOT)
                self.state = 683
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 684
                self.match(D96Parser.DOT)
                self.state = 685
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 686
                self.match(D96Parser.LB)
                self.state = 687
                self.list_expr()
                self.state = 688
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
        self.enterRule(localctx, 150, self.RULE_static_accesses)
        try:
            self.state = 696
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.static_access()
                self.state = 693
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 695
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
        self.enterRule(localctx, 152, self.RULE_static_access)
        try:
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 698
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 699
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 700
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 701
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 702
                self.match(D96Parser.LB)
                self.state = 703
                self.list_expr()
                self.state = 704
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
        self.enterRule(localctx, 154, self.RULE_list_expr)
        try:
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 708
                self.expr()
                self.state = 709
                self.match(D96Parser.COMMA)
                self.state = 710
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 712
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
        self.enterRule(localctx, 156, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 716
            self.match(D96Parser.ARRAY)
            self.state = 717
            self.match(D96Parser.LB)
            self.state = 718
            self.array_val()
            self.state = 719
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
        self.enterRule(localctx, 158, self.RULE_array_val)
        try:
            self.state = 727
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 721
                self.expr()
                self.state = 722
                self.match(D96Parser.COMMA)
                self.state = 723
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 725
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
        self.enterRule(localctx, 160, self.RULE_literal)
        try:
            self.state = 735
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 730
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 731
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 732
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 733
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 734
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
        self.enterRule(localctx, 162, self.RULE_list_parameters)
        try:
            self.state = 743
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 737
                self.param()
                self.state = 738
                self.match(D96Parser.SEMICOLON)
                self.state = 739
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 741
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
        self.enterRule(localctx, 164, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 745
            self.identifier_list()
            self.state = 746
            self.match(D96Parser.COLON)
            self.state = 747
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
        self.enterRule(localctx, 166, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 754
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 749
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 750
                self.match(D96Parser.COMMA)
                self.state = 751
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 752
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
        self.enterRule(localctx, 168, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 761
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 756
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 757
                self.match(D96Parser.COMMA)
                self.state = 758
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 759
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
        self.enterRule(localctx, 170, self.RULE_value_list)
        try:
            self.state = 775
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 765
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 763
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 764
                    self.expr()
                    pass


                self.state = 767
                self.match(D96Parser.COMMA)
                self.state = 768
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 772
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 770
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 771
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
        self.enterRule(localctx, 172, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
            self.match(D96Parser.ARRAY)
            self.state = 778
            self.match(D96Parser.LSB)
            self.state = 779
            self.array_element_type()
            self.state = 780
            self.match(D96Parser.COMMA)
            self.state = 781
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 782
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
        self.enterRule(localctx, 174, self.RULE_array_element_type)
        try:
            self.state = 789
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 784
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 785
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 786
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 787
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 788
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
        self.enterRule(localctx, 176, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 791
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
        self.enterRule(localctx, 178, self.RULE_variable_type)
        try:
            self.state = 796
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 793
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 794
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 795
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
        self._predicates[59] = self.expr2_sempred
        self._predicates[60] = self.expr3_sempred
        self._predicates[61] = self.expr4_sempred
        self._predicates[64] = self.expr7_sempred
        self._predicates[65] = self.expr8_sempred
        self._predicates[70] = self.index_operators_sempred
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
         




