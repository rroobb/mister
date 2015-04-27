# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
import sys
from antlr4 import *
from cubo_semantico import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .misterListener import misterListener
else:
    from misterListener import misterListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\63")
        buf.write("\u0216\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\3\2\3\2\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00a0\n\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5\u00ad\n\5\3\6\3\6")
        buf.write("\3\6\5\6\u00b2\n\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00ba\n")
        buf.write("\b\3\t\3\t\3\t\3\n\3\n\3\n\5\n\u00c2\n\n\3\13\3\13\3\13")
        buf.write("\3\f\3\f\3\f\5\f\u00ca\n\f\3\r\3\r\5\r\u00ce\n\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00da")
        buf.write("\n\17\3\20\3\20\3\20\3\21\3\21\5\21\u00e1\n\21\3\22\3")
        buf.write("\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\25\5\25\u00f3\n\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\3\26\5\26\u00fb\n\26\3\27\3\27\5\27\u00ff\n\27")
        buf.write("\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u010a")
        buf.write("\n\31\3\32\3\32\5\32\u010e\n\32\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\33\5\33\u0116\n\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\35\3\35\3\35\3\35\5\35\u0123\n\35\3\36\3\36\3")
        buf.write("\36\3\36\5\36\u0129\n\36\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u0130\n\37\3 \3 \3 \3!\3!\3!\3!\5!\u0139\n!\3\"\3\"\3")
        buf.write("#\3#\3#\3#\3#\3#\3#\3#\5#\u0145\n#\3$\3$\3$\3%\3%\3&\3")
        buf.write("&\3&\3&\5&\u0150\n&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3")
        buf.write("(\3(\5(\u015e\n(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\5*\u016b")
        buf.write("\n*\3+\3+\3+\3+\3+\5+\u0172\n+\3,\3,\3,\5,\u0177\n,\3")
        buf.write("-\3-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0185\n.\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\5/\u018f\n/\3\60\3\60\3\61\3\61\3\61")
        buf.write("\3\62\3\62\3\62\5\62\u0199\n\62\3\63\3\63\3\63\5\63\u019e")
        buf.write("\n\63\3\64\3\64\3\64\5\64\u01a3\n\64\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\3\66\3\66\5\66\u01ad\n\66\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\38\38\38\58\u01b9\n8\39\39\39\39")
        buf.write("\39\3:\3:\3:\3:\5:\u01c4\n:\3;\3;\3;\3;\3;\3;\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3=\3=\3=\3=\3=\5=\u01d8\n=\3>\3>\3>\3>\3")
        buf.write(">\3>\3?\3?\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\5@\u01ec\n@\3")
        buf.write("A\3A\5A\u01f0\nA\3B\3B\5B\u01f4\nB\3C\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3E\3E\3F\3F\5F\u0202\nF\3G\3G\3G\3G\3H\3H\3H\3H\3")
        buf.write("H\3H\3I\3I\5I\u0210\nI\3J\3J\5J\u0214\nJ\3J\2\2K\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084")
        buf.write("\u0086\u0088\u008a\u008c\u008e\u0090\u0092\2\7\3\2\n\f")
        buf.write("\4\2\27\27\31\31\4\2\32\32!%\3\2\35\36\3\2\24\25\u0202")
        buf.write("\2\u0094\3\2\2\2\4\u009f\3\2\2\2\6\u00a1\3\2\2\2\b\u00ac")
        buf.write("\3\2\2\2\n\u00b1\3\2\2\2\f\u00b3\3\2\2\2\16\u00b9\3\2")
        buf.write("\2\2\20\u00bb\3\2\2\2\22\u00c1\3\2\2\2\24\u00c3\3\2\2")
        buf.write("\2\26\u00c9\3\2\2\2\30\u00cd\3\2\2\2\32\u00cf\3\2\2\2")
        buf.write("\34\u00d9\3\2\2\2\36\u00db\3\2\2\2 \u00e0\3\2\2\2\"\u00e2")
        buf.write("\3\2\2\2$\u00e4\3\2\2\2&\u00e8\3\2\2\2(\u00f2\3\2\2\2")
        buf.write("*\u00fa\3\2\2\2,\u00fe\3\2\2\2.\u0100\3\2\2\2\60\u0109")
        buf.write("\3\2\2\2\62\u010d\3\2\2\2\64\u0115\3\2\2\2\66\u0117\3")
        buf.write("\2\2\28\u0122\3\2\2\2:\u0128\3\2\2\2<\u012f\3\2\2\2>\u0131")
        buf.write("\3\2\2\2@\u0138\3\2\2\2B\u013a\3\2\2\2D\u0144\3\2\2\2")
        buf.write("F\u0146\3\2\2\2H\u0149\3\2\2\2J\u014f\3\2\2\2L\u0151\3")
        buf.write("\2\2\2N\u015d\3\2\2\2P\u015f\3\2\2\2R\u016a\3\2\2\2T\u0171")
        buf.write("\3\2\2\2V\u0176\3\2\2\2X\u0178\3\2\2\2Z\u0184\3\2\2\2")
        buf.write("\\\u018e\3\2\2\2^\u0190\3\2\2\2`\u0192\3\2\2\2b\u0198")
        buf.write("\3\2\2\2d\u019d\3\2\2\2f\u01a2\3\2\2\2h\u01a4\3\2\2\2")
        buf.write("j\u01ac\3\2\2\2l\u01ae\3\2\2\2n\u01b8\3\2\2\2p\u01ba\3")
        buf.write("\2\2\2r\u01c3\3\2\2\2t\u01c5\3\2\2\2v\u01cb\3\2\2\2x\u01d7")
        buf.write("\3\2\2\2z\u01d9\3\2\2\2|\u01df\3\2\2\2~\u01eb\3\2\2\2")
        buf.write("\u0080\u01ef\3\2\2\2\u0082\u01f3\3\2\2\2\u0084\u01f5\3")
        buf.write("\2\2\2\u0086\u01f9\3\2\2\2\u0088\u01fd\3\2\2\2\u008a\u0201")
        buf.write("\3\2\2\2\u008c\u0203\3\2\2\2\u008e\u0207\3\2\2\2\u0090")
        buf.write("\u020f\3\2\2\2\u0092\u0213\3\2\2\2\u0094\u0095\5\4\3\2")
        buf.write("\u0095\u0096\5\6\4\2\u0096\u0097\7\2\2\3\u0097\3\3\2\2")
        buf.write("\2\u0098\u0099\5\20\t\2\u0099\u009a\5\4\3\2\u009a\u00a0")
        buf.write("\3\2\2\2\u009b\u009c\5|?\2\u009c\u009d\5\4\3\2\u009d\u00a0")
        buf.write("\3\2\2\2\u009e\u00a0\3\2\2\2\u009f\u0098\3\2\2\2\u009f")
        buf.write("\u009b\3\2\2\2\u009f\u009e\3\2\2\2\u00a0\5\3\2\2\2\u00a1")
        buf.write("\u00a2\7\t\2\2\u00a2\u00a3\5\b\5\2\u00a3\7\3\2\2\2\u00a4")
        buf.write("\u00a5\7\n\2\2\u00a5\u00ad\5\n\6\2\u00a6\u00a7\7\13\2")
        buf.write("\2\u00a7\u00ad\5\f\7\2\u00a8\u00a9\7\f\2\2\u00a9\u00ad")
        buf.write("\5\f\7\2\u00aa\u00ab\7\23\2\2\u00ab\u00ad\5\f\7\2\u00ac")
        buf.write("\u00a4\3\2\2\2\u00ac\u00a6\3\2\2\2\u00ac\u00a8\3\2\2\2")
        buf.write("\u00ac\u00aa\3\2\2\2\u00ad\t\3\2\2\2\u00ae\u00af\7\3\2")
        buf.write("\2\u00af\u00b2\5\66\34\2\u00b0\u00b2\5\f\7\2\u00b1\u00ae")
        buf.write("\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\13\3\2\2\2\u00b3\u00b4")
        buf.write("\7/\2\2\u00b4\u00b5\5\66\34\2\u00b5\u00b6\5\6\4\2\u00b6")
        buf.write("\r\3\2\2\2\u00b7\u00ba\5\"\22\2\u00b8\u00ba\7\23\2\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00b8\3\2\2\2\u00ba\17\3\2\2\2\u00bb")
        buf.write("\u00bc\5\22\n\2\u00bc\u00bd\5\24\13\2\u00bd\21\3\2\2\2")
        buf.write("\u00be\u00c2\7/\2\2\u00bf\u00c2\5\"\22\2\u00c0\u00c2\5")
        buf.write("$\23\2\u00c1\u00be\3\2\2\2\u00c1\u00bf\3\2\2\2\u00c1\u00c0")
        buf.write("\3\2\2\2\u00c2\23\3\2\2\2\u00c3\u00c4\5\32\16\2\u00c4")
        buf.write("\u00c5\7,\2\2\u00c5\25\3\2\2\2\u00c6\u00c7\7\33\2\2\u00c7")
        buf.write("\u00ca\5\30\r\2\u00c8\u00ca\3\2\2\2\u00c9\u00c6\3\2\2")
        buf.write("\2\u00c9\u00c8\3\2\2\2\u00ca\27\3\2\2\2\u00cb\u00ce\5")
        buf.write("> \2\u00cc\u00ce\5&\24\2\u00cd\u00cb\3\2\2\2\u00cd\u00cc")
        buf.write("\3\2\2\2\u00ce\31\3\2\2\2\u00cf\u00d0\7/\2\2\u00d0\u00d1")
        buf.write("\5\26\f\2\u00d1\u00d2\5\34\17\2\u00d2\33\3\2\2\2\u00d3")
        buf.write("\u00d4\7\34\2\2\u00d4\u00d5\7/\2\2\u00d5\u00d6\5\26\f")
        buf.write("\2\u00d6\u00d7\5\34\17\2\u00d7\u00da\3\2\2\2\u00d8\u00da")
        buf.write("\3\2\2\2\u00d9\u00d3\3\2\2\2\u00d9\u00d8\3\2\2\2\u00da")
        buf.write("\35\3\2\2\2\u00db\u00dc\5 \21\2\u00dc\u00dd\5\24\13\2")
        buf.write("\u00dd\37\3\2\2\2\u00de\u00e1\5\"\22\2\u00df\u00e1\5$")
        buf.write("\23\2\u00e0\u00de\3\2\2\2\u00e0\u00df\3\2\2\2\u00e1!\3")
        buf.write("\2\2\2\u00e2\u00e3\t\2\2\2\u00e3#\3\2\2\2\u00e4\u00e5")
        buf.write("\7\16\2\2\u00e5\u00e6\5\"\22\2\u00e6\u00e7\7\60\2\2\u00e7")
        buf.write("%\3\2\2\2\u00e8\u00e9\7*\2\2\u00e9\u00ea\5*\26\2\u00ea")
        buf.write("\u00eb\5(\25\2\u00eb\u00ec\7+\2\2\u00ec\'\3\2\2\2\u00ed")
        buf.write("\u00ee\7\34\2\2\u00ee\u00ef\5*\26\2\u00ef\u00f0\5(\25")
        buf.write("\2\u00f0\u00f3\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00ed")
        buf.write("\3\2\2\2\u00f2\u00f1\3\2\2\2\u00f3)\3\2\2\2\u00f4\u00fb")
        buf.write("\7\60\2\2\u00f5\u00fb\7\61\2\2\u00f6\u00f7\5`\61\2\u00f7")
        buf.write("\u00f8\5,\27\2\u00f8\u00fb\3\2\2\2\u00f9\u00fb\7\62\2")
        buf.write("\2\u00fa\u00f4\3\2\2\2\u00fa\u00f5\3\2\2\2\u00fa\u00f6")
        buf.write("\3\2\2\2\u00fa\u00f9\3\2\2\2\u00fb+\3\2\2\2\u00fc\u00ff")
        buf.write("\5P)\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff-\3\2\2\2\u0100\u0101\7&\2\2\u0101\u0102")
        buf.write("\5\60\31\2\u0102\u0103\7\'\2\2\u0103/\3\2\2\2\u0104\u0105")
        buf.write("\5\62\32\2\u0105\u0106\7/\2\2\u0106\u0107\5\64\33\2\u0107")
        buf.write("\u010a\3\2\2\2\u0108\u010a\3\2\2\2\u0109\u0104\3\2\2\2")
        buf.write("\u0109\u0108\3\2\2\2\u010a\61\3\2\2\2\u010b\u010e\5\"")
        buf.write("\22\2\u010c\u010e\5$\23\2\u010d\u010b\3\2\2\2\u010d\u010c")
        buf.write("\3\2\2\2\u010e\63\3\2\2\2\u010f\u0110\7\34\2\2\u0110\u0111")
        buf.write("\5\62\32\2\u0111\u0112\7/\2\2\u0112\u0113\5\64\33\2\u0113")
        buf.write("\u0116\3\2\2\2\u0114\u0116\3\2\2\2\u0115\u010f\3\2\2\2")
        buf.write("\u0115\u0114\3\2\2\2\u0116\65\3\2\2\2\u0117\u0118\5.\30")
        buf.write("\2\u0118\u0119\7(\2\2\u0119\u011a\58\35\2\u011a\u011b")
        buf.write("\5:\36\2\u011b\u011c\5<\37\2\u011c\u011d\7)\2\2\u011d")
        buf.write("\67\3\2\2\2\u011e\u011f\5\20\t\2\u011f\u0120\58\35\2\u0120")
        buf.write("\u0123\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u011e\3\2\2\2")
        buf.write("\u0122\u0121\3\2\2\2\u01239\3\2\2\2\u0124\u0125\5D#\2")
        buf.write("\u0125\u0126\5:\36\2\u0126\u0129\3\2\2\2\u0127\u0129\3")
        buf.write("\2\2\2\u0128\u0124\3\2\2\2\u0128\u0127\3\2\2\2\u0129;")
        buf.write("\3\2\2\2\u012a\u012b\7\r\2\2\u012b\u012c\5> \2\u012c\u012d")
        buf.write("\7,\2\2\u012d\u0130\3\2\2\2\u012e\u0130\3\2\2\2\u012f")
        buf.write("\u012a\3\2\2\2\u012f\u012e\3\2\2\2\u0130=\3\2\2\2\u0131")
        buf.write("\u0132\5F$\2\u0132\u0133\5@!\2\u0133?\3\2\2\2\u0134\u0135")
        buf.write("\5B\"\2\u0135\u0136\5> \2\u0136\u0139\3\2\2\2\u0137\u0139")
        buf.write("\3\2\2\2\u0138\u0134\3\2\2\2\u0138\u0137\3\2\2\2\u0139")
        buf.write("A\3\2\2\2\u013a\u013b\t\3\2\2\u013bC\3\2\2\2\u013c\u0145")
        buf.write("\5h\65\2\u013d\u0145\5l\67\2\u013e\u013f\5> \2\u013f\u0140")
        buf.write("\7,\2\2\u0140\u0145\3\2\2\2\u0141\u0145\5v<\2\u0142\u0145")
        buf.write("\5t;\2\u0143\u0145\5z>\2\u0144\u013c\3\2\2\2\u0144\u013d")
        buf.write("\3\2\2\2\u0144\u013e\3\2\2\2\u0144\u0141\3\2\2\2\u0144")
        buf.write("\u0142\3\2\2\2\u0144\u0143\3\2\2\2\u0145E\3\2\2\2\u0146")
        buf.write("\u0147\5L\'\2\u0147\u0148\5J&\2\u0148G\3\2\2\2\u0149\u014a")
        buf.write("\t\4\2\2\u014aI\3\2\2\2\u014b\u014c\5H%\2\u014c\u014d")
        buf.write("\5L\'\2\u014d\u0150\3\2\2\2\u014e\u0150\3\2\2\2\u014f")
        buf.write("\u014b\3\2\2\2\u014f\u014e\3\2\2\2\u0150K\3\2\2\2\u0151")
        buf.write("\u0152\5X-\2\u0152\u0153\5N(\2\u0153M\3\2\2\2\u0154\u0155")
        buf.write("\7\35\2\2\u0155\u0156\5X-\2\u0156\u0157\5N(\2\u0157\u015e")
        buf.write("\3\2\2\2\u0158\u0159\7\36\2\2\u0159\u015a\5X-\2\u015a")
        buf.write("\u015b\5N(\2\u015b\u015e\3\2\2\2\u015c\u015e\3\2\2\2\u015d")
        buf.write("\u0154\3\2\2\2\u015d\u0158\3\2\2\2\u015d\u015c\3\2\2\2")
        buf.write("\u015eO\3\2\2\2\u015f\u0160\7&\2\2\u0160\u0161\5R*\2\u0161")
        buf.write("\u0162\7\'\2\2\u0162Q\3\2\2\2\u0163\u0164\5> \2\u0164")
        buf.write("\u0165\5T+\2\u0165\u016b\3\2\2\2\u0166\u0167\7\30\2\2")
        buf.write("\u0167\u0168\7/\2\2\u0168\u016b\5T+\2\u0169\u016b\3\2")
        buf.write("\2\2\u016a\u0163\3\2\2\2\u016a\u0166\3\2\2\2\u016a\u0169")
        buf.write("\3\2\2\2\u016bS\3\2\2\2\u016c\u016d\7\34\2\2\u016d\u016e")
        buf.write("\5V,\2\u016e\u016f\5T+\2\u016f\u0172\3\2\2\2\u0170\u0172")
        buf.write("\3\2\2\2\u0171\u016c\3\2\2\2\u0171\u0170\3\2\2\2\u0172")
        buf.write("U\3\2\2\2\u0173\u0177\5> \2\u0174\u0175\7\30\2\2\u0175")
        buf.write("\u0177\7/\2\2\u0176\u0173\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0177W\3\2\2\2\u0178\u0179\5\\/\2\u0179\u017a\5Z.\2\u017a")
        buf.write("Y\3\2\2\2\u017b\u017c\7 \2\2\u017c\u017d\5\\/\2\u017d")
        buf.write("\u017e\5Z.\2\u017e\u0185\3\2\2\2\u017f\u0180\7\37\2\2")
        buf.write("\u0180\u0181\5\\/\2\u0181\u0182\5Z.\2\u0182\u0185\3\2")
        buf.write("\2\2\u0183\u0185\3\2\2\2\u0184\u017b\3\2\2\2\u0184\u017f")
        buf.write("\3\2\2\2\u0184\u0183\3\2\2\2\u0185[\3\2\2\2\u0186\u0187")
        buf.write("\7&\2\2\u0187\u0188\5> \2\u0188\u0189\7\'\2\2\u0189\u018f")
        buf.write("\3\2\2\2\u018a\u018f\5*\26\2\u018b\u018c\5^\60\2\u018c")
        buf.write("\u018d\5*\26\2\u018d\u018f\3\2\2\2\u018e\u0186\3\2\2\2")
        buf.write("\u018e\u018a\3\2\2\2\u018e\u018b\3\2\2\2\u018f]\3\2\2")
        buf.write("\2\u0190\u0191\t\5\2\2\u0191_\3\2\2\2\u0192\u0193\7/\2")
        buf.write("\2\u0193\u0194\5b\62\2\u0194a\3\2\2\2\u0195\u0196\7.\2")
        buf.write("\2\u0196\u0199\5d\63\2\u0197\u0199\3\2\2\2\u0198\u0195")
        buf.write("\3\2\2\2\u0198\u0197\3\2\2\2\u0199c\3\2\2\2\u019a\u019b")
        buf.write("\7/\2\2\u019b\u019e\5f\64\2\u019c\u019e\7\60\2\2\u019d")
        buf.write("\u019a\3\2\2\2\u019d\u019c\3\2\2\2\u019ee\3\2\2\2\u019f")
        buf.write("\u01a0\7.\2\2\u01a0\u01a3\7\60\2\2\u01a1\u01a3\3\2\2\2")
        buf.write("\u01a2\u019f\3\2\2\2\u01a2\u01a1\3\2\2\2\u01a3g\3\2\2")
        buf.write("\2\u01a4\u01a5\7\26\2\2\u01a5\u01a6\5`\61\2\u01a6\u01a7")
        buf.write("\7\33\2\2\u01a7\u01a8\5j\66\2\u01a8\u01a9\7,\2\2\u01a9")
        buf.write("i\3\2\2\2\u01aa\u01ad\5> \2\u01ab\u01ad\5&\24\2\u01ac")
        buf.write("\u01aa\3\2\2\2\u01ac\u01ab\3\2\2\2\u01adk\3\2\2\2\u01ae")
        buf.write("\u01af\7\4\2\2\u01af\u01b0\7&\2\2\u01b0\u01b1\5> \2\u01b1")
        buf.write("\u01b2\7\'\2\2\u01b2\u01b3\5p9\2\u01b3\u01b4\5n8\2\u01b4")
        buf.write("m\3\2\2\2\u01b5\u01b6\7\5\2\2\u01b6\u01b9\5p9\2\u01b7")
        buf.write("\u01b9\3\2\2\2\u01b8\u01b5\3\2\2\2\u01b8\u01b7\3\2\2\2")
        buf.write("\u01b9o\3\2\2\2\u01ba\u01bb\7(\2\2\u01bb\u01bc\5D#\2\u01bc")
        buf.write("\u01bd\5r:\2\u01bd\u01be\7)\2\2\u01beq\3\2\2\2\u01bf\u01c0")
        buf.write("\5D#\2\u01c0\u01c1\5r:\2\u01c1\u01c4\3\2\2\2\u01c2\u01c4")
        buf.write("\3\2\2\2\u01c3\u01bf\3\2\2\2\u01c3\u01c2\3\2\2\2\u01c4")
        buf.write("s\3\2\2\2\u01c5\u01c6\7\6\2\2\u01c6\u01c7\7&\2\2\u01c7")
        buf.write("\u01c8\5> \2\u01c8\u01c9\7\'\2\2\u01c9\u01ca\5p9\2\u01ca")
        buf.write("u\3\2\2\2\u01cb\u01cc\7\b\2\2\u01cc\u01cd\7&\2\2\u01cd")
        buf.write("\u01ce\5> \2\u01ce\u01cf\5x=\2\u01cf\u01d0\7\'\2\2\u01d0")
        buf.write("\u01d1\7,\2\2\u01d1w\3\2\2\2\u01d2\u01d3\7\34\2\2\u01d3")
        buf.write("\u01d4\5> \2\u01d4\u01d5\5x=\2\u01d5\u01d8\3\2\2\2\u01d6")
        buf.write("\u01d8\3\2\2\2\u01d7\u01d2\3\2\2\2\u01d7\u01d6\3\2\2\2")
        buf.write("\u01d8y\3\2\2\2\u01d9\u01da\7\7\2\2\u01da\u01db\7&\2\2")
        buf.write("\u01db\u01dc\7/\2\2\u01dc\u01dd\7\'\2\2\u01dd\u01de\7")
        buf.write(",\2\2\u01de{\3\2\2\2\u01df\u01e0\7\17\2\2\u01e0\u01e1")
        buf.write("\7/\2\2\u01e1\u01e2\5~@\2\u01e2\u01e3\7(\2\2\u01e3\u01e4")
        buf.write("\5\u0080A\2\u01e4\u01e5\5\u0082B\2\u01e5\u01e6\7)\2\2")
        buf.write("\u01e6\u01e7\7,\2\2\u01e7}\3\2\2\2\u01e8\u01e9\7\22\2")
        buf.write("\2\u01e9\u01ec\7/\2\2\u01ea\u01ec\3\2\2\2\u01eb\u01e8")
        buf.write("\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\177\3\2\2\2\u01ed\u01f0")
        buf.write("\5\u0084C\2\u01ee\u01f0\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef")
        buf.write("\u01ee\3\2\2\2\u01f0\u0081\3\2\2\2\u01f1\u01f4\5\u008c")
        buf.write("G\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f2")
        buf.write("\3\2\2\2\u01f4\u0083\3\2\2\2\u01f5\u01f6\7\20\2\2\u01f6")
        buf.write("\u01f7\7-\2\2\u01f7\u01f8\5\u0086D\2\u01f8\u0085\3\2\2")
        buf.write("\2\u01f9\u01fa\5\u0088E\2\u01fa\u01fb\5\36\20\2\u01fb")
        buf.write("\u01fc\5\u008aF\2\u01fc\u0087\3\2\2\2\u01fd\u01fe\t\6")
        buf.write("\2\2\u01fe\u0089\3\2\2\2\u01ff\u0202\5\u0086D\2\u0200")
        buf.write("\u0202\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0200\3\2\2\2")
        buf.write("\u0202\u008b\3\2\2\2\u0203\u0204\7\21\2\2\u0204\u0205")
        buf.write("\7-\2\2\u0205\u0206\5\u008eH\2\u0206\u008d\3\2\2\2\u0207")
        buf.write("\u0208\7\t\2\2\u0208\u0209\5\u0090I\2\u0209\u020a\7/\2")
        buf.write("\2\u020a\u020b\5\66\34\2\u020b\u020c\5\u0092J\2\u020c")
        buf.write("\u008f\3\2\2\2\u020d\u0210\5\"\22\2\u020e\u0210\7\23\2")
        buf.write("\2\u020f\u020d\3\2\2\2\u020f\u020e\3\2\2\2\u0210\u0091")
        buf.write("\3\2\2\2\u0211\u0214\5\u008eH\2\u0212\u0214\3\2\2\2\u0213")
        buf.write("\u0211\3\2\2\2\u0213\u0212\3\2\2\2\u0214\u0093\3\2\2\2")
        buf.write("*\u009f\u00ac\u00b1\u00b9\u00c1\u00c9\u00cd\u00d9\u00e0")
        buf.write("\u00f2\u00fa\u00fe\u0109\u010d\u0115\u0122\u0128\u012f")
        buf.write("\u0138\u0144\u014f\u015d\u016a\u0171\u0176\u0184\u018e")
        buf.write("\u0198\u019d\u01a2\u01ac\u01b8\u01c3\u01d7\u01eb\u01ef")
        buf.write("\u01f3\u0201\u020f\u0213")
        return buf.getvalue()


class misterParser ( Parser ):
# 0 -> void, 1 -> entero, 2 -> decimal, 3 -> texto, 4 -> lista
    grammarFileName = "java-escape"

    AuxTipo = None

    AuxTipoVar = None

    AuxVisVar = None

    RetornoTipo = None

    AuxTipoLista = None

    AuxTamanioLista = 0

    funcionActual = None

    claseActual = None

    variableActual = None

    contAuxParametroActual = None

    stackParametros = []

    stackContParametros = []

    AuxPadre = None

    AuxLongLista = None

    dirPrincipal = {'global':[None, None, None, {}, None, None, None, None]}

    semanticaCompuestoAux = None

    semanticaCompuestoAux2 = None

    semanticaCompuestoAux3 = None

    terminacionProc = None #Auxiliar para saber si estas en una funcion o en el main

    pilaO = [] #Pila de operandos

    pOper = [] #Pila de operadores

    pTipos = [] #Pila de tipos de los operadores

    pSaltos = [] #Pila de saltos

    tipoOperando = None #Para los cuadruplos

    operando = None #Para los cuadruplos

    operador = None #Para los cuadruplos

    numeroParametro = [] #Para cuadruplo al llamar func

    numeroParametroEntero = [] #Para cuadruplo al llamar func

    numeroParametroDecimal = [] #Para cuadruplo al llamar func

    numeroParametroTexto = [] #Para cuadruplo al llamar func

    numeroDirParametroEntero = [] #Para cuadruplo al llamar func

    numeroDirParametroDecimal = [] #Para cuadruplo al llamar func

    numeroDirParametroTexto = [] #Para cuadruplo al llamar func

    asignacionRetorno = [] #Para funciones con retorno de variables

    cuboSem = cuboSemantico()

    quadList = [] #Cuadruplos

    quadOperadores = [['*','/'],['+','-'],['==','!=','>','>=','<','<='],['&&','||'],['=']]

    memGlobalEntero = -1 #Contador para memoria virtual de variables globales enteras

    memGlobalDecimal = 2999 #Contador para memoria virtual de variables globales decimales

    memGlobalTexto = 5999 #Contador para memoria virtual de variables globales texto

    memLocalEntero = 8999 #Contador para memoria virtual de variables locales y temporales enteras

    memLocalDecimal = 14999 #Contador para memoria virtual de variables locales y temporales decimales

    memLocalTexto = 20999 #Contador para memoria virtual de variables locales y temporales texto

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'INICIO'", u"'SI'", u"'SINO'", u"'MIENTRAS'", 
                     u"'LEER'", u"'IMPRIMIR'", u"'FUNCION'", u"'ENTERO'", 
                     u"'DECIMAL'", u"'TEXTO'", u"'RETORNAR'", u"'LISTA'", 
                     u"'CLASE'", u"'ATRIBUTOS'", u"'METODOS'", u"'HEREDA'", 
                     u"'NADA'", u"'PRIVADO'", u"'PUBLICO'", u"'ASIGNAR'", 
                     u"'&&'", u"'&'", u"'||'", u"'=='", u"'='", u"','", 
                     u"'+'", u"'-'", u"'/'", u"'*'", u"'!='", u"'>='", u"'<='", 
                     u"'<'", u"'>'", u"'('", u"')'", u"'{'", u"'}'", u"'['", 
                     u"']'", u"';'", u"':'", u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"INICIO", u"SI", u"SINO", u"MIENTRAS", 
                      u"LEER", u"IMPRIMIR", u"FUNCION", u"ENTERO", u"DECIMAL", 
                      u"TEXTO", u"RETORNAR", u"LISTA", u"CLASE", u"ATRIBUTOS", 
                      u"METODOS", u"HEREDA", u"NADA", u"PRIVADO", u"PUBLICO", 
                      u"ASIGNAR", u"Y", u"REFERENCIA", u"O", u"IDENTICO", 
                      u"IGUAL", u"COMA", u"SUMA", u"RESTA", u"DIVISION", 
                      u"MULTIPLICACION", u"DIFERENTE", u"MAYORIGUAL", u"MENORIGUAL", 
                      u"MENOR", u"MAYOR", u"PARENTESIS1", u"PARENTESIS2", 
                      u"LLAVE1", u"LLAVE2", u"CORCHETE1", u"CORCHETE2", 
                      u"PUNTOYCOMA", u"DOSPUNTOS", u"PUNTO", u"ID", u"CTENTERO", 
                      u"CTEDECIMAL", u"CTETEXTO", u"WS" ]

    RULE_programa = 0
    RULE_programaAux1 = 1
    RULE_programaAux3 = 2
    RULE_programaAux5 = 3
    RULE_programaAux6 = 4
    RULE_programaAux7 = 5
    RULE_programaAux4 = 6
    RULE_v_vars = 7
    RULE_varsAux1 = 8
    RULE_v_varsDefinicion = 9
    RULE_varsAux2 = 10
    RULE_varsAux3 = 11
    RULE_varsAux4 = 12
    RULE_varsAux5 = 13
    RULE_v_varsAtrib = 14
    RULE_varsAtribAux1 = 15
    RULE_tipo = 16
    RULE_l_list = 17
    RULE_cteL = 18
    RULE_cteLAux1 = 19
    RULE_valor = 20
    RULE_valorAux1 = 21
    RULE_parametros = 22
    RULE_parametrosAux1 = 23
    RULE_parametrosAux2 = 24
    RULE_parametrosAux3 = 25
    RULE_func = 26
    RULE_funcAux1 = 27
    RULE_funcAux2 = 28
    RULE_funcAux3 = 29
    RULE_expresion = 30
    RULE_expresionAux1 = 31
    RULE_expresionAux2 = 32
    RULE_estatuto = 33
    RULE_declaracion = 34
    RULE_declaracionAux1 = 35
    RULE_declaracionAux2 = 36
    RULE_exp = 37
    RULE_expAux1 = 38
    RULE_llamarFunc = 39
    RULE_llamarFuncAux1 = 40
    RULE_llamarFuncAux2 = 41
    RULE_llamarFuncAux3 = 42
    RULE_termino = 43
    RULE_terminoAux1 = 44
    RULE_factor = 45
    RULE_factorAux1 = 46
    RULE_compuesto = 47
    RULE_compuestoAux1 = 48
    RULE_compuestoAux3 = 49
    RULE_compuestoAux2 = 50
    RULE_asignacion = 51
    RULE_asignacionAux1 = 52
    RULE_condicion = 53
    RULE_condicionAux1 = 54
    RULE_bloque = 55
    RULE_bloqueAux1 = 56
    RULE_ciclo = 57
    RULE_escritura = 58
    RULE_escrituraAux1 = 59
    RULE_lectura = 60
    RULE_c_class = 61
    RULE_classAux1 = 62
    RULE_classAux2 = 63
    RULE_classAux3 = 64
    RULE_atrib = 65
    RULE_atribAux1 = 66
    RULE_atribAux2 = 67
    RULE_atribAux3 = 68
    RULE_metod = 69
    RULE_metodAux1 = 70
    RULE_metodAux2 = 71
    RULE_metodAux3 = 72

    ruleNames =  [ "programa", "programaAux1", "programaAux3", "programaAux5", 
                   "programaAux6", "programaAux7", "programaAux4", "v_vars", 
                   "varsAux1", "v_varsDefinicion", "varsAux2", "varsAux3", 
                   "varsAux4", "varsAux5", "v_varsAtrib", "varsAtribAux1", 
                   "tipo", "l_list", "cteL", "cteLAux1", "valor", "valorAux1", 
                   "parametros", "parametrosAux1", "parametrosAux2", "parametrosAux3", 
                   "func", "funcAux1", "funcAux2", "funcAux3", "expresion", 
                   "expresionAux1", "expresionAux2", "estatuto", "declaracion", 
                   "declaracionAux1", "declaracionAux2", "exp", "expAux1", 
                   "llamarFunc", "llamarFuncAux1", "llamarFuncAux2", "llamarFuncAux3", 
                   "termino", "terminoAux1", "factor", "factorAux1", "compuesto", 
                   "compuestoAux1", "compuestoAux3", "compuestoAux2", "asignacion", 
                   "asignacionAux1", "condicion", "condicionAux1", "bloque", 
                   "bloqueAux1", "ciclo", "escritura", "escrituraAux1", 
                   "lectura", "c_class", "classAux1", "classAux2", "classAux3", 
                   "atrib", "atribAux1", "atribAux2", "atribAux3", "metod", 
                   "metodAux1", "metodAux2", "metodAux3" ]

    EOF = Token.EOF
    INICIO=1
    SI=2
    SINO=3
    MIENTRAS=4
    LEER=5
    IMPRIMIR=6
    FUNCION=7
    ENTERO=8
    DECIMAL=9
    TEXTO=10
    RETORNAR=11
    LISTA=12
    CLASE=13
    ATRIBUTOS=14
    METODOS=15
    HEREDA=16
    NADA=17
    PRIVADO=18
    PUBLICO=19
    ASIGNAR=20
    Y=21
    REFERENCIA=22
    O=23
    IDENTICO=24
    IGUAL=25
    COMA=26
    SUMA=27
    RESTA=28
    DIVISION=29
    MULTIPLICACION=30
    DIFERENTE=31
    MAYORIGUAL=32
    MENORIGUAL=33
    MENOR=34
    MAYOR=35
    PARENTESIS1=36
    PARENTESIS2=37
    LLAVE1=38
    LLAVE2=39
    CORCHETE1=40
    CORCHETE2=41
    PUNTOYCOMA=42
    DOSPUNTOS=43
    PUNTO=44
    ID=45
    CTENTERO=46
    CTEDECIMAL=47
    CTETEXTO=48
    WS=49

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def programaAux1(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux1Context,0)


        def programaAux3(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux3Context,0)


        def EOF(self):
            return self.getToken(misterParser.EOF, 0)

        def getRuleIndex(self):
            return misterParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitPrograma(self)

    def insertarFunc(self):
        self.funcionActual = self.getCurrentToken().text
        if self.dirPrincipal.get(self.funcionActual) != None:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Funcion ya existente" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
            return
        if self.claseActual == None:
            self.dirPrincipal[self.funcionActual] = [self.AuxTipo, None, None, {}, [0,0,0,0], [], None, [0,0,0]]
        else:
            self.dirPrincipal[self.claseActual][1][self.funcionActual] = [self.AuxTipo, {}, [0,0,0,0], [], None, [0,0,0]]
        self.AuxTipo = None

    def insertarClase(self):
        if self.dirPrincipal.get(self.claseActual) != None:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Clase ya existente" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
            return
        self.dirPrincipal[self.claseActual] = [None, {}, self.AuxPadre, {}, None, None, None, [0,0,0]]
        self.AuxPadre = None

    def insertarVariable(self):
        direccion = None
        isClase = False
        isGlobal = False
        dicAtributos = {}

        #Variables globales
        if self.claseActual == None and self.funcionActual == None:
            if self.AuxTipoVar == "ENTERO":
                self.memGlobalEntero = self.memGlobalEntero + 1
                direccion = self.memGlobalEntero
            elif self.AuxTipoVar == "DECIMAL":
                self.memGlobalDecimal = self.memGlobalDecimal + 1
                direccion = self.memGlobalDecimal
            elif self.AuxTipoVar == "TEXTO":
                self.memGlobalTexto = self.memGlobalTexto + 1
                direccion = self.memGlobalTexto
            elif self.AuxTipoVar == "LISTA":
                if self.AuxTipoLista == "ENTERO":
                    self.memGlobalEntero = self.memGlobalEntero + 1
                    direccion = self.memGlobalEntero
                    self.memGlobalEntero = self.memGlobalEntero + int(self.AuxTamanioLista) - 1
                elif self.AuxTipoLista == "DECIMAL":
                    self.memGlobalDecimal = self.memGlobalDecimal + 1
                    direccion = self.memGlobalDecimal
                    self.memGlobalDecimal = self.memGlobalDecimal + int(self.AuxTamanioLista) - 1
                elif self.AuxTipoLista == "TEXTO":
                    self.memGlobalTexto = self.memGlobalTexto + 1
                    direccion = self.memGlobalTexto
                    self.memGlobalTexto = self.memGlobalTexto + int(self.AuxTamanioLista) - 1
            else:
                isClase = True
                isGlobal = True

        #Variables Locales
        if (self.claseActual == None and self.funcionActual != None) or (self.claseActual != None and self.funcionActual != None):
            if self.AuxTipoVar == "ENTERO":
                self.memLocalEntero = self.memLocalEntero + 1
                direccion = self.memLocalEntero
            elif self.AuxTipoVar == "DECIMAL":
                self.memLocalDecimal = self.memLocalDecimal + 1
                direccion = self.memLocalDecimal
            elif self.AuxTipoVar == "TEXTO":
                self.memLocalTexto = self.memLocalTexto + 1
                direccion = self.memLocalTexto
            elif self.AuxTipoVar == "LISTA":
                if self.AuxTipoLista == "ENTERO":
                    self.memLocalEntero = self.memLocalEntero + 1
                    direccion = self.memLocalEntero
                    self.memLocalEntero = self.memLocalEntero + int(self.AuxTamanioLista) - 1
                elif self.AuxTipoLista == "DECIMAL":
                    self.memLocalDecimal = self.memLocalDecimal + 1
                    direccion = self.memLocalDecimal
                    self.memLocalDecimal = self.memLocalDecimal + int(self.AuxTamanioLista) - 1
                elif self.AuxTipoLista == "TEXTO":
                    self.memLocalTexto = self.memLocalTexto + 1
                    direccion = self.memLocalTexto
                    self.memLocalTexto = self.memLocalTexto + int(self.AuxTamanioLista) - 1
            else:
                isClase = True
                

        tipo = None
        if self.AuxTipoLista == None and self.AuxTipoVar != "LISTA":
            tipo = self.AuxTipoVar
        else:
            tipo = self.AuxTipoVar + "," + self.AuxTipoLista + "," + self.AuxTamanioLista

        if isClase:
            NombrePadre = self.AuxTipoVar
            direccionAux = None
            if self.dirPrincipal.get(self.AuxTipoVar) == None:
                return
            while True:
                dictAux = self.dirPrincipal[NombrePadre][3]
                for key in dictAux.keys():

                    if dictAux[key][0] == "ENTERO":
                        if isGlobal:
                            self.memGlobalEntero = self.memGlobalEntero + 1
                            direccionAux = self.memGlobalEntero
                        else:
                            self.memLocalEntero = self.memLocalEntero + 1
                            direccionAux = self.memLocalEntero
                    elif dictAux[key][0] == "DECIMAL":
                        if isGlobal:
                            self.memGlobalDecimal = self.memGlobalDecimal + 1
                            direccionAux = self.memGlobalDecimal
                        else:
                            self.memLocalDecimal = self.memLocalDecimal + 1
                            direccionAux = self.memLocalDecimal
                    elif dictAux[key][0] == "TEXTO":
                        if isGlobal:
                            self.memGlobalTexto = self.memGlobalTexto + 1
                            direccionAux = self.memGlobalTexto
                        else:
                            self.memLocalTexto = self.memLocalTexto + 1
                            direccionAux = self.memLocalTexto
                    else:
                        dirTipoLista = dictAux[key][0].split(",")
                        if isGlobal:
                            if dirTipoLista[1] == "ENTERO":
                                self.memGlobalEntero = self.memGlobalEntero + 1
                                direccionAux = self.memGlobalEntero
                                self.memGlobalEntero = self.memGlobalEntero + int(dirTipoLista[2]) - 1
                            elif dirTipoLista[1] == "DECIMAL":
                                self.memGlobalDecimal = self.memGlobalDecimal + 1
                                direccionAux = self.memGlobalDecimal
                                self.memGlobalDecimal = self.memGlobalDecimal + int(dirTipoLista[2]) - 1
                            elif dirTipoLista[1] == "TEXTO":
                                self.memGlobalTexto = self.memGlobalTexto + 1
                                direccionAux = self.memGlobalTexto
                                self.memGlobalTexto = self.memGlobalTexto + int(dirTipoLista[2]) - 1
                        else:
                            if dirTipoLista[1] == "ENTERO":
                                self.memLocalEntero = self.memLocalEntero + 1
                                direccionAux = self.memLocalEntero
                                self.memLocalEntero = self.memLocalEntero + int(dirTipoLista[2]) - 1
                            elif dirTipoLista[1] == "DECIMAL":
                                self.memLocalDecimal = self.memLocalDecimal + 1
                                direccionAux = self.memLocalDecimal
                                self.memLocalDecimal = self.memLocalDecimal + int(dirTipoLista[2]) - 1
                            elif dirTipoLista[1] == "TEXTO":
                                self.memLocalTexto = self.memLocalTexto + 1
                                direccionAux = self.memLocalTexto
                                self.memLocalTexto = self.memLocalTexto + int(dirTipoLista[2]) - 1
                    dicAtributos[key] = [dictAux[key][0], dictAux[key][1], direccionAux]
                NombrePadre = self.dirPrincipal[NombrePadre][2]
                if NombrePadre == None:
                    break

        if self.claseActual == None:
            if self.funcionActual == None:
                if self.dirPrincipal['global'][3].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                self.dirPrincipal['global'][3][self.variableActual] = [tipo, direccion, dicAtributos]
            else:
                if self.dirPrincipal[self.funcionActual][3].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                self.dirPrincipal[self.funcionActual][3][self.variableActual] = [tipo, direccion, dicAtributos]
        else:
            if self.funcionActual == None:
                if self.dirPrincipal[self.claseActual][3].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                self.dirPrincipal[self.claseActual][3][self.variableActual] = [tipo, self.AuxVisVar, direccion, dicAtributos]
            else:
                if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                self.dirPrincipal[self.claseActual][1][self.funcionActual][1][self.variableActual] = [tipo, self.AuxVisVar, direccion, dicAtributos]
        self.variableActual = None

    def resetDireccionLocal(self):
        self.memLocalEntero = 8999
        self.memLocalDecimal = 14999
        self.memLocalTexto = 20999

    def checarId(self, variableId):
        if self.claseActual == None:
            if self.funcionActual == None:
                if self.dirPrincipal['global'][3].get(variableId) == None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
            else:
                if self.dirPrincipal[self.funcionActual][3].get(variableId) == None:
                    if self.dirPrincipal['global'][3].get(variableId) == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
        else:
            if self.funcionActual != None:
                if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(variableId) == None:
                    if self.dirPrincipal[self.claseActual][3].get(variableId) == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return

    def checarAtributo(self, atributoId):
        varAtributos = None
        if self.claseActual == None:
            if self.funcionActual == None:
                varAtributos = self.dirPrincipal['global'][3].get(self.semanticaCompuestoAux)
                if varAtributos == None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                varAtributos = varAtributos[2].get(atributoId)
                if varAtributos != None:
                    if varAtributos[1] == 'PRIVADO':
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al atributo" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                else:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Atributo no declarado" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return

            else:
                varAtributos = self.dirPrincipal[self.funcionActual][3].get(self.semanticaCompuestoAux)
                if varAtributos == None:
                    varAtributos = self.dirPrincipal['global'][3].get(self.semanticaCompuestoAux)
                    if varAtributos == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                varAtributos = varAtributos[2].get(atributoId)
                if varAtributos != None:
                    if varAtributos[1] == 'PRIVADO':
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al atributo" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                
                else:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Atributo no declarado" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return

        else:
            if self.funcionActual != None:
                varAtributos = self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(self.semanticaCompuestoAux)
                if varAtributos == None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                varAtributos = varAtributos[3].get(atributoId)
                if varAtributos != None:
                    if varAtributos[1] == 'PRIVADO':
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al atributo" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                else:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Atributo no declarado" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return

    def checarMetodo(self):
        if self.semanticaCompuestoAux2 == None:
            if self.claseActual == None:
                if self.dirPrincipal.get(self.semanticaCompuestoAux) == None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Funcion no declarada" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
            else:
                self.encontrarFuncionClase(self.claseActual)

        else:
            tipo = None
            if self.claseActual == None:
                if self.funcionActual == None:
                    tipo = self.dirPrincipal['global'][3].get(self.semanticaCompuestoAux)
                    if tipo == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                    tipo = tipo[0]
                    
                else:
                    tipo = self.dirPrincipal[self.funcionActual][3].get(self.semanticaCompuestoAux)
                    if tipo == None:
                        tipo = self.dirPrincipal['global'][3].get(self.semanticaCompuestoAux)
                        if tipo == None:
                            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                            self._syntaxErrors = self._syntaxErrors + 1
                            sys.exit()
                            return
                    tipo = tipo[0]
            
            else:
                if self.funcionActual == None:
                    tipo = self.dirPrincipal[self.claseActual][3].get(self.semanticaCompuestoAux)
                    if tipo == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                    tipo = tipo[0]

                else:
                    tipo = self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(self.semanticaCompuestoAux)
                    if tipo == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        sys.exit()
                        return
                    tipo = tipo[0]
                    
            self.encontrarFuncionClase(tipo)

    def encontrarFuncionClase(self, padre):
        if padre in ['ENTERO','DECIMAL','TEXTO','NADA', 'LISTA']:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al metodo" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
            return
        
        while True:
            dictAux = self.dirPrincipal[padre][1]
            value = dictAux.get(self.semanticaCompuestoAux2)
            if  value != None:
                return
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Funcion no declarada" )
        self._syntaxErrors = self._syntaxErrors + 1
        sys.exit()
        return

    def encontrarTipoFuncionClase(self, padre, funcion):
        while True:
            dictAux = self.dirPrincipal[padre][1]
            value = dictAux.get(funcion)
            if value != None:
                return value[0]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def encontrarTipoAtributoClase(self, padre, atributo):
        while True:
            dictAux = self.dirPrincipal[padre][3]
            value = dictAux.get(atributo)
            if value != None:
                return value[0]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def obtenerTipo(self, stringVariable):
        if stringVariable == None :
            return None
        listaAux = stringVariable.split(".")
        isInt = False
        if len(listaAux) == 2:
            isInt = True
            try:
                tempInt = int(listaAux[1])
            except ValueError:
                isInt = False
        if len(listaAux) == 1 or isInt:
            if listaAux[0].find("(") > 0:
                listaAux[0] = listaAux[0].replace("(", "")
                if self.claseActual == None:
                    if self.dirPrincipal.get(listaAux[0]):
                        return self.dirPrincipal[listaAux[0]][0]
                else:
                    return encontrarTipoFuncionClase(self.claseActual, listaAux[0])
            else:
                if self.claseActual == None:
                    if self.funcionActual == None:
                        if self.dirPrincipal["global"][3].get(listaAux[0]):
                            return self.dirPrincipal["global"][3][listaAux[0]][0]
                    else:
                        auxiliar = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                        if auxiliar != None:
                            return auxiliar[0]
                        else:
                            aux = self.dirPrincipal["global"][3].get(listaAux[0])
                            if aux != None:
                                return aux[0]
                            else:
                                return
                else:
                    if self.funcionActual == None:
                        if self.dirPrincipal[self.claseActual][3].get(listaAux[0]):
                            return self.dirPrincipal[self.claseActual][3][listaAux[0]][0]
                    else:
                        auxiliar = self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0])
                        if auxiliar != None:
                            return auxiliar[0]
                        else:
                            if self.dirPrincipal[self.claseActual][3].get(listaAux[0]):
                                return self.dirPrincipal[self.claseActual][3][listaAux[0]][0]
        else:
            if self.claseActual == None:
                if self.funcionActual == None:
                    if self.dirPrincipal['global'][3].get(listaAux[0]):
                        clase = self.dirPrincipal['global'][3][listaAux[0]][0]
                else:
                    clase = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                    if clase != None:
                        clase = clase[0]
                    else:
                        clase = self.dirPrincipal['global'][3].get(listaAux[0])
                        if clase != None:
                            clase = clase[0]
                        else:
                            return
            else:
                if self.funcionActual != None:
                    if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0]):
                        clase = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][0]

            if listaAux[1].find("(") > 0:
                return self.encontrarTipoFuncionClase(clase, listaAux[1].replace("(", ""))
            else:
                return self.encontrarTipoAtributoClase(clase, listaAux[1])

    def encontrarDireccionFuncionClase(self, padre, funcion):
        while True:
            dictAux = self.dirPrincipal[padre][1]
            value = dictAux.get(funcion)
            if value != None:
                return value[4]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def obtenerDireccionFuncion(self, stringFuncion):
        if stringFuncion == None:
            return None
        listaAux = stringFuncion.split(".")
        if len(listaAux) == 1:
            if listaAux[0].find("(") > 0:
                listaAux[0] = listaAux[0].replace("(", "")
                if self.claseActual == None:
                    if self.dirPrincipal.get(listaAux[0]):
                        return self.dirPrincipal[listaAux[0]][6]
                else:
                    return encontrarDireccionFuncionClase(self.claseActual, listaAux[0])
        else:
            if self.claseActual == None:
                if self.funcionActual == None:
                    if self.dirPrincipal['global'][3].get(listaAux[0]):
                        clase = self.dirPrincipal['global'][3][listaAux[0]][0]
                else:
                    clase = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                    if clase != None:
                        clase = clase[0]
                    else:
                        clase = self.dirPrincipal['global'][3].get(listaAux[0])
                        if clase != None:
                            clase = clase[0]
                        else:
                            return
            else:
                if self.funcionActual != None:
                    if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0]):
                        clase = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][0]

            if listaAux[1].find("(") > 0:
                return self.encontrarDireccionFuncionClase(clase, listaAux[1].replace("(", ""))

    def obtenerDireccionVariable(self, stringVariable):
        if stringVariable == None:
            return None
        listaAux = stringVariable.split(".")
        if len(listaAux) == 1:
            if listaAux[0].find("(") > 0:
                return None
            else:
                if self.claseActual == None:
                    if self.funcionActual == None:
                        if self.dirPrincipal["global"][3].get(listaAux[0]):
                            return self.dirPrincipal["global"][3][listaAux[0]][1]
                    else:
                        auxiliar = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                        if auxiliar != None:
                            return auxiliar[1]
                        else:
                            aux = self.dirPrincipal["global"][3].get(listaAux[0])
                            if aux != None:
                                return aux[1]
                            else:
                                return
                else:
                    if self.funcionActual == None:
                        if self.dirPrincipal[self.claseActual][3].get(listaAux[0]):
                            return self.dirPrincipal[self.claseActual][3][listaAux[0]][2]
                    else:
                        auxiliar = self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0])
                        if auxiliar != None:
                            return auxiliar[2]
                        else:
                            if self.dirPrincipal[self.claseActual][3].get(listaAux[0]):
                                return self.dirPrincipal[self.claseActual][3][listaAux[0]][2]
        else:
            if listaAux[1].find("(") > 0:
                return None

            if self.claseActual == None:
                if self.funcionActual == None:
                    if (self.dirPrincipal['global'][3].get(listaAux[0])) and (self.dirPrincipal['global'][3][listaAux[0]][2].get(listaAux[1])):
                        return self.dirPrincipal['global'][3][listaAux[0]][2][listaAux[1]][2]
                else:
                    clase = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                    if clase != None:
                        if clase[2].get(listaAux[1]):
                            return clase[2][listaAux[1]][2]
                    else:
                        if (self.dirPrincipal['global'][3].get(listaAux[0])) and (self.dirPrincipal['global'][3][listaAux[0]][2].get(listaAux[1])):
                            return self.dirPrincipal['global'][3][listaAux[0]][2][listaAux[1]][2]
            else:
                if self.funcionActual != None:
                    if (self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0])) and (self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][3].get(listaAux[1])):
                        return self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][3][listaAux[1]][2]

    def encontrarTamanioFuncionClase(self, padre, funcion):
        while True:
            dictAux = self.dirPrincipal[padre][1]
            value = dictAux.get(funcion)
            if value != None:
                return value[5]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def obtenerTamanioFuncion(self, stringFuncion):
        if stringFuncion == None:
            return None
        listaAux = stringFuncion.split(".")
        if len(listaAux) == 1:
            if listaAux[0].find("(") > 0:
                listaAux[0] = listaAux[0].replace("(", "")
                if self.claseActual == None:
                    if self.dirPrincipal.get(listaAux[0]):
                        return self.dirPrincipal[listaAux[0]][7]
                else:
                    return encontrarTamanioFuncionClase(self.claseActual, listaAux[0])
        else:
            if self.claseActual == None:
                if self.funcionActual == None:
                    if self.dirPrincipal['global'][3].get(listaAux[0]):
                        clase = self.dirPrincipal['global'][3][listaAux[0]][0]
                else:
                    clase = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                    if clase != None:
                        clase = clase[0]
                    else:
                        clase = self.dirPrincipal['global'][3].get(listaAux[0])
                        if clase != None:
                            clase = clase[0]
                        else:
                            return
            else:
                if self.funcionActual != None:
                    if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0]):
                        clase = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][0]

            if listaAux[1].find("(") > 0:
                return self.encontrarTamanioFuncionClase(clase, listaAux[1].replace("(", ""))

    def encontrarParametrosFuncionClase(self, padre, funcion):
        while True:
            dictAux = self.dirPrincipal[padre][1]
            value = dictAux.get(funcion)
            if value != None:
                return value[3]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def obtenerParametros(self, stringVariable):
        if stringVariable == None :
            return None
        listaAux = stringVariable.split(".")
        if len(listaAux) == 1:
            if listaAux[0].find("(") > 0:
                listaAux[0] = listaAux[0].replace("(", "")
                if self.claseActual == None:
                    if self.dirPrincipal.get(listaAux[0]):
                        return self.dirPrincipal[listaAux[0]][5]
                else:
                    return self.encontrarParametrosFuncionClase(self.claseActual, listaAux[0])
        else:
            if self.claseActual == None:
                if self.funcionActual == None:
                    if self.dirPrincipal['global'][3].get(listaAux[0]):
                        clase = self.dirPrincipal['global'][3][listaAux[0]][0]
                else:
                    clase = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                    if clase != None:
                        clase = clase[0]
                    else:
                        clase = self.dirPrincipal['global'][3].get(listaAux[0])
                        if clase == None:
                            return
                        clase = clase[0]
            else:
                if self.funcionActual != None:
                    if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0]):
                        clase = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][0]

            if listaAux[1].find("(") > 0:
                return self.encontrarParametrosFuncionClase(clase, listaAux[1].replace("(", ""))

    def encontrarDirParametroFuncionClase(self, padre, funcion, numParam):
        while True:
            dictAux = self.dirPrincipal[padre][1]
            value = dictAux.get(funcion)
            if value != None:
                return value[3][numParam]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def obtenerTipoDireccionParametro(self, stringVariable, numParam):
        if stringVariable == None :
            return None
        listaAux = stringVariable.split(".")
        if len(listaAux) == 1:
            if listaAux[0].find("(") > 0:
                listaAux[0] = listaAux[0].replace("(", "")
                if self.claseActual == None:
                    if self.dirPrincipal.get(listaAux[0]):
                        return self.dirPrincipal[listaAux[0]][5][numParam]
                else:
                    return self.encontrarDirParametroFuncionClase(self.claseActual, listaAux[0], numParam)
        else:
            if self.claseActual == None:
                if self.funcionActual == None:
                    if self.dirPrincipal['global'][3].get(listaAux[0]):
                        clase = self.dirPrincipal['global'][3][listaAux[0]][0]
                else:
                    clase = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                    if clase != None:
                        clase = clase[0]
                    else:
                        clase = self.dirPrincipal['global'][3].get(listaAux[0])
                        if clase == None:
                            return
                        clase = clase[0]
            else:
                if self.funcionActual != None:
                    if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0]):
                        clase = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][listaAux[0]][0]

            if listaAux[1].find("(") > 0:
                return self.encontrarDirParametroFuncionClase(clase, listaAux[1].replace("(", ""), numParam)

    def obtenerDireccionParametro(self, tipoDireccion):
        offset = 0
        tipoDireccion = tipoDireccion.split(',')
        if len(tipoDireccion) == 1:
            if tipoDireccion[0] == 'ENTERO':
                offset = self.numeroParametroEntero[len(self.numeroParametroEntero) - 1] + self.numeroDirParametroEntero[len(self.numeroDirParametroEntero) - 1]
                self.numeroParametroEntero[len(self.numeroParametroEntero) - 1] = self.numeroParametroEntero[len(self.numeroParametroEntero) - 1] + 1
                return 9000 + offset
            elif tipoDireccion[0] == 'DECIMAL':
                offset = self.numeroParametroDecimal[len(self.numeroParametroDecimal) - 1] + self.numeroDirParametroDecimal[len(self.numeroDirParametroDecimal) - 1]
                self.numeroParametroDecimal[len(self.numeroParametroDecimal) - 1] = self.numeroParametroDecimal[len(self.numeroParametroDecimal) - 1] + 1
                return 15000 + offset
            elif tipoDireccion[0] == 'TEXTO':
                offset = self.numeroParametroTexto[len(self.numeroParametroTexto) - 1] + self.numeroDirParametroTexto[len(self.numeroDirParametroTexto) - 1]
                self.numeroParametroTexto[len(self.numeroParametroTexto) - 1] = self.numeroParametroTexto[len(self.numeroParametroTexto) - 1] + 1
                return 21000 + offset
        else:
            if tipoDireccion[1] == 'ENTERO':
                offset = self.numeroParametroEntero[len(self.numeroParametroEntero) - 1] + self.numeroDirParametroEntero[len(self.numeroDirParametroEntero) - 1]
                self.numeroParametroEntero[len(self.numeroParametroEntero) - 1] = self.numeroParametroEntero[len(self.numeroParametroEntero) - 1] + 1
                self.numeroDirParametroEntero[len(self.numeroDirParametroEntero) - 1] = self.numeroDirParametroEntero[len(self.numeroDirParametroEntero) - 1] + int(tipoDireccion[2]) - 1
                return 9000 + offset
            elif tipoDireccion[1] == 'DECIMAL':
                offset = self.numeroParametroDecimal[len(self.numeroParametroDecimal) - 1] + self.numeroDirParametroDecimal[len(self.numeroDirParametroDecimal) - 1]
                self.numeroParametroDecimal[len(self.numeroParametroDecimal) - 1] = self.numeroParametroDecimal[len(self.numeroParametroDecimal) - 1] + 1
                self.numeroDirParametroDecimal[len(self.numeroDirParametroDecimal) - 1] = self.numeroDirParametroDecimal[len(self.numeroDirParametroDecimal) - 1] + int(tipoDireccion[2]) - 1
                return 15000 + offset
            elif tipoDireccion[1] == 'TEXTO':
                offset = self.numeroParametroTexto[len(self.numeroParametroTexto) - 1] + self.numeroDirParametroTexto[len(self.numeroDirParametroTexto) - 1]
                self.numeroParametroTexto[len(self.numeroParametroTexto) - 1] = self.numeroParametroTexto[len(self.numeroParametroTexto) - 1] + 1
                self.numeroDirParametroTexto[len(self.numeroDirParametroTexto) - 1] = self.numeroDirParametroTexto[len(self.numeroDirParametroTexto) - 1] + int(tipoDireccion[2]) - 1
                return 21000 + offset

        return -1

    def checarClase(self):
        if self.dirPrincipal.get(self.AuxTipoVar) == None:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Clase no declarada" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
            return

    def agregarParametro(self, tipo):
        if self.claseActual ==  None:
            dic = self.dirPrincipal[self.funcionActual]
            if tipo == "ENTERO":
                dic[5].append(tipo)
                dic[4][0] = dic[4][0] + 1
            elif tipo == "DECIMAL":
                dic[5].append(tipo)
                dic[4][1] = dic[4][1] + 1
            elif tipo == "TEXTO":
                dic[5].append(tipo)
                dic[4][2] = dic[4][2] + 1
            elif tipo == "LISTA":
                dic[5].append(tipo+','+self.AuxTipoLista+','+self.AuxTamanioLista)
                dic[4][3] = dic[4][3] + 1
        else: 
            dic = self.dirPrincipal[self.claseActual][1][self.funcionActual]
            if tipo == "ENTERO":
                dic[3].append(tipo)
                dic[2][0] = dic[2][0] + 1
            elif tipo == "DECIMAL":
                dic[3].append(tipo)
                dic[2][1] = dic[2][1] + 1
            elif tipo == "TEXTO":
                dic[3].append(tipo)
                dic[2][2] = dic[2][2] + 1
            elif tipo == "LISTA":
                dic[3].append(tipo+','+self.AuxTipoLista+','+self.AuxTamanioLista)
                dic[2][3] = dic[2][3] + 1
    
    def checarParametro(self):
        variableParametro = self.getCurrentToken().text
        
    def insertarValorTipo(self,op,tipoOp):
        self.pilaO.append(op)
        self.pTipos.append(tipoOp)

    def insertarOperador(self,op):
        self.pOper.append(op)

    def crearCuadruploExpresion(self,op,tipoCuadruplo):
        #OP = 0 - mult,div 1 - suma,resta 2 - relacionales 3 - logicos 4 - asignacion
        auxDireccion = 0
        if self.pOper:
            oper = self.pOper.pop()
            if oper in self.quadOperadores[op]:
                if self.pilaO:
                    oDer = self.pilaO.pop()
                    oDerTipo = self.pTipos.pop()
                    if self.pilaO:
                        oIzq = self.pilaO.pop()
                        oIzqTipo = self.pTipos.pop()
                        res = self.cuboSem.checarSemanticaExp(oIzqTipo,oDerTipo,oper)
                        if res != None:
                            if tipoCuadruplo == 'exp':
                                if res == "ENTERO":
                                    self.memLocalEntero = self.memLocalEntero + 1
                                    auxDireccion = self.memLocalEntero
                                elif res == "DECIMAL":
                                    self.memLocalDecimal = self.memLocalDecimal + 1
                                    auxDireccion = self.memLocalDecimal
                                elif res == "TEXTO":
                                    self.memLocalTexto = self.memLocalTexto + 1
                                    auxDireccion = self.memLocalTexto
                                self.quadList.append([oper,oIzq,oDer,auxDireccion])
                                self.insertarValorTipo(auxDireccion,res)
                            elif tipoCuadruplo == 'asignacion':
                                self.quadList.append([oper,oDer,None,oIzq])
                        else:
                            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Tipos de operandos no compatibles" )
                            self._syntaxErrors = self._syntaxErrors + 1
                            sys.exit()
                            return
                    else:
                        self.pilaO.append(oDer)
                        self.pTipos.append(oDerTipo)
                        self.pOper.append(oper)
            else:
                self.pOper.append(oper)

    def construirValidarCompuesto(self):
        self.checarId(self.semanticaCompuestoAux)
        if self.semanticaCompuestoAux2 == None:
            self.tipoOperando = self.obtenerTipo(self.semanticaCompuestoAux)
            auxDir = self.obtenerDireccionVariable(self.semanticaCompuestoAux)
            self.insertarValorTipo(auxDir,self.tipoOperando)
        elif self.semanticaCompuestoAux3 == None:
            isInt = True
            try:
                tempInt = int(self.semanticaCompuestoAux2)
            except ValueError:
                isInt = False
            if isInt == False:
                self.checarAtributo(self.semanticaCompuestoAux2)
                self.tipoOperando = self.obtenerTipo(self.semanticaCompuestoAux + '.' + self.semanticaCompuestoAux2)
            else:
                auxTipo = self.obtenerTipo(self.semanticaCompuestoAux)
                auxTipo = auxTipo.split(',')
                if len(auxTipo) < 2:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " La variable no es una lista" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                if int(auxTipo[2]) <= int(self.semanticaCompuestoAux2):
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Index fuera de rango" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                self.tipoOperando = auxTipo[1]
            auxDir = self.obtenerDireccionVariable(self.semanticaCompuestoAux + '.' + self.semanticaCompuestoAux2)
            self.insertarValorTipo(auxDir,self.tipoOperando)
        else:
            self.checarAtributo(self.semanticaCompuestoAux2)
            self.tipoOperando = self.obtenerTipo(self.semanticaCompuestoAux + '.' + self.semanticaCompuestoAux2 + '.' + self.semanticaCompuestoAux3)
            self.tipoOperando = self.tipoOperando.split(',')
            if len(self.tipoOperando) < 2:
                print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " La variable no es una lista" )
                self._syntaxErrors = self._syntaxErrors + 1
                sys.exit()
            if int(self.tipoOperando[2]) <= int(self.semanticaCompuestoAux3):
                print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Index fuera de rango" )
                self._syntaxErrors = self._syntaxErrors + 1
                sys.exit()
            self.tipoOperando = self.tipoOperando[1]
            auxDir = self.obtenerDireccionVariable(self.semanticaCompuestoAux + '.' + self.semanticaCompuestoAux2 + '.' + self.semanticaCompuestoAux3)
            self.insertarValorTipo(auxDir,self.tipoOperando)



    def crearCuadruploEscritura(self):
        if self.pilaO:
            elemento = self.pilaO.pop()
            elementoTipo = self.pTipos.pop()
            self.quadList.append(['escribir',None,None,elemento])

    def crearCuadruploLectura(self,elemento):
        self.quadList.append(['leer',None,None,elemento])

    def crearCuadruploCondicion(self):
        condicion = self.pilaO.pop()
        tipoCondicion = self.pTipos.pop()
        if tipoCondicion != 'ENTERO':
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Tipo de operando no compatible" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
            return
        else:
            self.quadList.append(['gotof',condicion,None,None])
            cont = len(self.quadList)
            self.pSaltos.append(cont-1)

    def crearCuadruploDecision2(self):
        salida = self.pSaltos.pop()
        cont = len(self.quadList)
        self.quadList[salida][3] = cont

    def crearCuadruploDecision3(self):
        falso = self.pSaltos.pop()
        self.quadList.append(['goto',None,None,None])
        cont = len(self.quadList)
        self.pSaltos.append(cont-1)
        self.quadList[falso][3] = cont

    def crearCuadruploCiclo1(self):
        cont = len(self.quadList)
        self.pSaltos.append(cont)

    def crearCuadruploCiclo3(self):
        falso = self.pSaltos.pop()
        retorno = self.pSaltos.pop()
        self.quadList.append(['goto',None,None,retorno])
        cont = len(self.quadList)
        self.quadList[falso][3] = cont

    def crearCuadruploEra(self, nombreFuncion):
        tamAux = self.obtenerTamanioFuncion(nombreFuncion)
        self.quadList.append(['ERA',None,None,tamAux])

    def crearCuadruploParam(self, referencia, numParam):
        elementoLlamada = self.pilaO[len(self.pilaO) - 1]
        elemParametro = self.obtenerTipoDireccionParametro(self.stackParametros[len(self.stackParametros) - 1], numParam)
        dirParametro = self.obtenerDireccionParametro(elemParametro)
        self.quadList.append(['PARAM',referencia,dirParametro,elementoLlamada])

    def crearCuadruploGosub(self, nombreFuncion):
        dirAux = self.obtenerDireccionFuncion(nombreFuncion)
        self.quadList.append(['GOSUB',None,None,dirAux])

    def crearCuadruploRetornar(self):
        elemento = self.pilaO.pop()
        tipoElemento = self.pTipos.pop()
        self.quadList.append(['RETORNAR',None,None,elemento])

    def crearCuadruploAsignacionRetorno(self):
        if self.asignacionRetorno:
            elemento = self.asignacionRetorno.pop()
            if elemento != None:
                self.quadList.append(['asignacionRetorno',None,None,elemento])

    def crearCuadruploTerminarProc(self):
        self.quadList.append([self.terminacionProc,None,None,None])

    def crearCuadruploInicial(self):
        self.quadList.append(['goto',None,None,None])

    def completarCuadruploInicial(self):
        cont = len(self.quadList)
        self.quadList[0][3] = cont

    def asignarDirInicioFuncion(self, nombreFuncion):
        cont = len(self.quadList)
        if self.claseActual == None:
            if self.dirPrincipal.get(nombreFuncion):
                self.dirPrincipal[nombreFuncion][6] = cont
        else:
            if self.dirPrincipal[self.claseActual][1].get(nombreFuncion):
                self.dirPrincipal[self.claseActual][1][nombreFuncion][4] = cont

    def asignarTamanioFuncion(self):
        contEntero = self.memLocalEntero - 8999
        contDecimal = self.memLocalDecimal - 14999
        contTexto = self.memLocalTexto - 20999
        if self.claseActual == None:
            if self.dirPrincipal.get(self.funcionActual):
                self.dirPrincipal[self.funcionActual][7] = [contEntero,contDecimal,contTexto]
        else:
            if self.dirPrincipal[self.claseActual][1].get(self.funcionActual):
                self.dirPrincipal[self.claseActual][1][self.funcionActual][5] = [contEntero,contDecimal,contTexto]

    def checarOrdenParametros(self):
        if len(self.stackParametros) == 0 or len(self.pTipos) == 0 or len(self.stackContParametros) == 0 :
            return
        listaPar = self.obtenerParametros(self.stackParametros[len(self.stackParametros) - 1])
        cont = self.stackContParametros[len(self.stackContParametros)-1]
        if listaPar == None or len(listaPar) < cont:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " La cantidad de parametros es incorrecta" )
            self._syntaxErrors = self._syntaxErrors + 1
            self.stackContParametros[len(self.stackContParametros)-1] = self.stackContParametros[len(self.stackContParametros)-1] + 1
            sys.exit()
            return
        tipoParametro = listaPar[cont].split(',')
        tipoLlamada = self.pTipos[len(self.pTipos)-1].split(',')
        if (len(tipoParametro) == 1) or (len(tipoLlamada) == 1):
            if tipoParametro[0] != tipoLlamada[0]:
                print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " El tipo de parametro es incorrecto" )
                self._syntaxErrors = self._syntaxErrors + 1
        else:
            if (tipoParametro[0] != tipoLlamada[0]) or (tipoParametro[1] != tipoLlamada[1]):
                print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " El tipo de parametro es incorrecto" )
                self._syntaxErrors = self._syntaxErrors + 1
        
        self.stackContParametros[len(self.stackContParametros)-1] = self.stackContParametros[len(self.stackContParametros)-1] + 1
        self.pilaO.pop()
        self.pTipos.pop()

    def validarTipoRetorno(self):
        if self.RetornoTipo == "NADA":
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se espera un valor de retorno" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
        elif self.RetornoTipo != self.pTipos[len(self.stackParametros) - 1]:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Se espera un valor de retorno de tipo " + self.RetornoTipo )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()

    def validarNoRetorno(self):
        if self.RetornoTipo != "NADA":
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Se espera un valor de retorno de tipo " + self.RetornoTipo )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()

    def checarLongitudParametros(self):
        if self.stackParametros:
            resObtenerParam = self.obtenerParametros(self.stackParametros[len(self.stackParametros) - 1])
            if resObtenerParam:
                if len(resObtenerParam) != self.stackContParametros[len(self.stackContParametros)-1]:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " La cantidad de parametros es incorrecta" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    sys.exit()
                    return
                self.stackParametros.pop()
                self.stackContParametros.pop()

    def programa(self):

        localctx = misterParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.crearCuadruploInicial()
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.programaAux1()
            self.state = 147
            self.programaAux3()
            self.state = 148
            self.match(misterParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_vars(self):
            return self.getTypedRuleContext(misterParser.V_varsContext,0)


        def programaAux1(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux1Context,0)


        def c_class(self):
            return self.getTypedRuleContext(misterParser.C_classContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_programaAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux1(self)




    def programaAux1(self):

        localctx = misterParser.ProgramaAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_programaAux1)
        try:
            self.state = 157
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.v_vars()
                self.state = 151
                self.programaAux1()

            elif token in [misterParser.CLASE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.c_class()
                self.state = 154
                self.programaAux1()

            elif token in [misterParser.FUNCION]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(misterParser.FUNCION, 0)

        def programaAux5(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux5Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_programaAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux3(self)




    def programaAux3(self):

        localctx = misterParser.ProgramaAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_programaAux3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(misterParser.FUNCION)
            self.state = 160
            self.programaAux5()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(misterParser.ENTERO, 0)

        def programaAux6(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux6Context,0)


        def DECIMAL(self):
            return self.getToken(misterParser.DECIMAL, 0)

        def programaAux7(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux7Context,0)


        def TEXTO(self):
            return self.getToken(misterParser.TEXTO, 0)

        def NADA(self):
            return self.getToken(misterParser.NADA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_programaAux5

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux5(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux5(self)




    def programaAux5(self):

        localctx = misterParser.ProgramaAux5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_programaAux5)
        try:
            self.state = 170
            token = self._input.LA(1)
            self.RetornoTipo = self.getCurrentToken().text
            if token in [misterParser.ENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(misterParser.ENTERO)
                self.state = 163
                self.AuxTipo = "ENTERO"
                self.programaAux6()

            elif token in [misterParser.DECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 164
                self.match(misterParser.DECIMAL)
                self.state = 165
                self.AuxTipo = "DECIMAL"
                self.programaAux7()

            elif token in [misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 166
                self.match(misterParser.TEXTO)
                self.state = 167
                self.AuxTipo = "TEXTO"
                self.programaAux7()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 4)
                self.state = 168
                self.match(misterParser.NADA)
                self.state = 169
                self.AuxTipo = "NADA"
                self.programaAux7()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INICIO(self):
            return self.getToken(misterParser.INICIO, 0)

        def func(self):
            return self.getTypedRuleContext(misterParser.FuncContext,0)


        def programaAux7(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux7Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_programaAux6

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux6(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux6(self)




    def programaAux6(self):

        localctx = misterParser.ProgramaAux6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_programaAux6)
        try:
            self.state = 175
            token = self._input.LA(1)
            if token in [misterParser.INICIO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.insertarFunc()
                self.match(misterParser.INICIO)
                self.completarCuadruploInicial()
                self.asignarDirInicioFuncion('INICIO')
                self.terminacionProc = 'END'
                self.state = 173
                self.func()

            elif token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
                self.programaAux7()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(misterParser.FuncContext,0)


        def programaAux3(self):
            return self.getTypedRuleContext(misterParser.ProgramaAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_programaAux7

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux7(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux7(self)




    def programaAux7(self):

        localctx = misterParser.ProgramaAux7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_programaAux7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.insertarFunc()
            self.asignarDirInicioFuncion(self.funcionActual)
            self.match(misterParser.ID)
            self.terminacionProc = 'ENDPROC'
            self.state = 178
            self.func()
            self.state = 179
            self.programaAux3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ProgramaAux4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def NADA(self):
            return self.getToken(misterParser.NADA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_programaAux4

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterProgramaAux4(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitProgramaAux4(self)




    def programaAux4(self):

        localctx = misterParser.ProgramaAux4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_programaAux4)
        try:
            self.state = 183
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 181
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(misterParser.NADA)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_varsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsAux1(self):
            return self.getTypedRuleContext(misterParser.VarsAux1Context,0)


        def v_varsDefinicion(self):
            return self.getTypedRuleContext(misterParser.V_varsDefinicionContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_v_vars

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterV_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitV_vars(self)




    def v_vars(self):

        localctx = misterParser.V_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_v_vars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.varsAux1()
            self.state = 186
            self.v_varsDefinicion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def l_list(self):
            return self.getTypedRuleContext(misterParser.L_listContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux1(self)




    def varsAux1(self):

        localctx = misterParser.VarsAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_varsAux1)
        try:
            self.state = 191
            token = self._input.LA(1)
            self.AuxTipoVar = self.getCurrentToken().text
            if token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(misterParser.ID)
                self.checarClase()

            elif token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.l_list()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_varsDefinicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsAux4(self):
            return self.getTypedRuleContext(misterParser.VarsAux4Context,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_v_varsDefinicion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterV_varsDefinicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitV_varsDefinicion(self)




    def v_varsDefinicion(self):

        localctx = misterParser.V_varsDefinicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_v_varsDefinicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.varsAux4()
            self.state = 194
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IGUAL(self):
            return self.getToken(misterParser.IGUAL, 0)

        def varsAux3(self):
            return self.getTypedRuleContext(misterParser.VarsAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux2(self)




    def varsAux2(self):

        localctx = misterParser.VarsAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_varsAux2)
        try:
            self.state = 199
            token = self._input.LA(1)
            if token in [misterParser.IGUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 196
                self.match(misterParser.IGUAL)
                self.insertarOperador('=')
                self.state = 197
                self.varsAux3()
                self.crearCuadruploExpresion(4,'asignacion')

            elif token in [misterParser.COMA, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def cteL(self):
            return self.getTypedRuleContext(misterParser.CteLContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux3(self)




    def varsAux3(self):

        localctx = misterParser.VarsAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_varsAux3)
        try:
            self.state = 203
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.cteL()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def varsAux2(self):
            return self.getTypedRuleContext(misterParser.VarsAux2Context,0)


        def varsAux5(self):
            return self.getTypedRuleContext(misterParser.VarsAux5Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux4

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux4(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux4(self)




    def varsAux4(self):

        localctx = misterParser.VarsAux4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_varsAux4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.variableActual = self.getCurrentToken().text
            self.match(misterParser.ID)
            auxVariableActual = self.variableActual
            self.insertarVariable()
            self.checarId(auxVariableActual)
            self.tipoOperando = self.obtenerTipo(auxVariableActual)
            auxDir = self.obtenerDireccionVariable(auxVariableActual)
            self.insertarValorTipo(auxDir,self.tipoOperando)
            self.state = 206
            self.varsAux2()
            self.state = 207
            self.varsAux5()
            self.AuxTipoVar = None
            self.AuxTipoLista = None
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAux5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def varsAux2(self):
            return self.getTypedRuleContext(misterParser.VarsAux2Context,0)


        def varsAux5(self):
            return self.getTypedRuleContext(misterParser.VarsAux5Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAux5

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAux5(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAux5(self)




    def varsAux5(self):

        localctx = misterParser.VarsAux5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_varsAux5)
        try:
            self.state = 215
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                self.match(misterParser.COMA)
                self.state = 210
                self.variableActual = self.getCurrentToken().text
                self.match(misterParser.ID)
                auxVariableActual = self.variableActual
                self.insertarVariable()
                self.checarId(auxVariableActual)
                self.tipoOperando = self.obtenerTipo(auxVariableActual)
                auxDir = self.obtenerDireccionVariable(auxVariableActual)
                self.insertarValorTipo(auxDir,self.tipoOperando)
                self.state = 211
                self.varsAux2()
                self.state = 212
                self.varsAux5()

            elif token in [misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_varsAtribContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsAtribAux1(self):
            return self.getTypedRuleContext(misterParser.VarsAtribAux1Context,0)


        def v_varsDefinicion(self):
            return self.getTypedRuleContext(misterParser.V_varsDefinicionContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_v_varsAtrib

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterV_varsAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitV_varsAtrib(self)




    def v_varsAtrib(self):

        localctx = misterParser.V_varsAtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_v_varsAtrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.varsAtribAux1()
            self.state = 218
            self.v_varsDefinicion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarsAtribAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def l_list(self):
            return self.getTypedRuleContext(misterParser.L_listContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_varsAtribAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterVarsAtribAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitVarsAtribAux1(self)




    def varsAtribAux1(self):

        localctx = misterParser.VarsAtribAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_varsAtribAux1)
        try:
            self.state = 222
            token = self._input.LA(1)
            self.AuxTipoVar = self.getCurrentToken().text
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.l_list()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(misterParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(misterParser.DECIMAL, 0)

        def TEXTO(self):
            return self.getToken(misterParser.TEXTO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = misterParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << misterParser.ENTERO) | (1 << misterParser.DECIMAL) | (1 << misterParser.TEXTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class L_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LISTA(self):
            return self.getToken(misterParser.LISTA, 0)

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def CTENTERO(self):
            return self.getToken(misterParser.CTENTERO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_l_list

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterL_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitL_list(self)




    def l_list(self):

        localctx = misterParser.L_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_l_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.match(misterParser.LISTA)
            self.state = 227
            self.AuxTipoLista = self.getCurrentToken().text
            self.tipo()
            self.state = 228
            self.AuxTamanioLista = self.getCurrentToken().text
            self.match(misterParser.CTENTERO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CteLContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCHETE1(self):
            return self.getToken(misterParser.CORCHETE1, 0)

        def valor(self):
            return self.getTypedRuleContext(misterParser.ValorContext,0)


        def cteLAux1(self):
            return self.getTypedRuleContext(misterParser.CteLAux1Context,0)


        def CORCHETE2(self):
            return self.getToken(misterParser.CORCHETE2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_cteL

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCteL(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCteL(self)




    def cteL(self):

        localctx = misterParser.CteLContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_cteL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.match(misterParser.CORCHETE1)
            self.state = 231
            self.valor()
            self.state = 232
            self.cteLAux1()
            self.state = 233
            self.match(misterParser.CORCHETE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CteLAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def valor(self):
            return self.getTypedRuleContext(misterParser.ValorContext,0)


        def cteLAux1(self):
            return self.getTypedRuleContext(misterParser.CteLAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_cteLAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCteLAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCteLAux1(self)




    def cteLAux1(self):

        localctx = misterParser.CteLAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_cteLAux1)
        try:
            self.state = 240
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.match(misterParser.COMA)
                self.state = 236
                self.valor()
                self.state = 237
                self.cteLAux1()

            elif token in [misterParser.CORCHETE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CTENTERO(self):
            return self.getToken(misterParser.CTENTERO, 0)

        def CTEDECIMAL(self):
            return self.getToken(misterParser.CTEDECIMAL, 0)

        def compuesto(self):
            return self.getTypedRuleContext(misterParser.CompuestoContext,0)


        def valorAux1(self):
            return self.getTypedRuleContext(misterParser.ValorAux1Context,0)


        def CTETEXTO(self):
            return self.getToken(misterParser.CTETEXTO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_valor

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterValor(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitValor(self)




    def valor(self):

        localctx = misterParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_valor)
        try:
            self.state = 248
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.tipoOperando = 'ENTERO'
                self.operando = self.getCurrentToken().text
                self.match(misterParser.CTENTERO)
                self.insertarValorTipo([int(self.operando)], self.tipoOperando)

            elif token in [misterParser.CTEDECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.tipoOperando = 'DECIMAL'
                self.operando = self.getCurrentToken().text
                self.match(misterParser.CTEDECIMAL)
                self.insertarValorTipo([float(self.operando)], self.tipoOperando)

            elif token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.compuesto()
                self.state = 245
                self.valorAux1()
                self.semanticaCompuestoAux = None
                self.semanticaCompuestoAux2 = None
                self.semanticaCompuestoAux3 = None


            elif token in [misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 247
                self.tipoOperando = 'TEXTO'
                self.operando = self.getCurrentToken().text
                self.match(misterParser.CTETEXTO)
                self.insertarValorTipo([self.operando.replace('"', "")], self.tipoOperando)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValorAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def llamarFunc(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_valorAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterValorAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitValorAux1(self)




    def valorAux1(self):

        localctx = misterParser.ValorAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_valorAux1)
        try:
            self.state = 252
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.checarMetodo()
                if self.semanticaCompuestoAux2 == None:
                    self.tipoOperando = self.obtenerTipo(self.semanticaCompuestoAux + '(')
                    direccion = self.semanticaCompuestoAux + '('
                    if self.tipoOperando == "ENTERO":
                        self.memLocalEntero = self.memLocalEntero + 1
                        direccion = self.memLocalEntero
                        self.asignacionRetorno.append(direccion)
                    elif self.tipoOperando == "DECIMAL":
                        self.memLocalDecimal = self.memLocalDecimal + 1
                        direccion = self.memLocalDecimal
                        self.asignacionRetorno.append(direccion)
                    elif self.tipoOperando == "TEXTO":
                        self.memLocalTexto = self.memLocalTexto + 1
                        direccion = self.memLocalTexto
                        self.asignacionRetorno.append(direccion)
                    self.insertarValorTipo(direccion,self.tipoOperando)
                else:
                    self.tipoOperando = self.obtenerTipo(self.semanticaCompuestoAux + '.' + self.semanticaCompuestoAux2 + '(')
                    direccion = self.semanticaCompuestoAux + '.' + self.semanticaCompuestoAux2 + '('
                    if self.tipoOperando == "ENTERO":
                        self.memLocalEntero = self.memLocalEntero + 1
                        direccion = self.memLocalEntero
                    elif self.tipoOperando == "DECIMAL":
                        self.memLocalDecimal = self.memLocalDecimal + 1
                        direccion = self.memLocalDecimal
                    elif self.tipoOperando == "TEXTO":
                        self.memLocalTexto = self.memLocalTexto + 1
                        direccion = self.memLocalTexto
                    self.insertarValorTipo(direccion,self.tipoOperando)
                self.llamarFunc()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIVISION, misterParser.MULTIPLICACION, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.CORCHETE2, misterParser.PUNTOYCOMA]:
                self.construirValidarCompuesto()
                self.enterOuterAlt(localctx, 2)


            else:
                self.construirValidarCompuesto()
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def parametrosAux1(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux1Context,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = misterParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self.match(misterParser.PARENTESIS1)
            self.state = 255
            self.parametrosAux1()
            self.state = 256
            self.match(misterParser.PARENTESIS2)
            self.AuxTipoVar = None
            self.AuxTipoLista = None
            self.variableActual = None
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametrosAux2(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux2Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def parametrosAux3(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_parametrosAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametrosAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametrosAux1(self)




    def parametrosAux1(self):

        localctx = misterParser.ParametrosAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_parametrosAux1)
        try:
            self.state = 263
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.parametrosAux2()
                self.state = 259
                self.variableActual = self.getCurrentToken().text
                self.insertarVariable()
                self.match(misterParser.ID)
                self.state = 260
                self.parametrosAux3()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def l_list(self):
            return self.getTypedRuleContext(misterParser.L_listContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_parametrosAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametrosAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametrosAux2(self)




    def parametrosAux2(self):

        localctx = misterParser.ParametrosAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parametrosAux2)
        try:
            self.state = 267
            token = self._input.LA(1)
            self.AuxTipoVar = self.getCurrentToken().text
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.agregarParametro(self.getCurrentToken().text)
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                tipo = self.getCurrentToken().text
                self.l_list()
                self.agregarParametro(tipo)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def parametrosAux2(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux2Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def parametrosAux3(self):
            return self.getTypedRuleContext(misterParser.ParametrosAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_parametrosAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterParametrosAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitParametrosAux3(self)




    def parametrosAux3(self):

        localctx = misterParser.ParametrosAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_parametrosAux3)
        try:
            self.state = 275
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 269
                self.match(misterParser.COMA)
                self.state = 270
                self.parametrosAux2()
                self.state = 271
                self.variableActual = self.getCurrentToken().text
                self.insertarVariable()
                self.match(misterParser.ID)
                self.state = 272
                self.parametrosAux3()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametros(self):
            return self.getTypedRuleContext(misterParser.ParametrosContext,0)


        def LLAVE1(self):
            return self.getToken(misterParser.LLAVE1, 0)

        def funcAux1(self):
            return self.getTypedRuleContext(misterParser.FuncAux1Context,0)


        def funcAux2(self):
            return self.getTypedRuleContext(misterParser.FuncAux2Context,0)


        def funcAux3(self):
            return self.getTypedRuleContext(misterParser.FuncAux3Context,0)


        def LLAVE2(self):
            return self.getToken(misterParser.LLAVE2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFunc(self)




    def func(self):

        localctx = misterParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_func)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.resetDireccionLocal()
            self.parametros()
            self.state = 278
            self.match(misterParser.LLAVE1)
            self.state = 279
            self.funcAux1()
            self.state = 280
            self.funcAux2()
            self.state = 281
            self.funcAux3()
            self.state = 282
            self.match(misterParser.LLAVE2)
            self.asignarTamanioFuncion()
            self.crearCuadruploTerminarProc()
            self.funcionActual = None
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_vars(self):
            return self.getTypedRuleContext(misterParser.V_varsContext,0)


        def funcAux1(self):
            return self.getTypedRuleContext(misterParser.FuncAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_funcAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFuncAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFuncAux1(self)




    def funcAux1(self):

        localctx = misterParser.FuncAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_funcAux1)
        try:
            self.state = 288
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 284
                self.v_vars()
                self.state = 285
                self.funcAux1()
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

    class FuncAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(misterParser.EstatutoContext,0)


        def funcAux2(self):
            return self.getTypedRuleContext(misterParser.FuncAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_funcAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFuncAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFuncAux2(self)




    def funcAux2(self):

        localctx = misterParser.FuncAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcAux2)
        try:
            self.state = 294
            token = self._input.LA(1)
            if token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.ASIGNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.estatuto()
                self.state = 291
                self.funcAux2()

            elif token in [misterParser.RETORNAR, misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETORNAR(self):
            return self.getToken(misterParser.RETORNAR, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_funcAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFuncAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFuncAux3(self)




    def funcAux3(self):

        localctx = misterParser.FuncAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_funcAux3)
        try:
            self.state = 301
            token = self._input.LA(1)
            if token in [misterParser.RETORNAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 296
                self.match(misterParser.RETORNAR)
                self.state = 297
                self.expresion()
                self.validarTipoRetorno()
                self.crearCuadruploRetornar()
                self.state = 298
                self.match(misterParser.PUNTOYCOMA)

            elif token in [misterParser.LLAVE2]:
                self.validarNoRetorno()
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(misterParser.DeclaracionContext,0)


        def expresionAux1(self):
            return self.getTypedRuleContext(misterParser.ExpresionAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = misterParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.declaracion()
            self.state = 304
            self.expresionAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionAux2(self):
            return self.getTypedRuleContext(misterParser.ExpresionAux2Context,0)


        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_expresionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpresionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpresionAux1(self)




    def expresionAux1(self):

        localctx = misterParser.ExpresionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expresionAux1)
        try:
            self.state = 310
            token = self._input.LA(1)
            if token in [misterParser.Y, misterParser.O]:
                self.enterOuterAlt(localctx, 1)
                self.state = 306
                self.operador = self.getCurrentToken().text
                self.expresionAux2()
                self.insertarOperador(self.operador)
                self.state = 307
                self.expresion()
                self.crearCuadruploExpresion(3,'exp')

            elif token in [misterParser.COMA, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Y(self):
            return self.getToken(misterParser.Y, 0)

        def O(self):
            return self.getToken(misterParser.O, 0)

        def getRuleIndex(self):
            return misterParser.RULE_expresionAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpresionAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpresionAux2(self)




    def expresionAux2(self):

        localctx = misterParser.ExpresionAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expresionAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            _la = self._input.LA(1)
            if not(_la==misterParser.Y or _la==misterParser.O):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstatutoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(misterParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(misterParser.CondicionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def escritura(self):
            return self.getTypedRuleContext(misterParser.EscrituraContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(misterParser.CicloContext,0)


        def lectura(self):
            return self.getTypedRuleContext(misterParser.LecturaContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = misterParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_estatuto)
        try:
            self.state = 322
            token = self._input.LA(1)
            if token in [misterParser.ASIGNAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
                self.asignacion()

            elif token in [misterParser.SI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 315
                self.condicion()

            elif token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 316
                self.expresion()
                self.state = 317
                self.match(misterParser.PUNTOYCOMA)

            elif token in [misterParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 319
                self.escritura()

            elif token in [misterParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 320
                self.ciclo()

            elif token in [misterParser.LEER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 321
                self.lectura()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(misterParser.ExpContext,0)


        def declaracionAux2(self):
            return self.getTypedRuleContext(misterParser.DeclaracionAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = misterParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self.exp()
            self.state = 325
            self.declaracionAux2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAYOR(self):
            return self.getToken(misterParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(misterParser.MENOR, 0)

        def DIFERENTE(self):
            return self.getToken(misterParser.DIFERENTE, 0)

        def MAYORIGUAL(self):
            return self.getToken(misterParser.MAYORIGUAL, 0)

        def MENORIGUAL(self):
            return self.getToken(misterParser.MENORIGUAL, 0)

        def IDENTICO(self):
            return self.getToken(misterParser.IDENTICO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_declaracionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterDeclaracionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitDeclaracionAux1(self)




    def declaracionAux1(self):

        localctx = misterParser.DeclaracionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_declaracionAux1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << misterParser.IDENTICO) | (1 << misterParser.DIFERENTE) | (1 << misterParser.MAYORIGUAL) | (1 << misterParser.MENORIGUAL) | (1 << misterParser.MENOR) | (1 << misterParser.MAYOR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionAux1(self):
            return self.getTypedRuleContext(misterParser.DeclaracionAux1Context,0)


        def exp(self):
            return self.getTypedRuleContext(misterParser.ExpContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_declaracionAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterDeclaracionAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitDeclaracionAux2(self)




    def declaracionAux2(self):

        localctx = misterParser.DeclaracionAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_declaracionAux2)
        try:
            self.state = 333
            token = self._input.LA(1)
            if token in [misterParser.IDENTICO, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.operador = self.getCurrentToken().text
                self.declaracionAux1()
                self.insertarOperador(self.operador)
                self.state = 330
                self.exp()
                self.crearCuadruploExpresion(2,'exp')

            elif token in [misterParser.Y, misterParser.O, misterParser.COMA, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(misterParser.TerminoContext,0)


        def expAux1(self):
            return self.getTypedRuleContext(misterParser.ExpAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExp(self)




    def exp(self):

        localctx = misterParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.termino()
            self.crearCuadruploExpresion(1,'exp')
            self.state = 336
            self.expAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(misterParser.SUMA, 0)

        def termino(self):
            return self.getTypedRuleContext(misterParser.TerminoContext,0)


        def expAux1(self):
            return self.getTypedRuleContext(misterParser.ExpAux1Context,0)


        def RESTA(self):
            return self.getToken(misterParser.RESTA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_expAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterExpAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitExpAux1(self)




    def expAux1(self):

        localctx = misterParser.ExpAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expAux1)
        try:
            self.state = 347
            token = self._input.LA(1)
            if token in [misterParser.SUMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.match(misterParser.SUMA)
                self.insertarOperador('+')
                self.state = 339
                self.termino()
                self.crearCuadruploExpresion(1,'exp')
                self.state = 340
                self.expAux1()

            elif token in [misterParser.RESTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(misterParser.RESTA)
                self.insertarOperador('-')
                self.state = 343
                self.termino()
                self.crearCuadruploExpresion(1,'exp')
                self.state = 344
                self.expAux1()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def llamarFuncAux1(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux1Context,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_llamarFunc

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFunc(self)




    def llamarFunc(self):

        localctx = misterParser.LlamarFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_llamarFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(misterParser.PARENTESIS1)
            if self.semanticaCompuestoAux != None and self.semanticaCompuestoAux2 != None:
                self.stackParametros.append(self.semanticaCompuestoAux + "." + self.semanticaCompuestoAux2 + "(")
                self.stackContParametros.append(0)
            elif self.semanticaCompuestoAux != None:
                self.stackParametros.append(self.semanticaCompuestoAux + "(")
                self.stackContParametros.append(0)
            self.numeroParametro.append(0)
            self.numeroParametroEntero.append(0)
            self.numeroParametroDecimal.append(0)
            self.numeroParametroTexto.append(0)
            self.numeroDirParametroEntero.append(0)
            self.numeroDirParametroDecimal.append(0)
            self.numeroDirParametroTexto.append(0)
            self.crearCuadruploEra(self.stackParametros[len(self.stackParametros) - 1])
            self.state = 350
            self.llamarFuncAux1()
            self.state = 351
            self.match(misterParser.PARENTESIS2)
            self.numeroParametro.pop()
            self.numeroParametroEntero.pop()
            self.numeroParametroDecimal.pop()
            self.numeroParametroTexto.pop()
            self.numeroDirParametroEntero.pop()
            self.numeroDirParametroDecimal.pop()
            self.numeroDirParametroTexto.pop()
            self.crearCuadruploAsignacionRetorno()
            self.crearCuadruploGosub(self.stackParametros[len(self.stackParametros) - 1])
            self.checarLongitudParametros()
            
            
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def llamarFuncAux2(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux2Context,0)


        def REFERENCIA(self):
            return self.getToken(misterParser.REFERENCIA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def getRuleIndex(self):
            return misterParser.RULE_llamarFuncAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFuncAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFuncAux1(self)




    def llamarFuncAux1(self):

        localctx = misterParser.LlamarFuncAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_llamarFuncAux1)
        try:
            self.state = 360
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.expresion()
                self.state = 354
                self.crearCuadruploParam(False, self.numeroParametro[len(self.numeroParametro) - 1])
                self.numeroParametro[len(self.numeroParametro) - 1] = self.numeroParametro[len(self.numeroParametro) - 1] + 1
                self.llamarFuncAux2()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(misterParser.REFERENCIA)
                self.state = 357
                paramReferenciaId = self.getCurrentToken().text
                self.match(misterParser.ID)
                paramReferenciaTipo = self.obtenerTipo(paramReferenciaId)
                auxDir = self.obtenerDireccionVariable(paramReferenciaId)
                self.insertarValorTipo(auxDir, paramReferenciaTipo)
                self.state = 358
                self.crearCuadruploParam(True, self.numeroParametro[len(self.numeroParametro) - 1])
                self.numeroParametro[len(self.numeroParametro) - 1] = self.numeroParametro[len(self.numeroParametro) - 1] + 1
                self.llamarFuncAux2()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def llamarFuncAux3(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux3Context,0)


        def llamarFuncAux2(self):
            return self.getTypedRuleContext(misterParser.LlamarFuncAux2Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_llamarFuncAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFuncAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFuncAux2(self)




    def llamarFuncAux2(self):

        localctx = misterParser.LlamarFuncAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_llamarFuncAux2)
        try:
            self.state = 367
            token = self._input.LA(1)
            self.checarOrdenParametros()
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(misterParser.COMA)
                self.state = 363
                self.llamarFuncAux3()
                self.state = 364
                self.llamarFuncAux2()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarFuncAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def REFERENCIA(self):
            return self.getToken(misterParser.REFERENCIA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def getRuleIndex(self):
            return misterParser.RULE_llamarFuncAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLlamarFuncAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLlamarFuncAux3(self)




    def llamarFuncAux3(self):

        localctx = misterParser.LlamarFuncAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_llamarFuncAux3)
        try:
            self.state = 372
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.expresion()
                self.crearCuadruploParam(False, self.numeroParametro[len(self.numeroParametro) - 1])
                self.numeroParametro[len(self.numeroParametro) - 1] = self.numeroParametro[len(self.numeroParametro) - 1] + 1

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(misterParser.REFERENCIA)
                self.state = 371
                paramReferenciaId = self.getCurrentToken().text
                self.match(misterParser.ID)
                paramReferenciaTipo = self.obtenerTipo(paramReferenciaId)
                auxDir = self.obtenerDireccionVariable(paramReferenciaId)
                self.insertarValorTipo(auxDir, paramReferenciaTipo)
                self.crearCuadruploParam(True, self.numeroParametro[len(self.numeroParametro) - 1])
                self.numeroParametro[len(self.numeroParametro) - 1] = self.numeroParametro[len(self.numeroParametro) - 1] + 1

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(misterParser.FactorContext,0)


        def terminoAux1(self):
            return self.getTypedRuleContext(misterParser.TerminoAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitTermino(self)




    def termino(self):

        localctx = misterParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 374
            self.factor()
            self.crearCuadruploExpresion(0,'exp')
            self.state = 375
            self.terminoAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminoAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTIPLICACION(self):
            return self.getToken(misterParser.MULTIPLICACION, 0)

        def factor(self):
            return self.getTypedRuleContext(misterParser.FactorContext,0)


        def terminoAux1(self):
            return self.getTypedRuleContext(misterParser.TerminoAux1Context,0)


        def DIVISION(self):
            return self.getToken(misterParser.DIVISION, 0)

        def getRuleIndex(self):
            return misterParser.RULE_terminoAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterTerminoAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitTerminoAux1(self)




    def terminoAux1(self):

        localctx = misterParser.TerminoAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_terminoAux1)
        try:
            self.state = 386
            token = self._input.LA(1)
            if token in [misterParser.MULTIPLICACION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.match(misterParser.MULTIPLICACION)
                self.insertarOperador('*')
                self.state = 378
                self.factor()
                self.crearCuadruploExpresion(0,'exp')
                self.state = 379
                self.terminoAux1()

            elif token in [misterParser.DIVISION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(misterParser.DIVISION)
                self.insertarOperador('/')
                self.state = 382
                self.factor()
                self.crearCuadruploExpresion(0,'exp')
                self.state = 383
                self.terminoAux1()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def valor(self):
            return self.getTypedRuleContext(misterParser.ValorContext,0)


        def factorAux1(self):
            return self.getTypedRuleContext(misterParser.FactorAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFactor(self)




    def factor(self):

        localctx = misterParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_factor)
        try:
            self.state = 396
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 388
                self.match(misterParser.PARENTESIS1)
                self.insertarOperador('(')
                self.state = 389
                self.expresion()
                self.state = 390
                self.match(misterParser.PARENTESIS2)
                self.pOper.pop()

            elif token in [misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.valor()

            elif token in [misterParser.SUMA, misterParser.RESTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 393
                self.factorAux1()
                self.state = 394
                self.valor()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(misterParser.SUMA, 0)

        def RESTA(self):
            return self.getToken(misterParser.RESTA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_factorAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterFactorAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitFactorAux1(self)




    def factorAux1(self):

        localctx = misterParser.FactorAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_factorAux1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            _la = self._input.LA(1)
            if not(_la==misterParser.SUMA or _la==misterParser.RESTA):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompuestoContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def compuestoAux1(self):
            return self.getTypedRuleContext(misterParser.CompuestoAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_compuesto

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuesto(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuesto(self)




    def compuesto(self):

        localctx = misterParser.CompuestoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_compuesto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 400
            self.semanticaCompuestoAux = self.getCurrentToken().text
            self.match(misterParser.ID)
            self.state = 401
            self.compuestoAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompuestoAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(misterParser.PUNTO, 0)

        def compuestoAux3(self):
            return self.getTypedRuleContext(misterParser.CompuestoAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_compuestoAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuestoAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuestoAux1(self)




    def compuestoAux1(self):

        localctx = misterParser.CompuestoAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_compuestoAux1)
        try:
            self.state = 406
            token = self._input.LA(1)
            if token in [misterParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(misterParser.PUNTO)
                self.state = 404
                self.compuestoAux3()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.IGUAL, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIVISION, misterParser.MULTIPLICACION, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS1, misterParser.PARENTESIS2, misterParser.CORCHETE2, misterParser.PUNTOYCOMA]:
                self.semanticaCompuestoAux2 = None
                self.enterOuterAlt(localctx, 2)


            else:
                self.semanticaCompuestoAux2 = None
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompuestoAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def compuestoAux2(self):
            return self.getTypedRuleContext(misterParser.CompuestoAux2Context,0)


        def CTENTERO(self):
            return self.getToken(misterParser.CTENTERO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_compuestoAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuestoAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuestoAux3(self)




    def compuestoAux3(self):

        localctx = misterParser.CompuestoAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_compuestoAux3)
        try:
            self.state = 411
            token = self._input.LA(1)
            if token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                self.semanticaCompuestoAux2 = self.getCurrentToken().text
                self.match(misterParser.ID)
                self.state = 409
                self.compuestoAux2()

            elif token in [misterParser.CTENTERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.semanticaCompuestoAux2 = self.getCurrentToken().text
                self.match(misterParser.CTENTERO)

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompuestoAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(misterParser.PUNTO, 0)

        def CTENTERO(self):
            return self.getToken(misterParser.CTENTERO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_compuestoAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCompuestoAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCompuestoAux2(self)




    def compuestoAux2(self):

        localctx = misterParser.CompuestoAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_compuestoAux2)
        try:
            self.state = 416
            token = self._input.LA(1)
            if token in [misterParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 413
                self.match(misterParser.PUNTO)
                self.state = 414
                self.semanticaCompuestoAux3 = self.getCurrentToken().text
                self.match(misterParser.CTENTERO)

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.IGUAL, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIVISION, misterParser.MULTIPLICACION, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS1, misterParser.PARENTESIS2, misterParser.CORCHETE2, misterParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASIGNAR(self):
            return self.getToken(misterParser.ASIGNAR, 0)

        def compuesto(self):
            return self.getTypedRuleContext(misterParser.CompuestoContext,0)


        def IGUAL(self):
            return self.getToken(misterParser.IGUAL, 0)

        def asignacionAux1(self):
            return self.getTypedRuleContext(misterParser.AsignacionAux1Context,0)


        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = misterParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self.match(misterParser.ASIGNAR)
            self.state = 419
            self.compuesto()
            self.construirValidarCompuesto()
            self.state = 420  
            self.match(misterParser.IGUAL)
            self.insertarOperador('=')
            self.state = 421
            self.asignacionAux1()
            self.crearCuadruploExpresion(4,'asignacion')
            self.state = 422
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignacionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def cteL(self):
            return self.getTypedRuleContext(misterParser.CteLContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_asignacionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAsignacionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAsignacionAux1(self)




    def asignacionAux1(self):

        localctx = misterParser.AsignacionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_asignacionAux1)
        try:
            self.state = 426
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
                self.cteL()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(misterParser.SI, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def bloque(self):
            return self.getTypedRuleContext(misterParser.BloqueContext,0)


        def condicionAux1(self):
            return self.getTypedRuleContext(misterParser.CondicionAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = misterParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(misterParser.SI)
            self.state = 429
            self.match(misterParser.PARENTESIS1)
            self.state = 430
            self.expresion()
            self.state = 431
            self.match(misterParser.PARENTESIS2)
            self.crearCuadruploCondicion()
            self.state = 432
            self.bloque()
            self.state = 433
            self.condicionAux1()
            self.crearCuadruploDecision2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondicionAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SINO(self):
            return self.getToken(misterParser.SINO, 0)

        def bloque(self):
            return self.getTypedRuleContext(misterParser.BloqueContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_condicionAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCondicionAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCondicionAux1(self)




    def condicionAux1(self):

        localctx = misterParser.CondicionAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_condicionAux1)
        try:
            self.state = 438
            token = self._input.LA(1)
            if token in [misterParser.SINO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(misterParser.SINO)
                self.crearCuadruploDecision3()
                self.state = 436
                self.bloque()

            elif token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.RETORNAR, misterParser.ASIGNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.LLAVE2, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloqueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LLAVE1(self):
            return self.getToken(misterParser.LLAVE1, 0)

        def estatuto(self):
            return self.getTypedRuleContext(misterParser.EstatutoContext,0)


        def bloqueAux1(self):
            return self.getTypedRuleContext(misterParser.BloqueAux1Context,0)


        def LLAVE2(self):
            return self.getToken(misterParser.LLAVE2, 0)

        def getRuleIndex(self):
            return misterParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = misterParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 440
            self.match(misterParser.LLAVE1)
            self.state = 441
            self.estatuto()
            self.state = 442
            self.bloqueAux1()
            self.state = 443
            self.match(misterParser.LLAVE2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloqueAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(misterParser.EstatutoContext,0)


        def bloqueAux1(self):
            return self.getTypedRuleContext(misterParser.BloqueAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_bloqueAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterBloqueAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitBloqueAux1(self)




    def bloqueAux1(self):

        localctx = misterParser.BloqueAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_bloqueAux1)
        try:
            self.state = 449
            token = self._input.LA(1)
            if token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.ASIGNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 445
                self.estatuto()
                self.state = 446
                self.bloqueAux1()

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CicloContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(misterParser.MIENTRAS, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def bloque(self):
            return self.getTypedRuleContext(misterParser.BloqueContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitCiclo(self)




    def ciclo(self):

        localctx = misterParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 451
            self.match(misterParser.MIENTRAS)
            self.crearCuadruploCiclo1()
            self.state = 452
            self.match(misterParser.PARENTESIS1)
            self.state = 453
            self.expresion()
            self.state = 454
            self.match(misterParser.PARENTESIS2)
            self.crearCuadruploCondicion()
            self.state = 455
            self.bloque()
            self.crearCuadruploCiclo3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscrituraContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(misterParser.IMPRIMIR, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def escrituraAux1(self):
            return self.getTypedRuleContext(misterParser.EscrituraAux1Context,0)


        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitEscritura(self)




    def escritura(self):

        localctx = misterParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(misterParser.IMPRIMIR)
            self.state = 458
            self.match(misterParser.PARENTESIS1)
            self.state = 459
            self.expresion()
            self.crearCuadruploEscritura()
            self.state = 460
            self.escrituraAux1()
            self.state = 461
            self.match(misterParser.PARENTESIS2)
            self.state = 462
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscrituraAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(misterParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(misterParser.ExpresionContext,0)


        def escrituraAux1(self):
            return self.getTypedRuleContext(misterParser.EscrituraAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_escrituraAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterEscrituraAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitEscrituraAux1(self)




    def escrituraAux1(self):

        localctx = misterParser.EscrituraAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_escrituraAux1)
        try:
            self.state = 469
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.match(misterParser.COMA)
                self.state = 465
                self.expresion()
                self.crearCuadruploEscritura()
                self.state = 466
                self.escrituraAux1()

            elif token in [misterParser.PARENTESIS2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LecturaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(misterParser.LEER, 0)

        def PARENTESIS1(self):
            return self.getToken(misterParser.PARENTESIS1, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def PARENTESIS2(self):
            return self.getToken(misterParser.PARENTESIS2, 0)

        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_lectura

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterLectura(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitLectura(self)




    def lectura(self):

        localctx = misterParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(misterParser.LEER)
            self.state = 472
            self.match(misterParser.PARENTESIS1)
            self.state = 473
            idTempLectura = self.getCurrentToken().text
            self.match(misterParser.ID)
            self.checarId(idTempLectura)
            leerDirAux = self.obtenerDireccionVariable(idTempLectura)
            self.crearCuadruploLectura(leerDirAux)
            self.state = 474
            self.match(misterParser.PARENTESIS2)
            self.state = 475
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class C_classContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASE(self):
            return self.getToken(misterParser.CLASE, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def classAux1(self):
            return self.getTypedRuleContext(misterParser.ClassAux1Context,0)


        def LLAVE1(self):
            return self.getToken(misterParser.LLAVE1, 0)

        def classAux2(self):
            return self.getTypedRuleContext(misterParser.ClassAux2Context,0)


        def classAux3(self):
            return self.getTypedRuleContext(misterParser.ClassAux3Context,0)


        def LLAVE2(self):
            return self.getToken(misterParser.LLAVE2, 0)

        def PUNTOYCOMA(self):
            return self.getToken(misterParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_c_class

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterC_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitC_class(self)




    def c_class(self):

        localctx = misterParser.C_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_c_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(misterParser.CLASE)
            self.state = 478
            self.claseActual = self.getCurrentToken().text
            self.match(misterParser.ID)
            self.state = 479
            self.classAux1()
            self.state = 480
            self.insertarClase()
            self.match(misterParser.LLAVE1)
            self.state = 481
            self.classAux2()
            self.state = 482
            self.classAux3()
            self.state = 483
            self.match(misterParser.LLAVE2)
            self.claseActual = None
            self.state = 484
            self.match(misterParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEREDA(self):
            return self.getToken(misterParser.HEREDA, 0)

        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def getRuleIndex(self):
            return misterParser.RULE_classAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterClassAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitClassAux1(self)




    def classAux1(self):

        localctx = misterParser.ClassAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_classAux1)
        try:
            self.state = 489
            token = self._input.LA(1)
            if token in [misterParser.HEREDA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 486
                self.match(misterParser.HEREDA)
                self.state = 487
                self.AuxPadre = self.getCurrentToken().text
                self.match(misterParser.ID)

            elif token in [misterParser.LLAVE1]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atrib(self):
            return self.getTypedRuleContext(misterParser.AtribContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_classAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterClassAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitClassAux2(self)




    def classAux2(self):

        localctx = misterParser.ClassAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_classAux2)
        try:
            self.state = 493
            token = self._input.LA(1)
            if token in [misterParser.ATRIBUTOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.atrib()

            elif token in [misterParser.METODOS, misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClassAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metod(self):
            return self.getTypedRuleContext(misterParser.MetodContext,0)


        def getRuleIndex(self):
            return misterParser.RULE_classAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterClassAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitClassAux3(self)




    def classAux3(self):

        localctx = misterParser.ClassAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_classAux3)
        try:
            self.state = 497
            token = self._input.LA(1)
            if token in [misterParser.METODOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
                self.metod()

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ATRIBUTOS(self):
            return self.getToken(misterParser.ATRIBUTOS, 0)

        def DOSPUNTOS(self):
            return self.getToken(misterParser.DOSPUNTOS, 0)

        def atribAux1(self):
            return self.getTypedRuleContext(misterParser.AtribAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_atrib

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtrib(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtrib(self)




    def atrib(self):

        localctx = misterParser.AtribContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(misterParser.ATRIBUTOS)
            self.state = 500
            self.match(misterParser.DOSPUNTOS)
            self.state = 501
            self.atribAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribAux2(self):
            return self.getTypedRuleContext(misterParser.AtribAux2Context,0)


        def v_varsAtrib(self):
            return self.getTypedRuleContext(misterParser.V_varsAtribContext,0)


        def atribAux3(self):
            return self.getTypedRuleContext(misterParser.AtribAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_atribAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtribAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtribAux1(self)




    def atribAux1(self):

        localctx = misterParser.AtribAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_atribAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.atribAux2()
            self.state = 504
            self.v_varsAtrib()
            self.state = 505
            self.AuxVisVar = None
            self.atribAux3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLICO(self):
            return self.getToken(misterParser.PUBLICO, 0)

        def PRIVADO(self):
            return self.getToken(misterParser.PRIVADO, 0)

        def getRuleIndex(self):
            return misterParser.RULE_atribAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtribAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtribAux2(self)




    def atribAux2(self):

        localctx = misterParser.AtribAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_atribAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            _la = self._input.LA(1)
            self.AuxVisVar = self.getCurrentToken().text
            if not(_la==misterParser.PRIVADO or _la==misterParser.PUBLICO):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtribAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atribAux1(self):
            return self.getTypedRuleContext(misterParser.AtribAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_atribAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterAtribAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitAtribAux3(self)




    def atribAux3(self):

        localctx = misterParser.AtribAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_atribAux3)
        try:
            self.state = 511
            token = self._input.LA(1)
            if token in [misterParser.PRIVADO, misterParser.PUBLICO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.atribAux1()

            elif token in [misterParser.METODOS, misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def METODOS(self):
            return self.getToken(misterParser.METODOS, 0)

        def DOSPUNTOS(self):
            return self.getToken(misterParser.DOSPUNTOS, 0)

        def metodAux1(self):
            return self.getTypedRuleContext(misterParser.MetodAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_metod

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetod(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetod(self)




    def metod(self):

        localctx = misterParser.MetodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_metod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.match(misterParser.METODOS)
            self.state = 514
            self.match(misterParser.DOSPUNTOS)
            self.state = 515
            self.metodAux1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodAux1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(misterParser.FUNCION, 0)

        def metodAux2(self):
            return self.getTypedRuleContext(misterParser.MetodAux2Context,0)


        def ID(self):
            return self.getToken(misterParser.ID, 0)

        def func(self):
            return self.getTypedRuleContext(misterParser.FuncContext,0)


        def metodAux3(self):
            return self.getTypedRuleContext(misterParser.MetodAux3Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_metodAux1

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetodAux1(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetodAux1(self)




    def metodAux1(self):

        localctx = misterParser.MetodAux1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_metodAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(misterParser.FUNCION)
            self.state = 518
            self.metodAux2()
            self.state = 519
            self.insertarFunc()
            self.asignarDirInicioFuncion(self.funcionActual)
            self.match(misterParser.ID)
            self.terminacionProc = 'ENDPROC'
            self.state = 520
            self.func()
            self.state = 521
            self.metodAux3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodAux2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(misterParser.TipoContext,0)


        def NADA(self):
            return self.getToken(misterParser.NADA, 0)

        def getRuleIndex(self):
            return misterParser.RULE_metodAux2

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetodAux2(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetodAux2(self)




    def metodAux2(self):

        localctx = misterParser.MetodAux2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_metodAux2)
        try:
            self.state = 525
            token = self._input.LA(1)
            self.RetornoTipo = self.getCurrentToken().text
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.AuxTipo = self.getCurrentToken().text
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.match(misterParser.NADA)
                self.AuxTipo = "NADA"

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodAux3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def metodAux1(self):
            return self.getTypedRuleContext(misterParser.MetodAux1Context,0)


        def getRuleIndex(self):
            return misterParser.RULE_metodAux3

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.enterMetodAux3(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, misterListener ):
                listener.exitMetodAux3(self)




    def metodAux3(self):

        localctx = misterParser.MetodAux3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_metodAux3)
        try:
            self.state = 529
            token = self._input.LA(1)
            if token in [misterParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.metodAux1()

            elif token in [misterParser.LLAVE2]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




