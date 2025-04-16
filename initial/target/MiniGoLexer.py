# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\28")
        buf.write("\u01e4\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\3\2\5\2\u0082\n\2")
        buf.write("\3\3\3\3\7\3\u0086\n\3\f\3\16\3\u0089\13\3\3\3\5\3\u008c")
        buf.write("\n\3\3\4\3\4\6\4\u0090\n\4\r\4\16\4\u0091\3\5\3\5\3\5")
        buf.write("\6\5\u0097\n\5\r\5\16\5\u0098\3\6\3\6\3\6\6\6\u009e\n")
        buf.write("\6\r\6\16\6\u009f\3\7\3\7\5\7\u00a4\n\7\3\b\6\b\u00a7")
        buf.write("\n\b\r\b\16\b\u00a8\3\b\3\b\7\b\u00ad\n\b\f\b\16\b\u00b0")
        buf.write("\13\b\3\b\3\b\5\b\u00b4\n\b\3\b\6\b\u00b7\n\b\r\b\16\b")
        buf.write("\u00b8\5\b\u00bb\n\b\3\b\3\b\6\b\u00bf\n\b\r\b\16\b\u00c0")
        buf.write("\3\b\3\b\5\b\u00c5\n\b\3\b\6\b\u00c8\n\b\r\b\16\b\u00c9")
        buf.write("\5\b\u00cc\n\b\3\b\6\b\u00cf\n\b\r\b\16\b\u00d0\3\b\3")
        buf.write("\b\5\b\u00d5\n\b\3\b\6\b\u00d8\n\b\r\b\16\b\u00d9\5\b")
        buf.write("\u00dc\n\b\3\t\3\t\3\t\6\t\u00e1\n\t\r\t\16\t\u00e2\3")
        buf.write("\t\5\t\u00e6\n\t\3\t\7\t\u00e9\n\t\f\t\16\t\u00ec\13\t")
        buf.write("\3\t\3\t\6\t\u00f0\n\t\r\t\16\t\u00f1\5\t\u00f4\n\t\3")
        buf.write("\t\3\t\5\t\u00f8\n\t\3\t\6\t\u00fb\n\t\r\t\16\t\u00fc")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u0108\n\n\3\13")
        buf.write("\3\13\3\13\7\13\u010d\n\13\f\13\16\13\u0110\13\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\5\r\u011a\n\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20")
        buf.write("\3\20\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\26")
        buf.write("\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32")
        buf.write("\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("\"\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3")
        buf.write("*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3\61")
        buf.write("\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67")
        buf.write("\3\67\38\38\78\u01a7\n8\f8\168\u01aa\138\39\69\u01ad\n")
        buf.write("9\r9\169\u01ae\39\39\3:\3:\3:\3:\7:\u01b7\n:\f:\16:\u01ba")
        buf.write("\13:\3:\3:\3;\3;\3;\3;\7;\u01c2\n;\f;\16;\u01c5\13;\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\7<\u01cf\n<\f<\16<\u01d2\13<\3")
        buf.write("<\5<\u01d5\n<\3=\3=\3=\7=\u01da\n=\f=\16=\u01dd\13=\3")
        buf.write("=\3=\3=\3>\3>\3>\3\u01c3\2?\3\3\5\2\7\2\t\2\13\2\r\4\17")
        buf.write("\2\21\2\23\5\25\6\27\2\31\7\33\b\35\t\37\n!\13#\f%\r\'")
        buf.write("\16)\17+\20-\21/\22\61\23\63\24\65\25\67\269\27;\30=\31")
        buf.write("?\32A\33C\34E\35G\36I\37K M!O\"Q#S$U%W&Y\'[(])_*a+c,e")
        buf.write("-g.i/k\60m\61o\62q\63s\64u\65w\66y\67{8\3\2\24\3\2\63")
        buf.write(";\3\2\62;\3\2\629\4\2ZZzz\5\2\62;CHch\4\2DDdd\3\2\62\63")
        buf.write("\4\2GGgg\4\2--//\4\2RRrr\5\2\f\f$$^^\n\2$$))^^ddhhppt")
        buf.write("tvv\5\2\f\f))^^\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17")
        buf.write("\17\"\"\3\2\f\f\3\3\f\f\2\u0206\2\3\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3")
        buf.write("\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2")
        buf.write("/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\3\u0081\3\2\2\2\5\u008b\3\2\2\2\7\u008d\3\2")
        buf.write("\2\2\t\u0093\3\2\2\2\13\u009a\3\2\2\2\r\u00a3\3\2\2\2")
        buf.write("\17\u00db\3\2\2\2\21\u00dd\3\2\2\2\23\u0107\3\2\2\2\25")
        buf.write("\u0109\3\2\2\2\27\u0113\3\2\2\2\31\u0116\3\2\2\2\33\u011d")
        buf.write("\3\2\2\2\35\u0121\3\2\2\2\37\u0126\3\2\2\2!\u0129\3\2")
        buf.write("\2\2#\u012e\3\2\2\2%\u0132\3\2\2\2\'\u0139\3\2\2\2)\u013f")
        buf.write("\3\2\2\2+\u0148\3\2\2\2-\u014c\3\2\2\2/\u0152\3\2\2\2")
        buf.write("\61\u015a\3\2\2\2\63\u015d\3\2\2\2\65\u0160\3\2\2\2\67")
        buf.write("\u0163\3\2\2\29\u0166\3\2\2\2;\u0169\3\2\2\2=\u016c\3")
        buf.write("\2\2\2?\u016f\3\2\2\2A\u0172\3\2\2\2C\u0175\3\2\2\2E\u0178")
        buf.write("\3\2\2\2G\u017a\3\2\2\2I\u017c\3\2\2\2K\u017f\3\2\2\2")
        buf.write("M\u0182\3\2\2\2O\u0184\3\2\2\2Q\u0186\3\2\2\2S\u0188\3")
        buf.write("\2\2\2U\u018a\3\2\2\2W\u018c\3\2\2\2Y\u018e\3\2\2\2[\u0190")
        buf.write("\3\2\2\2]\u0192\3\2\2\2_\u0194\3\2\2\2a\u0196\3\2\2\2")
        buf.write("c\u0198\3\2\2\2e\u019a\3\2\2\2g\u019c\3\2\2\2i\u019e\3")
        buf.write("\2\2\2k\u01a0\3\2\2\2m\u01a2\3\2\2\2o\u01a4\3\2\2\2q\u01ac")
        buf.write("\3\2\2\2s\u01b2\3\2\2\2u\u01bd\3\2\2\2w\u01cb\3\2\2\2")
        buf.write("y\u01d6\3\2\2\2{\u01e1\3\2\2\2}\u0082\5\5\3\2~\u0082\5")
        buf.write("\7\4\2\177\u0082\5\t\5\2\u0080\u0082\5\13\6\2\u0081}\3")
        buf.write("\2\2\2\u0081~\3\2\2\2\u0081\177\3\2\2\2\u0081\u0080\3")
        buf.write("\2\2\2\u0082\4\3\2\2\2\u0083\u0087\t\2\2\2\u0084\u0086")
        buf.write("\t\3\2\2\u0085\u0084\3\2\2\2\u0086\u0089\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008c\3\2\2\2")
        buf.write("\u0089\u0087\3\2\2\2\u008a\u008c\7\62\2\2\u008b\u0083")
        buf.write("\3\2\2\2\u008b\u008a\3\2\2\2\u008c\6\3\2\2\2\u008d\u008f")
        buf.write("\7\62\2\2\u008e\u0090\t\4\2\2\u008f\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\u008f\3\2\2\2\u0091\u0092\3\2\2\2")
        buf.write("\u0092\b\3\2\2\2\u0093\u0094\7\62\2\2\u0094\u0096\t\5")
        buf.write("\2\2\u0095\u0097\t\6\2\2\u0096\u0095\3\2\2\2\u0097\u0098")
        buf.write("\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2\u0099")
        buf.write("\n\3\2\2\2\u009a\u009b\7\62\2\2\u009b\u009d\t\7\2\2\u009c")
        buf.write("\u009e\t\b\2\2\u009d\u009c\3\2\2\2\u009e\u009f\3\2\2\2")
        buf.write("\u009f\u009d\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0\f\3\2\2")
        buf.write("\2\u00a1\u00a4\5\17\b\2\u00a2\u00a4\5\21\t\2\u00a3\u00a1")
        buf.write("\3\2\2\2\u00a3\u00a2\3\2\2\2\u00a4\16\3\2\2\2\u00a5\u00a7")
        buf.write("\t\3\2\2\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2")
        buf.write("\u00aa\u00ae\7\60\2\2\u00ab\u00ad\t\3\2\2\u00ac\u00ab")
        buf.write("\3\2\2\2\u00ad\u00b0\3\2\2\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00af\3\2\2\2\u00af\u00ba\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b1\u00b3\t\t\2\2\u00b2\u00b4\t\n\2\2\u00b3\u00b2\3")
        buf.write("\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b6\3\2\2\2\u00b5\u00b7")
        buf.write("\t\3\2\2\u00b6\u00b5\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00bb\3\2\2\2")
        buf.write("\u00ba\u00b1\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00dc\3")
        buf.write("\2\2\2\u00bc\u00be\7\60\2\2\u00bd\u00bf\t\3\2\2\u00be")
        buf.write("\u00bd\3\2\2\2\u00bf\u00c0\3\2\2\2\u00c0\u00be\3\2\2\2")
        buf.write("\u00c0\u00c1\3\2\2\2\u00c1\u00cb\3\2\2\2\u00c2\u00c4\t")
        buf.write("\t\2\2\u00c3\u00c5\t\n\2\2\u00c4\u00c3\3\2\2\2\u00c4\u00c5")
        buf.write("\3\2\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00c8\t\3\2\2\u00c7")
        buf.write("\u00c6\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00c7\3\2\2\2")
        buf.write("\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb\u00c2\3")
        buf.write("\2\2\2\u00cb\u00cc\3\2\2\2\u00cc\u00dc\3\2\2\2\u00cd\u00cf")
        buf.write("\t\3\2\2\u00ce\u00cd\3\2\2\2\u00cf\u00d0\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d2\3\2\2\2")
        buf.write("\u00d2\u00d4\t\t\2\2\u00d3\u00d5\t\n\2\2\u00d4\u00d3\3")
        buf.write("\2\2\2\u00d4\u00d5\3\2\2\2\u00d5\u00d7\3\2\2\2\u00d6\u00d8")
        buf.write("\t\3\2\2\u00d7\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9")
        buf.write("\u00d7\3\2\2\2\u00d9\u00da\3\2\2\2\u00da\u00dc\3\2\2\2")
        buf.write("\u00db\u00a6\3\2\2\2\u00db\u00bc\3\2\2\2\u00db\u00ce\3")
        buf.write("\2\2\2\u00dc\20\3\2\2\2\u00dd\u00de\7\62\2\2\u00de\u00f3")
        buf.write("\t\5\2\2\u00df\u00e1\t\6\2\2\u00e0\u00df\3\2\2\2\u00e1")
        buf.write("\u00e2\3\2\2\2\u00e2\u00e0\3\2\2\2\u00e2\u00e3\3\2\2\2")
        buf.write("\u00e3\u00e5\3\2\2\2\u00e4\u00e6\7\60\2\2\u00e5\u00e4")
        buf.write("\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00f4\3\2\2\2\u00e7")
        buf.write("\u00e9\t\6\2\2\u00e8\u00e7\3\2\2\2\u00e9\u00ec\3\2\2\2")
        buf.write("\u00ea\u00e8\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb\u00ed\3")
        buf.write("\2\2\2\u00ec\u00ea\3\2\2\2\u00ed\u00ef\7\60\2\2\u00ee")
        buf.write("\u00f0\t\6\2\2\u00ef\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2")
        buf.write("\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4\3")
        buf.write("\2\2\2\u00f3\u00e0\3\2\2\2\u00f3\u00ea\3\2\2\2\u00f4\u00f5")
        buf.write("\3\2\2\2\u00f5\u00f7\t\13\2\2\u00f6\u00f8\t\n\2\2\u00f7")
        buf.write("\u00f6\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00fa\3\2\2\2")
        buf.write("\u00f9\u00fb\t\3\2\2\u00fa\u00f9\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\22")
        buf.write("\3\2\2\2\u00fe\u00ff\7v\2\2\u00ff\u0100\7t\2\2\u0100\u0101")
        buf.write("\7w\2\2\u0101\u0108\7g\2\2\u0102\u0103\7h\2\2\u0103\u0104")
        buf.write("\7c\2\2\u0104\u0105\7n\2\2\u0105\u0106\7u\2\2\u0106\u0108")
        buf.write("\7g\2\2\u0107\u00fe\3\2\2\2\u0107\u0102\3\2\2\2\u0108")
        buf.write("\24\3\2\2\2\u0109\u010e\7$\2\2\u010a\u010d\n\f\2\2\u010b")
        buf.write("\u010d\5\27\f\2\u010c\u010a\3\2\2\2\u010c\u010b\3\2\2")
        buf.write("\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2\u010e\u010f")
        buf.write("\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3\2\2\2\u0111")
        buf.write("\u0112\7$\2\2\u0112\26\3\2\2\2\u0113\u0114\7^\2\2\u0114")
        buf.write("\u0115\t\r\2\2\u0115\30\3\2\2\2\u0116\u0119\7)\2\2\u0117")
        buf.write("\u011a\n\16\2\2\u0118\u011a\5\27\f\2\u0119\u0117\3\2\2")
        buf.write("\2\u0119\u0118\3\2\2\2\u011a\u011b\3\2\2\2\u011b\u011c")
        buf.write("\7)\2\2\u011c\32\3\2\2\2\u011d\u011e\7x\2\2\u011e\u011f")
        buf.write("\7c\2\2\u011f\u0120\7t\2\2\u0120\34\3\2\2\2\u0121\u0122")
        buf.write("\7h\2\2\u0122\u0123\7w\2\2\u0123\u0124\7p\2\2\u0124\u0125")
        buf.write("\7e\2\2\u0125\36\3\2\2\2\u0126\u0127\7k\2\2\u0127\u0128")
        buf.write("\7h\2\2\u0128 \3\2\2\2\u0129\u012a\7g\2\2\u012a\u012b")
        buf.write("\7n\2\2\u012b\u012c\7u\2\2\u012c\u012d\7g\2\2\u012d\"")
        buf.write("\3\2\2\2\u012e\u012f\7h\2\2\u012f\u0130\7q\2\2\u0130\u0131")
        buf.write("\7t\2\2\u0131$\3\2\2\2\u0132\u0133\7t\2\2\u0133\u0134")
        buf.write("\7g\2\2\u0134\u0135\7v\2\2\u0135\u0136\7w\2\2\u0136\u0137")
        buf.write("\7t\2\2\u0137\u0138\7p\2\2\u0138&\3\2\2\2\u0139\u013a")
        buf.write("\7d\2\2\u013a\u013b\7t\2\2\u013b\u013c\7g\2\2\u013c\u013d")
        buf.write("\7c\2\2\u013d\u013e\7m\2\2\u013e(\3\2\2\2\u013f\u0140")
        buf.write("\7e\2\2\u0140\u0141\7q\2\2\u0141\u0142\7p\2\2\u0142\u0143")
        buf.write("\7v\2\2\u0143\u0144\7k\2\2\u0144\u0145\7p\2\2\u0145\u0146")
        buf.write("\7w\2\2\u0146\u0147\7g\2\2\u0147*\3\2\2\2\u0148\u0149")
        buf.write("\7k\2\2\u0149\u014a\7p\2\2\u014a\u014b\7v\2\2\u014b,\3")
        buf.write("\2\2\2\u014c\u014d\7h\2\2\u014d\u014e\7n\2\2\u014e\u014f")
        buf.write("\7q\2\2\u014f\u0150\7c\2\2\u0150\u0151\7v\2\2\u0151.\3")
        buf.write("\2\2\2\u0152\u0153\7d\2\2\u0153\u0154\7q\2\2\u0154\u0155")
        buf.write("\7q\2\2\u0155\u0156\7n\2\2\u0156\u0157\7g\2\2\u0157\u0158")
        buf.write("\7c\2\2\u0158\u0159\7p\2\2\u0159\60\3\2\2\2\u015a\u015b")
        buf.write("\7-\2\2\u015b\u015c\7-\2\2\u015c\62\3\2\2\2\u015d\u015e")
        buf.write("\7/\2\2\u015e\u015f\7/\2\2\u015f\64\3\2\2\2\u0160\u0161")
        buf.write("\7-\2\2\u0161\u0162\7?\2\2\u0162\66\3\2\2\2\u0163\u0164")
        buf.write("\7/\2\2\u0164\u0165\7?\2\2\u01658\3\2\2\2\u0166\u0167")
        buf.write("\7,\2\2\u0167\u0168\7?\2\2\u0168:\3\2\2\2\u0169\u016a")
        buf.write("\7\61\2\2\u016a\u016b\7?\2\2\u016b<\3\2\2\2\u016c\u016d")
        buf.write("\7?\2\2\u016d\u016e\7?\2\2\u016e>\3\2\2\2\u016f\u0170")
        buf.write("\7#\2\2\u0170\u0171\7?\2\2\u0171@\3\2\2\2\u0172\u0173")
        buf.write("\7>\2\2\u0173\u0174\7?\2\2\u0174B\3\2\2\2\u0175\u0176")
        buf.write("\7@\2\2\u0176\u0177\7?\2\2\u0177D\3\2\2\2\u0178\u0179")
        buf.write("\7>\2\2\u0179F\3\2\2\2\u017a\u017b\7@\2\2\u017bH\3\2\2")
        buf.write("\2\u017c\u017d\7(\2\2\u017d\u017e\7(\2\2\u017eJ\3\2\2")
        buf.write("\2\u017f\u0180\7~\2\2\u0180\u0181\7~\2\2\u0181L\3\2\2")
        buf.write("\2\u0182\u0183\7#\2\2\u0183N\3\2\2\2\u0184\u0185\7-\2")
        buf.write("\2\u0185P\3\2\2\2\u0186\u0187\7/\2\2\u0187R\3\2\2\2\u0188")
        buf.write("\u0189\7,\2\2\u0189T\3\2\2\2\u018a\u018b\7\61\2\2\u018b")
        buf.write("V\3\2\2\2\u018c\u018d\7\'\2\2\u018dX\3\2\2\2\u018e\u018f")
        buf.write("\7?\2\2\u018fZ\3\2\2\2\u0190\u0191\7*\2\2\u0191\\\3\2")
        buf.write("\2\2\u0192\u0193\7+\2\2\u0193^\3\2\2\2\u0194\u0195\7}")
        buf.write("\2\2\u0195`\3\2\2\2\u0196\u0197\7\177\2\2\u0197b\3\2\2")
        buf.write("\2\u0198\u0199\7]\2\2\u0199d\3\2\2\2\u019a\u019b\7_\2")
        buf.write("\2\u019bf\3\2\2\2\u019c\u019d\7=\2\2\u019dh\3\2\2\2\u019e")
        buf.write("\u019f\7.\2\2\u019fj\3\2\2\2\u01a0\u01a1\7<\2\2\u01a1")
        buf.write("l\3\2\2\2\u01a2\u01a3\7\60\2\2\u01a3n\3\2\2\2\u01a4\u01a8")
        buf.write("\t\17\2\2\u01a5\u01a7\t\20\2\2\u01a6\u01a5\3\2\2\2\u01a7")
        buf.write("\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2")
        buf.write("\u01a9p\3\2\2\2\u01aa\u01a8\3\2\2\2\u01ab\u01ad\t\21\2")
        buf.write("\2\u01ac\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac")
        buf.write("\3\2\2\2\u01ae\u01af\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0")
        buf.write("\u01b1\b9\2\2\u01b1r\3\2\2\2\u01b2\u01b3\7\61\2\2\u01b3")
        buf.write("\u01b4\7\61\2\2\u01b4\u01b8\3\2\2\2\u01b5\u01b7\n\22\2")
        buf.write("\2\u01b6\u01b5\3\2\2\2\u01b7\u01ba\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb\3\2\2\2\u01ba")
        buf.write("\u01b8\3\2\2\2\u01bb\u01bc\b:\2\2\u01bct\3\2\2\2\u01bd")
        buf.write("\u01be\7\61\2\2\u01be\u01bf\7,\2\2\u01bf\u01c3\3\2\2\2")
        buf.write("\u01c0\u01c2\13\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c3\u01c1\3\2\2\2\u01c4")
        buf.write("\u01c6\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c6\u01c7\7,\2\2")
        buf.write("\u01c7\u01c8\7\61\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca")
        buf.write("\b;\2\2\u01cav\3\2\2\2\u01cb\u01d0\7$\2\2\u01cc\u01cf")
        buf.write("\n\f\2\2\u01cd\u01cf\5\27\f\2\u01ce\u01cc\3\2\2\2\u01ce")
        buf.write("\u01cd\3\2\2\2\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3")
        buf.write("\2\2\2\u01d3\u01d5\t\23\2\2\u01d4\u01d3\3\2\2\2\u01d5")
        buf.write("x\3\2\2\2\u01d6\u01db\7$\2\2\u01d7\u01da\n\f\2\2\u01d8")
        buf.write("\u01da\5\27\f\2\u01d9\u01d7\3\2\2\2\u01d9\u01d8\3\2\2")
        buf.write("\2\u01da\u01dd\3\2\2\2\u01db\u01d9\3\2\2\2\u01db\u01dc")
        buf.write("\3\2\2\2\u01dc\u01de\3\2\2\2\u01dd\u01db\3\2\2\2\u01de")
        buf.write("\u01df\7^\2\2\u01df\u01e0\n\r\2\2\u01e0z\3\2\2\2\u01e1")
        buf.write("\u01e2\13\2\2\2\u01e2\u01e3\b>\3\2\u01e3|\3\2\2\2+\2\u0081")
        buf.write("\u0087\u008b\u0091\u0098\u009f\u00a3\u00a8\u00ae\u00b3")
        buf.write("\u00b8\u00ba\u00c0\u00c4\u00c9\u00cb\u00d0\u00d4\u00d9")
        buf.write("\u00db\u00e2\u00e5\u00ea\u00f1\u00f3\u00f7\u00fc\u0107")
        buf.write("\u010c\u010e\u0119\u01a8\u01ae\u01b8\u01c3\u01ce\u01d0")
        buf.write("\u01d4\u01d9\u01db\4\b\2\2\3>\2")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTLIT = 1
    FLOATLIT = 2
    BOOLLIT = 3
    STRINGLIT = 4
    RUNELIT = 5
    VAR = 6
    FUNC = 7
    IF = 8
    ELSE = 9
    FOR = 10
    RETURN = 11
    BREAK = 12
    CONTINUE = 13
    INT = 14
    FLOAT = 15
    BOOLEAN = 16
    INCREMENT = 17
    DECREMENT = 18
    PLUS_ASSIGN = 19
    MINUS_ASSIGN = 20
    MUL_ASSIGN = 21
    DIV_ASSIGN = 22
    EQ = 23
    NEQ = 24
    LE = 25
    GE = 26
    LT = 27
    GT = 28
    AND = 29
    OR = 30
    NOT = 31
    PLUS = 32
    MINUS = 33
    MUL = 34
    DIV = 35
    MOD = 36
    ASSIGN = 37
    LPAREN = 38
    RPAREN = 39
    LBRACE = 40
    RBRACE = 41
    LBRACKET = 42
    RBRACKET = 43
    SEMI = 44
    COMMA = 45
    COLON = 46
    DOT = 47
    ID = 48
    WS = 49
    LINE_COMMENT = 50
    BLOCK_COMMENT = 51
    UNCLOSE_STRING = 52
    ILLEGAL_ESCAPE = 53
    ERROR_CHAR = 54

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'func'", "'if'", "'else'", "'for'", "'return'", "'break'", 
            "'continue'", "'int'", "'float'", "'boolean'", "'++'", "'--'", 
            "'+='", "'-='", "'*='", "'/='", "'=='", "'!='", "'<='", "'>='", 
            "'<'", "'>'", "'&&'", "'||'", "'!'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'='", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "':'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INTLIT", "FLOATLIT", "BOOLLIT", "STRINGLIT", "RUNELIT", "VAR", 
            "FUNC", "IF", "ELSE", "FOR", "RETURN", "BREAK", "CONTINUE", 
            "INT", "FLOAT", "BOOLEAN", "INCREMENT", "DECREMENT", "PLUS_ASSIGN", 
            "MINUS_ASSIGN", "MUL_ASSIGN", "DIV_ASSIGN", "EQ", "NEQ", "LE", 
            "GE", "LT", "GT", "AND", "OR", "NOT", "PLUS", "MINUS", "MUL", 
            "DIV", "MOD", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
            "LBRACKET", "RBRACKET", "SEMI", "COMMA", "COLON", "DOT", "ID", 
            "WS", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "ERROR_CHAR" ]

    ruleNames = [ "INTLIT", "DecimalLit", "OctalLit", "HexLit", "BinaryLit", 
                  "FLOATLIT", "DecimalFloat", "HexFloat", "BOOLLIT", "STRINGLIT", 
                  "EscapeSeq", "RUNELIT", "VAR", "FUNC", "IF", "ELSE", "FOR", 
                  "RETURN", "BREAK", "CONTINUE", "INT", "FLOAT", "BOOLEAN", 
                  "INCREMENT", "DECREMENT", "PLUS_ASSIGN", "MINUS_ASSIGN", 
                  "MUL_ASSIGN", "DIV_ASSIGN", "EQ", "NEQ", "LE", "GE", "LT", 
                  "GT", "AND", "OR", "NOT", "PLUS", "MINUS", "MUL", "DIV", 
                  "MOD", "ASSIGN", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
                  "LBRACKET", "RBRACKET", "SEMI", "COMMA", "COLON", "DOT", 
                  "ID", "WS", "LINE_COMMENT", "BLOCK_COMMENT", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

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
                text = result.text
                if text[-1] in ['\n', '\r']:
                    raise UncloseString(text[:-1]) 
                else:
                    raise UncloseString(text)       
            elif tk == self.ILLEGAL_ESCAPE:
                result = super().emit()
                raise IllegalEscape(result.text)    
            elif tk == self.ERROR_CHAR:
                result = super().emit()
                raise ErrorToken(result.text)
            else:
                return super().emit()


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[60] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
             raise ErrorToken(self.text) 
     


