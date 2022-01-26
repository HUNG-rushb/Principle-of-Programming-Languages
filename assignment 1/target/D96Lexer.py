# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
import inspect



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u02dc\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00d0\n")
        buf.write("\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3#")
        buf.write("\3#\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3(\3)\3)")
        buf.write("\3)\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\3-\3.\3.\3.\3/\3/\3")
        buf.write("\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65")
        buf.write("\3\65\3\66\3\66\3\67\3\67\38\38\39\39\79\u0185\n9\f9\16")
        buf.write("9\u0188\139\3:\3:\6:\u018c\n:\r:\16:\u018d\3;\3;\3<\3")
        buf.write("<\7<\u0194\n<\f<\16<\u0197\13<\3<\3<\3<\3=\3=\7=\u019e")
        buf.write("\n=\f=\16=\u01a1\13=\3>\3>\3>\5>\u01a6\n>\3>\7>\u01a9")
        buf.write("\n>\f>\16>\u01ac\13>\3>\3>\7>\u01b0\n>\f>\16>\u01b3\13")
        buf.write(">\3>\6>\u01b6\n>\r>\16>\u01b7\5>\u01ba\n>\3?\3?\5?\u01be")
        buf.write("\n?\3?\3?\3?\3?\3?\3?\3?\5?\u01c7\n?\3?\3?\3?\3?\3?\3")
        buf.write("?\5?\u01cf\n?\3?\3?\3?\3?\3?\3?\3?\3?\3?\5?\u01da\n?\3")
        buf.write("?\3?\3@\3@\3@\3@\3@\7@\u01e3\n@\f@\16@\u01e6\13@\3A\3")
        buf.write("A\3A\6A\u01eb\nA\rA\16A\u01ec\3A\3A\6A\u01f1\nA\rA\16")
        buf.write("A\u01f2\7A\u01f5\nA\fA\16A\u01f8\13A\3A\7A\u01fb\nA\f")
        buf.write("A\16A\u01fe\13A\5A\u0200\nA\3A\5A\u0203\nA\3B\3B\6B\u0207")
        buf.write("\nB\rB\16B\u0208\3B\3B\6B\u020d\nB\rB\16B\u020e\7B\u0211")
        buf.write("\nB\fB\16B\u0214\13B\3B\7B\u0217\nB\fB\16B\u021a\13B\5")
        buf.write("B\u021c\nB\3B\5B\u021f\nB\3C\3C\3C\6C\u0224\nC\rC\16C")
        buf.write("\u0225\3C\3C\6C\u022a\nC\rC\16C\u022b\7C\u022e\nC\fC\16")
        buf.write("C\u0231\13C\3C\7C\u0234\nC\fC\16C\u0237\13C\5C\u0239\n")
        buf.write("C\3C\5C\u023c\nC\3D\3D\3D\6D\u0241\nD\rD\16D\u0242\3D")
        buf.write("\3D\6D\u0247\nD\rD\16D\u0248\7D\u024b\nD\fD\16D\u024e")
        buf.write("\13D\3D\7D\u0251\nD\fD\16D\u0254\13D\5D\u0256\nD\3E\3")
        buf.write("E\6E\u025a\nE\rE\16E\u025b\3E\3E\6E\u0260\nE\rE\16E\u0261")
        buf.write("\7E\u0264\nE\fE\16E\u0267\13E\3E\7E\u026a\nE\fE\16E\u026d")
        buf.write("\13E\5E\u026f\nE\3F\3F\3F\6F\u0274\nF\rF\16F\u0275\3F")
        buf.write("\3F\6F\u027a\nF\rF\16F\u027b\7F\u027e\nF\fF\16F\u0281")
        buf.write("\13F\3F\7F\u0284\nF\fF\16F\u0287\13F\5F\u0289\nF\3G\3")
        buf.write("G\3G\3G\5G\u028f\nG\3G\3G\3H\3H\3H\3H\5H\u0297\nH\3H\3")
        buf.write("H\3H\5H\u029c\nH\3I\3I\7I\u02a0\nI\fI\16I\u02a3\13I\3")
        buf.write("I\3I\3J\3J\7J\u02a9\nJ\fJ\16J\u02ac\13J\3J\3J\3J\3K\3")
        buf.write("K\3K\3K\5K\u02b5\nK\3L\3L\3L\3M\3M\3M\5M\u02bd\nM\3N\3")
        buf.write("N\3N\3N\7N\u02c3\nN\fN\16N\u02c6\13N\3N\3N\3N\3N\3N\3")
        buf.write("O\6O\u02ce\nO\rO\16O\u02cf\3O\3O\3P\3P\3P\3Q\3Q\3R\3R")
        buf.write("\3S\3S\3\u02c4\2T\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65")
        buf.write("i\66k\67m8o9q:s;u\2w<y\2{\2}=\177\2\u0081\2\u0083\2\u0085")
        buf.write("\2\u0087\2\u0089\2\u008b\2\u008d>\u008f?\u0091@\u0093")
        buf.write("A\u0095\2\u0097\2\u0099\2\u009bB\u009dC\u009fD\u00a1\2")
        buf.write("\u00a3\2\u00a5\2\3\2\21\5\2C\\aac|\6\2\62;C\\aac|\3\2")
        buf.write("\62;\3\2\63;\5\2\63;CHch\5\2\62;CHch\3\2\639\3\2\629\3")
        buf.write("\2\62\63\4\2$$^^\t\2))^^ddhhppttvv\5\2\n\f\16\17\"\"\4")
        buf.write("\2DDdd\4\2GGgg\4\2ZZzz\2\u030d\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2w\3")
        buf.write("\2\2\2\2}\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\3\u00a7\3\2\2\2\5\u00ad\3\2\2\2\7\u00b6")
        buf.write("\3\2\2\2\t\u00b9\3\2\2\2\13\u00c0\3\2\2\2\r\u00c5\3\2")
        buf.write("\2\2\17\u00cf\3\2\2\2\21\u00d1\3\2\2\2\23\u00d6\3\2\2")
        buf.write("\2\25\u00dc\3\2\2\2\27\u00e2\3\2\2\2\31\u00e5\3\2\2\2")
        buf.write("\33\u00e9\3\2\2\2\35\u00ef\3\2\2\2\37\u00f7\3\2\2\2!\u00fe")
        buf.write("\3\2\2\2#\u0105\3\2\2\2%\u010a\3\2\2\2\'\u0110\3\2\2\2")
        buf.write(")\u0114\3\2\2\2+\u0118\3\2\2\2-\u0124\3\2\2\2/\u012f\3")
        buf.write("\2\2\2\61\u0133\3\2\2\2\63\u0136\3\2\2\2\65\u013b\3\2")
        buf.write("\2\2\67\u013e\3\2\2\29\u0141\3\2\2\2;\u0143\3\2\2\2=\u0145")
        buf.write("\3\2\2\2?\u0147\3\2\2\2A\u0149\3\2\2\2C\u014b\3\2\2\2")
        buf.write("E\u014d\3\2\2\2G\u014f\3\2\2\2I\u0152\3\2\2\2K\u0155\3")
        buf.write("\2\2\2M\u0158\3\2\2\2O\u015a\3\2\2\2Q\u015d\3\2\2\2S\u0160")
        buf.write("\3\2\2\2U\u0163\3\2\2\2W\u0165\3\2\2\2Y\u0167\3\2\2\2")
        buf.write("[\u016b\3\2\2\2]\u016e\3\2\2\2_\u0170\3\2\2\2a\u0172\3")
        buf.write("\2\2\2c\u0174\3\2\2\2e\u0176\3\2\2\2g\u0178\3\2\2\2i\u017a")
        buf.write("\3\2\2\2k\u017c\3\2\2\2m\u017e\3\2\2\2o\u0180\3\2\2\2")
        buf.write("q\u0182\3\2\2\2s\u0189\3\2\2\2u\u018f\3\2\2\2w\u0191\3")
        buf.write("\2\2\2y\u019b\3\2\2\2{\u01a2\3\2\2\2}\u01d9\3\2\2\2\177")
        buf.write("\u01dd\3\2\2\2\u0081\u01e7\3\2\2\2\u0083\u0204\3\2\2\2")
        buf.write("\u0085\u0220\3\2\2\2\u0087\u023d\3\2\2\2\u0089\u0257\3")
        buf.write("\2\2\2\u008b\u0270\3\2\2\2\u008d\u028e\3\2\2\2\u008f\u029b")
        buf.write("\3\2\2\2\u0091\u029d\3\2\2\2\u0093\u02a6\3\2\2\2\u0095")
        buf.write("\u02b4\3\2\2\2\u0097\u02b6\3\2\2\2\u0099\u02bc\3\2\2\2")
        buf.write("\u009b\u02be\3\2\2\2\u009d\u02cd\3\2\2\2\u009f\u02d3\3")
        buf.write("\2\2\2\u00a1\u02d6\3\2\2\2\u00a3\u02d8\3\2\2\2\u00a5\u02da")
        buf.write("\3\2\2\2\u00a7\u00a8\7D\2\2\u00a8\u00a9\7t\2\2\u00a9\u00aa")
        buf.write("\7g\2\2\u00aa\u00ab\7c\2\2\u00ab\u00ac\7m\2\2\u00ac\4")
        buf.write("\3\2\2\2\u00ad\u00ae\7E\2\2\u00ae\u00af\7q\2\2\u00af\u00b0")
        buf.write("\7p\2\2\u00b0\u00b1\7v\2\2\u00b1\u00b2\7k\2\2\u00b2\u00b3")
        buf.write("\7p\2\2\u00b3\u00b4\7w\2\2\u00b4\u00b5\7g\2\2\u00b5\6")
        buf.write("\3\2\2\2\u00b6\u00b7\7K\2\2\u00b7\u00b8\7h\2\2\u00b8\b")
        buf.write("\3\2\2\2\u00b9\u00ba\7G\2\2\u00ba\u00bb\7n\2\2\u00bb\u00bc")
        buf.write("\7u\2\2\u00bc\u00bd\7g\2\2\u00bd\u00be\7k\2\2\u00be\u00bf")
        buf.write("\7h\2\2\u00bf\n\3\2\2\2\u00c0\u00c1\7G\2\2\u00c1\u00c2")
        buf.write("\7n\2\2\u00c2\u00c3\7u\2\2\u00c3\u00c4\7g\2\2\u00c4\f")
        buf.write("\3\2\2\2\u00c5\u00c6\7H\2\2\u00c6\u00c7\7q\2\2\u00c7\u00c8")
        buf.write("\7t\2\2\u00c8\u00c9\7g\2\2\u00c9\u00ca\7c\2\2\u00ca\u00cb")
        buf.write("\7e\2\2\u00cb\u00cc\7j\2\2\u00cc\16\3\2\2\2\u00cd\u00d0")
        buf.write("\5\21\t\2\u00ce\u00d0\5\23\n\2\u00cf\u00cd\3\2\2\2\u00cf")
        buf.write("\u00ce\3\2\2\2\u00d0\20\3\2\2\2\u00d1\u00d2\7V\2\2\u00d2")
        buf.write("\u00d3\7t\2\2\u00d3\u00d4\7w\2\2\u00d4\u00d5\7g\2\2\u00d5")
        buf.write("\22\3\2\2\2\u00d6\u00d7\7H\2\2\u00d7\u00d8\7c\2\2\u00d8")
        buf.write("\u00d9\7n\2\2\u00d9\u00da\7u\2\2\u00da\u00db\7g\2\2\u00db")
        buf.write("\24\3\2\2\2\u00dc\u00dd\7C\2\2\u00dd\u00de\7t\2\2\u00de")
        buf.write("\u00df\7t\2\2\u00df\u00e0\7c\2\2\u00e0\u00e1\7{\2\2\u00e1")
        buf.write("\26\3\2\2\2\u00e2\u00e3\7K\2\2\u00e3\u00e4\7p\2\2\u00e4")
        buf.write("\30\3\2\2\2\u00e5\u00e6\7K\2\2\u00e6\u00e7\7p\2\2\u00e7")
        buf.write("\u00e8\7v\2\2\u00e8\32\3\2\2\2\u00e9\u00ea\7H\2\2\u00ea")
        buf.write("\u00eb\7n\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7c\2\2\u00ed")
        buf.write("\u00ee\7v\2\2\u00ee\34\3\2\2\2\u00ef\u00f0\7D\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1\u00f2\7q\2\2\u00f2\u00f3\7n\2\2\u00f3")
        buf.write("\u00f4\7g\2\2\u00f4\u00f5\7c\2\2\u00f5\u00f6\7p\2\2\u00f6")
        buf.write("\36\3\2\2\2\u00f7\u00f8\7U\2\2\u00f8\u00f9\7v\2\2\u00f9")
        buf.write("\u00fa\7t\2\2\u00fa\u00fb\7k\2\2\u00fb\u00fc\7p\2\2\u00fc")
        buf.write("\u00fd\7i\2\2\u00fd \3\2\2\2\u00fe\u00ff\7T\2\2\u00ff")
        buf.write("\u0100\7g\2\2\u0100\u0101\7v\2\2\u0101\u0102\7w\2\2\u0102")
        buf.write("\u0103\7t\2\2\u0103\u0104\7p\2\2\u0104\"\3\2\2\2\u0105")
        buf.write("\u0106\7P\2\2\u0106\u0107\7w\2\2\u0107\u0108\7n\2\2\u0108")
        buf.write("\u0109\7n\2\2\u0109$\3\2\2\2\u010a\u010b\7E\2\2\u010b")
        buf.write("\u010c\7n\2\2\u010c\u010d\7c\2\2\u010d\u010e\7u\2\2\u010e")
        buf.write("\u010f\7u\2\2\u010f&\3\2\2\2\u0110\u0111\7X\2\2\u0111")
        buf.write("\u0112\7c\2\2\u0112\u0113\7n\2\2\u0113(\3\2\2\2\u0114")
        buf.write("\u0115\7X\2\2\u0115\u0116\7c\2\2\u0116\u0117\7t\2\2\u0117")
        buf.write("*\3\2\2\2\u0118\u0119\7E\2\2\u0119\u011a\7q\2\2\u011a")
        buf.write("\u011b\7p\2\2\u011b\u011c\7u\2\2\u011c\u011d\7v\2\2\u011d")
        buf.write("\u011e\7t\2\2\u011e\u011f\7w\2\2\u011f\u0120\7e\2\2\u0120")
        buf.write("\u0121\7v\2\2\u0121\u0122\7q\2\2\u0122\u0123\7t\2\2\u0123")
        buf.write(",\3\2\2\2\u0124\u0125\7F\2\2\u0125\u0126\7g\2\2\u0126")
        buf.write("\u0127\7u\2\2\u0127\u0128\7v\2\2\u0128\u0129\7t\2\2\u0129")
        buf.write("\u012a\7w\2\2\u012a\u012b\7e\2\2\u012b\u012c\7v\2\2\u012c")
        buf.write("\u012d\7q\2\2\u012d\u012e\7t\2\2\u012e.\3\2\2\2\u012f")
        buf.write("\u0130\7P\2\2\u0130\u0131\7g\2\2\u0131\u0132\7y\2\2\u0132")
        buf.write("\60\3\2\2\2\u0133\u0134\7D\2\2\u0134\u0135\7{\2\2\u0135")
        buf.write("\62\3\2\2\2\u0136\u0137\7U\2\2\u0137\u0138\7g\2\2\u0138")
        buf.write("\u0139\7n\2\2\u0139\u013a\7h\2\2\u013a\64\3\2\2\2\u013b")
        buf.write("\u013c\7<\2\2\u013c\u013d\7<\2\2\u013d\66\3\2\2\2\u013e")
        buf.write("\u013f\7\60\2\2\u013f\u0140\7\60\2\2\u01408\3\2\2\2\u0141")
        buf.write("\u0142\7a\2\2\u0142:\3\2\2\2\u0143\u0144\7-\2\2\u0144")
        buf.write("<\3\2\2\2\u0145\u0146\7/\2\2\u0146>\3\2\2\2\u0147\u0148")
        buf.write("\7,\2\2\u0148@\3\2\2\2\u0149\u014a\7\61\2\2\u014aB\3\2")
        buf.write("\2\2\u014b\u014c\7\'\2\2\u014cD\3\2\2\2\u014d\u014e\7")
        buf.write("#\2\2\u014eF\3\2\2\2\u014f\u0150\7(\2\2\u0150\u0151\7")
        buf.write("(\2\2\u0151H\3\2\2\2\u0152\u0153\7~\2\2\u0153\u0154\7")
        buf.write("~\2\2\u0154J\3\2\2\2\u0155\u0156\7?\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157L\3\2\2\2\u0158\u0159\7?\2\2\u0159N\3\2\2\2")
        buf.write("\u015a\u015b\7#\2\2\u015b\u015c\7?\2\2\u015cP\3\2\2\2")
        buf.write("\u015d\u015e\7@\2\2\u015e\u015f\7?\2\2\u015fR\3\2\2\2")
        buf.write("\u0160\u0161\7>\2\2\u0161\u0162\7?\2\2\u0162T\3\2\2\2")
        buf.write("\u0163\u0164\7@\2\2\u0164V\3\2\2\2\u0165\u0166\7>\2\2")
        buf.write("\u0166X\3\2\2\2\u0167\u0168\7?\2\2\u0168\u0169\7?\2\2")
        buf.write("\u0169\u016a\7\60\2\2\u016aZ\3\2\2\2\u016b\u016c\7-\2")
        buf.write("\2\u016c\u016d\7\60\2\2\u016d\\\3\2\2\2\u016e\u016f\7")
        buf.write("*\2\2\u016f^\3\2\2\2\u0170\u0171\7+\2\2\u0171`\3\2\2\2")
        buf.write("\u0172\u0173\7]\2\2\u0173b\3\2\2\2\u0174\u0175\7_\2\2")
        buf.write("\u0175d\3\2\2\2\u0176\u0177\7}\2\2\u0177f\3\2\2\2\u0178")
        buf.write("\u0179\7\177\2\2\u0179h\3\2\2\2\u017a\u017b\7\60\2\2\u017b")
        buf.write("j\3\2\2\2\u017c\u017d\7.\2\2\u017dl\3\2\2\2\u017e\u017f")
        buf.write("\7<\2\2\u017fn\3\2\2\2\u0180\u0181\7=\2\2\u0181p\3\2\2")
        buf.write("\2\u0182\u0186\t\2\2\2\u0183\u0185\t\3\2\2\u0184\u0183")
        buf.write("\3\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186")
        buf.write("\u0187\3\2\2\2\u0187r\3\2\2\2\u0188\u0186\3\2\2\2\u0189")
        buf.write("\u018b\5u;\2\u018a\u018c\t\3\2\2\u018b\u018a\3\2\2\2\u018c")
        buf.write("\u018d\3\2\2\2\u018d\u018b\3\2\2\2\u018d\u018e\3\2\2\2")
        buf.write("\u018et\3\2\2\2\u018f\u0190\7&\2\2\u0190v\3\2\2\2\u0191")
        buf.write("\u0195\7$\2\2\u0192\u0194\5\u0095K\2\u0193\u0192\3\2\2")
        buf.write("\2\u0194\u0197\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196")
        buf.write("\3\2\2\2\u0196\u0198\3\2\2\2\u0197\u0195\3\2\2\2\u0198")
        buf.write("\u0199\7$\2\2\u0199\u019a\b<\2\2\u019ax\3\2\2\2\u019b")
        buf.write("\u019f\7\60\2\2\u019c\u019e\t\4\2\2\u019d\u019c\3\2\2")
        buf.write("\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f\u01a0")
        buf.write("\3\2\2\2\u01a0z\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2\u01a5")
        buf.write("\5\u00a3R\2\u01a3\u01a6\5=\37\2\u01a4\u01a6\5;\36\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a4\3\2\2\2\u01a5\u01a6\3\2\2\2")
        buf.write("\u01a6\u01b9\3\2\2\2\u01a7\u01a9\7\62\2\2\u01a8\u01a7")
        buf.write("\3\2\2\2\u01a9\u01ac\3\2\2\2\u01aa\u01a8\3\2\2\2\u01aa")
        buf.write("\u01ab\3\2\2\2\u01ab\u01ad\3\2\2\2\u01ac\u01aa\3\2\2\2")
        buf.write("\u01ad\u01b1\t\5\2\2\u01ae\u01b0\t\4\2\2\u01af\u01ae\3")
        buf.write("\2\2\2\u01b0\u01b3\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b2")
        buf.write("\3\2\2\2\u01b2\u01ba\3\2\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b6\7\62\2\2\u01b5\u01b4\3\2\2\2\u01b6\u01b7\3\2\2")
        buf.write("\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8\u01ba")
        buf.write("\3\2\2\2\u01b9\u01aa\3\2\2\2\u01b9\u01b5\3\2\2\2\u01ba")
        buf.write("|\3\2\2\2\u01bb\u01be\5\177@\2\u01bc\u01be\7\62\2\2\u01bd")
        buf.write("\u01bb\3\2\2\2\u01bd\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2")
        buf.write("\u01bf\u01c0\5y=\2\u01c0\u01c1\5{>\2\u01c1\u01c2\3\2\2")
        buf.write("\2\u01c2\u01c3\b?\3\2\u01c3\u01da\3\2\2\2\u01c4\u01c7")
        buf.write("\5\177@\2\u01c5\u01c7\7\62\2\2\u01c6\u01c4\3\2\2\2\u01c6")
        buf.write("\u01c5\3\2\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\5y=\2\u01c9")
        buf.write("\u01ca\3\2\2\2\u01ca\u01cb\b?\4\2\u01cb\u01da\3\2\2\2")
        buf.write("\u01cc\u01cf\5\177@\2\u01cd\u01cf\7\62\2\2\u01ce\u01cc")
        buf.write("\3\2\2\2\u01ce\u01cd\3\2\2\2\u01cf\u01d0\3\2\2\2\u01d0")
        buf.write("\u01d1\5{>\2\u01d1\u01d2\3\2\2\2\u01d2\u01d3\b?\5\2\u01d3")
        buf.write("\u01da\3\2\2\2\u01d4\u01d5\5y=\2\u01d5\u01d6\5{>\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d8\b?\6\2\u01d8\u01da\3\2\2\2")
        buf.write("\u01d9\u01bd\3\2\2\2\u01d9\u01c6\3\2\2\2\u01d9\u01ce\3")
        buf.write("\2\2\2\u01d9\u01d4\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dc")
        buf.write("\b?\7\2\u01dc~\3\2\2\2\u01dd\u01e4\t\5\2\2\u01de\u01df")
        buf.write("\59\35\2\u01df\u01e0\t\4\2\2\u01e0\u01e3\3\2\2\2\u01e1")
        buf.write("\u01e3\t\4\2\2\u01e2\u01de\3\2\2\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u0080\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8")
        buf.write("\7\62\2\2\u01e8\u0202\5\u00a5S\2\u01e9\u01eb\t\6\2\2\u01ea")
        buf.write("\u01e9\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ea\3\2\2\2")
        buf.write("\u01ec\u01ed\3\2\2\2\u01ed\u01ff\3\2\2\2\u01ee\u01f0\5")
        buf.write("9\35\2\u01ef\u01f1\t\7\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f5\3\2\2\2\u01f4\u01ee\3\2\2\2\u01f5\u01f8\3\2\2\2")
        buf.write("\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u0200\3")
        buf.write("\2\2\2\u01f8\u01f6\3\2\2\2\u01f9\u01fb\t\7\2\2\u01fa\u01f9")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc")
        buf.write("\u01fd\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2")
        buf.write("\u01ff\u01f6\3\2\2\2\u01ff\u01fc\3\2\2\2\u0200\u0203\3")
        buf.write("\2\2\2\u0201\u0203\7\62\2\2\u0202\u01ea\3\2\2\2\u0202")
        buf.write("\u0201\3\2\2\2\u0203\u0082\3\2\2\2\u0204\u021e\7\62\2")
        buf.write("\2\u0205\u0207\t\b\2\2\u0206\u0205\3\2\2\2\u0207\u0208")
        buf.write("\3\2\2\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209")
        buf.write("\u021b\3\2\2\2\u020a\u020c\59\35\2\u020b\u020d\t\t\2\2")
        buf.write("\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u020c\3")
        buf.write("\2\2\2\u020e\u020f\3\2\2\2\u020f\u0211\3\2\2\2\u0210\u020a")
        buf.write("\3\2\2\2\u0211\u0214\3\2\2\2\u0212\u0210\3\2\2\2\u0212")
        buf.write("\u0213\3\2\2\2\u0213\u021c\3\2\2\2\u0214\u0212\3\2\2\2")
        buf.write("\u0215\u0217\t\t\2\2\u0216\u0215\3\2\2\2\u0217\u021a\3")
        buf.write("\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219\u021c")
        buf.write("\3\2\2\2\u021a\u0218\3\2\2\2\u021b\u0212\3\2\2\2\u021b")
        buf.write("\u0218\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021f\7\62\2")
        buf.write("\2\u021e\u0206\3\2\2\2\u021e\u021d\3\2\2\2\u021f\u0084")
        buf.write("\3\2\2\2\u0220\u0221\7\62\2\2\u0221\u023b\5\u00a1Q\2\u0222")
        buf.write("\u0224\7\63\2\2\u0223\u0222\3\2\2\2\u0224\u0225\3\2\2")
        buf.write("\2\u0225\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0238")
        buf.write("\3\2\2\2\u0227\u0229\59\35\2\u0228\u022a\t\n\2\2\u0229")
        buf.write("\u0228\3\2\2\2\u022a\u022b\3\2\2\2\u022b\u0229\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u022e\3\2\2\2\u022d\u0227\3")
        buf.write("\2\2\2\u022e\u0231\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230")
        buf.write("\3\2\2\2\u0230\u0239\3\2\2\2\u0231\u022f\3\2\2\2\u0232")
        buf.write("\u0234\t\n\2\2\u0233\u0232\3\2\2\2\u0234\u0237\3\2\2\2")
        buf.write("\u0235\u0233\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0239\3")
        buf.write("\2\2\2\u0237\u0235\3\2\2\2\u0238\u022f\3\2\2\2\u0238\u0235")
        buf.write("\3\2\2\2\u0239\u023c\3\2\2\2\u023a\u023c\7\62\2\2\u023b")
        buf.write("\u0223\3\2\2\2\u023b\u023a\3\2\2\2\u023c\u0086\3\2\2\2")
        buf.write("\u023d\u023e\7\62\2\2\u023e\u0240\5\u00a5S\2\u023f\u0241")
        buf.write("\t\6\2\2\u0240\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242")
        buf.write("\u0240\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0255\3\2\2\2")
        buf.write("\u0244\u0246\59\35\2\u0245\u0247\t\7\2\2\u0246\u0245\3")
        buf.write("\2\2\2\u0247\u0248\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249")
        buf.write("\3\2\2\2\u0249\u024b\3\2\2\2\u024a\u0244\3\2\2\2\u024b")
        buf.write("\u024e\3\2\2\2\u024c\u024a\3\2\2\2\u024c\u024d\3\2\2\2")
        buf.write("\u024d\u0256\3\2\2\2\u024e\u024c\3\2\2\2\u024f\u0251\t")
        buf.write("\7\2\2\u0250\u024f\3\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250")
        buf.write("\3\2\2\2\u0252\u0253\3\2\2\2\u0253\u0256\3\2\2\2\u0254")
        buf.write("\u0252\3\2\2\2\u0255\u024c\3\2\2\2\u0255\u0252\3\2\2\2")
        buf.write("\u0256\u0088\3\2\2\2\u0257\u0259\7\62\2\2\u0258\u025a")
        buf.write("\t\b\2\2\u0259\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write("\u0259\3\2\2\2\u025b\u025c\3\2\2\2\u025c\u026e\3\2\2\2")
        buf.write("\u025d\u025f\59\35\2\u025e\u0260\t\t\2\2\u025f\u025e\3")
        buf.write("\2\2\2\u0260\u0261\3\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262")
        buf.write("\3\2\2\2\u0262\u0264\3\2\2\2\u0263\u025d\3\2\2\2\u0264")
        buf.write("\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2")
        buf.write("\u0266\u026f\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u026a\t")
        buf.write("\t\2\2\u0269\u0268\3\2\2\2\u026a\u026d\3\2\2\2\u026b\u0269")
        buf.write("\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026f\3\2\2\2\u026d")
        buf.write("\u026b\3\2\2\2\u026e\u0265\3\2\2\2\u026e\u026b\3\2\2\2")
        buf.write("\u026f\u008a\3\2\2\2\u0270\u0271\7\62\2\2\u0271\u0273")
        buf.write("\5\u00a1Q\2\u0272\u0274\7\63\2\2\u0273\u0272\3\2\2\2\u0274")
        buf.write("\u0275\3\2\2\2\u0275\u0273\3\2\2\2\u0275\u0276\3\2\2\2")
        buf.write("\u0276\u0288\3\2\2\2\u0277\u0279\59\35\2\u0278\u027a\t")
        buf.write("\n\2\2\u0279\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u0279")
        buf.write("\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027e\3\2\2\2\u027d")
        buf.write("\u0277\3\2\2\2\u027e\u0281\3\2\2\2\u027f\u027d\3\2\2\2")
        buf.write("\u027f\u0280\3\2\2\2\u0280\u0289\3\2\2\2\u0281\u027f\3")
        buf.write("\2\2\2\u0282\u0284\t\n\2\2\u0283\u0282\3\2\2\2\u0284\u0287")
        buf.write("\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2\u0286")
        buf.write("\u0289\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u027f\3\2\2\2")
        buf.write("\u0288\u0285\3\2\2\2\u0289\u008c\3\2\2\2\u028a\u028f\5")
        buf.write("\177@\2\u028b\u028f\5\u0087D\2\u028c\u028f\5\u0089E\2")
        buf.write("\u028d\u028f\5\u008bF\2\u028e\u028a\3\2\2\2\u028e\u028b")
        buf.write("\3\2\2\2\u028e\u028c\3\2\2\2\u028e\u028d\3\2\2\2\u028f")
        buf.write("\u0290\3\2\2\2\u0290\u0291\bG\b\2\u0291\u008e\3\2\2\2")
        buf.write("\u0292\u0297\5\177@\2\u0293\u0297\5\u0081A\2\u0294\u0297")
        buf.write("\5\u0083B\2\u0295\u0297\5\u0085C\2\u0296\u0292\3\2\2\2")
        buf.write("\u0296\u0293\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0295\3")
        buf.write("\2\2\2\u0297\u0298\3\2\2\2\u0298\u0299\bH\t\2\u0299\u029c")
        buf.write("\3\2\2\2\u029a\u029c\7\62\2\2\u029b\u0296\3\2\2\2\u029b")
        buf.write("\u029a\3\2\2\2\u029c\u0090\3\2\2\2\u029d\u02a1\7$\2\2")
        buf.write("\u029e\u02a0\5\u0095K\2\u029f\u029e\3\2\2\2\u02a0\u02a3")
        buf.write("\3\2\2\2\u02a1\u029f\3\2\2\2\u02a1\u02a2\3\2\2\2\u02a2")
        buf.write("\u02a4\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a4\u02a5\bI\n\2")
        buf.write("\u02a5\u0092\3\2\2\2\u02a6\u02aa\7$\2\2\u02a7\u02a9\5")
        buf.write("\u0095K\2\u02a8\u02a7\3\2\2\2\u02a9\u02ac\3\2\2\2\u02aa")
        buf.write("\u02a8\3\2\2\2\u02aa\u02ab\3\2\2\2\u02ab\u02ad\3\2\2\2")
        buf.write("\u02ac\u02aa\3\2\2\2\u02ad\u02ae\5\u0099M\2\u02ae\u02af")
        buf.write("\bJ\13\2\u02af\u0094\3\2\2\2\u02b0\u02b1\7)\2\2\u02b1")
        buf.write("\u02b5\7$\2\2\u02b2\u02b5\5\u0097L\2\u02b3\u02b5\n\13")
        buf.write("\2\2\u02b4\u02b0\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b4\u02b3")
        buf.write("\3\2\2\2\u02b5\u0096\3\2\2\2\u02b6\u02b7\7^\2\2\u02b7")
        buf.write("\u02b8\t\f\2\2\u02b8\u0098\3\2\2\2\u02b9\u02ba\7^\2\2")
        buf.write("\u02ba\u02bd\n\f\2\2\u02bb\u02bd\7^\2\2\u02bc\u02b9\3")
        buf.write("\2\2\2\u02bc\u02bb\3\2\2\2\u02bd\u009a\3\2\2\2\u02be\u02bf")
        buf.write("\7%\2\2\u02bf\u02c0\7%\2\2\u02c0\u02c4\3\2\2\2\u02c1\u02c3")
        buf.write("\13\2\2\2\u02c2\u02c1\3\2\2\2\u02c3\u02c6\3\2\2\2\u02c4")
        buf.write("\u02c5\3\2\2\2\u02c4\u02c2\3\2\2\2\u02c5\u02c7\3\2\2\2")
        buf.write("\u02c6\u02c4\3\2\2\2\u02c7\u02c8\7%\2\2\u02c8\u02c9\7")
        buf.write("%\2\2\u02c9\u02ca\3\2\2\2\u02ca\u02cb\bN\f\2\u02cb\u009c")
        buf.write("\3\2\2\2\u02cc\u02ce\t\r\2\2\u02cd\u02cc\3\2\2\2\u02ce")
        buf.write("\u02cf\3\2\2\2\u02cf\u02cd\3\2\2\2\u02cf\u02d0\3\2\2\2")
        buf.write("\u02d0\u02d1\3\2\2\2\u02d1\u02d2\bO\f\2\u02d2\u009e\3")
        buf.write("\2\2\2\u02d3\u02d4\13\2\2\2\u02d4\u02d5\bP\r\2\u02d5\u00a0")
        buf.write("\3\2\2\2\u02d6\u02d7\t\16\2\2\u02d7\u00a2\3\2\2\2\u02d8")
        buf.write("\u02d9\t\17\2\2\u02d9\u00a4\3\2\2\2\u02da\u02db\t\20\2")
        buf.write("\2\u02db\u00a6\3\2\2\2=\2\u00cf\u0186\u018d\u0195\u019f")
        buf.write("\u01a5\u01aa\u01b1\u01b7\u01b9\u01bd\u01c6\u01ce\u01d9")
        buf.write("\u01e2\u01e4\u01ec\u01f2\u01f6\u01fc\u01ff\u0202\u0208")
        buf.write("\u020e\u0212\u0218\u021b\u021e\u0225\u022b\u022f\u0235")
        buf.write("\u0238\u023b\u0242\u0248\u024c\u0252\u0255\u025b\u0261")
        buf.write("\u0265\u026b\u026e\u0275\u027b\u027f\u0285\u0288\u028e")
        buf.write("\u0296\u029b\u02a1\u02aa\u02b4\u02bc\u02c4\u02cf\16\3")
        buf.write("<\2\3?\3\3?\4\3?\5\3?\6\3?\7\3G\b\3H\t\3I\n\3J\13\b\2")
        buf.write("\2\3P\f")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    BREAK = 1
    CONTINUE = 2
    IF = 3
    ELSEIF = 4
    ELSE = 5
    FOREACH = 6
    BOOLLIT = 7
    TRUE = 8
    FALSE = 9
    ARRAY = 10
    IN = 11
    INT = 12
    FLOAT = 13
    BOOLEAN = 14
    STRING = 15
    RETURN = 16
    NULL = 17
    CLASS = 18
    VAL = 19
    VAR = 20
    CONSTRUCTOR = 21
    DESTRUCTOR = 22
    NEW = 23
    BY = 24
    SELF = 25
    DOUBLECOLONOP = 26
    DOUBLEDOTOP = 27
    UNDERSCORE = 28
    PLUSOP = 29
    MINUSOP = 30
    MULTIPLYOP = 31
    DIVIDEOP = 32
    MODULOOP = 33
    NOTOP = 34
    ANDOP = 35
    OROP = 36
    EQUALOP = 37
    ASSIGNOP = 38
    NOTEQUALOP = 39
    GTE = 40
    LTE = 41
    GT = 42
    LT = 43
    STREQUALOP = 44
    STRCONCATOP = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    LCB = 50
    RCB = 51
    DOT = 52
    COMMA = 53
    COLON = 54
    SEMICOLON = 55
    VARIABLE_IN_FUNC_IDENTIFIERS = 56
    DOLLAR_IDENTIFIERS = 57
    STRINGLIT = 58
    FLOATLIT = 59
    INTLIT_IN_ARRAY = 60
    INTLIT = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63
    BLOCK_COMMENT = 64
    WS = 65
    ERROR_CHAR = 66

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'::'", "'..'", "'_'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", 
            "'&&'", "'||'", "'=='", "'='", "'!='", "'>='", "'<='", "'>'", 
            "'<'", "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'.'", "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLLIT", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", 
            "PLUSOP", "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
            "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", "GTE", 
            "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", "LB", "RB", 
            "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", 
            "VARIABLE_IN_FUNC_IDENTIFIERS", "DOLLAR_IDENTIFIERS", "STRINGLIT", 
            "FLOATLIT", "INTLIT_IN_ARRAY", "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "BLOCK_COMMENT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "BOOLLIT", "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", 
                  "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", "VAL", 
                  "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "SELF", 
                  "DOUBLECOLONOP", "DOUBLEDOTOP", "UNDERSCORE", "PLUSOP", 
                  "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", 
                  "ANDOP", "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", 
                  "GTE", "LTE", "GT", "LT", "STREQUALOP", "STRCONCATOP", 
                  "LB", "RB", "LSB", "RSB", "LCB", "RCB", "DOT", "COMMA", 
                  "COLON", "SEMICOLON", "VARIABLE_IN_FUNC_IDENTIFIERS", 
                  "DOLLAR_IDENTIFIERS", "DOLLAR", "STRINGLIT", "DECIMALPART", 
                  "EXPONENTPART", "FLOATLIT", "DEC", "HEX", "OCT", "BIN", 
                  "HEX_ARRAY_SIZE", "OCT_ARRAY_SIZE", "BIN_ARRAY_SIZE", 
                  "INTLIT_IN_ARRAY", "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STRING_CHAR", "ESC_CHAR", "ESC_UNAVAILABLE", "BLOCK_COMMENT", 
                  "WS", "ERROR_CHAR", "B", "E", "X" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[58] = self.STRINGLIT_action 
            actions[61] = self.FLOATLIT_action 
            actions[69] = self.INTLIT_IN_ARRAY_action 
            actions[70] = self.INTLIT_action 
            actions[71] = self.UNCLOSE_STRING_action 
            actions[72] = self.ILLEGAL_ESCAPE_action 
            actions[78] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRINGLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    if str(self.text)[-1] == '"' and str(self.text)[-2] == '\'': 
                        raise UncloseString(str(self.text)[1:])
                    
                    current = self.text.find('\n')
                    if current != -1: 
                        raise UncloseString(str(self.text[:current - 1]))
                    self.text = str(self.text)[1:-1]

     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 2:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 3:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 4:
            self.text = self.text.replace("_", "")
     

        if actionIndex == 5:
            self.text = self.text.replace("_", "")
     

    def INTLIT_IN_ARRAY_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 6:
            self.text = self.text.replace("_", "")
     

    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 7:
            self.text = self.text.replace("_", "")
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 8:

            	current = str(self.text)
            	raise UncloseString(current[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 9:

            	current = str(self.text)
            	raise IllegalEscape(current[1:])

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 10:
             raise ErrorToken(self.text) 
     


