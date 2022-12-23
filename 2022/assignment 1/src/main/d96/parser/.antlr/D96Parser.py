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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3C")
        buf.write("\u02dc\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3\2\3\3")
        buf.write("\3\3\3\3\3\3\5\3\u00ae\n\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5")
        buf.write("\3\5\5\5\u00b8\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00ce")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00d6\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00dd\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00e7\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00f3\n\r\3\16\3\16\3\16\5\16\u00f8\n\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u0100\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u0107\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u0111\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u011d\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0131\n\26\3\26\3")
        buf.write("\26\3\26\5\26\u0136\n\26\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u013d\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0146")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\5\33\u0156\n\33\3\33\3\33\5\33\u015a")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0167\n\34\3\35\3\35\3\35\3\35\5\35\u016d\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \5 \u017b\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3&\3&\5&\u01a0\n&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3)\3*\3*\5*\u01ad\n*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\5/\u01c6\n/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u01cd\n\60\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u01d3\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u01de\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u01e5\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u01ec\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u01f4\n\65\f\65")
        buf.write("\16\65\u01f7\13\65\3\66\3\66\3\66\3\66\3\66\3\66\7\66")
        buf.write("\u01ff\n\66\f\66\16\66\u0202\13\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u020a\n\67\f\67\16\67\u020d\13\67\38\3")
        buf.write("8\38\58\u0212\n8\39\39\39\59\u0217\n9\3:\3:\3:\3:\3:\7")
        buf.write(":\u021e\n:\f:\16:\u0221\13:\3;\3;\3;\3;\3;\7;\u0228\n")
        buf.write(";\f;\16;\u022b\13;\3<\3<\3<\5<\u0230\n<\3=\3=\3=\3=\3")
        buf.write("=\3=\3=\5=\u0239\n=\3>\3>\3>\3>\5>\u023f\n>\3?\3?\3?\3")
        buf.write("?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\7@\u024f\n@\f@\16@\u0252")
        buf.write("\13@\3A\3A\3A\3A\5A\u0258\nA\3B\3B\3B\3B\3B\3B\5B\u0260")
        buf.write("\nB\3C\3C\3C\3C\5C\u0266\nC\3D\3D\3D\3D\3D\3D\3D\3D\5")
        buf.write("D\u0270\nD\3E\3E\3E\3E\5E\u0276\nE\3F\3F\3F\3F\3F\3F\3")
        buf.write("F\3F\5F\u0280\nF\3G\3G\3G\3G\3G\3G\5G\u0288\nG\3H\3H\3")
        buf.write("H\3H\3H\3I\3I\3I\3I\3I\3I\5I\u0295\nI\3J\3J\3J\3J\3J\3")
        buf.write("J\5J\u029d\nJ\3K\3K\3K\3K\3K\3K\5K\u02a5\nK\3L\3L\3L\3")
        buf.write("L\3M\3M\3M\3M\3M\5M\u02b0\nM\3N\3N\3N\3N\3N\5N\u02b7\n")
        buf.write("N\3O\3O\5O\u02bb\nO\3O\3O\3O\3O\3O\5O\u02c2\nO\3O\5O\u02c5")
        buf.write("\nO\3P\3P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3Q\5Q\u02d3\nQ\3")
        buf.write("R\3R\3S\3S\3S\5S\u02da\nS\3S\2\bhjlrt~T\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDF")
        buf.write("HJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098")
        buf.write("\u009a\u009c\u009e\u00a0\u00a2\u00a4\2\n\3\29:\3\2\25")
        buf.write("\26\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3\2\16\21\2\u02e4")
        buf.write("\2\u00a6\3\2\2\2\4\u00ad\3\2\2\2\6\u00af\3\2\2\2\b\u00b7")
        buf.write("\3\2\2\2\n\u00b9\3\2\2\2\f\u00bf\3\2\2\2\16\u00c4\3\2")
        buf.write("\2\2\20\u00ca\3\2\2\2\22\u00d5\3\2\2\2\24\u00dc\3\2\2")
        buf.write("\2\26\u00e6\3\2\2\2\30\u00f2\3\2\2\2\32\u00f4\3\2\2\2")
        buf.write("\34\u00ff\3\2\2\2\36\u0106\3\2\2\2 \u0110\3\2\2\2\"\u011c")
        buf.write("\3\2\2\2$\u011e\3\2\2\2&\u0124\3\2\2\2(\u0129\3\2\2\2")
        buf.write("*\u012d\3\2\2\2,\u013c\3\2\2\2.\u013e\3\2\2\2\60\u0147")
        buf.write("\3\2\2\2\62\u014d\3\2\2\2\64\u0155\3\2\2\2\66\u015b\3")
        buf.write("\2\2\28\u016c\3\2\2\2:\u016e\3\2\2\2<\u0174\3\2\2\2>\u017a")
        buf.write("\3\2\2\2@\u017c\3\2\2\2B\u0187\3\2\2\2D\u018b\3\2\2\2")
        buf.write("F\u0192\3\2\2\2H\u0196\3\2\2\2J\u019f\3\2\2\2L\u01a1\3")
        buf.write("\2\2\2N\u01a4\3\2\2\2P\u01a7\3\2\2\2R\u01ac\3\2\2\2T\u01ae")
        buf.write("\3\2\2\2V\u01b2\3\2\2\2X\u01b6\3\2\2\2Z\u01ba\3\2\2\2")
        buf.write("\\\u01c5\3\2\2\2^\u01cc\3\2\2\2`\u01d2\3\2\2\2b\u01dd")
        buf.write("\3\2\2\2d\u01e4\3\2\2\2f\u01eb\3\2\2\2h\u01ed\3\2\2\2")
        buf.write("j\u01f8\3\2\2\2l\u0203\3\2\2\2n\u0211\3\2\2\2p\u0216\3")
        buf.write("\2\2\2r\u0218\3\2\2\2t\u0222\3\2\2\2v\u022f\3\2\2\2x\u0238")
        buf.write("\3\2\2\2z\u023e\3\2\2\2|\u0240\3\2\2\2~\u0244\3\2\2\2")
        buf.write("\u0080\u0257\3\2\2\2\u0082\u025f\3\2\2\2\u0084\u0265\3")
        buf.write("\2\2\2\u0086\u026f\3\2\2\2\u0088\u0275\3\2\2\2\u008a\u027f")
        buf.write("\3\2\2\2\u008c\u0287\3\2\2\2\u008e\u0289\3\2\2\2\u0090")
        buf.write("\u0294\3\2\2\2\u0092\u029c\3\2\2\2\u0094\u02a4\3\2\2\2")
        buf.write("\u0096\u02a6\3\2\2\2\u0098\u02af\3\2\2\2\u009a\u02b6\3")
        buf.write("\2\2\2\u009c\u02c4\3\2\2\2\u009e\u02c6\3\2\2\2\u00a0\u02d2")
        buf.write("\3\2\2\2\u00a2\u02d4\3\2\2\2\u00a4\u02d9\3\2\2\2\u00a6")
        buf.write("\u00a7\5\4\3\2\u00a7\u00a8\7\2\2\3\u00a8\3\3\2\2\2\u00a9")
        buf.write("\u00aa\5\6\4\2\u00aa\u00ab\5\4\3\2\u00ab\u00ae\3\2\2\2")
        buf.write("\u00ac\u00ae\5\6\4\2\u00ad\u00a9\3\2\2\2\u00ad\u00ac\3")
        buf.write("\2\2\2\u00ae\5\3\2\2\2\u00af\u00b0\7\24\2\2\u00b0\u00b1")
        buf.write("\79\2\2\u00b1\u00b2\5\b\5\2\u00b2\u00b3\5V,\2\u00b3\7")
        buf.write("\3\2\2\2\u00b4\u00b5\7\67\2\2\u00b5\u00b8\79\2\2\u00b6")
        buf.write("\u00b8\3\2\2\2\u00b7\u00b4\3\2\2\2\u00b7\u00b6\3\2\2\2")
        buf.write("\u00b8\t\3\2\2\2\u00b9\u00ba\7\27\2\2\u00ba\u00bb\7/\2")
        buf.write("\2\u00bb\u00bc\5\u0094K\2\u00bc\u00bd\7\60\2\2\u00bd\u00be")
        buf.write("\5X-\2\u00be\13\3\2\2\2\u00bf\u00c0\7\30\2\2\u00c0\u00c1")
        buf.write("\7/\2\2\u00c1\u00c2\7\60\2\2\u00c2\u00c3\5X-\2\u00c3\r")
        buf.write("\3\2\2\2\u00c4\u00c5\t\2\2\2\u00c5\u00c6\7/\2\2\u00c6")
        buf.write("\u00c7\5\u0094K\2\u00c7\u00c8\7\60\2\2\u00c8\u00c9\5X")
        buf.write("-\2\u00c9\17\3\2\2\2\u00ca\u00cd\t\3\2\2\u00cb\u00ce\5")
        buf.write("\26\f\2\u00cc\u00ce\5\22\n\2\u00cd\u00cb\3\2\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d0\78\2\2")
        buf.write("\u00d0\21\3\2\2\2\u00d1\u00d2\5\24\13\2\u00d2\u00d3\5")
        buf.write("\22\n\2\u00d3\u00d6\3\2\2\2\u00d4\u00d6\5\24\13\2\u00d5")
        buf.write("\u00d1\3\2\2\2\u00d5\u00d4\3\2\2\2\u00d6\23\3\2\2\2\u00d7")
        buf.write("\u00d8\79\2\2\u00d8\u00dd\7\66\2\2\u00d9\u00dd\79\2\2")
        buf.write("\u00da\u00db\7\67\2\2\u00db\u00dd\5\u00a4S\2\u00dc\u00d7")
        buf.write("\3\2\2\2\u00dc\u00d9\3\2\2\2\u00dc\u00da\3\2\2\2\u00dd")
        buf.write("\25\3\2\2\2\u00de\u00df\79\2\2\u00df\u00e0\5\30\r\2\u00e0")
        buf.write("\u00e1\5d\63\2\u00e1\u00e7\3\2\2\2\u00e2\u00e3\5\u009a")
        buf.write("N\2\u00e3\u00e4\7\67\2\2\u00e4\u00e5\5\u00a4S\2\u00e5")
        buf.write("\u00e7\3\2\2\2\u00e6\u00de\3\2\2\2\u00e6\u00e2\3\2\2\2")
        buf.write("\u00e7\27\3\2\2\2\u00e8\u00e9\7\66\2\2\u00e9\u00ea\79")
        buf.write("\2\2\u00ea\u00eb\5\30\r\2\u00eb\u00ec\5d\63\2\u00ec\u00ed")
        buf.write("\7\66\2\2\u00ed\u00f3\3\2\2\2\u00ee\u00ef\7\67\2\2\u00ef")
        buf.write("\u00f0\5\u00a4S\2\u00f0\u00f1\7\'\2\2\u00f1\u00f3\3\2")
        buf.write("\2\2\u00f2\u00e8\3\2\2\2\u00f2\u00ee\3\2\2\2\u00f3\31")
        buf.write("\3\2\2\2\u00f4\u00f7\t\3\2\2\u00f5\u00f8\5 \21\2\u00f6")
        buf.write("\u00f8\5\34\17\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2")
        buf.write("\2\u00f8\u00f9\3\2\2\2\u00f9\u00fa\78\2\2\u00fa\33\3\2")
        buf.write("\2\2\u00fb\u00fc\5\36\20\2\u00fc\u00fd\5\34\17\2\u00fd")
        buf.write("\u0100\3\2\2\2\u00fe\u0100\5\36\20\2\u00ff\u00fb\3\2\2")
        buf.write("\2\u00ff\u00fe\3\2\2\2\u0100\35\3\2\2\2\u0101\u0102\t")
        buf.write("\2\2\2\u0102\u0107\7\66\2\2\u0103\u0107\t\2\2\2\u0104")
        buf.write("\u0105\7\67\2\2\u0105\u0107\5\u00a4S\2\u0106\u0101\3\2")
        buf.write("\2\2\u0106\u0103\3\2\2\2\u0106\u0104\3\2\2\2\u0107\37")
        buf.write("\3\2\2\2\u0108\u0109\t\2\2\2\u0109\u010a\5\"\22\2\u010a")
        buf.write("\u010b\5d\63\2\u010b\u0111\3\2\2\2\u010c\u010d\5\u009a")
        buf.write("N\2\u010d\u010e\7\67\2\2\u010e\u010f\5\u00a4S\2\u010f")
        buf.write("\u0111\3\2\2\2\u0110\u0108\3\2\2\2\u0110\u010c\3\2\2\2")
        buf.write("\u0111!\3\2\2\2\u0112\u0113\7\66\2\2\u0113\u0114\t\2\2")
        buf.write("\2\u0114\u0115\5\"\22\2\u0115\u0116\5d\63\2\u0116\u0117")
        buf.write("\7\66\2\2\u0117\u011d\3\2\2\2\u0118\u0119\7\67\2\2\u0119")
        buf.write("\u011a\5\u00a4S\2\u011a\u011b\7\'\2\2\u011b\u011d\3\2")
        buf.write("\2\2\u011c\u0112\3\2\2\2\u011c\u0118\3\2\2\2\u011d#\3")
        buf.write("\2\2\2\u011e\u011f\t\2\2\2\u011f\u0120\7/\2\2\u0120\u0121")
        buf.write("\5\u0094K\2\u0121\u0122\7\60\2\2\u0122\u0123\5X-\2\u0123")
        buf.write("%\3\2\2\2\u0124\u0125\5*\26\2\u0125\u0126\5,\27\2\u0126")
        buf.write("\u0127\5\60\31\2\u0127\u0128\78\2\2\u0128\'\3\2\2\2\u0129")
        buf.write("\u012a\5*\26\2\u012a\u012b\5,\27\2\u012b\u012c\5\60\31")
        buf.write("\2\u012c)\3\2\2\2\u012d\u0130\t\2\2\2\u012e\u0131\5~@")
        buf.write("\2\u012f\u0131\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f")
        buf.write("\3\2\2\2\u0131\u0135\3\2\2\2\u0132\u0133\7\34\2\2\u0133")
        buf.write("\u0136\7:\2\2\u0134\u0136\3\2\2\2\u0135\u0132\3\2\2\2")
        buf.write("\u0135\u0134\3\2\2\2\u0136+\3\2\2\2\u0137\u0138\5.\30")
        buf.write("\2\u0138\u0139\5,\27\2\u0139\u013d\3\2\2\2\u013a\u013d")
        buf.write("\5.\30\2\u013b\u013d\3\2\2\2\u013c\u0137\3\2\2\2\u013c")
        buf.write("\u013a\3\2\2\2\u013c\u013b\3\2\2\2\u013d-\3\2\2\2\u013e")
        buf.write("\u0145\7\65\2\2\u013f\u0146\79\2\2\u0140\u0141\79\2\2")
        buf.write("\u0141\u0142\7/\2\2\u0142\u0143\5\u009cO\2\u0143\u0144")
        buf.write("\7\60\2\2\u0144\u0146\3\2\2\2\u0145\u013f\3\2\2\2\u0145")
        buf.write("\u0140\3\2\2\2\u0146/\3\2\2\2\u0147\u0148\7\65\2\2\u0148")
        buf.write("\u0149\79\2\2\u0149\u014a\7/\2\2\u014a\u014b\5\u009cO")
        buf.write("\2\u014b\u014c\7\60\2\2\u014c\61\3\2\2\2\u014d\u014e\5")
        buf.write("\64\33\2\u014e\u014f\7\'\2\2\u014f\u0150\5d\63\2\u0150")
        buf.write("\u0151\78\2\2\u0151\63\3\2\2\2\u0152\u0156\79\2\2\u0153")
        buf.write("\u0156\5B\"\2\u0154\u0156\5F$\2\u0155\u0152\3\2\2\2\u0155")
        buf.write("\u0153\3\2\2\2\u0155\u0154\3\2\2\2\u0156\u0159\3\2\2\2")
        buf.write("\u0157\u015a\5~@\2\u0158\u015a\3\2\2\2\u0159\u0157\3\2")
        buf.write("\2\2\u0159\u0158\3\2\2\2\u015a\65\3\2\2\2\u015b\u015c")
        buf.write("\7\5\2\2\u015c\u015d\7/\2\2\u015d\u015e\5d\63\2\u015e")
        buf.write("\u015f\7\60\2\2\u015f\u0166\5X-\2\u0160\u0161\58\35\2")
        buf.write("\u0161\u0162\5<\37\2\u0162\u0167\3\2\2\2\u0163\u0167\5")
        buf.write("8\35\2\u0164\u0167\5<\37\2\u0165\u0167\3\2\2\2\u0166\u0160")
        buf.write("\3\2\2\2\u0166\u0163\3\2\2\2\u0166\u0164\3\2\2\2\u0166")
        buf.write("\u0165\3\2\2\2\u0167\67\3\2\2\2\u0168\u0169\5:\36\2\u0169")
        buf.write("\u016a\58\35\2\u016a\u016d\3\2\2\2\u016b\u016d\5:\36\2")
        buf.write("\u016c\u0168\3\2\2\2\u016c\u016b\3\2\2\2\u016d9\3\2\2")
        buf.write("\2\u016e\u016f\7\6\2\2\u016f\u0170\7/\2\2\u0170\u0171")
        buf.write("\5d\63\2\u0171\u0172\7\60\2\2\u0172\u0173\5X-\2\u0173")
        buf.write(";\3\2\2\2\u0174\u0175\7\7\2\2\u0175\u0176\5X-\2\u0176")
        buf.write("=\3\2\2\2\u0177\u0178\7\32\2\2\u0178\u017b\5d\63\2\u0179")
        buf.write("\u017b\3\2\2\2\u017a\u0177\3\2\2\2\u017a\u0179\3\2\2\2")
        buf.write("\u017b?\3\2\2\2\u017c\u017d\7\b\2\2\u017d\u017e\7/\2\2")
        buf.write("\u017e\u017f\t\2\2\2\u017f\u0180\7\r\2\2\u0180\u0181\5")
        buf.write("d\63\2\u0181\u0182\7\35\2\2\u0182\u0183\5d\63\2\u0183")
        buf.write("\u0184\5> \2\u0184\u0185\7\60\2\2\u0185\u0186\5X-\2\u0186")
        buf.write("A\3\2\2\2\u0187\u0188\5d\63\2\u0188\u0189\7\65\2\2\u0189")
        buf.write("\u018a\79\2\2\u018aC\3\2\2\2\u018b\u018c\5d\63\2\u018c")
        buf.write("\u018d\7\65\2\2\u018d\u018e\79\2\2\u018e\u018f\7/\2\2")
        buf.write("\u018f\u0190\5\u008cG\2\u0190\u0191\7\60\2\2\u0191E\3")
        buf.write("\2\2\2\u0192\u0193\t\2\2\2\u0193\u0194\7\34\2\2\u0194")
        buf.write("\u0195\7:\2\2\u0195G\3\2\2\2\u0196\u0197\t\2\2\2\u0197")
        buf.write("\u0198\7\34\2\2\u0198\u0199\7:\2\2\u0199\u019a\7/\2\2")
        buf.write("\u019a\u019b\5\u008cG\2\u019b\u019c\7\60\2\2\u019cI\3")
        buf.write("\2\2\2\u019d\u01a0\5D#\2\u019e\u01a0\5H%\2\u019f\u019d")
        buf.write("\3\2\2\2\u019f\u019e\3\2\2\2\u01a0K\3\2\2\2\u01a1\u01a2")
        buf.write("\5J&\2\u01a2\u01a3\78\2\2\u01a3M\3\2\2\2\u01a4\u01a5\7")
        buf.write("\3\2\2\u01a5\u01a6\78\2\2\u01a6O\3\2\2\2\u01a7\u01a8\7")
        buf.write("\4\2\2\u01a8\u01a9\78\2\2\u01a9Q\3\2\2\2\u01aa\u01ad\5")
        buf.write("d\63\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01adS\3\2\2\2\u01ae\u01af\7\22\2\2\u01af\u01b0")
        buf.write("\5R*\2\u01b0\u01b1\78\2\2\u01b1U\3\2\2\2\u01b2\u01b3\7")
        buf.write("\63\2\2\u01b3\u01b4\5\\/\2\u01b4\u01b5\7\64\2\2\u01b5")
        buf.write("W\3\2\2\2\u01b6\u01b7\7\63\2\2\u01b7\u01b8\5^\60\2\u01b8")
        buf.write("\u01b9\7\64\2\2\u01b9Y\3\2\2\2\u01ba\u01bb\7\63\2\2\u01bb")
        buf.write("\u01bc\5^\60\2\u01bc\u01bd\7\22\2\2\u01bd\u01be\78\2\2")
        buf.write("\u01be\u01bf\7\64\2\2\u01bf[\3\2\2\2\u01c0\u01c1\5`\61")
        buf.write("\2\u01c1\u01c2\5\\/\2\u01c2\u01c6\3\2\2\2\u01c3\u01c6")
        buf.write("\5`\61\2\u01c4\u01c6\3\2\2\2\u01c5\u01c0\3\2\2\2\u01c5")
        buf.write("\u01c3\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6]\3\2\2\2\u01c7")
        buf.write("\u01c8\5b\62\2\u01c8\u01c9\5^\60\2\u01c9\u01cd\3\2\2\2")
        buf.write("\u01ca\u01cd\5b\62\2\u01cb\u01cd\3\2\2\2\u01cc\u01c7\3")
        buf.write("\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cb\3\2\2\2\u01cd_")
        buf.write("\3\2\2\2\u01ce\u01d3\5\32\16\2\u01cf\u01d3\5$\23\2\u01d0")
        buf.write("\u01d3\5\n\6\2\u01d1\u01d3\5\f\7\2\u01d2\u01ce\3\2\2\2")
        buf.write("\u01d2\u01cf\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d1\3")
        buf.write("\2\2\2\u01d3a\3\2\2\2\u01d4\u01de\5\20\t\2\u01d5\u01de")
        buf.write("\5\62\32\2\u01d6\u01de\5\66\34\2\u01d7\u01de\5@!\2\u01d8")
        buf.write("\u01de\5&\24\2\u01d9\u01de\5L\'\2\u01da\u01de\5N(\2\u01db")
        buf.write("\u01de\5P)\2\u01dc\u01de\5T+\2\u01dd\u01d4\3\2\2\2\u01dd")
        buf.write("\u01d5\3\2\2\2\u01dd\u01d6\3\2\2\2\u01dd\u01d7\3\2\2\2")
        buf.write("\u01dd\u01d8\3\2\2\2\u01dd\u01d9\3\2\2\2\u01dd\u01da\3")
        buf.write("\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2\u01dec")
        buf.write("\3\2\2\2\u01df\u01e0\5f\64\2\u01e0\u01e1\t\4\2\2\u01e1")
        buf.write("\u01e2\5f\64\2\u01e2\u01e5\3\2\2\2\u01e3\u01e5\5f\64\2")
        buf.write("\u01e4\u01df\3\2\2\2\u01e4\u01e3\3\2\2\2\u01e5e\3\2\2")
        buf.write("\2\u01e6\u01e7\5h\65\2\u01e7\u01e8\t\5\2\2\u01e8\u01e9")
        buf.write("\5h\65\2\u01e9\u01ec\3\2\2\2\u01ea\u01ec\5h\65\2\u01eb")
        buf.write("\u01e6\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ecg\3\2\2\2\u01ed")
        buf.write("\u01ee\b\65\1\2\u01ee\u01ef\5j\66\2\u01ef\u01f5\3\2\2")
        buf.write("\2\u01f0\u01f1\f\4\2\2\u01f1\u01f2\t\6\2\2\u01f2\u01f4")
        buf.write("\5j\66\2\u01f3\u01f0\3\2\2\2\u01f4\u01f7\3\2\2\2\u01f5")
        buf.write("\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6i\3\2\2\2\u01f7")
        buf.write("\u01f5\3\2\2\2\u01f8\u01f9\b\66\1\2\u01f9\u01fa\5l\67")
        buf.write("\2\u01fa\u0200\3\2\2\2\u01fb\u01fc\f\4\2\2\u01fc\u01fd")
        buf.write("\t\7\2\2\u01fd\u01ff\5l\67\2\u01fe\u01fb\3\2\2\2\u01ff")
        buf.write("\u0202\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2")
        buf.write("\u0201k\3\2\2\2\u0202\u0200\3\2\2\2\u0203\u0204\b\67\1")
        buf.write("\2\u0204\u0205\5n8\2\u0205\u020b\3\2\2\2\u0206\u0207\f")
        buf.write("\4\2\2\u0207\u0208\t\b\2\2\u0208\u020a\5n8\2\u0209\u0206")
        buf.write("\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3\2\2\2\u020b")
        buf.write("\u020c\3\2\2\2\u020cm\3\2\2\2\u020d\u020b\3\2\2\2\u020e")
        buf.write("\u020f\7#\2\2\u020f\u0212\5n8\2\u0210\u0212\5p9\2\u0211")
        buf.write("\u020e\3\2\2\2\u0211\u0210\3\2\2\2\u0212o\3\2\2\2\u0213")
        buf.write("\u0214\7\37\2\2\u0214\u0217\5p9\2\u0215\u0217\5r:\2\u0216")
        buf.write("\u0213\3\2\2\2\u0216\u0215\3\2\2\2\u0217q\3\2\2\2\u0218")
        buf.write("\u0219\b:\1\2\u0219\u021a\5t;\2\u021a\u021f\3\2\2\2\u021b")
        buf.write("\u021c\f\4\2\2\u021c\u021e\5~@\2\u021d\u021b\3\2\2\2\u021e")
        buf.write("\u0221\3\2\2\2\u021f\u021d\3\2\2\2\u021f\u0220\3\2\2\2")
        buf.write("\u0220s\3\2\2\2\u0221\u021f\3\2\2\2\u0222\u0223\b;\1\2")
        buf.write("\u0223\u0224\5v<\2\u0224\u0229\3\2\2\2\u0225\u0226\f\4")
        buf.write("\2\2\u0226\u0228\5\u0084C\2\u0227\u0225\3\2\2\2\u0228")
        buf.write("\u022b\3\2\2\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2")
        buf.write("\u022au\3\2\2\2\u022b\u0229\3\2\2\2\u022c\u022d\79\2\2")
        buf.write("\u022d\u0230\5\u0088E\2\u022e\u0230\5x=\2\u022f\u022c")
        buf.write("\3\2\2\2\u022f\u022e\3\2\2\2\u0230w\3\2\2\2\u0231\u0232")
        buf.write("\7\31\2\2\u0232\u0233\5d\63\2\u0233\u0234\7/\2\2\u0234")
        buf.write("\u0235\5\u008cG\2\u0235\u0236\7\60\2\2\u0236\u0239\3\2")
        buf.write("\2\2\u0237\u0239\5z>\2\u0238\u0231\3\2\2\2\u0238\u0237")
        buf.write("\3\2\2\2\u0239y\3\2\2\2\u023a\u023f\5\u0092J\2\u023b\u023f")
        buf.write("\79\2\2\u023c\u023f\7\33\2\2\u023d\u023f\5|?\2\u023e\u023a")
        buf.write("\3\2\2\2\u023e\u023b\3\2\2\2\u023e\u023c\3\2\2\2\u023e")
        buf.write("\u023d\3\2\2\2\u023f{\3\2\2\2\u0240\u0241\7/\2\2\u0241")
        buf.write("\u0242\5d\63\2\u0242\u0243\7\60\2\2\u0243}\3\2\2\2\u0244")
        buf.write("\u0245\b@\1\2\u0245\u0246\7\61\2\2\u0246\u0247\5d\63\2")
        buf.write("\u0247\u0248\7\62\2\2\u0248\u0250\3\2\2\2\u0249\u024a")
        buf.write("\f\4\2\2\u024a\u024b\7\61\2\2\u024b\u024c\5d\63\2\u024c")
        buf.write("\u024d\7\62\2\2\u024d\u024f\3\2\2\2\u024e\u0249\3\2\2")
        buf.write("\2\u024f\u0252\3\2\2\2\u0250\u024e\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\177\3\2\2\2\u0252\u0250\3\2\2\2\u0253\u0258")
        buf.write("\5\u0082B\2\u0254\u0255\5\u0082B\2\u0255\u0256\5~@\2\u0256")
        buf.write("\u0258\3\2\2\2\u0257\u0253\3\2\2\2\u0257\u0254\3\2\2\2")
        buf.write("\u0258\u0081\3\2\2\2\u0259\u0260\t\2\2\2\u025a\u025b\5")
        buf.write("d\63\2\u025b\u025c\5B\"\2\u025c\u025d\t\2\2\2\u025d\u0260")
        buf.write("\3\2\2\2\u025e\u0260\3\2\2\2\u025f\u0259\3\2\2\2\u025f")
        buf.write("\u025a\3\2\2\2\u025f\u025e\3\2\2\2\u0260\u0083\3\2\2\2")
        buf.write("\u0261\u0262\5\u0086D\2\u0262\u0263\5\u0084C\2\u0263\u0266")
        buf.write("\3\2\2\2\u0264\u0266\5\u0086D\2\u0265\u0261\3\2\2\2\u0265")
        buf.write("\u0264\3\2\2\2\u0266\u0085\3\2\2\2\u0267\u0268\7\65\2")
        buf.write("\2\u0268\u0270\79\2\2\u0269\u026a\7\65\2\2\u026a\u026b")
        buf.write("\79\2\2\u026b\u026c\7/\2\2\u026c\u026d\5\u008cG\2\u026d")
        buf.write("\u026e\7\60\2\2\u026e\u0270\3\2\2\2\u026f\u0267\3\2\2")
        buf.write("\2\u026f\u0269\3\2\2\2\u0270\u0087\3\2\2\2\u0271\u0272")
        buf.write("\5\u008aF\2\u0272\u0273\5\u0088E\2\u0273\u0276\3\2\2\2")
        buf.write("\u0274\u0276\5\u008aF\2\u0275\u0271\3\2\2\2\u0275\u0274")
        buf.write("\3\2\2\2\u0276\u0089\3\2\2\2\u0277\u0278\7\34\2\2\u0278")
        buf.write("\u0280\7:\2\2\u0279\u027a\7\34\2\2\u027a\u027b\7:\2\2")
        buf.write("\u027b\u027c\7/\2\2\u027c\u027d\5\u008cG\2\u027d\u027e")
        buf.write("\7\60\2\2\u027e\u0280\3\2\2\2\u027f\u0277\3\2\2\2\u027f")
        buf.write("\u0279\3\2\2\2\u0280\u008b\3\2\2\2\u0281\u0282\5d\63\2")
        buf.write("\u0282\u0283\7\66\2\2\u0283\u0284\5\u008cG\2\u0284\u0288")
        buf.write("\3\2\2\2\u0285\u0288\5d\63\2\u0286\u0288\3\2\2\2\u0287")
        buf.write("\u0281\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0286\3\2\2\2")
        buf.write("\u0288\u008d\3\2\2\2\u0289\u028a\7\f\2\2\u028a\u028b\7")
        buf.write("/\2\2\u028b\u028c\5\u0090I\2\u028c\u028d\7\60\2\2\u028d")
        buf.write("\u008f\3\2\2\2\u028e\u028f\5d\63\2\u028f\u0290\7\66\2")
        buf.write("\2\u0290\u0291\5\u0090I\2\u0291\u0295\3\2\2\2\u0292\u0295")
        buf.write("\5d\63\2\u0293\u0295\3\2\2\2\u0294\u028e\3\2\2\2\u0294")
        buf.write("\u0292\3\2\2\2\u0294\u0293\3\2\2\2\u0295\u0091\3\2\2\2")
        buf.write("\u0296\u029d\7=\2\2\u0297\u029d\7>\2\2\u0298\u029d\7<")
        buf.write("\2\2\u0299\u029d\7\t\2\2\u029a\u029d\7;\2\2\u029b\u029d")
        buf.write("\5\u008eH\2\u029c\u0296\3\2\2\2\u029c\u0297\3\2\2\2\u029c")
        buf.write("\u0298\3\2\2\2\u029c\u0299\3\2\2\2\u029c\u029a\3\2\2\2")
        buf.write("\u029c\u029b\3\2\2\2\u029d\u0093\3\2\2\2\u029e\u029f\5")
        buf.write("\u0096L\2\u029f\u02a0\78\2\2\u02a0\u02a1\5\u0094K\2\u02a1")
        buf.write("\u02a5\3\2\2\2\u02a2\u02a5\5\u0096L\2\u02a3\u02a5\3\2")
        buf.write("\2\2\u02a4\u029e\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a4\u02a3")
        buf.write("\3\2\2\2\u02a5\u0095\3\2\2\2\u02a6\u02a7\5\u0098M\2\u02a7")
        buf.write("\u02a8\7\67\2\2\u02a8\u02a9\5\u00a4S\2\u02a9\u0097\3\2")
        buf.write("\2\2\u02aa\u02ab\t\2\2\2\u02ab\u02ac\7\66\2\2\u02ac\u02b0")
        buf.write("\5\u0098M\2\u02ad\u02b0\t\2\2\2\u02ae\u02b0\3\2\2\2\u02af")
        buf.write("\u02aa\3\2\2\2\u02af\u02ad\3\2\2\2\u02af\u02ae\3\2\2\2")
        buf.write("\u02b0\u0099\3\2\2\2\u02b1\u02b2\79\2\2\u02b2\u02b3\7")
        buf.write("\66\2\2\u02b3\u02b7\5\u009aN\2\u02b4\u02b7\79\2\2\u02b5")
        buf.write("\u02b7\3\2\2\2\u02b6\u02b1\3\2\2\2\u02b6\u02b4\3\2\2\2")
        buf.write("\u02b6\u02b5\3\2\2\2\u02b7\u009b\3\2\2\2\u02b8\u02bb\5")
        buf.write("\u0092J\2\u02b9\u02bb\5d\63\2\u02ba\u02b8\3\2\2\2\u02ba")
        buf.write("\u02b9\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd\7\66\2")
        buf.write("\2\u02bd\u02be\5\u009cO\2\u02be\u02c5\3\2\2\2\u02bf\u02c2")
        buf.write("\5\u0092J\2\u02c0\u02c2\5d\63\2\u02c1\u02bf\3\2\2\2\u02c1")
        buf.write("\u02c0\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3\u02c5\3\2\2\2")
        buf.write("\u02c4\u02ba\3\2\2\2\u02c4\u02c1\3\2\2\2\u02c4\u02c3\3")
        buf.write("\2\2\2\u02c5\u009d\3\2\2\2\u02c6\u02c7\7\f\2\2\u02c7\u02c8")
        buf.write("\7\61\2\2\u02c8\u02c9\5\u00a0Q\2\u02c9\u02ca\7\66\2\2")
        buf.write("\u02ca\u02cb\7=\2\2\u02cb\u02cc\7\62\2\2\u02cc\u009f\3")
        buf.write("\2\2\2\u02cd\u02d3\5\u009eP\2\u02ce\u02d3\7\16\2\2\u02cf")
        buf.write("\u02d3\7\17\2\2\u02d0\u02d3\7\20\2\2\u02d1\u02d3\7\21")
        buf.write("\2\2\u02d2\u02cd\3\2\2\2\u02d2\u02ce\3\2\2\2\u02d2\u02cf")
        buf.write("\3\2\2\2\u02d2\u02d0\3\2\2\2\u02d2\u02d1\3\2\2\2\u02d3")
        buf.write("\u00a1\3\2\2\2\u02d4\u02d5\t\t\2\2\u02d5\u00a3\3\2\2\2")
        buf.write("\u02d6\u02da\5\u00a2R\2\u02d7\u02da\5\u009eP\2\u02d8\u02da")
        buf.write("\79\2\2\u02d9\u02d6\3\2\2\2\u02d9\u02d7\3\2\2\2\u02d9")
        buf.write("\u02d8\3\2\2\2\u02da\u00a5\3\2\2\2;\u00ad\u00b7\u00cd")
        buf.write("\u00d5\u00dc\u00e6\u00f2\u00f7\u00ff\u0106\u0110\u011c")
        buf.write("\u0130\u0135\u013c\u0145\u0155\u0159\u0166\u016c\u017a")
        buf.write("\u019f\u01ac\u01c5\u01cc\u01d2\u01dd\u01e4\u01eb\u01f5")
        buf.write("\u0200\u020b\u0211\u0216\u021f\u0229\u022f\u0238\u023e")
        buf.write("\u0250\u0257\u025f\u0265\u026f\u0275\u027f\u0287\u0294")
        buf.write("\u029c\u02a4\u02af\u02b6\u02ba\u02c1\u02c4\u02d2\u02d9")
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
    RULE_variable_declaration = 7
    RULE_no_value_assign_declare_list = 8
    RULE_no_value_assign_declare = 9
    RULE_declare_initiate_list = 10
    RULE_type_and_assign = 11
    RULE_both_variable_declaration = 12
    RULE_both_no_value_assign_declare_list = 13
    RULE_both_no_value_assign_declare = 14
    RULE_both_declare_initiate_list = 15
    RULE_both_type_and_assign = 16
    RULE_function_declaration = 17
    RULE_call_func_statement = 18
    RULE_call_func = 19
    RULE_call_func_header = 20
    RULE_call_func_attr_list = 21
    RULE_call_func_attr = 22
    RULE_call_func_end = 23
    RULE_assignment_statements = 24
    RULE_lhs = 25
    RULE_if_statements = 26
    RULE_elseif_list_statements = 27
    RULE_elseif_statement = 28
    RULE_else_statement = 29
    RULE_by_expr = 30
    RULE_forin_statements = 31
    RULE_instance_attr_access = 32
    RULE_instance_method_access = 33
    RULE_static_attr_access = 34
    RULE_static_method_access = 35
    RULE_method_invocation = 36
    RULE_method_invocation_statement = 37
    RULE_break_statements = 38
    RULE_continue_statements = 39
    RULE_return_expr = 40
    RULE_return_statements = 41
    RULE_block_class_statements = 42
    RULE_block_statements = 43
    RULE_block_statements_in_main = 44
    RULE_statements_class = 45
    RULE_statements = 46
    RULE_statement_class = 47
    RULE_statement = 48
    RULE_expr = 49
    RULE_expr1 = 50
    RULE_expr2 = 51
    RULE_expr3 = 52
    RULE_expr4 = 53
    RULE_expr5 = 54
    RULE_expr6 = 55
    RULE_expr7 = 56
    RULE_expr8 = 57
    RULE_expr9 = 58
    RULE_expr10 = 59
    RULE_expr11 = 60
    RULE_expr12 = 61
    RULE_index_operators = 62
    RULE_index_expr = 63
    RULE_index = 64
    RULE_instance_accesses = 65
    RULE_instance_access = 66
    RULE_static_accesses = 67
    RULE_static_access = 68
    RULE_list_expr = 69
    RULE_array_lit = 70
    RULE_array_val = 71
    RULE_literal = 72
    RULE_list_parameters = 73
    RULE_param = 74
    RULE_identifier_list = 75
    RULE_variable_in_func_identifier_list = 76
    RULE_value_list = 77
    RULE_array_type = 78
    RULE_array_element_type = 79
    RULE_primitive_type = 80
    RULE_variable_type = 81

    ruleNames =  [ "program", "class_declarations", "class_declaration", 
                   "class_inheritance", "constructor_dclr", "destructor_dclr", 
                   "method_declaration", "variable_declaration", "no_value_assign_declare_list", 
                   "no_value_assign_declare", "declare_initiate_list", "type_and_assign", 
                   "both_variable_declaration", "both_no_value_assign_declare_list", 
                   "both_no_value_assign_declare", "both_declare_initiate_list", 
                   "both_type_and_assign", "function_declaration", "call_func_statement", 
                   "call_func", "call_func_header", "call_func_attr_list", 
                   "call_func_attr", "call_func_end", "assignment_statements", 
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
            self.state = 164
            self.class_declarations()
            self.state = 165
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
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.class_declaration()
                self.state = 168
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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
            self.state = 173
            self.match(D96Parser.CLASS)
            self.state = 174
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 175
            self.class_inheritance()
            self.state = 176
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
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(D96Parser.COLON)
                self.state = 179
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
            self.state = 183
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 184
            self.match(D96Parser.LB)
            self.state = 185
            self.list_parameters()
            self.state = 186
            self.match(D96Parser.RB)
            self.state = 187
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
            self.state = 189
            self.match(D96Parser.DESTRUCTOR)
            self.state = 190
            self.match(D96Parser.LB)
            self.state = 191
            self.match(D96Parser.RB)
            self.state = 192
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
            self.state = 194
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 195
            self.match(D96Parser.LB)
            self.state = 196
            self.list_parameters()
            self.state = 197
            self.match(D96Parser.RB)
            self.state = 198
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


        def no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.No_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_declaration




    def variable_declaration(self):

        localctx = D96Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 203
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 201
                self.declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 202
                self.no_value_assign_declare_list()
                pass


            self.state = 205
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_value_assign_declare_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def no_value_assign_declare(self):
            return self.getTypedRuleContext(D96Parser.No_value_assign_declareContext,0)


        def no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.No_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_no_value_assign_declare_list




    def no_value_assign_declare_list(self):

        localctx = D96Parser.No_value_assign_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_no_value_assign_declare_list)
        try:
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 207
                self.no_value_assign_declare()
                self.state = 208
                self.no_value_assign_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.no_value_assign_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_value_assign_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def COMMA(self):
            return self.getToken(D96Parser.COMMA, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_no_value_assign_declare




    def no_value_assign_declare(self):

        localctx = D96Parser.No_value_assign_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_no_value_assign_declare)
        try:
            self.state = 218
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 214
                self.match(D96Parser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 216
                self.match(D96Parser.COLON)
                self.state = 217
                self.variable_type()
                pass


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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def variable_in_func_identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Variable_in_func_identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_declare_initiate_list




    def declare_initiate_list(self):

        localctx = D96Parser.Declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declare_initiate_list)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 221
                self.type_and_assign()
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


    class Type_and_assignContext(ParserRuleContext):

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

        def type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


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
        self.enterRule(localctx, 22, self.RULE_type_and_assign)
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
                self.type_and_assign()
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


    class Both_variable_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def both_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Both_declare_initiate_listContext,0)


        def both_no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.Both_no_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_both_variable_declaration




    def both_variable_declaration(self):

        localctx = D96Parser.Both_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_both_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 243
                self.both_declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 244
                self.both_no_value_assign_declare_list()
                pass


            self.state = 247
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Both_no_value_assign_declare_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def both_no_value_assign_declare(self):
            return self.getTypedRuleContext(D96Parser.Both_no_value_assign_declareContext,0)


        def both_no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.Both_no_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_both_no_value_assign_declare_list




    def both_no_value_assign_declare_list(self):

        localctx = D96Parser.Both_no_value_assign_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_both_no_value_assign_declare_list)
        try:
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 249
                self.both_no_value_assign_declare()
                self.state = 250
                self.both_no_value_assign_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 252
                self.both_no_value_assign_declare()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Both_no_value_assign_declareContext(ParserRuleContext):

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
            return D96Parser.RULE_both_no_value_assign_declare




    def both_no_value_assign_declare(self):

        localctx = D96Parser.Both_no_value_assign_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_both_no_value_assign_declare)
        self._la = 0 # Token type
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 256
                self.match(D96Parser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 258
                self.match(D96Parser.COLON)
                self.state = 259
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Both_declare_initiate_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def both_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Both_type_and_assignContext,0)


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
            return D96Parser.RULE_both_declare_initiate_list




    def both_declare_initiate_list(self):

        localctx = D96Parser.Both_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 270
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 263
                self.both_type_and_assign()
                self.state = 264
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.variable_in_func_identifier_list()
                self.state = 267
                self.match(D96Parser.COLON)
                self.state = 268
                self.variable_type()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Both_type_and_assignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.COMMA)
            else:
                return self.getToken(D96Parser.COMMA, i)

        def both_type_and_assign(self):
            return self.getTypedRuleContext(D96Parser.Both_type_and_assignContext,0)


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
            return D96Parser.RULE_both_type_and_assign




    def both_type_and_assign(self):

        localctx = D96Parser.Both_type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_both_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(D96Parser.COMMA)
                self.state = 273
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 274
                self.both_type_and_assign()
                self.state = 275
                self.expr()
                self.state = 276
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.match(D96Parser.COLON)
                self.state = 279
                self.variable_type()
                self.state = 280
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
        self.enterRule(localctx, 34, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 285
            self.match(D96Parser.LB)
            self.state = 286
            self.list_parameters()
            self.state = 287
            self.match(D96Parser.RB)
            self.state = 288
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
        self.enterRule(localctx, 36, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.call_func_header()
            self.state = 291
            self.call_func_attr_list()
            self.state = 292
            self.call_func_end()
            self.state = 293
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
        self.enterRule(localctx, 38, self.RULE_call_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.call_func_header()
            self.state = 296
            self.call_func_attr_list()
            self.state = 297
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
        self.enterRule(localctx, 40, self.RULE_call_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 300
                self.index_operators(0)
                pass
            elif token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOUBLECOLONOP]:
                self.state = 304
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 305
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
        self.enterRule(localctx, 42, self.RULE_call_func_attr_list)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.call_func_attr()
                self.state = 310
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 312
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
        self.enterRule(localctx, 44, self.RULE_call_func_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(D96Parser.DOT)
            self.state = 323
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 317
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 318
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 319
                self.match(D96Parser.LB)
                self.state = 320
                self.value_list()
                self.state = 321
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
        self.enterRule(localctx, 46, self.RULE_call_func_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 325
            self.match(D96Parser.DOT)
            self.state = 326
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 327
            self.match(D96Parser.LB)
            self.state = 328
            self.value_list()
            self.state = 329
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
        self.enterRule(localctx, 48, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.lhs()
            self.state = 332
            self.match(D96Parser.ASSIGNOP)
            self.state = 333
            self.expr()
            self.state = 334
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
        self.enterRule(localctx, 50, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 336
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 337
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.state = 338
                self.static_attr_access()
                pass


            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 341
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
        self.enterRule(localctx, 52, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(D96Parser.IF)
            self.state = 346
            self.match(D96Parser.LB)
            self.state = 347
            self.expr()
            self.state = 348
            self.match(D96Parser.RB)
            self.state = 349
            self.block_statements()
            self.state = 356
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 350
                self.elseif_list_statements()
                self.state = 351
                self.else_statement()
                pass

            elif la_ == 2:
                self.state = 353
                self.elseif_list_statements()
                pass

            elif la_ == 3:
                self.state = 354
                self.else_statement()
                pass

            elif la_ == 4:
                pass


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
        self.enterRule(localctx, 54, self.RULE_elseif_list_statements)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.elseif_statement()
                self.state = 359
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
        self.enterRule(localctx, 56, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(D96Parser.ELSEIF)
            self.state = 365
            self.match(D96Parser.LB)
            self.state = 366
            self.expr()
            self.state = 367
            self.match(D96Parser.RB)
            self.state = 368
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
        self.enterRule(localctx, 58, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(D96Parser.ELSE)
            self.state = 371
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
        self.enterRule(localctx, 60, self.RULE_by_expr)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(D96Parser.BY)
                self.state = 374
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
        self.enterRule(localctx, 62, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.FOREACH)
            self.state = 379
            self.match(D96Parser.LB)
            self.state = 380
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 381
            self.match(D96Parser.IN)
            self.state = 382
            self.expr()
            self.state = 383
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 384
            self.expr()
            self.state = 385
            self.by_expr()
            self.state = 386
            self.match(D96Parser.RB)
            self.state = 387
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
        self.enterRule(localctx, 64, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self.expr()
            self.state = 390
            self.match(D96Parser.DOT)
            self.state = 391
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
        self.enterRule(localctx, 66, self.RULE_instance_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expr()
            self.state = 394
            self.match(D96Parser.DOT)
            self.state = 395
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 396
            self.match(D96Parser.LB)
            self.state = 397
            self.list_expr()
            self.state = 398
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
        self.enterRule(localctx, 68, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 401
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 402
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
        self.enterRule(localctx, 70, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 405
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 406
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 407
            self.match(D96Parser.LB)
            self.state = 408
            self.list_expr()
            self.state = 409
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
        self.enterRule(localctx, 72, self.RULE_method_invocation)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
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
        self.enterRule(localctx, 74, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.method_invocation()
            self.state = 416
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
        self.enterRule(localctx, 76, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(D96Parser.BREAK)
            self.state = 419
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
        self.enterRule(localctx, 78, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(D96Parser.CONTINUE)
            self.state = 422
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
        self.enterRule(localctx, 80, self.RULE_return_expr)
        try:
            self.state = 426
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
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
        self.enterRule(localctx, 82, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(D96Parser.RETURN)
            self.state = 429
            self.return_expr()
            self.state = 430
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
        self.enterRule(localctx, 84, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(D96Parser.LCB)
            self.state = 433
            self.statements_class()
            self.state = 434
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
        self.enterRule(localctx, 86, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.match(D96Parser.LCB)
            self.state = 437
            self.statements()
            self.state = 438
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
        self.enterRule(localctx, 88, self.RULE_block_statements_in_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(D96Parser.LCB)
            self.state = 441
            self.statements()
            self.state = 442
            self.match(D96Parser.RETURN)
            self.state = 443
            self.match(D96Parser.SEMICOLON)
            self.state = 444
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
        self.enterRule(localctx, 90, self.RULE_statements_class)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.statement_class()
                self.state = 447
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 449
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
        self.enterRule(localctx, 92, self.RULE_statements)
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.statement()
                self.state = 454
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 456
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

        def both_variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Both_variable_declarationContext,0)


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
        self.enterRule(localctx, 94, self.RULE_statement_class)
        try:
            self.state = 464
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.both_variable_declaration()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.function_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 462
                self.constructor_dclr()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 463
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

        def variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_declarationContext,0)


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
        self.enterRule(localctx, 96, self.RULE_statement)
        try:
            self.state = 475
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 468
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 469
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 470
                self.call_func_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 471
                self.method_invocation_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 472
                self.break_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 473
                self.continue_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 474
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
        self.enterRule(localctx, 98, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 482
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
                self.expr1()
                self.state = 478
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 479
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
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
        self.enterRule(localctx, 100, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 489
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 484
                self.expr2(0)
                self.state = 485
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 486
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 488
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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 492
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 499
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 494
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 495
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 496
                    self.expr3(0) 
                self.state = 501
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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 510
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 505
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 506
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 507
                    self.expr4(0) 
                self.state = 512
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 521
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 516
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 517
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 518
                    self.expr5() 
                self.state = 523
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
        self.enterRule(localctx, 108, self.RULE_expr5)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self.match(D96Parser.NOTOP)
                self.state = 525
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
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
        self.enterRule(localctx, 110, self.RULE_expr6)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 529
                self.match(D96Parser.MINUSOP)
                self.state = 530
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 541
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 537
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 538
                    self.index_operators(0) 
                self.state = 543
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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 545
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 551
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 547
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 548
                    self.instance_accesses() 
                self.state = 553
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
        self.enterRule(localctx, 116, self.RULE_expr9)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 555
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 556
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
        self.enterRule(localctx, 118, self.RULE_expr10)
        try:
            self.state = 566
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(D96Parser.NEW)
                self.state = 560
                self.expr()
                self.state = 561
                self.match(D96Parser.LB)
                self.state = 562
                self.list_expr()
                self.state = 563
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
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
        self.enterRule(localctx, 120, self.RULE_expr11)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 568
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 570
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 571
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
        self.enterRule(localctx, 122, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            self.match(D96Parser.LB)
            self.state = 575
            self.expr()
            self.state = 576
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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(D96Parser.LSB)
            self.state = 580
            self.expr()
            self.state = 581
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 590
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 583
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 584
                    self.match(D96Parser.LSB)
                    self.state = 585
                    self.expr()
                    self.state = 586
                    self.match(D96Parser.RSB) 
                self.state = 592
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
        self.enterRule(localctx, 126, self.RULE_index_expr)
        try:
            self.state = 597
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 593
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 594
                self.index()
                self.state = 595
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
        self.enterRule(localctx, 128, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 605
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 599
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 600
                self.expr()
                self.state = 601
                self.instance_attr_access()
                self.state = 602
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
        self.enterRule(localctx, 130, self.RULE_instance_accesses)
        try:
            self.state = 611
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 607
                self.instance_access()
                self.state = 608
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 610
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
        self.enterRule(localctx, 132, self.RULE_instance_access)
        try:
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.match(D96Parser.DOT)
                self.state = 614
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.match(D96Parser.DOT)
                self.state = 616
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 617
                self.match(D96Parser.LB)
                self.state = 618
                self.list_expr()
                self.state = 619
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
        self.enterRule(localctx, 134, self.RULE_static_accesses)
        try:
            self.state = 627
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 623
                self.static_access()
                self.state = 624
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 626
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
        self.enterRule(localctx, 136, self.RULE_static_access)
        try:
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 629
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 630
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 631
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 632
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 633
                self.match(D96Parser.LB)
                self.state = 634
                self.list_expr()
                self.state = 635
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
        self.enterRule(localctx, 138, self.RULE_list_expr)
        try:
            self.state = 645
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 639
                self.expr()
                self.state = 640
                self.match(D96Parser.COMMA)
                self.state = 641
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 643
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
        self.enterRule(localctx, 140, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 647
            self.match(D96Parser.ARRAY)
            self.state = 648
            self.match(D96Parser.LB)
            self.state = 649
            self.array_val()
            self.state = 650
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
        self.enterRule(localctx, 142, self.RULE_array_val)
        try:
            self.state = 658
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.expr()
                self.state = 653
                self.match(D96Parser.COMMA)
                self.state = 654
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
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
        self.enterRule(localctx, 144, self.RULE_literal)
        try:
            self.state = 666
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 662
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 663
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 664
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 665
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
        self.enterRule(localctx, 146, self.RULE_list_parameters)
        try:
            self.state = 674
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 668
                self.param()
                self.state = 669
                self.match(D96Parser.SEMICOLON)
                self.state = 670
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 672
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
        self.enterRule(localctx, 148, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.identifier_list()
            self.state = 677
            self.match(D96Parser.COLON)
            self.state = 678
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
        self.enterRule(localctx, 150, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 685
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 681
                self.match(D96Parser.COMMA)
                self.state = 682
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 683
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
        self.enterRule(localctx, 152, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 692
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 687
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 688
                self.match(D96Parser.COMMA)
                self.state = 689
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 690
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
        self.enterRule(localctx, 154, self.RULE_value_list)
        try:
            self.state = 706
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 696
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 694
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 695
                    self.expr()
                    pass


                self.state = 698
                self.match(D96Parser.COMMA)
                self.state = 699
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 703
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 701
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 702
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
        self.enterRule(localctx, 156, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 708
            self.match(D96Parser.ARRAY)
            self.state = 709
            self.match(D96Parser.LSB)
            self.state = 710
            self.array_element_type()
            self.state = 711
            self.match(D96Parser.COMMA)
            self.state = 712
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 713
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
        self.enterRule(localctx, 158, self.RULE_array_element_type)
        try:
            self.state = 720
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 715
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 716
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 717
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 718
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 719
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
        self.enterRule(localctx, 160, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 722
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
        self.enterRule(localctx, 162, self.RULE_variable_type)
        try:
            self.state = 727
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 725
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 726
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
        self._predicates[51] = self.expr2_sempred
        self._predicates[52] = self.expr3_sempred
        self._predicates[53] = self.expr4_sempred
        self._predicates[56] = self.expr7_sempred
        self._predicates[57] = self.expr8_sempred
        self._predicates[62] = self.index_operators_sempred
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
         




