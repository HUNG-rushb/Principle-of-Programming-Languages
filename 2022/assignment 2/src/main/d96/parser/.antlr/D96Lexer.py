# Generated from d:\Github\Principle-of-Programming-Languages\2022\assignment 2\src\main\d96\parser\D96.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u02d7\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("\7E\u0264\nE\fE\16E\u0267\13E\3E\5E\u026a\nE\3F\3F\3F")
        buf.write("\6F\u026f\nF\rF\16F\u0270\3F\3F\6F\u0275\nF\rF\16F\u0276")
        buf.write("\7F\u0279\nF\fF\16F\u027c\13F\3F\7F\u027f\nF\fF\16F\u0282")
        buf.write("\13F\5F\u0284\nF\3G\3G\3G\3G\5G\u028a\nG\3G\3G\3H\3H\3")
        buf.write("H\3H\5H\u0292\nH\3H\3H\3H\5H\u0297\nH\3I\3I\7I\u029b\n")
        buf.write("I\fI\16I\u029e\13I\3I\3I\3J\3J\7J\u02a4\nJ\fJ\16J\u02a7")
        buf.write("\13J\3J\3J\3J\3K\3K\3K\3K\5K\u02b0\nK\3L\3L\3L\3M\3M\3")
        buf.write("M\5M\u02b8\nM\3N\3N\3N\3N\7N\u02be\nN\fN\16N\u02c1\13")
        buf.write("N\3N\3N\3N\3N\3N\3O\6O\u02c9\nO\rO\16O\u02ca\3O\3O\3P")
        buf.write("\3P\3P\3Q\3Q\3R\3R\3S\3S\3\u02bf\2T\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34")
        buf.write("\67\359\2;\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60")
        buf.write("a\61c\62e\63g\64i\65k\66m\67o8q9s:u\2w;y\2{\2}<\177\2")
        buf.write("\u0081\2\u0083\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d")
        buf.write("=\u008f>\u0091?\u0093@\u0095\2\u0097\2\u0099\2\u009bA")
        buf.write("\u009dB\u009fC\u00a1\2\u00a3\2\u00a5\2\3\2\21\5\2C\\a")
        buf.write("ac|\6\2\62;C\\aac|\3\2\62;\3\2\63;\4\2\63;CH\4\2\62;C")
        buf.write("H\3\2\639\3\2\629\3\2\62\63\4\2$$^^\t\2))^^ddhhppttvv")
        buf.write("\5\2\n\f\16\17\"\"\4\2DDdd\4\2GGgg\4\2ZZzz\2\u0306\2\3")
        buf.write("\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2")
        buf.write("\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2")
        buf.write("\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s")
        buf.write("\3\2\2\2\2w\3\2\2\2\2}\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\3\u00a7\3\2\2\2\5\u00ad")
        buf.write("\3\2\2\2\7\u00b6\3\2\2\2\t\u00b9\3\2\2\2\13\u00c0\3\2")
        buf.write("\2\2\r\u00c5\3\2\2\2\17\u00cf\3\2\2\2\21\u00d1\3\2\2\2")
        buf.write("\23\u00d6\3\2\2\2\25\u00dc\3\2\2\2\27\u00e2\3\2\2\2\31")
        buf.write("\u00e5\3\2\2\2\33\u00e9\3\2\2\2\35\u00ef\3\2\2\2\37\u00f7")
        buf.write("\3\2\2\2!\u00fe\3\2\2\2#\u0105\3\2\2\2%\u010a\3\2\2\2")
        buf.write("\'\u0110\3\2\2\2)\u0114\3\2\2\2+\u0118\3\2\2\2-\u0124")
        buf.write("\3\2\2\2/\u012f\3\2\2\2\61\u0133\3\2\2\2\63\u0136\3\2")
        buf.write("\2\2\65\u013b\3\2\2\2\67\u013e\3\2\2\29\u0141\3\2\2\2")
        buf.write(";\u0143\3\2\2\2=\u0145\3\2\2\2?\u0147\3\2\2\2A\u0149\3")
        buf.write("\2\2\2C\u014b\3\2\2\2E\u014d\3\2\2\2G\u014f\3\2\2\2I\u0152")
        buf.write("\3\2\2\2K\u0155\3\2\2\2M\u0158\3\2\2\2O\u015a\3\2\2\2")
        buf.write("Q\u015d\3\2\2\2S\u0160\3\2\2\2U\u0163\3\2\2\2W\u0165\3")
        buf.write("\2\2\2Y\u0167\3\2\2\2[\u016b\3\2\2\2]\u016e\3\2\2\2_\u0170")
        buf.write("\3\2\2\2a\u0172\3\2\2\2c\u0174\3\2\2\2e\u0176\3\2\2\2")
        buf.write("g\u0178\3\2\2\2i\u017a\3\2\2\2k\u017c\3\2\2\2m\u017e\3")
        buf.write("\2\2\2o\u0180\3\2\2\2q\u0182\3\2\2\2s\u0189\3\2\2\2u\u018f")
        buf.write("\3\2\2\2w\u0191\3\2\2\2y\u019b\3\2\2\2{\u01a2\3\2\2\2")
        buf.write("}\u01d9\3\2\2\2\177\u01dd\3\2\2\2\u0081\u01e7\3\2\2\2")
        buf.write("\u0083\u0204\3\2\2\2\u0085\u0220\3\2\2\2\u0087\u023d\3")
        buf.write("\2\2\2\u0089\u0257\3\2\2\2\u008b\u026b\3\2\2\2\u008d\u0289")
        buf.write("\3\2\2\2\u008f\u0296\3\2\2\2\u0091\u0298\3\2\2\2\u0093")
        buf.write("\u02a1\3\2\2\2\u0095\u02af\3\2\2\2\u0097\u02b1\3\2\2\2")
        buf.write("\u0099\u02b7\3\2\2\2\u009b\u02b9\3\2\2\2\u009d\u02c8\3")
        buf.write("\2\2\2\u009f\u02ce\3\2\2\2\u00a1\u02d1\3\2\2\2\u00a3\u02d3")
        buf.write("\3\2\2\2\u00a5\u02d5\3\2\2\2\u00a7\u00a8\7D\2\2\u00a8")
        buf.write("\u00a9\7t\2\2\u00a9\u00aa\7g\2\2\u00aa\u00ab\7c\2\2\u00ab")
        buf.write("\u00ac\7m\2\2\u00ac\4\3\2\2\2\u00ad\u00ae\7E\2\2\u00ae")
        buf.write("\u00af\7q\2\2\u00af\u00b0\7p\2\2\u00b0\u00b1\7v\2\2\u00b1")
        buf.write("\u00b2\7k\2\2\u00b2\u00b3\7p\2\2\u00b3\u00b4\7w\2\2\u00b4")
        buf.write("\u00b5\7g\2\2\u00b5\6\3\2\2\2\u00b6\u00b7\7K\2\2\u00b7")
        buf.write("\u00b8\7h\2\2\u00b8\b\3\2\2\2\u00b9\u00ba\7G\2\2\u00ba")
        buf.write("\u00bb\7n\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd\7g\2\2\u00bd")
        buf.write("\u00be\7k\2\2\u00be\u00bf\7h\2\2\u00bf\n\3\2\2\2\u00c0")
        buf.write("\u00c1\7G\2\2\u00c1\u00c2\7n\2\2\u00c2\u00c3\7u\2\2\u00c3")
        buf.write("\u00c4\7g\2\2\u00c4\f\3\2\2\2\u00c5\u00c6\7H\2\2\u00c6")
        buf.write("\u00c7\7q\2\2\u00c7\u00c8\7t\2\2\u00c8\u00c9\7g\2\2\u00c9")
        buf.write("\u00ca\7c\2\2\u00ca\u00cb\7e\2\2\u00cb\u00cc\7j\2\2\u00cc")
        buf.write("\16\3\2\2\2\u00cd\u00d0\5\21\t\2\u00ce\u00d0\5\23\n\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00cf\u00ce\3\2\2\2\u00d0\20\3\2")
        buf.write("\2\2\u00d1\u00d2\7V\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4")
        buf.write("\7w\2\2\u00d4\u00d5\7g\2\2\u00d5\22\3\2\2\2\u00d6\u00d7")
        buf.write("\7H\2\2\u00d7\u00d8\7c\2\2\u00d8\u00d9\7n\2\2\u00d9\u00da")
        buf.write("\7u\2\2\u00da\u00db\7g\2\2\u00db\24\3\2\2\2\u00dc\u00dd")
        buf.write("\7C\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7t\2\2\u00df\u00e0")
        buf.write("\7c\2\2\u00e0\u00e1\7{\2\2\u00e1\26\3\2\2\2\u00e2\u00e3")
        buf.write("\7K\2\2\u00e3\u00e4\7p\2\2\u00e4\30\3\2\2\2\u00e5\u00e6")
        buf.write("\7K\2\2\u00e6\u00e7\7p\2\2\u00e7\u00e8\7v\2\2\u00e8\32")
        buf.write("\3\2\2\2\u00e9\u00ea\7H\2\2\u00ea\u00eb\7n\2\2\u00eb\u00ec")
        buf.write("\7q\2\2\u00ec\u00ed\7c\2\2\u00ed\u00ee\7v\2\2\u00ee\34")
        buf.write("\3\2\2\2\u00ef\u00f0\7D\2\2\u00f0\u00f1\7q\2\2\u00f1\u00f2")
        buf.write("\7q\2\2\u00f2\u00f3\7n\2\2\u00f3\u00f4\7g\2\2\u00f4\u00f5")
        buf.write("\7c\2\2\u00f5\u00f6\7p\2\2\u00f6\36\3\2\2\2\u00f7\u00f8")
        buf.write("\7U\2\2\u00f8\u00f9\7v\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb")
        buf.write("\7k\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd\7i\2\2\u00fd \3")
        buf.write("\2\2\2\u00fe\u00ff\7T\2\2\u00ff\u0100\7g\2\2\u0100\u0101")
        buf.write("\7v\2\2\u0101\u0102\7w\2\2\u0102\u0103\7t\2\2\u0103\u0104")
        buf.write("\7p\2\2\u0104\"\3\2\2\2\u0105\u0106\7P\2\2\u0106\u0107")
        buf.write("\7w\2\2\u0107\u0108\7n\2\2\u0108\u0109\7n\2\2\u0109$\3")
        buf.write("\2\2\2\u010a\u010b\7E\2\2\u010b\u010c\7n\2\2\u010c\u010d")
        buf.write("\7c\2\2\u010d\u010e\7u\2\2\u010e\u010f\7u\2\2\u010f&\3")
        buf.write("\2\2\2\u0110\u0111\7X\2\2\u0111\u0112\7c\2\2\u0112\u0113")
        buf.write("\7n\2\2\u0113(\3\2\2\2\u0114\u0115\7X\2\2\u0115\u0116")
        buf.write("\7c\2\2\u0116\u0117\7t\2\2\u0117*\3\2\2\2\u0118\u0119")
        buf.write("\7E\2\2\u0119\u011a\7q\2\2\u011a\u011b\7p\2\2\u011b\u011c")
        buf.write("\7u\2\2\u011c\u011d\7v\2\2\u011d\u011e\7t\2\2\u011e\u011f")
        buf.write("\7w\2\2\u011f\u0120\7e\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7q\2\2\u0122\u0123\7t\2\2\u0123,\3\2\2\2\u0124\u0125")
        buf.write("\7F\2\2\u0125\u0126\7g\2\2\u0126\u0127\7u\2\2\u0127\u0128")
        buf.write("\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a\u012b")
        buf.write("\7e\2\2\u012b\u012c\7v\2\2\u012c\u012d\7q\2\2\u012d\u012e")
        buf.write("\7t\2\2\u012e.\3\2\2\2\u012f\u0130\7P\2\2\u0130\u0131")
        buf.write("\7g\2\2\u0131\u0132\7y\2\2\u0132\60\3\2\2\2\u0133\u0134")
        buf.write("\7D\2\2\u0134\u0135\7{\2\2\u0135\62\3\2\2\2\u0136\u0137")
        buf.write("\7U\2\2\u0137\u0138\7g\2\2\u0138\u0139\7n\2\2\u0139\u013a")
        buf.write("\7h\2\2\u013a\64\3\2\2\2\u013b\u013c\7<\2\2\u013c\u013d")
        buf.write("\7<\2\2\u013d\66\3\2\2\2\u013e\u013f\7\60\2\2\u013f\u0140")
        buf.write("\7\60\2\2\u01408\3\2\2\2\u0141\u0142\7a\2\2\u0142:\3\2")
        buf.write("\2\2\u0143\u0144\7-\2\2\u0144<\3\2\2\2\u0145\u0146\7/")
        buf.write("\2\2\u0146>\3\2\2\2\u0147\u0148\7,\2\2\u0148@\3\2\2\2")
        buf.write("\u0149\u014a\7\61\2\2\u014aB\3\2\2\2\u014b\u014c\7\'\2")
        buf.write("\2\u014cD\3\2\2\2\u014d\u014e\7#\2\2\u014eF\3\2\2\2\u014f")
        buf.write("\u0150\7(\2\2\u0150\u0151\7(\2\2\u0151H\3\2\2\2\u0152")
        buf.write("\u0153\7~\2\2\u0153\u0154\7~\2\2\u0154J\3\2\2\2\u0155")
        buf.write("\u0156\7?\2\2\u0156\u0157\7?\2\2\u0157L\3\2\2\2\u0158")
        buf.write("\u0159\7?\2\2\u0159N\3\2\2\2\u015a\u015b\7#\2\2\u015b")
        buf.write("\u015c\7?\2\2\u015cP\3\2\2\2\u015d\u015e\7@\2\2\u015e")
        buf.write("\u015f\7?\2\2\u015fR\3\2\2\2\u0160\u0161\7>\2\2\u0161")
        buf.write("\u0162\7?\2\2\u0162T\3\2\2\2\u0163\u0164\7@\2\2\u0164")
        buf.write("V\3\2\2\2\u0165\u0166\7>\2\2\u0166X\3\2\2\2\u0167\u0168")
        buf.write("\7?\2\2\u0168\u0169\7?\2\2\u0169\u016a\7\60\2\2\u016a")
        buf.write("Z\3\2\2\2\u016b\u016c\7-\2\2\u016c\u016d\7\60\2\2\u016d")
        buf.write("\\\3\2\2\2\u016e\u016f\7*\2\2\u016f^\3\2\2\2\u0170\u0171")
        buf.write("\7+\2\2\u0171`\3\2\2\2\u0172\u0173\7]\2\2\u0173b\3\2\2")
        buf.write("\2\u0174\u0175\7_\2\2\u0175d\3\2\2\2\u0176\u0177\7}\2")
        buf.write("\2\u0177f\3\2\2\2\u0178\u0179\7\177\2\2\u0179h\3\2\2\2")
        buf.write("\u017a\u017b\7\60\2\2\u017bj\3\2\2\2\u017c\u017d\7.\2")
        buf.write("\2\u017dl\3\2\2\2\u017e\u017f\7<\2\2\u017fn\3\2\2\2\u0180")
        buf.write("\u0181\7=\2\2\u0181p\3\2\2\2\u0182\u0186\t\2\2\2\u0183")
        buf.write("\u0185\t\3\2\2\u0184\u0183\3\2\2\2\u0185\u0188\3\2\2\2")
        buf.write("\u0186\u0184\3\2\2\2\u0186\u0187\3\2\2\2\u0187r\3\2\2")
        buf.write("\2\u0188\u0186\3\2\2\2\u0189\u018b\5u;\2\u018a\u018c\t")
        buf.write("\3\2\2\u018b\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018b")
        buf.write("\3\2\2\2\u018d\u018e\3\2\2\2\u018et\3\2\2\2\u018f\u0190")
        buf.write("\7&\2\2\u0190v\3\2\2\2\u0191\u0195\7$\2\2\u0192\u0194")
        buf.write("\5\u0095K\2\u0193\u0192\3\2\2\2\u0194\u0197\3\2\2\2\u0195")
        buf.write("\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196\u0198\3\2\2\2")
        buf.write("\u0197\u0195\3\2\2\2\u0198\u0199\7$\2\2\u0199\u019a\b")
        buf.write("<\2\2\u019ax\3\2\2\2\u019b\u019f\7\60\2\2\u019c\u019e")
        buf.write("\t\4\2\2\u019d\u019c\3\2\2\2\u019e\u01a1\3\2\2\2\u019f")
        buf.write("\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0z\3\2\2\2\u01a1")
        buf.write("\u019f\3\2\2\2\u01a2\u01a5\5\u00a3R\2\u01a3\u01a6\5=\37")
        buf.write("\2\u01a4\u01a6\5;\36\2\u01a5\u01a3\3\2\2\2\u01a5\u01a4")
        buf.write("\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u01b9\3\2\2\2\u01a7")
        buf.write("\u01a9\7\62\2\2\u01a8\u01a7\3\2\2\2\u01a9\u01ac\3\2\2")
        buf.write("\2\u01aa\u01a8\3\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ad")
        buf.write("\3\2\2\2\u01ac\u01aa\3\2\2\2\u01ad\u01b1\t\5\2\2\u01ae")
        buf.write("\u01b0\t\4\2\2\u01af\u01ae\3\2\2\2\u01b0\u01b3\3\2\2\2")
        buf.write("\u01b1\u01af\3\2\2\2\u01b1\u01b2\3\2\2\2\u01b2\u01ba\3")
        buf.write("\2\2\2\u01b3\u01b1\3\2\2\2\u01b4\u01b6\7\62\2\2\u01b5")
        buf.write("\u01b4\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b5\3\2\2\2")
        buf.write("\u01b7\u01b8\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01aa\3")
        buf.write("\2\2\2\u01b9\u01b5\3\2\2\2\u01ba|\3\2\2\2\u01bb\u01be")
        buf.write("\5\177@\2\u01bc\u01be\7\62\2\2\u01bd\u01bb\3\2\2\2\u01bd")
        buf.write("\u01bc\3\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\5y=\2\u01c0")
        buf.write("\u01c1\5{>\2\u01c1\u01c2\3\2\2\2\u01c2\u01c3\b?\3\2\u01c3")
        buf.write("\u01da\3\2\2\2\u01c4\u01c7\5\177@\2\u01c5\u01c7\7\62\2")
        buf.write("\2\u01c6\u01c4\3\2\2\2\u01c6\u01c5\3\2\2\2\u01c7\u01c8")
        buf.write("\3\2\2\2\u01c8\u01c9\5y=\2\u01c9\u01ca\3\2\2\2\u01ca\u01cb")
        buf.write("\b?\4\2\u01cb\u01da\3\2\2\2\u01cc\u01cf\5\177@\2\u01cd")
        buf.write("\u01cf\7\62\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cd\3\2\2")
        buf.write("\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\5{>\2\u01d1\u01d2\3")
        buf.write("\2\2\2\u01d2\u01d3\b?\5\2\u01d3\u01da\3\2\2\2\u01d4\u01d5")
        buf.write("\5y=\2\u01d5\u01d6\5{>\2\u01d6\u01d7\3\2\2\2\u01d7\u01d8")
        buf.write("\b?\6\2\u01d8\u01da\3\2\2\2\u01d9\u01bd\3\2\2\2\u01d9")
        buf.write("\u01c6\3\2\2\2\u01d9\u01ce\3\2\2\2\u01d9\u01d4\3\2\2\2")
        buf.write("\u01da\u01db\3\2\2\2\u01db\u01dc\b?\7\2\u01dc~\3\2\2\2")
        buf.write("\u01dd\u01e4\t\5\2\2\u01de\u01df\59\35\2\u01df\u01e0\t")
        buf.write("\4\2\2\u01e0\u01e3\3\2\2\2\u01e1\u01e3\t\4\2\2\u01e2\u01de")
        buf.write("\3\2\2\2\u01e2\u01e1\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e5\u0080\3\2\2\2")
        buf.write("\u01e6\u01e4\3\2\2\2\u01e7\u01e8\7\62\2\2\u01e8\u0202")
        buf.write("\5\u00a5S\2\u01e9\u01eb\t\6\2\2\u01ea\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\u01ea\3\2\2\2\u01ec\u01ed\3\2\2\2")
        buf.write("\u01ed\u01ff\3\2\2\2\u01ee\u01f0\59\35\2\u01ef\u01f1\t")
        buf.write("\7\2\2\u01f0\u01ef\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f0")
        buf.write("\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f5\3\2\2\2\u01f4")
        buf.write("\u01ee\3\2\2\2\u01f5\u01f8\3\2\2\2\u01f6\u01f4\3\2\2\2")
        buf.write("\u01f6\u01f7\3\2\2\2\u01f7\u0200\3\2\2\2\u01f8\u01f6\3")
        buf.write("\2\2\2\u01f9\u01fb\t\7\2\2\u01fa\u01f9\3\2\2\2\u01fb\u01fe")
        buf.write("\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd")
        buf.write("\u0200\3\2\2\2\u01fe\u01fc\3\2\2\2\u01ff\u01f6\3\2\2\2")
        buf.write("\u01ff\u01fc\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u0203\7")
        buf.write("\62\2\2\u0202\u01ea\3\2\2\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0082\3\2\2\2\u0204\u021e\7\62\2\2\u0205\u0207\t\b\2")
        buf.write("\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u0206")
        buf.write("\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u021b\3\2\2\2\u020a")
        buf.write("\u020c\59\35\2\u020b\u020d\t\t\2\2\u020c\u020b\3\2\2\2")
        buf.write("\u020d\u020e\3\2\2\2\u020e\u020c\3\2\2\2\u020e\u020f\3")
        buf.write("\2\2\2\u020f\u0211\3\2\2\2\u0210\u020a\3\2\2\2\u0211\u0214")
        buf.write("\3\2\2\2\u0212\u0210\3\2\2\2\u0212\u0213\3\2\2\2\u0213")
        buf.write("\u021c\3\2\2\2\u0214\u0212\3\2\2\2\u0215\u0217\t\t\2\2")
        buf.write("\u0216\u0215\3\2\2\2\u0217\u021a\3\2\2\2\u0218\u0216\3")
        buf.write("\2\2\2\u0218\u0219\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218")
        buf.write("\3\2\2\2\u021b\u0212\3\2\2\2\u021b\u0218\3\2\2\2\u021c")
        buf.write("\u021f\3\2\2\2\u021d\u021f\7\62\2\2\u021e\u0206\3\2\2")
        buf.write("\2\u021e\u021d\3\2\2\2\u021f\u0084\3\2\2\2\u0220\u0221")
        buf.write("\7\62\2\2\u0221\u023b\5\u00a1Q\2\u0222\u0224\7\63\2\2")
        buf.write("\u0223\u0222\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0223\3")
        buf.write("\2\2\2\u0225\u0226\3\2\2\2\u0226\u0238\3\2\2\2\u0227\u0229")
        buf.write("\59\35\2\u0228\u022a\t\n\2\2\u0229\u0228\3\2\2\2\u022a")
        buf.write("\u022b\3\2\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2")
        buf.write("\u022c\u022e\3\2\2\2\u022d\u0227\3\2\2\2\u022e\u0231\3")
        buf.write("\2\2\2\u022f\u022d\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0239")
        buf.write("\3\2\2\2\u0231\u022f\3\2\2\2\u0232\u0234\t\n\2\2\u0233")
        buf.write("\u0232\3\2\2\2\u0234\u0237\3\2\2\2\u0235\u0233\3\2\2\2")
        buf.write("\u0235\u0236\3\2\2\2\u0236\u0239\3\2\2\2\u0237\u0235\3")
        buf.write("\2\2\2\u0238\u022f\3\2\2\2\u0238\u0235\3\2\2\2\u0239\u023c")
        buf.write("\3\2\2\2\u023a\u023c\7\62\2\2\u023b\u0223\3\2\2\2\u023b")
        buf.write("\u023a\3\2\2\2\u023c\u0086\3\2\2\2\u023d\u023e\7\62\2")
        buf.write("\2\u023e\u0240\5\u00a5S\2\u023f\u0241\t\6\2\2\u0240\u023f")
        buf.write("\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0240\3\2\2\2\u0242")
        buf.write("\u0243\3\2\2\2\u0243\u0255\3\2\2\2\u0244\u0246\59\35\2")
        buf.write("\u0245\u0247\t\7\2\2\u0246\u0245\3\2\2\2\u0247\u0248\3")
        buf.write("\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3\2\2\2\u0249\u024b")
        buf.write("\3\2\2\2\u024a\u0244\3\2\2\2\u024b\u024e\3\2\2\2\u024c")
        buf.write("\u024a\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u0256\3\2\2\2")
        buf.write("\u024e\u024c\3\2\2\2\u024f\u0251\t\7\2\2\u0250\u024f\3")
        buf.write("\2\2\2\u0251\u0254\3\2\2\2\u0252\u0250\3\2\2\2\u0252\u0253")
        buf.write("\3\2\2\2\u0253\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0255")
        buf.write("\u024c\3\2\2\2\u0255\u0252\3\2\2\2\u0256\u0088\3\2\2\2")
        buf.write("\u0257\u0259\7\62\2\2\u0258\u025a\t\b\2\2\u0259\u0258")
        buf.write("\3\2\2\2\u025a\u025b\3\2\2\2\u025b\u0259\3\2\2\2\u025b")
        buf.write("\u025c\3\2\2\2\u025c\u0269\3\2\2\2\u025d\u025f\59\35\2")
        buf.write("\u025e\u0260\t\t\2\2\u025f\u025e\3\2\2\2\u0260\u0261\3")
        buf.write("\2\2\2\u0261\u025f\3\2\2\2\u0261\u0262\3\2\2\2\u0262\u0264")
        buf.write("\3\2\2\2\u0263\u025d\3\2\2\2\u0264\u0267\3\2\2\2\u0265")
        buf.write("\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266\u026a\3\2\2\2")
        buf.write("\u0267\u0265\3\2\2\2\u0268\u026a\t\t\2\2\u0269\u0265\3")
        buf.write("\2\2\2\u0269\u0268\3\2\2\2\u026a\u008a\3\2\2\2\u026b\u026c")
        buf.write("\7\62\2\2\u026c\u026e\5\u00a1Q\2\u026d\u026f\7\63\2\2")
        buf.write("\u026e\u026d\3\2\2\2\u026f\u0270\3\2\2\2\u0270\u026e\3")
        buf.write("\2\2\2\u0270\u0271\3\2\2\2\u0271\u0283\3\2\2\2\u0272\u0274")
        buf.write("\59\35\2\u0273\u0275\t\n\2\2\u0274\u0273\3\2\2\2\u0275")
        buf.write("\u0276\3\2\2\2\u0276\u0274\3\2\2\2\u0276\u0277\3\2\2\2")
        buf.write("\u0277\u0279\3\2\2\2\u0278\u0272\3\2\2\2\u0279\u027c\3")
        buf.write("\2\2\2\u027a\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b\u0284")
        buf.write("\3\2\2\2\u027c\u027a\3\2\2\2\u027d\u027f\t\n\2\2\u027e")
        buf.write("\u027d\3\2\2\2\u027f\u0282\3\2\2\2\u0280\u027e\3\2\2\2")
        buf.write("\u0280\u0281\3\2\2\2\u0281\u0284\3\2\2\2\u0282\u0280\3")
        buf.write("\2\2\2\u0283\u027a\3\2\2\2\u0283\u0280\3\2\2\2\u0284\u008c")
        buf.write("\3\2\2\2\u0285\u028a\5\177@\2\u0286\u028a\5\u0087D\2\u0287")
        buf.write("\u028a\5\u0089E\2\u0288\u028a\5\u008bF\2\u0289\u0285\3")
        buf.write("\2\2\2\u0289\u0286\3\2\2\2\u0289\u0287\3\2\2\2\u0289\u0288")
        buf.write("\3\2\2\2\u028a\u028b\3\2\2\2\u028b\u028c\bG\b\2\u028c")
        buf.write("\u008e\3\2\2\2\u028d\u0292\5\177@\2\u028e\u0292\5\u0081")
        buf.write("A\2\u028f\u0292\5\u0083B\2\u0290\u0292\5\u0085C\2\u0291")
        buf.write("\u028d\3\2\2\2\u0291\u028e\3\2\2\2\u0291\u028f\3\2\2\2")
        buf.write("\u0291\u0290\3\2\2\2\u0292\u0293\3\2\2\2\u0293\u0294\b")
        buf.write("H\t\2\u0294\u0297\3\2\2\2\u0295\u0297\7\62\2\2\u0296\u0291")
        buf.write("\3\2\2\2\u0296\u0295\3\2\2\2\u0297\u0090\3\2\2\2\u0298")
        buf.write("\u029c\7$\2\2\u0299\u029b\5\u0095K\2\u029a\u0299\3\2\2")
        buf.write("\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2\u029c\u029d")
        buf.write("\3\2\2\2\u029d\u029f\3\2\2\2\u029e\u029c\3\2\2\2\u029f")
        buf.write("\u02a0\bI\n\2\u02a0\u0092\3\2\2\2\u02a1\u02a5\7$\2\2\u02a2")
        buf.write("\u02a4\5\u0095K\2\u02a3\u02a2\3\2\2\2\u02a4\u02a7\3\2")
        buf.write("\2\2\u02a5\u02a3\3\2\2\2\u02a5\u02a6\3\2\2\2\u02a6\u02a8")
        buf.write("\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a8\u02a9\5\u0099M\2\u02a9")
        buf.write("\u02aa\bJ\13\2\u02aa\u0094\3\2\2\2\u02ab\u02ac\7)\2\2")
        buf.write("\u02ac\u02b0\7$\2\2\u02ad\u02b0\5\u0097L\2\u02ae\u02b0")
        buf.write("\n\13\2\2\u02af\u02ab\3\2\2\2\u02af\u02ad\3\2\2\2\u02af")
        buf.write("\u02ae\3\2\2\2\u02b0\u0096\3\2\2\2\u02b1\u02b2\7^\2\2")
        buf.write("\u02b2\u02b3\t\f\2\2\u02b3\u0098\3\2\2\2\u02b4\u02b5\7")
        buf.write("^\2\2\u02b5\u02b8\n\f\2\2\u02b6\u02b8\7^\2\2\u02b7\u02b4")
        buf.write("\3\2\2\2\u02b7\u02b6\3\2\2\2\u02b8\u009a\3\2\2\2\u02b9")
        buf.write("\u02ba\7%\2\2\u02ba\u02bb\7%\2\2\u02bb\u02bf\3\2\2\2\u02bc")
        buf.write("\u02be\13\2\2\2\u02bd\u02bc\3\2\2\2\u02be\u02c1\3\2\2")
        buf.write("\2\u02bf\u02c0\3\2\2\2\u02bf\u02bd\3\2\2\2\u02c0\u02c2")
        buf.write("\3\2\2\2\u02c1\u02bf\3\2\2\2\u02c2\u02c3\7%\2\2\u02c3")
        buf.write("\u02c4\7%\2\2\u02c4\u02c5\3\2\2\2\u02c5\u02c6\bN\f\2\u02c6")
        buf.write("\u009c\3\2\2\2\u02c7\u02c9\t\r\2\2\u02c8\u02c7\3\2\2\2")
        buf.write("\u02c9\u02ca\3\2\2\2\u02ca\u02c8\3\2\2\2\u02ca\u02cb\3")
        buf.write("\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02cd\bO\f\2\u02cd\u009e")
        buf.write("\3\2\2\2\u02ce\u02cf\13\2\2\2\u02cf\u02d0\bP\r\2\u02d0")
        buf.write("\u00a0\3\2\2\2\u02d1\u02d2\t\16\2\2\u02d2\u00a2\3\2\2")
        buf.write("\2\u02d3\u02d4\t\17\2\2\u02d4\u00a4\3\2\2\2\u02d5\u02d6")
        buf.write("\t\20\2\2\u02d6\u00a6\3\2\2\2<\2\u00cf\u0186\u018d\u0195")
        buf.write("\u019f\u01a5\u01aa\u01b1\u01b7\u01b9\u01bd\u01c6\u01ce")
        buf.write("\u01d9\u01e2\u01e4\u01ec\u01f2\u01f6\u01fc\u01ff\u0202")
        buf.write("\u0208\u020e\u0212\u0218\u021b\u021e\u0225\u022b\u022f")
        buf.write("\u0235\u0238\u023b\u0242\u0248\u024c\u0252\u0255\u025b")
        buf.write("\u0261\u0265\u0269\u0270\u0276\u027a\u0280\u0283\u0289")
        buf.write("\u0291\u0296\u029c\u02a5\u02af\u02b7\u02bf\u02ca\16\3")
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
    PLUSOP = 28
    MINUSOP = 29
    MULTIPLYOP = 30
    DIVIDEOP = 31
    MODULOOP = 32
    NOTOP = 33
    ANDOP = 34
    OROP = 35
    EQUALOP = 36
    ASSIGNOP = 37
    NOTEQUALOP = 38
    GTE = 39
    LTE = 40
    GT = 41
    LT = 42
    STREQUALOP = 43
    STRCONCATOP = 44
    LB = 45
    RB = 46
    LSB = 47
    RSB = 48
    LCB = 49
    RCB = 50
    DOT = 51
    COMMA = 52
    COLON = 53
    SEMICOLON = 54
    VARIABLE_IN_FUNC_IDENTIFIERS = 55
    DOLLAR_IDENTIFIERS = 56
    STRINGLIT = 57
    FLOATLIT = 58
    INTLIT_IN_ARRAY = 59
    INTLIT = 60
    UNCLOSE_STRING = 61
    ILLEGAL_ESCAPE = 62
    BLOCK_COMMENT = 63
    WS = 64
    ERROR_CHAR = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", "'Foreach'", 
            "'True'", "'False'", "'Array'", "'In'", "'Int'", "'Float'", 
            "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
            "'Var'", "'Constructor'", "'Destructor'", "'New'", "'By'", "'Self'", 
            "'::'", "'..'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", 
            "'||'", "'=='", "'='", "'!='", "'>='", "'<='", "'>'", "'<'", 
            "'==.'", "'+.'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'.'", 
            "','", "':'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "BOOLLIT", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "DOUBLECOLONOP", "DOUBLEDOTOP", "PLUSOP", 
            "MINUSOP", "MULTIPLYOP", "DIVIDEOP", "MODULOOP", "NOTOP", "ANDOP", 
            "OROP", "EQUALOP", "ASSIGNOP", "NOTEQUALOP", "GTE", "LTE", "GT", 
            "LT", "STREQUALOP", "STRCONCATOP", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "DOT", "COMMA", "COLON", "SEMICOLON", "VARIABLE_IN_FUNC_IDENTIFIERS", 
            "DOLLAR_IDENTIFIERS", "STRINGLIT", "FLOATLIT", "INTLIT_IN_ARRAY", 
            "INTLIT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "BLOCK_COMMENT", 
            "WS", "ERROR_CHAR" ]

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
                        if not str(self.text)[-3] == '\\':
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
     


