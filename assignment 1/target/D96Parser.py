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
        buf.write("\u0231\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\5\4\u0091\n\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\5\6\u009b\n\6\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\5\17\u00d1\n\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22")
        buf.write("\u00e4\n\22\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\5\23\u00f0\n\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\5\24\u00fa\n\24\3\25\3\25\3\25\3\25\3\25\3")
        buf.write("\25\5\25\u0102\n\25\3\26\3\26\3\26\5\26\u0107\n\26\3\27")
        buf.write("\3\27\3\27\5\27\u010c\n\27\3\30\3\30\3\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\5\31\u011b\n\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\36\3\36\5\36\u012f\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3\"\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3#\3#\5#\u0148\n#\3$\3$\3$\3$\3$\5")
        buf.write("$\u014f\n$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\5%\u015b\n%\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u0166\n&\3\'\3\'\3\'\3\'")
        buf.write("\3\'\5\'\u016d\n\'\3(\3(\3(\3(\3(\5(\u0174\n(\3)\3)\3")
        buf.write(")\3)\3)\3)\7)\u017c\n)\f)\16)\u017f\13)\3*\3*\3*\3*\3")
        buf.write("*\3*\7*\u0187\n*\f*\16*\u018a\13*\3+\3+\3+\3+\3+\3+\7")
        buf.write("+\u0192\n+\f+\16+\u0195\13+\3,\3,\3,\5,\u019a\n,\3-\3")
        buf.write("-\3-\5-\u019f\n-\3.\3.\3.\3.\3.\7.\u01a6\n.\f.\16.\u01a9")
        buf.write("\13.\3/\3/\3/\3/\3/\3/\7/\u01b1\n/\f/\16/\u01b4\13/\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\3\60\5\60\u01bd\n\60\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\5\61\u01c6\n\61\3\62\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u01d5\n\63\3\64\3\64\3\64\3\64\3\64\3\64\5")
        buf.write("\64\u01dd\n\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\5\66\u01ea\n\66\3\67\3\67\3\67\3\67\3")
        buf.write("\67\5\67\u01f1\n\67\38\38\38\38\38\38\58\u01f9\n8\39\3")
        buf.write("9\39\39\3:\3:\3:\3:\3:\5:\u0204\n:\3;\3;\3;\3;\3;\5;\u020b")
        buf.write("\n;\3<\3<\5<\u020f\n<\3<\3<\3<\3<\3<\5<\u0216\n<\3<\5")
        buf.write("<\u0219\n<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\5>\u0227")
        buf.write("\n>\3?\3?\3@\3@\3A\3A\5A\u022f\nA\3A\2\7PRTZ\\B\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\2\f\4\2\34")
        buf.write("\34<=\3\2<=\3\2\26\27\3\2/\60\4\2((*.\3\2&\'\3\2 !\3\2")
        buf.write("\"$\4\2\36\36\67\67\3\2\17\22\2\u023c\2\u0082\3\2\2\2")
        buf.write("\4\u0087\3\2\2\2\6\u0090\3\2\2\2\b\u0092\3\2\2\2\n\u009a")
        buf.write("\3\2\2\2\f\u009c\3\2\2\2\16\u00a2\3\2\2\2\20\u00a7\3\2")
        buf.write("\2\2\22\u00ab\3\2\2\2\24\u00b2\3\2\2\2\26\u00b6\3\2\2")
        buf.write("\2\30\u00bd\3\2\2\2\32\u00c3\3\2\2\2\34\u00c9\3\2\2\2")
        buf.write("\36\u00d4\3\2\2\2 \u00da\3\2\2\2\"\u00e3\3\2\2\2$\u00e9")
        buf.write("\3\2\2\2&\u00f9\3\2\2\2(\u00fb\3\2\2\2*\u0103\3\2\2\2")
        buf.write(",\u010b\3\2\2\2.\u010d\3\2\2\2\60\u011a\3\2\2\2\62\u011e")
        buf.write("\3\2\2\2\64\u0123\3\2\2\2\66\u0126\3\2\2\28\u0129\3\2")
        buf.write("\2\2:\u012e\3\2\2\2<\u0130\3\2\2\2>\u0134\3\2\2\2@\u013a")
        buf.write("\3\2\2\2B\u013e\3\2\2\2D\u0147\3\2\2\2F\u014e\3\2\2\2")
        buf.write("H\u015a\3\2\2\2J\u0165\3\2\2\2L\u016c\3\2\2\2N\u0173\3")
        buf.write("\2\2\2P\u0175\3\2\2\2R\u0180\3\2\2\2T\u018b\3\2\2\2V\u0199")
        buf.write("\3\2\2\2X\u019e\3\2\2\2Z\u01a0\3\2\2\2\\\u01aa\3\2\2\2")
        buf.write("^\u01bc\3\2\2\2`\u01c5\3\2\2\2b\u01c7\3\2\2\2d\u01d4\3")
        buf.write("\2\2\2f\u01dc\3\2\2\2h\u01de\3\2\2\2j\u01e9\3\2\2\2l\u01f0")
        buf.write("\3\2\2\2n\u01f8\3\2\2\2p\u01fa\3\2\2\2r\u0203\3\2\2\2")
        buf.write("t\u020a\3\2\2\2v\u0218\3\2\2\2x\u021a\3\2\2\2z\u0226\3")
        buf.write("\2\2\2|\u0228\3\2\2\2~\u022a\3\2\2\2\u0080\u022e\3\2\2")
        buf.write("\2\u0082\u0083\5\6\4\2\u0083\u0084\5\4\3\2\u0084\u0085")
        buf.write("\5\6\4\2\u0085\u0086\7\2\2\3\u0086\3\3\2\2\2\u0087\u0088")
        buf.write("\7\25\2\2\u0088\u0089\7;\2\2\u0089\u008a\5> \2\u008a\5")
        buf.write("\3\2\2\2\u008b\u008c\5\b\5\2\u008c\u008d\5\6\4\2\u008d")
        buf.write("\u0091\3\2\2\2\u008e\u0091\5\b\5\2\u008f\u0091\3\2\2\2")
        buf.write("\u0090\u008b\3\2\2\2\u0090\u008e\3\2\2\2\u0090\u008f\3")
        buf.write("\2\2\2\u0091\7\3\2\2\2\u0092\u0093\7\25\2\2\u0093\u0094")
        buf.write("\7<\2\2\u0094\u0095\5\n\6\2\u0095\u0096\5@!\2\u0096\t")
        buf.write("\3\2\2\2\u0097\u0098\79\2\2\u0098\u009b\7<\2\2\u0099\u009b")
        buf.write("\3\2\2\2\u009a\u0097\3\2\2\2\u009a\u0099\3\2\2\2\u009b")
        buf.write("\13\3\2\2\2\u009c\u009d\7\30\2\2\u009d\u009e\7\61\2\2")
        buf.write("\u009e\u009f\5n8\2\u009f\u00a0\7\62\2\2\u00a0\u00a1\5")
        buf.write("B\"\2\u00a1\r\3\2\2\2\u00a2\u00a3\7\31\2\2\u00a3\u00a4")
        buf.write("\7\61\2\2\u00a4\u00a5\7\62\2\2\u00a5\u00a6\5B\"\2\u00a6")
        buf.write("\17\3\2\2\2\u00a7\u00a8\5L\'\2\u00a8\u00a9\7\67\2\2\u00a9")
        buf.write("\u00aa\t\2\2\2\u00aa\21\3\2\2\2\u00ab\u00ac\5L\'\2\u00ac")
        buf.write("\u00ad\7\67\2\2\u00ad\u00ae\t\2\2\2\u00ae\u00af\7\61\2")
        buf.write("\2\u00af\u00b0\5f\64\2\u00b0\u00b1\7\62\2\2\u00b1\23\3")
        buf.write("\2\2\2\u00b2\u00b3\5L\'\2\u00b3\u00b4\7\35\2\2\u00b4\u00b5")
        buf.write("\t\2\2\2\u00b5\25\3\2\2\2\u00b6\u00b7\5L\'\2\u00b7\u00b8")
        buf.write("\7\35\2\2\u00b8\u00b9\t\2\2\2\u00b9\u00ba\7\61\2\2\u00ba")
        buf.write("\u00bb\5f\64\2\u00bb\u00bc\7\62\2\2\u00bc\27\3\2\2\2\u00bd")
        buf.write("\u00be\7\32\2\2\u00be\u00bf\t\3\2\2\u00bf\u00c0\7\61\2")
        buf.write("\2\u00c0\u00c1\5f\64\2\u00c1\u00c2\7\62\2\2\u00c2\31\3")
        buf.write("\2\2\2\u00c3\u00c4\t\3\2\2\u00c4\u00c5\7\61\2\2\u00c5")
        buf.write("\u00c6\5n8\2\u00c6\u00c7\7\62\2\2\u00c7\u00c8\5B\"\2\u00c8")
        buf.write("\33\3\2\2\2\u00c9\u00ca\t\4\2\2\u00ca\u00cb\5r:\2\u00cb")
        buf.write("\u00cc\79\2\2\u00cc\u00d0\5\u0080A\2\u00cd\u00ce\7)\2")
        buf.write("\2\u00ce\u00d1\5v<\2\u00cf\u00d1\3\2\2\2\u00d0\u00cd\3")
        buf.write("\2\2\2\u00d0\u00cf\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3")
        buf.write("\7:\2\2\u00d3\35\3\2\2\2\u00d4\u00d5\t\3\2\2\u00d5\u00d6")
        buf.write("\7\61\2\2\u00d6\u00d7\5n8\2\u00d7\u00d8\7\62\2\2\u00d8")
        buf.write("\u00d9\5B\"\2\u00d9\37\3\2\2\2\u00da\u00db\7\3\2\2\u00db")
        buf.write("\u00dc\7\61\2\2\u00dc\u00dd\7\62\2\2\u00dd\u00de\5B\"")
        buf.write("\2\u00de!\3\2\2\2\u00df\u00e4\7<\2\2\u00e0\u00e4\7=\2")
        buf.write("\2\u00e1\u00e4\5\20\t\2\u00e2\u00e4\5\24\13\2\u00e3\u00df")
        buf.write("\3\2\2\2\u00e3\u00e0\3\2\2\2\u00e3\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e6\7)\2\2")
        buf.write("\u00e6\u00e7\5L\'\2\u00e7\u00e8\7:\2\2\u00e8#\3\2\2\2")
        buf.write("\u00e9\u00ea\7\6\2\2\u00ea\u00eb\7\61\2\2\u00eb\u00ec")
        buf.write("\5L\'\2\u00ec\u00ef\7\62\2\2\u00ed\u00f0\5B\"\2\u00ee")
        buf.write("\u00f0\3\2\2\2\u00ef\u00ed\3\2\2\2\u00ef\u00ee\3\2\2\2")
        buf.write("\u00f0\u00f1\3\2\2\2\u00f1\u00f2\5&\24\2\u00f2\u00f3\5")
        buf.write("*\26\2\u00f3%\3\2\2\2\u00f4\u00f5\5(\25\2\u00f5\u00f6")
        buf.write("\5&\24\2\u00f6\u00fa\3\2\2\2\u00f7\u00fa\5(\25\2\u00f8")
        buf.write("\u00fa\3\2\2\2\u00f9\u00f4\3\2\2\2\u00f9\u00f7\3\2\2\2")
        buf.write("\u00f9\u00f8\3\2\2\2\u00fa\'\3\2\2\2\u00fb\u00fc\7\7\2")
        buf.write("\2\u00fc\u00fd\7\61\2\2\u00fd\u00fe\5L\'\2\u00fe\u0101")
        buf.write("\7\62\2\2\u00ff\u0102\5B\"\2\u0100\u0102\3\2\2\2\u0101")
        buf.write("\u00ff\3\2\2\2\u0101\u0100\3\2\2\2\u0102)\3\2\2\2\u0103")
        buf.write("\u0106\7\b\2\2\u0104\u0107\5B\"\2\u0105\u0107\3\2\2\2")
        buf.write("\u0106\u0104\3\2\2\2\u0106\u0105\3\2\2\2\u0107+\3\2\2")
        buf.write("\2\u0108\u0109\7\33\2\2\u0109\u010c\5L\'\2\u010a\u010c")
        buf.write("\3\2\2\2\u010b\u0108\3\2\2\2\u010b\u010a\3\2\2\2\u010c")
        buf.write("-\3\2\2\2\u010d\u010e\7\t\2\2\u010e\u010f\7\61\2\2\u010f")
        buf.write("\u0110\t\3\2\2\u0110\u0111\7\16\2\2\u0111\u0112\5L\'\2")
        buf.write("\u0112\u0113\7\36\2\2\u0113\u0114\5L\'\2\u0114\u0115\5")
        buf.write(",\27\2\u0115\u0116\7\62\2\2\u0116\u0117\5B\"\2\u0117/")
        buf.write("\3\2\2\2\u0118\u011b\5\22\n\2\u0119\u011b\5\26\f\2\u011a")
        buf.write("\u0118\3\2\2\2\u011a\u0119\3\2\2\2\u011b\u011c\3\2\2\2")
        buf.write("\u011c\u011d\7:\2\2\u011d\61\3\2\2\2\u011e\u011f\t\3\2")
        buf.write("\2\u011f\u0120\7\61\2\2\u0120\u0121\5f\64\2\u0121\u0122")
        buf.write("\7\62\2\2\u0122\63\3\2\2\2\u0123\u0124\5\62\32\2\u0124")
        buf.write("\u0125\7:\2\2\u0125\65\3\2\2\2\u0126\u0127\7\4\2\2\u0127")
        buf.write("\u0128\7:\2\2\u0128\67\3\2\2\2\u0129\u012a\7\5\2\2\u012a")
        buf.write("\u012b\7:\2\2\u012b9\3\2\2\2\u012c\u012f\5L\'\2\u012d")
        buf.write("\u012f\3\2\2\2\u012e\u012c\3\2\2\2\u012e\u012d\3\2\2\2")
        buf.write("\u012f;\3\2\2\2\u0130\u0131\7\23\2\2\u0131\u0132\5:\36")
        buf.write("\2\u0132\u0133\7:\2\2\u0133=\3\2\2\2\u0134\u0135\7\65")
        buf.write("\2\2\u0135\u0136\5D#\2\u0136\u0137\5 \21\2\u0137\u0138")
        buf.write("\5D#\2\u0138\u0139\7\66\2\2\u0139?\3\2\2\2\u013a\u013b")
        buf.write("\7\65\2\2\u013b\u013c\5D#\2\u013c\u013d\7\66\2\2\u013d")
        buf.write("A\3\2\2\2\u013e\u013f\7\65\2\2\u013f\u0140\5F$\2\u0140")
        buf.write("\u0141\7\66\2\2\u0141C\3\2\2\2\u0142\u0143\5H%\2\u0143")
        buf.write("\u0144\5D#\2\u0144\u0148\3\2\2\2\u0145\u0148\5H%\2\u0146")
        buf.write("\u0148\3\2\2\2\u0147\u0142\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0146\3\2\2\2\u0148E\3\2\2\2\u0149\u014a\5J&\2")
        buf.write("\u014a\u014b\5F$\2\u014b\u014f\3\2\2\2\u014c\u014f\5J")
        buf.write("&\2\u014d\u014f\3\2\2\2\u014e\u0149\3\2\2\2\u014e\u014c")
        buf.write("\3\2\2\2\u014e\u014d\3\2\2\2\u014fG\3\2\2\2\u0150\u015b")
        buf.write("\5\34\17\2\u0151\u015b\5\36\20\2\u0152\u015b\5\"\22\2")
        buf.write("\u0153\u015b\5$\23\2\u0154\u015b\5.\30\2\u0155\u015b\5")
        buf.write("\60\31\2\u0156\u015b\5\64\33\2\u0157\u015b\5\66\34\2\u0158")
        buf.write("\u015b\58\35\2\u0159\u015b\5<\37\2\u015a\u0150\3\2\2\2")
        buf.write("\u015a\u0151\3\2\2\2\u015a\u0152\3\2\2\2\u015a\u0153\3")
        buf.write("\2\2\2\u015a\u0154\3\2\2\2\u015a\u0155\3\2\2\2\u015a\u0156")
        buf.write("\3\2\2\2\u015a\u0157\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u0159\3\2\2\2\u015bI\3\2\2\2\u015c\u0166\5\34\17\2\u015d")
        buf.write("\u0166\5\"\22\2\u015e\u0166\5$\23\2\u015f\u0166\5.\30")
        buf.write("\2\u0160\u0166\5\60\31\2\u0161\u0166\5\64\33\2\u0162\u0166")
        buf.write("\5\66\34\2\u0163\u0166\58\35\2\u0164\u0166\5<\37\2\u0165")
        buf.write("\u015c\3\2\2\2\u0165\u015d\3\2\2\2\u0165\u015e\3\2\2\2")
        buf.write("\u0165\u015f\3\2\2\2\u0165\u0160\3\2\2\2\u0165\u0161\3")
        buf.write("\2\2\2\u0165\u0162\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0164")
        buf.write("\3\2\2\2\u0166K\3\2\2\2\u0167\u0168\5N(\2\u0168\u0169")
        buf.write("\t\5\2\2\u0169\u016a\5N(\2\u016a\u016d\3\2\2\2\u016b\u016d")
        buf.write("\5N(\2\u016c\u0167\3\2\2\2\u016c\u016b\3\2\2\2\u016dM")
        buf.write("\3\2\2\2\u016e\u016f\5P)\2\u016f\u0170\t\6\2\2\u0170\u0171")
        buf.write("\5P)\2\u0171\u0174\3\2\2\2\u0172\u0174\5P)\2\u0173\u016e")
        buf.write("\3\2\2\2\u0173\u0172\3\2\2\2\u0174O\3\2\2\2\u0175\u0176")
        buf.write("\b)\1\2\u0176\u0177\5R*\2\u0177\u017d\3\2\2\2\u0178\u0179")
        buf.write("\f\4\2\2\u0179\u017a\t\7\2\2\u017a\u017c\5R*\2\u017b\u0178")
        buf.write("\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017eQ\3\2\2\2\u017f\u017d\3\2\2\2\u0180")
        buf.write("\u0181\b*\1\2\u0181\u0182\5T+\2\u0182\u0188\3\2\2\2\u0183")
        buf.write("\u0184\f\4\2\2\u0184\u0185\t\b\2\2\u0185\u0187\5T+\2\u0186")
        buf.write("\u0183\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189S\3\2\2\2\u018a\u0188\3\2\2")
        buf.write("\2\u018b\u018c\b+\1\2\u018c\u018d\5V,\2\u018d\u0193\3")
        buf.write("\2\2\2\u018e\u018f\f\4\2\2\u018f\u0190\t\t\2\2\u0190\u0192")
        buf.write("\5V,\2\u0191\u018e\3\2\2\2\u0192\u0195\3\2\2\2\u0193\u0191")
        buf.write("\3\2\2\2\u0193\u0194\3\2\2\2\u0194U\3\2\2\2\u0195\u0193")
        buf.write("\3\2\2\2\u0196\u0197\7%\2\2\u0197\u019a\5V,\2\u0198\u019a")
        buf.write("\5X-\2\u0199\u0196\3\2\2\2\u0199\u0198\3\2\2\2\u019aW")
        buf.write("\3\2\2\2\u019b\u019c\7!\2\2\u019c\u019f\5X-\2\u019d\u019f")
        buf.write("\5Z.\2\u019e\u019b\3\2\2\2\u019e\u019d\3\2\2\2\u019fY")
        buf.write("\3\2\2\2\u01a0\u01a1\b.\1\2\u01a1\u01a2\5\\/\2\u01a2\u01a7")
        buf.write("\3\2\2\2\u01a3\u01a4\f\4\2\2\u01a4\u01a6\5d\63\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7\u01a5\3\2\2\2")
        buf.write("\u01a7\u01a8\3\2\2\2\u01a8[\3\2\2\2\u01a9\u01a7\3\2\2")
        buf.write("\2\u01aa\u01ab\b/\1\2\u01ab\u01ac\5^\60\2\u01ac\u01b2")
        buf.write("\3\2\2\2\u01ad\u01ae\f\4\2\2\u01ae\u01af\t\n\2\2\u01af")
        buf.write("\u01b1\5^\60\2\u01b0\u01ad\3\2\2\2\u01b1\u01b4\3\2\2\2")
        buf.write("\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3]\3\2\2")
        buf.write("\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\7\32\2\2\u01b6\u01b7")
        buf.write("\t\3\2\2\u01b7\u01b8\7\61\2\2\u01b8\u01b9\5f\64\2\u01b9")
        buf.write("\u01ba\7\62\2\2\u01ba\u01bd\3\2\2\2\u01bb\u01bd\5`\61")
        buf.write("\2\u01bc\u01b5\3\2\2\2\u01bc\u01bb\3\2\2\2\u01bd_\3\2")
        buf.write("\2\2\u01be\u01c6\5l\67\2\u01bf\u01c6\7<\2\2\u01c0\u01c6")
        buf.write("\7=\2\2\u01c1\u01c6\7\34\2\2\u01c2\u01c6\5\62\32\2\u01c3")
        buf.write("\u01c6\5\30\r\2\u01c4\u01c6\5b\62\2\u01c5\u01be\3\2\2")
        buf.write("\2\u01c5\u01bf\3\2\2\2\u01c5\u01c0\3\2\2\2\u01c5\u01c1")
        buf.write("\3\2\2\2\u01c5\u01c2\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5")
        buf.write("\u01c4\3\2\2\2\u01c6a\3\2\2\2\u01c7\u01c8\7\61\2\2\u01c8")
        buf.write("\u01c9\5L\'\2\u01c9\u01ca\7\62\2\2\u01cac\3\2\2\2\u01cb")
        buf.write("\u01cc\7\63\2\2\u01cc\u01cd\5L\'\2\u01cd\u01ce\7\64\2")
        buf.write("\2\u01ce\u01d5\3\2\2\2\u01cf\u01d0\7\63\2\2\u01d0\u01d1")
        buf.write("\5L\'\2\u01d1\u01d2\7\64\2\2\u01d2\u01d3\5d\63\2\u01d3")
        buf.write("\u01d5\3\2\2\2\u01d4\u01cb\3\2\2\2\u01d4\u01cf\3\2\2\2")
        buf.write("\u01d5e\3\2\2\2\u01d6\u01d7\5L\'\2\u01d7\u01d8\78\2\2")
        buf.write("\u01d8\u01d9\5f\64\2\u01d9\u01dd\3\2\2\2\u01da\u01dd\5")
        buf.write("L\'\2\u01db\u01dd\3\2\2\2\u01dc\u01d6\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01db\3\2\2\2\u01ddg\3\2\2\2\u01de\u01df")
        buf.write("\7\r\2\2\u01df\u01e0\7\61\2\2\u01e0\u01e1\5j\66\2\u01e1")
        buf.write("\u01e2\7\62\2\2\u01e2i\3\2\2\2\u01e3\u01e4\5L\'\2\u01e4")
        buf.write("\u01e5\78\2\2\u01e5\u01e6\5j\66\2\u01e6\u01ea\3\2\2\2")
        buf.write("\u01e7\u01ea\5L\'\2\u01e8\u01ea\3\2\2\2\u01e9\u01e3\3")
        buf.write("\2\2\2\u01e9\u01e7\3\2\2\2\u01e9\u01e8\3\2\2\2\u01eak")
        buf.write("\3\2\2\2\u01eb\u01f1\7@\2\2\u01ec\u01f1\7?\2\2\u01ed\u01f1")
        buf.write("\7\n\2\2\u01ee\u01f1\7>\2\2\u01ef\u01f1\5h\65\2\u01f0")
        buf.write("\u01eb\3\2\2\2\u01f0\u01ec\3\2\2\2\u01f0\u01ed\3\2\2\2")
        buf.write("\u01f0\u01ee\3\2\2\2\u01f0\u01ef\3\2\2\2\u01f1m\3\2\2")
        buf.write("\2\u01f2\u01f3\5p9\2\u01f3\u01f4\7:\2\2\u01f4\u01f5\5")
        buf.write("n8\2\u01f5\u01f9\3\2\2\2\u01f6\u01f9\5p9\2\u01f7\u01f9")
        buf.write("\3\2\2\2\u01f8\u01f2\3\2\2\2\u01f8\u01f6\3\2\2\2\u01f8")
        buf.write("\u01f7\3\2\2\2\u01f9o\3\2\2\2\u01fa\u01fb\5r:\2\u01fb")
        buf.write("\u01fc\79\2\2\u01fc\u01fd\5\u0080A\2\u01fdq\3\2\2\2\u01fe")
        buf.write("\u01ff\t\3\2\2\u01ff\u0200\78\2\2\u0200\u0204\5r:\2\u0201")
        buf.write("\u0204\t\3\2\2\u0202\u0204\3\2\2\2\u0203\u01fe\3\2\2\2")
        buf.write("\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204s\3\2\2")
        buf.write("\2\u0205\u0206\7<\2\2\u0206\u0207\78\2\2\u0207\u020b\5")
        buf.write("t;\2\u0208\u020b\7<\2\2\u0209\u020b\3\2\2\2\u020a\u0205")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3\2\2\2\u020b")
        buf.write("u\3\2\2\2\u020c\u020f\5l\67\2\u020d\u020f\5L\'\2\u020e")
        buf.write("\u020c\3\2\2\2\u020e\u020d\3\2\2\2\u020f\u0210\3\2\2\2")
        buf.write("\u0210\u0211\78\2\2\u0211\u0212\5v<\2\u0212\u0219\3\2")
        buf.write("\2\2\u0213\u0216\5l\67\2\u0214\u0216\5L\'\2\u0215\u0213")
        buf.write("\3\2\2\2\u0215\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217")
        buf.write("\u0219\3\2\2\2\u0218\u020e\3\2\2\2\u0218\u0215\3\2\2\2")
        buf.write("\u0218\u0217\3\2\2\2\u0219w\3\2\2\2\u021a\u021b\7\r\2")
        buf.write("\2\u021b\u021c\7\63\2\2\u021c\u021d\5z>\2\u021d\u021e")
        buf.write("\78\2\2\u021e\u021f\5|?\2\u021f\u0220\7\64\2\2\u0220y")
        buf.write("\3\2\2\2\u0221\u0227\5x=\2\u0222\u0227\7\17\2\2\u0223")
        buf.write("\u0227\7\20\2\2\u0224\u0227\7\21\2\2\u0225\u0227\7\22")
        buf.write("\2\2\u0226\u0221\3\2\2\2\u0226\u0222\3\2\2\2\u0226\u0223")
        buf.write("\3\2\2\2\u0226\u0224\3\2\2\2\u0226\u0225\3\2\2\2\u0227")
        buf.write("{\3\2\2\2\u0228\u0229\7@\2\2\u0229}\3\2\2\2\u022a\u022b")
        buf.write("\t\13\2\2\u022b\177\3\2\2\2\u022c\u022f\5~@\2\u022d\u022f")
        buf.write("\5x=\2\u022e\u022c\3\2\2\2\u022e\u022d\3\2\2\2\u022f\u0081")
        buf.write("\3\2\2\2(\u0090\u009a\u00d0\u00e3\u00ef\u00f9\u0101\u0106")
        buf.write("\u010b\u011a\u012e\u0147\u014e\u015a\u0165\u016c\u0173")
        buf.write("\u017d\u0188\u0193\u0199\u019e\u01a7\u01b2\u01bc\u01c5")
        buf.write("\u01d4\u01dc\u01e9\u01f0\u01f8\u0203\u020a\u020e\u0215")
        buf.write("\u0218\u0226\u022e")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "<INVALID>", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'::'", "'..'", "'_'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'=='", 
                     "'='", "'!='", "'>='", "'<='", "'>'", "'<'", "'==.'", 
                     "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
                     "','", "':'", "';'", "'Program'" ]

    symbolicNames = [ "<INVALID>", "MAIN", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                      "ELSE", "FOREACH", "BOOLLIT", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", 
                      "UNDERSCORE", "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", 
                      "MODULOOP", "NOTOP", "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", 
                      "NOTEQUALOP", "GTE", "LTE", "GT", "LT", "STREQUALOP", 
                      "STRCONCATOP", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                      "DOT", "COMMA", "COLON", "SEMICOLON", "PROGRAM", "VARIABLE_IN_FUNC_IDENTIFIERS", 
                      "DOLLAR_IDENTIFIERS", "STRINGLIT", "FLOATLIT", "INTLIT", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "BLOCK_COMMENT", 
                      "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_class_main_program_declarations = 1
    RULE_class_declarations = 2
    RULE_class_declaration = 3
    RULE_class_inheritance = 4
    RULE_constructor_dclr = 5
    RULE_destructor_dclr = 6
    RULE_instance_attr_access = 7
    RULE_instance_method_access = 8
    RULE_static_attr_access = 9
    RULE_static_method_access = 10
    RULE_obj_creation = 11
    RULE_method_declaration = 12
    RULE_variable_declaration = 13
    RULE_function_declaration = 14
    RULE_main_function_declaration = 15
    RULE_assignment_statements = 16
    RULE_if_statements = 17
    RULE_elseif_list_statements = 18
    RULE_elseif_statement = 19
    RULE_else_statement = 20
    RULE_by_expr = 21
    RULE_forin_statements = 22
    RULE_methodinvocation_statement = 23
    RULE_call_func = 24
    RULE_call_func_statement = 25
    RULE_break_statements = 26
    RULE_continue_statements = 27
    RULE_return_expr = 28
    RULE_return_statements = 29
    RULE_program_block_class_statements = 30
    RULE_block_class_statements = 31
    RULE_block_statements = 32
    RULE_statements_class = 33
    RULE_statements = 34
    RULE_statement_class = 35
    RULE_statement = 36
    RULE_expr = 37
    RULE_expr1 = 38
    RULE_expr2 = 39
    RULE_expr3 = 40
    RULE_expr4 = 41
    RULE_expr5 = 42
    RULE_expr6 = 43
    RULE_expr7 = 44
    RULE_expr8 = 45
    RULE_expr9 = 46
    RULE_expr10 = 47
    RULE_expr11 = 48
    RULE_index_operators = 49
    RULE_list_expr = 50
    RULE_array_lit = 51
    RULE_array_val = 52
    RULE_literal = 53
    RULE_list_parameters = 54
    RULE_param = 55
    RULE_identifier_list = 56
    RULE_variable_in_func_identifier_list = 57
    RULE_value_list = 58
    RULE_array_type = 59
    RULE_array_element_type = 60
    RULE_array_size = 61
    RULE_primitive_type = 62
    RULE_variable_type = 63

    ruleNames =  [ "program", "class_main_program_declarations", "class_declarations", 
                   "class_declaration", "class_inheritance", "constructor_dclr", 
                   "destructor_dclr", "instance_attr_access", "instance_method_access", 
                   "static_attr_access", "static_method_access", "obj_creation", 
                   "method_declaration", "variable_declaration", "function_declaration", 
                   "main_function_declaration", "assignment_statements", 
                   "if_statements", "elseif_list_statements", "elseif_statement", 
                   "else_statement", "by_expr", "forin_statements", "methodinvocation_statement", 
                   "call_func", "call_func_statement", "break_statements", 
                   "continue_statements", "return_expr", "return_statements", 
                   "program_block_class_statements", "block_class_statements", 
                   "block_statements", "statements_class", "statements", 
                   "statement_class", "statement", "expr", "expr1", "expr2", 
                   "expr3", "expr4", "expr5", "expr6", "expr7", "expr8", 
                   "expr9", "expr10", "expr11", "index_operators", "list_expr", 
                   "array_lit", "array_val", "literal", "list_parameters", 
                   "param", "identifier_list", "variable_in_func_identifier_list", 
                   "value_list", "array_type", "array_element_type", "array_size", 
                   "primitive_type", "variable_type" ]

    EOF = Token.EOF
    MAIN=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    BOOLLIT=8
    TRUE=9
    FALSE=10
    ARRAY=11
    IN=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    STRING=16
    RETURN=17
    NULL=18
    CLASS=19
    VAL=20
    VAR=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    NEW=24
    BY=25
    SELF=26
    DOUBLECOLONOP=27
    DOUBLEDOTOP=28
    UNDERSCORE=29
    PLUSOP=30
    MINUSOP=31
    MULTIPLYOP=32
    DIVIDEOP=33
    MODULOOP=34
    NOTOP=35
    ANDOP=36
    OROP=37
    EQUALOP=38
    ASSIGNOP=39
    NOTEQUALOP=40
    GTE=41
    LTE=42
    GT=43
    LT=44
    STREQUALOP=45
    STRCONCATOP=46
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
    PROGRAM=57
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

        def class_declarations(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Class_declarationsContext)
            else:
                return self.getTypedRuleContext(D96Parser.Class_declarationsContext,i)


        def class_main_program_declarations(self):
            return self.getTypedRuleContext(D96Parser.Class_main_program_declarationsContext,0)


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
            self.state = 128
            self.class_declarations()
            self.state = 129
            self.class_main_program_declarations()
            self.state = 130
            self.class_declarations()
            self.state = 131
            self.match(D96Parser.EOF)
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
            self.state = 133
            self.match(D96Parser.CLASS)
            self.state = 134
            self.match(D96Parser.PROGRAM)
            self.state = 135
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
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.class_declaration()
                self.state = 138
                self.class_declarations()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 140
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
            self.state = 144
            self.match(D96Parser.CLASS)
            self.state = 145
            self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
            self.state = 146
            self.class_inheritance()
            self.state = 147
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
            self.state = 152
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.match(D96Parser.COLON)
                self.state = 150
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
            self.state = 154
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 155
            self.match(D96Parser.LB)
            self.state = 156
            self.list_parameters()
            self.state = 157
            self.match(D96Parser.RB)
            self.state = 158
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
            self.state = 160
            self.match(D96Parser.DESTRUCTOR)
            self.state = 161
            self.match(D96Parser.LB)
            self.state = 162
            self.match(D96Parser.RB)
            self.state = 163
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

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_attr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_attr_access" ):
                return visitor.visitInstance_attr_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_attr_access(self):

        localctx = D96Parser.Instance_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instance_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expr()
            self.state = 166
            self.match(D96Parser.DOT)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS))) != 0)):
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

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_instance_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstance_method_access" ):
                return visitor.visitInstance_method_access(self)
            else:
                return visitor.visitChildren(self)




    def instance_method_access(self):

        localctx = D96Parser.Instance_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_instance_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.expr()
            self.state = 170
            self.match(D96Parser.DOT)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 172
            self.match(D96Parser.LB)
            self.state = 173
            self.list_expr()
            self.state = 174
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

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_attr_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_attr_access" ):
                return visitor.visitStatic_attr_access(self)
            else:
                return visitor.visitChildren(self)




    def static_attr_access(self):

        localctx = D96Parser.Static_attr_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_static_attr_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.expr()
            self.state = 177
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 178
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS))) != 0)):
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
        __slots__ = 'parser'

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

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_static_method_access

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatic_method_access" ):
                return visitor.visitStatic_method_access(self)
            else:
                return visitor.visitChildren(self)




    def static_method_access(self):

        localctx = D96Parser.Static_method_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_static_method_access)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.expr()
            self.state = 181
            self.match(D96Parser.DOUBLECOLONOP)
            self.state = 182
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.SELF) | (1 << D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS) | (1 << D96Parser.DOLLAR_IDENTIFIERS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 183
            self.match(D96Parser.LB)
            self.state = 184
            self.list_expr()
            self.state = 185
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_creationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

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
            return D96Parser.RULE_obj_creation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_creation" ):
                return visitor.visitObj_creation(self)
            else:
                return visitor.visitChildren(self)




    def obj_creation(self):

        localctx = D96Parser.Obj_creationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_obj_creation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(D96Parser.NEW)
            self.state = 188
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 189
            self.match(D96Parser.LB)
            self.state = 190
            self.list_expr()
            self.state = 191
            self.match(D96Parser.RB)
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
        self.enterRule(localctx, 24, self.RULE_method_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 194
            self.match(D96Parser.LB)
            self.state = 195
            self.list_parameters()
            self.state = 196
            self.match(D96Parser.RB)
            self.state = 197
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

        def identifier_list(self):
            return self.getTypedRuleContext(D96Parser.Identifier_listContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def variable_type(self):
            return self.getTypedRuleContext(D96Parser.Variable_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def value_list(self):
            return self.getTypedRuleContext(D96Parser.Value_listContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_variable_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable_declaration" ):
                return visitor.visitVariable_declaration(self)
            else:
                return visitor.visitChildren(self)




    def variable_declaration(self):

        localctx = D96Parser.Variable_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variable_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 200
            self.identifier_list()
            self.state = 201
            self.match(D96Parser.COLON)
            self.state = 202
            self.variable_type()
            self.state = 206
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ASSIGNOP]:
                self.state = 203
                self.match(D96Parser.ASSIGNOP)
                self.state = 204
                self.value_list()
                pass
            elif token in [D96Parser.SEMICOLON]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 208
            self.match(D96Parser.SEMICOLON)
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
            self.state = 210
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 211
            self.match(D96Parser.LB)
            self.state = 212
            self.list_parameters()
            self.state = 213
            self.match(D96Parser.RB)
            self.state = 214
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

        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


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
            self.state = 216
            self.match(D96Parser.MAIN)
            self.state = 217
            self.match(D96Parser.LB)
            self.state = 218
            self.match(D96Parser.RB)
            self.state = 219
            self.block_statements()
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

        def ASSIGNOP(self):
            return self.getToken(D96Parser.ASSIGNOP, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def instance_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_attr_accessContext,0)


        def static_attr_access(self):
            return self.getTypedRuleContext(D96Parser.Static_attr_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_assignment_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment_statements" ):
                return visitor.visitAssignment_statements(self)
            else:
                return visitor.visitChildren(self)




    def assignment_statements(self):

        localctx = D96Parser.Assignment_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_assignment_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 221
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 2:
                self.state = 222
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.state = 223
                self.instance_attr_access()
                pass

            elif la_ == 4:
                self.state = 224
                self.static_attr_access()
                pass


            self.state = 227
            self.match(D96Parser.ASSIGNOP)
            self.state = 228
            self.expr()
            self.state = 229
            self.match(D96Parser.SEMICOLON)
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

        def elseif_list_statements(self):
            return self.getTypedRuleContext(D96Parser.Elseif_list_statementsContext,0)


        def else_statement(self):
            return self.getTypedRuleContext(D96Parser.Else_statementContext,0)


        def block_statements(self):
            return self.getTypedRuleContext(D96Parser.Block_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_if_statements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statements" ):
                return visitor.visitIf_statements(self)
            else:
                return visitor.visitChildren(self)




    def if_statements(self):

        localctx = D96Parser.If_statementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(D96Parser.IF)
            self.state = 232
            self.match(D96Parser.LB)
            self.state = 233
            self.expr()
            self.state = 234
            self.match(D96Parser.RB)
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LCB]:
                self.state = 235
                self.block_statements()
                pass
            elif token in [D96Parser.ELSEIF, D96Parser.ELSE]:
                pass
            else:
                raise NoViableAltException(self)

            self.state = 239
            self.elseif_list_statements()
            self.state = 240
            self.else_statement()
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
        self.enterRule(localctx, 36, self.RULE_elseif_list_statements)
        try:
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.elseif_statement()
                self.state = 243
                self.elseif_list_statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 245
                self.elseif_statement()
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
        self.enterRule(localctx, 38, self.RULE_elseif_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(D96Parser.ELSEIF)
            self.state = 250
            self.match(D96Parser.LB)
            self.state = 251
            self.expr()
            self.state = 252
            self.match(D96Parser.RB)
            self.state = 255
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LCB]:
                self.state = 253
                self.block_statements()
                pass
            elif token in [D96Parser.ELSEIF, D96Parser.ELSE]:
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
        self.enterRule(localctx, 40, self.RULE_else_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(D96Parser.ELSE)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LCB]:
                self.state = 258
                self.block_statements()
                pass
            elif token in [D96Parser.MAIN, D96Parser.BREAK, D96Parser.CONTINUE, D96Parser.IF, D96Parser.FOREACH, D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.RETURN, D96Parser.VAL, D96Parser.VAR, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.RCB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
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
        self.enterRule(localctx, 42, self.RULE_by_expr)
        try:
            self.state = 265
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 262
                self.match(D96Parser.BY)
                self.state = 263
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
        self.enterRule(localctx, 44, self.RULE_forin_statements)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(D96Parser.FOREACH)
            self.state = 268
            self.match(D96Parser.LB)
            self.state = 269
            _la = self._input.LA(1)
            if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 270
            self.match(D96Parser.IN)
            self.state = 271
            self.expr()
            self.state = 272
            self.match(D96Parser.DOUBLEDOTOP)
            self.state = 273
            self.expr()
            self.state = 274
            self.by_expr()
            self.state = 275
            self.match(D96Parser.RB)
            self.state = 276
            self.block_statements()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Methodinvocation_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(D96Parser.SEMICOLON, 0)

        def instance_method_access(self):
            return self.getTypedRuleContext(D96Parser.Instance_method_accessContext,0)


        def static_method_access(self):
            return self.getTypedRuleContext(D96Parser.Static_method_accessContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_methodinvocation_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodinvocation_statement" ):
                return visitor.visitMethodinvocation_statement(self)
            else:
                return visitor.visitChildren(self)




    def methodinvocation_statement(self):

        localctx = D96Parser.Methodinvocation_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_methodinvocation_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 278
                self.instance_method_access()
                pass

            elif la_ == 2:
                self.state = 279
                self.static_method_access()
                pass


            self.state = 282
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
            return D96Parser.RULE_call_func

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_func" ):
                return visitor.visitCall_func(self)
            else:
                return visitor.visitChildren(self)




    def call_func(self):

        localctx = D96Parser.Call_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_call_func)
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
            self.list_expr()
            self.state = 287
            self.match(D96Parser.RB)
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

        def call_func(self):
            return self.getTypedRuleContext(D96Parser.Call_funcContext,0)


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
            self.state = 289
            self.call_func()
            self.state = 290
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
        self.enterRule(localctx, 52, self.RULE_break_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(D96Parser.BREAK)
            self.state = 293
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
        self.enterRule(localctx, 54, self.RULE_continue_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.match(D96Parser.CONTINUE)
            self.state = 296
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
        self.enterRule(localctx, 56, self.RULE_return_expr)
        try:
            self.state = 300
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.NOTOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
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
        self.enterRule(localctx, 58, self.RULE_return_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(D96Parser.RETURN)
            self.state = 303
            self.return_expr()
            self.state = 304
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
        self.enterRule(localctx, 60, self.RULE_program_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(D96Parser.LCB)
            self.state = 307
            self.statements_class()
            self.state = 308
            self.main_function_declaration()
            self.state = 309
            self.statements_class()
            self.state = 310
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
        self.enterRule(localctx, 62, self.RULE_block_class_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(D96Parser.LCB)
            self.state = 313
            self.statements_class()
            self.state = 314
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
        self.enterRule(localctx, 64, self.RULE_block_statements)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(D96Parser.LCB)
            self.state = 317
            self.statements()
            self.state = 318
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
        self.enterRule(localctx, 66, self.RULE_statements_class)
        try:
            self.state = 325
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.statement_class()
                self.state = 321
                self.statements_class()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 323
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
        self.enterRule(localctx, 68, self.RULE_statements)
        try:
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 327
                self.statement()
                self.state = 328
                self.statements()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
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


        def assignment_statements(self):
            return self.getTypedRuleContext(D96Parser.Assignment_statementsContext,0)


        def if_statements(self):
            return self.getTypedRuleContext(D96Parser.If_statementsContext,0)


        def forin_statements(self):
            return self.getTypedRuleContext(D96Parser.Forin_statementsContext,0)


        def methodinvocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Methodinvocation_statementContext,0)


        def call_func_statement(self):
            return self.getTypedRuleContext(D96Parser.Call_func_statementContext,0)


        def break_statements(self):
            return self.getTypedRuleContext(D96Parser.Break_statementsContext,0)


        def continue_statements(self):
            return self.getTypedRuleContext(D96Parser.Continue_statementsContext,0)


        def return_statements(self):
            return self.getTypedRuleContext(D96Parser.Return_statementsContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_statement_class

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement_class" ):
                return visitor.visitStatement_class(self)
            else:
                return visitor.visitChildren(self)




    def statement_class(self):

        localctx = D96Parser.Statement_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_statement_class)
        try:
            self.state = 344
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 335
                self.function_declaration()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 336
                self.assignment_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 337
                self.if_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 338
                self.forin_statements()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 339
                self.methodinvocation_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 340
                self.call_func_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 341
                self.break_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 342
                self.continue_statements()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 343
                self.return_statements()
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

        def variable_declaration(self):
            return self.getTypedRuleContext(D96Parser.Variable_declarationContext,0)


        def assignment_statements(self):
            return self.getTypedRuleContext(D96Parser.Assignment_statementsContext,0)


        def if_statements(self):
            return self.getTypedRuleContext(D96Parser.If_statementsContext,0)


        def forin_statements(self):
            return self.getTypedRuleContext(D96Parser.Forin_statementsContext,0)


        def methodinvocation_statement(self):
            return self.getTypedRuleContext(D96Parser.Methodinvocation_statementContext,0)


        def call_func_statement(self):
            return self.getTypedRuleContext(D96Parser.Call_func_statementContext,0)


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
        self.enterRule(localctx, 72, self.RULE_statement)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 346
                self.variable_declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                self.assignment_statements()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 348
                self.if_statements()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 349
                self.forin_statements()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 350
                self.methodinvocation_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 351
                self.call_func_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 352
                self.break_statements()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 353
                self.continue_statements()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 354
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
        self.enterRule(localctx, 74, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.expr1()
                self.state = 358
                _la = self._input.LA(1)
                if not(_la==D96Parser.STREQUALOP or _la==D96Parser.STRCONCATOP):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 359
                self.expr1()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 361
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
        self.enterRule(localctx, 76, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 364
                self.expr2(0)
                self.state = 365
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.EQUALOP) | (1 << D96Parser.NOTEQUALOP) | (1 << D96Parser.GTE) | (1 << D96Parser.LTE) | (1 << D96Parser.GT) | (1 << D96Parser.LT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 366
                self.expr2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 372
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 379
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 374
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 375
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ANDOP or _la==D96Parser.OROP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 376
                    self.expr3(0) 
                self.state = 381
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 390
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 385
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 386
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.PLUSOP or _la==D96Parser.MINUSOP):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 387
                    self.expr4(0) 
                self.state = 392
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 401
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 396
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 397
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MULTIPLYOP) | (1 << D96Parser.DIVIDEOP) | (1 << D96Parser.MODULOOP))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 398
                    self.expr5() 
                self.state = 403
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        self.enterRule(localctx, 84, self.RULE_expr5)
        try:
            self.state = 407
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOTOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.match(D96Parser.NOTOP)
                self.state = 405
                self.expr5()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.MINUSOP, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
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
        self.enterRule(localctx, 86, self.RULE_expr6)
        try:
            self.state = 412
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.MINUSOP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(D96Parser.MINUSOP)
                self.state = 410
                self.expr6()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.ARRAY, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, D96Parser.DOLLAR_IDENTIFIERS, D96Parser.STRINGLIT, D96Parser.FLOATLIT, D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
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
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.expr8(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 417
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 418
                    self.index_operators() 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def DOUBLEDOTOP(self):
            return self.getToken(D96Parser.DOUBLEDOTOP, 0)

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
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_expr8, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.expr9()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Expr8Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr8)
                    self.state = 427
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 428
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.DOUBLEDOTOP or _la==D96Parser.DOT):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 429
                    self.expr9() 
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

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

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

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
        self.enterRule(localctx, 92, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(D96Parser.NEW)
                self.state = 436
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self.match(D96Parser.LB)
                self.state = 438
                self.list_expr()
                self.state = 439
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
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

        def literal(self):
            return self.getTypedRuleContext(D96Parser.LiteralContext,0)


        def VARIABLE_IN_FUNC_IDENTIFIERS(self):
            return self.getToken(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS, 0)

        def DOLLAR_IDENTIFIERS(self):
            return self.getToken(D96Parser.DOLLAR_IDENTIFIERS, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def call_func(self):
            return self.getTypedRuleContext(D96Parser.Call_funcContext,0)


        def obj_creation(self):
            return self.getTypedRuleContext(D96Parser.Obj_creationContext,0)


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
        self.enterRule(localctx, 94, self.RULE_expr10)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 444
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 445
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 446
                self.match(D96Parser.DOLLAR_IDENTIFIERS)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 447
                self.match(D96Parser.SELF)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 448
                self.call_func()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 449
                self.obj_creation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 450
                self.expr11()
                pass


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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expr11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr11" ):
                return visitor.visitExpr11(self)
            else:
                return visitor.visitChildren(self)




    def expr11(self):

        localctx = D96Parser.Expr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self.match(D96Parser.LB)
            self.state = 454
            self.expr()
            self.state = 455
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
        self.enterRule(localctx, 98, self.RULE_index_operators)
        try:
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 457
                self.match(D96Parser.LSB)
                self.state = 458
                self.expr()
                self.state = 459
                self.match(D96Parser.RSB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 461
                self.match(D96Parser.LSB)
                self.state = 462
                self.expr()
                self.state = 463
                self.match(D96Parser.RSB)
                self.state = 464
                self.index_operators()
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
        self.enterRule(localctx, 100, self.RULE_list_expr)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 468
                self.expr()
                self.state = 469
                self.match(D96Parser.COMMA)
                self.state = 470
                self.list_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 472
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
        self.enterRule(localctx, 102, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(D96Parser.ARRAY)
            self.state = 477
            self.match(D96Parser.LB)
            self.state = 478
            self.array_val()
            self.state = 479
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
        self.enterRule(localctx, 104, self.RULE_array_val)
        try:
            self.state = 487
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
                self.expr()
                self.state = 482
                self.match(D96Parser.COMMA)
                self.state = 483
                self.array_val()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 485
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
        self.enterRule(localctx, 106, self.RULE_literal)
        try:
            self.state = 494
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 489
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 490
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 491
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRINGLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 492
                self.match(D96Parser.STRINGLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 493
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
        self.enterRule(localctx, 108, self.RULE_list_parameters)
        try:
            self.state = 502
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.param()
                self.state = 497
                self.match(D96Parser.SEMICOLON)
                self.state = 498
                self.list_parameters()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
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
        self.enterRule(localctx, 110, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.identifier_list()
            self.state = 505
            self.match(D96Parser.COLON)
            self.state = 506
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
        self.enterRule(localctx, 112, self.RULE_identifier_list)
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                _la = self._input.LA(1)
                if not(_la==D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS or _la==D96Parser.DOLLAR_IDENTIFIERS):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 509
                self.match(D96Parser.COMMA)
                self.state = 510
                self.identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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
        self.enterRule(localctx, 114, self.RULE_variable_in_func_identifier_list)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(D96Parser.VARIABLE_IN_FUNC_IDENTIFIERS)
                self.state = 516
                self.match(D96Parser.COMMA)
                self.state = 517
                self.variable_in_func_identifier_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 518
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
        self.enterRule(localctx, 116, self.RULE_value_list)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 524
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                if la_ == 1:
                    self.state = 522
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 523
                    self.expr()
                    pass


                self.state = 526
                self.match(D96Parser.COMMA)
                self.state = 527
                self.value_list()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
                if la_ == 1:
                    self.state = 529
                    self.literal()
                    pass

                elif la_ == 2:
                    self.state = 530
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
        self.enterRule(localctx, 118, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.match(D96Parser.ARRAY)
            self.state = 537
            self.match(D96Parser.LSB)
            self.state = 538
            self.array_element_type()
            self.state = 539
            self.match(D96Parser.COMMA)
            self.state = 540
            self.array_size()
            self.state = 541
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
        self.enterRule(localctx, 120, self.RULE_array_element_type)
        try:
            self.state = 548
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 543
                self.array_type()
                pass
            elif token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 544
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 545
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 4)
                self.state = 546
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 5)
                self.state = 547
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
        self.enterRule(localctx, 122, self.RULE_array_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
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
        self.enterRule(localctx, 124, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
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
        self.enterRule(localctx, 126, self.RULE_variable_type)
        try:
            self.state = 556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT, D96Parser.FLOAT, D96Parser.BOOLEAN, D96Parser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 554
                self.primitive_type()
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 555
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
        self._predicates[39] = self.expr2_sempred
        self._predicates[40] = self.expr3_sempred
        self._predicates[41] = self.expr4_sempred
        self._predicates[44] = self.expr7_sempred
        self._predicates[45] = self.expr8_sempred
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
         




