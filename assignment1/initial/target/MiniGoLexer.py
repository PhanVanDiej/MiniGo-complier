# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2h")
        buf.write("\u030c\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\17")
        buf.write("\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3%\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&")
        buf.write("\3&\3\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3")
        buf.write(",\3,\3,\3-\3-\3-\3.\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\39\39\3")
        buf.write("9\39\39\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3<\3<\3=\3")
        buf.write("=\3>\3>\3?\3?\3@\3@\3A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3")
        buf.write("E\3F\3F\3F\3G\3G\3G\3H\3H\3H\3I\3I\3I\3J\3J\3K\3K\3K\3")
        buf.write("L\3L\3M\3M\3M\3N\3N\3N\3O\3O\3O\3P\3P\3Q\3Q\3Q\5Q\u021b")
        buf.write("\nQ\3R\3R\3R\6R\u0220\nR\rR\16R\u0221\3S\3S\7S\u0226\n")
        buf.write("S\fS\16S\u0229\13S\3S\5S\u022c\nS\3T\3T\6T\u0230\nT\r")
        buf.write("T\16T\u0231\3U\3U\3U\6U\u0237\nU\rU\16U\u0238\3V\3V\5")
        buf.write("V\u023d\nV\3W\6W\u0240\nW\rW\16W\u0241\3W\3W\7W\u0246")
        buf.write("\nW\fW\16W\u0249\13W\3W\5W\u024c\nW\3W\3W\6W\u0250\nW")
        buf.write("\rW\16W\u0251\3W\5W\u0255\nW\3W\6W\u0258\nW\rW\16W\u0259")
        buf.write("\3W\5W\u025d\nW\3X\3X\3X\6X\u0262\nX\rX\16X\u0263\3X\3")
        buf.write("X\7X\u0268\nX\fX\16X\u026b\13X\3X\3X\3X\3X\3X\6X\u0272")
        buf.write("\nX\rX\16X\u0273\3X\3X\3X\3X\6X\u027a\nX\rX\16X\u027b")
        buf.write("\3X\5X\u027f\nX\3Y\3Y\5Y\u0283\nY\3Y\6Y\u0286\nY\rY\16")
        buf.write("Y\u0287\3Z\3Z\5Z\u028c\nZ\3Z\6Z\u028f\nZ\rZ\16Z\u0290")
        buf.write("\3[\3[\3[\3[\3[\3[\3[\3[\3[\5[\u029c\n[\3\\\3\\\5\\\u02a0")
        buf.write("\n\\\3]\3]\7]\u02a4\n]\f]\16]\u02a7\13]\3]\3]\3^\3^\3")
        buf.write("^\7^\u02ae\n^\f^\16^\u02b1\13^\3^\3^\3_\3_\3_\3`\3`\3")
        buf.write("`\5`\u02bb\n`\3`\3`\3a\3a\7a\u02c1\na\fa\16a\u02c4\13")
        buf.write("a\3b\3b\3b\3b\7b\u02ca\nb\fb\16b\u02cd\13b\3b\3b\3c\3")
        buf.write("c\3c\3c\3c\7c\u02d6\nc\fc\16c\u02d9\13c\3c\3c\3c\3c\3")
        buf.write("c\3d\6d\u02e1\nd\rd\16d\u02e2\3d\3d\3e\3e\3e\3f\3f\3f")
        buf.write("\3f\7f\u02ee\nf\ff\16f\u02f1\13f\3f\3f\3f\7f\u02f6\nf")
        buf.write("\ff\16f\u02f9\13f\3f\3f\3g\3g\3g\3h\3h\3h\7h\u0303\nh")
        buf.write("\fh\16h\u0306\13h\3h\5h\u0309\nh\3h\3h\3\u02d7\2i\3\3")
        buf.write("\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w")
        buf.write("=y>{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008b")
        buf.write("G\u008dH\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009b")
        buf.write("O\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00ab")
        buf.write("W\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb")
        buf.write("_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7e\u00c9f\u00cb")
        buf.write("g\u00cd\2\u00cfh\3\2\27\4\2DDdd\3\2\62\63\3\2\63;\3\2")
        buf.write("\62;\3\2\629\4\2ZZzz\5\2\62;CHch\4\2GGgg\4\2--//\4\2R")
        buf.write("Rrr\3\2bb\6\2\f\f\17\17$$^^\13\2$$))^^cdhhppttvvxx\6\2")
        buf.write("\f\f\17\17))^^\5\2C\\aac|\6\2\62;C\\aac|\4\2\f\f\17\17")
        buf.write("\5\2\13\f\17\17\"\"\n\2$$))^^ddhhppttvv\5\2\f\f\17\17")
        buf.write("$$\4\3\f\f\17\17\2\u0334\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2")
        buf.write("\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5")
        buf.write("\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cb\3\2\2")
        buf.write("\2\2\u00cf\3\2\2\2\3\u00d1\3\2\2\2\5\u00d9\3\2\2\2\7\u00db")
        buf.write("\3\2\2\2\t\u00e2\3\2\2\2\13\u00e4\3\2\2\2\r\u00e6\3\2")
        buf.write("\2\2\17\u00ea\3\2\2\2\21\u00ec\3\2\2\2\23\u00ee\3\2\2")
        buf.write("\2\25\u00f1\3\2\2\2\27\u00f6\3\2\2\2\31\u00fb\3\2\2\2")
        buf.write("\33\u00fd\3\2\2\2\35\u0101\3\2\2\2\37\u0105\3\2\2\2!\u010a")
        buf.write("\3\2\2\2#\u0110\3\2\2\2%\u0116\3\2\2\2\'\u011c\3\2\2\2")
        buf.write(")\u0121\3\2\2\2+\u0127\3\2\2\2-\u012e\3\2\2\2/\u0135\3")
        buf.write("\2\2\2\61\u013c\3\2\2\2\63\u0144\3\2\2\2\65\u014c\3\2")
        buf.write("\2\2\67\u0152\3\2\2\29\u0159\3\2\2\2;\u015e\3\2\2\2=\u0163")
        buf.write("\3\2\2\2?\u0168\3\2\2\2A\u016a\3\2\2\2C\u016c\3\2\2\2")
        buf.write("E\u0173\3\2\2\2G\u0175\3\2\2\2I\u0177\3\2\2\2K\u0181\3")
        buf.write("\2\2\2M\u0185\3\2\2\2O\u0188\3\2\2\2Q\u018b\3\2\2\2S\u018e")
        buf.write("\3\2\2\2U\u0191\3\2\2\2W\u0194\3\2\2\2Y\u0197\3\2\2\2")
        buf.write("[\u019a\3\2\2\2]\u019d\3\2\2\2_\u01a2\3\2\2\2a\u01a6\3")
        buf.write("\2\2\2c\u01ac\3\2\2\2e\u01b3\3\2\2\2g\u01b8\3\2\2\2i\u01c0")
        buf.write("\3\2\2\2k\u01c2\3\2\2\2m\u01c5\3\2\2\2o\u01cb\3\2\2\2")
        buf.write("q\u01d2\3\2\2\2s\u01d8\3\2\2\2u\u01e1\3\2\2\2w\u01e3\3")
        buf.write("\2\2\2y\u01e5\3\2\2\2{\u01e7\3\2\2\2}\u01e9\3\2\2\2\177")
        buf.write("\u01eb\3\2\2\2\u0081\u01ed\3\2\2\2\u0083\u01f0\3\2\2\2")
        buf.write("\u0085\u01f2\3\2\2\2\u0087\u01f4\3\2\2\2\u0089\u01f6\3")
        buf.write("\2\2\2\u008b\u01f9\3\2\2\2\u008d\u01fc\3\2\2\2\u008f\u01ff")
        buf.write("\3\2\2\2\u0091\u0202\3\2\2\2\u0093\u0205\3\2\2\2\u0095")
        buf.write("\u0207\3\2\2\2\u0097\u020a\3\2\2\2\u0099\u020c\3\2\2\2")
        buf.write("\u009b\u020f\3\2\2\2\u009d\u0212\3\2\2\2\u009f\u0215\3")
        buf.write("\2\2\2\u00a1\u021a\3\2\2\2\u00a3\u021c\3\2\2\2\u00a5\u022b")
        buf.write("\3\2\2\2\u00a7\u022d\3\2\2\2\u00a9\u0233\3\2\2\2\u00ab")
        buf.write("\u023c\3\2\2\2\u00ad\u025c\3\2\2\2\u00af\u027e\3\2\2\2")
        buf.write("\u00b1\u0280\3\2\2\2\u00b3\u0289\3\2\2\2\u00b5\u029b\3")
        buf.write("\2\2\2\u00b7\u029f\3\2\2\2\u00b9\u02a1\3\2\2\2\u00bb\u02aa")
        buf.write("\3\2\2\2\u00bd\u02b4\3\2\2\2\u00bf\u02b7\3\2\2\2\u00c1")
        buf.write("\u02be\3\2\2\2\u00c3\u02c5\3\2\2\2\u00c5\u02d0\3\2\2\2")
        buf.write("\u00c7\u02e0\3\2\2\2\u00c9\u02e6\3\2\2\2\u00cb\u02e9\3")
        buf.write("\2\2\2\u00cd\u02fc\3\2\2\2\u00cf\u02ff\3\2\2\2\u00d1\u00d2")
        buf.write("\7r\2\2\u00d2\u00d3\7c\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5")
        buf.write("\7m\2\2\u00d5\u00d6\7c\2\2\u00d6\u00d7\7i\2\2\u00d7\u00d8")
        buf.write("\7g\2\2\u00d8\4\3\2\2\2\u00d9\u00da\7=\2\2\u00da\6\3\2")
        buf.write("\2\2\u00db\u00dc\7k\2\2\u00dc\u00dd\7o\2\2\u00dd\u00de")
        buf.write("\7r\2\2\u00de\u00df\7q\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1")
        buf.write("\7v\2\2\u00e1\b\3\2\2\2\u00e2\u00e3\7*\2\2\u00e3\n\3\2")
        buf.write("\2\2\u00e4\u00e5\7+\2\2\u00e5\f\3\2\2\2\u00e6\u00e7\7")
        buf.write("x\2\2\u00e7\u00e8\7c\2\2\u00e8\u00e9\7t\2\2\u00e9\16\3")
        buf.write("\2\2\2\u00ea\u00eb\7?\2\2\u00eb\20\3\2\2\2\u00ec\u00ed")
        buf.write("\7.\2\2\u00ed\22\3\2\2\2\u00ee\u00ef\7<\2\2\u00ef\u00f0")
        buf.write("\7?\2\2\u00f0\24\3\2\2\2\u00f1\u00f2\7v\2\2\u00f2\u00f3")
        buf.write("\7{\2\2\u00f3\u00f4\7r\2\2\u00f4\u00f5\7g\2\2\u00f5\26")
        buf.write("\3\2\2\2\u00f6\u00f7\7h\2\2\u00f7\u00f8\7w\2\2\u00f8\u00f9")
        buf.write("\7p\2\2\u00f9\u00fa\7e\2\2\u00fa\30\3\2\2\2\u00fb\u00fc")
        buf.write("\7,\2\2\u00fc\32\3\2\2\2\u00fd\u00fe\7\60\2\2\u00fe\u00ff")
        buf.write("\7\60\2\2\u00ff\u0100\7\60\2\2\u0100\34\3\2\2\2\u0101")
        buf.write("\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104\7v\2\2\u0104")
        buf.write("\36\3\2\2\2\u0105\u0106\7k\2\2\u0106\u0107\7p\2\2\u0107")
        buf.write("\u0108\7v\2\2\u0108\u0109\7:\2\2\u0109 \3\2\2\2\u010a")
        buf.write("\u010b\7k\2\2\u010b\u010c\7p\2\2\u010c\u010d\7v\2\2\u010d")
        buf.write("\u010e\7\63\2\2\u010e\u010f\78\2\2\u010f\"\3\2\2\2\u0110")
        buf.write("\u0111\7k\2\2\u0111\u0112\7p\2\2\u0112\u0113\7v\2\2\u0113")
        buf.write("\u0114\7\65\2\2\u0114\u0115\7\64\2\2\u0115$\3\2\2\2\u0116")
        buf.write("\u0117\7k\2\2\u0117\u0118\7p\2\2\u0118\u0119\7v\2\2\u0119")
        buf.write("\u011a\78\2\2\u011a\u011b\7\66\2\2\u011b&\3\2\2\2\u011c")
        buf.write("\u011d\7w\2\2\u011d\u011e\7k\2\2\u011e\u011f\7p\2\2\u011f")
        buf.write("\u0120\7v\2\2\u0120(\3\2\2\2\u0121\u0122\7w\2\2\u0122")
        buf.write("\u0123\7k\2\2\u0123\u0124\7p\2\2\u0124\u0125\7v\2\2\u0125")
        buf.write("\u0126\7:\2\2\u0126*\3\2\2\2\u0127\u0128\7w\2\2\u0128")
        buf.write("\u0129\7k\2\2\u0129\u012a\7p\2\2\u012a\u012b\7v\2\2\u012b")
        buf.write("\u012c\7\63\2\2\u012c\u012d\78\2\2\u012d,\3\2\2\2\u012e")
        buf.write("\u012f\7w\2\2\u012f\u0130\7k\2\2\u0130\u0131\7p\2\2\u0131")
        buf.write("\u0132\7v\2\2\u0132\u0133\7\65\2\2\u0133\u0134\7\64\2")
        buf.write("\2\u0134.\3\2\2\2\u0135\u0136\7w\2\2\u0136\u0137\7k\2")
        buf.write("\2\u0137\u0138\7p\2\2\u0138\u0139\7v\2\2\u0139\u013a\7")
        buf.write("8\2\2\u013a\u013b\7\66\2\2\u013b\60\3\2\2\2\u013c\u013d")
        buf.write("\7h\2\2\u013d\u013e\7n\2\2\u013e\u013f\7q\2\2\u013f\u0140")
        buf.write("\7c\2\2\u0140\u0141\7v\2\2\u0141\u0142\7\65\2\2\u0142")
        buf.write("\u0143\7\64\2\2\u0143\62\3\2\2\2\u0144\u0145\7h\2\2\u0145")
        buf.write("\u0146\7n\2\2\u0146\u0147\7q\2\2\u0147\u0148\7c\2\2\u0148")
        buf.write("\u0149\7v\2\2\u0149\u014a\78\2\2\u014a\u014b\7\66\2\2")
        buf.write("\u014b\64\3\2\2\2\u014c\u014d\7h\2\2\u014d\u014e\7n\2")
        buf.write("\2\u014e\u014f\7q\2\2\u014f\u0150\7c\2\2\u0150\u0151\7")
        buf.write("v\2\2\u0151\66\3\2\2\2\u0152\u0153\7u\2\2\u0153\u0154")
        buf.write("\7v\2\2\u0154\u0155\7t\2\2\u0155\u0156\7k\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157\u0158\7i\2\2\u01588\3\2\2\2\u0159\u015a")
        buf.write("\7d\2\2\u015a\u015b\7q\2\2\u015b\u015c\7q\2\2\u015c\u015d")
        buf.write("\7n\2\2\u015d:\3\2\2\2\u015e\u015f\7d\2\2\u015f\u0160")
        buf.write("\7{\2\2\u0160\u0161\7v\2\2\u0161\u0162\7g\2\2\u0162<\3")
        buf.write("\2\2\2\u0163\u0164\7t\2\2\u0164\u0165\7w\2\2\u0165\u0166")
        buf.write("\7p\2\2\u0166\u0167\7g\2\2\u0167>\3\2\2\2\u0168\u0169")
        buf.write("\7]\2\2\u0169@\3\2\2\2\u016a\u016b\7_\2\2\u016bB\3\2\2")
        buf.write("\2\u016c\u016d\7u\2\2\u016d\u016e\7v\2\2\u016e\u016f\7")
        buf.write("t\2\2\u016f\u0170\7w\2\2\u0170\u0171\7e\2\2\u0171\u0172")
        buf.write("\7v\2\2\u0172D\3\2\2\2\u0173\u0174\7}\2\2\u0174F\3\2\2")
        buf.write("\2\u0175\u0176\7\177\2\2\u0176H\3\2\2\2\u0177\u0178\7")
        buf.write("k\2\2\u0178\u0179\7p\2\2\u0179\u017a\7v\2\2\u017a\u017b")
        buf.write("\7g\2\2\u017b\u017c\7t\2\2\u017c\u017d\7h\2\2\u017d\u017e")
        buf.write("\7c\2\2\u017e\u017f\7e\2\2\u017f\u0180\7g\2\2\u0180J\3")
        buf.write("\2\2\2\u0181\u0182\7o\2\2\u0182\u0183\7c\2\2\u0183\u0184")
        buf.write("\7r\2\2\u0184L\3\2\2\2\u0185\u0186\7-\2\2\u0186\u0187")
        buf.write("\7?\2\2\u0187N\3\2\2\2\u0188\u0189\7/\2\2\u0189\u018a")
        buf.write("\7?\2\2\u018aP\3\2\2\2\u018b\u018c\7,\2\2\u018c\u018d")
        buf.write("\7?\2\2\u018dR\3\2\2\2\u018e\u018f\7\61\2\2\u018f\u0190")
        buf.write("\7?\2\2\u0190T\3\2\2\2\u0191\u0192\7\'\2\2\u0192\u0193")
        buf.write("\7?\2\2\u0193V\3\2\2\2\u0194\u0195\7-\2\2\u0195\u0196")
        buf.write("\7-\2\2\u0196X\3\2\2\2\u0197\u0198\7/\2\2\u0198\u0199")
        buf.write("\7/\2\2\u0199Z\3\2\2\2\u019a\u019b\7k\2\2\u019b\u019c")
        buf.write("\7h\2\2\u019c\\\3\2\2\2\u019d\u019e\7g\2\2\u019e\u019f")
        buf.write("\7n\2\2\u019f\u01a0\7u\2\2\u01a0\u01a1\7g\2\2\u01a1^\3")
        buf.write("\2\2\2\u01a2\u01a3\7h\2\2\u01a3\u01a4\7q\2\2\u01a4\u01a5")
        buf.write("\7t\2\2\u01a5`\3\2\2\2\u01a6\u01a7\7t\2\2\u01a7\u01a8")
        buf.write("\7c\2\2\u01a8\u01a9\7p\2\2\u01a9\u01aa\7i\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01abb\3\2\2\2\u01ac\u01ad\7u\2\2\u01ad\u01ae")
        buf.write("\7y\2\2\u01ae\u01af\7k\2\2\u01af\u01b0\7v\2\2\u01b0\u01b1")
        buf.write("\7e\2\2\u01b1\u01b2\7j\2\2\u01b2d\3\2\2\2\u01b3\u01b4")
        buf.write("\7e\2\2\u01b4\u01b5\7c\2\2\u01b5\u01b6\7u\2\2\u01b6\u01b7")
        buf.write("\7g\2\2\u01b7f\3\2\2\2\u01b8\u01b9\7f\2\2\u01b9\u01ba")
        buf.write("\7g\2\2\u01ba\u01bb\7h\2\2\u01bb\u01bc\7c\2\2\u01bc\u01bd")
        buf.write("\7w\2\2\u01bd\u01be\7n\2\2\u01be\u01bf\7v\2\2\u01bfh\3")
        buf.write("\2\2\2\u01c0\u01c1\7<\2\2\u01c1j\3\2\2\2\u01c2\u01c3\7")
        buf.write("i\2\2\u01c3\u01c4\7q\2\2\u01c4l\3\2\2\2\u01c5\u01c6\7")
        buf.write("f\2\2\u01c6\u01c7\7g\2\2\u01c7\u01c8\7h\2\2\u01c8\u01c9")
        buf.write("\7g\2\2\u01c9\u01ca\7t\2\2\u01can\3\2\2\2\u01cb\u01cc")
        buf.write("\7t\2\2\u01cc\u01cd\7g\2\2\u01cd\u01ce\7v\2\2\u01ce\u01cf")
        buf.write("\7w\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7p\2\2\u01d1p\3")
        buf.write("\2\2\2\u01d2\u01d3\7d\2\2\u01d3\u01d4\7t\2\2\u01d4\u01d5")
        buf.write("\7g\2\2\u01d5\u01d6\7c\2\2\u01d6\u01d7\7m\2\2\u01d7r\3")
        buf.write("\2\2\2\u01d8\u01d9\7e\2\2\u01d9\u01da\7q\2\2\u01da\u01db")
        buf.write("\7p\2\2\u01db\u01dc\7v\2\2\u01dc\u01dd\7k\2\2\u01dd\u01de")
        buf.write("\7p\2\2\u01de\u01df\7w\2\2\u01df\u01e0\7g\2\2\u01e0t\3")
        buf.write("\2\2\2\u01e1\u01e2\7A\2\2\u01e2v\3\2\2\2\u01e3\u01e4\7")
        buf.write("-\2\2\u01e4x\3\2\2\2\u01e5\u01e6\7/\2\2\u01e6z\3\2\2\2")
        buf.write("\u01e7\u01e8\7#\2\2\u01e8|\3\2\2\2\u01e9\u01ea\7`\2\2")
        buf.write("\u01ea~\3\2\2\2\u01eb\u01ec\7(\2\2\u01ec\u0080\3\2\2\2")
        buf.write("\u01ed\u01ee\7>\2\2\u01ee\u01ef\7/\2\2\u01ef\u0082\3\2")
        buf.write("\2\2\u01f0\u01f1\7\61\2\2\u01f1\u0084\3\2\2\2\u01f2\u01f3")
        buf.write("\7\'\2\2\u01f3\u0086\3\2\2\2\u01f4\u01f5\7~\2\2\u01f5")
        buf.write("\u0088\3\2\2\2\u01f6\u01f7\7>\2\2\u01f7\u01f8\7>\2\2\u01f8")
        buf.write("\u008a\3\2\2\2\u01f9\u01fa\7@\2\2\u01fa\u01fb\7@\2\2\u01fb")
        buf.write("\u008c\3\2\2\2\u01fc\u01fd\7(\2\2\u01fd\u01fe\7`\2\2\u01fe")
        buf.write("\u008e\3\2\2\2\u01ff\u0200\7?\2\2\u0200\u0201\7?\2\2\u0201")
        buf.write("\u0090\3\2\2\2\u0202\u0203\7#\2\2\u0203\u0204\7?\2\2\u0204")
        buf.write("\u0092\3\2\2\2\u0205\u0206\7>\2\2\u0206\u0094\3\2\2\2")
        buf.write("\u0207\u0208\7>\2\2\u0208\u0209\7?\2\2\u0209\u0096\3\2")
        buf.write("\2\2\u020a\u020b\7@\2\2\u020b\u0098\3\2\2\2\u020c\u020d")
        buf.write("\7@\2\2\u020d\u020e\7?\2\2\u020e\u009a\3\2\2\2\u020f\u0210")
        buf.write("\7(\2\2\u0210\u0211\7(\2\2\u0211\u009c\3\2\2\2\u0212\u0213")
        buf.write("\7~\2\2\u0213\u0214\7~\2\2\u0214\u009e\3\2\2\2\u0215\u0216")
        buf.write("\7\60\2\2\u0216\u00a0\3\2\2\2\u0217\u021b\5\u00a5S\2\u0218")
        buf.write("\u021b\5\u00a7T\2\u0219\u021b\5\u00a9U\2\u021a\u0217\3")
        buf.write("\2\2\2\u021a\u0218\3\2\2\2\u021a\u0219\3\2\2\2\u021b\u00a2")
        buf.write("\3\2\2\2\u021c\u021d\7\62\2\2\u021d\u021f\t\2\2\2\u021e")
        buf.write("\u0220\t\3\2\2\u021f\u021e\3\2\2\2\u0220\u0221\3\2\2\2")
        buf.write("\u0221\u021f\3\2\2\2\u0221\u0222\3\2\2\2\u0222\u00a4\3")
        buf.write("\2\2\2\u0223\u0227\t\4\2\2\u0224\u0226\t\5\2\2\u0225\u0224")
        buf.write("\3\2\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u022c\3\2\2\2\u0229\u0227\3\2\2\2")
        buf.write("\u022a\u022c\7\62\2\2\u022b\u0223\3\2\2\2\u022b\u022a")
        buf.write("\3\2\2\2\u022c\u00a6\3\2\2\2\u022d\u022f\7\62\2\2\u022e")
        buf.write("\u0230\t\6\2\2\u022f\u022e\3\2\2\2\u0230\u0231\3\2\2\2")
        buf.write("\u0231\u022f\3\2\2\2\u0231\u0232\3\2\2\2\u0232\u00a8\3")
        buf.write("\2\2\2\u0233\u0234\7\62\2\2\u0234\u0236\t\7\2\2\u0235")
        buf.write("\u0237\t\b\2\2\u0236\u0235\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0238\u0236\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u00aa\3")
        buf.write("\2\2\2\u023a\u023d\5\u00adW\2\u023b\u023d\5\u00afX\2\u023c")
        buf.write("\u023a\3\2\2\2\u023c\u023b\3\2\2\2\u023d\u00ac\3\2\2\2")
        buf.write("\u023e\u0240\t\5\2\2\u023f\u023e\3\2\2\2\u0240\u0241\3")
        buf.write("\2\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0243")
        buf.write("\3\2\2\2\u0243\u0247\7\60\2\2\u0244\u0246\t\5\2\2\u0245")
        buf.write("\u0244\3\2\2\2\u0246\u0249\3\2\2\2\u0247\u0245\3\2\2\2")
        buf.write("\u0247\u0248\3\2\2\2\u0248\u024b\3\2\2\2\u0249\u0247\3")
        buf.write("\2\2\2\u024a\u024c\5\u00b1Y\2\u024b\u024a\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024c\u025d\3\2\2\2\u024d\u024f\7\60\2")
        buf.write("\2\u024e\u0250\t\5\2\2\u024f\u024e\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\u024f\3\2\2\2\u0251\u0252\3\2\2\2\u0252")
        buf.write("\u0254\3\2\2\2\u0253\u0255\5\u00b1Y\2\u0254\u0253\3\2")
        buf.write("\2\2\u0254\u0255\3\2\2\2\u0255\u025d\3\2\2\2\u0256\u0258")
        buf.write("\t\5\2\2\u0257\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write("\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025a\u025b\3\2\2\2")
        buf.write("\u025b\u025d\5\u00b1Y\2\u025c\u023f\3\2\2\2\u025c\u024d")
        buf.write("\3\2\2\2\u025c\u0257\3\2\2\2\u025d\u00ae\3\2\2\2\u025e")
        buf.write("\u025f\7\62\2\2\u025f\u0261\t\7\2\2\u0260\u0262\t\b\2")
        buf.write("\2\u0261\u0260\3\2\2\2\u0262\u0263\3\2\2\2\u0263\u0261")
        buf.write("\3\2\2\2\u0263\u0264\3\2\2\2\u0264\u0265\3\2\2\2\u0265")
        buf.write("\u0269\7\60\2\2\u0266\u0268\t\b\2\2\u0267\u0266\3\2\2")
        buf.write("\2\u0268\u026b\3\2\2\2\u0269\u0267\3\2\2\2\u0269\u026a")
        buf.write("\3\2\2\2\u026a\u026c\3\2\2\2\u026b\u0269\3\2\2\2\u026c")
        buf.write("\u027f\5\u00b3Z\2\u026d\u026e\7\62\2\2\u026e\u026f\t\7")
        buf.write("\2\2\u026f\u0271\7\60\2\2\u0270\u0272\t\b\2\2\u0271\u0270")
        buf.write("\3\2\2\2\u0272\u0273\3\2\2\2\u0273\u0271\3\2\2\2\u0273")
        buf.write("\u0274\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u027f\5\u00b3")
        buf.write("Z\2\u0276\u0277\7\62\2\2\u0277\u0279\t\7\2\2\u0278\u027a")
        buf.write("\t\b\2\2\u0279\u0278\3\2\2\2\u027a\u027b\3\2\2\2\u027b")
        buf.write("\u0279\3\2\2\2\u027b\u027c\3\2\2\2\u027c\u027d\3\2\2\2")
        buf.write("\u027d\u027f\5\u00b3Z\2\u027e\u025e\3\2\2\2\u027e\u026d")
        buf.write("\3\2\2\2\u027e\u0276\3\2\2\2\u027f\u00b0\3\2\2\2\u0280")
        buf.write("\u0282\t\t\2\2\u0281\u0283\t\n\2\2\u0282\u0281\3\2\2\2")
        buf.write("\u0282\u0283\3\2\2\2\u0283\u0285\3\2\2\2\u0284\u0286\t")
        buf.write("\5\2\2\u0285\u0284\3\2\2\2\u0286\u0287\3\2\2\2\u0287\u0285")
        buf.write("\3\2\2\2\u0287\u0288\3\2\2\2\u0288\u00b2\3\2\2\2\u0289")
        buf.write("\u028b\t\13\2\2\u028a\u028c\t\n\2\2\u028b\u028a\3\2\2")
        buf.write("\2\u028b\u028c\3\2\2\2\u028c\u028e\3\2\2\2\u028d\u028f")
        buf.write("\t\5\2\2\u028e\u028d\3\2\2\2\u028f\u0290\3\2\2\2\u0290")
        buf.write("\u028e\3\2\2\2\u0290\u0291\3\2\2\2\u0291\u00b4\3\2\2\2")
        buf.write("\u0292\u0293\7v\2\2\u0293\u0294\7t\2\2\u0294\u0295\7w")
        buf.write("\2\2\u0295\u029c\7g\2\2\u0296\u0297\7h\2\2\u0297\u0298")
        buf.write("\7c\2\2\u0298\u0299\7n\2\2\u0299\u029a\7u\2\2\u029a\u029c")
        buf.write("\7g\2\2\u029b\u0292\3\2\2\2\u029b\u0296\3\2\2\2\u029c")
        buf.write("\u00b6\3\2\2\2\u029d\u02a0\5\u00b9]\2\u029e\u02a0\5\u00bb")
        buf.write("^\2\u029f\u029d\3\2\2\2\u029f\u029e\3\2\2\2\u02a0\u00b8")
        buf.write("\3\2\2\2\u02a1\u02a5\7b\2\2\u02a2\u02a4\n\f\2\2\u02a3")
        buf.write("\u02a2\3\2\2\2\u02a4\u02a7\3\2\2\2\u02a5\u02a3\3\2\2\2")
        buf.write("\u02a5\u02a6\3\2\2\2\u02a6\u02a8\3\2\2\2\u02a7\u02a5\3")
        buf.write("\2\2\2\u02a8\u02a9\7b\2\2\u02a9\u00ba\3\2\2\2\u02aa\u02af")
        buf.write("\7$\2\2\u02ab\u02ae\n\r\2\2\u02ac\u02ae\5\u00bd_\2\u02ad")
        buf.write("\u02ab\3\2\2\2\u02ad\u02ac\3\2\2\2\u02ae\u02b1\3\2\2\2")
        buf.write("\u02af\u02ad\3\2\2\2\u02af\u02b0\3\2\2\2\u02b0\u02b2\3")
        buf.write("\2\2\2\u02b1\u02af\3\2\2\2\u02b2\u02b3\7$\2\2\u02b3\u00bc")
        buf.write("\3\2\2\2\u02b4\u02b5\7^\2\2\u02b5\u02b6\t\16\2\2\u02b6")
        buf.write("\u00be\3\2\2\2\u02b7\u02ba\7)\2\2\u02b8\u02bb\n\17\2\2")
        buf.write("\u02b9\u02bb\5\u00bd_\2\u02ba\u02b8\3\2\2\2\u02ba\u02b9")
        buf.write("\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02bd\7)\2\2\u02bd")
        buf.write("\u00c0\3\2\2\2\u02be\u02c2\t\20\2\2\u02bf\u02c1\t\21\2")
        buf.write("\2\u02c0\u02bf\3\2\2\2\u02c1\u02c4\3\2\2\2\u02c2\u02c0")
        buf.write("\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u00c2\3\2\2\2\u02c4")
        buf.write("\u02c2\3\2\2\2\u02c5\u02c6\7\61\2\2\u02c6\u02c7\7\61\2")
        buf.write("\2\u02c7\u02cb\3\2\2\2\u02c8\u02ca\n\22\2\2\u02c9\u02c8")
        buf.write("\3\2\2\2\u02ca\u02cd\3\2\2\2\u02cb\u02c9\3\2\2\2\u02cb")
        buf.write("\u02cc\3\2\2\2\u02cc\u02ce\3\2\2\2\u02cd\u02cb\3\2\2\2")
        buf.write("\u02ce\u02cf\bb\2\2\u02cf\u00c4\3\2\2\2\u02d0\u02d1\7")
        buf.write("\61\2\2\u02d1\u02d2\7,\2\2\u02d2\u02d7\3\2\2\2\u02d3\u02d6")
        buf.write("\5\u00c5c\2\u02d4\u02d6\13\2\2\2\u02d5\u02d3\3\2\2\2\u02d5")
        buf.write("\u02d4\3\2\2\2\u02d6\u02d9\3\2\2\2\u02d7\u02d8\3\2\2\2")
        buf.write("\u02d7\u02d5\3\2\2\2\u02d8\u02da\3\2\2\2\u02d9\u02d7\3")
        buf.write("\2\2\2\u02da\u02db\7,\2\2\u02db\u02dc\7\61\2\2\u02dc\u02dd")
        buf.write("\3\2\2\2\u02dd\u02de\bc\2\2\u02de\u00c6\3\2\2\2\u02df")
        buf.write("\u02e1\t\23\2\2\u02e0\u02df\3\2\2\2\u02e1\u02e2\3\2\2")
        buf.write("\2\u02e2\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2\u02e3\u02e4")
        buf.write("\3\2\2\2\u02e4\u02e5\bd\2\2\u02e5\u00c8\3\2\2\2\u02e6")
        buf.write("\u02e7\13\2\2\2\u02e7\u02e8\be\3\2\u02e8\u00ca\3\2\2\2")
        buf.write("\u02e9\u02ef\7$\2\2\u02ea\u02ee\n\r\2\2\u02eb\u02ec\7")
        buf.write("^\2\2\u02ec\u02ee\t\24\2\2\u02ed\u02ea\3\2\2\2\u02ed\u02eb")
        buf.write("\3\2\2\2\u02ee\u02f1\3\2\2\2\u02ef\u02ed\3\2\2\2\u02ef")
        buf.write("\u02f0\3\2\2\2\u02f0\u02f2\3\2\2\2\u02f1\u02ef\3\2\2\2")
        buf.write("\u02f2\u02f3\7^\2\2\u02f3\u02f7\n\24\2\2\u02f4\u02f6\n")
        buf.write("\25\2\2\u02f5\u02f4\3\2\2\2\u02f6\u02f9\3\2\2\2\u02f7")
        buf.write("\u02f5\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\u02fa\3\2\2\2")
        buf.write("\u02f9\u02f7\3\2\2\2\u02fa\u02fb\bf\4\2\u02fb\u00cc\3")
        buf.write("\2\2\2\u02fc\u02fd\7^\2\2\u02fd\u02fe\t\24\2\2\u02fe\u00ce")
        buf.write("\3\2\2\2\u02ff\u0304\7$\2\2\u0300\u0303\5\u00cdg\2\u0301")
        buf.write("\u0303\n\r\2\2\u0302\u0300\3\2\2\2\u0302\u0301\3\2\2\2")
        buf.write("\u0303\u0306\3\2\2\2\u0304\u0302\3\2\2\2\u0304\u0305\3")
        buf.write("\2\2\2\u0305\u0308\3\2\2\2\u0306\u0304\3\2\2\2\u0307\u0309")
        buf.write("\t\26\2\2\u0308\u0307\3\2\2\2\u0309\u030a\3\2\2\2\u030a")
        buf.write("\u030b\bh\5\2\u030b\u00d0\3\2\2\2+\2\u021a\u0221\u0227")
        buf.write("\u022b\u0231\u0238\u023c\u0241\u0247\u024b\u0251\u0254")
        buf.write("\u0259\u025c\u0263\u0269\u0273\u027b\u027e\u0282\u0287")
        buf.write("\u028b\u0290\u029b\u029f\u02a5\u02ad\u02af\u02ba\u02c2")
        buf.write("\u02cb\u02d5\u02d7\u02e2\u02ed\u02ef\u02f7\u0302\u0304")
        buf.write("\u0308\6\b\2\2\3e\2\3f\3\3h\4")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    T__72 = 73
    T__73 = 74
    T__74 = 75
    T__75 = 76
    T__76 = 77
    T__77 = 78
    T__78 = 79
    INTLIT = 80
    BINARY_LIT = 81
    DECIMAL_LIT = 82
    OCTAL_LIT = 83
    HEX_LIT = 84
    FLOATLIT = 85
    DECIMAL_FLOAT = 86
    HEX_FLOAT = 87
    EXPONENT = 88
    HEX_EXPONENT = 89
    BOOLLIT = 90
    STRINGLIT = 91
    RAW_STRING = 92
    INTERPRETED_STRING = 93
    ESCAPED_CHAR = 94
    RUNELIT = 95
    ID = 96
    COMMENT = 97
    BLOCK_COMMENT = 98
    WS = 99
    ERROR_CHAR = 100
    ILLEGAL_ESCAPE = 101
    UNCLOSE_STRING = 102

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'package'", "';'", "'import'", "'('", "')'", "'var'", "'='", 
            "','", "':='", "'type'", "'func'", "'*'", "'...'", "'int'", 
            "'int8'", "'int16'", "'int32'", "'int64'", "'uint'", "'uint8'", 
            "'uint16'", "'uint32'", "'uint64'", "'float32'", "'float64'", 
            "'float'", "'string'", "'bool'", "'byte'", "'rune'", "'['", 
            "']'", "'struct'", "'{'", "'}'", "'interface'", "'map'", "'+='", 
            "'-='", "'*='", "'/='", "'%='", "'++'", "'--'", "'if'", "'else'", 
            "'for'", "'range'", "'switch'", "'case'", "'default'", "':'", 
            "'go'", "'defer'", "'return'", "'break'", "'continue'", "'?'", 
            "'+'", "'-'", "'!'", "'^'", "'&'", "'<-'", "'/'", "'%'", "'|'", 
            "'<<'", "'>>'", "'&^'", "'=='", "'!='", "'<'", "'<='", "'>'", 
            "'>='", "'&&'", "'||'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "BINARY_LIT", "DECIMAL_LIT", "OCTAL_LIT", "HEX_LIT", 
            "FLOATLIT", "DECIMAL_FLOAT", "HEX_FLOAT", "EXPONENT", "HEX_EXPONENT", 
            "BOOLLIT", "STRINGLIT", "RAW_STRING", "INTERPRETED_STRING", 
            "ESCAPED_CHAR", "RUNELIT", "ID", "COMMENT", "BLOCK_COMMENT", 
            "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "T__72", "T__73", 
                  "T__74", "T__75", "T__76", "T__77", "T__78", "INTLIT", 
                  "BINARY_LIT", "DECIMAL_LIT", "OCTAL_LIT", "HEX_LIT", "FLOATLIT", 
                  "DECIMAL_FLOAT", "HEX_FLOAT", "EXPONENT", "HEX_EXPONENT", 
                  "BOOLLIT", "STRINGLIT", "RAW_STRING", "INTERPRETED_STRING", 
                  "ESCAPED_CHAR", "RUNELIT", "ID", "COMMENT", "BLOCK_COMMENT", 
                  "WS", "ERROR_CHAR", "ILLEGAL_ESCAPE", "ESC_SEQ", "UNCLOSE_STRING" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:
            result = super().emit()
            raise UncloseString(result.text[0:])
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit()
            raise IllegalEscape(result.text[0:])
        elif tk == self.ERROR_CHAR:
            result = super().emit()
            raise ErrorToken(result.text)
        else:
            return super().emit()


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[99] = self.ERROR_CHAR_action 
            actions[100] = self.ILLEGAL_ESCAPE_action 
            actions[102] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                    current = self.text
                    if not hasattr(self, '_errors'):
                        self._errors = []
                    self._errors.append(ErrorToken(current))
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                    result = self.text
                    raise IllegalEscape(result[0:])
                
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                    text = self.text
                    if text.endswith('\n') or text.endswith('\r\n'):
                        text = text[:-1]
                    raise UncloseString(text)
                
     


