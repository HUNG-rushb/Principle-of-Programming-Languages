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
        buf.write("\u02e1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\3\3\3\3\3\3\3\5\3\u00af\n\3\3\4\3\4\3\4\3\4\3\4\3\5")
        buf.write("\3\5\3\5\5\5\u00b9\n\5\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\5\t\u00cf")
        buf.write("\n\t\3\t\3\t\3\n\3\n\3\n\3\n\5\n\u00d7\n\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13\u00de\n\13\3\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\f\5\f\u00e8\n\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\5\r\u00f4\n\r\3\16\3\16\3\16\5\16\u00f9\n\16")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\17\5\17\u0101\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u0108\n\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\5\21\u0112\n\21\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u011e\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\5\26\u0132\n\26\3\26\3")
        buf.write("\26\3\26\5\26\u0137\n\26\3\27\3\27\3\27\3\27\3\27\5\27")
        buf.write("\u013e\n\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0147")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\5\33\u0157\n\33\3\33\3\33\5\33\u015b")
        buf.write("\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\5\34\u0168\n\34\3\35\3\35\3\35\3\35\5\35\u016e\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3 \3")
        buf.write(" \3 \5 \u017c\n \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3\"")
        buf.write("\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3&\3&\5&\u01a1\n&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3)\3*\3*\5*\u01ae\n*\3+\3+\3+\3+\3,\3,\3,\3,\3-\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\5/\u01c7\n/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\5\60\u01ce\n\60\3\61\3\61\3\61")
        buf.write("\3\61\5\61\u01d4\n\61\3\62\3\62\3\62\3\62\3\62\3\62\3")
        buf.write("\62\3\62\3\62\5\62\u01df\n\62\3\63\3\63\3\63\3\63\3\63")
        buf.write("\5\63\u01e6\n\63\3\64\3\64\3\64\3\64\3\64\5\64\u01ed\n")
        buf.write("\64\3\65\3\65\3\65\3\65\3\65\3\65\7\65\u01f5\n\65\f\65")
        buf.write("\16\65\u01f8\13\65\3\66\3\66\3\66\3\66\3\66\3\66\7\66")
        buf.write("\u0200\n\66\f\66\16\66\u0203\13\66\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\7\67\u020b\n\67\f\67\16\67\u020e\13\67\38\3")
        buf.write("8\38\58\u0213\n8\39\39\39\59\u0218\n9\3:\3:\3:\3:\3:\7")
        buf.write(":\u021f\n:\f:\16:\u0222\13:\3;\3;\3;\3;\3;\3;\5;\u022a")
        buf.write("\n;\3;\7;\u022d\n;\f;\16;\u0230\13;\3<\3<\3<\5<\u0235")
        buf.write("\n<\3=\3=\3=\3=\3=\3=\3=\5=\u023e\n=\3>\3>\3>\3>\5>\u0244")
        buf.write("\n>\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\3@\7@\u0254")
        buf.write("\n@\f@\16@\u0257\13@\3A\3A\3A\3A\5A\u025d\nA\3B\3B\3B")
        buf.write("\3B\3B\3B\5B\u0265\nB\3C\3C\3C\3C\5C\u026b\nC\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\5D\u0275\nD\3E\3E\3E\3E\5E\u027b\nE\3")
        buf.write("F\3F\3F\3F\3F\3F\3F\3F\5F\u0285\nF\3G\3G\3G\3G\3G\3G\5")
        buf.write("G\u028d\nG\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\5I\u029a\n")
        buf.write("I\3J\3J\3J\3J\3J\3J\5J\u02a2\nJ\3K\3K\3K\3K\3K\3K\5K\u02aa")
        buf.write("\nK\3L\3L\3L\3L\3M\3M\3M\3M\3M\5M\u02b5\nM\3N\3N\3N\3")
        buf.write("N\3N\5N\u02bc\nN\3O\3O\5O\u02c0\nO\3O\3O\3O\3O\3O\5O\u02c7")
        buf.write("\nO\3O\5O\u02ca\nO\3P\3P\3P\3P\3P\3P\3P\3Q\3Q\3Q\3Q\3")
        buf.write("Q\5Q\u02d8\nQ\3R\3R\3S\3S\3S\5S\u02df\nS\3S\2\bhjlrt~")
        buf.write("T\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092\u0094")
        buf.write("\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4\2\n\3")
        buf.write("\29:\3\2\25\26\3\2-.\4\2&&(,\3\2$%\3\2\36\37\3\2 \"\3")
        buf.write("\2\16\21\2\u02eb\2\u00a6\3\2\2\2\4\u00ae\3\2\2\2\6\u00b0")
        buf.write("\3\2\2\2\b\u00b8\3\2\2\2\n\u00ba\3\2\2\2\f\u00c0\3\2\2")
        buf.write("\2\16\u00c5\3\2\2\2\20\u00cb\3\2\2\2\22\u00d6\3\2\2\2")
        buf.write("\24\u00dd\3\2\2\2\26\u00e7\3\2\2\2\30\u00f3\3\2\2\2\32")
        buf.write("\u00f5\3\2\2\2\34\u0100\3\2\2\2\36\u0107\3\2\2\2 \u0111")
        buf.write("\3\2\2\2\"\u011d\3\2\2\2$\u011f\3\2\2\2&\u0125\3\2\2\2")
        buf.write("(\u012a\3\2\2\2*\u012e\3\2\2\2,\u013d\3\2\2\2.\u013f\3")
        buf.write("\2\2\2\60\u0148\3\2\2\2\62\u014e\3\2\2\2\64\u0156\3\2")
        buf.write("\2\2\66\u015c\3\2\2\28\u016d\3\2\2\2:\u016f\3\2\2\2<\u0175")
        buf.write("\3\2\2\2>\u017b\3\2\2\2@\u017d\3\2\2\2B\u0188\3\2\2\2")
        buf.write("D\u018c\3\2\2\2F\u0193\3\2\2\2H\u0197\3\2\2\2J\u01a0\3")
        buf.write("\2\2\2L\u01a2\3\2\2\2N\u01a5\3\2\2\2P\u01a8\3\2\2\2R\u01ad")
        buf.write("\3\2\2\2T\u01af\3\2\2\2V\u01b3\3\2\2\2X\u01b7\3\2\2\2")
        buf.write("Z\u01bb\3\2\2\2\\\u01c6\3\2\2\2^\u01cd\3\2\2\2`\u01d3")
        buf.write("\3\2\2\2b\u01de\3\2\2\2d\u01e5\3\2\2\2f\u01ec\3\2\2\2")
        buf.write("h\u01ee\3\2\2\2j\u01f9\3\2\2\2l\u0204\3\2\2\2n\u0212\3")
        buf.write("\2\2\2p\u0217\3\2\2\2r\u0219\3\2\2\2t\u0223\3\2\2\2v\u0234")
        buf.write("\3\2\2\2x\u023d\3\2\2\2z\u0243\3\2\2\2|\u0245\3\2\2\2")
        buf.write("~\u0249\3\2\2\2\u0080\u025c\3\2\2\2\u0082\u0264\3\2\2")
        buf.write("\2\u0084\u026a\3\2\2\2\u0086\u0274\3\2\2\2\u0088\u027a")
        buf.write("\3\2\2\2\u008a\u0284\3\2\2\2\u008c\u028c\3\2\2\2\u008e")
        buf.write("\u028e\3\2\2\2\u0090\u0299\3\2\2\2\u0092\u02a1\3\2\2\2")
        buf.write("\u0094\u02a9\3\2\2\2\u0096\u02ab\3\2\2\2\u0098\u02b4\3")
        buf.write("\2\2\2\u009a\u02bb\3\2\2\2\u009c\u02c9\3\2\2\2\u009e\u02cb")
        buf.write("\3\2\2\2\u00a0\u02d7\3\2\2\2\u00a2\u02d9\3\2\2\2\u00a4")
        buf.write("\u02de\3\2\2\2\u00a6\u00a7\5\4\3\2\u00a7\u00a8\7\2\2\3")
        buf.write("\u00a8\3\3\2\2\2\u00a9\u00aa\5\6\4\2\u00aa\u00ab\5\4\3")
        buf.write("\2\u00ab\u00af\3\2\2\2\u00ac\u00af\5\6\4\2\u00ad\u00af")
        buf.write("\3\2\2\2\u00ae\u00a9\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\5\3\2\2\2\u00b0\u00b1\7\24\2\2\u00b1")
        buf.write("\u00b2\79\2\2\u00b2\u00b3\5\b\5\2\u00b3\u00b4\5V,\2\u00b4")
        buf.write("\7\3\2\2\2\u00b5\u00b6\7\67\2\2\u00b6\u00b9\79\2\2\u00b7")
        buf.write("\u00b9\3\2\2\2\u00b8\u00b5\3\2\2\2\u00b8\u00b7\3\2\2\2")
        buf.write("\u00b9\t\3\2\2\2\u00ba\u00bb\7\27\2\2\u00bb\u00bc\7/\2")
        buf.write("\2\u00bc\u00bd\5\u0094K\2\u00bd\u00be\7\60\2\2\u00be\u00bf")
        buf.write("\5X-\2\u00bf\13\3\2\2\2\u00c0\u00c1\7\30\2\2\u00c1\u00c2")
        buf.write("\7/\2\2\u00c2\u00c3\7\60\2\2\u00c3\u00c4\5X-\2\u00c4\r")
        buf.write("\3\2\2\2\u00c5\u00c6\t\2\2\2\u00c6\u00c7\7/\2\2\u00c7")
        buf.write("\u00c8\5\u0094K\2\u00c8\u00c9\7\60\2\2\u00c9\u00ca\5X")
        buf.write("-\2\u00ca\17\3\2\2\2\u00cb\u00ce\t\3\2\2\u00cc\u00cf\5")
        buf.write("\26\f\2\u00cd\u00cf\5\22\n\2\u00ce\u00cc\3\2\2\2\u00ce")
        buf.write("\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0\u00d1\78\2\2")
        buf.write("\u00d1\21\3\2\2\2\u00d2\u00d3\5\24\13\2\u00d3\u00d4\5")
        buf.write("\22\n\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5\24\13\2\u00d6")
        buf.write("\u00d2\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7\23\3\2\2\2\u00d8")
        buf.write("\u00d9\79\2\2\u00d9\u00de\7\66\2\2\u00da\u00de\79\2\2")
        buf.write("\u00db\u00dc\7\67\2\2\u00dc\u00de\5\u00a4S\2\u00dd\u00d8")
        buf.write("\3\2\2\2\u00dd\u00da\3\2\2\2\u00dd\u00db\3\2\2\2\u00de")
        buf.write("\25\3\2\2\2\u00df\u00e0\79\2\2\u00e0\u00e1\5\30\r\2\u00e1")
        buf.write("\u00e2\5d\63\2\u00e2\u00e8\3\2\2\2\u00e3\u00e4\5\u009a")
        buf.write("N\2\u00e4\u00e5\7\67\2\2\u00e5\u00e6\5\u00a4S\2\u00e6")
        buf.write("\u00e8\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7\u00e3\3\2\2\2")
        buf.write("\u00e8\27\3\2\2\2\u00e9\u00ea\7\66\2\2\u00ea\u00eb\79")
        buf.write("\2\2\u00eb\u00ec\5\30\r\2\u00ec\u00ed\5d\63\2\u00ed\u00ee")
        buf.write("\7\66\2\2\u00ee\u00f4\3\2\2\2\u00ef\u00f0\7\67\2\2\u00f0")
        buf.write("\u00f1\5\u00a4S\2\u00f1\u00f2\7\'\2\2\u00f2\u00f4\3\2")
        buf.write("\2\2\u00f3\u00e9\3\2\2\2\u00f3\u00ef\3\2\2\2\u00f4\31")
        buf.write("\3\2\2\2\u00f5\u00f8\t\3\2\2\u00f6\u00f9\5 \21\2\u00f7")
        buf.write("\u00f9\5\34\17\2\u00f8\u00f6\3\2\2\2\u00f8\u00f7\3\2\2")
        buf.write("\2\u00f9\u00fa\3\2\2\2\u00fa\u00fb\78\2\2\u00fb\33\3\2")
        buf.write("\2\2\u00fc\u00fd\5\36\20\2\u00fd\u00fe\5\34\17\2\u00fe")
        buf.write("\u0101\3\2\2\2\u00ff\u0101\5\36\20\2\u0100\u00fc\3\2\2")
        buf.write("\2\u0100\u00ff\3\2\2\2\u0101\35\3\2\2\2\u0102\u0103\t")
        buf.write("\2\2\2\u0103\u0108\7\66\2\2\u0104\u0108\t\2\2\2\u0105")
        buf.write("\u0106\7\67\2\2\u0106\u0108\5\u00a4S\2\u0107\u0102\3\2")
        buf.write("\2\2\u0107\u0104\3\2\2\2\u0107\u0105\3\2\2\2\u0108\37")
        buf.write("\3\2\2\2\u0109\u010a\t\2\2\2\u010a\u010b\5\"\22\2\u010b")
        buf.write("\u010c\5d\63\2\u010c\u0112\3\2\2\2\u010d\u010e\5\u009a")
        buf.write("N\2\u010e\u010f\7\67\2\2\u010f\u0110\5\u00a4S\2\u0110")
        buf.write("\u0112\3\2\2\2\u0111\u0109\3\2\2\2\u0111\u010d\3\2\2\2")
        buf.write("\u0112!\3\2\2\2\u0113\u0114\7\66\2\2\u0114\u0115\t\2\2")
        buf.write("\2\u0115\u0116\5\"\22\2\u0116\u0117\5d\63\2\u0117\u0118")
        buf.write("\7\66\2\2\u0118\u011e\3\2\2\2\u0119\u011a\7\67\2\2\u011a")
        buf.write("\u011b\5\u00a4S\2\u011b\u011c\7\'\2\2\u011c\u011e\3\2")
        buf.write("\2\2\u011d\u0113\3\2\2\2\u011d\u0119\3\2\2\2\u011e#\3")
        buf.write("\2\2\2\u011f\u0120\t\2\2\2\u0120\u0121\7/\2\2\u0121\u0122")
        buf.write("\5\u0094K\2\u0122\u0123\7\60\2\2\u0123\u0124\5X-\2\u0124")
        buf.write("%\3\2\2\2\u0125\u0126\5*\26\2\u0126\u0127\5,\27\2\u0127")
        buf.write("\u0128\5\60\31\2\u0128\u0129\78\2\2\u0129\'\3\2\2\2\u012a")
        buf.write("\u012b\5*\26\2\u012b\u012c\5,\27\2\u012c\u012d\5\60\31")
        buf.write("\2\u012d)\3\2\2\2\u012e\u0131\t\2\2\2\u012f\u0132\5~@")
        buf.write("\2\u0130\u0132\3\2\2\2\u0131\u012f\3\2\2\2\u0131\u0130")
        buf.write("\3\2\2\2\u0132\u0136\3\2\2\2\u0133\u0134\7\34\2\2\u0134")
        buf.write("\u0137\7:\2\2\u0135\u0137\3\2\2\2\u0136\u0133\3\2\2\2")
        buf.write("\u0136\u0135\3\2\2\2\u0137+\3\2\2\2\u0138\u0139\5.\30")
        buf.write("\2\u0139\u013a\5,\27\2\u013a\u013e\3\2\2\2\u013b\u013e")
        buf.write("\5.\30\2\u013c\u013e\3\2\2\2\u013d\u0138\3\2\2\2\u013d")
        buf.write("\u013b\3\2\2\2\u013d\u013c\3\2\2\2\u013e-\3\2\2\2\u013f")
        buf.write("\u0146\7\65\2\2\u0140\u0147\79\2\2\u0141\u0142\79\2\2")
        buf.write("\u0142\u0143\7/\2\2\u0143\u0144\5\u009cO\2\u0144\u0145")
        buf.write("\7\60\2\2\u0145\u0147\3\2\2\2\u0146\u0140\3\2\2\2\u0146")
        buf.write("\u0141\3\2\2\2\u0147/\3\2\2\2\u0148\u0149\7\65\2\2\u0149")
        buf.write("\u014a\79\2\2\u014a\u014b\7/\2\2\u014b\u014c\5\u009cO")
        buf.write("\2\u014c\u014d\7\60\2\2\u014d\61\3\2\2\2\u014e\u014f\5")
        buf.write("\64\33\2\u014f\u0150\7\'\2\2\u0150\u0151\5d\63\2\u0151")
        buf.write("\u0152\78\2\2\u0152\63\3\2\2\2\u0153\u0157\79\2\2\u0154")
        buf.write("\u0157\5B\"\2\u0155\u0157\5F$\2\u0156\u0153\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0155\3\2\2\2\u0157\u015a\3\2\2\2")
        buf.write("\u0158\u015b\5~@\2\u0159\u015b\3\2\2\2\u015a\u0158\3\2")
        buf.write("\2\2\u015a\u0159\3\2\2\2\u015b\65\3\2\2\2\u015c\u015d")
        buf.write("\7\5\2\2\u015d\u015e\7/\2\2\u015e\u015f\5d\63\2\u015f")
        buf.write("\u0160\7\60\2\2\u0160\u0167\5X-\2\u0161\u0162\58\35\2")
        buf.write("\u0162\u0163\5<\37\2\u0163\u0168\3\2\2\2\u0164\u0168\5")
        buf.write("8\35\2\u0165\u0168\5<\37\2\u0166\u0168\3\2\2\2\u0167\u0161")
        buf.write("\3\2\2\2\u0167\u0164\3\2\2\2\u0167\u0165\3\2\2\2\u0167")
        buf.write("\u0166\3\2\2\2\u0168\67\3\2\2\2\u0169\u016a\5:\36\2\u016a")
        buf.write("\u016b\58\35\2\u016b\u016e\3\2\2\2\u016c\u016e\5:\36\2")
        buf.write("\u016d\u0169\3\2\2\2\u016d\u016c\3\2\2\2\u016e9\3\2\2")
        buf.write("\2\u016f\u0170\7\6\2\2\u0170\u0171\7/\2\2\u0171\u0172")
        buf.write("\5d\63\2\u0172\u0173\7\60\2\2\u0173\u0174\5X-\2\u0174")
        buf.write(";\3\2\2\2\u0175\u0176\7\7\2\2\u0176\u0177\5X-\2\u0177")
        buf.write("=\3\2\2\2\u0178\u0179\7\32\2\2\u0179\u017c\5d\63\2\u017a")
        buf.write("\u017c\3\2\2\2\u017b\u0178\3\2\2\2\u017b\u017a\3\2\2\2")
        buf.write("\u017c?\3\2\2\2\u017d\u017e\7\b\2\2\u017e\u017f\7/\2\2")
        buf.write("\u017f\u0180\t\2\2\2\u0180\u0181\7\r\2\2\u0181\u0182\5")
        buf.write("d\63\2\u0182\u0183\7\35\2\2\u0183\u0184\5d\63\2\u0184")
        buf.write("\u0185\5> \2\u0185\u0186\7\60\2\2\u0186\u0187\5X-\2\u0187")
        buf.write("A\3\2\2\2\u0188\u0189\5d\63\2\u0189\u018a\7\65\2\2\u018a")
        buf.write("\u018b\79\2\2\u018bC\3\2\2\2\u018c\u018d\5d\63\2\u018d")
        buf.write("\u018e\7\65\2\2\u018e\u018f\79\2\2\u018f\u0190\7/\2\2")
        buf.write("\u0190\u0191\5\u008cG\2\u0191\u0192\7\60\2\2\u0192E\3")
        buf.write("\2\2\2\u0193\u0194\t\2\2\2\u0194\u0195\7\34\2\2\u0195")
        buf.write("\u0196\7:\2\2\u0196G\3\2\2\2\u0197\u0198\t\2\2\2\u0198")
        buf.write("\u0199\7\34\2\2\u0199\u019a\7:\2\2\u019a\u019b\7/\2\2")
        buf.write("\u019b\u019c\5\u008cG\2\u019c\u019d\7\60\2\2\u019dI\3")
        buf.write("\2\2\2\u019e\u01a1\5D#\2\u019f\u01a1\5H%\2\u01a0\u019e")
        buf.write("\3\2\2\2\u01a0\u019f\3\2\2\2\u01a1K\3\2\2\2\u01a2\u01a3")
        buf.write("\5J&\2\u01a3\u01a4\78\2\2\u01a4M\3\2\2\2\u01a5\u01a6\7")
        buf.write("\3\2\2\u01a6\u01a7\78\2\2\u01a7O\3\2\2\2\u01a8\u01a9\7")
        buf.write("\4\2\2\u01a9\u01aa\78\2\2\u01aaQ\3\2\2\2\u01ab\u01ae\5")
        buf.write("d\63\2\u01ac\u01ae\3\2\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac")
        buf.write("\3\2\2\2\u01aeS\3\2\2\2\u01af\u01b0\7\22\2\2\u01b0\u01b1")
        buf.write("\5R*\2\u01b1\u01b2\78\2\2\u01b2U\3\2\2\2\u01b3\u01b4\7")
        buf.write("\63\2\2\u01b4\u01b5\5\\/\2\u01b5\u01b6\7\64\2\2\u01b6")
        buf.write("W\3\2\2\2\u01b7\u01b8\7\63\2\2\u01b8\u01b9\5^\60\2\u01b9")
        buf.write("\u01ba\7\64\2\2\u01baY\3\2\2\2\u01bb\u01bc\7\63\2\2\u01bc")
        buf.write("\u01bd\5^\60\2\u01bd\u01be\7\22\2\2\u01be\u01bf\78\2\2")
        buf.write("\u01bf\u01c0\7\64\2\2\u01c0[\3\2\2\2\u01c1\u01c2\5`\61")
        buf.write("\2\u01c2\u01c3\5\\/\2\u01c3\u01c7\3\2\2\2\u01c4\u01c7")
        buf.write("\5`\61\2\u01c5\u01c7\3\2\2\2\u01c6\u01c1\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7]\3\2\2\2\u01c8")
        buf.write("\u01c9\5b\62\2\u01c9\u01ca\5^\60\2\u01ca\u01ce\3\2\2\2")
        buf.write("\u01cb\u01ce\5b\62\2\u01cc\u01ce\3\2\2\2\u01cd\u01c8\3")
        buf.write("\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01cc\3\2\2\2\u01ce_")
        buf.write("\3\2\2\2\u01cf\u01d4\5\32\16\2\u01d0\u01d4\5$\23\2\u01d1")
        buf.write("\u01d4\5\n\6\2\u01d2\u01d4\5\f\7\2\u01d3\u01cf\3\2\2\2")
        buf.write("\u01d3\u01d0\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d2\3")
        buf.write("\2\2\2\u01d4a\3\2\2\2\u01d5\u01df\5\20\t\2\u01d6\u01df")
        buf.write("\5\62\32\2\u01d7\u01df\5\66\34\2\u01d8\u01df\5@!\2\u01d9")
        buf.write("\u01df\5&\24\2\u01da\u01df\5L\'\2\u01db\u01df\5N(\2\u01dc")
        buf.write("\u01df\5P)\2\u01dd\u01df\5T+\2\u01de\u01d5\3\2\2\2\u01de")
        buf.write("\u01d6\3\2\2\2\u01de\u01d7\3\2\2\2\u01de\u01d8\3\2\2\2")
        buf.write("\u01de\u01d9\3\2\2\2\u01de\u01da\3\2\2\2\u01de\u01db\3")
        buf.write("\2\2\2\u01de\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01dfc")
        buf.write("\3\2\2\2\u01e0\u01e1\5f\64\2\u01e1\u01e2\t\4\2\2\u01e2")
        buf.write("\u01e3\5f\64\2\u01e3\u01e6\3\2\2\2\u01e4\u01e6\5f\64\2")
        buf.write("\u01e5\u01e0\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6e\3\2\2")
        buf.write("\2\u01e7\u01e8\5h\65\2\u01e8\u01e9\t\5\2\2\u01e9\u01ea")
        buf.write("\5h\65\2\u01ea\u01ed\3\2\2\2\u01eb\u01ed\5h\65\2\u01ec")
        buf.write("\u01e7\3\2\2\2\u01ec\u01eb\3\2\2\2\u01edg\3\2\2\2\u01ee")
        buf.write("\u01ef\b\65\1\2\u01ef\u01f0\5j\66\2\u01f0\u01f6\3\2\2")
        buf.write("\2\u01f1\u01f2\f\4\2\2\u01f2\u01f3\t\6\2\2\u01f3\u01f5")
        buf.write("\5j\66\2\u01f4\u01f1\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7i\3\2\2\2\u01f8")
        buf.write("\u01f6\3\2\2\2\u01f9\u01fa\b\66\1\2\u01fa\u01fb\5l\67")
        buf.write("\2\u01fb\u0201\3\2\2\2\u01fc\u01fd\f\4\2\2\u01fd\u01fe")
        buf.write("\t\7\2\2\u01fe\u0200\5l\67\2\u01ff\u01fc\3\2\2\2\u0200")
        buf.write("\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2")
        buf.write("\u0202k\3\2\2\2\u0203\u0201\3\2\2\2\u0204\u0205\b\67\1")
        buf.write("\2\u0205\u0206\5n8\2\u0206\u020c\3\2\2\2\u0207\u0208\f")
        buf.write("\4\2\2\u0208\u0209\t\b\2\2\u0209\u020b\5n8\2\u020a\u0207")
        buf.write("\3\2\2\2\u020b\u020e\3\2\2\2\u020c\u020a\3\2\2\2\u020c")
        buf.write("\u020d\3\2\2\2\u020dm\3\2\2\2\u020e\u020c\3\2\2\2\u020f")
        buf.write("\u0210\7#\2\2\u0210\u0213\5n8\2\u0211\u0213\5p9\2\u0212")
        buf.write("\u020f\3\2\2\2\u0212\u0211\3\2\2\2\u0213o\3\2\2\2\u0214")
        buf.write("\u0215\7\37\2\2\u0215\u0218\5p9\2\u0216\u0218\5r:\2\u0217")
        buf.write("\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218q\3\2\2\2\u0219")
        buf.write("\u021a\b:\1\2\u021a\u021b\5t;\2\u021b\u0220\3\2\2\2\u021c")
        buf.write("\u021d\f\4\2\2\u021d\u021f\5~@\2\u021e\u021c\3\2\2\2\u021f")
        buf.write("\u0222\3\2\2\2\u0220\u021e\3\2\2\2\u0220\u0221\3\2\2\2")
        buf.write("\u0221s\3\2\2\2\u0222\u0220\3\2\2\2\u0223\u0224\b;\1\2")
        buf.write("\u0224\u0225\5v<\2\u0225\u022e\3\2\2\2\u0226\u0229\f\4")
        buf.write("\2\2\u0227\u022a\5~@\2\u0228\u022a\3\2\2\2\u0229\u0227")
        buf.write("\3\2\2\2\u0229\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b")
        buf.write("\u022d\5\u0084C\2\u022c\u0226\3\2\2\2\u022d\u0230\3\2")
        buf.write("\2\2\u022e\u022c\3\2\2\2\u022e\u022f\3\2\2\2\u022fu\3")
        buf.write("\2\2\2\u0230\u022e\3\2\2\2\u0231\u0232\79\2\2\u0232\u0235")
        buf.write("\5\u0088E\2\u0233\u0235\5x=\2\u0234\u0231\3\2\2\2\u0234")
        buf.write("\u0233\3\2\2\2\u0235w\3\2\2\2\u0236\u0237\7\31\2\2\u0237")
        buf.write("\u0238\5d\63\2\u0238\u0239\7/\2\2\u0239\u023a\5\u008c")
        buf.write("G\2\u023a\u023b\7\60\2\2\u023b\u023e\3\2\2\2\u023c\u023e")
        buf.write("\5z>\2\u023d\u0236\3\2\2\2\u023d\u023c\3\2\2\2\u023ey")
        buf.write("\3\2\2\2\u023f\u0244\5\u0092J\2\u0240\u0244\79\2\2\u0241")
        buf.write("\u0244\7\33\2\2\u0242\u0244\5|?\2\u0243\u023f\3\2\2\2")
        buf.write("\u0243\u0240\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0242\3")
        buf.write("\2\2\2\u0244{\3\2\2\2\u0245\u0246\7/\2\2\u0246\u0247\5")
        buf.write("d\63\2\u0247\u0248\7\60\2\2\u0248}\3\2\2\2\u0249\u024a")
        buf.write("\b@\1\2\u024a\u024b\7\61\2\2\u024b\u024c\5d\63\2\u024c")
        buf.write("\u024d\7\62\2\2\u024d\u0255\3\2\2\2\u024e\u024f\f\4\2")
        buf.write("\2\u024f\u0250\7\61\2\2\u0250\u0251\5d\63\2\u0251\u0252")
        buf.write("\7\62\2\2\u0252\u0254\3\2\2\2\u0253\u024e\3\2\2\2\u0254")
        buf.write("\u0257\3\2\2\2\u0255\u0253\3\2\2\2\u0255\u0256\3\2\2\2")
        buf.write("\u0256\177\3\2\2\2\u0257\u0255\3\2\2\2\u0258\u025d\5\u0082")
        buf.write("B\2\u0259\u025a\5\u0082B\2\u025a\u025b\5~@\2\u025b\u025d")
        buf.write("\3\2\2\2\u025c\u0258\3\2\2\2\u025c\u0259\3\2\2\2\u025d")
        buf.write("\u0081\3\2\2\2\u025e\u0265\t\2\2\2\u025f\u0260\5d\63\2")
        buf.write("\u0260\u0261\5B\"\2\u0261\u0262\t\2\2\2\u0262\u0265\3")
        buf.write("\2\2\2\u0263\u0265\3\2\2\2\u0264\u025e\3\2\2\2\u0264\u025f")
        buf.write("\3\2\2\2\u0264\u0263\3\2\2\2\u0265\u0083\3\2\2\2\u0266")
        buf.write("\u0267\5\u0086D\2\u0267\u0268\5\u0084C\2\u0268\u026b\3")
        buf.write("\2\2\2\u0269\u026b\5\u0086D\2\u026a\u0266\3\2\2\2\u026a")
        buf.write("\u0269\3\2\2\2\u026b\u0085\3\2\2\2\u026c\u026d\7\65\2")
        buf.write("\2\u026d\u0275\79\2\2\u026e\u026f\7\65\2\2\u026f\u0270")
        buf.write("\79\2\2\u0270\u0271\7/\2\2\u0271\u0272\5\u008cG\2\u0272")
        buf.write("\u0273\7\60\2\2\u0273\u0275\3\2\2\2\u0274\u026c\3\2\2")
        buf.write("\2\u0274\u026e\3\2\2\2\u0275\u0087\3\2\2\2\u0276\u0277")
        buf.write("\5\u008aF\2\u0277\u0278\5\u0088E\2\u0278\u027b\3\2\2\2")
        buf.write("\u0279\u027b\5\u008aF\2\u027a\u0276\3\2\2\2\u027a\u0279")
        buf.write("\3\2\2\2\u027b\u0089\3\2\2\2\u027c\u027d\7\34\2\2\u027d")
        buf.write("\u0285\7:\2\2\u027e\u027f\7\34\2\2\u027f\u0280\7:\2\2")
        buf.write("\u0280\u0281\7/\2\2\u0281\u0282\5\u008cG\2\u0282\u0283")
        buf.write("\7\60\2\2\u0283\u0285\3\2\2\2\u0284\u027c\3\2\2\2\u0284")
        buf.write("\u027e\3\2\2\2\u0285\u008b\3\2\2\2\u0286\u0287\5d\63\2")
        buf.write("\u0287\u0288\7\66\2\2\u0288\u0289\5\u008cG\2\u0289\u028d")
        buf.write("\3\2\2\2\u028a\u028d\5d\63\2\u028b\u028d\3\2\2\2\u028c")
        buf.write("\u0286\3\2\2\2\u028c\u028a\3\2\2\2\u028c\u028b\3\2\2\2")
        buf.write("\u028d\u008d\3\2\2\2\u028e\u028f\7\f\2\2\u028f\u0290\7")
        buf.write("/\2\2\u0290\u0291\5\u0090I\2\u0291\u0292\7\60\2\2\u0292")
        buf.write("\u008f\3\2\2\2\u0293\u0294\5d\63\2\u0294\u0295\7\66\2")
        buf.write("\2\u0295\u0296\5\u0090I\2\u0296\u029a\3\2\2\2\u0297\u029a")
        buf.write("\5d\63\2\u0298\u029a\3\2\2\2\u0299\u0293\3\2\2\2\u0299")
        buf.write("\u0297\3\2\2\2\u0299\u0298\3\2\2\2\u029a\u0091\3\2\2\2")
        buf.write("\u029b\u02a2\7=\2\2\u029c\u02a2\7>\2\2\u029d\u02a2\7<")
        buf.write("\2\2\u029e\u02a2\7\t\2\2\u029f\u02a2\7;\2\2\u02a0\u02a2")
        buf.write("\5\u008eH\2\u02a1\u029b\3\2\2\2\u02a1\u029c\3\2\2\2\u02a1")
        buf.write("\u029d\3\2\2\2\u02a1\u029e\3\2\2\2\u02a1\u029f\3\2\2\2")
        buf.write("\u02a1\u02a0\3\2\2\2\u02a2\u0093\3\2\2\2\u02a3\u02a4\5")
        buf.write("\u0096L\2\u02a4\u02a5\78\2\2\u02a5\u02a6\5\u0094K\2\u02a6")
        buf.write("\u02aa\3\2\2\2\u02a7\u02aa\5\u0096L\2\u02a8\u02aa\3\2")
        buf.write("\2\2\u02a9\u02a3\3\2\2\2\u02a9\u02a7\3\2\2\2\u02a9\u02a8")
        buf.write("\3\2\2\2\u02aa\u0095\3\2\2\2\u02ab\u02ac\5\u0098M\2\u02ac")
        buf.write("\u02ad\7\67\2\2\u02ad\u02ae\5\u00a4S\2\u02ae\u0097\3\2")
        buf.write("\2\2\u02af\u02b0\t\2\2\2\u02b0\u02b1\7\66\2\2\u02b1\u02b5")
        buf.write("\5\u0098M\2\u02b2\u02b5\t\2\2\2\u02b3\u02b5\3\2\2\2\u02b4")
        buf.write("\u02af\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b3\3\2\2\2")
        buf.write("\u02b5\u0099\3\2\2\2\u02b6\u02b7\79\2\2\u02b7\u02b8\7")
        buf.write("\66\2\2\u02b8\u02bc\5\u009aN\2\u02b9\u02bc\79\2\2\u02ba")
        buf.write("\u02bc\3\2\2\2\u02bb\u02b6\3\2\2\2\u02bb\u02b9\3\2\2\2")
        buf.write("\u02bb\u02ba\3\2\2\2\u02bc\u009b\3\2\2\2\u02bd\u02c0\5")
        buf.write("\u0092J\2\u02be\u02c0\5d\63\2\u02bf\u02bd\3\2\2\2\u02bf")
        buf.write("\u02be\3\2\2\2\u02c0\u02c1\3\2\2\2\u02c1\u02c2\7\66\2")
        buf.write("\2\u02c2\u02c3\5\u009cO\2\u02c3\u02ca\3\2\2\2\u02c4\u02c7")
        buf.write("\5\u0092J\2\u02c5\u02c7\5d\63\2\u02c6\u02c4\3\2\2\2\u02c6")
        buf.write("\u02c5\3\2\2\2\u02c7\u02ca\3\2\2\2\u02c8\u02ca\3\2\2\2")
        buf.write("\u02c9\u02bf\3\2\2\2\u02c9\u02c6\3\2\2\2\u02c9\u02c8\3")
        buf.write("\2\2\2\u02ca\u009d\3\2\2\2\u02cb\u02cc\7\f\2\2\u02cc\u02cd")
        buf.write("\7\61\2\2\u02cd\u02ce\5\u00a0Q\2\u02ce\u02cf\7\66\2\2")
        buf.write("\u02cf\u02d0\7=\2\2\u02d0\u02d1\7\62\2\2\u02d1\u009f\3")
        buf.write("\2\2\2\u02d2\u02d8\5\u009eP\2\u02d3\u02d8\7\16\2\2\u02d4")
        buf.write("\u02d8\7\17\2\2\u02d5\u02d8\7\20\2\2\u02d6\u02d8\7\21")
        buf.write("\2\2\u02d7\u02d2\3\2\2\2\u02d7\u02d3\3\2\2\2\u02d7\u02d4")
        buf.write("\3\2\2\2\u02d7\u02d5\3\2\2\2\u02d7\u02d6\3\2\2\2\u02d8")
        buf.write("\u00a1\3\2\2\2\u02d9\u02da\t\t\2\2\u02da\u00a3\3\2\2\2")
        buf.write("\u02db\u02df\5\u00a2R\2\u02dc\u02df\5\u009eP\2\u02dd\u02df")
        buf.write("\79\2\2\u02de\u02db\3\2\2\2\u02de\u02dc\3\2\2\2\u02de")
        buf.write("\u02dd\3\2\2\2\u02df\u00a5\3\2\2\2<\u00ae\u00b8\u00ce")
        buf.write("\u00d6\u00dd\u00e7\u00f3\u00f8\u0100\u0107\u0111\u011d")
        buf.write("\u0131\u0136\u013d\u0146\u0156\u015a\u0167\u016d\u017b")
        buf.write("\u01a0\u01ad\u01c6\u01cd\u01d3\u01de\u01e5\u01ec\u01f6")
        buf.write("\u0201\u020c\u0212\u0217\u0220\u0229\u022e\u0234\u023d")
        buf.write("\u0243\u0255\u025c\u0264\u026a\u0274\u027a\u0284\u028c")
        buf.write("\u0299\u02a1\u02a9\u02b4\u02bb\u02bf\u02c6\u02c9\u02d7")
        buf.write("\u02de")
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
            self.state = 172
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
        self.enterRule(localctx, 4, self.RULE_class_declaration)
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
        self.enterRule(localctx, 12, self.RULE_method_declaration)
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


        def no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.No_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = D96Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_variable_declaration)
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
            self.state = 204
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 202
                self.declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 203
                self.no_value_assign_declare_list()
                pass


            self.state = 206
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class No_value_assign_declare_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def no_value_assign_declare(self):
            return self.getTypedRuleContext(D96Parser.No_value_assign_declareContext,0)


        def no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.No_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_no_value_assign_declare_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_value_assign_declare_list" ):
                return visitor.visitNo_value_assign_declare_list(self)
            else:
                return visitor.visitChildren(self)




    def no_value_assign_declare_list(self):

        localctx = D96Parser.No_value_assign_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_no_value_assign_declare_list)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 208
                self.no_value_assign_declare()
                self.state = 209
                self.no_value_assign_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNo_value_assign_declare" ):
                return visitor.visitNo_value_assign_declare(self)
            else:
                return visitor.visitChildren(self)




    def no_value_assign_declare(self):

        localctx = D96Parser.No_value_assign_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_no_value_assign_declare)
        try:
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 215
                self.match(D96Parser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(D96Parser.COLON)
                self.state = 218
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclare_initiate_list" ):
                return visitor.visitDeclare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def declare_initiate_list(self):

        localctx = D96Parser.Declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_declare_initiate_list)
        try:
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 221
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 222
                self.type_and_assign()
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_and_assign" ):
                return visitor.visitType_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def type_and_assign(self):

        localctx = D96Parser.Type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_type_and_assign)
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
                self.type_and_assign()
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


    class Both_variable_declarationContext(ParserRuleContext):
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

        def both_declare_initiate_list(self):
            return self.getTypedRuleContext(D96Parser.Both_declare_initiate_listContext,0)


        def both_no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.Both_no_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_both_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoth_variable_declaration" ):
                return visitor.visitBoth_variable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def both_variable_declaration(self):

        localctx = D96Parser.Both_variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_both_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 244
                self.both_declare_initiate_list()
                pass

            elif la_ == 2:
                self.state = 245
                self.both_no_value_assign_declare_list()
                pass


            self.state = 248
            self.match(D96Parser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Both_no_value_assign_declare_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def both_no_value_assign_declare(self):
            return self.getTypedRuleContext(D96Parser.Both_no_value_assign_declareContext,0)


        def both_no_value_assign_declare_list(self):
            return self.getTypedRuleContext(D96Parser.Both_no_value_assign_declare_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_both_no_value_assign_declare_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoth_no_value_assign_declare_list" ):
                return visitor.visitBoth_no_value_assign_declare_list(self)
            else:
                return visitor.visitChildren(self)




    def both_no_value_assign_declare_list(self):

        localctx = D96Parser.Both_no_value_assign_declare_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_both_no_value_assign_declare_list)
        try:
            self.state = 254
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.both_no_value_assign_declare()
                self.state = 251
                self.both_no_value_assign_declare_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 253
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
            return D96Parser.RULE_both_no_value_assign_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoth_no_value_assign_declare" ):
                return visitor.visitBoth_no_value_assign_declare(self)
            else:
                return visitor.visitChildren(self)




    def both_no_value_assign_declare(self):

        localctx = D96Parser.Both_no_value_assign_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_both_no_value_assign_declare)
        self._la = 0 # Token type
        try:
            self.state = 261
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 257
                self.match(D96Parser.COMMA)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 258
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 259
                self.match(D96Parser.COLON)
                self.state = 260
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoth_declare_initiate_list" ):
                return visitor.visitBoth_declare_initiate_list(self)
            else:
                return visitor.visitChildren(self)




    def both_declare_initiate_list(self):

        localctx = D96Parser.Both_declare_initiate_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_both_declare_initiate_list)
        self._la = 0 # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 264
                self.both_type_and_assign()
                self.state = 265
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 267
                self.variable_in_func_identifier_list()
                self.state = 268
                self.match(D96Parser.COLON)
                self.state = 269
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoth_type_and_assign" ):
                return visitor.visitBoth_type_and_assign(self)
            else:
                return visitor.visitChildren(self)




    def both_type_and_assign(self):

        localctx = D96Parser.Both_type_and_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_both_type_and_assign)
        self._la = 0 # Token type
        try:
            self.state = 283
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COMMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 273
                self.match(D96Parser.COMMA)
                self.state = 274
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 275
                self.both_type_and_assign()
                self.state = 276
                self.expr()
                self.state = 277
                self.match(D96Parser.COMMA)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 279
                self.match(D96Parser.COLON)
                self.state = 280
                self.variable_type()
                self.state = 281
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
        self.enterRule(localctx, 34, self.RULE_function_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 286
            self.match(D96Parser.LB)
            self.state = 287
            self.list_parameters()
            self.state = 288
            self.match(D96Parser.RB)
            self.state = 289
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
        self.enterRule(localctx, 36, self.RULE_call_func_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            self.call_func_header()
            self.state = 292
            self.call_func_attr_list()
            self.state = 293
            self.call_func_end()
            self.state = 294
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
        self.enterRule(localctx, 38, self.RULE_call_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.call_func_header()
            self.state = 297
            self.call_func_attr_list()
            self.state = 298
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
        self.enterRule(localctx, 40, self.RULE_call_func_header)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 303
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 301
                self.index_operators(0)
                pass
            elif token in [D96Parser.DOUBLECOLONOP, D96Parser.DOT]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 308
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.DOUBLECOLONOP]:
                self.state = 305
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 306
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
        self.enterRule(localctx, 42, self.RULE_call_func_attr_list)
        try:
            self.state = 315
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.call_func_attr()
                self.state = 311
                self.call_func_attr_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 313
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
        self.enterRule(localctx, 44, self.RULE_call_func_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(D96Parser.DOT)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 318
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 319
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 320
                self.match(D96Parser.LB)
                self.state = 321
                self.value_list()
                self.state = 322
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
        self.enterRule(localctx, 46, self.RULE_call_func_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.DOT)
            self.state = 327
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 328
            self.match(D96Parser.LB)
            self.state = 329
            self.value_list()
            self.state = 330
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
        self.enterRule(localctx, 48, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.lhs()
            self.state = 333
            self.match(D96Parser.ASSIGNOP)
            self.state = 334
            self.expr()
            self.state = 335
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
        self.enterRule(localctx, 50, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 337
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 338
                self.instance_attr_access()
                pass

            elif la_ == 3:
                self.state = 339
                self.static_attr_access()
                pass


            self.state = 344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LSB]:
                self.state = 342
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
        self.enterRule(localctx, 52, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.match(D96Parser.IF)
            self.state = 347
            self.match(D96Parser.LB)
            self.state = 348
            self.expr()
            self.state = 349
            self.match(D96Parser.RB)
            self.state = 350
            self.block_statements()
            self.state = 357
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 351
                self.elseif_list_statements()
                self.state = 352
                self.else_statement()
                pass

            elif la_ == 2:
                self.state = 354
                self.elseif_list_statements()
                pass

            elif la_ == 3:
                self.state = 355
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
        self.enterRule(localctx, 54, self.RULE_elseif_list_statements)
        try:
            self.state = 363
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 359
                self.elseif_statement()
                self.state = 360
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
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
        self.enterRule(localctx, 56, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.match(D96Parser.ELSEIF)
            self.state = 366
            self.match(D96Parser.LB)
            self.state = 367
            self.expr()
            self.state = 368
            self.match(D96Parser.RB)
            self.state = 369
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
        self.enterRule(localctx, 58, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.match(D96Parser.ELSE)
            self.state = 372
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
        self.enterRule(localctx, 60, self.RULE_by_expr)
        try:
            self.state = 377
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(D96Parser.BY)
                self.state = 375
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
        self.enterRule(localctx, 62, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(D96Parser.FOREACH)
            self.state = 380
            self.match(D96Parser.LB)
            self.state = 381
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 382
            self.match(D96Parser.IN)
            self.state = 383
            self.expr()
            self.state = 384
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 385
            self.expr()
            self.state = 386
            self.by_expr()
            self.state = 387
            self.match(D96Parser.RB)
            self.state = 388
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
        self.enterRule(localctx, 64, self.RULE_instance_attr_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.expr()
            self.state = 391
            self.match(D96Parser.DOT)
            self.state = 392
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
        self.enterRule(localctx, 66, self.RULE_instance_method_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.expr()
            self.state = 395
            self.match(D96Parser.DOT)
            self.state = 396
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 397
            self.match(D96Parser.LB)
            self.state = 398
            self.list_expr()
            self.state = 399
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
        self.enterRule(localctx, 68, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 402
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 403
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
        self.enterRule(localctx, 70, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 406
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 407
            self.match(D96Parser.DOLLAR_IDENTIFIERS)
            self.state = 408
            self.match(D96Parser.LB)
            self.state = 409
            self.list_expr()
            self.state = 410
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
        self.enterRule(localctx, 72, self.RULE_method_invocation)
        try:
            self.state = 414
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 412
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 413
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
        self.enterRule(localctx, 74, self.RULE_method_invocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.method_invocation()
            self.state = 417
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
        self.enterRule(localctx, 76, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.match(D96Parser.BREAK)
            self.state = 420
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
        self.enterRule(localctx, 78, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(D96Parser.CONTINUE)
            self.state = 423
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
        self.enterRule(localctx, 80, self.RULE_return_expr)
        try:
            self.state = 427
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
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
        self.enterRule(localctx, 82, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 429
            self.match(D96Parser.RETURN)
            self.state = 430
            self.return_expr()
            self.state = 431
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
        self.enterRule(localctx, 84, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.match(D96Parser.LCB)
            self.state = 434
            self.statements_class()
            self.state = 435
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
        self.enterRule(localctx, 86, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(D96Parser.LCB)
            self.state = 438
            self.statements()
            self.state = 439
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
        self.enterRule(localctx, 88, self.RULE_block_statements_in_main)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.match(D96Parser.LCB)
            self.state = 442
            self.statements()
            self.state = 443
            self.match(D96Parser.RETURN)
            self.state = 444
            self.match(D96Parser.SEMICOLON)
            self.state = 445
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
        self.enterRule(localctx, 90, self.RULE_statements_class)
        try:
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.statement_class()
                self.state = 448
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
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
        self.enterRule(localctx, 92, self.RULE_statements)
        try:
            self.state = 459
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 454
                self.statement()
                self.state = 455
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_class" ):
                return visitor.visitStatement_class(self)
            else:
                return visitor.visitChildren(self)




    def statement_class(self):

        localctx = D96Parser.Statement_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_statement_class)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.VAL, D96Parser.VAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.both_variable_declaration()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
                self.function_declaration()
                pass
            elif token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 463
                self.constructor_dclr()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 464
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = D96Parser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_statement)
        try:
            self.state = 476
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 468
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 469
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 470
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 471
                self.call_func_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 472
                self.method_invocation_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 473
                self.break_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 474
                self.continue_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 475
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
        self.enterRule(localctx, 98, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 478
                self.expr1()
                self.state = 479
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 480
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 482
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
        self.enterRule(localctx, 100, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 490
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 485
                self.expr2(0)
                self.state = 486
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 487
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 489
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
        _startState = 102
        self.enterRecursionRule(localctx, 102, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 495
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 496
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 497
                    self.expr3(0) 
                self.state = 502
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
        _startState = 104
        self.enterRecursionRule(localctx, 104, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 506
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 507
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 508
                    self.expr4(0) 
                self.state = 513
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
        _startState = 106
        self.enterRecursionRule(localctx, 106, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 522
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 517
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 518
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 519
                    self.expr5() 
                self.state = 524
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
        self.enterRule(localctx, 108, self.RULE_expr5)
        try:
            self.state = 528
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.match(D96Parser.NOTOP)
                self.state = 526
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
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
        self.enterRule(localctx, 110, self.RULE_expr6)
        try:
            self.state = 533
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 530
                self.match(D96Parser.MINUSOP)
                self.state = 531
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 532
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
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 542
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 538
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 539
                    self.index_operators(0) 
                self.state = 544
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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_expr8, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 546
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 556
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 548
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 551
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [D96Parser.LSB]:
                        self.state = 549
                        self.index_operators(0)
                        pass
                    elif token in [D96Parser.DOT]:
                        pass
                    else:
                        raise NoViableAltException(self)

                    self.state = 553
                    self.instance_accesses() 
                self.state = 558
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

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
        self.enterRule(localctx, 116, self.RULE_expr9)
        try:
            self.state = 562
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 559
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 560
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 561
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
        self.enterRule(localctx, 118, self.RULE_expr10)
        try:
            self.state = 571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(D96Parser.NEW)
                self.state = 565
                self.expr()
                self.state = 566
                self.match(D96Parser.LB)
                self.state = 567
                self.list_expr()
                self.state = 568
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
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
        self.enterRule(localctx, 120, self.RULE_expr11)
        try:
            self.state = 577
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT_IN_ARRAY, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 573
                self.literal()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 574
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass
            elif token in [D96Parser.SELF]:
                self.enterOuterAlt(localctx, 3)
                self.state = 575
                self.match(D96Parser.SELF)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 4)
                self.state = 576
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
        self.enterRule(localctx, 122, self.RULE_expr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(D96Parser.LB)
            self.state = 580
            self.expr()
            self.state = 581
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
        _startState = 124
        self.enterRecursionRule(localctx, 124, self.RULE_index_operators, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(D96Parser.LSB)
            self.state = 585
            self.expr()
            self.state = 586
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 595
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Index_operatorsContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_index_operators)
                    self.state = 588
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 589
                    self.match(D96Parser.LSB)
                    self.state = 590
                    self.expr()
                    self.state = 591
                    self.match(D96Parser.RSB) 
                self.state = 597
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        self.enterRule(localctx, 126, self.RULE_index_expr)
        try:
            self.state = 602
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.index()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.index()
                self.state = 600
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
        self.enterRule(localctx, 128, self.RULE_index)
        self._la = 0 # Token type
        try:
            self.state = 610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 604
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.expr()
                self.state = 606
                self.instance_attr_access()
                self.state = 607
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
        self.enterRule(localctx, 130, self.RULE_instance_accesses)
        try:
            self.state = 616
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 612
                self.instance_access()
                self.state = 613
                self.instance_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 615
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
        self.enterRule(localctx, 132, self.RULE_instance_access)
        try:
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.match(D96Parser.DOT)
                self.state = 619
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
                self.match(D96Parser.DOT)
                self.state = 621
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 622
                self.match(D96Parser.LB)
                self.state = 623
                self.list_expr()
                self.state = 624
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
        self.enterRule(localctx, 134, self.RULE_static_accesses)
        try:
            self.state = 632
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 628
                self.static_access()
                self.state = 629
                self.static_accesses()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 631
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
        self.enterRule(localctx, 136, self.RULE_static_access)
        try:
            self.state = 642
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 634
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 635
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 636
                self.match(D96Parser.DOUBLECOLONOP)
                self.state = 637
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                self.state = 638
                self.match(D96Parser.LB)
                self.state = 639
                self.list_expr()
                self.state = 640
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
        self.enterRule(localctx, 138, self.RULE_list_expr)
        try:
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 644
                self.expr()
                self.state = 645
                self.match(D96Parser.COMMA)
                self.state = 646
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 648
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
        self.enterRule(localctx, 140, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            self.match(D96Parser.ARRAY)
            self.state = 653
            self.match(D96Parser.LB)
            self.state = 654
            self.array_val()
            self.state = 655
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
        self.enterRule(localctx, 142, self.RULE_array_val)
        try:
            self.state = 663
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 657
                self.expr()
                self.state = 658
                self.match(D96Parser.COMMA)
                self.state = 659
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 661
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
        self.enterRule(localctx, 144, self.RULE_literal)
        try:
            self.state = 671
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT_IN_ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 665
                self.match(D96Parser.INTLIT_IN_ARRAY)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 666
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 667
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 668
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 669
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 670
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
        self.enterRule(localctx, 146, self.RULE_list_parameters)
        try:
            self.state = 679
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 673
                self.param()
                self.state = 674
                self.match(D96Parser.SEMICOLON)
                self.state = 675
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 677
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
        self.enterRule(localctx, 148, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 681
            self.identifier_list()
            self.state = 682
            self.match(D96Parser.COLON)
            self.state = 683
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
        self.enterRule(localctx, 150, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 690
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 685
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 686
                self.match(D96Parser.COMMA)
                self.state = 687
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 688
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
        self.enterRule(localctx, 152, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 697
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 693
                self.match(D96Parser.COMMA)
                self.state = 694
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 695
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
        self.enterRule(localctx, 154, self.RULE_value_list)
        try:
            self.state = 711
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 701
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 699
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 700
                    self.expr()
                    pass


                self.state = 703
                self.match(D96Parser.COMMA)
                self.state = 704
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 708
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
                if la_ == 1:
                    self.state = 706
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 707
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
        self.enterRule(localctx, 156, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 713
            self.match(D96Parser.ARRAY)
            self.state = 714
            self.match(D96Parser.LSB)
            self.state = 715
            self.array_element_type()
            self.state = 716
            self.match(D96Parser.COMMA)
            self.state = 717
            self.match(D96Parser.INTLIT_IN_ARRAY)
            self.state = 718
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
        self.enterRule(localctx, 158, self.RULE_array_element_type)
        try:
            self.state = 725
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 720
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 722
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 723
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 724
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
        self.enterRule(localctx, 160, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 727
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
        self.enterRule(localctx, 162, self.RULE_variable_type)
        try:
            self.state = 732
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 729
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 730
                self.array_type()
                pass
            elif token in [D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 731
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
         




