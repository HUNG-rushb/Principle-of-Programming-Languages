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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
        buf.write("\u02b8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("M\4N\tN\4O\tO\3\2\3\2\3\2\6\2\u00a2\n\2\r\2\16\2\u00a3")
        buf.write("\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u00af\n\4\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00b9\n\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00d2\n\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13\u00de\n\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00ea\n\f\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\5\16\u00f8\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\5\17\u0104\n\17\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\5\23\u0119\n\23\3\24\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u0124\n\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u012b\n\24\3\25\3\25\3\25\3\25\5\25\u0131")
        buf.write("\n\25\3\26\3\26\3\26\5\26\u0136\n\26\3\26\3\26\3\26\3")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0146\n\27\3\30\3\30\3\30\3\30\5\30\u014c\n\30\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\5\33\u015a\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3!\3!\5!\u017f\n!\3\"\3\"\3\"\3#\3#\3#\3")
        buf.write("$\3$\3$\3%\3%\5%\u018c\n%\3&\3&\3&\3&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\3*\3*\5*\u01a5")
        buf.write("\n*\3+\3+\3+\3+\3+\5+\u01ac\n+\3,\3,\3,\3,\5,\u01b2\n")
        buf.write(",\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u01bd\n-\3.\3.\3.\3.\5")
        buf.write(".\u01c3\n.\3/\3/\3/\3/\3/\3/\3/\3/\5/\u01cd\n/\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01d3\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\5\61\u01dd\n\61\3\62\3\62\3\62\3\62\3")
        buf.write("\62\5\62\u01e4\n\62\3\63\3\63\3\63\3\63\3\63\5\63\u01eb")
        buf.write("\n\63\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u01f3\n\64\f")
        buf.write("\64\16\64\u01f6\13\64\3\65\3\65\3\65\3\65\3\65\3\65\7")
        buf.write("\65\u01fe\n\65\f\65\16\65\u0201\13\65\3\66\3\66\3\66\3")
        buf.write("\66\3\66\3\66\7\66\u0209\n\66\f\66\16\66\u020c\13\66\3")
        buf.write("\67\3\67\3\67\5\67\u0211\n\67\38\38\38\58\u0216\n8\39")
        buf.write("\39\39\39\39\79\u021d\n9\f9\169\u0220\139\3:\3:\3:\3:")
        buf.write("\3:\7:\u0227\n:\f:\16:\u022a\13:\3;\3;\3;\5;\u022f\n;")
        buf.write("\3<\3<\3<\3<\3<\3<\3<\5<\u0238\n<\3=\3=\3=\3=\3=\5=\u023f")
        buf.write("\n=\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u024e\n")
        buf.write("?\3@\3@\3@\3@\5@\u0254\n@\3A\3A\3A\3A\3A\3A\5A\u025c\n")
        buf.write("A\3B\3B\3B\3B\3B\3B\5B\u0264\nB\3C\3C\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3D\3D\5D\u0271\nD\3E\3E\3E\3E\3E\5E\u0278\nE\3F\3")
        buf.write("F\3F\3F\3F\3F\5F\u0280\nF\3G\3G\3G\3G\3H\3H\3H\3H\3H\5")
        buf.write("H\u028b\nH\3I\3I\3I\3I\3I\5I\u0292\nI\3J\3J\5J\u0296\n")
        buf.write("J\3J\3J\3J\3J\3J\5J\u029d\nJ\3J\5J\u02a0\nJ\3K\3K\3K\3")
        buf.write("K\3K\3K\3K\3L\3L\3L\3L\3L\5L\u02ae\nL\3M\3M\3N\3N\3O\3")
        buf.write("O\5O\u02b6\nO\3O\2\7fhjprP\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a")
        buf.write("\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c")
        buf.write("\2\13\3\2<=\3\2\25\26\4\2\34\34\66\66\3\2./\4\2\'\')-")
        buf.write("\3\2%&\3\2\37 \3\2!#\3\2\16\21\2\u02bb\2\u00a1\3\2\2\2")
        buf.write("\4\u00a5\3\2\2\2\6\u00ae\3\2\2\2\b\u00b0\3\2\2\2\n\u00b8")
        buf.write("\3\2\2\2\f\u00ba\3\2\2\2\16\u00c0\3\2\2\2\20\u00c5\3\2")
        buf.write("\2\2\22\u00cb\3\2\2\2\24\u00dd\3\2\2\2\26\u00e9\3\2\2")
        buf.write("\2\30\u00eb\3\2\2\2\32\u00f7\3\2\2\2\34\u0103\3\2\2\2")
        buf.write("\36\u0105\3\2\2\2 \u010b\3\2\2\2\"\u0110\3\2\2\2$\u0118")
        buf.write("\3\2\2\2&\u012a\3\2\2\2(\u0130\3\2\2\2*\u0135\3\2\2\2")
        buf.write(",\u013b\3\2\2\2.\u014b\3\2\2\2\60\u014d\3\2\2\2\62\u0153")
        buf.write("\3\2\2\2\64\u0159\3\2\2\2\66\u015b\3\2\2\28\u0166\3\2")
        buf.write("\2\2:\u016a\3\2\2\2<\u0171\3\2\2\2>\u0175\3\2\2\2@\u017e")
        buf.write("\3\2\2\2B\u0180\3\2\2\2D\u0183\3\2\2\2F\u0186\3\2\2\2")
        buf.write("H\u018b\3\2\2\2J\u018d\3\2\2\2L\u0191\3\2\2\2N\u0197\3")
        buf.write("\2\2\2P\u019b\3\2\2\2R\u01a4\3\2\2\2T\u01ab\3\2\2\2V\u01b1")
        buf.write("\3\2\2\2X\u01bc\3\2\2\2Z\u01c2\3\2\2\2\\\u01cc\3\2\2\2")
        buf.write("^\u01d2\3\2\2\2`\u01dc\3\2\2\2b\u01e3\3\2\2\2d\u01ea\3")
        buf.write("\2\2\2f\u01ec\3\2\2\2h\u01f7\3\2\2\2j\u0202\3\2\2\2l\u0210")
        buf.write("\3\2\2\2n\u0215\3\2\2\2p\u0217\3\2\2\2r\u0221\3\2\2\2")
        buf.write("t\u022e\3\2\2\2v\u0237\3\2\2\2x\u023e\3\2\2\2z\u0240\3")
        buf.write("\2\2\2|\u024d\3\2\2\2~\u0253\3\2\2\2\u0080\u025b\3\2\2")
        buf.write("\2\u0082\u0263\3\2\2\2\u0084\u0265\3\2\2\2\u0086\u0270")
        buf.write("\3\2\2\2\u0088\u0277\3\2\2\2\u008a\u027f\3\2\2\2\u008c")
        buf.write("\u0281\3\2\2\2\u008e\u028a\3\2\2\2\u0090\u0291\3\2\2\2")
        buf.write("\u0092\u029f\3\2\2\2\u0094\u02a1\3\2\2\2\u0096\u02ad\3")
        buf.write("\2\2\2\u0098\u02af\3\2\2\2\u009a\u02b1\3\2\2\2\u009c\u02b5")
        buf.write("\3\2\2\2\u009e\u009f\5b\62\2\u009f\u00a0\7\67\2\2\u00a0")
        buf.write("\u00a2\3\2\2\2\u00a1\u009e\3\2\2\2\u00a2\u00a3\3\2\2\2")
        buf.write("\u00a3\u00a1\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\3\3\2\2")
        buf.write("\2\u00a5\u00a6\7\24\2\2\u00a6\u00a7\7:\2\2\u00a7\u00a8")
        buf.write("\5L\'\2\u00a8\5\3\2\2\2\u00a9\u00aa\5\b\5\2\u00aa\u00ab")
        buf.write("\5\6\4\2\u00ab\u00af\3\2\2\2\u00ac\u00af\5\b\5\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae\u00ac\3\2\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\7\3\2\2\2\u00b0\u00b1\7\24")
        buf.write("\2\2\u00b1\u00b2\7<\2\2\u00b2\u00b3\5\n\6\2\u00b3\u00b4")
        buf.write("\5N(\2\u00b4\t\3\2\2\2\u00b5\u00b6\78\2\2\u00b6\u00b9")
        buf.write("\7<\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8")
        buf.write("\u00b7\3\2\2\2\u00b9\13\3\2\2\2\u00ba\u00bb\7\27\2\2\u00bb")
        buf.write("\u00bc\7\60\2\2\u00bc\u00bd\5\u008aF\2\u00bd\u00be\7\61")
        buf.write("\2\2\u00be\u00bf\5P)\2\u00bf\r\3\2\2\2\u00c0\u00c1\7\30")
        buf.write("\2\2\u00c1\u00c2\7\60\2\2\u00c2\u00c3\7\61\2\2\u00c3\u00c4")
        buf.write("\5P)\2\u00c4\17\3\2\2\2\u00c5\u00c6\t\2\2\2\u00c6\u00c7")
        buf.write("\7\60\2\2\u00c7\u00c8\5\u008aF\2\u00c8\u00c9\7\61\2\2")
        buf.write("\u00c9\u00ca\5P)\2\u00ca\21\3\2\2\2\u00cb\u00d1\t\3\2")
        buf.write("\2\u00cc\u00d2\5\24\13\2\u00cd\u00ce\5\u008eH\2\u00ce")
        buf.write("\u00cf\78\2\2\u00cf\u00d0\5\u009cO\2\u00d0\u00d2\3\2\2")
        buf.write("\2\u00d1\u00cc\3\2\2\2\u00d1\u00cd\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d4\79\2\2\u00d4\23\3\2\2\2\u00d5\u00d6")
        buf.write("\t\2\2\2\u00d6\u00d7\5\26\f\2\u00d7\u00d8\5b\62\2\u00d8")
        buf.write("\u00de\3\2\2\2\u00d9\u00da\5\u008eH\2\u00da\u00db\78\2")
        buf.write("\2\u00db\u00dc\5\u009cO\2\u00dc\u00de\3\2\2\2\u00dd\u00d5")
        buf.write("\3\2\2\2\u00dd\u00d9\3\2\2\2\u00de\25\3\2\2\2\u00df\u00e0")
        buf.write("\7\67\2\2\u00e0\u00e1\t\2\2\2\u00e1\u00e2\5\26\f\2\u00e2")
        buf.write("\u00e3\5b\62\2\u00e3\u00e4\7\67\2\2\u00e4\u00ea\3\2\2")
        buf.write("\2\u00e5\u00e6\78\2\2\u00e6\u00e7\5\u009cO\2\u00e7\u00e8")
        buf.write("\7(\2\2\u00e8\u00ea\3\2\2\2\u00e9\u00df\3\2\2\2\u00e9")
        buf.write("\u00e5\3\2\2\2\u00ea\27\3\2\2\2\u00eb\u00ec\t\3\2\2\u00ec")
        buf.write("\u00ed\5\32\16\2\u00ed\u00ee\79\2\2\u00ee\31\3\2\2\2\u00ef")
        buf.write("\u00f0\t\2\2\2\u00f0\u00f1\5\34\17\2\u00f1\u00f2\5b\62")
        buf.write("\2\u00f2\u00f8\3\2\2\2\u00f3\u00f4\5\u0090I\2\u00f4\u00f5")
        buf.write("\78\2\2\u00f5\u00f6\5\u009cO\2\u00f6\u00f8\3\2\2\2\u00f7")
        buf.write("\u00ef\3\2\2\2\u00f7\u00f3\3\2\2\2\u00f8\33\3\2\2\2\u00f9")
        buf.write("\u00fa\7\67\2\2\u00fa\u00fb\t\2\2\2\u00fb\u00fc\5\34\17")
        buf.write("\2\u00fc\u00fd\5b\62\2\u00fd\u00fe\7\67\2\2\u00fe\u0104")
        buf.write("\3\2\2\2\u00ff\u0100\78\2\2\u0100\u0101\5\u009cO\2\u0101")
        buf.write("\u0102\7(\2\2\u0102\u0104\3\2\2\2\u0103\u00f9\3\2\2\2")
        buf.write("\u0103\u00ff\3\2\2\2\u0104\35\3\2\2\2\u0105\u0106\t\2")
        buf.write("\2\2\u0106\u0107\7\60\2\2\u0107\u0108\5\u008aF\2\u0108")
        buf.write("\u0109\7\61\2\2\u0109\u010a\5P)\2\u010a\37\3\2\2\2\u010b")
        buf.write("\u010c\7;\2\2\u010c\u010d\7\60\2\2\u010d\u010e\7\61\2")
        buf.write("\2\u010e\u010f\5P)\2\u010f!\3\2\2\2\u0110\u0111\5$\23")
        buf.write("\2\u0111\u0112\79\2\2\u0112#\3\2\2\2\u0113\u0114\5&\24")
        buf.write("\2\u0114\u0115\t\4\2\2\u0115\u0116\5$\23\2\u0116\u0119")
        buf.write("\3\2\2\2\u0117\u0119\5&\24\2\u0118\u0113\3\2\2\2\u0118")
        buf.write("\u0117\3\2\2\2\u0119%\3\2\2\2\u011a\u011b\t\2\2\2\u011b")
        buf.write("\u011c\7\60\2\2\u011c\u011d\5\u0092J\2\u011d\u011e\7\61")
        buf.write("\2\2\u011e\u012b\3\2\2\2\u011f\u0120\5(\25\2\u0120\u0121")
        buf.write("\t\4\2\2\u0121\u0124\3\2\2\2\u0122\u0124\3\2\2\2\u0123")
        buf.write("\u011f\3\2\2\2\u0123\u0122\3\2\2\2\u0124\u0125\3\2\2\2")
        buf.write("\u0125\u0126\t\2\2\2\u0126\u0127\7\60\2\2\u0127\u0128")
        buf.write("\5\u0092J\2\u0128\u0129\7\61\2\2\u0129\u012b\3\2\2\2\u012a")
        buf.write("\u011a\3\2\2\2\u012a\u0123\3\2\2\2\u012b\'\3\2\2\2\u012c")
        buf.write("\u012d\t\2\2\2\u012d\u012e\t\4\2\2\u012e\u0131\5(\25\2")
        buf.write("\u012f\u0131\t\2\2\2\u0130\u012c\3\2\2\2\u0130\u012f\3")
        buf.write("\2\2\2\u0131)\3\2\2\2\u0132\u0136\7<\2\2\u0133\u0136\7")
        buf.write("=\2\2\u0134\u0136\5b\62\2\u0135\u0132\3\2\2\2\u0135\u0133")
        buf.write("\3\2\2\2\u0135\u0134\3\2\2\2\u0136\u0137\3\2\2\2\u0137")
        buf.write("\u0138\7(\2\2\u0138\u0139\5b\62\2\u0139\u013a\79\2\2\u013a")
        buf.write("+\3\2\2\2\u013b\u013c\7\5\2\2\u013c\u013d\7\60\2\2\u013d")
        buf.write("\u013e\5b\62\2\u013e\u013f\7\61\2\2\u013f\u0145\5P)\2")
        buf.write("\u0140\u0141\5.\30\2\u0141\u0142\5\62\32\2\u0142\u0146")
        buf.write("\3\2\2\2\u0143\u0146\5\62\32\2\u0144\u0146\3\2\2\2\u0145")
        buf.write("\u0140\3\2\2\2\u0145\u0143\3\2\2\2\u0145\u0144\3\2\2\2")
        buf.write("\u0146-\3\2\2\2\u0147\u0148\5\60\31\2\u0148\u0149\5.\30")
        buf.write("\2\u0149\u014c\3\2\2\2\u014a\u014c\5\60\31\2\u014b\u0147")
        buf.write("\3\2\2\2\u014b\u014a\3\2\2\2\u014c/\3\2\2\2\u014d\u014e")
        buf.write("\7\6\2\2\u014e\u014f\7\60\2\2\u014f\u0150\5b\62\2\u0150")
        buf.write("\u0151\7\61\2\2\u0151\u0152\5P)\2\u0152\61\3\2\2\2\u0153")
        buf.write("\u0154\7\7\2\2\u0154\u0155\5P)\2\u0155\63\3\2\2\2\u0156")
        buf.write("\u0157\7\32\2\2\u0157\u015a\5b\62\2\u0158\u015a\3\2\2")
        buf.write("\2\u0159\u0156\3\2\2\2\u0159\u0158\3\2\2\2\u015a\65\3")
        buf.write("\2\2\2\u015b\u015c\7\b\2\2\u015c\u015d\7\60\2\2\u015d")
        buf.write("\u015e\t\2\2\2\u015e\u015f\7\r\2\2\u015f\u0160\5b\62\2")
        buf.write("\u0160\u0161\7\35\2\2\u0161\u0162\5b\62\2\u0162\u0163")
        buf.write("\5\64\33\2\u0163\u0164\7\61\2\2\u0164\u0165\5P)\2\u0165")
        buf.write("\67\3\2\2\2\u0166\u0167\5b\62\2\u0167\u0168\7\66\2\2\u0168")
        buf.write("\u0169\t\2\2\2\u01699\3\2\2\2\u016a\u016b\5b\62\2\u016b")
        buf.write("\u016c\7\66\2\2\u016c\u016d\t\2\2\2\u016d\u016e\7\60\2")
        buf.write("\2\u016e\u016f\5\u0082B\2\u016f\u0170\7\61\2\2\u0170;")
        buf.write("\3\2\2\2\u0171\u0172\5b\62\2\u0172\u0173\7\34\2\2\u0173")
        buf.write("\u0174\t\2\2\2\u0174=\3\2\2\2\u0175\u0176\5b\62\2\u0176")
        buf.write("\u0177\7\34\2\2\u0177\u0178\t\2\2\2\u0178\u0179\7\60\2")
        buf.write("\2\u0179\u017a\5\u0082B\2\u017a\u017b\7\61\2\2\u017b?")
        buf.write("\3\2\2\2\u017c\u017f\5:\36\2\u017d\u017f\5> \2\u017e\u017c")
        buf.write("\3\2\2\2\u017e\u017d\3\2\2\2\u017fA\3\2\2\2\u0180\u0181")
        buf.write("\5@!\2\u0181\u0182\79\2\2\u0182C\3\2\2\2\u0183\u0184\7")
        buf.write("\3\2\2\u0184\u0185\79\2\2\u0185E\3\2\2\2\u0186\u0187\7")
        buf.write("\4\2\2\u0187\u0188\79\2\2\u0188G\3\2\2\2\u0189\u018c\5")
        buf.write("b\62\2\u018a\u018c\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018a")
        buf.write("\3\2\2\2\u018cI\3\2\2\2\u018d\u018e\7\22\2\2\u018e\u018f")
        buf.write("\5H%\2\u018f\u0190\79\2\2\u0190K\3\2\2\2\u0191\u0192\7")
        buf.write("\64\2\2\u0192\u0193\5R*\2\u0193\u0194\5 \21\2\u0194\u0195")
        buf.write("\5R*\2\u0195\u0196\7\65\2\2\u0196M\3\2\2\2\u0197\u0198")
        buf.write("\7\64\2\2\u0198\u0199\5R*\2\u0199\u019a\7\65\2\2\u019a")
        buf.write("O\3\2\2\2\u019b\u019c\7\64\2\2\u019c\u019d\5T+\2\u019d")
        buf.write("\u019e\7\65\2\2\u019eQ\3\2\2\2\u019f\u01a0\5V,\2\u01a0")
        buf.write("\u01a1\5R*\2\u01a1\u01a5\3\2\2\2\u01a2\u01a5\5V,\2\u01a3")
        buf.write("\u01a5\3\2\2\2\u01a4\u019f\3\2\2\2\u01a4\u01a2\3\2\2\2")
        buf.write("\u01a4\u01a3\3\2\2\2\u01a5S\3\2\2\2\u01a6\u01a7\5X-\2")
        buf.write("\u01a7\u01a8\5T+\2\u01a8\u01ac\3\2\2\2\u01a9\u01ac\5X")
        buf.write("-\2\u01aa\u01ac\3\2\2\2\u01ab\u01a6\3\2\2\2\u01ab\u01a9")
        buf.write("\3\2\2\2\u01ab\u01aa\3\2\2\2\u01acU\3\2\2\2\u01ad\u01b2")
        buf.write("\5\22\n\2\u01ae\u01b2\5\36\20\2\u01af\u01b2\5\f\7\2\u01b0")
        buf.write("\u01b2\5\16\b\2\u01b1\u01ad\3\2\2\2\u01b1\u01ae\3\2\2")
        buf.write("\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2W\3\2")
        buf.write("\2\2\u01b3\u01bd\5\30\r\2\u01b4\u01bd\5*\26\2\u01b5\u01bd")
        buf.write("\5,\27\2\u01b6\u01bd\5\66\34\2\u01b7\u01bd\5\"\22\2\u01b8")
        buf.write("\u01bd\5B\"\2\u01b9\u01bd\5D#\2\u01ba\u01bd\5F$\2\u01bb")
        buf.write("\u01bd\5J&\2\u01bc\u01b3\3\2\2\2\u01bc\u01b4\3\2\2\2\u01bc")
        buf.write("\u01b5\3\2\2\2\u01bc\u01b6\3\2\2\2\u01bc\u01b7\3\2\2\2")
        buf.write("\u01bc\u01b8\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01ba\3")
        buf.write("\2\2\2\u01bc\u01bb\3\2\2\2\u01bdY\3\2\2\2\u01be\u01bf")
        buf.write("\5\\/\2\u01bf\u01c0\5Z.\2\u01c0\u01c3\3\2\2\2\u01c1\u01c3")
        buf.write("\5\\/\2\u01c2\u01be\3\2\2\2\u01c2\u01c1\3\2\2\2\u01c3")
        buf.write("[\3\2\2\2\u01c4\u01c5\7\66\2\2\u01c5\u01cd\t\2\2\2\u01c6")
        buf.write("\u01c7\7\66\2\2\u01c7\u01c8\t\2\2\2\u01c8\u01c9\7\60\2")
        buf.write("\2\u01c9\u01ca\5\u0082B\2\u01ca\u01cb\7\61\2\2\u01cb\u01cd")
        buf.write("\3\2\2\2\u01cc\u01c4\3\2\2\2\u01cc\u01c6\3\2\2\2\u01cd")
        buf.write("]\3\2\2\2\u01ce\u01cf\5`\61\2\u01cf\u01d0\5^\60\2\u01d0")
        buf.write("\u01d3\3\2\2\2\u01d1\u01d3\5`\61\2\u01d2\u01ce\3\2\2\2")
        buf.write("\u01d2\u01d1\3\2\2\2\u01d3_\3\2\2\2\u01d4\u01d5\7\34\2")
        buf.write("\2\u01d5\u01dd\t\2\2\2\u01d6\u01d7\7\34\2\2\u01d7\u01d8")
        buf.write("\t\2\2\2\u01d8\u01d9\7\60\2\2\u01d9\u01da\5\u0082B\2\u01da")
        buf.write("\u01db\7\61\2\2\u01db\u01dd\3\2\2\2\u01dc\u01d4\3\2\2")
        buf.write("\2\u01dc\u01d6\3\2\2\2\u01dda\3\2\2\2\u01de\u01df\5d\63")
        buf.write("\2\u01df\u01e0\t\5\2\2\u01e0\u01e1\5d\63\2\u01e1\u01e4")
        buf.write("\3\2\2\2\u01e2\u01e4\5d\63\2\u01e3\u01de\3\2\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4c\3\2\2\2\u01e5\u01e6\5f\64\2\u01e6")
        buf.write("\u01e7\t\6\2\2\u01e7\u01e8\5f\64\2\u01e8\u01eb\3\2\2\2")
        buf.write("\u01e9\u01eb\5f\64\2\u01ea\u01e5\3\2\2\2\u01ea\u01e9\3")
        buf.write("\2\2\2\u01ebe\3\2\2\2\u01ec\u01ed\b\64\1\2\u01ed\u01ee")
        buf.write("\5h\65\2\u01ee\u01f4\3\2\2\2\u01ef\u01f0\f\4\2\2\u01f0")
        buf.write("\u01f1\t\7\2\2\u01f1\u01f3\5h\65\2\u01f2\u01ef\3\2\2\2")
        buf.write("\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3")
        buf.write("\2\2\2\u01f5g\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8")
        buf.write("\b\65\1\2\u01f8\u01f9\5j\66\2\u01f9\u01ff\3\2\2\2\u01fa")
        buf.write("\u01fb\f\4\2\2\u01fb\u01fc\t\b\2\2\u01fc\u01fe\5j\66\2")
        buf.write("\u01fd\u01fa\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3")
        buf.write("\2\2\2\u01ff\u0200\3\2\2\2\u0200i\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0202\u0203\b\66\1\2\u0203\u0204\5l\67\2\u0204")
        buf.write("\u020a\3\2\2\2\u0205\u0206\f\4\2\2\u0206\u0207\t\t\2\2")
        buf.write("\u0207\u0209\5l\67\2\u0208\u0205\3\2\2\2\u0209\u020c\3")
        buf.write("\2\2\2\u020a\u0208\3\2\2\2\u020a\u020b\3\2\2\2\u020bk")
        buf.write("\3\2\2\2\u020c\u020a\3\2\2\2\u020d\u020e\7$\2\2\u020e")
        buf.write("\u0211\5l\67\2\u020f\u0211\5n8\2\u0210\u020d\3\2\2\2\u0210")
        buf.write("\u020f\3\2\2\2\u0211m\3\2\2\2\u0212\u0213\7 \2\2\u0213")
        buf.write("\u0216\5n8\2\u0214\u0216\5p9\2\u0215\u0212\3\2\2\2\u0215")
        buf.write("\u0214\3\2\2\2\u0216o\3\2\2\2\u0217\u0218\b9\1\2\u0218")
        buf.write("\u0219\5r:\2\u0219\u021e\3\2\2\2\u021a\u021b\f\4\2\2\u021b")
        buf.write("\u021d\5|?\2\u021c\u021a\3\2\2\2\u021d\u0220\3\2\2\2\u021e")
        buf.write("\u021c\3\2\2\2\u021e\u021f\3\2\2\2\u021fq\3\2\2\2\u0220")
        buf.write("\u021e\3\2\2\2\u0221\u0222\b:\1\2\u0222\u0223\5t;\2\u0223")
        buf.write("\u0228\3\2\2\2\u0224\u0225\f\4\2\2\u0225\u0227\5Z.\2\u0226")
        buf.write("\u0224\3\2\2\2\u0227\u022a\3\2\2\2\u0228\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229s\3\2\2\2\u022a\u0228\3\2\2")
        buf.write("\2\u022b\u022c\t\2\2\2\u022c\u022f\5^\60\2\u022d\u022f")
        buf.write("\5v<\2\u022e\u022b\3\2\2\2\u022e\u022d\3\2\2\2\u022fu")
        buf.write("\3\2\2\2\u0230\u0231\7\31\2\2\u0231\u0232\5b\62\2\u0232")
        buf.write("\u0233\7\60\2\2\u0233\u0234\5\u0082B\2\u0234\u0235\7\61")
        buf.write("\2\2\u0235\u0238\3\2\2\2\u0236\u0238\5x=\2\u0237\u0230")
        buf.write("\3\2\2\2\u0237\u0236\3\2\2\2\u0238w\3\2\2\2\u0239\u023f")
        buf.write("\5\u0088E\2\u023a\u023f\7<\2\2\u023b\u023f\7=\2\2\u023c")
        buf.write("\u023f\7\33\2\2\u023d\u023f\5z>\2\u023e\u0239\3\2\2\2")
        buf.write("\u023e\u023a\3\2\2\2\u023e\u023b\3\2\2\2\u023e\u023c\3")
        buf.write("\2\2\2\u023e\u023d\3\2\2\2\u023fy\3\2\2\2\u0240\u0241")
        buf.write("\7\60\2\2\u0241\u0242\5b\62\2\u0242\u0243\7\61\2\2\u0243")
        buf.write("{\3\2\2\2\u0244\u0245\7\62\2\2\u0245\u0246\5b\62\2\u0246")
        buf.write("\u0247\7\63\2\2\u0247\u024e\3\2\2\2\u0248\u0249\7\62\2")
        buf.write("\2\u0249\u024a\5b\62\2\u024a\u024b\7\63\2\2\u024b\u024c")
        buf.write("\5|?\2\u024c\u024e\3\2\2\2\u024d\u0244\3\2\2\2\u024d\u0248")
        buf.write("\3\2\2\2\u024e}\3\2\2\2\u024f\u0254\5\u0080A\2\u0250\u0251")
        buf.write("\5\u0080A\2\u0251\u0252\5|?\2\u0252\u0254\3\2\2\2\u0253")
        buf.write("\u024f\3\2\2\2\u0253\u0250\3\2\2\2\u0254\177\3\2\2\2\u0255")
        buf.write("\u025c\t\2\2\2\u0256\u0257\5b\62\2\u0257\u0258\58\35\2")
        buf.write("\u0258\u0259\t\2\2\2\u0259\u025c\3\2\2\2\u025a\u025c\3")
        buf.write("\2\2\2\u025b\u0255\3\2\2\2\u025b\u0256\3\2\2\2\u025b\u025a")
        buf.write("\3\2\2\2\u025c\u0081\3\2\2\2\u025d\u025e\5b\62\2\u025e")
        buf.write("\u025f\7\67\2\2\u025f\u0260\5\u0082B\2\u0260\u0264\3\2")
        buf.write("\2\2\u0261\u0264\5b\62\2\u0262\u0264\3\2\2\2\u0263\u025d")
        buf.write("\3\2\2\2\u0263\u0261\3\2\2\2\u0263\u0262\3\2\2\2\u0264")
        buf.write("\u0083\3\2\2\2\u0265\u0266\7\f\2\2\u0266\u0267\7\60\2")
        buf.write("\2\u0267\u0268\5\u0086D\2\u0268\u0269\7\61\2\2\u0269\u0085")
        buf.write("\3\2\2\2\u026a\u026b\5b\62\2\u026b\u026c\7\67\2\2\u026c")
        buf.write("\u026d\5\u0086D\2\u026d\u0271\3\2\2\2\u026e\u0271\5b\62")
        buf.write("\2\u026f\u0271\3\2\2\2\u0270\u026a\3\2\2\2\u0270\u026e")
        buf.write("\3\2\2\2\u0270\u026f\3\2\2\2\u0271\u0087\3\2\2\2\u0272")
        buf.write("\u0278\7@\2\2\u0273\u0278\7?\2\2\u0274\u0278\7\t\2\2\u0275")
        buf.write("\u0278\7>\2\2\u0276\u0278\5\u0084C\2\u0277\u0272\3\2\2")
        buf.write("\2\u0277\u0273\3\2\2\2\u0277\u0274\3\2\2\2\u0277\u0275")
        buf.write("\3\2\2\2\u0277\u0276\3\2\2\2\u0278\u0089\3\2\2\2\u0279")
        buf.write("\u027a\5\u008cG\2\u027a\u027b\79\2\2\u027b\u027c\5\u008a")
        buf.write("F\2\u027c\u0280\3\2\2\2\u027d\u0280\5\u008cG\2\u027e\u0280")
        buf.write("\3\2\2\2\u027f\u0279\3\2\2\2\u027f\u027d\3\2\2\2\u027f")
        buf.write("\u027e\3\2\2\2\u0280\u008b\3\2\2\2\u0281\u0282\5\u008e")
        buf.write("H\2\u0282\u0283\78\2\2\u0283\u0284\5\u009cO\2\u0284\u008d")
        buf.write("\3\2\2\2\u0285\u0286\t\2\2\2\u0286\u0287\7\67\2\2\u0287")
        buf.write("\u028b\5\u008eH\2\u0288\u028b\t\2\2\2\u0289\u028b\3\2")
        buf.write("\2\2\u028a\u0285\3\2\2\2\u028a\u0288\3\2\2\2\u028a\u0289")
        buf.write("\3\2\2\2\u028b\u008f\3\2\2\2\u028c\u028d\7<\2\2\u028d")
        buf.write("\u028e\7\67\2\2\u028e\u0292\5\u0090I\2\u028f\u0292\7<")
        buf.write("\2\2\u0290\u0292\3\2\2\2\u0291\u028c\3\2\2\2\u0291\u028f")
        buf.write("\3\2\2\2\u0291\u0290\3\2\2\2\u0292\u0091\3\2\2\2\u0293")
        buf.write("\u0296\5\u0088E\2\u0294\u0296\5b\62\2\u0295\u0293\3\2")
        buf.write("\2\2\u0295\u0294\3\2\2\2\u0296\u0297\3\2\2\2\u0297\u0298")
        buf.write("\7\67\2\2\u0298\u0299\5\u0092J\2\u0299\u02a0\3\2\2\2\u029a")
        buf.write("\u029d\5\u0088E\2\u029b\u029d\5b\62\2\u029c\u029a\3\2")
        buf.write("\2\2\u029c\u029b\3\2\2\2\u029d\u02a0\3\2\2\2\u029e\u02a0")
        buf.write("\3\2\2\2\u029f\u0295\3\2\2\2\u029f\u029c\3\2\2\2\u029f")
        buf.write("\u029e\3\2\2\2\u02a0\u0093\3\2\2\2\u02a1\u02a2\7\f\2\2")
        buf.write("\u02a2\u02a3\7\62\2\2\u02a3\u02a4\5\u0096L\2\u02a4\u02a5")
        buf.write("\7\67\2\2\u02a5\u02a6\5\u0098M\2\u02a6\u02a7\7\63\2\2")
        buf.write("\u02a7\u0095\3\2\2\2\u02a8\u02ae\5\u0094K\2\u02a9\u02ae")
        buf.write("\7\16\2\2\u02aa\u02ae\7\17\2\2\u02ab\u02ae\7\20\2\2\u02ac")
        buf.write("\u02ae\7\21\2\2\u02ad\u02a8\3\2\2\2\u02ad\u02a9\3\2\2")
        buf.write("\2\u02ad\u02aa\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ac")
        buf.write("\3\2\2\2\u02ae\u0097\3\2\2\2\u02af\u02b0\7@\2\2\u02b0")
        buf.write("\u0099\3\2\2\2\u02b1\u02b2\t\n\2\2\u02b2\u009b\3\2\2\2")
        buf.write("\u02b3\u02b6\5\u009aN\2\u02b4\u02b6\5\u0094K\2\u02b5\u02b3")
        buf.write("\3\2\2\2\u02b5\u02b4\3\2\2\2\u02b6\u009d\3\2\2\2\66\u00a3")
        buf.write("\u00ae\u00b8\u00d1\u00dd\u00e9\u00f7\u0103\u0118\u0123")
        buf.write("\u012a\u0130\u0135\u0145\u014b\u0159\u017e\u018b\u01a4")
        buf.write("\u01ab\u01b1\u01bc\u01c2\u01cc\u01d2\u01dc\u01e3\u01ea")
        buf.write("\u01f4\u01ff\u020a\u0210\u0215\u021e\u0228\u022e\u0237")
        buf.write("\u023e\u024d\u0253\u025b\u0263\u0270\u0277\u027f\u028a")
        buf.write("\u0291\u0295\u029c\u029f\u02ad\u02b5")
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
                     "','", "':'", "';'", "'Program'", "'main'" ]

    symbolicNames = [ "<INVALID>", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "BOOLLIT", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", 
                      "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                      "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", 
                      "NOTEQUALOP", "GTE", "LTE", "GT", "LT", "STREQUALOP", 
                      "STRCONCATOP", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                      "DOT", "COMMA", "COLON", "SEMICOLON", "PROGRAM", "MAIN", 
                      "VARIABLE_IN_FUNC_IDENTIFIERS", "DOLLAR_IDENTIFIERS", 
                      "STRINGLIT", "FLOATLIT", "INTLIT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_main_program_declarations = 1
    RULE_class_declarations = 2
    RULE_class_declaration = 3
    RULE_class_inheritance = 4
    RULE_constructor_dclr = 5
    RULE_destructor_dclr = 6
    RULE_method_declaration = 7
    RULE_variable_declaration = 8
    RULE_declare_initiate_list = 9
    RULE_type_and_assign = 10
    RULE_variable_in_func_declaration = 11
    RULE_declare_initiate_in_func_list = 12
    RULE_type_and_assign_in_func = 13
    RULE_function_declaration = 14
    RULE_main_function_declaration = 15
    RULE_call_func_statement = 16
    RULE_call_funcs = 17
    RULE_call_func = 18
    RULE_call_func_attr_list = 19
    RULE_assignment_statements = 20
    RULE_if_statements = 21
    RULE_elseif_list_statements = 22
    RULE_elseif_statement = 23
    RULE_else_statement = 24
    RULE_by_expr = 25
    RULE_forin_statements = 26
    RULE_instance_attr_access = 27
    RULE_instance_method_access = 28
    RULE_static_attr_access = 29
    RULE_static_method_access = 30
    RULE_method_invocation = 31
    RULE_method_invocation_statement = 32
    RULE_break_statements = 33
    RULE_continue_statements = 34
    RULE_return_expr = 35
    RULE_return_statements = 36
    RULE_program_block_class_statements = 37
    RULE_block_class_statements = 38
    RULE_block_statements = 39
    RULE_statements_class = 40
    RULE_statements = 41
    RULE_statement_class = 42
    RULE_statement = 43
    RULE_instance_accesses = 44
    RULE_instance_access = 45
    RULE_static_accesses = 46
    RULE_static_access = 47
    RULE_expr = 48
    RULE_expr1 = 49
    RULE_expr2 = 50
    RULE_expr3 = 51
    RULE_expr4 = 52
    RULE_expr5 = 53
    RULE_expr6 = 54
    RULE_expr7 = 55
    RULE_expr8 = 56
    RULE_expr9 = 57
    RULE_expr10 = 58
    RULE_expr11 = 59
    RULE_expr12 = 60
    RULE_index_operators = 61
    RULE_index_expr = 62
    RULE_index = 63
    RULE_list_expr = 64
    RULE_array_lit = 65
    RULE_array_val = 66
    RULE_literal = 67
    RULE_list_parameters = 68
    RULE_param = 69
    RULE_identifier_list = 70
    RULE_variable_in_func_identifier_list = 71
    RULE_value_list = 72
    RULE_array_type = 73
    RULE_array_element_type = 74
    RULE_array_size = 75
    RULE_primitive_type = 76
    RULE_variable_type = 77

    ruleNames =  [ "program", "class_main_program_declarations", "class_declarations", 
                   "class_declaration", "class_inheritance", "constructor_dclr", 
                   "destructor_dclr", "method_declaration", "variable_declaration", 
                   "declare_initiate_list", "type_and_assign", "variable_in_func_declaration", 
                   "declare_initiate_in_func_list", "type_and_assign_in_func", 
                   "function_declaration", "main_function_declaration", 
                   "call_func_statement", "call_funcs", "call_func", "call_func_attr_list", 
                   "assignment_statements", "if_statements", "elseif_list_statements", 
                   "elseif_statement", "else_statement", "by_expr", "forin_statements", 
                   "instance_attr_access", "instance_method_access", "static_attr_access", 
                   "static_method_access", "method_invocation", "method_invocation_statement", 
                   "break_statements", "continue_statements", "return_expr", 
                   "return_statements", "program_block_class_statements", 
                   "block_class_statements", "block_statements", "statements_class", 
                   "statements", "statement_class", "statement", "instance_accesses", 
                   "instance_access", "static_accesses", "static_access", 
                   "expr", "expr1", "expr2", "expr3", "expr4", "expr5", 
                   "expr6", "expr7", "expr8", "expr9", "expr10", "expr11", 
                   "expr12", "index_operators", "index_expr", "index", "list_expr", 
                   "array_lit", "array_val", "literal", "list_parameters", 
                   "param", "identifier_list", "variable_in_func_identifier_list", 
                   "value_list", "array_type", "array_element_type", "array_size", 
                   "primitive_type", "variable_type" ]

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
    PROGRAM=56
    MAIN=57
    VARIABLE_IN_FUNC_IDENTIFIERS=58
    DOLLAR_IDENTIFIERS=59
    STRINGLIT=60
    FLOATLIT=61
    INTLIT=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64
    BLOCK_COMMENT=65
    WS=66
    ERROR_CHAR=67

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
            self.state = 159 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 156
                self.expr()
                self.state = 157
                self.match(D96Parser.COMMA)
                self.state = 161 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.MINUSOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_main_program_declarationsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def PROGRAM(self):
            return self.getToken(D96Parser.PROGRAM, 0)

        def program_block_class_statements(self):
            return self.getTypedRuleContext(D96Parser.Program_block_class_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_main_program_declarations




    def class_main_program_declarations(self):

        localctx = D96Parser.Class_main_program_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_main_program_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(D96Parser.CLASS)
            self.state = 164
            self.match(D96Parser.PROGRAM)
            self.state = 165
            self.program_block_class_statements()
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
        self.enterRule(localctx, 4, self.RULE_class_declarations)
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
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
        self.enterRule(localctx, 6, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(D96Parser.CLASS)
            self.state = 175
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 176
            self.class_inheritance()
            self.state = 177
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
        self.enterRule(localctx, 8, self.RULE_class_inheritance)
        try:
            self.state = 182
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.match(D96Parser.COLON)
                self.state = 180
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
        self.enterRule(localctx, 10, self.RULE_constructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 185
            self.match(D96Parser.LB)
            self.state = 186
            self.list_parameters()
            self.state = 187
            self.match(D96Parser.RB)
            self.state = 188
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
        self.enterRule(localctx, 12, self.RULE_destructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(D96Parser.DESTRUCTOR)
            self.state = 191
            self.match(D96Parser.LB)
            self.state = 192
            self.match(D96Parser.RB)
            self.state = 193
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
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 196
            self.match(D96Parser.LB)
            self.state = 197
            self.list_parameters()
            self.state = 198
            self.match(D96Parser.RB)
            self.state = 199
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
        self.enterRule(localctx, 16, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 202
                self.declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 203
                self.identifier_list()
                self.state = 204
                self.match(D96Parser.COLON)
                self.state = 205
                self.variable_type()
                pass


            self.state = 209
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
        self.enterRule(localctx, 18, self.RULE_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 212
                self.type_and_assign()
                self.state = 213
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.identifier_list()
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
        self.enterRule(localctx, 20, self.RULE_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(D96Parser.COMMA)
                self.state = 222
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.type_and_assign()
                self.state = 224
                self.expr()
                self.state = 225
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
                self.match(D96Parser.COLON)
                self.state = 228
                self.variable_type()
                self.state = 229
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
        self.enterRule(localctx, 22, self.RULE_variable_in_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 234
            self.declare_initiate_in_func_list()
            self.state = 235
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

        def type_and_assign_in_func(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assign_in_funcContext,0)


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
            return D96Parser.RULE_declare_initiate_in_func_list




    def declare_initiate_in_func_list(self):

        localctx = D96Parser.Declare_initiate_in_func_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declare_initiate_in_func_list)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 238
                self.type_and_assign_in_func()
                self.state = 239
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.variable_in_func_identifier_list()
                self.state = 242
                self.match(D96Parser.COLON)
                self.state = 243
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

        def type_and_assign_in_func(self):
            return self.getTypedRuleContext(D96Parser.Type_and_assign_in_funcContext,0)


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
            return D96Parser.RULE_type_and_assign_in_func




    def type_and_assign_in_func(self):

        localctx = D96Parser.Type_and_assign_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_and_assign_in_func)
        self._la = 0 # Token type
        try:
            self.state = 257
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 247
                self.match(D96Parser.COMMA)
                self.state = 248
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 249
                self.type_and_assign_in_func()
                self.state = 250
                self.expr()
                self.state = 251
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
                self.match(D96Parser.COLON)
                self.state = 254
                self.variable_type()
                self.state = 255
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
        self.enterRule(localctx, 28, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 260
            self.match(D96Parser.LB)
            self.state = 261
            self.list_parameters()
            self.state = 262
            self.match(D96Parser.RB)
            self.state = 263
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_function_declarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(D96Parser.MAIN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_main_function_declaration




    def main_function_declaration(self):

        localctx = D96Parser.Main_function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_main_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.match(D96Parser.MAIN)
            self.state = 266
            self.match(D96Parser.LB)
            self.state = 267
            self.match(D96Parser.RB)
            self.state = 268
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

        def call_funcs(self):
            return self.getTypedRuleContext(D96Parser.Call_funcsContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func_statement




    def call_func_statement(self):

        localctx = D96Parser.Call_func_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.call_funcs()
            self.state = 271
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_funcsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func(self):
            return self.getTypedRuleContext(D96Parser.Call_funcContext,0)


        def call_funcs(self):
            return self.getTypedRuleContext(D96Parser.Call_funcsContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_funcs




    def call_funcs(self):

        localctx = D96Parser.Call_funcsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_call_funcs)
        self._la = 0 # Token type
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.call_func()
                self.state = 274
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOUBLECOLONOP or _la==D96Parser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.call_funcs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.call_func()
                pass


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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def call_func_attr_list(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attr_listContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func




    def call_func(self):

        localctx = D96Parser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call_func)
        self._la = 0 # Token type
        try:
            self.state = 296
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                self.match(D96Parser.LB)
                self.state = 282
                self.value_list()
                self.state = 283
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 289
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                if la_ == 1:
                    self.state = 285
                    self.call_func_attr_list()
                    self.state = 286
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.DOUBLECOLONOP or _la==D96Parser.DOT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    pass

                elif la_ == 2:
                    pass


                self.state = 291
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 292
                self.match(D96Parser.LB)
                self.state = 293
                self.value_list()
                self.state = 294
                self.match(D96Parser.RB)
                pass


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

        def call_func_attr_list(self):
            return self.getTypedRuleContext(D96Parser.Call_func_attr_listContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_call_func_attr_list




    def call_func_attr_list(self):

        localctx = D96Parser.Call_func_attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call_func_attr_list)
        self._la = 0 # Token type
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
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
                _la = self._input.LA(1)
                if not(_la==D96Parser.DOUBLECOLONOP or _la==D96Parser.DOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 300
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


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

        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statements




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 304
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 305
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.state = 306
                self.expr()
                pass


            self.state = 309
            self.match(D96Parser.ASSIGNOP)
            self.state = 310
            self.expr()
            self.state = 311
            self.match(D96Parser.SEMICOLON)
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
        self.enterRule(localctx, 42, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(D96Parser.IF)
            self.state = 314
            self.match(D96Parser.LB)
            self.state = 315
            self.expr()
            self.state = 316
            self.match(D96Parser.RB)
            self.state = 317
            self.block_statements()
            self.state = 323
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 318
                self.elseif_list_statements()
                self.state = 319
                self.else_statement()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 321
                self.else_statement()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.RCB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
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
        self.enterRule(localctx, 44, self.RULE_elseif_list_statements)
        try:
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.elseif_statement()
                self.state = 326
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 328
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
        self.enterRule(localctx, 46, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(D96Parser.ELSEIF)
            self.state = 332
            self.match(D96Parser.LB)
            self.state = 333
            self.expr()
            self.state = 334
            self.match(D96Parser.RB)
            self.state = 335
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
        self.enterRule(localctx, 48, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(D96Parser.ELSE)
            self.state = 338
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
        self.enterRule(localctx, 50, self.RULE_by_expr)
        try:
            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.match(D96Parser.BY)
                self.state = 341
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
        self.enterRule(localctx, 52, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 345
            self.match(D96Parser.FOREACH)
            self.state = 346
            self.match(D96Parser.LB)
            self.state = 347
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 348
            self.match(D96Parser.IN)
            self.state = 349
            self.expr()
            self.state = 350
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 351
            self.expr()
            self.state = 352
            self.by_expr()
            self.state = 353
            self.match(D96Parser.RB)
            self.state = 354
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
        self.enterRule(localctx, 54, self.RULE_instance_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 356
            self.expr()
            self.state = 357
            self.match(D96Parser.DOT)
            self.state = 358
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
        self.enterRule(localctx, 56, self.RULE_instance_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.expr()
            self.state = 361
            self.match(D96Parser.DOT)
            self.state = 362
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 363
            self.match(D96Parser.LB)
            self.state = 364
            self.list_expr()
            self.state = 365
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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr_access




    def static_attr_access(self):

        localctx = D96Parser.Static_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.expr()
            self.state = 368
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 369
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


    class Static_method_accessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

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
            return D96Parser.RULE_static_method_access




    def static_method_access(self):

        localctx = D96Parser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.expr()
            self.state = 372
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 373
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 374
            self.match(D96Parser.LB)
            self.state = 375
            self.list_expr()
            self.state = 376
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
        self.enterRule(localctx, 62, self.RULE_method_invocation)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 378
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 379
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
        self.enterRule(localctx, 64, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.method_invocation()
            self.state = 383
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
        self.enterRule(localctx, 66, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(D96Parser.BREAK)
            self.state = 386
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
        self.enterRule(localctx, 68, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.match(D96Parser.CONTINUE)
            self.state = 389
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
        self.enterRule(localctx, 70, self.RULE_return_expr)
        try:
            self.state = 393
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 391
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
        self.enterRule(localctx, 72, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(D96Parser.RETURN)
            self.state = 396
            self.return_expr()
            self.state = 397
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_block_class_statementsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def statements_class(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Statements_classContext)
            else:
                return self.getTypedRuleContext(D96Parser.Statements_classContext,i)


        def main_function_declaration(self):
            return self.getTypedRuleContext(D96Parser.Main_function_declarationContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_program_block_class_statements




    def program_block_class_statements(self):

        localctx = D96Parser.Program_block_class_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_program_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(D96Parser.LCB)
            self.state = 400
            self.statements_class()
            self.state = 401
            self.main_function_declaration()
            self.state = 402
            self.statements_class()
            self.state = 403
            self.match(D96Parser.RCB)
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
            self.state = 405
            self.match(D96Parser.LCB)
            self.state = 406
            self.statements_class()
            self.state = 407
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
            self.state = 409
            self.match(D96Parser.LCB)
            self.state = 410
            self.statements()
            self.state = 411
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
            self.state = 418
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.statement_class()
                self.state = 414
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 416
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
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 420
                self.statement()
                self.state = 421
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
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
        self.enterRule(localctx, 84, self.RULE_statement_class)
        try:
            self.state = 431
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.variable_declaration()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.function_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.constructor_dclr()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
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
        self.enterRule(localctx, 86, self.RULE_statement)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 433
                self.variable_in_func_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 435
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 436
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 437
                self.call_func_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 438
                self.method_invocation_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 439
                self.break_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 440
                self.continue_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 441
                self.return_statements()
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
        self.enterRule(localctx, 88, self.RULE_instance_accesses)
        try:
            self.state = 448
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.instance_access()
                self.state = 445
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
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
        self.enterRule(localctx, 90, self.RULE_instance_access)
        self._la = 0 # Token type
        try:
            self.state = 458
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(D96Parser.DOT)
                self.state = 451
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 452
                self.match(D96Parser.DOT)
                self.state = 453
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 454
                self.match(D96Parser.LB)
                self.state = 455
                self.list_expr()
                self.state = 456
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
        self.enterRule(localctx, 92, self.RULE_static_accesses)
        try:
            self.state = 464
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 460
                self.static_access()
                self.state = 461
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 463
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
            return D96Parser.RULE_static_access




    def static_access(self):

        localctx = D96Parser.Static_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_static_access)
        self._la = 0 # Token type
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 467
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 469
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 470
                self.match(D96Parser.LB)
                self.state = 471
                self.list_expr()
                self.state = 472
                self.match(D96Parser.RB)
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
        self.enterRule(localctx, 96, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 476
                self.expr1()
                self.state = 477
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 478
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 480
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
        self.enterRule(localctx, 98, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 483
                self.expr2(0)
                self.state = 484
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 485
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 487
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
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 498
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 493
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 494
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 495
                    self.expr3(0) 
                self.state = 500
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 509
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 504
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 505
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 506
                    self.expr4(0) 
                self.state = 511
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 520
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 515
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 516
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 517
                    self.expr5() 
                self.state = 522
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 106, self.RULE_expr5)
        try:
            self.state = 526
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.match(D96Parser.NOTOP)
                self.state = 524
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 525
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
        self.enterRule(localctx, 108, self.RULE_expr6)
        try:
            self.state = 531
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(D96Parser.MINUSOP)
                self.state = 529
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 530
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
        _startState = 110
        self.enterRecursionRule(localctx, 110, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 540
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 536
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 537
                    self.index_operators() 
                self.state = 542
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 546
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 547
                    self.instance_accesses() 
                self.state = 552
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

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
        self.enterRule(localctx, 114, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 556
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 554
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
        self.enterRule(localctx, 116, self.RULE_expr10)
        try:
            self.state = 565
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 558
                self.match(D96Parser.NEW)
                self.state = 559
                self.expr()
                self.state = 560
                self.match(D96Parser.LB)
                self.state = 561
                self.list_expr()
                self.state = 562
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 564
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
        self.enterRule(localctx, 118, self.RULE_expr11)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 567
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 569
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 570
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 5)
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
        self.enterRule(localctx, 120, self.RULE_expr12)
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




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_index_operators)
        try:
            self.state = 587
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 578
                self.match(D96Parser.LSB)
                self.state = 579
                self.expr()
                self.state = 580
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 582
                self.match(D96Parser.LSB)
                self.state = 583
                self.expr()
                self.state = 584
                self.match(D96Parser.RSB)
                self.state = 585
                self.index_operators()
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
        self.enterRule(localctx, 124, self.RULE_index_expr)
        try:
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 589
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 590
                self.index()
                self.state = 591
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
        self.enterRule(localctx, 126, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 595
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.expr()
                self.state = 597
                self.instance_attr_access()
                self.state = 598
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
        self.enterRule(localctx, 128, self.RULE_list_expr)
        try:
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 603
                self.expr()
                self.state = 604
                self.match(D96Parser.COMMA)
                self.state = 605
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 607
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
        self.enterRule(localctx, 130, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(D96Parser.ARRAY)
            self.state = 612
            self.match(D96Parser.LB)
            self.state = 613
            self.array_val()
            self.state = 614
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
        self.enterRule(localctx, 132, self.RULE_array_val)
        try:
            self.state = 622
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 616
                self.expr()
                self.state = 617
                self.match(D96Parser.COMMA)
                self.state = 618
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
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
        self.enterRule(localctx, 134, self.RULE_literal)
        try:
            self.state = 629
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 624
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 625
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 626
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 627
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 628
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
        self.enterRule(localctx, 136, self.RULE_list_parameters)
        try:
            self.state = 637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 631
                self.param()
                self.state = 632
                self.match(D96Parser.SEMICOLON)
                self.state = 633
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 635
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
        self.enterRule(localctx, 138, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 639
            self.identifier_list()
            self.state = 640
            self.match(D96Parser.COLON)
            self.state = 641
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
        self.enterRule(localctx, 140, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 648
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 643
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 644
                self.match(D96Parser.COMMA)
                self.state = 645
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 646
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
        self.enterRule(localctx, 142, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 655
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 650
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 651
                self.match(D96Parser.COMMA)
                self.state = 652
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 653
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
        self.enterRule(localctx, 144, self.RULE_value_list)
        try:
            self.state = 669
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 657
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 658
                    self.expr()
                    pass


                self.state = 661
                self.match(D96Parser.COMMA)
                self.state = 662
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 666
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 664
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 665
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

        def array_size(self):
            return self.getTypedRuleContext(D96Parser.Array_sizeContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_type




    def array_type(self):

        localctx = D96Parser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 671
            self.match(D96Parser.ARRAY)
            self.state = 672
            self.match(D96Parser.LSB)
            self.state = 673
            self.array_element_type()
            self.state = 674
            self.match(D96Parser.COMMA)
            self.state = 675
            self.array_size()
            self.state = 676
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
        self.enterRule(localctx, 148, self.RULE_array_element_type)
        try:
            self.state = 683
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 679
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 680
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 681
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 682
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


    class Array_sizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_size




    def array_size(self):

        localctx = D96Parser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.match(D96Parser.INTLIT)
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
        self.enterRule(localctx, 152, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
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
        self.enterRule(localctx, 154, self.RULE_variable_type)
        try:
            self.state = 691
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 689
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 690
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
        self._predicates[50] = self.expr2_sempred
        self._predicates[51] = self.expr3_sempred
        self._predicates[52] = self.expr4_sempred
        self._predicates[55] = self.expr7_sempred
        self._predicates[56] = self.expr8_sempred
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
         




