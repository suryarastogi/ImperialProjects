// Generated from ./WaccLexer.g4 by ANTLR 4.4
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class WaccLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.4", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		WS=1, COMMENT=2, BOOL_LIT=3, STRING_LIT=4, CHAR_LIT=5, PAIR_LIT=6, OPEN_BRACKET=7, 
		CLOSE_BRACKET=8, OPEN_PAREN=9, CLOSE_PAREN=10, DOUBLEQUOTE=11, SINGLEQUOTE=12, 
		INT=13, BOOL=14, CHAR=15, STRING=16, PAIR=17, EQUALS=18, FST=19, SND=20, 
		NEWPAIR=21, CALL=22, COMMA=23, BEGIN=24, END=25, IS=26, SKIP=27, READ=28, 
		FREE=29, RETURN=30, EXIT=31, PRINT=32, PRINTLN=33, IF=34, THEN=35, ELSE=36, 
		FI=37, SEMICOLON=38, WHILE=39, DO=40, DONE=41, MINUS=42, UNARY_OP=43, 
		BIN_OP0=44, BIN_OP1=45, BIN_OP2=46, BIN_OP3=47, BIN_OP4=48, ID=49, INT_LIT=50;
	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] tokenNames = {
		"'\\u0000'", "'\\u0001'", "'\\u0002'", "'\\u0003'", "'\\u0004'", "'\\u0005'", 
		"'\\u0006'", "'\\u0007'", "'\b'", "'\t'", "'\n'", "'\\u000B'", "'\f'", 
		"'\r'", "'\\u000E'", "'\\u000F'", "'\\u0010'", "'\\u0011'", "'\\u0012'", 
		"'\\u0013'", "'\\u0014'", "'\\u0015'", "'\\u0016'", "'\\u0017'", "'\\u0018'", 
		"'\\u0019'", "'\\u001A'", "'\\u001B'", "'\\u001C'", "'\\u001D'", "'\\u001E'", 
		"'\\u001F'", "' '", "'!'", "'\"'", "'#'", "'$'", "'%'", "'&'", "'''", 
		"'('", "')'", "'*'", "'+'", "','", "'-'", "'.'", "'/'", "'0'", "'1'", 
		"'2'"
	};
	public static final String[] ruleNames = {
		"WS", "COMMENT", "BOOL_LIT", "STRING_LIT", "CHAR_LIT", "PAIR_LIT", "OPEN_BRACKET", 
		"CLOSE_BRACKET", "OPEN_PAREN", "CLOSE_PAREN", "DOUBLEQUOTE", "SINGLEQUOTE", 
		"INT", "BOOL", "CHAR", "STRING", "PAIR", "EQUALS", "FST", "SND", "NEWPAIR", 
		"CALL", "COMMA", "BEGIN", "END", "IS", "SKIP", "READ", "FREE", "RETURN", 
		"EXIT", "PRINT", "PRINTLN", "IF", "THEN", "ELSE", "FI", "SEMICOLON", "WHILE", 
		"DO", "DONE", "MINUS", "UNARY_OP", "BIN_OP0", "BIN_OP1", "BIN_OP2", "BIN_OP3", 
		"BIN_OP4", "ID", "INT_LIT", "ESCAPED_CHAR", "CHARACTER"
	};


	public WaccLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "WaccLexer.g4"; }

	@Override
	public String[] getTokenNames() { return tokenNames; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 49: return INT_LIT_sempred((RuleContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean INT_LIT_sempred(RuleContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0: return new Long(getText()) <= 2147483647 && new Long(getText()) >= -2147483648;
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2\64\u016e\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t"+
		" \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t"+
		"+\4,\t,\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64"+
		"\t\64\4\65\t\65\3\2\6\2m\n\2\r\2\16\2n\3\2\3\2\3\3\3\3\7\3u\n\3\f\3\16"+
		"\3x\13\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0087"+
		"\n\4\3\5\3\5\7\5\u008b\n\5\f\5\16\5\u008e\13\5\3\5\3\5\3\6\3\6\3\6\3\6"+
		"\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r"+
		"\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20"+
		"\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\23\3\23"+
		"\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26"+
		"\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\35"+
		"\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37"+
		"\3\37\3\37\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3"+
		"\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3"+
		"(\3(\3(\3(\3)\3)\3)\3*\3*\3*\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3"+
		",\5,\u013c\n,\3-\3-\3.\3.\3/\3/\3/\3/\5/\u0146\n/\3\60\3\60\3\60\3\60"+
		"\3\60\5\60\u014d\n\60\3\61\3\61\3\61\3\61\5\61\u0153\n\61\3\62\5\62\u0156"+
		"\n\62\3\62\7\62\u0159\n\62\f\62\16\62\u015c\13\62\3\63\5\63\u015f\n\63"+
		"\3\63\6\63\u0162\n\63\r\63\16\63\u0163\3\63\3\63\3\64\3\64\3\65\3\65\3"+
		"\65\5\65\u016d\n\65\3v\2\66\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25"+
		"\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32"+
		"\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a"+
		"\62c\63e\64g\2i\2\3\2\13\5\2\13\f\17\17\"\"\5\2\'\',,\61\61\4\2>>@@\5"+
		"\2C\\aac|\6\2\62;C\\aac|\4\2--//\3\2\62;\n\2$$))\62\62^^ddhhppvv\5\2$"+
		"$))^^\u017a\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2"+
		"\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27"+
		"\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2"+
		"\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2"+
		"\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2"+
		"\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2"+
		"\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S"+
		"\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2"+
		"\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\3l\3\2\2\2\5r\3\2\2\2\7\u0086\3"+
		"\2\2\2\t\u0088\3\2\2\2\13\u0091\3\2\2\2\r\u0095\3\2\2\2\17\u009a\3\2\2"+
		"\2\21\u009c\3\2\2\2\23\u009e\3\2\2\2\25\u00a0\3\2\2\2\27\u00a2\3\2\2\2"+
		"\31\u00a4\3\2\2\2\33\u00a6\3\2\2\2\35\u00aa\3\2\2\2\37\u00af\3\2\2\2!"+
		"\u00b4\3\2\2\2#\u00bb\3\2\2\2%\u00c0\3\2\2\2\'\u00c2\3\2\2\2)\u00c6\3"+
		"\2\2\2+\u00ca\3\2\2\2-\u00d2\3\2\2\2/\u00d7\3\2\2\2\61\u00d9\3\2\2\2\63"+
		"\u00df\3\2\2\2\65\u00e3\3\2\2\2\67\u00e6\3\2\2\29\u00eb\3\2\2\2;\u00f0"+
		"\3\2\2\2=\u00f5\3\2\2\2?\u00fc\3\2\2\2A\u0101\3\2\2\2C\u0107\3\2\2\2E"+
		"\u010f\3\2\2\2G\u0112\3\2\2\2I\u0117\3\2\2\2K\u011c\3\2\2\2M\u011f\3\2"+
		"\2\2O\u0121\3\2\2\2Q\u0127\3\2\2\2S\u012a\3\2\2\2U\u012f\3\2\2\2W\u013b"+
		"\3\2\2\2Y\u013d\3\2\2\2[\u013f\3\2\2\2]\u0145\3\2\2\2_\u014c\3\2\2\2a"+
		"\u0152\3\2\2\2c\u0155\3\2\2\2e\u015e\3\2\2\2g\u0167\3\2\2\2i\u016c\3\2"+
		"\2\2km\t\2\2\2lk\3\2\2\2mn\3\2\2\2nl\3\2\2\2no\3\2\2\2op\3\2\2\2pq\b\2"+
		"\2\2q\4\3\2\2\2rv\7%\2\2su\13\2\2\2ts\3\2\2\2ux\3\2\2\2vw\3\2\2\2vt\3"+
		"\2\2\2wy\3\2\2\2xv\3\2\2\2yz\7\f\2\2z{\3\2\2\2{|\b\3\2\2|\6\3\2\2\2}~"+
		"\7v\2\2~\177\7t\2\2\177\u0080\7w\2\2\u0080\u0087\7g\2\2\u0081\u0082\7"+
		"h\2\2\u0082\u0083\7c\2\2\u0083\u0084\7n\2\2\u0084\u0085\7u\2\2\u0085\u0087"+
		"\7g\2\2\u0086}\3\2\2\2\u0086\u0081\3\2\2\2\u0087\b\3\2\2\2\u0088\u008c"+
		"\5\27\f\2\u0089\u008b\5i\65\2\u008a\u0089\3\2\2\2\u008b\u008e\3\2\2\2"+
		"\u008c\u008a\3\2\2\2\u008c\u008d\3\2\2\2\u008d\u008f\3\2\2\2\u008e\u008c"+
		"\3\2\2\2\u008f\u0090\5\27\f\2\u0090\n\3\2\2\2\u0091\u0092\5\31\r\2\u0092"+
		"\u0093\5i\65\2\u0093\u0094\5\31\r\2\u0094\f\3\2\2\2\u0095\u0096\7p\2\2"+
		"\u0096\u0097\7w\2\2\u0097\u0098\7n\2\2\u0098\u0099\7n\2\2\u0099\16\3\2"+
		"\2\2\u009a\u009b\7]\2\2\u009b\20\3\2\2\2\u009c\u009d\7_\2\2\u009d\22\3"+
		"\2\2\2\u009e\u009f\7*\2\2\u009f\24\3\2\2\2\u00a0\u00a1\7+\2\2\u00a1\26"+
		"\3\2\2\2\u00a2\u00a3\7$\2\2\u00a3\30\3\2\2\2\u00a4\u00a5\7)\2\2\u00a5"+
		"\32\3\2\2\2\u00a6\u00a7\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9"+
		"\34\3\2\2\2\u00aa\u00ab\7d\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad\7q\2\2\u00ad"+
		"\u00ae\7n\2\2\u00ae\36\3\2\2\2\u00af\u00b0\7e\2\2\u00b0\u00b1\7j\2\2\u00b1"+
		"\u00b2\7c\2\2\u00b2\u00b3\7t\2\2\u00b3 \3\2\2\2\u00b4\u00b5\7u\2\2\u00b5"+
		"\u00b6\7v\2\2\u00b6\u00b7\7t\2\2\u00b7\u00b8\7k\2\2\u00b8\u00b9\7p\2\2"+
		"\u00b9\u00ba\7i\2\2\u00ba\"\3\2\2\2\u00bb\u00bc\7r\2\2\u00bc\u00bd\7c"+
		"\2\2\u00bd\u00be\7k\2\2\u00be\u00bf\7t\2\2\u00bf$\3\2\2\2\u00c0\u00c1"+
		"\7?\2\2\u00c1&\3\2\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4\7u\2\2\u00c4\u00c5"+
		"\7v\2\2\u00c5(\3\2\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7p\2\2\u00c8\u00c9"+
		"\7f\2\2\u00c9*\3\2\2\2\u00ca\u00cb\7p\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd"+
		"\7y\2\2\u00cd\u00ce\7r\2\2\u00ce\u00cf\7c\2\2\u00cf\u00d0\7k\2\2\u00d0"+
		"\u00d1\7t\2\2\u00d1,\3\2\2\2\u00d2\u00d3\7e\2\2\u00d3\u00d4\7c\2\2\u00d4"+
		"\u00d5\7n\2\2\u00d5\u00d6\7n\2\2\u00d6.\3\2\2\2\u00d7\u00d8\7.\2\2\u00d8"+
		"\60\3\2\2\2\u00d9\u00da\7d\2\2\u00da\u00db\7g\2\2\u00db\u00dc\7i\2\2\u00dc"+
		"\u00dd\7k\2\2\u00dd\u00de\7p\2\2\u00de\62\3\2\2\2\u00df\u00e0\7g\2\2\u00e0"+
		"\u00e1\7p\2\2\u00e1\u00e2\7f\2\2\u00e2\64\3\2\2\2\u00e3\u00e4\7k\2\2\u00e4"+
		"\u00e5\7u\2\2\u00e5\66\3\2\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8\7m\2\2\u00e8"+
		"\u00e9\7k\2\2\u00e9\u00ea\7r\2\2\u00ea8\3\2\2\2\u00eb\u00ec\7t\2\2\u00ec"+
		"\u00ed\7g\2\2\u00ed\u00ee\7c\2\2\u00ee\u00ef\7f\2\2\u00ef:\3\2\2\2\u00f0"+
		"\u00f1\7h\2\2\u00f1\u00f2\7t\2\2\u00f2\u00f3\7g\2\2\u00f3\u00f4\7g\2\2"+
		"\u00f4<\3\2\2\2\u00f5\u00f6\7t\2\2\u00f6\u00f7\7g\2\2\u00f7\u00f8\7v\2"+
		"\2\u00f8\u00f9\7w\2\2\u00f9\u00fa\7t\2\2\u00fa\u00fb\7p\2\2\u00fb>\3\2"+
		"\2\2\u00fc\u00fd\7g\2\2\u00fd\u00fe\7z\2\2\u00fe\u00ff\7k\2\2\u00ff\u0100"+
		"\7v\2\2\u0100@\3\2\2\2\u0101\u0102\7r\2\2\u0102\u0103\7t\2\2\u0103\u0104"+
		"\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106\7v\2\2\u0106B\3\2\2\2\u0107\u0108"+
		"\7r\2\2\u0108\u0109\7t\2\2\u0109\u010a\7k\2\2\u010a\u010b\7p\2\2\u010b"+
		"\u010c\7v\2\2\u010c\u010d\7n\2\2\u010d\u010e\7p\2\2\u010eD\3\2\2\2\u010f"+
		"\u0110\7k\2\2\u0110\u0111\7h\2\2\u0111F\3\2\2\2\u0112\u0113\7v\2\2\u0113"+
		"\u0114\7j\2\2\u0114\u0115\7g\2\2\u0115\u0116\7p\2\2\u0116H\3\2\2\2\u0117"+
		"\u0118\7g\2\2\u0118\u0119\7n\2\2\u0119\u011a\7u\2\2\u011a\u011b\7g\2\2"+
		"\u011bJ\3\2\2\2\u011c\u011d\7h\2\2\u011d\u011e\7k\2\2\u011eL\3\2\2\2\u011f"+
		"\u0120\7=\2\2\u0120N\3\2\2\2\u0121\u0122\7y\2\2\u0122\u0123\7j\2\2\u0123"+
		"\u0124\7k\2\2\u0124\u0125\7n\2\2\u0125\u0126\7g\2\2\u0126P\3\2\2\2\u0127"+
		"\u0128\7f\2\2\u0128\u0129\7q\2\2\u0129R\3\2\2\2\u012a\u012b\7f\2\2\u012b"+
		"\u012c\7q\2\2\u012c\u012d\7p\2\2\u012d\u012e\7g\2\2\u012eT\3\2\2\2\u012f"+
		"\u0130\7/\2\2\u0130V\3\2\2\2\u0131\u013c\7#\2\2\u0132\u0133\7n\2\2\u0133"+
		"\u0134\7g\2\2\u0134\u013c\7p\2\2\u0135\u0136\7q\2\2\u0136\u0137\7t\2\2"+
		"\u0137\u013c\7f\2\2\u0138\u0139\7e\2\2\u0139\u013a\7j\2\2\u013a\u013c"+
		"\7t\2\2\u013b\u0131\3\2\2\2\u013b\u0132\3\2\2\2\u013b\u0135\3\2\2\2\u013b"+
		"\u0138\3\2\2\2\u013cX\3\2\2\2\u013d\u013e\t\3\2\2\u013eZ\3\2\2\2\u013f"+
		"\u0140\7-\2\2\u0140\\\3\2\2\2\u0141\u0142\7?\2\2\u0142\u0146\7?\2\2\u0143"+
		"\u0144\7#\2\2\u0144\u0146\7?\2\2\u0145\u0141\3\2\2\2\u0145\u0143\3\2\2"+
		"\2\u0146^\3\2\2\2\u0147\u0148\7@\2\2\u0148\u014d\7?\2\2\u0149\u014d\t"+
		"\4\2\2\u014a\u014b\7>\2\2\u014b\u014d\7?\2\2\u014c\u0147\3\2\2\2\u014c"+
		"\u0149\3\2\2\2\u014c\u014a\3\2\2\2\u014d`\3\2\2\2\u014e\u014f\7(\2\2\u014f"+
		"\u0153\7(\2\2\u0150\u0151\7~\2\2\u0151\u0153\7~\2\2\u0152\u014e\3\2\2"+
		"\2\u0152\u0150\3\2\2\2\u0153b\3\2\2\2\u0154\u0156\t\5\2\2\u0155\u0154"+
		"\3\2\2\2\u0156\u015a\3\2\2\2\u0157\u0159\t\6\2\2\u0158\u0157\3\2\2\2\u0159"+
		"\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a\u015b\3\2\2\2\u015bd\3\2\2\2"+
		"\u015c\u015a\3\2\2\2\u015d\u015f\t\7\2\2\u015e\u015d\3\2\2\2\u015e\u015f"+
		"\3\2\2\2\u015f\u0161\3\2\2\2\u0160\u0162\t\b\2\2\u0161\u0160\3\2\2\2\u0162"+
		"\u0163\3\2\2\2\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3\2"+
		"\2\2\u0165\u0166\6\63\2\2\u0166f\3\2\2\2\u0167\u0168\t\t\2\2\u0168h\3"+
		"\2\2\2\u0169\u016d\n\n\2\2\u016a\u016b\7^\2\2\u016b\u016d\5g\64\2\u016c"+
		"\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016dj\3\2\2\2\21\2nv\u0086\u008c\u013b"+
		"\u0145\u014c\u0152\u0155\u0158\u015a\u015e\u0163\u016c\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}