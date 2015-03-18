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
        buf.write("\u0208\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\5\3\u009c\n\3\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\3\5\5\5\u00a9\n\5\3\6\3\6\3\6\5\6\u00ae")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\b\3\b\5\b\u00b6\n\b\3\t\3\t\3\t")
        buf.write("\3\n\3\n\3\n\5\n\u00be\n\n\3\13\3\13\3\13\3\f\3\f\3\f")
        buf.write("\5\f\u00c6\n\f\3\r\3\r\5\r\u00ca\n\r\3\16\3\16\3\16\3")
        buf.write("\16\3\17\3\17\3\17\3\17\3\17\3\17\5\17\u00d6\n\17\3\20")
        buf.write("\3\20\3\20\3\21\3\21\5\21\u00dd\n\21\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\5\25\u00ef\n\25\3\26\3\26\3\26\3\26\3\26\3")
        buf.write("\26\5\26\u00f7\n\26\3\27\3\27\5\27\u00fb\n\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\5\31\u0106\n\31\3")
        buf.write("\32\3\32\5\32\u010a\n\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\5\33\u0112\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\35\3\35\3\35\3\35\5\35\u011f\n\35\3\36\3\36\3\36\3\36")
        buf.write("\5\36\u0125\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u012c\n")
        buf.write("\37\3 \3 \3 \3!\3!\3!\3!\5!\u0135\n!\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3#\3#\3#\3#\5#\u0141\n#\3$\3$\3$\3%\3%\3&\3&\3&\3")
        buf.write("&\5&\u014c\n&\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5")
        buf.write("(\u015a\n(\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3*\5*\u0167\n")
        buf.write("*\3+\3+\3+\3+\3+\5+\u016e\n+\3,\3,\3,\5,\u0173\n,\3-\3")
        buf.write("-\3-\3.\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0181\n.\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\5/\u018b\n/\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\62\5\62\u0195\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\63\3\64\3\64\5\64\u019f\n\64\3\65\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\65\3\66\3\66\3\66\5\66\u01ab\n\66\3\67\3\67\3")
        buf.write("\67\3\67\3\67\38\38\38\38\58\u01b6\n8\39\39\39\39\39\3")
        buf.write("9\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\5;\u01ca\n;\3<\3")
        buf.write("<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\5>\u01de")
        buf.write("\n>\3?\3?\5?\u01e2\n?\3@\3@\5@\u01e6\n@\3A\3A\3A\3A\3")
        buf.write("B\3B\3B\3B\3C\3C\3D\3D\5D\u01f4\nD\3E\3E\3E\3E\3F\3F\3")
        buf.write("F\3F\3F\3F\3G\3G\5G\u0202\nG\3H\3H\5H\u0206\nH\3H\2\2")
        buf.write("I\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62")
        buf.write("\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082")
        buf.write("\u0084\u0086\u0088\u008a\u008c\u008e\2\7\3\2\n\f\4\2\27")
        buf.write("\27\31\31\4\2\32\32!%\3\2\35\36\3\2\24\25\u01f4\2\u0090")
        buf.write("\3\2\2\2\4\u009b\3\2\2\2\6\u009d\3\2\2\2\b\u00a8\3\2\2")
        buf.write("\2\n\u00ad\3\2\2\2\f\u00af\3\2\2\2\16\u00b5\3\2\2\2\20")
        buf.write("\u00b7\3\2\2\2\22\u00bd\3\2\2\2\24\u00bf\3\2\2\2\26\u00c5")
        buf.write("\3\2\2\2\30\u00c9\3\2\2\2\32\u00cb\3\2\2\2\34\u00d5\3")
        buf.write("\2\2\2\36\u00d7\3\2\2\2 \u00dc\3\2\2\2\"\u00de\3\2\2\2")
        buf.write("$\u00e0\3\2\2\2&\u00e4\3\2\2\2(\u00ee\3\2\2\2*\u00f6\3")
        buf.write("\2\2\2,\u00fa\3\2\2\2.\u00fc\3\2\2\2\60\u0105\3\2\2\2")
        buf.write("\62\u0109\3\2\2\2\64\u0111\3\2\2\2\66\u0113\3\2\2\28\u011e")
        buf.write("\3\2\2\2:\u0124\3\2\2\2<\u012b\3\2\2\2>\u012d\3\2\2\2")
        buf.write("@\u0134\3\2\2\2B\u0136\3\2\2\2D\u0140\3\2\2\2F\u0142\3")
        buf.write("\2\2\2H\u0145\3\2\2\2J\u014b\3\2\2\2L\u014d\3\2\2\2N\u0159")
        buf.write("\3\2\2\2P\u015b\3\2\2\2R\u0166\3\2\2\2T\u016d\3\2\2\2")
        buf.write("V\u0172\3\2\2\2X\u0174\3\2\2\2Z\u0180\3\2\2\2\\\u018a")
        buf.write("\3\2\2\2^\u018c\3\2\2\2`\u018e\3\2\2\2b\u0194\3\2\2\2")
        buf.write("d\u0196\3\2\2\2f\u019e\3\2\2\2h\u01a0\3\2\2\2j\u01aa\3")
        buf.write("\2\2\2l\u01ac\3\2\2\2n\u01b5\3\2\2\2p\u01b7\3\2\2\2r\u01bd")
        buf.write("\3\2\2\2t\u01c9\3\2\2\2v\u01cb\3\2\2\2x\u01d1\3\2\2\2")
        buf.write("z\u01dd\3\2\2\2|\u01e1\3\2\2\2~\u01e5\3\2\2\2\u0080\u01e7")
        buf.write("\3\2\2\2\u0082\u01eb\3\2\2\2\u0084\u01ef\3\2\2\2\u0086")
        buf.write("\u01f3\3\2\2\2\u0088\u01f5\3\2\2\2\u008a\u01f9\3\2\2\2")
        buf.write("\u008c\u0201\3\2\2\2\u008e\u0205\3\2\2\2\u0090\u0091\5")
        buf.write("\4\3\2\u0091\u0092\5\6\4\2\u0092\u0093\7\2\2\3\u0093\3")
        buf.write("\3\2\2\2\u0094\u0095\5\20\t\2\u0095\u0096\5\4\3\2\u0096")
        buf.write("\u009c\3\2\2\2\u0097\u0098\5x=\2\u0098\u0099\5\4\3\2\u0099")
        buf.write("\u009c\3\2\2\2\u009a\u009c\3\2\2\2\u009b\u0094\3\2\2\2")
        buf.write("\u009b\u0097\3\2\2\2\u009b\u009a\3\2\2\2\u009c\5\3\2\2")
        buf.write("\2\u009d\u009e\7\t\2\2\u009e\u009f\5\b\5\2\u009f\7\3\2")
        buf.write("\2\2\u00a0\u00a1\7\n\2\2\u00a1\u00a9\5\n\6\2\u00a2\u00a3")
        buf.write("\7\13\2\2\u00a3\u00a9\5\f\7\2\u00a4\u00a5\7\f\2\2\u00a5")
        buf.write("\u00a9\5\f\7\2\u00a6\u00a7\7\23\2\2\u00a7\u00a9\5\f\7")
        buf.write("\2\u00a8\u00a0\3\2\2\2\u00a8\u00a2\3\2\2\2\u00a8\u00a4")
        buf.write("\3\2\2\2\u00a8\u00a6\3\2\2\2\u00a9\t\3\2\2\2\u00aa\u00ab")
        buf.write("\7\3\2\2\u00ab\u00ae\5\66\34\2\u00ac\u00ae\5\f\7\2\u00ad")
        buf.write("\u00aa\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\13\3\2\2\2\u00af")
        buf.write("\u00b0\7/\2\2\u00b0\u00b1\5\66\34\2\u00b1\u00b2\5\6\4")
        buf.write("\2\u00b2\r\3\2\2\2\u00b3\u00b6\5\"\22\2\u00b4\u00b6\7")
        buf.write("\23\2\2\u00b5\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6")
        buf.write("\17\3\2\2\2\u00b7\u00b8\5\22\n\2\u00b8\u00b9\5\24\13\2")
        buf.write("\u00b9\21\3\2\2\2\u00ba\u00be\7/\2\2\u00bb\u00be\5\"\22")
        buf.write("\2\u00bc\u00be\5$\23\2\u00bd\u00ba\3\2\2\2\u00bd\u00bb")
        buf.write("\3\2\2\2\u00bd\u00bc\3\2\2\2\u00be\23\3\2\2\2\u00bf\u00c0")
        buf.write("\5\32\16\2\u00c0\u00c1\7,\2\2\u00c1\25\3\2\2\2\u00c2\u00c3")
        buf.write("\7\33\2\2\u00c3\u00c6\5\30\r\2\u00c4\u00c6\3\2\2\2\u00c5")
        buf.write("\u00c2\3\2\2\2\u00c5\u00c4\3\2\2\2\u00c6\27\3\2\2\2\u00c7")
        buf.write("\u00ca\5> \2\u00c8\u00ca\5&\24\2\u00c9\u00c7\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca\31\3\2\2\2\u00cb\u00cc\7/\2\2\u00cc")
        buf.write("\u00cd\5\26\f\2\u00cd\u00ce\5\34\17\2\u00ce\33\3\2\2\2")
        buf.write("\u00cf\u00d0\7\34\2\2\u00d0\u00d1\7/\2\2\u00d1\u00d2\5")
        buf.write("\26\f\2\u00d2\u00d3\5\34\17\2\u00d3\u00d6\3\2\2\2\u00d4")
        buf.write("\u00d6\3\2\2\2\u00d5\u00cf\3\2\2\2\u00d5\u00d4\3\2\2\2")
        buf.write("\u00d6\35\3\2\2\2\u00d7\u00d8\5 \21\2\u00d8\u00d9\5\24")
        buf.write("\13\2\u00d9\37\3\2\2\2\u00da\u00dd\5\"\22\2\u00db\u00dd")
        buf.write("\5$\23\2\u00dc\u00da\3\2\2\2\u00dc\u00db\3\2\2\2\u00dd")
        buf.write("!\3\2\2\2\u00de\u00df\t\2\2\2\u00df#\3\2\2\2\u00e0\u00e1")
        buf.write("\7\16\2\2\u00e1\u00e2\5\"\22\2\u00e2\u00e3\7\60\2\2\u00e3")
        buf.write("%\3\2\2\2\u00e4\u00e5\7*\2\2\u00e5\u00e6\5*\26\2\u00e6")
        buf.write("\u00e7\5(\25\2\u00e7\u00e8\7+\2\2\u00e8\'\3\2\2\2\u00e9")
        buf.write("\u00ea\7\34\2\2\u00ea\u00eb\5*\26\2\u00eb\u00ec\5(\25")
        buf.write("\2\u00ec\u00ef\3\2\2\2\u00ed\u00ef\3\2\2\2\u00ee\u00e9")
        buf.write("\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef)\3\2\2\2\u00f0\u00f7")
        buf.write("\7\60\2\2\u00f1\u00f7\7\61\2\2\u00f2\u00f3\5`\61\2\u00f3")
        buf.write("\u00f4\5,\27\2\u00f4\u00f7\3\2\2\2\u00f5\u00f7\7\62\2")
        buf.write("\2\u00f6\u00f0\3\2\2\2\u00f6\u00f1\3\2\2\2\u00f6\u00f2")
        buf.write("\3\2\2\2\u00f6\u00f5\3\2\2\2\u00f7+\3\2\2\2\u00f8\u00fb")
        buf.write("\5P)\2\u00f9\u00fb\3\2\2\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9")
        buf.write("\3\2\2\2\u00fb-\3\2\2\2\u00fc\u00fd\7&\2\2\u00fd\u00fe")
        buf.write("\5\60\31\2\u00fe\u00ff\7\'\2\2\u00ff/\3\2\2\2\u0100\u0101")
        buf.write("\5\62\32\2\u0101\u0102\7/\2\2\u0102\u0103\5\64\33\2\u0103")
        buf.write("\u0106\3\2\2\2\u0104\u0106\3\2\2\2\u0105\u0100\3\2\2\2")
        buf.write("\u0105\u0104\3\2\2\2\u0106\61\3\2\2\2\u0107\u010a\5\"")
        buf.write("\22\2\u0108\u010a\5$\23\2\u0109\u0107\3\2\2\2\u0109\u0108")
        buf.write("\3\2\2\2\u010a\63\3\2\2\2\u010b\u010c\7\34\2\2\u010c\u010d")
        buf.write("\5\62\32\2\u010d\u010e\7/\2\2\u010e\u010f\5\64\33\2\u010f")
        buf.write("\u0112\3\2\2\2\u0110\u0112\3\2\2\2\u0111\u010b\3\2\2\2")
        buf.write("\u0111\u0110\3\2\2\2\u0112\65\3\2\2\2\u0113\u0114\5.\30")
        buf.write("\2\u0114\u0115\7(\2\2\u0115\u0116\58\35\2\u0116\u0117")
        buf.write("\5:\36\2\u0117\u0118\5<\37\2\u0118\u0119\7)\2\2\u0119")
        buf.write("\67\3\2\2\2\u011a\u011b\5\20\t\2\u011b\u011c\58\35\2\u011c")
        buf.write("\u011f\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u011a\3\2\2\2")
        buf.write("\u011e\u011d\3\2\2\2\u011f9\3\2\2\2\u0120\u0121\5D#\2")
        buf.write("\u0121\u0122\5:\36\2\u0122\u0125\3\2\2\2\u0123\u0125\3")
        buf.write("\2\2\2\u0124\u0120\3\2\2\2\u0124\u0123\3\2\2\2\u0125;")
        buf.write("\3\2\2\2\u0126\u0127\7\r\2\2\u0127\u0128\5> \2\u0128\u0129")
        buf.write("\7,\2\2\u0129\u012c\3\2\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write("\u0126\3\2\2\2\u012b\u012a\3\2\2\2\u012c=\3\2\2\2\u012d")
        buf.write("\u012e\5F$\2\u012e\u012f\5@!\2\u012f?\3\2\2\2\u0130\u0131")
        buf.write("\5B\"\2\u0131\u0132\5> \2\u0132\u0135\3\2\2\2\u0133\u0135")
        buf.write("\3\2\2\2\u0134\u0130\3\2\2\2\u0134\u0133\3\2\2\2\u0135")
        buf.write("A\3\2\2\2\u0136\u0137\t\3\2\2\u0137C\3\2\2\2\u0138\u0141")
        buf.write("\5d\63\2\u0139\u0141\5h\65\2\u013a\u013b\5> \2\u013b\u013c")
        buf.write("\7,\2\2\u013c\u0141\3\2\2\2\u013d\u0141\5r:\2\u013e\u0141")
        buf.write("\5p9\2\u013f\u0141\5v<\2\u0140\u0138\3\2\2\2\u0140\u0139")
        buf.write("\3\2\2\2\u0140\u013a\3\2\2\2\u0140\u013d\3\2\2\2\u0140")
        buf.write("\u013e\3\2\2\2\u0140\u013f\3\2\2\2\u0141E\3\2\2\2\u0142")
        buf.write("\u0143\5L\'\2\u0143\u0144\5J&\2\u0144G\3\2\2\2\u0145\u0146")
        buf.write("\t\4\2\2\u0146I\3\2\2\2\u0147\u0148\5H%\2\u0148\u0149")
        buf.write("\5L\'\2\u0149\u014c\3\2\2\2\u014a\u014c\3\2\2\2\u014b")
        buf.write("\u0147\3\2\2\2\u014b\u014a\3\2\2\2\u014cK\3\2\2\2\u014d")
        buf.write("\u014e\5X-\2\u014e\u014f\5N(\2\u014fM\3\2\2\2\u0150\u0151")
        buf.write("\7\35\2\2\u0151\u0152\5X-\2\u0152\u0153\5N(\2\u0153\u015a")
        buf.write("\3\2\2\2\u0154\u0155\7\36\2\2\u0155\u0156\5X-\2\u0156")
        buf.write("\u0157\5N(\2\u0157\u015a\3\2\2\2\u0158\u015a\3\2\2\2\u0159")
        buf.write("\u0150\3\2\2\2\u0159\u0154\3\2\2\2\u0159\u0158\3\2\2\2")
        buf.write("\u015aO\3\2\2\2\u015b\u015c\7&\2\2\u015c\u015d\5R*\2\u015d")
        buf.write("\u015e\7\'\2\2\u015eQ\3\2\2\2\u015f\u0160\5> \2\u0160")
        buf.write("\u0161\5T+\2\u0161\u0167\3\2\2\2\u0162\u0163\7\30\2\2")
        buf.write("\u0163\u0164\7/\2\2\u0164\u0167\5T+\2\u0165\u0167\3\2")
        buf.write("\2\2\u0166\u015f\3\2\2\2\u0166\u0162\3\2\2\2\u0166\u0165")
        buf.write("\3\2\2\2\u0167S\3\2\2\2\u0168\u0169\7\34\2\2\u0169\u016a")
        buf.write("\5V,\2\u016a\u016b\5T+\2\u016b\u016e\3\2\2\2\u016c\u016e")
        buf.write("\3\2\2\2\u016d\u0168\3\2\2\2\u016d\u016c\3\2\2\2\u016e")
        buf.write("U\3\2\2\2\u016f\u0173\5> \2\u0170\u0171\7\30\2\2\u0171")
        buf.write("\u0173\7/\2\2\u0172\u016f\3\2\2\2\u0172\u0170\3\2\2\2")
        buf.write("\u0173W\3\2\2\2\u0174\u0175\5\\/\2\u0175\u0176\5Z.\2\u0176")
        buf.write("Y\3\2\2\2\u0177\u0178\7 \2\2\u0178\u0179\5\\/\2\u0179")
        buf.write("\u017a\5Z.\2\u017a\u0181\3\2\2\2\u017b\u017c\7\37\2\2")
        buf.write("\u017c\u017d\5\\/\2\u017d\u017e\5Z.\2\u017e\u0181\3\2")
        buf.write("\2\2\u017f\u0181\3\2\2\2\u0180\u0177\3\2\2\2\u0180\u017b")
        buf.write("\3\2\2\2\u0180\u017f\3\2\2\2\u0181[\3\2\2\2\u0182\u0183")
        buf.write("\7&\2\2\u0183\u0184\5> \2\u0184\u0185\7\'\2\2\u0185\u018b")
        buf.write("\3\2\2\2\u0186\u018b\5*\26\2\u0187\u0188\5^\60\2\u0188")
        buf.write("\u0189\5*\26\2\u0189\u018b\3\2\2\2\u018a\u0182\3\2\2\2")
        buf.write("\u018a\u0186\3\2\2\2\u018a\u0187\3\2\2\2\u018b]\3\2\2")
        buf.write("\2\u018c\u018d\t\5\2\2\u018d_\3\2\2\2\u018e\u018f\7/\2")
        buf.write("\2\u018f\u0190\5b\62\2\u0190a\3\2\2\2\u0191\u0192\7.\2")
        buf.write("\2\u0192\u0195\7/\2\2\u0193\u0195\3\2\2\2\u0194\u0191")
        buf.write("\3\2\2\2\u0194\u0193\3\2\2\2\u0195c\3\2\2\2\u0196\u0197")
        buf.write("\7\26\2\2\u0197\u0198\5`\61\2\u0198\u0199\7\33\2\2\u0199")
        buf.write("\u019a\5f\64\2\u019a\u019b\7,\2\2\u019be\3\2\2\2\u019c")
        buf.write("\u019f\5> \2\u019d\u019f\5&\24\2\u019e\u019c\3\2\2\2\u019e")
        buf.write("\u019d\3\2\2\2\u019fg\3\2\2\2\u01a0\u01a1\7\4\2\2\u01a1")
        buf.write("\u01a2\7&\2\2\u01a2\u01a3\5> \2\u01a3\u01a4\7\'\2\2\u01a4")
        buf.write("\u01a5\5l\67\2\u01a5\u01a6\5j\66\2\u01a6i\3\2\2\2\u01a7")
        buf.write("\u01a8\7\5\2\2\u01a8\u01ab\5l\67\2\u01a9\u01ab\3\2\2\2")
        buf.write("\u01aa\u01a7\3\2\2\2\u01aa\u01a9\3\2\2\2\u01abk\3\2\2")
        buf.write("\2\u01ac\u01ad\7(\2\2\u01ad\u01ae\5D#\2\u01ae\u01af\5")
        buf.write("n8\2\u01af\u01b0\7)\2\2\u01b0m\3\2\2\2\u01b1\u01b2\5D")
        buf.write("#\2\u01b2\u01b3\5n8\2\u01b3\u01b6\3\2\2\2\u01b4\u01b6")
        buf.write("\3\2\2\2\u01b5\u01b1\3\2\2\2\u01b5\u01b4\3\2\2\2\u01b6")
        buf.write("o\3\2\2\2\u01b7\u01b8\7\6\2\2\u01b8\u01b9\7&\2\2\u01b9")
        buf.write("\u01ba\5> \2\u01ba\u01bb\7\'\2\2\u01bb\u01bc\5l\67\2\u01bc")
        buf.write("q\3\2\2\2\u01bd\u01be\7\b\2\2\u01be\u01bf\7&\2\2\u01bf")
        buf.write("\u01c0\5> \2\u01c0\u01c1\5t;\2\u01c1\u01c2\7\'\2\2\u01c2")
        buf.write("\u01c3\7,\2\2\u01c3s\3\2\2\2\u01c4\u01c5\7\34\2\2\u01c5")
        buf.write("\u01c6\5> \2\u01c6\u01c7\5t;\2\u01c7\u01ca\3\2\2\2\u01c8")
        buf.write("\u01ca\3\2\2\2\u01c9\u01c4\3\2\2\2\u01c9\u01c8\3\2\2\2")
        buf.write("\u01cau\3\2\2\2\u01cb\u01cc\7\7\2\2\u01cc\u01cd\7&\2\2")
        buf.write("\u01cd\u01ce\7/\2\2\u01ce\u01cf\7\'\2\2\u01cf\u01d0\7")
        buf.write(",\2\2\u01d0w\3\2\2\2\u01d1\u01d2\7\17\2\2\u01d2\u01d3")
        buf.write("\7/\2\2\u01d3\u01d4\5z>\2\u01d4\u01d5\7(\2\2\u01d5\u01d6")
        buf.write("\5|?\2\u01d6\u01d7\5~@\2\u01d7\u01d8\7)\2\2\u01d8\u01d9")
        buf.write("\7,\2\2\u01d9y\3\2\2\2\u01da\u01db\7\22\2\2\u01db\u01de")
        buf.write("\7/\2\2\u01dc\u01de\3\2\2\2\u01dd\u01da\3\2\2\2\u01dd")
        buf.write("\u01dc\3\2\2\2\u01de{\3\2\2\2\u01df\u01e2\5\u0080A\2\u01e0")
        buf.write("\u01e2\3\2\2\2\u01e1\u01df\3\2\2\2\u01e1\u01e0\3\2\2\2")
        buf.write("\u01e2}\3\2\2\2\u01e3\u01e6\5\u0088E\2\u01e4\u01e6\3\2")
        buf.write("\2\2\u01e5\u01e3\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6\177")
        buf.write("\3\2\2\2\u01e7\u01e8\7\20\2\2\u01e8\u01e9\7-\2\2\u01e9")
        buf.write("\u01ea\5\u0082B\2\u01ea\u0081\3\2\2\2\u01eb\u01ec\5\u0084")
        buf.write("C\2\u01ec\u01ed\5\36\20\2\u01ed\u01ee\5\u0086D\2\u01ee")
        buf.write("\u0083\3\2\2\2\u01ef\u01f0\t\6\2\2\u01f0\u0085\3\2\2\2")
        buf.write("\u01f1\u01f4\5\u0082B\2\u01f2\u01f4\3\2\2\2\u01f3\u01f1")
        buf.write("\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4\u0087\3\2\2\2\u01f5")
        buf.write("\u01f6\7\21\2\2\u01f6\u01f7\7-\2\2\u01f7\u01f8\5\u008a")
        buf.write("F\2\u01f8\u0089\3\2\2\2\u01f9\u01fa\7\t\2\2\u01fa\u01fb")
        buf.write("\5\u008cG\2\u01fb\u01fc\7/\2\2\u01fc\u01fd\5\66\34\2\u01fd")
        buf.write("\u01fe\5\u008eH\2\u01fe\u008b\3\2\2\2\u01ff\u0202\5\"")
        buf.write("\22\2\u0200\u0202\7\23\2\2\u0201\u01ff\3\2\2\2\u0201\u0200")
        buf.write("\3\2\2\2\u0202\u008d\3\2\2\2\u0203\u0206\5\u008aF\2\u0204")
        buf.write("\u0206\3\2\2\2\u0205\u0203\3\2\2\2\u0205\u0204\3\2\2\2")
        buf.write("\u0206\u008f\3\2\2\2(\u009b\u00a8\u00ad\u00b5\u00bd\u00c5")
        buf.write("\u00c9\u00d5\u00dc\u00ee\u00f6\u00fa\u0105\u0109\u0111")
        buf.write("\u011e\u0124\u012b\u0134\u0140\u014b\u0159\u0166\u016d")
        buf.write("\u0172\u0180\u018a\u0194\u019e\u01aa\u01b5\u01c9\u01dd")
        buf.write("\u01e1\u01e5\u01f3\u0201\u0205")
        return buf.getvalue()


class misterParser ( Parser ):
# 0 -> void, 1 -> entero, 2 -> decimal, 3 -> texto, 4 -> lista
    grammarFileName = "java-escape"

    contEnteros = 0

    contDecimal = 0

    contLista = 0

    contTexto = 0

    AuxTipo = None

    AuxTipoVar = None

    AuxVisVar = None

    AuxTipoLista = None

    funcionActual = None

    claseActual = None

    variableActual = None

    contAuxParametroActual = None

    AuxPadre = None

    AuxLongLista = None

    dirPrincipal = {'global':[None, None, None, {}, None, None]}

    semanticaCompuestoAux = None

    semanticaCompuestoAux2 = None

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
    RULE_asignacion = 49
    RULE_asignacionAux1 = 50
    RULE_condicion = 51
    RULE_condicionAux1 = 52
    RULE_bloque = 53
    RULE_bloqueAux1 = 54
    RULE_ciclo = 55
    RULE_escritura = 56
    RULE_escrituraAux1 = 57
    RULE_lectura = 58
    RULE_c_class = 59
    RULE_classAux1 = 60
    RULE_classAux2 = 61
    RULE_classAux3 = 62
    RULE_atrib = 63
    RULE_atribAux1 = 64
    RULE_atribAux2 = 65
    RULE_atribAux3 = 66
    RULE_metod = 67
    RULE_metodAux1 = 68
    RULE_metodAux2 = 69
    RULE_metodAux3 = 70

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
                   "compuestoAux1", "asignacion", "asignacionAux1", "condicion", 
                   "condicionAux1", "bloque", "bloqueAux1", "ciclo", "escritura", 
                   "escrituraAux1", "lectura", "c_class", "classAux1", "classAux2", 
                   "classAux3", "atrib", "atribAux1", "atribAux2", "atribAux3", 
                   "metod", "metodAux1", "metodAux2", "metodAux3" ]

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
            return
        if self.claseActual == None:
            self.dirPrincipal[self.funcionActual] = [self.AuxTipo, None, None, {}, [0,0,0,0], []]
        else:
            self.dirPrincipal[self.claseActual][1][self.funcionActual] = [self.AuxTipo, {}, [0,0,0,0],[]]
        self.AuxTipo = None

    def insertarClase(self):
        if self.dirPrincipal.get(self.claseActual) != None:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Clase ya existente" )
            self._syntaxErrors = self._syntaxErrors + 1
            return
        self.dirPrincipal[self.claseActual] = [None, {}, self.AuxPadre, {}, None, None ]
        self.AuxPadre = None

    def insertarVariable(self):
        direccion = None
        isClase = False
        dicAtributos = {}
        if (self.claseActual == None) or (self.claseActual != None and self.funcionActual != None) :
            if self.AuxTipoVar == "ENTERO":
                direccion = self.contEnteros
                self.contEnteros = self.contEnteros + 1
            elif self.AuxTipoVar == "DECIMAL":
                direccion = self.contDecimal
                self.contDecimal = self.contDecimal + 1
            elif self.AuxTipoVar == "TEXTO":
                direccion = self.contTexto
                self.contTexto = self.contTexto + 1
            elif self.AuxTipoVar == "LISTA":
                direccion = self.contLista
                self.contLista = self.contLista + 1
            else:
                isClase = True
                

        tipo = None
        if self.AuxTipoLista == None and self.AuxTipoVar != "LISTA":
            tipo = self.AuxTipoVar
        else:
            tipo = self.AuxTipoVar + "," + self.AuxTipoLista

        if isClase:
            NombrePadre = self.AuxTipoVar
            direccionAux = None
            while True:
                dictAux = self.dirPrincipal[NombrePadre][3]
                for key in dictAux.keys():

                    if dictAux[key][0] == "ENTERO":
                        direccionAux = self.contEnteros
                        self.contEnteros = self.contEnteros + 1
                    elif dictAux[key][0] == "DECIMAL":
                        direccionAux = self.contDecimal
                        self.contDecimal = self.contDecimal + 1
                    elif dictAux[key][0] == "TEXTO":
                        direccionAux = self.contTexto
                        self.contTexto = self.contTexto + 1
                    else:
                        direccionAux = self.contLista
                        self.contLista = self.contLista + 1
                    dicAtributos[key] = [dictAux[key][0], dictAux[key][1], direccionAux]
                NombrePadre = self.dirPrincipal[NombrePadre][2]
                if NombrePadre == None:
                    break

        if self.claseActual == None:
            if self.funcionActual == None:
                if self.dirPrincipal['global'][3].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return
                self.dirPrincipal['global'][3][self.variableActual] = [tipo, direccion, dicAtributos]
            else:
                if self.dirPrincipal[self.funcionActual][3].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return
                self.dirPrincipal[self.funcionActual][3][self.variableActual] = [tipo, direccion, dicAtributos]
        else:
            if self.funcionActual == None:
                if self.dirPrincipal[self.claseActual][3].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return
                self.dirPrincipal[self.claseActual][3][self.variableActual] = [tipo, self.AuxVisVar, direccion, dicAtributos]
            else:
                if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(self.variableActual) != None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable ya existente" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return
                self.dirPrincipal[self.claseActual][1][self.funcionActual][1][self.variableActual] = [tipo, self.AuxVisVar, direccion, dicAtributos]
        self.variableActual = None

    def checarId(self, variableId):
        if self.claseActual == None:
            if self.funcionActual == None:
                if self.dirPrincipal['global'][3].get(variableId) == None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return
            else:
                if self.dirPrincipal[self.funcionActual][3].get(variableId) == None:
                    if self.dirPrincipal['global'][3].get(variableId) == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        return
        else:
            if self.funcionActual != None:
                if self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(variableId) == None:
                    if self.dirPrincipal[self.claseActual][3].get(variableId) == None:
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Variable no declarada" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        return

    def checarAtributo(self, atributoId):
        varAtributos = None
        if self.claseActual == None:
            if self.funcionActual == None:
                varAtributos = self.dirPrincipal['global'][3][self.semanticaCompuestoAux][2].get(atributoId)
                if varAtributos != None:
                    if varAtributos[1] == 'PRIVADO':
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al atributo" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        return
                else:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Atributo no declarado" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return

            else:
                varAtributos = self.dirPrincipal[self.funcionActual][3][self.semanticaCompuestoAux][2].get(atributoId)
                if varAtributos != None:
                    if varAtributos[1] == 'PRIVADO':
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al atributo" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        return
                
                else:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Atributo no declarado" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return

        else:
            if self.funcionActual != None:
                varAtributos = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][self.semanticaCompuestoAux][3].get(atributoId)
                if varAtributos != None:
                    if varAtributos[1] == 'PRIVADO':
                        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al atributo" )
                        self._syntaxErrors = self._syntaxErrors + 1
                        return
                else:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Atributo no declarado" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return

    def checarMetodo(self):
        if self.semanticaCompuestoAux2 == None:
            if self.claseActual == None:
                if self.dirPrincipal.get(self.semanticaCompuestoAux) == None:
                    print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Funcion no declarada" )
                    self._syntaxErrors = self._syntaxErrors + 1
                    return
            else:
                self.encontrarFuncionClase(self.claseActual)

        else:
            tipo = None
            if self.claseActual == None:
                if self.funcionActual == None:
                    tipo = self.dirPrincipal['global'][3][self.semanticaCompuestoAux][0]
                    
                else:
                    tipo = self.dirPrincipal[self.funcionActual][3][self.semanticaCompuestoAux][0]
            
            else:
                if self.funcionActual == None:
                    tipo = self.dirPrincipal[self.claseActual][3][self.semanticaCompuestoAux][0]

                else:
                    tipo = self.dirPrincipal[self.claseActual][1][self.funcionActual][1][self.semanticaCompuestoAux][0]
                    
            self.encontrarFuncionClase(tipo)

    def encontrarFuncionClase(self, padre):
        if padre in ['ENTERO','DECIMAL','TEXTO','NADA', 'LISTA']:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " No se puede acceder al metodo" )
            self._syntaxErrors = self._syntaxErrors + 1
            return
        
        while True:
            dictAux = self.dirPrincipal[padre][1]
            for key in dictAux.keys():
                if self.semanticaCompuestoAux2 == key:
                    return
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Funcion no declarada" )
        self._syntaxErrors = self._syntaxErrors + 1
        return

    def encontrarTipoFuncionClase(self, padre, funcion):
        while True:
            dictAux = self.dirPrincipal[padre][1]
            for key in dictAux.keys():
                if funcion == key:
                    return dictAux[key][0]
            padre = self.dirPrincipal[padre][2]
            if padre == None:
                break
        return

    def obtenerTipo(self, stringVariable):
        if stringVariable == None || self._syntaxErrors > 0:
            return None
        listaAux = stringVariable.split(".")
        if len(listaAux) == 1:
            if listaAux[0].find("(") > 0:
                listaAux[0] = listaAux[0].replace("(", "")
                if self.claseActual == None:
                    return self.dirPrincipal[listaAux[0]][0]
                else:
                    return encontrarTipoFuncionClase(self.claseActual, listaAux[0])
            else:
                if self.claseActual == None:
                    if self.funcionActual == None:
                        return self.dirPrincipal["global"][3][listaAux[0]][0]
                    else:
                        auxiliar = self.dirPrincipal[self.funcionActual][3].get(listaAux[0])
                        if auxiliar != None:
                            return auxiliar[0]
                        else:
                            return self.dirPrincipal["global"][3][listaAux[0]][0]
                else:
                    if self.funcionActual == None:
                        return self.dirPrincipal[self.claseActual][3][listaAux[0]][0]
                    else:
                        auxiliar = self.dirPrincipal[self.claseActual][1][self.funcionActual][1].get(listaAux[0])
                        if auxiliar != None:
                            return auxiliar[0]
                        else:
                            return self.dirPrincipal[self.claseActual][3][listaAux[0]][0]
        else:
            if listaAux[1].find("(") > 0:
                return encontrarTipoFuncionClase(listaAux[0], listaAux[1].replace("(", ""))
            else:
                return self.dirPrincipal[listaAux[0]][3][listaAux[1]][0]

    def checarClase(self):
        if self.dirPrincipal.get(self.AuxTipoVar) == None:
            print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Clase no declarada" )
            self._syntaxErrors = self._syntaxErrors + 1
            return

    def agregarParametro(self):
        tipo = self.getCurrentToken().text
        if self.claseActual ==  None:
            dic = self.dirPrincipal[self.funcionActual]
            dic[5].append(tipo)
            if tipo == "ENTERO":
                dic[4][0] = dic[4][0] + 1
            elif tipo == "DECIMAL":
                dic[4][1] = dic[4][1] + 1
            elif tipo == "TEXTO":
                dic[4][2] = dic[4][2] + 1
            elif tipo == "LISTA":
                dic[4][3] = dic[4][3] + 1
        else: 
            dic = self.dirPrincipal[self.claseActual][1][self.funcionActual]
            dic[3].append(tipo)
            if tipo == "ENTERO":
                dic[2][0] = dic[2][0] + 1
            elif tipo == "DECIMAL":
                dic[2][1] = dic[2][1] + 1
            elif tipo == "TEXTO":
                dic[2][2] = dic[2][2] + 1
            elif tipo == "LISTA":
                dic[2][3] = dic[2][3] + 1
    
    def checarParametro(self):
        variableParametro = self.getCurrentToken().text
        


    def programa(self):

        localctx = misterParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            auxiliar = cuboSemantico()
            self.programaAux1()
            self.state = 143
            self.programaAux3()
            self.state = 144
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
            self.state = 153
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA, misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.v_vars()
                self.state = 147
                self.programaAux1()

            elif token in [misterParser.CLASE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 149
                self.c_class()
                self.state = 150
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
            self.state = 155
            self.match(misterParser.FUNCION)
            self.state = 156
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
            self.state = 166
            token = self._input.LA(1)
            if token in [misterParser.ENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(misterParser.ENTERO)
                self.state = 159
                self.AuxTipo = "ENTERO"
                self.programaAux6()

            elif token in [misterParser.DECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self.match(misterParser.DECIMAL)
                self.state = 161
                self.AuxTipo = "DECIMAL"
                self.programaAux7()

            elif token in [misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 162
                self.match(misterParser.TEXTO)
                self.state = 163
                self.AuxTipo = "TEXTO"
                self.programaAux7()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 4)
                self.state = 164
                self.match(misterParser.NADA)
                self.state = 165
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
            self.state = 171
            token = self._input.LA(1)
            if token in [misterParser.INICIO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 168
                self.insertarFunc()
                self.match(misterParser.INICIO)
                self.state = 169
                self.func()

            elif token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 170
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
            self.state = 173
            self.insertarFunc()
            self.match(misterParser.ID)
            self.state = 174
            self.func()
            self.state = 175
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
            self.state = 179
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
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
            self.state = 181
            self.varsAux1()
            self.state = 182
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
            self.state = 187
            token = self._input.LA(1)
            self.AuxTipoVar = self.getCurrentToken().text
            if token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(misterParser.ID)
                self.checarClase()

            elif token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 186
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
            self.state = 189
            self.varsAux4()
            self.state = 190
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
            self.state = 195
            token = self._input.LA(1)
            if token in [misterParser.IGUAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 192
                self.match(misterParser.IGUAL)
                self.state = 193
                self.varsAux3()

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
            self.state = 199
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
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
            self.state = 201
            self.variableActual = self.getCurrentToken().text
            self.insertarVariable()
            self.match(misterParser.ID)
            self.state = 202
            self.varsAux2()
            self.state = 203
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
            self.state = 211
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.match(misterParser.COMA)
                self.state = 206
                self.variableActual = self.getCurrentToken().text
                self.insertarVariable()
                self.match(misterParser.ID)
                self.state = 207
                self.varsAux2()
                self.state = 208
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
            self.state = 213
            self.varsAtribAux1()
            self.state = 214
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
            self.state = 218
            token = self._input.LA(1)
            self.AuxTipoVar = self.getCurrentToken().text
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
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
            self.state = 220
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
            self.state = 222
            self.match(misterParser.LISTA)
            self.state = 223
            self.AuxTipoLista = self.getCurrentToken().text
            self.tipo()
            self.state = 224
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
            self.state = 226
            self.match(misterParser.CORCHETE1)
            self.state = 227
            self.valor()
            self.state = 228
            self.cteLAux1()
            self.state = 229
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
            self.state = 236
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.match(misterParser.COMA)
                self.state = 232
                self.valor()
                self.state = 233
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
            self.state = 244
            token = self._input.LA(1)
            if token in [misterParser.CTENTERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 238
                self.match(misterParser.CTENTERO)

            elif token in [misterParser.CTEDECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(misterParser.CTEDECIMAL)

            elif token in [misterParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 240
                self.compuesto()
                self.state = 241
                self.valorAux1()
                semanticaCompuestoAux = None
                semanticaCompuestoAux2 = None


            elif token in [misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.match(misterParser.CTETEXTO)

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
            self.state = 248
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.checarMetodo()
                self.llamarFunc()

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIVISION, misterParser.MULTIPLICACION, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS2, misterParser.CORCHETE2, misterParser.PUNTOYCOMA]:
                if self.semanticaCompuestoAux2 == None:
                    self.checarId(self.semanticaCompuestoAux)
                else:
                    self.checarAtributo(self.semanticaCompuestoAux2)
                self.enterOuterAlt(localctx, 2)


            else:
                if self.semanticaCompuestoAux2 == None:
                    self.checarId(self.semanticaCompuestoAux)
                else:
                    self.checarAtributo(self.semanticaCompuestoAux2)
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
            self.state = 250
            self.match(misterParser.PARENTESIS1)
            self.state = 251
            self.parametrosAux1()
            self.state = 252
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
            self.state = 259
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO, misterParser.LISTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 254
                self.parametrosAux2()
                self.state = 255
                self.variableActual = self.getCurrentToken().text
                self.insertarVariable()
                self.match(misterParser.ID)
                self.state = 256
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
            self.state = 263
            token = self._input.LA(1)
            self.AuxTipoVar = self.getCurrentToken().text
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.agregarParametro()
                self.tipo()

            elif token in [misterParser.LISTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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
            self.state = 271
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.match(misterParser.COMA)
                self.state = 266
                self.parametrosAux2()
                self.state = 267
                self.variableActual = self.getCurrentToken().text
                self.insertarVariable()
                self.match(misterParser.ID)
                self.state = 268
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
            self.state = 273
            self.parametros()
            self.state = 274
            self.match(misterParser.LLAVE1)
            self.state = 275
            self.funcAux1()
            self.state = 276
            self.funcAux2()
            self.state = 277
            self.funcAux3()
            self.state = 278
            self.match(misterParser.LLAVE2)
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
            self.state = 284
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.v_vars()
                self.state = 281
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
            self.state = 290
            token = self._input.LA(1)
            if token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.ASIGNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 286
                self.estatuto()
                self.state = 287
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
            self.state = 297
            token = self._input.LA(1)
            if token in [misterParser.RETORNAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 292
                self.match(misterParser.RETORNAR)
                self.state = 293
                self.expresion()
                self.state = 294
                self.match(misterParser.PUNTOYCOMA)

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
            self.state = 299
            self.declaracion()
            self.state = 300
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
            self.state = 306
            token = self._input.LA(1)
            if token in [misterParser.Y, misterParser.O]:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.expresionAux2()
                self.state = 303
                self.expresion()

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
            self.state = 308
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
            self.state = 318
            token = self._input.LA(1)
            if token in [misterParser.ASIGNAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                self.asignacion()

            elif token in [misterParser.SI]:
                self.enterOuterAlt(localctx, 2)
                self.state = 311
                self.condicion()

            elif token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 3)
                self.state = 312
                self.expresion()
                self.state = 313
                self.match(misterParser.PUNTOYCOMA)

            elif token in [misterParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 4)
                self.state = 315
                self.escritura()

            elif token in [misterParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 5)
                self.state = 316
                self.ciclo()

            elif token in [misterParser.LEER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 317
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
            self.state = 320
            self.exp()
            self.state = 321
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
            self.state = 323
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
            self.state = 329
            token = self._input.LA(1)
            if token in [misterParser.IDENTICO, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.declaracionAux1()
                self.state = 326
                self.exp()

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
            self.state = 331
            self.termino()
            self.state = 332
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
            self.state = 343
            token = self._input.LA(1)
            if token in [misterParser.SUMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 334
                self.match(misterParser.SUMA)
                self.state = 335
                self.termino()
                self.state = 336
                self.expAux1()

            elif token in [misterParser.RESTA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 338
                self.match(misterParser.RESTA)
                self.state = 339
                self.termino()
                self.state = 340
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
            self.state = 345
            self.match(misterParser.PARENTESIS1)
            self.state = 346
            self.llamarFuncAux1()
            self.state = 347
            self.match(misterParser.PARENTESIS2)
            
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
            self.state = 356
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.expresion()
                self.state = 350
                self.llamarFuncAux2()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.match(misterParser.REFERENCIA)
                self.state = 353
                self.match(misterParser.ID)
                self.state = 354
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
            self.state = 363
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 358
                self.match(misterParser.COMA)
                self.state = 359
                self.llamarFuncAux3()
                self.state = 360
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
            self.state = 368
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.expresion()

            elif token in [misterParser.REFERENCIA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
                self.match(misterParser.REFERENCIA)
                self.state = 367
                self.match(misterParser.ID)

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
            self.state = 370
            self.factor()
            self.state = 371
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
            self.state = 382
            token = self._input.LA(1)
            if token in [misterParser.MULTIPLICACION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(misterParser.MULTIPLICACION)
                self.state = 374
                self.factor()
                self.state = 375
                self.terminoAux1()

            elif token in [misterParser.DIVISION]:
                self.enterOuterAlt(localctx, 2)
                self.state = 377
                self.match(misterParser.DIVISION)
                self.state = 378
                self.factor()
                self.state = 379
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
            self.state = 392
            token = self._input.LA(1)
            if token in [misterParser.PARENTESIS1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 384
                self.match(misterParser.PARENTESIS1)
                self.state = 385
                self.expresion()
                self.state = 386
                self.match(misterParser.PARENTESIS2)

            elif token in [misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
                self.valor()

            elif token in [misterParser.SUMA, misterParser.RESTA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 389
                self.factorAux1()
                self.state = 390
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
            self.state = 394
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
            self.state = 396
            self.semanticaCompuestoAux = self.getCurrentToken().text
            self.match(misterParser.ID)
            #self.checarId(self.semanticaCompuestoAux)
            self.state = 397
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

        def ID(self):
            return self.getToken(misterParser.ID, 0)

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
            self.state = 402
            token = self._input.LA(1)
            if token in [misterParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.match(misterParser.PUNTO)
                self.state = 400
                self.semanticaCompuestoAux2 = self.getCurrentToken().text
                self.match(misterParser.ID)

            elif token in [misterParser.Y, misterParser.O, misterParser.IDENTICO, misterParser.IGUAL, misterParser.COMA, misterParser.SUMA, misterParser.RESTA, misterParser.DIVISION, misterParser.MULTIPLICACION, misterParser.DIFERENTE, misterParser.MAYORIGUAL, misterParser.MENORIGUAL, misterParser.MENOR, misterParser.MAYOR, misterParser.PARENTESIS1, misterParser.PARENTESIS2, misterParser.CORCHETE2, misterParser.PUNTOYCOMA]:
                self.semanticaCompuestoAux2 = None
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
        self.enterRule(localctx, 98, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(misterParser.ASIGNAR)
            self.state = 405
            self.compuesto()
            if self.semanticaCompuestoAux2 == None:
                self.checarId(self.semanticaCompuestoAux)
            else:
                self.checarAtributo(self.semanticaCompuestoAux2)
            self.state = 406
            self.match(misterParser.IGUAL)
            self.state = 407
            self.asignacionAux1()
            self.state = 408
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
        self.enterRule(localctx, 100, self.RULE_asignacionAux1)
        try:
            self.state = 412
            token = self._input.LA(1)
            if token in [misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 410
                self.expresion()

            elif token in [misterParser.CORCHETE1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 411
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
        self.enterRule(localctx, 102, self.RULE_condicion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.match(misterParser.SI)
            self.state = 415
            self.match(misterParser.PARENTESIS1)
            self.state = 416
            self.expresion()
            self.state = 417
            self.match(misterParser.PARENTESIS2)
            self.state = 418
            self.bloque()
            self.state = 419
            self.condicionAux1()
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
        self.enterRule(localctx, 104, self.RULE_condicionAux1)
        try:
            self.state = 424
            token = self._input.LA(1)
            if token in [misterParser.SINO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.match(misterParser.SINO)
                self.state = 422
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
        self.enterRule(localctx, 106, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self.match(misterParser.LLAVE1)
            self.state = 427
            self.estatuto()
            self.state = 428
            self.bloqueAux1()
            self.state = 429
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
        self.enterRule(localctx, 108, self.RULE_bloqueAux1)
        try:
            self.state = 435
            token = self._input.LA(1)
            if token in [misterParser.SI, misterParser.MIENTRAS, misterParser.LEER, misterParser.IMPRIMIR, misterParser.ASIGNAR, misterParser.SUMA, misterParser.RESTA, misterParser.PARENTESIS1, misterParser.ID, misterParser.CTENTERO, misterParser.CTEDECIMAL, misterParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.estatuto()
                self.state = 432
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
        self.enterRule(localctx, 110, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(misterParser.MIENTRAS)
            self.state = 438
            self.match(misterParser.PARENTESIS1)
            self.state = 439
            self.expresion()
            self.state = 440
            self.match(misterParser.PARENTESIS2)
            self.state = 441
            self.bloque()
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
        self.enterRule(localctx, 112, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 443
            self.match(misterParser.IMPRIMIR)
            self.state = 444
            self.match(misterParser.PARENTESIS1)
            self.state = 445
            self.expresion()
            self.state = 446
            self.escrituraAux1()
            self.state = 447
            self.match(misterParser.PARENTESIS2)
            self.state = 448
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
        self.enterRule(localctx, 114, self.RULE_escrituraAux1)
        try:
            self.state = 455
            token = self._input.LA(1)
            if token in [misterParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 450
                self.match(misterParser.COMA)
                self.state = 451
                self.expresion()
                self.state = 452
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
        self.enterRule(localctx, 116, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.match(misterParser.LEER)
            self.state = 458
            self.match(misterParser.PARENTESIS1)
            self.state = 459
            self.match(misterParser.ID)
            self.state = 460
            self.match(misterParser.PARENTESIS2)
            self.state = 461
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
        self.enterRule(localctx, 118, self.RULE_c_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.match(misterParser.CLASE)
            self.state = 464
            self.claseActual = self.getCurrentToken().text
            self.match(misterParser.ID)
            self.state = 465
            self.classAux1()
            self.state = 466
            self.insertarClase()
            self.match(misterParser.LLAVE1)
            self.state = 467
            self.classAux2()
            self.state = 468
            self.classAux3()
            self.state = 469
            self.match(misterParser.LLAVE2)
            self.claseActual = None
            self.state = 470
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
        self.enterRule(localctx, 120, self.RULE_classAux1)
        try:
            self.state = 475
            token = self._input.LA(1)
            if token in [misterParser.HEREDA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 472
                self.match(misterParser.HEREDA)
                self.state = 473
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
        self.enterRule(localctx, 122, self.RULE_classAux2)
        try:
            self.state = 479
            token = self._input.LA(1)
            if token in [misterParser.ATRIBUTOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 477
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
        self.enterRule(localctx, 124, self.RULE_classAux3)
        try:
            self.state = 483
            token = self._input.LA(1)
            if token in [misterParser.METODOS]:
                self.enterOuterAlt(localctx, 1)
                self.state = 481
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
        self.enterRule(localctx, 126, self.RULE_atrib)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(misterParser.ATRIBUTOS)
            self.state = 486
            self.match(misterParser.DOSPUNTOS)
            self.state = 487
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
        self.enterRule(localctx, 128, self.RULE_atribAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.atribAux2()
            self.state = 490
            self.v_varsAtrib()
            self.state = 491
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
        self.enterRule(localctx, 130, self.RULE_atribAux2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
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
        self.enterRule(localctx, 132, self.RULE_atribAux3)
        try:
            self.state = 497
            token = self._input.LA(1)
            if token in [misterParser.PRIVADO, misterParser.PUBLICO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 495
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
        self.enterRule(localctx, 134, self.RULE_metod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(misterParser.METODOS)
            self.state = 500
            self.match(misterParser.DOSPUNTOS)
            self.state = 501
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
        self.enterRule(localctx, 136, self.RULE_metodAux1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(misterParser.FUNCION)
            self.state = 504
            self.metodAux2()
            self.state = 505
            self.insertarFunc()
            self.match(misterParser.ID)
            self.state = 506
            self.func()
            self.state = 507
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
        self.enterRule(localctx, 138, self.RULE_metodAux2)
        try:
            self.state = 511
            token = self._input.LA(1)
            if token in [misterParser.ENTERO, misterParser.DECIMAL, misterParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 509
                self.AuxTipo = self.getCurrentToken().text
                self.tipo()

            elif token in [misterParser.NADA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 510
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
        self.enterRule(localctx, 140, self.RULE_metodAux3)
        try:
            self.state = 515
            token = self._input.LA(1)
            if token in [misterParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 513
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




