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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3E")
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
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\6\2\u00a8\n")
        buf.write("\2\r\2\16\2\u00a9\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4")
        buf.write("\5\4\u00b5\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u00bf")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00d8\n")
        buf.write("\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u00e4\n\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5")
        buf.write("\f\u00f0\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\5\16\u00fe\n\16\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\3\17\5\17\u010a\n\17\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\5\23\u011e\n\23\3\24\3\24\3")
        buf.write("\24\3\24\5\24\u0124\n\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\25\5\25\u0132\n\25\5\25\u0134")
        buf.write("\n\25\3\26\3\26\3\26\3\26\5\26\u013a\n\26\3\27\3\27\3")
        buf.write("\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write("\u0148\n\30\5\30\u014a\n\30\3\30\3\30\5\30\u014e\n\30")
        buf.write("\3\31\3\31\3\31\3\31\5\31\u0154\n\31\3\32\3\32\3\32\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0160\n\32\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u0166\n\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\35\3\35\3\35\3\36\3\36\3\36\5\36\u0174\n\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\3#\3#\3#\3#\3$\3$\5$\u0199\n$\3%\3%\3%\3&\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\5(\u01a6\n(\3)\3)\3)\3)\3*\3*\3*\3*\3")
        buf.write("*\3*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\5.\u01c5\n.\3/\3/\3/\3/\3/\5/\u01cc\n/\3\60\3")
        buf.write("\60\3\60\3\60\5\60\u01d2\n\60\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\5\61\u01dd\n\61\3\62\3\62\3\62\3")
        buf.write("\62\3\62\5\62\u01e4\n\62\3\63\3\63\3\63\3\63\3\63\5\63")
        buf.write("\u01eb\n\63\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u01f3\n")
        buf.write("\64\f\64\16\64\u01f6\13\64\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\7\65\u01fe\n\65\f\65\16\65\u0201\13\65\3\66\3\66\3")
        buf.write("\66\3\66\3\66\3\66\7\66\u0209\n\66\f\66\16\66\u020c\13")
        buf.write("\66\3\67\3\67\3\67\5\67\u0211\n\67\38\38\38\58\u0216\n")
        buf.write("8\39\39\39\39\39\79\u021d\n9\f9\169\u0220\139\3:\3:\3")
        buf.write(":\3:\3:\3:\5:\u0228\n:\3:\7:\u022b\n:\f:\16:\u022e\13")
        buf.write(":\3;\3;\3;\5;\u0233\n;\3<\3<\3<\3<\3<\3<\3<\5<\u023c\n")
        buf.write("<\3=\3=\3=\3=\3=\5=\u0243\n=\3>\3>\3>\3>\3?\3?\3?\3?\3")
        buf.write("?\3?\3?\3?\3?\5?\u0252\n?\3@\3@\3@\3@\5@\u0258\n@\3A\3")
        buf.write("A\3A\3A\3A\3A\5A\u0260\nA\3B\3B\3B\3B\5B\u0266\nB\3C\3")
        buf.write("C\3C\3C\3C\3C\3C\3C\5C\u0270\nC\3D\3D\3D\3D\5D\u0276\n")
        buf.write("D\3E\3E\3E\3E\3E\3E\3E\3E\5E\u0280\nE\3F\3F\3F\3F\3F\3")
        buf.write("F\5F\u0288\nF\3G\3G\3G\3G\3G\3H\3H\3H\3H\3H\3H\5H\u0295")
        buf.write("\nH\3I\3I\3I\3I\3I\5I\u029c\nI\3J\3J\3J\3J\3J\3J\5J\u02a4")
        buf.write("\nJ\3K\3K\3K\3K\3L\3L\3L\3L\3L\5L\u02af\nL\3M\3M\3M\3")
        buf.write("M\3M\5M\u02b6\nM\3N\3N\5N\u02ba\nN\3N\3N\3N\3N\3N\5N\u02c1")
        buf.write("\nN\3N\5N\u02c4\nN\3O\3O\3O\3O\3O\3O\3O\3P\3P\3P\3P\3")
        buf.write("P\5P\u02d2\nP\3Q\3Q\3R\3R\3S\3S\5S\u02da\nS\3S\2\7fhj")
        buf.write("prT\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60")
        buf.write("\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\2\n\3")
        buf.write("\2<=\3\2\25\26\3\2./\4\2\'\')-\3\2%&\3\2\37 \3\2!#\3\2")
        buf.write("\16\21\2\u02e2\2\u00a7\3\2\2\2\4\u00ab\3\2\2\2\6\u00b4")
        buf.write("\3\2\2\2\b\u00b6\3\2\2\2\n\u00be\3\2\2\2\f\u00c0\3\2\2")
        buf.write("\2\16\u00c6\3\2\2\2\20\u00cb\3\2\2\2\22\u00d1\3\2\2\2")
        buf.write("\24\u00e3\3\2\2\2\26\u00ef\3\2\2\2\30\u00f1\3\2\2\2\32")
        buf.write("\u00fd\3\2\2\2\34\u0109\3\2\2\2\36\u010b\3\2\2\2 \u0111")
        buf.write("\3\2\2\2\"\u0116\3\2\2\2$\u011d\3\2\2\2&\u0123\3\2\2\2")
        buf.write("(\u0133\3\2\2\2*\u0139\3\2\2\2,\u013b\3\2\2\2.\u0149\3")
        buf.write("\2\2\2\60\u0153\3\2\2\2\62\u0155\3\2\2\2\64\u0165\3\2")
        buf.write("\2\2\66\u0167\3\2\2\28\u016d\3\2\2\2:\u0173\3\2\2\2<\u0175")
        buf.write("\3\2\2\2>\u0180\3\2\2\2@\u0184\3\2\2\2B\u018b\3\2\2\2")
        buf.write("D\u018f\3\2\2\2F\u0198\3\2\2\2H\u019a\3\2\2\2J\u019d\3")
        buf.write("\2\2\2L\u01a0\3\2\2\2N\u01a5\3\2\2\2P\u01a7\3\2\2\2R\u01ab")
        buf.write("\3\2\2\2T\u01b1\3\2\2\2V\u01b5\3\2\2\2X\u01b9\3\2\2\2")
        buf.write("Z\u01c4\3\2\2\2\\\u01cb\3\2\2\2^\u01d1\3\2\2\2`\u01dc")
        buf.write("\3\2\2\2b\u01e3\3\2\2\2d\u01ea\3\2\2\2f\u01ec\3\2\2\2")
        buf.write("h\u01f7\3\2\2\2j\u0202\3\2\2\2l\u0210\3\2\2\2n\u0215\3")
        buf.write("\2\2\2p\u0217\3\2\2\2r\u0221\3\2\2\2t\u0232\3\2\2\2v\u023b")
        buf.write("\3\2\2\2x\u0242\3\2\2\2z\u0244\3\2\2\2|\u0251\3\2\2\2")
        buf.write("~\u0257\3\2\2\2\u0080\u025f\3\2\2\2\u0082\u0265\3\2\2")
        buf.write("\2\u0084\u026f\3\2\2\2\u0086\u0275\3\2\2\2\u0088\u027f")
        buf.write("\3\2\2\2\u008a\u0287\3\2\2\2\u008c\u0289\3\2\2\2\u008e")
        buf.write("\u0294\3\2\2\2\u0090\u029b\3\2\2\2\u0092\u02a3\3\2\2\2")
        buf.write("\u0094\u02a5\3\2\2\2\u0096\u02ae\3\2\2\2\u0098\u02b5\3")
        buf.write("\2\2\2\u009a\u02c3\3\2\2\2\u009c\u02c5\3\2\2\2\u009e\u02d1")
        buf.write("\3\2\2\2\u00a0\u02d3\3\2\2\2\u00a2\u02d5\3\2\2\2\u00a4")
        buf.write("\u02d9\3\2\2\2\u00a6\u00a8\5,\27\2\u00a7\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\3\3\2\2\2\u00ab\u00ac\7\24\2\2\u00ac\u00ad")
        buf.write("\7:\2\2\u00ad\u00ae\5R*\2\u00ae\5\3\2\2\2\u00af\u00b0")
        buf.write("\5\b\5\2\u00b0\u00b1\5\6\4\2\u00b1\u00b5\3\2\2\2\u00b2")
        buf.write("\u00b5\5\b\5\2\u00b3\u00b5\3\2\2\2\u00b4\u00af\3\2\2\2")
        buf.write("\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\7\3\2\2")
        buf.write("\2\u00b6\u00b7\7\24\2\2\u00b7\u00b8\7<\2\2\u00b8\u00b9")
        buf.write("\5\n\6\2\u00b9\u00ba\5T+\2\u00ba\t\3\2\2\2\u00bb\u00bc")
        buf.write("\78\2\2\u00bc\u00bf\7<\2\2\u00bd\u00bf\3\2\2\2\u00be\u00bb")
        buf.write("\3\2\2\2\u00be\u00bd\3\2\2\2\u00bf\13\3\2\2\2\u00c0\u00c1")
        buf.write("\7\27\2\2\u00c1\u00c2\7\60\2\2\u00c2\u00c3\5\u0092J\2")
        buf.write("\u00c3\u00c4\7\61\2\2\u00c4\u00c5\5V,\2\u00c5\r\3\2\2")
        buf.write("\2\u00c6\u00c7\7\30\2\2\u00c7\u00c8\7\60\2\2\u00c8\u00c9")
        buf.write("\7\61\2\2\u00c9\u00ca\5V,\2\u00ca\17\3\2\2\2\u00cb\u00cc")
        buf.write("\t\2\2\2\u00cc\u00cd\7\60\2\2\u00cd\u00ce\5\u0092J\2\u00ce")
        buf.write("\u00cf\7\61\2\2\u00cf\u00d0\5V,\2\u00d0\21\3\2\2\2\u00d1")
        buf.write("\u00d7\t\3\2\2\u00d2\u00d8\5\24\13\2\u00d3\u00d4\5\u0096")
        buf.write("L\2\u00d4\u00d5\78\2\2\u00d5\u00d6\5\u00a4S\2\u00d6\u00d8")
        buf.write("\3\2\2\2\u00d7\u00d2\3\2\2\2\u00d7\u00d3\3\2\2\2\u00d8")
        buf.write("\u00d9\3\2\2\2\u00d9\u00da\79\2\2\u00da\23\3\2\2\2\u00db")
        buf.write("\u00dc\t\2\2\2\u00dc\u00dd\5\26\f\2\u00dd\u00de\5b\62")
        buf.write("\2\u00de\u00e4\3\2\2\2\u00df\u00e0\5\u0096L\2\u00e0\u00e1")
        buf.write("\78\2\2\u00e1\u00e2\5\u00a4S\2\u00e2\u00e4\3\2\2\2\u00e3")
        buf.write("\u00db\3\2\2\2\u00e3\u00df\3\2\2\2\u00e4\25\3\2\2\2\u00e5")
        buf.write("\u00e6\7\67\2\2\u00e6\u00e7\t\2\2\2\u00e7\u00e8\5\26\f")
        buf.write("\2\u00e8\u00e9\5b\62\2\u00e9\u00ea\7\67\2\2\u00ea\u00f0")
        buf.write("\3\2\2\2\u00eb\u00ec\78\2\2\u00ec\u00ed\5\u00a4S\2\u00ed")
        buf.write("\u00ee\7(\2\2\u00ee\u00f0\3\2\2\2\u00ef\u00e5\3\2\2\2")
        buf.write("\u00ef\u00eb\3\2\2\2\u00f0\27\3\2\2\2\u00f1\u00f2\t\3")
        buf.write("\2\2\u00f2\u00f3\5\32\16\2\u00f3\u00f4\79\2\2\u00f4\31")
        buf.write("\3\2\2\2\u00f5\u00f6\7<\2\2\u00f6\u00f7\5\34\17\2\u00f7")
        buf.write("\u00f8\5b\62\2\u00f8\u00fe\3\2\2\2\u00f9\u00fa\5\u0098")
        buf.write("M\2\u00fa\u00fb\78\2\2\u00fb\u00fc\5\u00a4S\2\u00fc\u00fe")
        buf.write("\3\2\2\2\u00fd\u00f5\3\2\2\2\u00fd\u00f9\3\2\2\2\u00fe")
        buf.write("\33\3\2\2\2\u00ff\u0100\7\67\2\2\u0100\u0101\7<\2\2\u0101")
        buf.write("\u0102\5\34\17\2\u0102\u0103\5b\62\2\u0103\u0104\7\67")
        buf.write("\2\2\u0104\u010a\3\2\2\2\u0105\u0106\78\2\2\u0106\u0107")
        buf.write("\5\u00a4S\2\u0107\u0108\7(\2\2\u0108\u010a\3\2\2\2\u0109")
        buf.write("\u00ff\3\2\2\2\u0109\u0105\3\2\2\2\u010a\35\3\2\2\2\u010b")
        buf.write("\u010c\t\2\2\2\u010c\u010d\7\60\2\2\u010d\u010e\5\u0092")
        buf.write("J\2\u010e\u010f\7\61\2\2\u010f\u0110\5V,\2\u0110\37\3")
        buf.write("\2\2\2\u0111\u0112\7;\2\2\u0112\u0113\7\60\2\2\u0113\u0114")
        buf.write("\7\61\2\2\u0114\u0115\5X-\2\u0115!\3\2\2\2\u0116\u0117")
        buf.write("\5&\24\2\u0117\u0118\79\2\2\u0118#\3\2\2\2\u0119\u011a")
        buf.write("\7\66\2\2\u011a\u011e\t\2\2\2\u011b\u011c\7\34\2\2\u011c")
        buf.write("\u011e\7=\2\2\u011d\u0119\3\2\2\2\u011d\u011b\3\2\2\2")
        buf.write("\u011e%\3\2\2\2\u011f\u0120\5(\25\2\u0120\u0121\5&\24")
        buf.write("\2\u0121\u0124\3\2\2\2\u0122\u0124\5(\25\2\u0123\u011f")
        buf.write("\3\2\2\2\u0123\u0122\3\2\2\2\u0124\'\3\2\2\2\u0125\u0126")
        buf.write("\t\2\2\2\u0126\u0127\7\60\2\2\u0127\u0128\5\u009aN\2\u0128")
        buf.write("\u0129\7\61\2\2\u0129\u012a\5(\25\2\u012a\u0134\3\2\2")
        buf.write("\2\u012b\u0131\5$\23\2\u012c\u012d\7\60\2\2\u012d\u012e")
        buf.write("\5\u009aN\2\u012e\u012f\7\61\2\2\u012f\u0132\3\2\2\2\u0130")
        buf.write("\u0132\3\2\2\2\u0131\u012c\3\2\2\2\u0131\u0130\3\2\2\2")
        buf.write("\u0132\u0134\3\2\2\2\u0133\u0125\3\2\2\2\u0133\u012b\3")
        buf.write("\2\2\2\u0134)\3\2\2\2\u0135\u0136\5$\23\2\u0136\u0137")
        buf.write("\5*\26\2\u0137\u013a\3\2\2\2\u0138\u013a\5$\23\2\u0139")
        buf.write("\u0135\3\2\2\2\u0139\u0138\3\2\2\2\u013a+\3\2\2\2\u013b")
        buf.write("\u013c\5.\30\2\u013c\u013d\7(\2\2\u013d\u013e\5b\62\2")
        buf.write("\u013e\u013f\79\2\2\u013f-\3\2\2\2\u0140\u014a\7<\2\2")
        buf.write("\u0141\u014a\7=\2\2\u0142\u014a\5> \2\u0143\u014a\5B\"")
        buf.write("\2\u0144\u0147\5&\24\2\u0145\u0148\5\60\31\2\u0146\u0148")
        buf.write("\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write("\u014a\3\2\2\2\u0149\u0140\3\2\2\2\u0149\u0141\3\2\2\2")
        buf.write("\u0149\u0142\3\2\2\2\u0149\u0143\3\2\2\2\u0149\u0144\3")
        buf.write("\2\2\2\u014a\u014d\3\2\2\2\u014b\u014e\5|?\2\u014c\u014e")
        buf.write("\3\2\2\2\u014d\u014b\3\2\2\2\u014d\u014c\3\2\2\2\u014e")
        buf.write("/\3\2\2\2\u014f\u0150\5$\23\2\u0150\u0151\5\60\31\2\u0151")
        buf.write("\u0154\3\2\2\2\u0152\u0154\5$\23\2\u0153\u014f\3\2\2\2")
        buf.write("\u0153\u0152\3\2\2\2\u0154\61\3\2\2\2\u0155\u0156\7\5")
        buf.write("\2\2\u0156\u0157\7\60\2\2\u0157\u0158\5b\62\2\u0158\u0159")
        buf.write("\7\61\2\2\u0159\u015f\5V,\2\u015a\u015b\5\64\33\2\u015b")
        buf.write("\u015c\58\35\2\u015c\u0160\3\2\2\2\u015d\u0160\58\35\2")
        buf.write("\u015e\u0160\3\2\2\2\u015f\u015a\3\2\2\2\u015f\u015d\3")
        buf.write("\2\2\2\u015f\u015e\3\2\2\2\u0160\63\3\2\2\2\u0161\u0162")
        buf.write("\5\66\34\2\u0162\u0163\5\64\33\2\u0163\u0166\3\2\2\2\u0164")
        buf.write("\u0166\5\66\34\2\u0165\u0161\3\2\2\2\u0165\u0164\3\2\2")
        buf.write("\2\u0166\65\3\2\2\2\u0167\u0168\7\6\2\2\u0168\u0169\7")
        buf.write("\60\2\2\u0169\u016a\5b\62\2\u016a\u016b\7\61\2\2\u016b")
        buf.write("\u016c\5V,\2\u016c\67\3\2\2\2\u016d\u016e\7\7\2\2\u016e")
        buf.write("\u016f\5V,\2\u016f9\3\2\2\2\u0170\u0171\7\32\2\2\u0171")
        buf.write("\u0174\5b\62\2\u0172\u0174\3\2\2\2\u0173\u0170\3\2\2\2")
        buf.write("\u0173\u0172\3\2\2\2\u0174;\3\2\2\2\u0175\u0176\7\b\2")
        buf.write("\2\u0176\u0177\7\60\2\2\u0177\u0178\t\2\2\2\u0178\u0179")
        buf.write("\7\r\2\2\u0179\u017a\5b\62\2\u017a\u017b\7\35\2\2\u017b")
        buf.write("\u017c\5b\62\2\u017c\u017d\5:\36\2\u017d\u017e\7\61\2")
        buf.write("\2\u017e\u017f\5V,\2\u017f=\3\2\2\2\u0180\u0181\5b\62")
        buf.write("\2\u0181\u0182\7\66\2\2\u0182\u0183\t\2\2\2\u0183?\3\2")
        buf.write("\2\2\u0184\u0185\5b\62\2\u0185\u0186\7\66\2\2\u0186\u0187")
        buf.write("\t\2\2\2\u0187\u0188\7\60\2\2\u0188\u0189\5\u008aF\2\u0189")
        buf.write("\u018a\7\61\2\2\u018aA\3\2\2\2\u018b\u018c\5b\62\2\u018c")
        buf.write("\u018d\7\34\2\2\u018d\u018e\7=\2\2\u018eC\3\2\2\2\u018f")
        buf.write("\u0190\5b\62\2\u0190\u0191\7\34\2\2\u0191\u0192\7=\2\2")
        buf.write("\u0192\u0193\7\60\2\2\u0193\u0194\5\u008aF\2\u0194\u0195")
        buf.write("\7\61\2\2\u0195E\3\2\2\2\u0196\u0199\5@!\2\u0197\u0199")
        buf.write("\5D#\2\u0198\u0196\3\2\2\2\u0198\u0197\3\2\2\2\u0199G")
        buf.write("\3\2\2\2\u019a\u019b\5F$\2\u019b\u019c\79\2\2\u019cI\3")
        buf.write("\2\2\2\u019d\u019e\7\3\2\2\u019e\u019f\79\2\2\u019fK\3")
        buf.write("\2\2\2\u01a0\u01a1\7\4\2\2\u01a1\u01a2\79\2\2\u01a2M\3")
        buf.write("\2\2\2\u01a3\u01a6\5b\62\2\u01a4\u01a6\3\2\2\2\u01a5\u01a3")
        buf.write("\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a6O\3\2\2\2\u01a7\u01a8")
        buf.write("\7\22\2\2\u01a8\u01a9\5N(\2\u01a9\u01aa\79\2\2\u01aaQ")
        buf.write("\3\2\2\2\u01ab\u01ac\7\64\2\2\u01ac\u01ad\5Z.\2\u01ad")
        buf.write("\u01ae\5 \21\2\u01ae\u01af\5Z.\2\u01af\u01b0\7\65\2\2")
        buf.write("\u01b0S\3\2\2\2\u01b1\u01b2\7\64\2\2\u01b2\u01b3\5Z.\2")
        buf.write("\u01b3\u01b4\7\65\2\2\u01b4U\3\2\2\2\u01b5\u01b6\7\64")
        buf.write("\2\2\u01b6\u01b7\5\\/\2\u01b7\u01b8\7\65\2\2\u01b8W\3")
        buf.write("\2\2\2\u01b9\u01ba\7\64\2\2\u01ba\u01bb\5\\/\2\u01bb\u01bc")
        buf.write("\7\22\2\2\u01bc\u01bd\79\2\2\u01bd\u01be\7\65\2\2\u01be")
        buf.write("Y\3\2\2\2\u01bf\u01c0\5^\60\2\u01c0\u01c1\5Z.\2\u01c1")
        buf.write("\u01c5\3\2\2\2\u01c2\u01c5\5^\60\2\u01c3\u01c5\3\2\2\2")
        buf.write("\u01c4\u01bf\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c4\u01c3\3")
        buf.write("\2\2\2\u01c5[\3\2\2\2\u01c6\u01c7\5`\61\2\u01c7\u01c8")
        buf.write("\5\\/\2\u01c8\u01cc\3\2\2\2\u01c9\u01cc\5`\61\2\u01ca")
        buf.write("\u01cc\3\2\2\2\u01cb\u01c6\3\2\2\2\u01cb\u01c9\3\2\2\2")
        buf.write("\u01cb\u01ca\3\2\2\2\u01cc]\3\2\2\2\u01cd\u01d2\5\22\n")
        buf.write("\2\u01ce\u01d2\5\36\20\2\u01cf\u01d2\5\f\7\2\u01d0\u01d2")
        buf.write("\5\16\b\2\u01d1\u01cd\3\2\2\2\u01d1\u01ce\3\2\2\2\u01d1")
        buf.write("\u01cf\3\2\2\2\u01d1\u01d0\3\2\2\2\u01d2_\3\2\2\2\u01d3")
        buf.write("\u01dd\5\30\r\2\u01d4\u01dd\5,\27\2\u01d5\u01dd\5\62\32")
        buf.write("\2\u01d6\u01dd\5<\37\2\u01d7\u01dd\5\"\22\2\u01d8\u01dd")
        buf.write("\5H%\2\u01d9\u01dd\5J&\2\u01da\u01dd\5L\'\2\u01db\u01dd")
        buf.write("\5P)\2\u01dc\u01d3\3\2\2\2\u01dc\u01d4\3\2\2\2\u01dc\u01d5")
        buf.write("\3\2\2\2\u01dc\u01d6\3\2\2\2\u01dc\u01d7\3\2\2\2\u01dc")
        buf.write("\u01d8\3\2\2\2\u01dc\u01d9\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dc\u01db\3\2\2\2\u01dda\3\2\2\2\u01de\u01df\5d\63")
        buf.write("\2\u01df\u01e0\t\4\2\2\u01e0\u01e1\5d\63\2\u01e1\u01e4")
        buf.write("\3\2\2\2\u01e2\u01e4\5d\63\2\u01e3\u01de\3\2\2\2\u01e3")
        buf.write("\u01e2\3\2\2\2\u01e4c\3\2\2\2\u01e5\u01e6\5f\64\2\u01e6")
        buf.write("\u01e7\t\5\2\2\u01e7\u01e8\5f\64\2\u01e8\u01eb\3\2\2\2")
        buf.write("\u01e9\u01eb\5f\64\2\u01ea\u01e5\3\2\2\2\u01ea\u01e9\3")
        buf.write("\2\2\2\u01ebe\3\2\2\2\u01ec\u01ed\b\64\1\2\u01ed\u01ee")
        buf.write("\5h\65\2\u01ee\u01f4\3\2\2\2\u01ef\u01f0\f\4\2\2\u01f0")
        buf.write("\u01f1\t\6\2\2\u01f1\u01f3\5h\65\2\u01f2\u01ef\3\2\2\2")
        buf.write("\u01f3\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3")
        buf.write("\2\2\2\u01f5g\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8")
        buf.write("\b\65\1\2\u01f8\u01f9\5j\66\2\u01f9\u01ff\3\2\2\2\u01fa")
        buf.write("\u01fb\f\4\2\2\u01fb\u01fc\t\7\2\2\u01fc\u01fe\5j\66\2")
        buf.write("\u01fd\u01fa\3\2\2\2\u01fe\u0201\3\2\2\2\u01ff\u01fd\3")
        buf.write("\2\2\2\u01ff\u0200\3\2\2\2\u0200i\3\2\2\2\u0201\u01ff")
        buf.write("\3\2\2\2\u0202\u0203\b\66\1\2\u0203\u0204\5l\67\2\u0204")
        buf.write("\u020a\3\2\2\2\u0205\u0206\f\4\2\2\u0206\u0207\t\b\2\2")
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
        buf.write("\u022c\3\2\2\2\u0224\u0227\f\4\2\2\u0225\u0228\5|?\2\u0226")
        buf.write("\u0228\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0226\3\2\2\2")
        buf.write("\u0228\u0229\3\2\2\2\u0229\u022b\5\u0082B\2\u022a\u0224")
        buf.write("\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022ds\3\2\2\2\u022e\u022c\3\2\2\2\u022f")
        buf.write("\u0230\t\2\2\2\u0230\u0233\5\u0086D\2\u0231\u0233\5v<")
        buf.write("\2\u0232\u022f\3\2\2\2\u0232\u0231\3\2\2\2\u0233u\3\2")
        buf.write("\2\2\u0234\u0235\7\31\2\2\u0235\u0236\5b\62\2\u0236\u0237")
        buf.write("\7\60\2\2\u0237\u0238\5\u008aF\2\u0238\u0239\7\61\2\2")
        buf.write("\u0239\u023c\3\2\2\2\u023a\u023c\5x=\2\u023b\u0234\3\2")
        buf.write("\2\2\u023b\u023a\3\2\2\2\u023cw\3\2\2\2\u023d\u0243\5")
        buf.write("\u0090I\2\u023e\u0243\7<\2\2\u023f\u0243\7=\2\2\u0240")
        buf.write("\u0243\7\33\2\2\u0241\u0243\5z>\2\u0242\u023d\3\2\2\2")
        buf.write("\u0242\u023e\3\2\2\2\u0242\u023f\3\2\2\2\u0242\u0240\3")
        buf.write("\2\2\2\u0242\u0241\3\2\2\2\u0243y\3\2\2\2\u0244\u0245")
        buf.write("\7\60\2\2\u0245\u0246\5b\62\2\u0246\u0247\7\61\2\2\u0247")
        buf.write("{\3\2\2\2\u0248\u0249\7\62\2\2\u0249\u024a\5b\62\2\u024a")
        buf.write("\u024b\7\63\2\2\u024b\u024c\5|?\2\u024c\u0252\3\2\2\2")
        buf.write("\u024d\u024e\7\62\2\2\u024e\u024f\5b\62\2\u024f\u0250")
        buf.write("\7\63\2\2\u0250\u0252\3\2\2\2\u0251\u0248\3\2\2\2\u0251")
        buf.write("\u024d\3\2\2\2\u0252}\3\2\2\2\u0253\u0258\5\u0080A\2\u0254")
        buf.write("\u0255\5\u0080A\2\u0255\u0256\5|?\2\u0256\u0258\3\2\2")
        buf.write("\2\u0257\u0253\3\2\2\2\u0257\u0254\3\2\2\2\u0258\177\3")
        buf.write("\2\2\2\u0259\u0260\t\2\2\2\u025a\u025b\5b\62\2\u025b\u025c")
        buf.write("\5> \2\u025c\u025d\t\2\2\2\u025d\u0260\3\2\2\2\u025e\u0260")
        buf.write("\3\2\2\2\u025f\u0259\3\2\2\2\u025f\u025a\3\2\2\2\u025f")
        buf.write("\u025e\3\2\2\2\u0260\u0081\3\2\2\2\u0261\u0262\5\u0084")
        buf.write("C\2\u0262\u0263\5\u0082B\2\u0263\u0266\3\2\2\2\u0264\u0266")
        buf.write("\5\u0084C\2\u0265\u0261\3\2\2\2\u0265\u0264\3\2\2\2\u0266")
        buf.write("\u0083\3\2\2\2\u0267\u0268\7\66\2\2\u0268\u0270\t\2\2")
        buf.write("\2\u0269\u026a\7\66\2\2\u026a\u026b\t\2\2\2\u026b\u026c")
        buf.write("\7\60\2\2\u026c\u026d\5\u008aF\2\u026d\u026e\7\61\2\2")
        buf.write("\u026e\u0270\3\2\2\2\u026f\u0267\3\2\2\2\u026f\u0269\3")
        buf.write("\2\2\2\u0270\u0085\3\2\2\2\u0271\u0272\5\u0088E\2\u0272")
        buf.write("\u0273\5\u0086D\2\u0273\u0276\3\2\2\2\u0274\u0276\5\u0088")
        buf.write("E\2\u0275\u0271\3\2\2\2\u0275\u0274\3\2\2\2\u0276\u0087")
        buf.write("\3\2\2\2\u0277\u0278\7\34\2\2\u0278\u0280\7=\2\2\u0279")
        buf.write("\u027a\7\34\2\2\u027a\u027b\7=\2\2\u027b\u027c\7\60\2")
        buf.write("\2\u027c\u027d\5\u008aF\2\u027d\u027e\7\61\2\2\u027e\u0280")
        buf.write("\3\2\2\2\u027f\u0277\3\2\2\2\u027f\u0279\3\2\2\2\u0280")
        buf.write("\u0089\3\2\2\2\u0281\u0282\5b\62\2\u0282\u0283\7\67\2")
        buf.write("\2\u0283\u0284\5\u008aF\2\u0284\u0288\3\2\2\2\u0285\u0288")
        buf.write("\5b\62\2\u0286\u0288\3\2\2\2\u0287\u0281\3\2\2\2\u0287")
        buf.write("\u0285\3\2\2\2\u0287\u0286\3\2\2\2\u0288\u008b\3\2\2\2")
        buf.write("\u0289\u028a\7\f\2\2\u028a\u028b\7\60\2\2\u028b\u028c")
        buf.write("\5\u008eH\2\u028c\u028d\7\61\2\2\u028d\u008d\3\2\2\2\u028e")
        buf.write("\u028f\5b\62\2\u028f\u0290\7\67\2\2\u0290\u0291\5\u008e")
        buf.write("H\2\u0291\u0295\3\2\2\2\u0292\u0295\5b\62\2\u0293\u0295")
        buf.write("\3\2\2\2\u0294\u028e\3\2\2\2\u0294\u0292\3\2\2\2\u0294")
        buf.write("\u0293\3\2\2\2\u0295\u008f\3\2\2\2\u0296\u029c\7@\2\2")
        buf.write("\u0297\u029c\7?\2\2\u0298\u029c\7\t\2\2\u0299\u029c\7")
        buf.write(">\2\2\u029a\u029c\5\u008cG\2\u029b\u0296\3\2\2\2\u029b")
        buf.write("\u0297\3\2\2\2\u029b\u0298\3\2\2\2\u029b\u0299\3\2\2\2")
        buf.write("\u029b\u029a\3\2\2\2\u029c\u0091\3\2\2\2\u029d\u029e\5")
        buf.write("\u0094K\2\u029e\u029f\79\2\2\u029f\u02a0\5\u0092J\2\u02a0")
        buf.write("\u02a4\3\2\2\2\u02a1\u02a4\5\u0094K\2\u02a2\u02a4\3\2")
        buf.write("\2\2\u02a3\u029d\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a2")
        buf.write("\3\2\2\2\u02a4\u0093\3\2\2\2\u02a5\u02a6\5\u0096L\2\u02a6")
        buf.write("\u02a7\78\2\2\u02a7\u02a8\5\u00a4S\2\u02a8\u0095\3\2\2")
        buf.write("\2\u02a9\u02aa\t\2\2\2\u02aa\u02ab\7\67\2\2\u02ab\u02af")
        buf.write("\5\u0096L\2\u02ac\u02af\t\2\2\2\u02ad\u02af\3\2\2\2\u02ae")
        buf.write("\u02a9\3\2\2\2\u02ae\u02ac\3\2\2\2\u02ae\u02ad\3\2\2\2")
        buf.write("\u02af\u0097\3\2\2\2\u02b0\u02b1\7<\2\2\u02b1\u02b2\7")
        buf.write("\67\2\2\u02b2\u02b6\5\u0098M\2\u02b3\u02b6\7<\2\2\u02b4")
        buf.write("\u02b6\3\2\2\2\u02b5\u02b0\3\2\2\2\u02b5\u02b3\3\2\2\2")
        buf.write("\u02b5\u02b4\3\2\2\2\u02b6\u0099\3\2\2\2\u02b7\u02ba\5")
        buf.write("\u0090I\2\u02b8\u02ba\5b\62\2\u02b9\u02b7\3\2\2\2\u02b9")
        buf.write("\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bc\7\67\2")
        buf.write("\2\u02bc\u02bd\5\u009aN\2\u02bd\u02c4\3\2\2\2\u02be\u02c1")
        buf.write("\5\u0090I\2\u02bf\u02c1\5b\62\2\u02c0\u02be\3\2\2\2\u02c0")
        buf.write("\u02bf\3\2\2\2\u02c1\u02c4\3\2\2\2\u02c2\u02c4\3\2\2\2")
        buf.write("\u02c3\u02b9\3\2\2\2\u02c3\u02c0\3\2\2\2\u02c3\u02c2\3")
        buf.write("\2\2\2\u02c4\u009b\3\2\2\2\u02c5\u02c6\7\f\2\2\u02c6\u02c7")
        buf.write("\7\62\2\2\u02c7\u02c8\5\u009eP\2\u02c8\u02c9\7\67\2\2")
        buf.write("\u02c9\u02ca\5\u00a0Q\2\u02ca\u02cb\7\63\2\2\u02cb\u009d")
        buf.write("\3\2\2\2\u02cc\u02d2\5\u009cO\2\u02cd\u02d2\7\16\2\2\u02ce")
        buf.write("\u02d2\7\17\2\2\u02cf\u02d2\7\20\2\2\u02d0\u02d2\7\21")
        buf.write("\2\2\u02d1\u02cc\3\2\2\2\u02d1\u02cd\3\2\2\2\u02d1\u02ce")
        buf.write("\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d1\u02d0\3\2\2\2\u02d2")
        buf.write("\u009f\3\2\2\2\u02d3\u02d4\7@\2\2\u02d4\u00a1\3\2\2\2")
        buf.write("\u02d5\u02d6\t\t\2\2\u02d6\u00a3\3\2\2\2\u02d7\u02da\5")
        buf.write("\u00a2R\2\u02d8\u02da\5\u009cO\2\u02d9\u02d7\3\2\2\2\u02d9")
        buf.write("\u02d8\3\2\2\2\u02da\u00a5\3\2\2\2;\u00a9\u00b4\u00be")
        buf.write("\u00d7\u00e3\u00ef\u00fd\u0109\u011d\u0123\u0131\u0133")
        buf.write("\u0139\u0147\u0149\u014d\u0153\u015f\u0165\u0173\u0198")
        buf.write("\u01a5\u01c4\u01cb\u01d1\u01dc\u01e3\u01ea\u01f4\u01ff")
        buf.write("\u020a\u0210\u0215\u021e\u0227\u022c\u0232\u023b\u0242")
        buf.write("\u0251\u0257\u025f\u0265\u026f\u0275\u027f\u0287\u0294")
        buf.write("\u029b\u02a3\u02ae\u02b5\u02b9\u02c0\u02c3\u02d1\u02d9")
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
    RULE_dot_doublesemicolon_and_name = 17
    RULE_call_funcs = 18
    RULE_call_func = 19
    RULE_call_func_attr_list = 20
    RULE_assignment_statements = 21
    RULE_lhs = 22
    RULE_multiple_accesses = 23
    RULE_if_statements = 24
    RULE_elseif_list_statements = 25
    RULE_elseif_statement = 26
    RULE_else_statement = 27
    RULE_by_expr = 28
    RULE_forin_statements = 29
    RULE_instance_attr_access = 30
    RULE_instance_method_access = 31
    RULE_static_attr_access = 32
    RULE_static_method_access = 33
    RULE_method_invocation = 34
    RULE_method_invocation_statement = 35
    RULE_break_statements = 36
    RULE_continue_statements = 37
    RULE_return_expr = 38
    RULE_return_statements = 39
    RULE_program_block_class_statements = 40
    RULE_block_class_statements = 41
    RULE_block_statements = 42
    RULE_block_statements_in_main = 43
    RULE_statements_class = 44
    RULE_statements = 45
    RULE_statement_class = 46
    RULE_statement = 47
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
    RULE_instance_accesses = 64
    RULE_instance_access = 65
    RULE_static_accesses = 66
    RULE_static_access = 67
    RULE_list_expr = 68
    RULE_array_lit = 69
    RULE_array_val = 70
    RULE_literal = 71
    RULE_list_parameters = 72
    RULE_param = 73
    RULE_identifier_list = 74
    RULE_variable_in_func_identifier_list = 75
    RULE_value_list = 76
    RULE_array_type = 77
    RULE_array_element_type = 78
    RULE_array_size = 79
    RULE_primitive_type = 80
    RULE_variable_type = 81

    ruleNames =  [ "program", "class_main_program_declarations", "class_declarations", 
                   "class_declaration", "class_inheritance", "constructor_dclr", 
                   "destructor_dclr", "method_declaration", "variable_declaration", 
                   "declare_initiate_list", "type_and_assign", "variable_in_func_declaration", 
                   "declare_initiate_in_func_list", "type_and_assign_in_func", 
                   "function_declaration", "main_function_declaration", 
                   "call_func_statement", "dot_doublesemicolon_and_name", 
                   "call_funcs", "call_func", "call_func_attr_list", "assignment_statements", 
                   "lhs", "multiple_accesses", "if_statements", "elseif_list_statements", 
                   "elseif_statement", "else_statement", "by_expr", "forin_statements", 
                   "instance_attr_access", "instance_method_access", "static_attr_access", 
                   "static_method_access", "method_invocation", "method_invocation_statement", 
                   "break_statements", "continue_statements", "return_expr", 
                   "return_statements", "program_block_class_statements", 
                   "block_class_statements", "block_statements", "block_statements_in_main", 
                   "statements_class", "statements", "statement_class", 
                   "statement", "expr", "expr1", "expr2", "expr3", "expr4", 
                   "expr5", "expr6", "expr7", "expr8", "expr9", "expr10", 
                   "expr11", "expr12", "index_operators", "index_expr", 
                   "index", "instance_accesses", "instance_access", "static_accesses", 
                   "static_access", "list_expr", "array_lit", "array_val", 
                   "literal", "list_parameters", "param", "identifier_list", 
                   "variable_in_func_identifier_list", "value_list", "array_type", 
                   "array_element_type", "array_size", "primitive_type", 
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
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment_statements(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Assignment_statementsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Assignment_statementsContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 164
                self.assignment_statements()
                self.state = 167 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.DOUBLECOLONOP) | (1 << D96Parser.MINUSOP) | (1 << D96Parser.NOTOP) | (1 << D96Parser.LB) | (1 << D96Parser.DOT) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS) | (1 << D96Parser.STRINGLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.INTLIT))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_main_program_declarationsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_main_program_declarations" ):
                return visitor.visitClass_main_program_declarations(self)
            else:
                return visitor.visitChildren(self)




    def class_main_program_declarations(self):

        localctx = D96Parser.Class_main_program_declarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_class_main_program_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.CLASS)
            self.state = 170
            self.match(D96Parser.PROGRAM)
            self.state = 171
            self.program_block_class_statements()
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
        self.enterRule(localctx, 4, self.RULE_class_declarations)
        try:
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.class_declaration()
                self.state = 174
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
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
        self.enterRule(localctx, 6, self.RULE_class_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(D96Parser.CLASS)
            self.state = 181
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 182
            self.class_inheritance()
            self.state = 183
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
        self.enterRule(localctx, 8, self.RULE_class_inheritance)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self.match(D96Parser.COLON)
                self.state = 186
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
        self.enterRule(localctx, 10, self.RULE_constructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 191
            self.match(D96Parser.LB)
            self.state = 192
            self.list_parameters()
            self.state = 193
            self.match(D96Parser.RB)
            self.state = 194
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
        self.enterRule(localctx, 12, self.RULE_destructor_dclr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(D96Parser.DESTRUCTOR)
            self.state = 197
            self.match(D96Parser.LB)
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
        self.enterRule(localctx, 14, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
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


    class Variable_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = D96Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 208
                self.declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 209
                self.identifier_list()
                self.state = 210
                self.match(D96Parser.COLON)
                self.state = 211
                self.variable_type()
                pass


            self.state = 215
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_initiate_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_initiate_list" ):
                return visitor.visitDeclare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def declare_initiate_list(self):

        localctx = D96Parser.Declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 218
                self.type_and_assign()
                self.state = 219
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.identifier_list()
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


    class Type_and_assignContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_and_assign" ):
                return visitor.visitType_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def type_and_assign(self):

        localctx = D96Parser.Type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.match(D96Parser.COMMA)
                self.state = 228
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 229
                self.type_and_assign()
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


    class Variable_in_func_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_in_func_declaration" ):
                return visitor.visitVariable_in_func_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_in_func_declaration(self):

        localctx = D96Parser.Variable_in_func_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_variable_in_func_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 240
            self.declare_initiate_in_func_list()
            self.state = 241
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declare_initiate_in_func_listContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_initiate_in_func_list" ):
                return visitor.visitDeclare_initiate_in_func_list(self)
            else:
                return visitor.visitChildren(self)




    def declare_initiate_in_func_list(self):

        localctx = D96Parser.Declare_initiate_in_func_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_declare_initiate_in_func_list)
        try:
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 243
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 244
                self.type_and_assign_in_func()
                self.state = 245
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.variable_in_func_identifier_list()
                self.state = 248
                self.match(D96Parser.COLON)
                self.state = 249
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_and_assign_in_func" ):
                return visitor.visitType_and_assign_in_func(self)
            else:
                return visitor.visitChildren(self)




    def type_and_assign_in_func(self):

        localctx = D96Parser.Type_and_assign_in_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_type_and_assign_in_func)
        try:
            self.state = 263
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(D96Parser.COMMA)
                self.state = 254
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 255
                self.type_and_assign_in_func()
                self.state = 256
                self.expr()
                self.state = 257
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.match(D96Parser.COLON)
                self.state = 260
                self.variable_type()
                self.state = 261
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
        self.enterRule(localctx, 28, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 266
            self.match(D96Parser.LB)
            self.state = 267
            self.list_parameters()
            self.state = 268
            self.match(D96Parser.RB)
            self.state = 269
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_function_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAIN(self):
            return self.getToken(D96Parser.MAIN, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def block_statements_in_main(self):
            return self.getTypedRuleContext(D96Parser.Block_statements_in_mainContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_main_function_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_function_declaration" ):
                return visitor.visitMain_function_declaration(self)
            else:
                return visitor.visitChildren(self)




    def main_function_declaration(self):

        localctx = D96Parser.Main_function_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_main_function_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(D96Parser.MAIN)
            self.state = 272
            self.match(D96Parser.LB)
            self.state = 273
            self.match(D96Parser.RB)
            self.state = 274
            self.block_statements_in_main()
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

        def call_funcs(self):
            return self.getTypedRuleContext(D96Parser.Call_funcsContext,0)


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
        self.enterRule(localctx, 32, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.call_funcs()
            self.state = 277
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dot_doublesemicolon_and_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_dot_doublesemicolon_and_name

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDot_doublesemicolon_and_name" ):
                return visitor.visitDot_doublesemicolon_and_name(self)
            else:
                return visitor.visitChildren(self)




    def dot_doublesemicolon_and_name(self):

        localctx = D96Parser.Dot_doublesemicolon_and_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_dot_doublesemicolon_and_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOT]:
                self.state = 279
                self.match(D96Parser.DOT)
                self.state = 280
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [D96Parser.DOUBLECOLONOP]:
                self.state = 281
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 282
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
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


    class Call_funcsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_func(self):
            return self.getTypedRuleContext(D96Parser.Call_funcContext,0)


        def call_funcs(self):
            return self.getTypedRuleContext(D96Parser.Call_funcsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_funcs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_funcs" ):
                return visitor.visitCall_funcs(self)
            else:
                return visitor.visitChildren(self)




    def call_funcs(self):

        localctx = D96Parser.Call_funcsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call_funcs)
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.call_func()
                self.state = 286
                self.call_funcs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 288
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def call_func(self):
            return self.getTypedRuleContext(D96Parser.Call_funcContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def dot_doublesemicolon_and_name(self):
            return self.getTypedRuleContext(D96Parser.Dot_doublesemicolon_and_nameContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = D96Parser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_call_func)
        self._la = 0 # Token type
        try:
            self.state = 305
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 1)
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
                self.state = 295
                self.call_func()
                pass
            elif token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 297
                self.dot_doublesemicolon_and_name()
                self.state = 303
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.LB]:
                    self.state = 298
                    self.match(D96Parser.LB)
                    self.state = 299
                    self.value_list()
                    self.state = 300
                    self.match(D96Parser.RB)
                    pass
                elif token in [D96Parser.DOUBLECOLONOP, D96Parser.ASSIGNOP, D96Parser.LSB, D96Parser.DOT, D96Parser.SEMICOLON, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                    pass
                else:
                    raise NoViableAltException(self)

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

        def dot_doublesemicolon_and_name(self):
            return self.getTypedRuleContext(D96Parser.Dot_doublesemicolon_and_nameContext,0)


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
        self.enterRule(localctx, 40, self.RULE_call_func_attr_list)
        try:
            self.state = 311
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 307
                self.dot_doublesemicolon_and_name()
                self.state = 308
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.dot_doublesemicolon_and_name()
                pass


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
        self.enterRule(localctx, 42, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.lhs()
            self.state = 314
            self.match(D96Parser.ASSIGNOP)
            self.state = 315
            self.expr()
            self.state = 316
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

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def instance_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_accessContext,0)


        def static_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_accessContext,0)


        def call_funcs(self):
            return self.getTypedRuleContext(D96Parser.Call_funcsContext,0)


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


        def multiple_accesses(self):
            return self.getTypedRuleContext(D96Parser.Multiple_accessesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 318
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 319
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.state = 320
                self.instance_attr_access()
                pass

            elif la_ == 4:
                self.state = 321
                self.static_attr_access()
                pass

            elif la_ == 5:
                self.state = 322
                self.call_funcs()
                self.state = 325
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                    self.state = 323
                    self.multiple_accesses()
                    pass
                elif token in [D96Parser.ASSIGNOP, D96Parser.LSB]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass


            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 329
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


    class Multiple_accessesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dot_doublesemicolon_and_name(self):
            return self.getTypedRuleContext(D96Parser.Dot_doublesemicolon_and_nameContext,0)


        def multiple_accesses(self):
            return self.getTypedRuleContext(D96Parser.Multiple_accessesContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_multiple_accesses

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiple_accesses" ):
                return visitor.visitMultiple_accesses(self)
            else:
                return visitor.visitChildren(self)




    def multiple_accesses(self):

        localctx = D96Parser.Multiple_accessesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_multiple_accesses)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.dot_doublesemicolon_and_name()
                self.state = 334
                self.multiple_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 336
                self.dot_doublesemicolon_and_name()
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


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statements" ):
                return visitor.visitIf_statements(self)
            else:
                return visitor.visitChildren(self)




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(D96Parser.IF)
            self.state = 340
            self.match(D96Parser.LB)
            self.state = 341
            self.expr()
            self.state = 342
            self.match(D96Parser.RB)
            self.state = 343
            self.block_statements()
            self.state = 349
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ELSEIF]:
                self.state = 344
                self.elseif_list_statements()
                self.state = 345
                self.else_statement()
                pass
            elif token in [D96Parser.ELSE]:
                self.state = 347
                self.else_statement()
                pass
            elif token in [D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.DOUBLECOLONOP, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.RCB, D96Parser.DOT, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elseif_statement(self):
            return self.getTypedRuleContext(D96Parser.Elseif_statementContext,0)


        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_list_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_list_statements" ):
                return visitor.visitElseif_list_statements(self)
            else:
                return visitor.visitChildren(self)




    def elseif_list_statements(self):

        localctx = D96Parser.Elseif_list_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elseif_list_statements)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.elseif_statement()
                self.state = 352
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
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


        def getRuleIndex(self):
            return D96Parser.RULE_elseif_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseif_statement" ):
                return visitor.visitElseif_statement(self)
            else:
                return visitor.visitChildren(self)




    def elseif_statement(self):

        localctx = D96Parser.Elseif_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(D96Parser.ELSEIF)
            self.state = 358
            self.match(D96Parser.LB)
            self.state = 359
            self.expr()
            self.state = 360
            self.match(D96Parser.RB)
            self.state = 361
            self.block_statements()
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
        self.enterRule(localctx, 54, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(D96Parser.ELSE)
            self.state = 364
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
        self.enterRule(localctx, 56, self.RULE_by_expr)
        try:
            self.state = 369
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 366
                self.match(D96Parser.BY)
                self.state = 367
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
        self.enterRule(localctx, 58, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(D96Parser.FOREACH)
            self.state = 372
            self.match(D96Parser.LB)
            self.state = 373
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 374
            self.match(D96Parser.IN)
            self.state = 375
            self.expr()
            self.state = 376
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 377
            self.expr()
            self.state = 378
            self.by_expr()
            self.state = 379
            self.match(D96Parser.RB)
            self.state = 380
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

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr_access" ):
                return visitor.visitInstance_attr_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr_access(self):

        localctx = D96Parser.Instance_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_instance_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.expr()
            self.state = 383
            self.match(D96Parser.DOT)
            self.state = 384
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_access" ):
                return visitor.visitInstance_method_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_access(self):

        localctx = D96Parser.Instance_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_instance_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.expr()
            self.state = 387
            self.match(D96Parser.DOT)
            self.state = 388
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 389
            self.match(D96Parser.LB)
            self.state = 390
            self.list_expr()
            self.state = 391
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

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def DOUBLECOLONOP(self):
            return self.getToken(D96Parser.DOUBLECOLONOP, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr_access" ):
                return visitor.visitStatic_attr_access(self)
            else:
                return visitor.visitChildren(self)




    def static_attr_access(self):

        localctx = D96Parser.Static_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_static_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.expr()
            self.state = 394
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 395
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_access" ):
                return visitor.visitStatic_method_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_access(self):

        localctx = D96Parser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_static_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.expr()
            self.state = 398
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 399
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 400
            self.match(D96Parser.LB)
            self.state = 401
            self.list_expr()
            self.state = 402
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
        self.enterRule(localctx, 68, self.RULE_method_invocation)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
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
        self.enterRule(localctx, 70, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.method_invocation()
            self.state = 409
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
        self.enterRule(localctx, 72, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.match(D96Parser.BREAK)
            self.state = 412
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
        self.enterRule(localctx, 74, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(D96Parser.CONTINUE)
            self.state = 415
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
        self.enterRule(localctx, 76, self.RULE_return_expr)
        try:
            self.state = 419
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
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
        self.enterRule(localctx, 78, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(D96Parser.RETURN)
            self.state = 422
            self.return_expr()
            self.state = 423
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Program_block_class_statementsContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram_block_class_statements" ):
                return visitor.visitProgram_block_class_statements(self)
            else:
                return visitor.visitChildren(self)




    def program_block_class_statements(self):

        localctx = D96Parser.Program_block_class_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_program_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(D96Parser.LCB)
            self.state = 426
            self.statements_class()
            self.state = 427
            self.main_function_declaration()
            self.state = 428
            self.statements_class()
            self.state = 429
            self.match(D96Parser.RCB)
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
        self.enterRule(localctx, 82, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 431
            self.match(D96Parser.LCB)
            self.state = 432
            self.statements_class()
            self.state = 433
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
        self.enterRule(localctx, 84, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(D96Parser.LCB)
            self.state = 436
            self.statements()
            self.state = 437
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statements_in_mainContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statements_in_main" ):
                return visitor.visitBlock_statements_in_main(self)
            else:
                return visitor.visitChildren(self)




    def block_statements_in_main(self):

        localctx = D96Parser.Block_statements_in_mainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_block_statements_in_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(D96Parser.LCB)
            self.state = 440
            self.statements()
            self.state = 441
            self.match(D96Parser.RETURN)
            self.state = 442
            self.match(D96Parser.SEMICOLON)
            self.state = 443
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
        self.enterRule(localctx, 88, self.RULE_statements_class)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.statement_class()
                self.state = 446
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
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
        self.enterRule(localctx, 90, self.RULE_statements)
        try:
            self.state = 457
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.statement()
                self.state = 453
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 455
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_class" ):
                return visitor.visitStatement_class(self)
            else:
                return visitor.visitChildren(self)




    def statement_class(self):

        localctx = D96Parser.Statement_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statement_class)
        try:
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 459
                self.variable_declaration()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.function_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 461
                self.constructor_dclr()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 462
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_statement)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 465
                self.variable_in_func_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 466
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 467
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 468
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 469
                self.call_func_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 470
                self.method_invocation_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 471
                self.break_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 472
                self.continue_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 473
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


        def index_operators(self):
            return self.getTypedRuleContext(D96Parser.Index_operatorsContext,0)


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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 554
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
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
                    self.state = 549
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.LSB]:
                        self.state = 547
                        self.index_operators()
                        pass
                    elif token in [D96Parser.DOT]:
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 551
                    self.instance_accesses() 
                self.state = 556
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr9" ):
                return visitor.visitExpr9(self)
            else:
                return visitor.visitChildren(self)




    def expr9(self):

        localctx = D96Parser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 557
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 558
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
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
        self.enterRule(localctx, 116, self.RULE_expr10)
        try:
            self.state = 569
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.match(D96Parser.NEW)
                self.state = 563
                self.expr()
                self.state = 564
                self.match(D96Parser.LB)
                self.state = 565
                self.list_expr()
                self.state = 566
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 568
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

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

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
        self.enterRule(localctx, 118, self.RULE_expr11)
        try:
            self.state = 576
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 571
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 573
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 4)
                self.state = 574
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 5)
                self.state = 575
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
        self.enterRule(localctx, 120, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 578
            self.match(D96Parser.LB)
            self.state = 579
            self.expr()
            self.state = 580
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




    def index_operators(self):

        localctx = D96Parser.Index_operatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_index_operators)
        try:
            self.state = 591
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 582
                self.match(D96Parser.LSB)
                self.state = 583
                self.expr()
                self.state = 584
                self.match(D96Parser.RSB)
                self.state = 585
                self.index_operators()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 587
                self.match(D96Parser.LSB)
                self.state = 588
                self.expr()
                self.state = 589
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
        self.enterRule(localctx, 124, self.RULE_index_expr)
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
        self.enterRule(localctx, 126, self.RULE_index)
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
        self.enterRule(localctx, 128, self.RULE_instance_accesses)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_access" ):
                return visitor.visitInstance_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_access(self):

        localctx = D96Parser.Instance_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_instance_access)
        self._la = 0 # Token type
        try:
            self.state = 621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 613
                self.match(D96Parser.DOT)
                self.state = 614
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
                self.match(D96Parser.DOT)
                self.state = 616
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 132, self.RULE_static_accesses)
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
        self.enterRule(localctx, 134, self.RULE_static_access)
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
        self.enterRule(localctx, 136, self.RULE_list_expr)
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
        self.enterRule(localctx, 138, self.RULE_array_lit)
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
        self.enterRule(localctx, 140, self.RULE_array_val)
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = D96Parser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_literal)
        try:
            self.state = 665
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 660
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 662
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 663
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 664
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
        self.enterRule(localctx, 144, self.RULE_list_parameters)
        try:
            self.state = 673
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 667
                self.param()
                self.state = 668
                self.match(D96Parser.SEMICOLON)
                self.state = 669
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
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
        self.enterRule(localctx, 146, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 675
            self.identifier_list()
            self.state = 676
            self.match(D96Parser.COLON)
            self.state = 677
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
        self.enterRule(localctx, 148, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 684
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 680
                self.match(D96Parser.COMMA)
                self.state = 681
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 682
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
        self.enterRule(localctx, 150, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 691
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 686
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 687
                self.match(D96Parser.COMMA)
                self.state = 688
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 689
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
        self.enterRule(localctx, 152, self.RULE_value_list)
        try:
            self.state = 705
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 695
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 693
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 694
                    self.expr()
                    pass


                self.state = 697
                self.match(D96Parser.COMMA)
                self.state = 698
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 702
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 700
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 701
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

        def array_size(self):
            return self.getTypedRuleContext(D96Parser.Array_sizeContext,0)


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
        self.enterRule(localctx, 154, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.match(D96Parser.ARRAY)
            self.state = 708
            self.match(D96Parser.LSB)
            self.state = 709
            self.array_element_type()
            self.state = 710
            self.match(D96Parser.COMMA)
            self.state = 711
            self.array_size()
            self.state = 712
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
        self.enterRule(localctx, 156, self.RULE_array_element_type)
        try:
            self.state = 719
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 714
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 715
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 716
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 717
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 718
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_size

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_size" ):
                return visitor.visitArray_size(self)
            else:
                return visitor.visitChildren(self)




    def array_size(self):

        localctx = D96Parser.Array_sizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 721
            self.match(D96Parser.INTLIT)
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
        self.enterRule(localctx, 160, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 723
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


        def getRuleIndex(self):
            return D96Parser.RULE_variable_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_type" ):
                return visitor.visitVariable_type(self)
            else:
                return visitor.visitChildren(self)




    def variable_type(self):

        localctx = D96Parser.Variable_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_variable_type)
        try:
            self.state = 727
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 726
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
         




