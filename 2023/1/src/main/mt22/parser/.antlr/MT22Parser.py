# Generated from d:\Github\Principle-of-Programming-Languages\2023\1\src\main\mt22\parser\MT22.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u0227\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\u0083")
        buf.write("\n\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u008e\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0096\n\4\3\4\3\4\3\5\3\5")
        buf.write("\5\5\u009c\n\5\3\5\3\5\5\5\u00a0\n\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6\u00ac\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\5\t\u00c2\n\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\5\13\u00cf\n\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00e0\n\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\5\16\u00ec")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u00f8\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u0104\n\22\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\23\3\24\3\24\3\24\3\24\5\24\u0110\n\24\3\24\3\24\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\5\27\u0123\n\27\3\27\3\27\3\30\3")
        buf.write("\30\3\30\5\30\u012a\n\30\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0133\n\31\3\31\3\31\3\32\3\32\3\32\5\32\u013a")
        buf.write("\n\32\3\32\5\32\u013d\n\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u014b\n\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\5\34\u0153\n\34\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3 \3 \5 \u0165\n \3!\3!\3!\3!\3\"\3\"\3\"\3#\3#")
        buf.write("\3#\3#\5#\u0172\n#\3$\3$\3$\3$\5$\u0178\n$\3%\3%\3%\3")
        buf.write("%\3&\3&\3&\3&\3&\5&\u0183\n&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0192\n\'\3(\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3)\5)\u019d\n)\3*\3*\3*\5*\u01a2\n*\3+\3+\5")
        buf.write("+\u01a6\n+\3,\3,\3,\3,\3,\5,\u01ad\n,\3-\3-\3-\3-\3-\5")
        buf.write("-\u01b4\n-\3.\3.\3.\3.\3.\5.\u01bb\n.\3/\3/\3/\3/\3/\3")
        buf.write("/\7/\u01c3\n/\f/\16/\u01c6\13/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\7\60\u01ce\n\60\f\60\16\60\u01d1\13\60\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u01d9\n\61\f\61\16\61\u01dc")
        buf.write("\13\61\3\62\3\62\3\62\5\62\u01e1\n\62\3\63\3\63\3\63\5")
        buf.write("\63\u01e6\n\63\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\7\64\u01f0\n\64\f\64\16\64\u01f3\13\64\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\65\5\65\u01fb\n\65\3\66\3\66\3\66\5\66\u0200")
        buf.write("\n\66\3\67\3\67\3\67\3\67\38\38\38\38\38\39\39\39\39\3")
        buf.write("9\59\u0210\n9\3:\3:\3:\5:\u0215\n:\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3<\3<\3=\3=\3=\3=\3=\5=\u0225\n=\3=\2\6\\^`f>\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvx\2\7\5\2)*,-/\60\3\2")
        buf.write("\'(\3\2!\"\3\2#%\3\2\34\37\2\u0235\2z\3\2\2\2\4}\3\2\2")
        buf.write("\2\6\u0088\3\2\2\2\b\u009b\3\2\2\2\n\u00ab\3\2\2\2\f\u00ad")
        buf.write("\3\2\2\2\16\u00b2\3\2\2\2\20\u00c1\3\2\2\2\22\u00c3\3")
        buf.write("\2\2\2\24\u00ce\3\2\2\2\26\u00df\3\2\2\2\30\u00e3\3\2")
        buf.write("\2\2\32\u00e7\3\2\2\2\34\u00ef\3\2\2\2\36\u00f3\3\2\2")
        buf.write("\2 \u00fb\3\2\2\2\"\u00ff\3\2\2\2$\u0107\3\2\2\2&\u010b")
        buf.write("\3\2\2\2(\u0113\3\2\2\2*\u0118\3\2\2\2,\u011c\3\2\2\2")
        buf.write(".\u0129\3\2\2\2\60\u012b\3\2\2\2\62\u013c\3\2\2\2\64\u013e")
        buf.write("\3\2\2\2\66\u014c\3\2\2\28\u0154\3\2\2\2:\u015c\3\2\2")
        buf.write("\2<\u015f\3\2\2\2>\u0164\3\2\2\2@\u0166\3\2\2\2B\u016a")
        buf.write("\3\2\2\2D\u0171\3\2\2\2F\u0177\3\2\2\2H\u0179\3\2\2\2")
        buf.write("J\u0182\3\2\2\2L\u0191\3\2\2\2N\u0193\3\2\2\2P\u019c\3")
        buf.write("\2\2\2R\u01a1\3\2\2\2T\u01a5\3\2\2\2V\u01ac\3\2\2\2X\u01b3")
        buf.write("\3\2\2\2Z\u01ba\3\2\2\2\\\u01bc\3\2\2\2^\u01c7\3\2\2\2")
        buf.write("`\u01d2\3\2\2\2b\u01e0\3\2\2\2d\u01e5\3\2\2\2f\u01e7\3")
        buf.write("\2\2\2h\u01fa\3\2\2\2j\u01ff\3\2\2\2l\u0201\3\2\2\2n\u0205")
        buf.write("\3\2\2\2p\u020f\3\2\2\2r\u0214\3\2\2\2t\u0216\3\2\2\2")
        buf.write("v\u021d\3\2\2\2x\u0224\3\2\2\2z{\5D#\2{|\7\2\2\3|\3\3")
        buf.write("\2\2\2}~\7\3\2\2~\177\79\2\2\177\u0082\7\4\2\2\u0080\u0083")
        buf.write("\5r:\2\u0081\u0083\7 \2\2\u0082\u0080\3\2\2\2\u0082\u0081")
        buf.write("\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0085\7\61\2\2\u0085")
        buf.write("\u0086\7\62\2\2\u0086\u0087\5H%\2\u0087\5\3\2\2\2\u0088")
        buf.write("\u0089\7;\2\2\u0089\u008a\79\2\2\u008a\u008d\7\4\2\2\u008b")
        buf.write("\u008e\5r:\2\u008c\u008e\7 \2\2\u008d\u008b\3\2\2\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u0090\7\61\2")
        buf.write("\2\u0090\u0091\5\n\6\2\u0091\u0095\7\62\2\2\u0092\u0093")
        buf.write("\7\32\2\2\u0093\u0096\7;\2\2\u0094\u0096\3\2\2\2\u0095")
        buf.write("\u0092\3\2\2\2\u0095\u0094\3\2\2\2\u0096\u0097\3\2\2\2")
        buf.write("\u0097\u0098\5H%\2\u0098\7\3\2\2\2\u0099\u009c\7\32\2")
        buf.write("\2\u009a\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009b\u009a")
        buf.write("\3\2\2\2\u009c\u009f\3\2\2\2\u009d\u00a0\7\27\2\2\u009e")
        buf.write("\u00a0\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u009e\3\2\2\2")
        buf.write("\u00a0\u00a1\3\2\2\2\u00a1\u00a2\7;\2\2\u00a2\u00a3\7")
        buf.write("9\2\2\u00a3\u00a4\5r:\2\u00a4\t\3\2\2\2\u00a5\u00a6\5")
        buf.write("\b\5\2\u00a6\u00a7\78\2\2\u00a7\u00a8\5\n\6\2\u00a8\u00ac")
        buf.write("\3\2\2\2\u00a9\u00ac\5\b\5\2\u00aa\u00ac\3\2\2\2\u00ab")
        buf.write("\u00a5\3\2\2\2\u00ab\u00a9\3\2\2\2\u00ab\u00aa\3\2\2\2")
        buf.write("\u00ac\13\3\2\2\2\u00ad\u00ae\5x=\2\u00ae\u00af\79\2\2")
        buf.write("\u00af\u00b0\5r:\2\u00b0\u00b1\7:\2\2\u00b1\r\3\2\2\2")
        buf.write("\u00b2\u00b3\7;\2\2\u00b3\u00b4\5\20\t\2\u00b4\u00b5\5")
        buf.write("X-\2\u00b5\u00b6\7:\2\2\u00b6\17\3\2\2\2\u00b7\u00b8\7")
        buf.write("8\2\2\u00b8\u00b9\7;\2\2\u00b9\u00ba\5\20\t\2\u00ba\u00bb")
        buf.write("\5X-\2\u00bb\u00bc\78\2\2\u00bc\u00c2\3\2\2\2\u00bd\u00be")
        buf.write("\79\2\2\u00be\u00bf\5r:\2\u00bf\u00c0\7.\2\2\u00c0\u00c2")
        buf.write("\3\2\2\2\u00c1\u00b7\3\2\2\2\u00c1\u00bd\3\2\2\2\u00c2")
        buf.write("\21\3\2\2\2\u00c3\u00c4\5\24\13\2\u00c4\u00c5\7.\2\2\u00c5")
        buf.write("\u00c6\5X-\2\u00c6\u00c7\7:\2\2\u00c7\23\3\2\2\2\u00c8")
        buf.write("\u00cf\7;\2\2\u00c9\u00ca\7;\2\2\u00ca\u00cb\7\63\2\2")
        buf.write("\u00cb\u00cc\5V,\2\u00cc\u00cd\7\64\2\2\u00cd\u00cf\3")
        buf.write("\2\2\2\u00ce\u00c8\3\2\2\2\u00ce\u00c9\3\2\2\2\u00cf\25")
        buf.write("\3\2\2\2\u00d0\u00d1\7;\2\2\u00d1\u00d2\7\61\2\2\u00d2")
        buf.write("\u00d3\5T+\2\u00d3\u00d4\7\62\2\2\u00d4\u00e0\3\2\2\2")
        buf.write("\u00d5\u00e0\5\30\r\2\u00d6\u00e0\5\32\16\2\u00d7\u00e0")
        buf.write("\5\34\17\2\u00d8\u00e0\5\36\20\2\u00d9\u00e0\5 \21\2\u00da")
        buf.write("\u00e0\5\"\22\2\u00db\u00e0\5$\23\2\u00dc\u00e0\5&\24")
        buf.write("\2\u00dd\u00e0\5(\25\2\u00de\u00e0\5*\26\2\u00df\u00d0")
        buf.write("\3\2\2\2\u00df\u00d5\3\2\2\2\u00df\u00d6\3\2\2\2\u00df")
        buf.write("\u00d7\3\2\2\2\u00df\u00d8\3\2\2\2\u00df\u00d9\3\2\2\2")
        buf.write("\u00df\u00da\3\2\2\2\u00df\u00db\3\2\2\2\u00df\u00dc\3")
        buf.write("\2\2\2\u00df\u00dd\3\2\2\2\u00df\u00de\3\2\2\2\u00e0\u00e1")
        buf.write("\3\2\2\2\u00e1\u00e2\7:\2\2\u00e2\27\3\2\2\2\u00e3\u00e4")
        buf.write("\7\5\2\2\u00e4\u00e5\7\61\2\2\u00e5\u00e6\7\62\2\2\u00e6")
        buf.write("\31\3\2\2\2\u00e7\u00e8\7\6\2\2\u00e8\u00eb\7\61\2\2\u00e9")
        buf.write("\u00ec\5X-\2\u00ea\u00ec\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb")
        buf.write("\u00ea\3\2\2\2\u00ec\u00ed\3\2\2\2\u00ed\u00ee\7\62\2")
        buf.write("\2\u00ee\33\3\2\2\2\u00ef\u00f0\7\7\2\2\u00f0\u00f1\7")
        buf.write("\61\2\2\u00f1\u00f2\7\62\2\2\u00f2\35\3\2\2\2\u00f3\u00f4")
        buf.write("\7\b\2\2\u00f4\u00f7\7\61\2\2\u00f5\u00f8\5X-\2\u00f6")
        buf.write("\u00f8\3\2\2\2\u00f7\u00f5\3\2\2\2\u00f7\u00f6\3\2\2\2")
        buf.write("\u00f8\u00f9\3\2\2\2\u00f9\u00fa\7\62\2\2\u00fa\37\3\2")
        buf.write("\2\2\u00fb\u00fc\7\t\2\2\u00fc\u00fd\7\61\2\2\u00fd\u00fe")
        buf.write("\7\62\2\2\u00fe!\3\2\2\2\u00ff\u0100\7\n\2\2\u0100\u0103")
        buf.write("\7\61\2\2\u0101\u0104\5X-\2\u0102\u0104\3\2\2\2\u0103")
        buf.write("\u0101\3\2\2\2\u0103\u0102\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0106\7\62\2\2\u0106#\3\2\2\2\u0107\u0108\7\13")
        buf.write("\2\2\u0108\u0109\7\61\2\2\u0109\u010a\7\62\2\2\u010a%")
        buf.write("\3\2\2\2\u010b\u010c\7\f\2\2\u010c\u010f\7\61\2\2\u010d")
        buf.write("\u0110\5X-\2\u010e\u0110\3\2\2\2\u010f\u010d\3\2\2\2\u010f")
        buf.write("\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\7\62\2")
        buf.write("\2\u0112\'\3\2\2\2\u0113\u0114\7\r\2\2\u0114\u0115\7\61")
        buf.write("\2\2\u0115\u0116\5T+\2\u0116\u0117\7\62\2\2\u0117)\3\2")
        buf.write("\2\2\u0118\u0119\7\16\2\2\u0119\u011a\7\61\2\2\u011a\u011b")
        buf.write("\7\62\2\2\u011b+\3\2\2\2\u011c\u011d\7\24\2\2\u011d\u011e")
        buf.write("\7\61\2\2\u011e\u011f\5X-\2\u011f\u0122\7\62\2\2\u0120")
        buf.write("\u0123\5H%\2\u0121\u0123\5L\'\2\u0122\u0120\3\2\2\2\u0122")
        buf.write("\u0121\3\2\2\2\u0123\u0124\3\2\2\2\u0124\u0125\5.\30\2")
        buf.write("\u0125-\3\2\2\2\u0126\u012a\5\60\31\2\u0127\u012a\5\62")
        buf.write("\32\2\u0128\u012a\3\2\2\2\u0129\u0126\3\2\2\2\u0129\u0127")
        buf.write("\3\2\2\2\u0129\u0128\3\2\2\2\u012a/\3\2\2\2\u012b\u012c")
        buf.write("\7\22\2\2\u012c\u012d\7\24\2\2\u012d\u012e\7\61\2\2\u012e")
        buf.write("\u012f\5X-\2\u012f\u0132\7\62\2\2\u0130\u0133\5H%\2\u0131")
        buf.write("\u0133\5L\'\2\u0132\u0130\3\2\2\2\u0132\u0131\3\2\2\2")
        buf.write("\u0133\u0134\3\2\2\2\u0134\u0135\5.\30\2\u0135\61\3\2")
        buf.write("\2\2\u0136\u0139\7\22\2\2\u0137\u013a\5H%\2\u0138\u013a")
        buf.write("\5L\'\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2\u013a")
        buf.write("\u013d\3\2\2\2\u013b\u013d\3\2\2\2\u013c\u0136\3\2\2\2")
        buf.write("\u013c\u013b\3\2\2\2\u013d\63\3\2\2\2\u013e\u013f\7\23")
        buf.write("\2\2\u013f\u0140\7\61\2\2\u0140\u0141\7;\2\2\u0141\u0142")
        buf.write("\7.\2\2\u0142\u0143\5X-\2\u0143\u0144\78\2\2\u0144\u0145")
        buf.write("\5X-\2\u0145\u0146\78\2\2\u0146\u0147\5X-\2\u0147\u014a")
        buf.write("\7\62\2\2\u0148\u014b\5H%\2\u0149\u014b\5L\'\2\u014a\u0148")
        buf.write("\3\2\2\2\u014a\u0149\3\2\2\2\u014b\65\3\2\2\2\u014c\u014d")
        buf.write("\7\26\2\2\u014d\u014e\7\61\2\2\u014e\u014f\5X-\2\u014f")
        buf.write("\u0152\7\62\2\2\u0150\u0153\5H%\2\u0151\u0153\5L\'\2\u0152")
        buf.write("\u0150\3\2\2\2\u0152\u0151\3\2\2\2\u0153\67\3\2\2\2\u0154")
        buf.write("\u0155\7\21\2\2\u0155\u0156\5H%\2\u0156\u0157\7\26\2\2")
        buf.write("\u0157\u0158\7\61\2\2\u0158\u0159\5X-\2\u0159\u015a\7")
        buf.write("\62\2\2\u015a\u015b\7:\2\2\u015b9\3\2\2\2\u015c\u015d")
        buf.write("\7\20\2\2\u015d\u015e\7:\2\2\u015e;\3\2\2\2\u015f\u0160")
        buf.write("\7\30\2\2\u0160\u0161\7:\2\2\u0161=\3\2\2\2\u0162\u0165")
        buf.write("\5X-\2\u0163\u0165\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165?\3\2\2\2\u0166\u0167\7\25\2\2\u0167\u0168")
        buf.write("\5> \2\u0168\u0169\7:\2\2\u0169A\3\2\2\2\u016a\u016b\7")
        buf.write("\25\2\2\u016b\u016c\7:\2\2\u016cC\3\2\2\2\u016d\u016e")
        buf.write("\5F$\2\u016e\u016f\5D#\2\u016f\u0172\3\2\2\2\u0170\u0172")
        buf.write("\5F$\2\u0171\u016d\3\2\2\2\u0171\u0170\3\2\2\2\u0172E")
        buf.write("\3\2\2\2\u0173\u0178\5\f\7\2\u0174\u0178\5\16\b\2\u0175")
        buf.write("\u0178\5\6\4\2\u0176\u0178\5\4\3\2\u0177\u0173\3\2\2\2")
        buf.write("\u0177\u0174\3\2\2\2\u0177\u0175\3\2\2\2\u0177\u0176\3")
        buf.write("\2\2\2\u0178G\3\2\2\2\u0179\u017a\7\65\2\2\u017a\u017b")
        buf.write("\5J&\2\u017b\u017c\7\66\2\2\u017cI\3\2\2\2\u017d\u017e")
        buf.write("\5L\'\2\u017e\u017f\5J&\2\u017f\u0183\3\2\2\2\u0180\u0183")
        buf.write("\5L\'\2\u0181\u0183\3\2\2\2\u0182\u017d\3\2\2\2\u0182")
        buf.write("\u0180\3\2\2\2\u0182\u0181\3\2\2\2\u0183K\3\2\2\2\u0184")
        buf.write("\u0192\5\f\7\2\u0185\u0192\5\16\b\2\u0186\u0192\5\6\4")
        buf.write("\2\u0187\u0192\5\22\n\2\u0188\u0192\5,\27\2\u0189\u0192")
        buf.write("\5\64\33\2\u018a\u0192\5\66\34\2\u018b\u0192\58\35\2\u018c")
        buf.write("\u0192\5\26\f\2\u018d\u0192\5@!\2\u018e\u0192\5B\"\2\u018f")
        buf.write("\u0192\5R*\2\u0190\u0192\5H%\2\u0191\u0184\3\2\2\2\u0191")
        buf.write("\u0185\3\2\2\2\u0191\u0186\3\2\2\2\u0191\u0187\3\2\2\2")
        buf.write("\u0191\u0188\3\2\2\2\u0191\u0189\3\2\2\2\u0191\u018a\3")
        buf.write("\2\2\2\u0191\u018b\3\2\2\2\u0191\u018c\3\2\2\2\u0191\u018d")
        buf.write("\3\2\2\2\u0191\u018e\3\2\2\2\u0191\u018f\3\2\2\2\u0191")
        buf.write("\u0190\3\2\2\2\u0192M\3\2\2\2\u0193\u0194\7\65\2\2\u0194")
        buf.write("\u0195\5P)\2\u0195\u0196\7\66\2\2\u0196O\3\2\2\2\u0197")
        buf.write("\u0198\5R*\2\u0198\u0199\5P)\2\u0199\u019d\3\2\2\2\u019a")
        buf.write("\u019d\5R*\2\u019b\u019d\3\2\2\2\u019c\u0197\3\2\2\2\u019c")
        buf.write("\u019a\3\2\2\2\u019c\u019b\3\2\2\2\u019dQ\3\2\2\2\u019e")
        buf.write("\u01a2\5:\36\2\u019f\u01a2\5<\37\2\u01a0\u01a2\5N(\2\u01a1")
        buf.write("\u019e\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a0\3\2\2\2")
        buf.write("\u01a2S\3\2\2\2\u01a3\u01a6\5V,\2\u01a4\u01a6\3\2\2\2")
        buf.write("\u01a5\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6U\3\2\2")
        buf.write("\2\u01a7\u01a8\5X-\2\u01a8\u01a9\78\2\2\u01a9\u01aa\5")
        buf.write("T+\2\u01aa\u01ad\3\2\2\2\u01ab\u01ad\5X-\2\u01ac\u01a7")
        buf.write("\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adW\3\2\2\2\u01ae\u01af")
        buf.write("\5Z.\2\u01af\u01b0\7+\2\2\u01b0\u01b1\5Z.\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b4\5Z.\2\u01b3\u01ae\3\2\2\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b4Y\3\2\2\2\u01b5\u01b6\5\\/\2\u01b6\u01b7")
        buf.write("\t\2\2\2\u01b7\u01b8\5\\/\2\u01b8\u01bb\3\2\2\2\u01b9")
        buf.write("\u01bb\5\\/\2\u01ba\u01b5\3\2\2\2\u01ba\u01b9\3\2\2\2")
        buf.write("\u01bb[\3\2\2\2\u01bc\u01bd\b/\1\2\u01bd\u01be\5^\60\2")
        buf.write("\u01be\u01c4\3\2\2\2\u01bf\u01c0\f\4\2\2\u01c0\u01c1\t")
        buf.write("\3\2\2\u01c1\u01c3\5^\60\2\u01c2\u01bf\3\2\2\2\u01c3\u01c6")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("]\3\2\2\2\u01c6\u01c4\3\2\2\2\u01c7\u01c8\b\60\1\2\u01c8")
        buf.write("\u01c9\5`\61\2\u01c9\u01cf\3\2\2\2\u01ca\u01cb\f\4\2\2")
        buf.write("\u01cb\u01cc\t\4\2\2\u01cc\u01ce\5`\61\2\u01cd\u01ca\3")
        buf.write("\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2\u01cf\u01d0")
        buf.write("\3\2\2\2\u01d0_\3\2\2\2\u01d1\u01cf\3\2\2\2\u01d2\u01d3")
        buf.write("\b\61\1\2\u01d3\u01d4\5b\62\2\u01d4\u01da\3\2\2\2\u01d5")
        buf.write("\u01d6\f\4\2\2\u01d6\u01d7\t\5\2\2\u01d7\u01d9\5b\62\2")
        buf.write("\u01d8\u01d5\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da\u01d8\3")
        buf.write("\2\2\2\u01da\u01db\3\2\2\2\u01dba\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dd\u01de\7&\2\2\u01de\u01e1\5b\62\2\u01df")
        buf.write("\u01e1\5d\63\2\u01e0\u01dd\3\2\2\2\u01e0\u01df\3\2\2\2")
        buf.write("\u01e1c\3\2\2\2\u01e2\u01e3\7\"\2\2\u01e3\u01e6\5d\63")
        buf.write("\2\u01e4\u01e6\5f\64\2\u01e5\u01e2\3\2\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6e\3\2\2\2\u01e7\u01e8\b\64\1\2\u01e8\u01e9")
        buf.write("\5h\65\2\u01e9\u01f1\3\2\2\2\u01ea\u01eb\f\4\2\2\u01eb")
        buf.write("\u01ec\7\63\2\2\u01ec\u01ed\5V,\2\u01ed\u01ee\7\64\2\2")
        buf.write("\u01ee\u01f0\3\2\2\2\u01ef\u01ea\3\2\2\2\u01f0\u01f3\3")
        buf.write("\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2g")
        buf.write("\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f4\u01f5\7;\2\2\u01f5")
        buf.write("\u01f6\7\61\2\2\u01f6\u01f7\5T+\2\u01f7\u01f8\7\62\2\2")
        buf.write("\u01f8\u01fb\3\2\2\2\u01f9\u01fb\5j\66\2\u01fa\u01f4\3")
        buf.write("\2\2\2\u01fa\u01f9\3\2\2\2\u01fbi\3\2\2\2\u01fc\u0200")
        buf.write("\5p9\2\u01fd\u0200\7;\2\2\u01fe\u0200\5l\67\2\u01ff\u01fc")
        buf.write("\3\2\2\2\u01ff\u01fd\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("k\3\2\2\2\u0201\u0202\7\61\2\2\u0202\u0203\5X-\2\u0203")
        buf.write("\u0204\7\62\2\2\u0204m\3\2\2\2\u0205\u0206\7\33\2\2\u0206")
        buf.write("\u0207\7\63\2\2\u0207\u0208\5T+\2\u0208\u0209\7\64\2\2")
        buf.write("\u0209o\3\2\2\2\u020a\u0210\7>\2\2\u020b\u0210\7=\2\2")
        buf.write("\u020c\u0210\7<\2\2\u020d\u0210\7?\2\2\u020e\u0210\5n")
        buf.write("8\2\u020f\u020a\3\2\2\2\u020f\u020b\3\2\2\2\u020f\u020c")
        buf.write("\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("q\3\2\2\2\u0211\u0215\5v<\2\u0212\u0215\5t;\2\u0213\u0215")
        buf.write("\7\17\2\2\u0214\u0211\3\2\2\2\u0214\u0212\3\2\2\2\u0214")
        buf.write("\u0213\3\2\2\2\u0215s\3\2\2\2\u0216\u0217\7\33\2\2\u0217")
        buf.write("\u0218\7\63\2\2\u0218\u0219\5V,\2\u0219\u021a\7\64\2\2")
        buf.write("\u021a\u021b\7\31\2\2\u021b\u021c\5v<\2\u021cu\3\2\2\2")
        buf.write("\u021d\u021e\t\6\2\2\u021ew\3\2\2\2\u021f\u0220\7;\2\2")
        buf.write("\u0220\u0221\78\2\2\u0221\u0225\5x=\2\u0222\u0225\7;\2")
        buf.write("\2\u0223\u0225\3\2\2\2\u0224\u021f\3\2\2\2\u0224\u0222")
        buf.write("\3\2\2\2\u0224\u0223\3\2\2\2\u0225y\3\2\2\2,\u0082\u008d")
        buf.write("\u0095\u009b\u009f\u00ab\u00c1\u00ce\u00df\u00eb\u00f7")
        buf.write("\u0103\u010f\u0122\u0129\u0132\u0139\u013c\u014a\u0152")
        buf.write("\u0164\u0171\u0177\u0182\u0191\u019c\u01a1\u01a5\u01ac")
        buf.write("\u01b3\u01ba\u01c4\u01cf\u01da\u01e0\u01e5\u01f1\u01fa")
        buf.write("\u01ff\u020f\u0214\u0224")
        return buf.getvalue()


class MT22Parser ( Parser ):

    grammarFileName = "MT22.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'function'", "'readInteger'", 
                     "'printInteger'", "'readFloat'", "'writeFloat'", "'readBoolean'", 
                     "'printBoolean'", "'readString'", "'printString'", 
                     "'super'", "'preventDefault'", "'auto'", "'break'", 
                     "'do'", "'else'", "'for'", "'if'", "'return'", "'while'", 
                     "'out'", "'continue'", "'of'", "'inherit'", "'array'", 
                     "'boolean'", "'float'", "'integer'", "'string'", "'void'", 
                     "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", 
                     "'=='", "'!='", "'::'", "'>='", "'<='", "'='", "'>'", 
                     "'<'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
                     "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "FUNCTION", "READ_INTEGER", "PRINT_INTEGER", 
                      "READ_FLOAT", "WRITE_FLOAT", "READ_BOOLEAN", "PRINT_BOOLEAN", 
                      "READ_STRING", "PRINT_STRING", "SUPER", "PREVENT_DEFAULT", 
                      "AUTO", "BREAK", "DO", "ELSE", "FOR", "IF", "RETURN", 
                      "WHILE", "OUT", "CONTINUE", "OF", "INHERIT", "ARRAY", 
                      "BOOLEAN", "FLOAT", "INTEGER", "STRING", "VOID", "PLUSOP", 
                      "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                      "ANDOP", "OROP", "EQUALOP", "NOTEQUALOP", "DOUBLECOLONOP", 
                      "GTE", "LTE", "EQUAL", "GT", "LT", "LB", "RB", "LSB", 
                      "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
                      "VARIABLE_IDENTIFIERS", "BOOLLIT", "FLOATLIT", "INTLIT", 
                      "STRINGLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "WS", 
                      "BLOCK_CMT", "LINE_CMT", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_main_function = 1
    RULE_function_declaration = 2
    RULE_param = 3
    RULE_param_list = 4
    RULE_variable_declaration_no_init = 5
    RULE_variable_declaration_init = 6
    RULE_variable_declaration_init_list = 7
    RULE_assignment_statements = 8
    RULE_lhs = 9
    RULE_method_invocation_statements = 10
    RULE_read_integer_function = 11
    RULE_print_integer_function = 12
    RULE_read_float_function = 13
    RULE_write_float_function = 14
    RULE_read_boolean_function = 15
    RULE_print_boolean_function = 16
    RULE_read_string_function = 17
    RULE_print_string_function = 18
    RULE_super_function = 19
    RULE_prevent_default_function = 20
    RULE_if_statements = 21
    RULE_elseif_list_statements = 22
    RULE_elseif_statement = 23
    RULE_else_statement = 24
    RULE_for_statements = 25
    RULE_while_statements = 26
    RULE_do_while_statements = 27
    RULE_break_statements = 28
    RULE_continue_statements = 29
    RULE_return_expr = 30
    RULE_return_statements = 31
    RULE_return_nothing_statements = 32
    RULE_global_statements = 33
    RULE_global_statement = 34
    RULE_block_statements = 35
    RULE_statements = 36
    RULE_statement = 37
    RULE_block_in_loop_statements = 38
    RULE_in_loop_statements = 39
    RULE_in_loop_statement = 40
    RULE_expr_list = 41
    RULE_expr_list_no_empty = 42
    RULE_expr = 43
    RULE_expr1 = 44
    RULE_expr2 = 45
    RULE_expr3 = 46
    RULE_expr4 = 47
    RULE_expr5 = 48
    RULE_expr6 = 49
    RULE_expr7 = 50
    RULE_expr8 = 51
    RULE_expr9 = 52
    RULE_expr10 = 53
    RULE_array_lit = 54
    RULE_literal = 55
    RULE_all_type = 56
    RULE_array_type = 57
    RULE_atomic_types = 58
    RULE_variable_id_list = 59

    ruleNames =  [ "program", "main_function", "function_declaration", "param", 
                   "param_list", "variable_declaration_no_init", "variable_declaration_init", 
                   "variable_declaration_init_list", "assignment_statements", 
                   "lhs", "method_invocation_statements", "read_integer_function", 
                   "print_integer_function", "read_float_function", "write_float_function", 
                   "read_boolean_function", "print_boolean_function", "read_string_function", 
                   "print_string_function", "super_function", "prevent_default_function", 
                   "if_statements", "elseif_list_statements", "elseif_statement", 
                   "else_statement", "for_statements", "while_statements", 
                   "do_while_statements", "break_statements", "continue_statements", 
                   "return_expr", "return_statements", "return_nothing_statements", 
                   "global_statements", "global_statement", "block_statements", 
                   "statements", "statement", "block_in_loop_statements", 
                   "in_loop_statements", "in_loop_statement", "expr_list", 
                   "expr_list_no_empty", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "expr10", "array_lit", "literal", "all_type", "array_type", 
                   "atomic_types", "variable_id_list" ]

    EOF = Token.EOF
    MAIN=1
    FUNCTION=2
    READ_INTEGER=3
    PRINT_INTEGER=4
    READ_FLOAT=5
    WRITE_FLOAT=6
    READ_BOOLEAN=7
    PRINT_BOOLEAN=8
    READ_STRING=9
    PRINT_STRING=10
    SUPER=11
    PREVENT_DEFAULT=12
    AUTO=13
    BREAK=14
    DO=15
    ELSE=16
    FOR=17
    IF=18
    RETURN=19
    WHILE=20
    OUT=21
    CONTINUE=22
    OF=23
    INHERIT=24
    ARRAY=25
    BOOLEAN=26
    FLOAT=27
    INTEGER=28
    STRING=29
    VOID=30
    PLUSOP=31
    MINUSOP=32
    MULTIPLYOP=33
    DIVIDEOP=34
    MODULOOP=35
    NOTOP=36
    ANDOP=37
    OROP=38
    EQUALOP=39
    NOTEQUALOP=40
    DOUBLECOLONOP=41
    GTE=42
    LTE=43
    EQUAL=44
    GT=45
    LT=46
    LB=47
    RB=48
    LSB=49
    RSB=50
    LCB=51
    RCB=52
    DOT=53
    COMMA=54
    COLON=55
    SEMICOLON=56
    VARIABLE_IDENTIFIERS=57
    BOOLLIT=58
    FLOATLIT=59
    INTLIT=60
    STRINGLIT=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    WS=64
    BLOCK_CMT=65
    LINE_CMT=66
    ERROR_CHAR=67

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

        def global_statements(self):
            return self.getTypedRuleContext(MT22Parser.Global_statementsContext,0)


        def EOF(self):
            return self.getToken(MT22Parser.EOF, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_program




    def program(self):

        localctx = MT22Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.global_statements()
            self.state = 121
            self.match(MT22Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(MT22Parser.MAIN, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MT22Parser.All_typeContext,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_main_function




    def main_function(self):

        localctx = MT22Parser.Main_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(MT22Parser.MAIN)
            self.state = 124
            self.match(MT22Parser.COLON)
            self.state = 125
            self.match(MT22Parser.FUNCTION)
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.ARRAY, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 126
                self.all_type()
                pass
            elif token in [MT22Parser.VOID]:
                self.state = 127
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 130
            self.match(MT22Parser.LB)
            self.state = 131
            self.match(MT22Parser.RB)
            self.state = 132
            self.block_statements()
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

        def VARIABLE_IDENTIFIERS(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.VARIABLE_IDENTIFIERS)
            else:
                return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, i)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def FUNCTION(self):
            return self.getToken(MT22Parser.FUNCTION, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def all_type(self):
            return self.getTypedRuleContext(MT22Parser.All_typeContext,0)


        def VOID(self):
            return self.getToken(MT22Parser.VOID, 0)

        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_function_declaration




    def function_declaration(self):

        localctx = MT22Parser.Function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(MT22Parser.VARIABLE_IDENTIFIERS)
            self.state = 135
            self.match(MT22Parser.COLON)
            self.state = 136
            self.match(MT22Parser.FUNCTION)
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.AUTO, MT22Parser.ARRAY, MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.state = 137
                self.all_type()
                pass
            elif token in [MT22Parser.VOID]:
                self.state = 138
                self.match(MT22Parser.VOID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 141
            self.match(MT22Parser.LB)
            self.state = 142
            self.param_list()
            self.state = 143
            self.match(MT22Parser.RB)
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.state = 144
                self.match(MT22Parser.INHERIT)
                self.state = 145
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                pass
            elif token in [MT22Parser.LCB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 149
            self.block_statements()
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

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def all_type(self):
            return self.getTypedRuleContext(MT22Parser.All_typeContext,0)


        def INHERIT(self):
            return self.getToken(MT22Parser.INHERIT, 0)

        def OUT(self):
            return self.getToken(MT22Parser.OUT, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_param




    def param(self):

        localctx = MT22Parser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INHERIT]:
                self.state = 151
                self.match(MT22Parser.INHERIT)
                pass
            elif token in [MT22Parser.OUT, MT22Parser.VARIABLE_IDENTIFIERS]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 157
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.OUT]:
                self.state = 155
                self.match(MT22Parser.OUT)
                pass
            elif token in [MT22Parser.VARIABLE_IDENTIFIERS]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 159
            self.match(MT22Parser.VARIABLE_IDENTIFIERS)
            self.state = 160
            self.match(MT22Parser.COLON)
            self.state = 161
            self.all_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MT22Parser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def param_list(self):
            return self.getTypedRuleContext(MT22Parser.Param_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_param_list




    def param_list(self):

        localctx = MT22Parser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_param_list)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.param()
                self.state = 164
                self.match(MT22Parser.COMMA)
                self.state = 165
                self.param_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
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


    class Variable_declaration_no_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_id_list(self):
            return self.getTypedRuleContext(MT22Parser.Variable_id_listContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def all_type(self):
            return self.getTypedRuleContext(MT22Parser.All_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variable_declaration_no_init




    def variable_declaration_no_init(self):

        localctx = MT22Parser.Variable_declaration_no_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variable_declaration_no_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.variable_id_list()
            self.state = 172
            self.match(MT22Parser.COLON)
            self.state = 173
            self.all_type()
            self.state = 174
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaration_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def variable_declaration_init_list(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declaration_init_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variable_declaration_init




    def variable_declaration_init(self):

        localctx = MT22Parser.Variable_declaration_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable_declaration_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MT22Parser.VARIABLE_IDENTIFIERS)
            self.state = 177
            self.variable_declaration_init_list()
            self.state = 178
            self.expr()
            self.state = 179
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_declaration_init_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def variable_declaration_init_list(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declaration_init_listContext,0)


        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COLON(self):
            return self.getToken(MT22Parser.COLON, 0)

        def all_type(self):
            return self.getTypedRuleContext(MT22Parser.All_typeContext,0)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_variable_declaration_init_list




    def variable_declaration_init_list(self):

        localctx = MT22Parser.Variable_declaration_init_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_declaration_init_list)
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.match(MT22Parser.COMMA)
                self.state = 182
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                self.state = 183
                self.variable_declaration_init_list()
                self.state = 184
                self.expr()
                self.state = 185
                self.match(MT22Parser.COMMA)
                pass
            elif token in [MT22Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.match(MT22Parser.COLON)
                self.state = 188
                self.all_type()
                self.state = 189
                self.match(MT22Parser.EQUAL)
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


    class Assignment_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MT22Parser.LhsContext,0)


        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_assignment_statements




    def assignment_statements(self):

        localctx = MT22Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.lhs()
            self.state = 194
            self.match(MT22Parser.EQUAL)
            self.state = 195
            self.expr()
            self.state = 196
            self.match(MT22Parser.SEMICOLON)
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

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expr_list_no_empty(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list_no_emptyContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_lhs




    def lhs(self):

        localctx = MT22Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_lhs)
        try:
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                self.state = 200
                self.match(MT22Parser.LSB)
                self.state = 201
                self.expr_list_no_empty()
                self.state = 202
                self.match(MT22Parser.RSB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Method_invocation_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def read_integer_function(self):
            return self.getTypedRuleContext(MT22Parser.Read_integer_functionContext,0)


        def print_integer_function(self):
            return self.getTypedRuleContext(MT22Parser.Print_integer_functionContext,0)


        def read_float_function(self):
            return self.getTypedRuleContext(MT22Parser.Read_float_functionContext,0)


        def write_float_function(self):
            return self.getTypedRuleContext(MT22Parser.Write_float_functionContext,0)


        def read_boolean_function(self):
            return self.getTypedRuleContext(MT22Parser.Read_boolean_functionContext,0)


        def print_boolean_function(self):
            return self.getTypedRuleContext(MT22Parser.Print_boolean_functionContext,0)


        def read_string_function(self):
            return self.getTypedRuleContext(MT22Parser.Read_string_functionContext,0)


        def print_string_function(self):
            return self.getTypedRuleContext(MT22Parser.Print_string_functionContext,0)


        def super_function(self):
            return self.getTypedRuleContext(MT22Parser.Super_functionContext,0)


        def prevent_default_function(self):
            return self.getTypedRuleContext(MT22Parser.Prevent_default_functionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_method_invocation_statements




    def method_invocation_statements(self):

        localctx = MT22Parser.Method_invocation_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_method_invocation_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.VARIABLE_IDENTIFIERS]:
                self.state = 206
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                self.state = 207
                self.match(MT22Parser.LB)
                self.state = 208
                self.expr_list()
                self.state = 209
                self.match(MT22Parser.RB)
                pass
            elif token in [MT22Parser.READ_INTEGER]:
                self.state = 211
                self.read_integer_function()
                pass
            elif token in [MT22Parser.PRINT_INTEGER]:
                self.state = 212
                self.print_integer_function()
                pass
            elif token in [MT22Parser.READ_FLOAT]:
                self.state = 213
                self.read_float_function()
                pass
            elif token in [MT22Parser.WRITE_FLOAT]:
                self.state = 214
                self.write_float_function()
                pass
            elif token in [MT22Parser.READ_BOOLEAN]:
                self.state = 215
                self.read_boolean_function()
                pass
            elif token in [MT22Parser.PRINT_BOOLEAN]:
                self.state = 216
                self.print_boolean_function()
                pass
            elif token in [MT22Parser.READ_STRING]:
                self.state = 217
                self.read_string_function()
                pass
            elif token in [MT22Parser.PRINT_STRING]:
                self.state = 218
                self.print_string_function()
                pass
            elif token in [MT22Parser.SUPER]:
                self.state = 219
                self.super_function()
                pass
            elif token in [MT22Parser.PREVENT_DEFAULT]:
                self.state = 220
                self.prevent_default_function()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 223
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_integer_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_INTEGER(self):
            return self.getToken(MT22Parser.READ_INTEGER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_read_integer_function




    def read_integer_function(self):

        localctx = MT22Parser.Read_integer_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_read_integer_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(MT22Parser.READ_INTEGER)
            self.state = 226
            self.match(MT22Parser.LB)
            self.state = 227
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_integer_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_INTEGER(self):
            return self.getToken(MT22Parser.PRINT_INTEGER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_print_integer_function




    def print_integer_function(self):

        localctx = MT22Parser.Print_integer_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_print_integer_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(MT22Parser.PRINT_INTEGER)
            self.state = 230
            self.match(MT22Parser.LB)
            self.state = 233
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.NOTOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.state = 231
                self.expr()
                pass
            elif token in [MT22Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 235
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_float_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_FLOAT(self):
            return self.getToken(MT22Parser.READ_FLOAT, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_read_float_function




    def read_float_function(self):

        localctx = MT22Parser.Read_float_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_read_float_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(MT22Parser.READ_FLOAT)
            self.state = 238
            self.match(MT22Parser.LB)
            self.state = 239
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Write_float_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE_FLOAT(self):
            return self.getToken(MT22Parser.WRITE_FLOAT, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_write_float_function




    def write_float_function(self):

        localctx = MT22Parser.Write_float_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_write_float_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MT22Parser.WRITE_FLOAT)
            self.state = 242
            self.match(MT22Parser.LB)
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.NOTOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.state = 243
                self.expr()
                pass
            elif token in [MT22Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 247
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_boolean_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_BOOLEAN(self):
            return self.getToken(MT22Parser.READ_BOOLEAN, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_read_boolean_function




    def read_boolean_function(self):

        localctx = MT22Parser.Read_boolean_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_read_boolean_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(MT22Parser.READ_BOOLEAN)
            self.state = 250
            self.match(MT22Parser.LB)
            self.state = 251
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_boolean_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_BOOLEAN(self):
            return self.getToken(MT22Parser.PRINT_BOOLEAN, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_print_boolean_function




    def print_boolean_function(self):

        localctx = MT22Parser.Print_boolean_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_print_boolean_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MT22Parser.PRINT_BOOLEAN)
            self.state = 254
            self.match(MT22Parser.LB)
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.NOTOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.state = 255
                self.expr()
                pass
            elif token in [MT22Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 259
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Read_string_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ_STRING(self):
            return self.getToken(MT22Parser.READ_STRING, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_read_string_function




    def read_string_function(self):

        localctx = MT22Parser.Read_string_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_read_string_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(MT22Parser.READ_STRING)
            self.state = 262
            self.match(MT22Parser.LB)
            self.state = 263
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Print_string_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT_STRING(self):
            return self.getToken(MT22Parser.PRINT_STRING, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_print_string_function




    def print_string_function(self):

        localctx = MT22Parser.Print_string_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_print_string_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(MT22Parser.PRINT_STRING)
            self.state = 266
            self.match(MT22Parser.LB)
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.NOTOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.state = 267
                self.expr()
                pass
            elif token in [MT22Parser.RB]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 271
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Super_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUPER(self):
            return self.getToken(MT22Parser.SUPER, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_super_function




    def super_function(self):

        localctx = MT22Parser.Super_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_super_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(MT22Parser.SUPER)
            self.state = 274
            self.match(MT22Parser.LB)
            self.state = 275
            self.expr_list()
            self.state = 276
            self.match(MT22Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Prevent_default_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PREVENT_DEFAULT(self):
            return self.getToken(MT22Parser.PREVENT_DEFAULT, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_prevent_default_function




    def prevent_default_function(self):

        localctx = MT22Parser.Prevent_default_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_prevent_default_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(MT22Parser.PREVENT_DEFAULT)
            self.state = 279
            self.match(MT22Parser.LB)
            self.state = 280
            self.match(MT22Parser.RB)
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
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def elseif_list_statements(self):
            return self.getTypedRuleContext(MT22Parser.Elseif_list_statementsContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_if_statements




    def if_statements(self):

        localctx = MT22Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(MT22Parser.IF)
            self.state = 283
            self.match(MT22Parser.LB)
            self.state = 284
            self.expr()
            self.state = 285
            self.match(MT22Parser.RB)
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 286
                self.block_statements()
                pass

            elif la_ == 2:
                self.state = 287
                self.statement()
                pass


            self.state = 290
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
            return self.getTypedRuleContext(MT22Parser.Elseif_statementContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(MT22Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_elseif_list_statements




    def elseif_list_statements(self):

        localctx = MT22Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_elseif_list_statements)
        try:
            self.state = 295
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.elseif_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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

        def ELSE(self):
            return self.getToken(MT22Parser.ELSE, 0)

        def IF(self):
            return self.getToken(MT22Parser.IF, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def elseif_list_statements(self):
            return self.getTypedRuleContext(MT22Parser.Elseif_list_statementsContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_elseif_statement




    def elseif_statement(self):

        localctx = MT22Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MT22Parser.ELSE)
            self.state = 298
            self.match(MT22Parser.IF)
            self.state = 299
            self.match(MT22Parser.LB)
            self.state = 300
            self.expr()
            self.state = 301
            self.match(MT22Parser.RB)
            self.state = 304
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 302
                self.block_statements()
                pass

            elif la_ == 2:
                self.state = 303
                self.statement()
                pass


            self.state = 306
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
            return self.getToken(MT22Parser.ELSE, 0)

        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_else_statement




    def else_statement(self):

        localctx = MT22Parser.Else_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_else_statement)
        try:
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.match(MT22Parser.ELSE)
                self.state = 311
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 309
                    self.block_statements()
                    pass

                elif la_ == 2:
                    self.state = 310
                    self.statement()
                    pass


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


    class For_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MT22Parser.FOR, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def EQUAL(self):
            return self.getToken(MT22Parser.EQUAL, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MT22Parser.ExprContext)
            else:
                return self.getTypedRuleContext(MT22Parser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MT22Parser.COMMA)
            else:
                return self.getToken(MT22Parser.COMMA, i)

        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_for_statements




    def for_statements(self):

        localctx = MT22Parser.For_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_for_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MT22Parser.FOR)
            self.state = 317
            self.match(MT22Parser.LB)
            self.state = 318
            self.match(MT22Parser.VARIABLE_IDENTIFIERS)
            self.state = 319
            self.match(MT22Parser.EQUAL)
            self.state = 320
            self.expr()
            self.state = 321
            self.match(MT22Parser.COMMA)
            self.state = 322
            self.expr()
            self.state = 323
            self.match(MT22Parser.COMMA)
            self.state = 324
            self.expr()
            self.state = 325
            self.match(MT22Parser.RB)
            self.state = 328
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 326
                self.block_statements()
                pass

            elif la_ == 2:
                self.state = 327
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def statement(self):
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_while_statements




    def while_statements(self):

        localctx = MT22Parser.While_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_while_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 330
            self.match(MT22Parser.WHILE)
            self.state = 331
            self.match(MT22Parser.LB)
            self.state = 332
            self.expr()
            self.state = 333
            self.match(MT22Parser.RB)
            self.state = 336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 334
                self.block_statements()
                pass

            elif la_ == 2:
                self.state = 335
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_while_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(MT22Parser.DO, 0)

        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def WHILE(self):
            return self.getToken(MT22Parser.WHILE, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_do_while_statements




    def do_while_statements(self):

        localctx = MT22Parser.Do_while_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_do_while_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(MT22Parser.DO)
            self.state = 339
            self.block_statements()
            self.state = 340
            self.match(MT22Parser.WHILE)
            self.state = 341
            self.match(MT22Parser.LB)
            self.state = 342
            self.expr()
            self.state = 343
            self.match(MT22Parser.RB)
            self.state = 344
            self.match(MT22Parser.SEMICOLON)
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
            return self.getToken(MT22Parser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_break_statements




    def break_statements(self):

        localctx = MT22Parser.Break_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(MT22Parser.BREAK)
            self.state = 347
            self.match(MT22Parser.SEMICOLON)
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
            return self.getToken(MT22Parser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_continue_statements




    def continue_statements(self):

        localctx = MT22Parser.Continue_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MT22Parser.CONTINUE)
            self.state = 350
            self.match(MT22Parser.SEMICOLON)
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
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_return_expr




    def return_expr(self):

        localctx = MT22Parser.Return_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_return_expr)
        try:
            self.state = 354
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.NOTOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 352
                self.expr()
                pass
            elif token in [MT22Parser.SEMICOLON]:
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
            return self.getToken(MT22Parser.RETURN, 0)

        def return_expr(self):
            return self.getTypedRuleContext(MT22Parser.Return_exprContext,0)


        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_return_statements




    def return_statements(self):

        localctx = MT22Parser.Return_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.match(MT22Parser.RETURN)
            self.state = 357
            self.return_expr()
            self.state = 358
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_nothing_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MT22Parser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(MT22Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_return_nothing_statements




    def return_nothing_statements(self):

        localctx = MT22Parser.Return_nothing_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_return_nothing_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(MT22Parser.RETURN)
            self.state = 361
            self.match(MT22Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def global_statement(self):
            return self.getTypedRuleContext(MT22Parser.Global_statementContext,0)


        def global_statements(self):
            return self.getTypedRuleContext(MT22Parser.Global_statementsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_global_statements




    def global_statements(self):

        localctx = MT22Parser.Global_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_global_statements)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 363
                self.global_statement()
                self.state = 364
                self.global_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.global_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_no_init(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declaration_no_initContext,0)


        def variable_declaration_init(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declaration_initContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Function_declarationContext,0)


        def main_function(self):
            return self.getTypedRuleContext(MT22Parser.Main_functionContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_global_statement




    def global_statement(self):

        localctx = MT22Parser.Global_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_global_statement)
        try:
            self.state = 373
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.variable_declaration_no_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.variable_declaration_init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.function_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
                self.main_function()
                pass


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
            return self.getToken(MT22Parser.LCB, 0)

        def statements(self):
            return self.getTypedRuleContext(MT22Parser.StatementsContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_block_statements




    def block_statements(self):

        localctx = MT22Parser.Block_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(MT22Parser.LCB)
            self.state = 376
            self.statements()
            self.state = 377
            self.match(MT22Parser.RCB)
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
            return self.getTypedRuleContext(MT22Parser.StatementContext,0)


        def statements(self):
            return self.getTypedRuleContext(MT22Parser.StatementsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statements




    def statements(self):

        localctx = MT22Parser.StatementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_statements)
        try:
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                self.statement()
                self.state = 380
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_declaration_no_init(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declaration_no_initContext,0)


        def variable_declaration_init(self):
            return self.getTypedRuleContext(MT22Parser.Variable_declaration_initContext,0)


        def function_declaration(self):
            return self.getTypedRuleContext(MT22Parser.Function_declarationContext,0)


        def assignment_statements(self):
            return self.getTypedRuleContext(MT22Parser.Assignment_statementsContext,0)


        def if_statements(self):
            return self.getTypedRuleContext(MT22Parser.If_statementsContext,0)


        def for_statements(self):
            return self.getTypedRuleContext(MT22Parser.For_statementsContext,0)


        def while_statements(self):
            return self.getTypedRuleContext(MT22Parser.While_statementsContext,0)


        def do_while_statements(self):
            return self.getTypedRuleContext(MT22Parser.Do_while_statementsContext,0)


        def method_invocation_statements(self):
            return self.getTypedRuleContext(MT22Parser.Method_invocation_statementsContext,0)


        def return_statements(self):
            return self.getTypedRuleContext(MT22Parser.Return_statementsContext,0)


        def return_nothing_statements(self):
            return self.getTypedRuleContext(MT22Parser.Return_nothing_statementsContext,0)


        def in_loop_statement(self):
            return self.getTypedRuleContext(MT22Parser.In_loop_statementContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_statement




    def statement(self):

        localctx = MT22Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_statement)
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.variable_declaration_no_init()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 387
                self.variable_declaration_init()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 388
                self.function_declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 389
                self.assignment_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 390
                self.if_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 391
                self.for_statements()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 392
                self.while_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 393
                self.do_while_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 394
                self.method_invocation_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 395
                self.return_statements()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 396
                self.return_nothing_statements()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 397
                self.in_loop_statement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 398
                self.block_statements()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_in_loop_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(MT22Parser.LCB, 0)

        def in_loop_statements(self):
            return self.getTypedRuleContext(MT22Parser.In_loop_statementsContext,0)


        def RCB(self):
            return self.getToken(MT22Parser.RCB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_block_in_loop_statements




    def block_in_loop_statements(self):

        localctx = MT22Parser.Block_in_loop_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block_in_loop_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self.match(MT22Parser.LCB)
            self.state = 402
            self.in_loop_statements()
            self.state = 403
            self.match(MT22Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class In_loop_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def in_loop_statement(self):
            return self.getTypedRuleContext(MT22Parser.In_loop_statementContext,0)


        def in_loop_statements(self):
            return self.getTypedRuleContext(MT22Parser.In_loop_statementsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_in_loop_statements




    def in_loop_statements(self):

        localctx = MT22Parser.In_loop_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_in_loop_statements)
        try:
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 405
                self.in_loop_statement()
                self.state = 406
                self.in_loop_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 408
                self.in_loop_statement()
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


    class In_loop_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def break_statements(self):
            return self.getTypedRuleContext(MT22Parser.Break_statementsContext,0)


        def continue_statements(self):
            return self.getTypedRuleContext(MT22Parser.Continue_statementsContext,0)


        def block_in_loop_statements(self):
            return self.getTypedRuleContext(MT22Parser.Block_in_loop_statementsContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_in_loop_statement




    def in_loop_statement(self):

        localctx = MT22Parser.In_loop_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_in_loop_statement)
        try:
            self.state = 415
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BREAK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.break_statements()
                pass
            elif token in [MT22Parser.CONTINUE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
                self.continue_statements()
                pass
            elif token in [MT22Parser.LCB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 414
                self.block_in_loop_statements()
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


    class Expr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr_list_no_empty(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list_no_emptyContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list




    def expr_list(self):

        localctx = MT22Parser.Expr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expr_list)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.NOTOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.expr_list_no_empty()
                pass
            elif token in [MT22Parser.RB, MT22Parser.RSB]:
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


    class Expr_list_no_emptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr_list_no_empty




    def expr_list_no_empty(self):

        localctx = MT22Parser.Expr_list_no_emptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr_list_no_empty)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.expr()
                self.state = 422
                self.match(MT22Parser.COMMA)
                self.state = 423
                self.expr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.expr()
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
                return self.getTypedRuleContexts(MT22Parser.Expr1Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr1Context,i)


        def DOUBLECOLONOP(self):
            return self.getToken(MT22Parser.DOUBLECOLONOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr




    def expr(self):

        localctx = MT22Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_expr)
        try:
            self.state = 433
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.expr1()
                self.state = 429
                self.match(MT22Parser.DOUBLECOLONOP)
                self.state = 430
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
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
                return self.getTypedRuleContexts(MT22Parser.Expr2Context)
            else:
                return self.getTypedRuleContext(MT22Parser.Expr2Context,i)


        def EQUALOP(self):
            return self.getToken(MT22Parser.EQUALOP, 0)

        def NOTEQUALOP(self):
            return self.getToken(MT22Parser.NOTEQUALOP, 0)

        def LT(self):
            return self.getToken(MT22Parser.LT, 0)

        def GT(self):
            return self.getToken(MT22Parser.GT, 0)

        def LTE(self):
            return self.getToken(MT22Parser.LTE, 0)

        def GTE(self):
            return self.getToken(MT22Parser.GTE, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr1




    def expr1(self):

        localctx = MT22Parser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 440
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.expr2(0)
                self.state = 436
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.EQUALOP) | (1 << MT22Parser.NOTEQUALOP) | (1 << MT22Parser.GTE) | (1 << MT22Parser.LTE) | (1 << MT22Parser.GT) | (1 << MT22Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 439
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
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MT22Parser.Expr2Context,0)


        def ANDOP(self):
            return self.getToken(MT22Parser.ANDOP, 0)

        def OROP(self):
            return self.getToken(MT22Parser.OROP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 445
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 446
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.ANDOP or _la==MT22Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 447
                    self.expr3(0) 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

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
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MT22Parser.Expr3Context,0)


        def PLUSOP(self):
            return self.getToken(MT22Parser.PLUSOP, 0)

        def MINUSOP(self):
            return self.getToken(MT22Parser.MINUSOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 92
        self.enterRecursionRule(localctx, 92, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 461
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,32,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 456
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 457
                    _la = self._input.LA(1)
                    if not(_la==MT22Parser.PLUSOP or _la==MT22Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 458
                    self.expr4(0) 
                self.state = 463
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,32,self._ctx)

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
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MT22Parser.Expr4Context,0)


        def MULTIPLYOP(self):
            return self.getToken(MT22Parser.MULTIPLYOP, 0)

        def DIVIDEOP(self):
            return self.getToken(MT22Parser.DIVIDEOP, 0)

        def MODULOOP(self):
            return self.getToken(MT22Parser.MODULOOP, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 94
        self.enterRecursionRule(localctx, 94, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 465
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 472
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 467
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 468
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.MULTIPLYOP) | (1 << MT22Parser.DIVIDEOP) | (1 << MT22Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 469
                    self.expr5() 
                self.state = 474
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
            return self.getToken(MT22Parser.NOTOP, 0)

        def expr5(self):
            return self.getTypedRuleContext(MT22Parser.Expr5Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr5




    def expr5(self):

        localctx = MT22Parser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr5)
        try:
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self.match(MT22Parser.NOTOP)
                self.state = 476
                self.expr5()
                pass
            elif token in [MT22Parser.ARRAY, MT22Parser.MINUSOP, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 477
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
            return self.getToken(MT22Parser.MINUSOP, 0)

        def expr6(self):
            return self.getTypedRuleContext(MT22Parser.Expr6Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr6




    def expr6(self):

        localctx = MT22Parser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr6)
        try:
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.match(MT22Parser.MINUSOP)
                self.state = 481
                self.expr6()
                pass
            elif token in [MT22Parser.ARRAY, MT22Parser.LB, MT22Parser.VARIABLE_IDENTIFIERS, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
            return self.getTypedRuleContext(MT22Parser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(MT22Parser.Expr7Context,0)


        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expr_list_no_empty(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list_no_emptyContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MT22Parser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 495
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MT22Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 488
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 489
                    self.match(MT22Parser.LSB)
                    self.state = 490
                    self.expr_list_no_empty()
                    self.state = 491
                    self.match(MT22Parser.RSB) 
                self.state = 497
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def expr9(self):
            return self.getTypedRuleContext(MT22Parser.Expr9Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr8




    def expr8(self):

        localctx = MT22Parser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expr8)
        try:
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 498
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                self.state = 499
                self.match(MT22Parser.LB)
                self.state = 500
                self.expr_list()
                self.state = 501
                self.match(MT22Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 503
                self.expr9()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MT22Parser.LiteralContext,0)


        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def expr10(self):
            return self.getTypedRuleContext(MT22Parser.Expr10Context,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_expr9




    def expr9(self):

        localctx = MT22Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr9)
        try:
            self.state = 509
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.ARRAY, MT22Parser.BOOLLIT, MT22Parser.FLOATLIT, MT22Parser.INTLIT, MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                self.literal()
                pass
            elif token in [MT22Parser.VARIABLE_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                pass
            elif token in [MT22Parser.LB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 508
                self.expr10()
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


    class Expr10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(MT22Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(MT22Parser.ExprContext,0)


        def RB(self):
            return self.getToken(MT22Parser.RB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_expr10




    def expr10(self):

        localctx = MT22Parser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr10)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(MT22Parser.LB)
            self.state = 512
            self.expr()
            self.state = 513
            self.match(MT22Parser.RB)
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
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expr_list(self):
            return self.getTypedRuleContext(MT22Parser.Expr_listContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_array_lit




    def array_lit(self):

        localctx = MT22Parser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(MT22Parser.ARRAY)
            self.state = 516
            self.match(MT22Parser.LSB)
            self.state = 517
            self.expr_list()
            self.state = 518
            self.match(MT22Parser.RSB)
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

        def INTLIT(self):
            return self.getToken(MT22Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MT22Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MT22Parser.BOOLLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MT22Parser.STRINGLIT, 0)

        def array_lit(self):
            return self.getTypedRuleContext(MT22Parser.Array_litContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_literal




    def literal(self):

        localctx = MT22Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_literal)
        try:
            self.state = 525
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.match(MT22Parser.INTLIT)
                pass
            elif token in [MT22Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.match(MT22Parser.FLOATLIT)
                pass
            elif token in [MT22Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 522
                self.match(MT22Parser.BOOLLIT)
                pass
            elif token in [MT22Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 523
                self.match(MT22Parser.STRINGLIT)
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 524
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


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atomic_types(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typesContext,0)


        def array_type(self):
            return self.getTypedRuleContext(MT22Parser.Array_typeContext,0)


        def AUTO(self):
            return self.getToken(MT22Parser.AUTO, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_all_type




    def all_type(self):

        localctx = MT22Parser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_all_type)
        try:
            self.state = 530
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MT22Parser.BOOLEAN, MT22Parser.FLOAT, MT22Parser.INTEGER, MT22Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.atomic_types()
                pass
            elif token in [MT22Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 528
                self.array_type()
                pass
            elif token in [MT22Parser.AUTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 529
                self.match(MT22Parser.AUTO)
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


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(MT22Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(MT22Parser.LSB, 0)

        def expr_list_no_empty(self):
            return self.getTypedRuleContext(MT22Parser.Expr_list_no_emptyContext,0)


        def RSB(self):
            return self.getToken(MT22Parser.RSB, 0)

        def OF(self):
            return self.getToken(MT22Parser.OF, 0)

        def atomic_types(self):
            return self.getTypedRuleContext(MT22Parser.Atomic_typesContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_array_type




    def array_type(self):

        localctx = MT22Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.match(MT22Parser.ARRAY)
            self.state = 533
            self.match(MT22Parser.LSB)
            self.state = 534
            self.expr_list_no_empty()
            self.state = 535
            self.match(MT22Parser.RSB)
            self.state = 536
            self.match(MT22Parser.OF)
            self.state = 537
            self.atomic_types()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Atomic_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BOOLEAN(self):
            return self.getToken(MT22Parser.BOOLEAN, 0)

        def INTEGER(self):
            return self.getToken(MT22Parser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(MT22Parser.FLOAT, 0)

        def STRING(self):
            return self.getToken(MT22Parser.STRING, 0)

        def getRuleIndex(self):
            return MT22Parser.RULE_atomic_types




    def atomic_types(self):

        localctx = MT22Parser.Atomic_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_atomic_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MT22Parser.BOOLEAN) | (1 << MT22Parser.FLOAT) | (1 << MT22Parser.INTEGER) | (1 << MT22Parser.STRING))) != 0)):
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


    class Variable_id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE_IDENTIFIERS(self):
            return self.getToken(MT22Parser.VARIABLE_IDENTIFIERS, 0)

        def COMMA(self):
            return self.getToken(MT22Parser.COMMA, 0)

        def variable_id_list(self):
            return self.getTypedRuleContext(MT22Parser.Variable_id_listContext,0)


        def getRuleIndex(self):
            return MT22Parser.RULE_variable_id_list




    def variable_id_list(self):

        localctx = MT22Parser.Variable_id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_variable_id_list)
        try:
            self.state = 546
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 541
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
                self.state = 542
                self.match(MT22Parser.COMMA)
                self.state = 543
                self.variable_id_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.match(MT22Parser.VARIABLE_IDENTIFIERS)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[45] = self.expr2_sempred
        self._predicates[46] = self.expr3_sempred
        self._predicates[47] = self.expr4_sempred
        self._predicates[50] = self.expr7_sempred
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
         




