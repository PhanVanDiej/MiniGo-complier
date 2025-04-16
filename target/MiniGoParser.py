# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3h")
        buf.write("\u0285\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\3\2\3\2\7\2q\n\2\f\2\16")
        buf.write("\2t\13\2\3\2\6\2w\n\2\r\2\16\2x\3\2\3\2\3\3\3\3\3\3\5")
        buf.write("\3\u0080\n\3\3\4\3\4\3\4\3\4\6\4\u0086\n\4\r\4\16\4\u0087")
        buf.write("\3\4\3\4\5\4\u008c\n\4\3\4\5\4\u008f\n\4\3\5\3\5\5\5\u0093")
        buf.write("\n\5\3\6\3\6\3\6\5\6\u0098\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00aa\n\7")
        buf.write("\3\7\3\7\7\7\u00ae\n\7\f\7\16\7\u00b1\13\7\3\7\5\7\u00b4")
        buf.write("\n\7\3\b\3\b\3\b\7\b\u00b9\n\b\f\b\16\b\u00bc\13\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\t\u00cc\n\t\f\t\16\t\u00cf\13\t\3\t\5\t\u00d2\n\t\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u00d8\n\n\3\n\3\n\3\n\3\n\5\n\u00de\n")
        buf.write("\n\3\n\5\n\u00e1\n\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\u00ec\n\13\3\13\3\13\5\13\u00f0\n\13\3")
        buf.write("\13\3\13\3\f\3\f\5\f\u00f6\n\f\3\f\3\f\3\f\3\f\5\f\u00fc")
        buf.write("\n\f\3\f\3\f\3\f\5\f\u0101\n\f\3\r\3\r\3\r\5\r\u0106\n")
        buf.write("\r\3\r\5\r\u0109\n\r\3\16\3\16\3\16\7\16\u010e\n\16\f")
        buf.write("\16\16\16\u0111\13\16\3\17\3\17\3\17\3\17\3\17\3\17\5")
        buf.write("\17\u0119\n\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\5\20\u0123\n\20\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\7\24")
        buf.write("\u0136\n\24\f\24\16\24\u0139\13\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\26\3\26\3\26\5\26\u0143\n\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u0149\n\26\3\26\5\26\u014c\n\26\3\27\3\27\3\27")
        buf.write("\3\27\3\27\5\27\u0153\n\27\3\27\3\27\3\27\3\27\5\27\u0159")
        buf.write("\n\27\3\27\5\27\u015c\n\27\3\27\7\27\u015f\n\27\f\27\16")
        buf.write("\27\u0162\13\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0179\n\31\3\32\3\32\3\32\3\32\5\32\u017f")
        buf.write("\n\32\3\33\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\37\3\37\3\37\3\37\5\37\u0190\n\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\5\37\u0197\n\37\5\37\u0199\n\37\3 \3 \3")
        buf.write(" \3 \3 \5 \u01a0\n \3 \3 \5 \u01a4\n \3 \3 \5 \u01a8\n")
        buf.write(" \3 \3 \3 \7 \u01ad\n \f \16 \u01b0\13 \3 \3 \3 \5 \u01b5")
        buf.write("\n \3 \3 \3!\3!\3!\3!\5!\u01bd\n!\3!\5!\u01c0\n!\3!\3")
        buf.write("!\7!\u01c4\n!\f!\16!\u01c7\13!\3!\3!\3\"\3\"\3\"\5\"\u01ce")
        buf.write("\n\"\3\"\3\"\7\"\u01d2\n\"\f\"\16\"\u01d5\13\"\3#\3#\7")
        buf.write("#\u01d9\n#\f#\16#\u01dc\13#\3#\3#\3$\3$\3$\3$\3%\3%\3")
        buf.write("%\3%\3&\3&\5&\u01ea\n&\3&\3&\3\'\3\'\5\'\u01f0\n\'\3\'")
        buf.write("\3\'\3(\3(\5(\u01f6\n(\3(\3(\3)\3)\3)\5)\u01fd\n)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\3)\7)\u0209\n)\f)\16)\u020c\13")
        buf.write(")\3*\3*\3*\3+\3+\3,\3,\3-\3-\3-\5-\u0218\n-\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\5-\u0225\n-\3-\3-\5-\u0229\n-\3")
        buf.write("-\3-\3-\3-\5-\u022f\n-\3-\7-\u0232\n-\f-\16-\u0235\13")
        buf.write("-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u023f\n.\3/\3/\3\60\3\60")
        buf.write("\3\60\5\60\u0246\n\60\3\60\3\60\3\60\3\60\5\60\u024c\n")
        buf.write("\60\3\60\5\60\u024f\n\60\3\60\3\60\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u0257\n\61\3\61\3\61\3\62\3\62\3\62\3\62\5\62\u025f")
        buf.write("\n\62\3\63\3\63\3\63\7\63\u0264\n\63\f\63\16\63\u0267")
        buf.write("\13\63\3\64\3\64\3\64\5\64\u026c\n\64\3\64\3\64\3\65\3")
        buf.write("\65\3\65\3\65\3\65\3\66\3\66\3\66\7\66\u0278\n\66\f\66")
        buf.write("\16\66\u027b\13\66\3\67\3\67\3\67\7\67\u0280\n\67\f\67")
        buf.write("\16\67\u0283\13\67\3\67\2\4PX8\2\4\6\b\n\f\16\20\22\24")
        buf.write("\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVX")
        buf.write("Z\\^`bdfhjl\2\b\3\2\20 \4\2\t\t(,\3\2-.\4\2\16\16=B\6")
        buf.write("\2\16\16=>@ACP\6\2RRWW\\]aa\2\u02ba\2n\3\2\2\2\4|\3\2")
        buf.write("\2\2\6\u0081\3\2\2\2\b\u0090\3\2\2\2\n\u0097\3\2\2\2\f")
        buf.write("\u0099\3\2\2\2\16\u00b5\3\2\2\2\20\u00c1\3\2\2\2\22\u00d3")
        buf.write("\3\2\2\2\24\u00e4\3\2\2\2\26\u00f3\3\2\2\2\30\u0108\3")
        buf.write("\2\2\2\32\u010a\3\2\2\2\34\u0118\3\2\2\2\36\u0122\3\2")
        buf.write("\2\2 \u0124\3\2\2\2\"\u0126\3\2\2\2$\u012b\3\2\2\2&\u012f")
        buf.write("\3\2\2\2(\u013c\3\2\2\2*\u013f\3\2\2\2,\u014d\3\2\2\2")
        buf.write(".\u0165\3\2\2\2\60\u0178\3\2\2\2\62\u017e\3\2\2\2\64\u0180")
        buf.write("\3\2\2\2\66\u0184\3\2\2\28\u0186\3\2\2\2:\u0188\3\2\2")
        buf.write("\2<\u018b\3\2\2\2>\u019a\3\2\2\2@\u01b8\3\2\2\2B\u01cd")
        buf.write("\3\2\2\2D\u01d6\3\2\2\2F\u01df\3\2\2\2H\u01e3\3\2\2\2")
        buf.write("J\u01e7\3\2\2\2L\u01ed\3\2\2\2N\u01f3\3\2\2\2P\u01fc\3")
        buf.write("\2\2\2R\u020d\3\2\2\2T\u0210\3\2\2\2V\u0212\3\2\2\2X\u0217")
        buf.write("\3\2\2\2Z\u023e\3\2\2\2\\\u0240\3\2\2\2^\u0242\3\2\2\2")
        buf.write("`\u0252\3\2\2\2b\u025e\3\2\2\2d\u0260\3\2\2\2f\u026b\3")
        buf.write("\2\2\2h\u026f\3\2\2\2j\u0274\3\2\2\2l\u027c\3\2\2\2nr")
        buf.write("\5\4\3\2oq\5\6\4\2po\3\2\2\2qt\3\2\2\2rp\3\2\2\2rs\3\2")
        buf.write("\2\2sv\3\2\2\2tr\3\2\2\2uw\5\n\6\2vu\3\2\2\2wx\3\2\2\2")
        buf.write("xv\3\2\2\2xy\3\2\2\2yz\3\2\2\2z{\7\2\2\3{\3\3\2\2\2|}")
        buf.write("\7\3\2\2}\177\7b\2\2~\u0080\7\4\2\2\177~\3\2\2\2\177\u0080")
        buf.write("\3\2\2\2\u0080\5\3\2\2\2\u0081\u008b\7\5\2\2\u0082\u008c")
        buf.write("\7]\2\2\u0083\u0085\7\6\2\2\u0084\u0086\5\b\5\2\u0085")
        buf.write("\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\7")
        buf.write("\7\2\2\u008a\u008c\3\2\2\2\u008b\u0082\3\2\2\2\u008b\u0083")
        buf.write("\3\2\2\2\u008c\u008e\3\2\2\2\u008d\u008f\7\4\2\2\u008e")
        buf.write("\u008d\3\2\2\2\u008e\u008f\3\2\2\2\u008f\7\3\2\2\2\u0090")
        buf.write("\u0092\7]\2\2\u0091\u0093\7\4\2\2\u0092\u0091\3\2\2\2")
        buf.write("\u0092\u0093\3\2\2\2\u0093\t\3\2\2\2\u0094\u0098\5\22")
        buf.write("\n\2\u0095\u0098\5\f\7\2\u0096\u0098\5\20\t\2\u0097\u0094")
        buf.write("\3\2\2\2\u0097\u0095\3\2\2\2\u0097\u0096\3\2\2\2\u0098")
        buf.write("\13\3\2\2\2\u0099\u00b3\7\b\2\2\u009a\u009b\5l\67\2\u009b")
        buf.write("\u009c\5\36\20\2\u009c\u009d\7\4\2\2\u009d\u00b4\3\2\2")
        buf.write("\2\u009e\u009f\5l\67\2\u009f\u00a0\5\36\20\2\u00a0\u00a1")
        buf.write("\7\t\2\2\u00a1\u00a2\5j\66\2\u00a2\u00a3\7\4\2\2\u00a3")
        buf.write("\u00b4\3\2\2\2\u00a4\u00af\7\6\2\2\u00a5\u00a6\7b\2\2")
        buf.write("\u00a6\u00a9\5\36\20\2\u00a7\u00a8\7\t\2\2\u00a8\u00aa")
        buf.write("\5P)\2\u00a9\u00a7\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab")
        buf.write("\3\2\2\2\u00ab\u00ac\7\4\2\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write("\u00a5\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2")
        buf.write("\u00af\u00b0\3\2\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00af\3")
        buf.write("\2\2\2\u00b2\u00b4\7\7\2\2\u00b3\u009a\3\2\2\2\u00b3\u009e")
        buf.write("\3\2\2\2\u00b3\u00a4\3\2\2\2\u00b4\r\3\2\2\2\u00b5\u00ba")
        buf.write("\7b\2\2\u00b6\u00b7\7\n\2\2\u00b7\u00b9\7b\2\2\u00b8\u00b6")
        buf.write("\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3\2\2\2\u00ba")
        buf.write("\u00bb\3\2\2\2\u00bb\u00bd\3\2\2\2\u00bc\u00ba\3\2\2\2")
        buf.write("\u00bd\u00be\7\13\2\2\u00be\u00bf\5j\66\2\u00bf\u00c0")
        buf.write("\7\4\2\2\u00c0\17\3\2\2\2\u00c1\u00d1\7\f\2\2\u00c2\u00c3")
        buf.write("\7b\2\2\u00c3\u00c4\5\36\20\2\u00c4\u00c5\7\4\2\2\u00c5")
        buf.write("\u00d2\3\2\2\2\u00c6\u00cd\7\6\2\2\u00c7\u00c8\7b\2\2")
        buf.write("\u00c8\u00c9\5\36\20\2\u00c9\u00ca\7\4\2\2\u00ca\u00cc")
        buf.write("\3\2\2\2\u00cb\u00c7\3\2\2\2\u00cc\u00cf\3\2\2\2\u00cd")
        buf.write("\u00cb\3\2\2\2\u00cd\u00ce\3\2\2\2\u00ce\u00d0\3\2\2\2")
        buf.write("\u00cf\u00cd\3\2\2\2\u00d0\u00d2\7\7\2\2\u00d1\u00c2\3")
        buf.write("\2\2\2\u00d1\u00c6\3\2\2\2\u00d2\21\3\2\2\2\u00d3\u00d4")
        buf.write("\7\r\2\2\u00d4\u00d5\7b\2\2\u00d5\u00d7\7\6\2\2\u00d6")
        buf.write("\u00d8\5\32\16\2\u00d7\u00d6\3\2\2\2\u00d7\u00d8\3\2\2")
        buf.write("\2\u00d8\u00d9\3\2\2\2\u00d9\u00e0\7\7\2\2\u00da\u00e1")
        buf.write("\5\36\20\2\u00db\u00dd\7\6\2\2\u00dc\u00de\5\32\16\2\u00dd")
        buf.write("\u00dc\3\2\2\2\u00dd\u00de\3\2\2\2\u00de\u00df\3\2\2\2")
        buf.write("\u00df\u00e1\7\7\2\2\u00e0\u00da\3\2\2\2\u00e0\u00db\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e3")
        buf.write("\5D#\2\u00e3\23\3\2\2\2\u00e4\u00e5\7\r\2\2\u00e5\u00e6")
        buf.write("\7\6\2\2\u00e6\u00e7\5\26\f\2\u00e7\u00e8\7\7\2\2\u00e8")
        buf.write("\u00e9\7b\2\2\u00e9\u00eb\7\6\2\2\u00ea\u00ec\5\32\16")
        buf.write("\2\u00eb\u00ea\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00ef\7\7\2\2\u00ee\u00f0\5\30\r\2\u00ef")
        buf.write("\u00ee\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2")
        buf.write("\u00f1\u00f2\5D#\2\u00f2\25\3\2\2\2\u00f3\u0100\7b\2\2")
        buf.write("\u00f4\u00f6\7\16\2\2\u00f5\u00f4\3\2\2\2\u00f5\u00f6")
        buf.write("\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u0101\5\36\20\2\u00f8")
        buf.write("\u00f9\7\6\2\2\u00f9\u00fb\7b\2\2\u00fa\u00fc\7\16\2\2")
        buf.write("\u00fb\u00fa\3\2\2\2\u00fb\u00fc\3\2\2\2\u00fc\u00fd\3")
        buf.write("\2\2\2\u00fd\u00fe\5\36\20\2\u00fe\u00ff\7\7\2\2\u00ff")
        buf.write("\u0101\3\2\2\2\u0100\u00f5\3\2\2\2\u0100\u00f8\3\2\2\2")
        buf.write("\u0101\27\3\2\2\2\u0102\u0109\5\36\20\2\u0103\u0105\7")
        buf.write("\6\2\2\u0104\u0106\5\32\16\2\u0105\u0104\3\2\2\2\u0105")
        buf.write("\u0106\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\7\7\2\2")
        buf.write("\u0108\u0102\3\2\2\2\u0108\u0103\3\2\2\2\u0109\31\3\2")
        buf.write("\2\2\u010a\u010f\5\34\17\2\u010b\u010c\7\n\2\2\u010c\u010e")
        buf.write("\5\34\17\2\u010d\u010b\3\2\2\2\u010e\u0111\3\2\2\2\u010f")
        buf.write("\u010d\3\2\2\2\u010f\u0110\3\2\2\2\u0110\33\3\2\2\2\u0111")
        buf.write("\u010f\3\2\2\2\u0112\u0113\7b\2\2\u0113\u0119\5\36\20")
        buf.write("\2\u0114\u0119\5\36\20\2\u0115\u0116\7b\2\2\u0116\u0117")
        buf.write("\7\17\2\2\u0117\u0119\5\36\20\2\u0118\u0112\3\2\2\2\u0118")
        buf.write("\u0114\3\2\2\2\u0118\u0115\3\2\2\2\u0119\35\3\2\2\2\u011a")
        buf.write("\u0123\5 \21\2\u011b\u0123\5\"\22\2\u011c\u0123\5$\23")
        buf.write("\2\u011d\u0123\5&\24\2\u011e\u0123\5(\25\2\u011f\u0123")
        buf.write("\5*\26\2\u0120\u0123\5,\27\2\u0121\u0123\5.\30\2\u0122")
        buf.write("\u011a\3\2\2\2\u0122\u011b\3\2\2\2\u0122\u011c\3\2\2\2")
        buf.write("\u0122\u011d\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u011f\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123\37")
        buf.write("\3\2\2\2\u0124\u0125\t\2\2\2\u0125!\3\2\2\2\u0126\u0127")
        buf.write("\7!\2\2\u0127\u0128\5P)\2\u0128\u0129\7\"\2\2\u0129\u012a")
        buf.write("\5\36\20\2\u012a#\3\2\2\2\u012b\u012c\7!\2\2\u012c\u012d")
        buf.write("\7\"\2\2\u012d\u012e\5\36\20\2\u012e%\3\2\2\2\u012f\u0130")
        buf.write("\7#\2\2\u0130\u0137\7$\2\2\u0131\u0132\7b\2\2\u0132\u0133")
        buf.write("\5\36\20\2\u0133\u0134\7\4\2\2\u0134\u0136\3\2\2\2\u0135")
        buf.write("\u0131\3\2\2\2\u0136\u0139\3\2\2\2\u0137\u0135\3\2\2\2")
        buf.write("\u0137\u0138\3\2\2\2\u0138\u013a\3\2\2\2\u0139\u0137\3")
        buf.write("\2\2\2\u013a\u013b\7%\2\2\u013b\'\3\2\2\2\u013c\u013d")
        buf.write("\7\16\2\2\u013d\u013e\5\36\20\2\u013e)\3\2\2\2\u013f\u0140")
        buf.write("\7\r\2\2\u0140\u0142\7\6\2\2\u0141\u0143\5\32\16\2\u0142")
        buf.write("\u0141\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\3\2\2\2")
        buf.write("\u0144\u014b\7\7\2\2\u0145\u014c\5\36\20\2\u0146\u0148")
        buf.write("\7\6\2\2\u0147\u0149\5\32\16\2\u0148\u0147\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\u014a\3\2\2\2\u014a\u014c\7\7\2\2")
        buf.write("\u014b\u0145\3\2\2\2\u014b\u0146\3\2\2\2\u014b\u014c\3")
        buf.write("\2\2\2\u014c+\3\2\2\2\u014d\u014e\7&\2\2\u014e\u0160\7")
        buf.write("$\2\2\u014f\u0150\7b\2\2\u0150\u0152\7\6\2\2\u0151\u0153")
        buf.write("\5\32\16\2\u0152\u0151\3\2\2\2\u0152\u0153\3\2\2\2\u0153")
        buf.write("\u0154\3\2\2\2\u0154\u015b\7\7\2\2\u0155\u015c\5\36\20")
        buf.write("\2\u0156\u0158\7\6\2\2\u0157\u0159\5\32\16\2\u0158\u0157")
        buf.write("\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\3\2\2\2\u015a")
        buf.write("\u015c\7\7\2\2\u015b\u0155\3\2\2\2\u015b\u0156\3\2\2\2")
        buf.write("\u015b\u015c\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015f\7")
        buf.write("\4\2\2\u015e\u014f\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e")
        buf.write("\3\2\2\2\u0160\u0161\3\2\2\2\u0161\u0163\3\2\2\2\u0162")
        buf.write("\u0160\3\2\2\2\u0163\u0164\7%\2\2\u0164-\3\2\2\2\u0165")
        buf.write("\u0166\7\'\2\2\u0166\u0167\7!\2\2\u0167\u0168\5\36\20")
        buf.write("\2\u0168\u0169\7\"\2\2\u0169\u016a\5\36\20\2\u016a/\3")
        buf.write("\2\2\2\u016b\u016c\5\62\32\2\u016c\u016d\7\4\2\2\u016d")
        buf.write("\u0179\3\2\2\2\u016e\u0179\5<\37\2\u016f\u0179\5> \2\u0170")
        buf.write("\u0179\5@!\2\u0171\u0179\5D#\2\u0172\u0179\5J&\2\u0173")
        buf.write("\u0179\5L\'\2\u0174\u0179\5N(\2\u0175\u0179\5F$\2\u0176")
        buf.write("\u0179\5H%\2\u0177\u0179\5\f\7\2\u0178\u016b\3\2\2\2\u0178")
        buf.write("\u016e\3\2\2\2\u0178\u016f\3\2\2\2\u0178\u0170\3\2\2\2")
        buf.write("\u0178\u0171\3\2\2\2\u0178\u0172\3\2\2\2\u0178\u0173\3")
        buf.write("\2\2\2\u0178\u0174\3\2\2\2\u0178\u0175\3\2\2\2\u0178\u0176")
        buf.write("\3\2\2\2\u0178\u0177\3\2\2\2\u0179\61\3\2\2\2\u017a\u017f")
        buf.write("\5\64\33\2\u017b\u017f\5\16\b\2\u017c\u017f\5:\36\2\u017d")
        buf.write("\u017f\58\35\2\u017e\u017a\3\2\2\2\u017e\u017b\3\2\2\2")
        buf.write("\u017e\u017c\3\2\2\2\u017e\u017d\3\2\2\2\u017f\63\3\2")
        buf.write("\2\2\u0180\u0181\5\66\34\2\u0181\u0182\t\3\2\2\u0182\u0183")
        buf.write("\5j\66\2\u0183\65\3\2\2\2\u0184\u0185\5j\66\2\u0185\67")
        buf.write("\3\2\2\2\u0186\u0187\5P)\2\u01879\3\2\2\2\u0188\u0189")
        buf.write("\5P)\2\u0189\u018a\t\4\2\2\u018a;\3\2\2\2\u018b\u018f")
        buf.write("\7/\2\2\u018c\u018d\5\62\32\2\u018d\u018e\7\4\2\2\u018e")
        buf.write("\u0190\3\2\2\2\u018f\u018c\3\2\2\2\u018f\u0190\3\2\2\2")
        buf.write("\u0190\u0191\3\2\2\2\u0191\u0192\5P)\2\u0192\u0198\5D")
        buf.write("#\2\u0193\u0196\7\60\2\2\u0194\u0197\5<\37\2\u0195\u0197")
        buf.write("\5D#\2\u0196\u0194\3\2\2\2\u0196\u0195\3\2\2\2\u0197\u0199")
        buf.write("\3\2\2\2\u0198\u0193\3\2\2\2\u0198\u0199\3\2\2\2\u0199")
        buf.write("=\3\2\2\2\u019a\u01b4\7\61\2\2\u019b\u01b5\3\2\2\2\u019c")
        buf.write("\u01b5\3\2\2\2\u019d\u01b5\5P)\2\u019e\u01a0\5\62\32\2")
        buf.write("\u019f\u019e\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0\u01a1\3")
        buf.write("\2\2\2\u01a1\u01a3\7\4\2\2\u01a2\u01a4\5P)\2\u01a3\u01a2")
        buf.write("\3\2\2\2\u01a3\u01a4\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5")
        buf.write("\u01a7\7\4\2\2\u01a6\u01a8\5\62\32\2\u01a7\u01a6\3\2\2")
        buf.write("\2\u01a7\u01a8\3\2\2\2\u01a8\u01b5\3\2\2\2\u01a9\u01ae")
        buf.write("\7b\2\2\u01aa\u01ab\7\n\2\2\u01ab\u01ad\7b\2\2\u01ac\u01aa")
        buf.write("\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u01b1\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b1\u01b2\7\13\2\2\u01b2\u01b3\7\62\2\2\u01b3\u01b5")
        buf.write("\5P)\2\u01b4\u019b\3\2\2\2\u01b4\u019c\3\2\2\2\u01b4\u019d")
        buf.write("\3\2\2\2\u01b4\u019f\3\2\2\2\u01b4\u01a9\3\2\2\2\u01b5")
        buf.write("\u01b6\3\2\2\2\u01b6\u01b7\5D#\2\u01b7?\3\2\2\2\u01b8")
        buf.write("\u01bc\7\63\2\2\u01b9\u01ba\5\62\32\2\u01ba\u01bb\7\4")
        buf.write("\2\2\u01bb\u01bd\3\2\2\2\u01bc\u01b9\3\2\2\2\u01bc\u01bd")
        buf.write("\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01c0\5P)\2\u01bf\u01be")
        buf.write("\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c1")
        buf.write("\u01c5\7$\2\2\u01c2\u01c4\5B\"\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("\u01c7\3\2\2\2\u01c5\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c8\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c8\u01c9\7")
        buf.write("%\2\2\u01c9A\3\2\2\2\u01ca\u01cb\7\64\2\2\u01cb\u01ce")
        buf.write("\5j\66\2\u01cc\u01ce\7\65\2\2\u01cd\u01ca\3\2\2\2\u01cd")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d3\7\66\2")
        buf.write("\2\u01d0\u01d2\5\60\31\2\u01d1\u01d0\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4")
        buf.write("C\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01da\7$\2\2\u01d7")
        buf.write("\u01d9\5\60\31\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2")
        buf.write("\2\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd")
        buf.write("\3\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01de\7%\2\2\u01de")
        buf.write("E\3\2\2\2\u01df\u01e0\7\67\2\2\u01e0\u01e1\5P)\2\u01e1")
        buf.write("\u01e2\7\4\2\2\u01e2G\3\2\2\2\u01e3\u01e4\78\2\2\u01e4")
        buf.write("\u01e5\5P)\2\u01e5\u01e6\7\4\2\2\u01e6I\3\2\2\2\u01e7")
        buf.write("\u01e9\79\2\2\u01e8\u01ea\5j\66\2\u01e9\u01e8\3\2\2\2")
        buf.write("\u01e9\u01ea\3\2\2\2\u01ea\u01eb\3\2\2\2\u01eb\u01ec\7")
        buf.write("\4\2\2\u01ecK\3\2\2\2\u01ed\u01ef\7:\2\2\u01ee\u01f0\7")
        buf.write("b\2\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1")
        buf.write("\3\2\2\2\u01f1\u01f2\7\4\2\2\u01f2M\3\2\2\2\u01f3\u01f5")
        buf.write("\7;\2\2\u01f4\u01f6\7b\2\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\7\4\2\2\u01f8")
        buf.write("O\3\2\2\2\u01f9\u01fa\b)\1\2\u01fa\u01fd\5X-\2\u01fb\u01fd")
        buf.write("\5R*\2\u01fc\u01f9\3\2\2\2\u01fc\u01fb\3\2\2\2\u01fd\u020a")
        buf.write("\3\2\2\2\u01fe\u01ff\f\4\2\2\u01ff\u0200\5V,\2\u0200\u0201")
        buf.write("\5P)\5\u0201\u0209\3\2\2\2\u0202\u0203\f\3\2\2\u0203\u0204")
        buf.write("\7<\2\2\u0204\u0205\5P)\2\u0205\u0206\7\66\2\2\u0206\u0207")
        buf.write("\5P)\4\u0207\u0209\3\2\2\2\u0208\u01fe\3\2\2\2\u0208\u0202")
        buf.write("\3\2\2\2\u0209\u020c\3\2\2\2\u020a\u0208\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020bQ\3\2\2\2\u020c\u020a\3\2\2\2\u020d")
        buf.write("\u020e\5T+\2\u020e\u020f\5P)\2\u020fS\3\2\2\2\u0210\u0211")
        buf.write("\t\5\2\2\u0211U\3\2\2\2\u0212\u0213\t\6\2\2\u0213W\3\2")
        buf.write("\2\2\u0214\u0215\b-\1\2\u0215\u0218\5Z.\2\u0216\u0218")
        buf.write("\5h\65\2\u0217\u0214\3\2\2\2\u0217\u0216\3\2\2\2\u0218")
        buf.write("\u0233\3\2\2\2\u0219\u021a\f\7\2\2\u021a\u021b\7Q\2\2")
        buf.write("\u021b\u0232\7b\2\2\u021c\u021d\f\6\2\2\u021d\u021e\7")
        buf.write("!\2\2\u021e\u021f\5P)\2\u021f\u0220\7\"\2\2\u0220\u0232")
        buf.write("\3\2\2\2\u0221\u0222\f\5\2\2\u0222\u0224\7!\2\2\u0223")
        buf.write("\u0225\5P)\2\u0224\u0223\3\2\2\2\u0224\u0225\3\2\2\2\u0225")
        buf.write("\u0226\3\2\2\2\u0226\u0228\7\66\2\2\u0227\u0229\5P)\2")
        buf.write("\u0228\u0227\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022a\3")
        buf.write("\2\2\2\u022a\u0232\7\"\2\2\u022b\u022c\f\4\2\2\u022c\u022e")
        buf.write("\7\6\2\2\u022d\u022f\5j\66\2\u022e\u022d\3\2\2\2\u022e")
        buf.write("\u022f\3\2\2\2\u022f\u0230\3\2\2\2\u0230\u0232\7\7\2\2")
        buf.write("\u0231\u0219\3\2\2\2\u0231\u021c\3\2\2\2\u0231\u0221\3")
        buf.write("\2\2\2\u0231\u022b\3\2\2\2\u0232\u0235\3\2\2\2\u0233\u0231")
        buf.write("\3\2\2\2\u0233\u0234\3\2\2\2\u0234Y\3\2\2\2\u0235\u0233")
        buf.write("\3\2\2\2\u0236\u023f\7b\2\2\u0237\u023f\5\\/\2\u0238\u0239")
        buf.write("\7\6\2\2\u0239\u023a\5P)\2\u023a\u023b\7\7\2\2\u023b\u023f")
        buf.write("\3\2\2\2\u023c\u023f\5^\60\2\u023d\u023f\5`\61\2\u023e")
        buf.write("\u0236\3\2\2\2\u023e\u0237\3\2\2\2\u023e\u0238\3\2\2\2")
        buf.write("\u023e\u023c\3\2\2\2\u023e\u023d\3\2\2\2\u023f[\3\2\2")
        buf.write("\2\u0240\u0241\t\7\2\2\u0241]\3\2\2\2\u0242\u0243\7\r")
        buf.write("\2\2\u0243\u0245\7\6\2\2\u0244\u0246\5\32\16\2\u0245\u0244")
        buf.write("\3\2\2\2\u0245\u0246\3\2\2\2\u0246\u0247\3\2\2\2\u0247")
        buf.write("\u024e\7\7\2\2\u0248\u024f\5\36\20\2\u0249\u024b\7\6\2")
        buf.write("\2\u024a\u024c\5\32\16\2\u024b\u024a\3\2\2\2\u024b\u024c")
        buf.write("\3\2\2\2\u024c\u024d\3\2\2\2\u024d\u024f\7\7\2\2\u024e")
        buf.write("\u0248\3\2\2\2\u024e\u0249\3\2\2\2\u024e\u024f\3\2\2\2")
        buf.write("\u024f\u0250\3\2\2\2\u0250\u0251\5D#\2\u0251_\3\2\2\2")
        buf.write("\u0252\u0253\5b\62\2\u0253\u0256\7$\2\2\u0254\u0257\5")
        buf.write("d\63\2\u0255\u0257\5j\66\2\u0256\u0254\3\2\2\2\u0256\u0255")
        buf.write("\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\3\2\2\2\u0258")
        buf.write("\u0259\7%\2\2\u0259a\3\2\2\2\u025a\u025f\5&\24\2\u025b")
        buf.write("\u025f\5\"\22\2\u025c\u025f\5$\23\2\u025d\u025f\5.\30")
        buf.write("\2\u025e\u025a\3\2\2\2\u025e\u025b\3\2\2\2\u025e\u025c")
        buf.write("\3\2\2\2\u025e\u025d\3\2\2\2\u025fc\3\2\2\2\u0260\u0265")
        buf.write("\5f\64\2\u0261\u0262\7\n\2\2\u0262\u0264\5f\64\2\u0263")
        buf.write("\u0261\3\2\2\2\u0264\u0267\3\2\2\2\u0265\u0263\3\2\2\2")
        buf.write("\u0265\u0266\3\2\2\2\u0266e\3\2\2\2\u0267\u0265\3\2\2")
        buf.write("\2\u0268\u0269\5P)\2\u0269\u026a\7\66\2\2\u026a\u026c")
        buf.write("\3\2\2\2\u026b\u0268\3\2\2\2\u026b\u026c\3\2\2\2\u026c")
        buf.write("\u026d\3\2\2\2\u026d\u026e\5P)\2\u026eg\3\2\2\2\u026f")
        buf.write("\u0270\5\36\20\2\u0270\u0271\7\6\2\2\u0271\u0272\5P)\2")
        buf.write("\u0272\u0273\7\7\2\2\u0273i\3\2\2\2\u0274\u0279\5P)\2")
        buf.write("\u0275\u0276\7\n\2\2\u0276\u0278\5P)\2\u0277\u0275\3\2")
        buf.write("\2\2\u0278\u027b\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u027a")
        buf.write("\3\2\2\2\u027ak\3\2\2\2\u027b\u0279\3\2\2\2\u027c\u0281")
        buf.write("\7b\2\2\u027d\u027e\7\n\2\2\u027e\u0280\7b\2\2\u027f\u027d")
        buf.write("\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0281")
        buf.write("\u0282\3\2\2\2\u0282m\3\2\2\2\u0283\u0281\3\2\2\2Krx\177")
        buf.write("\u0087\u008b\u008e\u0092\u0097\u00a9\u00af\u00b3\u00ba")
        buf.write("\u00cd\u00d1\u00d7\u00dd\u00e0\u00eb\u00ef\u00f5\u00fb")
        buf.write("\u0100\u0105\u0108\u010f\u0118\u0122\u0137\u0142\u0148")
        buf.write("\u014b\u0152\u0158\u015b\u0160\u0178\u017e\u018f\u0196")
        buf.write("\u0198\u019f\u01a3\u01a7\u01ae\u01b4\u01bc\u01bf\u01c5")
        buf.write("\u01cd\u01d3\u01da\u01e9\u01ef\u01f5\u01fc\u0208\u020a")
        buf.write("\u0217\u0224\u0228\u022e\u0231\u0233\u023e\u0245\u024b")
        buf.write("\u024e\u0256\u025e\u0265\u026b\u0279\u0281")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'package'", "';'", "'import'", "'('", 
                     "')'", "'var'", "'='", "','", "':='", "'type'", "'func'", 
                     "'*'", "'...'", "'int'", "'int8'", "'int16'", "'int32'", 
                     "'int64'", "'uint'", "'uint8'", "'uint16'", "'uint32'", 
                     "'uint64'", "'float32'", "'float64'", "'float'", "'string'", 
                     "'bool'", "'byte'", "'rune'", "'['", "']'", "'struct'", 
                     "'{'", "'}'", "'interface'", "'map'", "'+='", "'-='", 
                     "'*='", "'/='", "'%='", "'++'", "'--'", "'if'", "'else'", 
                     "'for'", "'range'", "'switch'", "'case'", "'default'", 
                     "':'", "'go'", "'defer'", "'return'", "'break'", "'continue'", 
                     "'?'", "'+'", "'-'", "'!'", "'^'", "'&'", "'<-'", "'/'", 
                     "'%'", "'|'", "'<<'", "'>>'", "'&^'", "'=='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "INTLIT", "BINARY_LIT", "DECIMAL_LIT", "OCTAL_LIT", 
                      "HEX_LIT", "FLOATLIT", "DECIMAL_FLOAT", "HEX_FLOAT", 
                      "EXPONENT", "HEX_EXPONENT", "BOOLLIT", "STRINGLIT", 
                      "RAW_STRING", "INTERPRETED_STRING", "ESCAPED_CHAR", 
                      "RUNELIT", "ID", "COMMENT", "BLOCK_COMMENT", "WS", 
                      "ERROR_CHAR", "ILLEGAL_ESCAPE", "UNCLOSE_STRING" ]

    RULE_program = 0
    RULE_packageDecl = 1
    RULE_importDecl = 2
    RULE_importSpec = 3
    RULE_decl = 4
    RULE_vardecl = 5
    RULE_shortVardecl = 6
    RULE_typedecl = 7
    RULE_funcdecl = 8
    RULE_methodDecl = 9
    RULE_receiver = 10
    RULE_result = 11
    RULE_paramlist = 12
    RULE_param = 13
    RULE_typespec = 14
    RULE_primitiveType = 15
    RULE_arrayType = 16
    RULE_sliceType = 17
    RULE_structType = 18
    RULE_pointerType = 19
    RULE_functionType = 20
    RULE_interfaceType = 21
    RULE_mapType = 22
    RULE_stmt = 23
    RULE_simpleStmt = 24
    RULE_assignstmt = 25
    RULE_lhs = 26
    RULE_exprStmt = 27
    RULE_incDecStmt = 28
    RULE_ifstmt = 29
    RULE_forstmt = 30
    RULE_switchstmt = 31
    RULE_caseclause = 32
    RULE_blockstmt = 33
    RULE_gostmt = 34
    RULE_deferstmt = 35
    RULE_returnstmt = 36
    RULE_breakstmt = 37
    RULE_continuestmt = 38
    RULE_expr = 39
    RULE_unaryExpr = 40
    RULE_unaryOp = 41
    RULE_binaryOp = 42
    RULE_primaryExpr = 43
    RULE_operand = 44
    RULE_basicLit = 45
    RULE_functionLit = 46
    RULE_compositeLit = 47
    RULE_literalType = 48
    RULE_keyValList = 49
    RULE_keyVal = 50
    RULE_conversion = 51
    RULE_exprlist = 52
    RULE_idlist = 53

    ruleNames =  [ "program", "packageDecl", "importDecl", "importSpec", 
                   "decl", "vardecl", "shortVardecl", "typedecl", "funcdecl", 
                   "methodDecl", "receiver", "result", "paramlist", "param", 
                   "typespec", "primitiveType", "arrayType", "sliceType", 
                   "structType", "pointerType", "functionType", "interfaceType", 
                   "mapType", "stmt", "simpleStmt", "assignstmt", "lhs", 
                   "exprStmt", "incDecStmt", "ifstmt", "forstmt", "switchstmt", 
                   "caseclause", "blockstmt", "gostmt", "deferstmt", "returnstmt", 
                   "breakstmt", "continuestmt", "expr", "unaryExpr", "unaryOp", 
                   "binaryOp", "primaryExpr", "operand", "basicLit", "functionLit", 
                   "compositeLit", "literalType", "keyValList", "keyVal", 
                   "conversion", "exprlist", "idlist" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    T__46=47
    T__47=48
    T__48=49
    T__49=50
    T__50=51
    T__51=52
    T__52=53
    T__53=54
    T__54=55
    T__55=56
    T__56=57
    T__57=58
    T__58=59
    T__59=60
    T__60=61
    T__61=62
    T__62=63
    T__63=64
    T__64=65
    T__65=66
    T__66=67
    T__67=68
    T__68=69
    T__69=70
    T__70=71
    T__71=72
    T__72=73
    T__73=74
    T__74=75
    T__75=76
    T__76=77
    T__77=78
    T__78=79
    INTLIT=80
    BINARY_LIT=81
    DECIMAL_LIT=82
    OCTAL_LIT=83
    HEX_LIT=84
    FLOATLIT=85
    DECIMAL_FLOAT=86
    HEX_FLOAT=87
    EXPONENT=88
    HEX_EXPONENT=89
    BOOLLIT=90
    STRINGLIT=91
    RAW_STRING=92
    INTERPRETED_STRING=93
    ESCAPED_CHAR=94
    RUNELIT=95
    ID=96
    COMMENT=97
    BLOCK_COMMENT=98
    WS=99
    ERROR_CHAR=100
    ILLEGAL_ESCAPE=101
    UNCLOSE_STRING=102

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

        def packageDecl(self):
            return self.getTypedRuleContext(MiniGoParser.PackageDeclContext,0)


        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def importDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ImportDeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ImportDeclContext,i)


        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.packageDecl()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__2:
                self.state = 109
                self.importDecl()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 115
                self.decl()
                self.state = 118 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__9) | (1 << MiniGoParser.T__10))) != 0)):
                    break

            self.state = 120
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PackageDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_packageDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPackageDecl" ):
                return visitor.visitPackageDecl(self)
            else:
                return visitor.visitChildren(self)




    def packageDecl(self):

        localctx = MiniGoParser.PackageDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_packageDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(MiniGoParser.T__0)
            self.state = 123
            self.match(MiniGoParser.ID)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 124
                self.match(MiniGoParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def importSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ImportSpecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ImportSpecContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_importDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportDecl" ):
                return visitor.visitImportDecl(self)
            else:
                return visitor.visitChildren(self)




    def importDecl(self):

        localctx = MiniGoParser.ImportDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_importDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self.match(MiniGoParser.T__2)
            self.state = 137
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.STRINGLIT]:
                self.state = 128
                self.match(MiniGoParser.STRINGLIT)
                pass
            elif token in [MiniGoParser.T__3]:
                self.state = 129
                self.match(MiniGoParser.T__3)
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 130
                    self.importSpec()
                    self.state = 133 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==MiniGoParser.STRINGLIT):
                        break

                self.state = 135
                self.match(MiniGoParser.T__4)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 139
                self.match(MiniGoParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_importSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportSpec" ):
                return visitor.visitImportSpec(self)
            else:
                return visitor.visitChildren(self)




    def importSpec(self):

        localctx = MiniGoParser.ImportSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_importSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(MiniGoParser.STRINGLIT)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__1:
                self.state = 143
                self.match(MiniGoParser.T__1)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def typedecl(self):
            return self.getTypedRuleContext(MiniGoParser.TypedeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 149
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.funcdecl()
                pass
            elif token in [MiniGoParser.T__5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 147
                self.vardecl()
                pass
            elif token in [MiniGoParser.T__9]:
                self.enterOuterAlt(localctx, 3)
                self.state = 148
                self.typedecl()
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def idlist(self):
            return self.getTypedRuleContext(MiniGoParser.IdlistContext,0)


        def typespec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypespecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypespecContext,i)


        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MiniGoParser.T__5)
            self.state = 177
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 152
                self.idlist()
                self.state = 153
                self.typespec()
                self.state = 154
                self.match(MiniGoParser.T__1)
                pass

            elif la_ == 2:
                self.state = 156
                self.idlist()
                self.state = 157
                self.typespec()
                self.state = 158
                self.match(MiniGoParser.T__6)
                self.state = 159
                self.exprlist()
                self.state = 160
                self.match(MiniGoParser.T__1)
                pass

            elif la_ == 3:
                self.state = 162
                self.match(MiniGoParser.T__3)
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.ID:
                    self.state = 163
                    self.match(MiniGoParser.ID)
                    self.state = 164
                    self.typespec()
                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.T__6:
                        self.state = 165
                        self.match(MiniGoParser.T__6)
                        self.state = 166
                        self.expr(0)


                    self.state = 169
                    self.match(MiniGoParser.T__1)
                    self.state = 175
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 176
                self.match(MiniGoParser.T__4)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ShortVardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_shortVardecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShortVardecl" ):
                return visitor.visitShortVardecl(self)
            else:
                return visitor.visitChildren(self)




    def shortVardecl(self):

        localctx = MiniGoParser.ShortVardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_shortVardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.match(MiniGoParser.ID)
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 180
                self.match(MiniGoParser.T__7)
                self.state = 181
                self.match(MiniGoParser.ID)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 187
            self.match(MiniGoParser.T__8)
            self.state = 188
            self.exprlist()
            self.state = 189
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typespec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypespecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypespecContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typedecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypedecl" ):
                return visitor.visitTypedecl(self)
            else:
                return visitor.visitChildren(self)




    def typedecl(self):

        localctx = MiniGoParser.TypedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_typedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.match(MiniGoParser.T__9)
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.state = 192
                self.match(MiniGoParser.ID)
                self.state = 193
                self.typespec()
                self.state = 194
                self.match(MiniGoParser.T__1)
                pass
            elif token in [MiniGoParser.T__3]:
                self.state = 196
                self.match(MiniGoParser.T__3)
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.ID:
                    self.state = 197
                    self.match(MiniGoParser.ID)
                    self.state = 198
                    self.typespec()
                    self.state = 199
                    self.match(MiniGoParser.T__1)
                    self.state = 205
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 206
                self.match(MiniGoParser.T__4)
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


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockstmtContext,0)


        def paramlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamlistContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamlistContext,i)


        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.T__10)
            self.state = 210
            self.match(MiniGoParser.ID)
            self.state = 211
            self.match(MiniGoParser.T__3)
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                self.state = 212
                self.paramlist()


            self.state = 215
            self.match(MiniGoParser.T__4)
            self.state = 222
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__10, MiniGoParser.T__11, MiniGoParser.T__13, MiniGoParser.T__14, MiniGoParser.T__15, MiniGoParser.T__16, MiniGoParser.T__17, MiniGoParser.T__18, MiniGoParser.T__19, MiniGoParser.T__20, MiniGoParser.T__21, MiniGoParser.T__22, MiniGoParser.T__23, MiniGoParser.T__24, MiniGoParser.T__25, MiniGoParser.T__26, MiniGoParser.T__27, MiniGoParser.T__28, MiniGoParser.T__29, MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__35, MiniGoParser.T__36]:
                self.state = 216
                self.typespec()
                pass
            elif token in [MiniGoParser.T__3]:
                self.state = 217
                self.match(MiniGoParser.T__3)
                self.state = 219
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                    self.state = 218
                    self.paramlist()


                self.state = 221
                self.match(MiniGoParser.T__4)
                pass
            elif token in [MiniGoParser.T__33]:
                pass
            else:
                pass
            self.state = 224
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def blockstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockstmtContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def result(self):
            return self.getTypedRuleContext(MiniGoParser.ResultContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodDecl" ):
                return visitor.visitMethodDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodDecl(self):

        localctx = MiniGoParser.MethodDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_methodDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(MiniGoParser.T__10)
            self.state = 227
            self.match(MiniGoParser.T__3)
            self.state = 228
            self.receiver()
            self.state = 229
            self.match(MiniGoParser.T__4)
            self.state = 230
            self.match(MiniGoParser.ID)
            self.state = 231
            self.match(MiniGoParser.T__3)
            self.state = 233
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                self.state = 232
                self.paramlist()


            self.state = 235
            self.match(MiniGoParser.T__4)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0):
                self.state = 236
                self.result()


            self.state = 239
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(MiniGoParser.ID)
            self.state = 254
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__10, MiniGoParser.T__11, MiniGoParser.T__13, MiniGoParser.T__14, MiniGoParser.T__15, MiniGoParser.T__16, MiniGoParser.T__17, MiniGoParser.T__18, MiniGoParser.T__19, MiniGoParser.T__20, MiniGoParser.T__21, MiniGoParser.T__22, MiniGoParser.T__23, MiniGoParser.T__24, MiniGoParser.T__25, MiniGoParser.T__26, MiniGoParser.T__27, MiniGoParser.T__28, MiniGoParser.T__29, MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__35, MiniGoParser.T__36]:
                self.state = 243
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 242
                    self.match(MiniGoParser.T__11)


                self.state = 245
                self.typespec()
                pass
            elif token in [MiniGoParser.T__3]:
                self.state = 246
                self.match(MiniGoParser.T__3)
                self.state = 247
                self.match(MiniGoParser.ID)
                self.state = 249
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 248
                    self.match(MiniGoParser.T__11)


                self.state = 251
                self.typespec()
                self.state = 252
                self.match(MiniGoParser.T__4)
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


    class ResultContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_result

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitResult" ):
                return visitor.visitResult(self)
            else:
                return visitor.visitChildren(self)




    def result(self):

        localctx = MiniGoParser.ResultContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_result)
        self._la = 0 # Token type
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__10, MiniGoParser.T__11, MiniGoParser.T__13, MiniGoParser.T__14, MiniGoParser.T__15, MiniGoParser.T__16, MiniGoParser.T__17, MiniGoParser.T__18, MiniGoParser.T__19, MiniGoParser.T__20, MiniGoParser.T__21, MiniGoParser.T__22, MiniGoParser.T__23, MiniGoParser.T__24, MiniGoParser.T__25, MiniGoParser.T__26, MiniGoParser.T__27, MiniGoParser.T__28, MiniGoParser.T__29, MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__35, MiniGoParser.T__36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 256
                self.typespec()
                pass
            elif token in [MiniGoParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                self.match(MiniGoParser.T__3)
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                    self.state = 258
                    self.paramlist()


                self.state = 261
                self.match(MiniGoParser.T__4)
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


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.param()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 265
                self.match(MiniGoParser.T__7)
                self.state = 266
                self.param()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_param)
        try:
            self.state = 278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 272
                self.match(MiniGoParser.ID)
                self.state = 273
                self.typespec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 274
                self.typespec()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 275
                self.match(MiniGoParser.ID)
                self.state = 276
                self.match(MiniGoParser.T__12)
                self.state = 277
                self.typespec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypespecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitiveType(self):
            return self.getTypedRuleContext(MiniGoParser.PrimitiveTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def sliceType(self):
            return self.getTypedRuleContext(MiniGoParser.SliceTypeContext,0)


        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def pointerType(self):
            return self.getTypedRuleContext(MiniGoParser.PointerTypeContext,0)


        def functionType(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionTypeContext,0)


        def interfaceType(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceTypeContext,0)


        def mapType(self):
            return self.getTypedRuleContext(MiniGoParser.MapTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typespec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypespec" ):
                return visitor.visitTypespec(self)
            else:
                return visitor.visitChildren(self)




    def typespec(self):

        localctx = MiniGoParser.TypespecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_typespec)
        try:
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.primitiveType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.sliceType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.structType()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.pointerType()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.functionType()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 286
                self.interfaceType()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 287
                self.mapType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimitiveTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_primitiveType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitiveType" ):
                return visitor.visitPrimitiveType(self)
            else:
                return visitor.visitChildren(self)




    def primitiveType(self):

        localctx = MiniGoParser.PrimitiveTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_primitiveType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29))) != 0)):
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


    class ArrayTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrayType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayType" ):
                return visitor.visitArrayType(self)
            else:
                return visitor.visitChildren(self)




    def arrayType(self):

        localctx = MiniGoParser.ArrayTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.match(MiniGoParser.T__30)
            self.state = 293
            self.expr(0)
            self.state = 294
            self.match(MiniGoParser.T__31)
            self.state = 295
            self.typespec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_sliceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSliceType" ):
                return visitor.visitSliceType(self)
            else:
                return visitor.visitChildren(self)




    def sliceType(self):

        localctx = MiniGoParser.SliceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_sliceType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.T__30)
            self.state = 298
            self.match(MiniGoParser.T__31)
            self.state = 299
            self.typespec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typespec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypespecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypespecContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructType" ):
                return visitor.visitStructType(self)
            else:
                return visitor.visitChildren(self)




    def structType(self):

        localctx = MiniGoParser.StructTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_structType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(MiniGoParser.T__32)
            self.state = 302
            self.match(MiniGoParser.T__33)
            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 303
                self.match(MiniGoParser.ID)
                self.state = 304
                self.typespec()
                self.state = 305
                self.match(MiniGoParser.T__1)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 312
            self.match(MiniGoParser.T__34)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointerTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_pointerType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointerType" ):
                return visitor.visitPointerType(self)
            else:
                return visitor.visitChildren(self)




    def pointerType(self):

        localctx = MiniGoParser.PointerTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_pointerType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(MiniGoParser.T__11)
            self.state = 315
            self.typespec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamlistContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamlistContext,i)


        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functionType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionType" ):
                return visitor.visitFunctionType(self)
            else:
                return visitor.visitChildren(self)




    def functionType(self):

        localctx = MiniGoParser.FunctionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_functionType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.match(MiniGoParser.T__10)
            self.state = 318
            self.match(MiniGoParser.T__3)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                self.state = 319
                self.paramlist()


            self.state = 322
            self.match(MiniGoParser.T__4)
            self.state = 329
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 323
                self.typespec()

            elif la_ == 2:
                self.state = 324
                self.match(MiniGoParser.T__3)
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                    self.state = 325
                    self.paramlist()


                self.state = 328
                self.match(MiniGoParser.T__4)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def paramlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamlistContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamlistContext,i)


        def typespec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypespecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypespecContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceType" ):
                return visitor.visitInterfaceType(self)
            else:
                return visitor.visitChildren(self)




    def interfaceType(self):

        localctx = MiniGoParser.InterfaceTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_interfaceType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.T__35)
            self.state = 332
            self.match(MiniGoParser.T__33)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 333
                self.match(MiniGoParser.ID)
                self.state = 334
                self.match(MiniGoParser.T__3)
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                    self.state = 335
                    self.paramlist()


                self.state = 338
                self.match(MiniGoParser.T__4)
                self.state = 345
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.T__10, MiniGoParser.T__11, MiniGoParser.T__13, MiniGoParser.T__14, MiniGoParser.T__15, MiniGoParser.T__16, MiniGoParser.T__17, MiniGoParser.T__18, MiniGoParser.T__19, MiniGoParser.T__20, MiniGoParser.T__21, MiniGoParser.T__22, MiniGoParser.T__23, MiniGoParser.T__24, MiniGoParser.T__25, MiniGoParser.T__26, MiniGoParser.T__27, MiniGoParser.T__28, MiniGoParser.T__29, MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__35, MiniGoParser.T__36]:
                    self.state = 339
                    self.typespec()
                    pass
                elif token in [MiniGoParser.T__3]:
                    self.state = 340
                    self.match(MiniGoParser.T__3)
                    self.state = 342
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                        self.state = 341
                        self.paramlist()


                    self.state = 344
                    self.match(MiniGoParser.T__4)
                    pass
                elif token in [MiniGoParser.T__1]:
                    pass
                else:
                    pass
                self.state = 347
                self.match(MiniGoParser.T__1)
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 353
            self.match(MiniGoParser.T__34)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.TypespecContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.TypespecContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_mapType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapType" ):
                return visitor.visitMapType(self)
            else:
                return visitor.visitChildren(self)




    def mapType(self):

        localctx = MiniGoParser.MapTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_mapType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(MiniGoParser.T__36)
            self.state = 356
            self.match(MiniGoParser.T__30)
            self.state = 357
            self.typespec()
            self.state = 358
            self.match(MiniGoParser.T__31)
            self.state = 359
            self.typespec()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStmt(self):
            return self.getTypedRuleContext(MiniGoParser.SimpleStmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def switchstmt(self):
            return self.getTypedRuleContext(MiniGoParser.SwitchstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmtContext,0)


        def gostmt(self):
            return self.getTypedRuleContext(MiniGoParser.GostmtContext,0)


        def deferstmt(self):
            return self.getTypedRuleContext(MiniGoParser.DeferstmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_stmt)
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__3, MiniGoParser.T__10, MiniGoParser.T__11, MiniGoParser.T__13, MiniGoParser.T__14, MiniGoParser.T__15, MiniGoParser.T__16, MiniGoParser.T__17, MiniGoParser.T__18, MiniGoParser.T__19, MiniGoParser.T__20, MiniGoParser.T__21, MiniGoParser.T__22, MiniGoParser.T__23, MiniGoParser.T__24, MiniGoParser.T__25, MiniGoParser.T__26, MiniGoParser.T__27, MiniGoParser.T__28, MiniGoParser.T__29, MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__35, MiniGoParser.T__36, MiniGoParser.T__58, MiniGoParser.T__59, MiniGoParser.T__60, MiniGoParser.T__61, MiniGoParser.T__62, MiniGoParser.T__63, MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT, MiniGoParser.RUNELIT, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.simpleStmt()
                self.state = 362
                self.match(MiniGoParser.T__1)
                pass
            elif token in [MiniGoParser.T__44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 364
                self.ifstmt()
                pass
            elif token in [MiniGoParser.T__46]:
                self.enterOuterAlt(localctx, 3)
                self.state = 365
                self.forstmt()
                pass
            elif token in [MiniGoParser.T__48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 366
                self.switchstmt()
                pass
            elif token in [MiniGoParser.T__33]:
                self.enterOuterAlt(localctx, 5)
                self.state = 367
                self.blockstmt()
                pass
            elif token in [MiniGoParser.T__54]:
                self.enterOuterAlt(localctx, 6)
                self.state = 368
                self.returnstmt()
                pass
            elif token in [MiniGoParser.T__55]:
                self.enterOuterAlt(localctx, 7)
                self.state = 369
                self.breakstmt()
                pass
            elif token in [MiniGoParser.T__56]:
                self.enterOuterAlt(localctx, 8)
                self.state = 370
                self.continuestmt()
                pass
            elif token in [MiniGoParser.T__52]:
                self.enterOuterAlt(localctx, 9)
                self.state = 371
                self.gostmt()
                pass
            elif token in [MiniGoParser.T__53]:
                self.enterOuterAlt(localctx, 10)
                self.state = 372
                self.deferstmt()
                pass
            elif token in [MiniGoParser.T__5]:
                self.enterOuterAlt(localctx, 11)
                self.state = 373
                self.vardecl()
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


    class SimpleStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def shortVardecl(self):
            return self.getTypedRuleContext(MiniGoParser.ShortVardeclContext,0)


        def incDecStmt(self):
            return self.getTypedRuleContext(MiniGoParser.IncDecStmtContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(MiniGoParser.ExprStmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_simpleStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimpleStmt" ):
                return visitor.visitSimpleStmt(self)
            else:
                return visitor.visitChildren(self)




    def simpleStmt(self):

        localctx = MiniGoParser.SimpleStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_simpleStmt)
        try:
            self.state = 380
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 376
                self.assignstmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.shortVardecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.incDecStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 379
                self.exprStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.lhs()
            self.state = 383
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__6) | (1 << MiniGoParser.T__37) | (1 << MiniGoParser.T__38) | (1 << MiniGoParser.T__39) | (1 << MiniGoParser.T__40) | (1 << MiniGoParser.T__41))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 384
            self.exprlist()
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

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_lhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.exprlist()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = MiniGoParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 388
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncDecStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_incDecStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncDecStmt" ):
                return visitor.visitIncDecStmt(self)
            else:
                return visitor.visitChildren(self)




    def incDecStmt(self):

        localctx = MiniGoParser.IncDecStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_incDecStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.expr(0)
            self.state = 391
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__42 or _la==MiniGoParser.T__43):
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


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def blockstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.BlockstmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.BlockstmtContext,i)


        def simpleStmt(self):
            return self.getTypedRuleContext(MiniGoParser.SimpleStmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(MiniGoParser.T__44)
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 394
                self.simpleStmt()
                self.state = 395
                self.match(MiniGoParser.T__1)


            self.state = 399
            self.expr(0)
            self.state = 400
            self.blockstmt()
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.T__45:
                self.state = 401
                self.match(MiniGoParser.T__45)
                self.state = 404
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [MiniGoParser.T__44]:
                    self.state = 402
                    self.ifstmt()
                    pass
                elif token in [MiniGoParser.T__33]:
                    self.state = 403
                    self.blockstmt()
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


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockstmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def simpleStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.SimpleStmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.SimpleStmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_forstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.match(MiniGoParser.T__46)
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                pass

            elif la_ == 2:
                pass

            elif la_ == 3:
                self.state = 411
                self.expr(0)
                pass

            elif la_ == 4:
                self.state = 413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                    self.state = 412
                    self.simpleStmt()


                self.state = 415
                self.match(MiniGoParser.T__1)
                self.state = 417
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                    self.state = 416
                    self.expr(0)


                self.state = 419
                self.match(MiniGoParser.T__1)
                self.state = 421
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                    self.state = 420
                    self.simpleStmt()


                pass

            elif la_ == 5:
                self.state = 423
                self.match(MiniGoParser.ID)
                self.state = 428
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.T__7:
                    self.state = 424
                    self.match(MiniGoParser.T__7)
                    self.state = 425
                    self.match(MiniGoParser.ID)
                    self.state = 430
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 431
                self.match(MiniGoParser.T__8)
                self.state = 432
                self.match(MiniGoParser.T__47)
                self.state = 433
                self.expr(0)
                pass


            self.state = 436
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simpleStmt(self):
            return self.getTypedRuleContext(MiniGoParser.SimpleStmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def caseclause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.CaseclauseContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.CaseclauseContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_switchstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchstmt" ):
                return visitor.visitSwitchstmt(self)
            else:
                return visitor.visitChildren(self)




    def switchstmt(self):

        localctx = MiniGoParser.SwitchstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_switchstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 438
            self.match(MiniGoParser.T__48)
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 439
                self.simpleStmt()
                self.state = 440
                self.match(MiniGoParser.T__1)


            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                self.state = 444
                self.expr(0)


            self.state = 447
            self.match(MiniGoParser.T__33)
            self.state = 451
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__49 or _la==MiniGoParser.T__50:
                self.state = 448
                self.caseclause()
                self.state = 453
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 454
            self.match(MiniGoParser.T__34)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseclauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_caseclause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseclause" ):
                return visitor.visitCaseclause(self)
            else:
                return visitor.visitChildren(self)




    def caseclause(self):

        localctx = MiniGoParser.CaseclauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_caseclause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__49]:
                self.state = 456
                self.match(MiniGoParser.T__49)
                self.state = 457
                self.exprlist()
                pass
            elif token in [MiniGoParser.T__50]:
                self.state = 458
                self.match(MiniGoParser.T__50)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 461
            self.match(MiniGoParser.T__51)
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__33) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__44) | (1 << MiniGoParser.T__46) | (1 << MiniGoParser.T__48) | (1 << MiniGoParser.T__52) | (1 << MiniGoParser.T__53) | (1 << MiniGoParser.T__54) | (1 << MiniGoParser.T__55) | (1 << MiniGoParser.T__56) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                self.state = 462
                self.stmt()
                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_blockstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockstmt" ):
                return visitor.visitBlockstmt(self)
            else:
                return visitor.visitChildren(self)




    def blockstmt(self):

        localctx = MiniGoParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.match(MiniGoParser.T__33)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__33) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__44) | (1 << MiniGoParser.T__46) | (1 << MiniGoParser.T__48) | (1 << MiniGoParser.T__52) | (1 << MiniGoParser.T__53) | (1 << MiniGoParser.T__54) | (1 << MiniGoParser.T__55) | (1 << MiniGoParser.T__56) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                self.state = 469
                self.stmt()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 475
            self.match(MiniGoParser.T__34)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GostmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_gostmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGostmt" ):
                return visitor.visitGostmt(self)
            else:
                return visitor.visitChildren(self)




    def gostmt(self):

        localctx = MiniGoParser.GostmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_gostmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(MiniGoParser.T__52)
            self.state = 478
            self.expr(0)
            self.state = 479
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeferstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_deferstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeferstmt" ):
                return visitor.visitDeferstmt(self)
            else:
                return visitor.visitChildren(self)




    def deferstmt(self):

        localctx = MiniGoParser.DeferstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_deferstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(MiniGoParser.T__53)
            self.state = 482
            self.expr(0)
            self.state = 483
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(MiniGoParser.T__54)
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                self.state = 486
                self.exprlist()


            self.state = 489
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_breakstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 491
            self.match(MiniGoParser.T__55)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 492
                self.match(MiniGoParser.ID)


            self.state = 495
            self.match(MiniGoParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_continuestmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(MiniGoParser.T__56)
            self.state = 499
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 498
                self.match(MiniGoParser.ID)


            self.state = 501
            self.match(MiniGoParser.T__1)
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

        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def unaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryExprContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def binaryOp(self):
            return self.getTypedRuleContext(MiniGoParser.BinaryOpContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 504
                self.primaryExpr(0)
                pass

            elif la_ == 2:
                self.state = 505
                self.unaryExpr()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 520
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 518
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 508
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 509
                        self.binaryOp()
                        self.state = 510
                        self.expr(3)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 512
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 513
                        self.match(MiniGoParser.T__57)
                        self.state = 514
                        self.expr(0)
                        self.state = 515
                        self.match(MiniGoParser.T__51)
                        self.state = 516
                        self.expr(2)
                        pass

             
                self.state = 522
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class UnaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryOp(self):
            return self.getTypedRuleContext(MiniGoParser.UnaryOpContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpr" ):
                return visitor.visitUnaryExpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryExpr(self):

        localctx = MiniGoParser.UnaryExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_unaryExpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.unaryOp()
            self.state = 524
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_unaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = MiniGoParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            _la = self._input.LA(1)
            if not(((((_la - 12)) & ~0x3f) == 0 and ((1 << (_la - 12)) & ((1 << (MiniGoParser.T__11 - 12)) | (1 << (MiniGoParser.T__58 - 12)) | (1 << (MiniGoParser.T__59 - 12)) | (1 << (MiniGoParser.T__60 - 12)) | (1 << (MiniGoParser.T__61 - 12)) | (1 << (MiniGoParser.T__62 - 12)) | (1 << (MiniGoParser.T__63 - 12)))) != 0)):
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


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MiniGoParser.RULE_binaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = MiniGoParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (MiniGoParser.T__64 - 65)) | (1 << (MiniGoParser.T__65 - 65)) | (1 << (MiniGoParser.T__66 - 65)) | (1 << (MiniGoParser.T__67 - 65)) | (1 << (MiniGoParser.T__68 - 65)) | (1 << (MiniGoParser.T__69 - 65)) | (1 << (MiniGoParser.T__70 - 65)) | (1 << (MiniGoParser.T__71 - 65)) | (1 << (MiniGoParser.T__72 - 65)) | (1 << (MiniGoParser.T__73 - 65)) | (1 << (MiniGoParser.T__74 - 65)) | (1 << (MiniGoParser.T__75 - 65)) | (1 << (MiniGoParser.T__76 - 65)) | (1 << (MiniGoParser.T__77 - 65)))) != 0)):
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


    class PrimaryExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def conversion(self):
            return self.getTypedRuleContext(MiniGoParser.ConversionContext,0)


        def primaryExpr(self):
            return self.getTypedRuleContext(MiniGoParser.PrimaryExprContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_primaryExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpr" ):
                return visitor.visitPrimaryExpr(self)
            else:
                return visitor.visitChildren(self)



    def primaryExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.PrimaryExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_primaryExpr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 533
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.state = 531
                self.operand()
                pass

            elif la_ == 2:
                self.state = 532
                self.conversion()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 561
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 559
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 535
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 536
                        self.match(MiniGoParser.T__78)
                        self.state = 537
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 538
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 539
                        self.match(MiniGoParser.T__30)
                        self.state = 540
                        self.expr(0)
                        self.state = 541
                        self.match(MiniGoParser.T__31)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 543
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 544
                        self.match(MiniGoParser.T__30)
                        self.state = 546
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                            self.state = 545
                            self.expr(0)


                        self.state = 548
                        self.match(MiniGoParser.T__51)
                        self.state = 550
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                            self.state = 549
                            self.expr(0)


                        self.state = 552
                        self.match(MiniGoParser.T__31)
                        pass

                    elif la_ == 4:
                        localctx = MiniGoParser.PrimaryExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_primaryExpr)
                        self.state = 553
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 554
                        self.match(MiniGoParser.T__3)
                        self.state = 556
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__3) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36) | (1 << MiniGoParser.T__58) | (1 << MiniGoParser.T__59) | (1 << MiniGoParser.T__60) | (1 << MiniGoParser.T__61) | (1 << MiniGoParser.T__62))) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & ((1 << (MiniGoParser.T__63 - 64)) | (1 << (MiniGoParser.INTLIT - 64)) | (1 << (MiniGoParser.FLOATLIT - 64)) | (1 << (MiniGoParser.BOOLLIT - 64)) | (1 << (MiniGoParser.STRINGLIT - 64)) | (1 << (MiniGoParser.RUNELIT - 64)) | (1 << (MiniGoParser.ID - 64)))) != 0):
                            self.state = 555
                            self.exprlist()


                        self.state = 558
                        self.match(MiniGoParser.T__4)
                        pass

             
                self.state = 563
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def basicLit(self):
            return self.getTypedRuleContext(MiniGoParser.BasicLitContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def functionLit(self):
            return self.getTypedRuleContext(MiniGoParser.FunctionLitContext,0)


        def compositeLit(self):
            return self.getTypedRuleContext(MiniGoParser.CompositeLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_operand)
        try:
            self.state = 572
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 564
                self.match(MiniGoParser.ID)
                pass
            elif token in [MiniGoParser.INTLIT, MiniGoParser.FLOATLIT, MiniGoParser.BOOLLIT, MiniGoParser.STRINGLIT, MiniGoParser.RUNELIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 565
                self.basicLit()
                pass
            elif token in [MiniGoParser.T__3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 566
                self.match(MiniGoParser.T__3)
                self.state = 567
                self.expr(0)
                self.state = 568
                self.match(MiniGoParser.T__4)
                pass
            elif token in [MiniGoParser.T__10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 570
                self.functionLit()
                pass
            elif token in [MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__36]:
                self.enterOuterAlt(localctx, 5)
                self.state = 571
                self.compositeLit()
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


    class BasicLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRINGLIT(self):
            return self.getToken(MiniGoParser.STRINGLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def RUNELIT(self):
            return self.getToken(MiniGoParser.RUNELIT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basicLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasicLit" ):
                return visitor.visitBasicLit(self)
            else:
                return visitor.visitChildren(self)




    def basicLit(self):

        localctx = MiniGoParser.BasicLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_basicLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 574
            _la = self._input.LA(1)
            if not(((((_la - 80)) & ~0x3f) == 0 and ((1 << (_la - 80)) & ((1 << (MiniGoParser.INTLIT - 80)) | (1 << (MiniGoParser.FLOATLIT - 80)) | (1 << (MiniGoParser.BOOLLIT - 80)) | (1 << (MiniGoParser.STRINGLIT - 80)) | (1 << (MiniGoParser.RUNELIT - 80)))) != 0)):
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


    class FunctionLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BlockstmtContext,0)


        def paramlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamlistContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamlistContext,i)


        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_functionLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionLit" ):
                return visitor.visitFunctionLit(self)
            else:
                return visitor.visitChildren(self)




    def functionLit(self):

        localctx = MiniGoParser.FunctionLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_functionLit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(MiniGoParser.T__10)
            self.state = 577
            self.match(MiniGoParser.T__3)
            self.state = 579
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                self.state = 578
                self.paramlist()


            self.state = 581
            self.match(MiniGoParser.T__4)
            self.state = 588
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.T__10, MiniGoParser.T__11, MiniGoParser.T__13, MiniGoParser.T__14, MiniGoParser.T__15, MiniGoParser.T__16, MiniGoParser.T__17, MiniGoParser.T__18, MiniGoParser.T__19, MiniGoParser.T__20, MiniGoParser.T__21, MiniGoParser.T__22, MiniGoParser.T__23, MiniGoParser.T__24, MiniGoParser.T__25, MiniGoParser.T__26, MiniGoParser.T__27, MiniGoParser.T__28, MiniGoParser.T__29, MiniGoParser.T__30, MiniGoParser.T__32, MiniGoParser.T__35, MiniGoParser.T__36]:
                self.state = 582
                self.typespec()
                pass
            elif token in [MiniGoParser.T__3]:
                self.state = 583
                self.match(MiniGoParser.T__3)
                self.state = 585
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__10) | (1 << MiniGoParser.T__11) | (1 << MiniGoParser.T__13) | (1 << MiniGoParser.T__14) | (1 << MiniGoParser.T__15) | (1 << MiniGoParser.T__16) | (1 << MiniGoParser.T__17) | (1 << MiniGoParser.T__18) | (1 << MiniGoParser.T__19) | (1 << MiniGoParser.T__20) | (1 << MiniGoParser.T__21) | (1 << MiniGoParser.T__22) | (1 << MiniGoParser.T__23) | (1 << MiniGoParser.T__24) | (1 << MiniGoParser.T__25) | (1 << MiniGoParser.T__26) | (1 << MiniGoParser.T__27) | (1 << MiniGoParser.T__28) | (1 << MiniGoParser.T__29) | (1 << MiniGoParser.T__30) | (1 << MiniGoParser.T__32) | (1 << MiniGoParser.T__35) | (1 << MiniGoParser.T__36))) != 0) or _la==MiniGoParser.ID:
                    self.state = 584
                    self.paramlist()


                self.state = 587
                self.match(MiniGoParser.T__4)
                pass
            elif token in [MiniGoParser.T__33]:
                pass
            else:
                pass
            self.state = 590
            self.blockstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompositeLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalType(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralTypeContext,0)


        def keyValList(self):
            return self.getTypedRuleContext(MiniGoParser.KeyValListContext,0)


        def exprlist(self):
            return self.getTypedRuleContext(MiniGoParser.ExprlistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_compositeLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompositeLit" ):
                return visitor.visitCompositeLit(self)
            else:
                return visitor.visitChildren(self)




    def compositeLit(self):

        localctx = MiniGoParser.CompositeLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_compositeLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 592
            self.literalType()
            self.state = 593
            self.match(MiniGoParser.T__33)
            self.state = 596
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 594
                self.keyValList()

            elif la_ == 2:
                self.state = 595
                self.exprlist()


            self.state = 598
            self.match(MiniGoParser.T__34)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structType(self):
            return self.getTypedRuleContext(MiniGoParser.StructTypeContext,0)


        def arrayType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrayTypeContext,0)


        def sliceType(self):
            return self.getTypedRuleContext(MiniGoParser.SliceTypeContext,0)


        def mapType(self):
            return self.getTypedRuleContext(MiniGoParser.MapTypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literalType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralType" ):
                return visitor.visitLiteralType(self)
            else:
                return visitor.visitChildren(self)




    def literalType(self):

        localctx = MiniGoParser.LiteralTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_literalType)
        try:
            self.state = 604
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.structType()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.arrayType()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 602
                self.sliceType()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 603
                self.mapType()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyVal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.KeyValContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.KeyValContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyValList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyValList" ):
                return visitor.visitKeyValList(self)
            else:
                return visitor.visitChildren(self)




    def keyValList(self):

        localctx = MiniGoParser.KeyValListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_keyValList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.keyVal()
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 607
                self.match(MiniGoParser.T__7)
                self.state = 608
                self.keyVal()
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KeyValContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_keyVal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeyVal" ):
                return visitor.visitKeyVal(self)
            else:
                return visitor.visitChildren(self)




    def keyVal(self):

        localctx = MiniGoParser.KeyValContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_keyVal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
            if la_ == 1:
                self.state = 614
                self.expr(0)
                self.state = 615
                self.match(MiniGoParser.T__51)


            self.state = 619
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConversionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typespec(self):
            return self.getTypedRuleContext(MiniGoParser.TypespecContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_conversion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConversion" ):
                return visitor.visitConversion(self)
            else:
                return visitor.visitChildren(self)




    def conversion(self):

        localctx = MiniGoParser.ConversionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_conversion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 621
            self.typespec()
            self.state = 622
            self.match(MiniGoParser.T__3)
            self.state = 623
            self.expr(0)
            self.state = 624
            self.match(MiniGoParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprlist" ):
                return visitor.visitExprlist(self)
            else:
                return visitor.visitChildren(self)




    def exprlist(self):

        localctx = MiniGoParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.expr(0)
            self.state = 631
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 627
                self.match(MiniGoParser.T__7)
                self.state = 628
                self.expr(0)
                self.state = 633
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_idlist

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdlist" ):
                return visitor.visitIdlist(self)
            else:
                return visitor.visitChildren(self)




    def idlist(self):

        localctx = MiniGoParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 634
            self.match(MiniGoParser.ID)
            self.state = 639
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.T__7:
                self.state = 635
                self.match(MiniGoParser.T__7)
                self.state = 636
                self.match(MiniGoParser.ID)
                self.state = 641
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self._predicates[39] = self.expr_sempred
        self._predicates[43] = self.primaryExpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         

    def primaryExpr_sempred(self, localctx:PrimaryExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




