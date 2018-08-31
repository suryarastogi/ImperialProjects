// Generated from ./WaccParser.g4 by ANTLR 4.4
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class WaccParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.4", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PRINT=32, PAIR_LIT=6, NEWPAIR=21, DO=40, INT_LIT=50, SINGLEQUOTE=12, MINUS=42, 
		UNARY_OP=43, SEMICOLON=38, ELSE=36, ID=49, IF=34, DONE=41, FST=19, IS=26, 
		READ=28, OPEN_PAREN=9, END=25, THEN=35, CLOSE_PAREN=10, EXIT=31, CALL=22, 
		FI=37, CHAR_LIT=5, PRINTLN=33, SND=20, CLOSE_BRACKET=8, CHAR=15, BEGIN=24, 
		FREE=29, COMMENT=2, DOUBLEQUOTE=11, INT=13, RETURN=30, SKIP=27, WS=1, 
		COMMA=23, EQUALS=18, BOOL_LIT=3, OPEN_BRACKET=7, STRING_LIT=4, BIN_OP0=44, 
		BOOL=14, STRING=16, WHILE=39, BIN_OP1=45, BIN_OP2=46, BIN_OP3=47, PAIR=17, 
		BIN_OP4=48;
	public static final String[] tokenNames = {
		"<INVALID>", "WS", "COMMENT", "BOOL_LIT", "STRING_LIT", "CHAR_LIT", "'null'", 
		"'['", "']'", "'('", "')'", "'\"'", "'''", "'int'", "'bool'", "'char'", 
		"'string'", "'pair'", "'='", "'fst'", "'snd'", "'newpair'", "'call'", 
		"','", "'begin'", "'end'", "'is'", "'skip'", "'read'", "'free'", "'return'", 
		"'exit'", "'print'", "'println'", "'if'", "'then'", "'else'", "'fi'", 
		"';'", "'while'", "'do'", "'done'", "'-'", "UNARY_OP", "BIN_OP0", "'+'", 
		"BIN_OP2", "BIN_OP3", "BIN_OP4", "ID", "INT_LIT"
	};
	public static final int
		RULE_start = 0, RULE_prog = 1, RULE_func = 2, RULE_param_list = 3, RULE_param = 4, 
		RULE_stat = 5, RULE_assign_lhs = 6, RULE_assign_rhs = 7, RULE_arg_list = 8, 
		RULE_pair_elem = 9, RULE_type = 10, RULE_base_type = 11, RULE_array_type = 12, 
		RULE_pair_type = 13, RULE_pair_elem_type = 14, RULE_expr = 15, RULE_array_elem = 16, 
		RULE_array_lit = 17;
	public static final String[] ruleNames = {
		"start", "prog", "func", "param_list", "param", "stat", "assign_lhs", 
		"assign_rhs", "arg_list", "pair_elem", "type", "base_type", "array_type", 
		"pair_type", "pair_elem_type", "expr", "array_elem", "array_lit"
	};

	@Override
	public String getGrammarFileName() { return "WaccParser.g4"; }

	@Override
	public String[] getTokenNames() { return tokenNames; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public WaccParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(WaccParser.EOF, 0); }
		public ProgContext prog() {
			return getRuleContext(ProgContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitStart(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitStart(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(36); prog();
			setState(37); match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgContext extends ParserRuleContext {
		public List<FuncContext> func() {
			return getRuleContexts(FuncContext.class);
		}
		public FuncContext func(int i) {
			return getRuleContext(FuncContext.class,i);
		}
		public TerminalNode BEGIN() { return getToken(WaccParser.BEGIN, 0); }
		public TerminalNode END() { return getToken(WaccParser.END, 0); }
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitProg(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitProg(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prog);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(39); match(BEGIN);
			setState(43);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(40); func();
					}
					} 
				}
				setState(45);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,0,_ctx);
			}
			setState(46); stat(0);
			setState(47); match(END);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FuncContext extends ParserRuleContext {
		public int rs;
		public int ps;
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public TerminalNode CLOSE_PAREN() { return getToken(WaccParser.CLOSE_PAREN, 0); }
		public TerminalNode IS() { return getToken(WaccParser.IS, 0); }
		public Param_listContext param_list() {
			return getRuleContext(Param_listContext.class,0);
		}
		public TerminalNode END() { return getToken(WaccParser.END, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public StatContext stat() {
			return getRuleContext(StatContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(WaccParser.OPEN_PAREN, 0); }
		public FuncContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_func; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterFunc(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitFunc(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitFunc(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FuncContext func() throws RecognitionException {
		FuncContext _localctx = new FuncContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_func);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(49); type();
			setState(50); match(ID);
			setState(51); match(OPEN_PAREN);
			setState(53);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << BOOL) | (1L << CHAR) | (1L << STRING) | (1L << PAIR))) != 0)) {
				{
				setState(52); param_list();
				}
			}

			setState(55); match(CLOSE_PAREN);
			setState(56); match(IS);
			setState(57); stat(1);
			setState(58); match(END);
			setState(59);
			if (!(_localctx.rs > 0)) throw new FailedPredicateException(this, "$rs > 0");
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Param_listContext extends ParserRuleContext {
		public List<ParamContext> param() {
			return getRuleContexts(ParamContext.class);
		}
		public List<TerminalNode> COMMA() { return getTokens(WaccParser.COMMA); }
		public ParamContext param(int i) {
			return getRuleContext(ParamContext.class,i);
		}
		public TerminalNode COMMA(int i) {
			return getToken(WaccParser.COMMA, i);
		}
		public Param_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterParam_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitParam_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitParam_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Param_listContext param_list() throws RecognitionException {
		Param_listContext _localctx = new Param_listContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_param_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61); param();
			setState(66);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(62); match(COMMA);
				setState(63); param();
				}
				}
				setState(68);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ParamContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ParamContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_param; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterParam(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitParam(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitParam(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ParamContext param() throws RecognitionException {
		ParamContext _localctx = new ParamContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_param);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69); type();
			setState(70); match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatContext extends ParserRuleContext {
		public int x;
		public TerminalNode SEMICOLON() { return getToken(WaccParser.SEMICOLON, 0); }
		public TerminalNode ELSE() { return getToken(WaccParser.ELSE, 0); }
		public TerminalNode IF() { return getToken(WaccParser.IF, 0); }
		public TerminalNode FREE() { return getToken(WaccParser.FREE, 0); }
		public TerminalNode READ() { return getToken(WaccParser.READ, 0); }
		public TerminalNode FI() { return getToken(WaccParser.FI, 0); }
		public TerminalNode DONE() { return getToken(WaccParser.DONE, 0); }
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public TerminalNode EQUALS() { return getToken(WaccParser.EQUALS, 0); }
		public TerminalNode RETURN() { return getToken(WaccParser.RETURN, 0); }
		public TerminalNode DO() { return getToken(WaccParser.DO, 0); }
		public Assign_rhsContext assign_rhs() {
			return getRuleContext(Assign_rhsContext.class,0);
		}
		public TerminalNode SKIP() { return getToken(WaccParser.SKIP, 0); }
		public StatContext stat(int i) {
			return getRuleContext(StatContext.class,i);
		}
		public TerminalNode BEGIN() { return getToken(WaccParser.BEGIN, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode PRINT() { return getToken(WaccParser.PRINT, 0); }
		public TerminalNode THEN() { return getToken(WaccParser.THEN, 0); }
		public List<StatContext> stat() {
			return getRuleContexts(StatContext.class);
		}
		public TerminalNode WHILE() { return getToken(WaccParser.WHILE, 0); }
		public TerminalNode EXIT() { return getToken(WaccParser.EXIT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode PRINTLN() { return getToken(WaccParser.PRINTLN, 0); }
		public TerminalNode END() { return getToken(WaccParser.END, 0); }
		public Assign_lhsContext assign_lhs() {
			return getRuleContext(Assign_lhsContext.class,0);
		}
		public StatContext(ParserRuleContext parent, int invokingState) { super(parent, invokingState); }
		public StatContext(ParserRuleContext parent, int invokingState, int x) {
			super(parent, invokingState);
			this.x = x;
		}
		@Override public int getRuleIndex() { return RULE_stat; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterStat(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitStat(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitStat(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatContext stat(int x) throws RecognitionException {
		StatContext _localctx = new StatContext(_ctx, getState(), x);
		enterRule(_localctx, 10, RULE_stat);
		int _la;
		try {
			setState(189);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(72); match(SKIP);
				setState(75);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(73); match(SEMICOLON);
					setState(74); stat(_localctx.x);
					}
				}

				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(77); type();
				setState(78); match(ID);
				setState(79); match(EQUALS);
				setState(80); assign_rhs();
				setState(83);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(81); match(SEMICOLON);
					setState(82); stat(_localctx.x);
					}
				}

				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(85); assign_lhs();
				setState(86); match(EQUALS);
				setState(87); assign_rhs();
				setState(90);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(88); match(SEMICOLON);
					setState(89); stat(_localctx.x);
					}
				}

				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(92); match(READ);
				setState(93); assign_lhs();
				setState(96);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(94); match(SEMICOLON);
					setState(95); stat(_localctx.x);
					}
				}

				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(98); match(FREE);
				setState(99); expr(0);
				setState(102);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(100); match(SEMICOLON);
					setState(101); stat(_localctx.x);
					}
				}

				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(104);
				if (!(_localctx.x == 0)) throw new FailedPredicateException(this, "$x == 0");
				setState(105); match(EXIT);
				setState(106); expr(0);
				setState(109);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(107); match(SEMICOLON);
					setState(108); stat(_localctx.x);
					}
				}

				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(111);
				if (!(_localctx.x == 1)) throw new FailedPredicateException(this, "$x == 1");
				setState(112); match(EXIT);
				setState(113); expr(0);
				((FuncContext)getInvokingContext(2)).rs++;
				setState(117);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(115); match(SEMICOLON);
					setState(116); stat(_localctx.x);
					}
				}

				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(119); match(PRINT);
				setState(120); expr(0);
				setState(123);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(121); match(SEMICOLON);
					setState(122); stat(_localctx.x);
					}
				}

				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(125); match(PRINTLN);
				setState(126); expr(0);
				setState(129);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(127); match(SEMICOLON);
					setState(128); stat(_localctx.x);
					}
				}

				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(131);
				if (!(_localctx.x == 1)) throw new FailedPredicateException(this, "$x == 1");
				setState(132); match(RETURN);
				setState(133); expr(0);
				((FuncContext)getInvokingContext(2)).rs++;
				setState(137);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(135); match(SEMICOLON);
					setState(136); stat(_localctx.x);
					}
				}

				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(139);
				if (!(_localctx.x == 0)) throw new FailedPredicateException(this, "$x == 0");
				setState(140); match(RETURN);
				setState(141); expr(0);
				setState(144);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(142); match(SEMICOLON);
					setState(143); stat(_localctx.x);
					}
				}

				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(146);
				if (!(_localctx.x == 1)) throw new FailedPredicateException(this, "$x == 1");
				setState(147); match(IF);
				setState(148); expr(0);
				((FuncContext)getInvokingContext(2)).rs =  0;
				setState(150); match(THEN);
				setState(151); stat(_localctx.x);
				((FuncContext)getInvokingContext(2)).ps =  ((FuncContext)getInvokingContext(2)).rs; ((FuncContext)getInvokingContext(2)).rs =  0;
				setState(153); match(ELSE);
				setState(154); stat(_localctx.x);
				if(((FuncContext)getInvokingContext(2)).ps != ((FuncContext)getInvokingContext(2)).rs) {((FuncContext)getInvokingContext(2)).rs =  0;}
				setState(156); match(FI);
				setState(159);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(157); match(SEMICOLON);
					setState(158); stat(_localctx.x);
					}
				}

				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(161);
				if (!(_localctx.x == 0)) throw new FailedPredicateException(this, "$x == 0");
				setState(162); match(IF);
				setState(163); expr(0);
				setState(164); match(THEN);
				setState(165); stat(_localctx.x);
				setState(166); match(ELSE);
				setState(167); stat(_localctx.x);
				setState(168); match(FI);
				setState(171);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(169); match(SEMICOLON);
					setState(170); stat(_localctx.x);
					}
				}

				}
				break;
			case 14:
				enterOuterAlt(_localctx, 14);
				{
				setState(173); match(WHILE);
				setState(174); expr(0);
				setState(175); match(DO);
				setState(176); stat(_localctx.x);
				setState(177); match(DONE);
				setState(180);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(178); match(SEMICOLON);
					setState(179); stat(_localctx.x);
					}
				}

				}
				break;
			case 15:
				enterOuterAlt(_localctx, 15);
				{
				setState(182); match(BEGIN);
				setState(183); stat(_localctx.x);
				setState(184); match(END);
				setState(187);
				_la = _input.LA(1);
				if (_la==SEMICOLON) {
					{
					setState(185); match(SEMICOLON);
					setState(186); stat(_localctx.x);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_lhsContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public Pair_elemContext pair_elem() {
			return getRuleContext(Pair_elemContext.class,0);
		}
		public Array_elemContext array_elem() {
			return getRuleContext(Array_elemContext.class,0);
		}
		public Assign_lhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_lhs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterAssign_lhs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitAssign_lhs(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitAssign_lhs(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Assign_lhsContext assign_lhs() throws RecognitionException {
		Assign_lhsContext _localctx = new Assign_lhsContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_assign_lhs);
		try {
			setState(194);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(191); match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(192); array_elem();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(193); pair_elem();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Assign_rhsContext extends ParserRuleContext {
		public TerminalNode NEWPAIR() { return getToken(WaccParser.NEWPAIR, 0); }
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(WaccParser.CLOSE_PAREN, 0); }
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode COMMA() { return getToken(WaccParser.COMMA, 0); }
		public TerminalNode CALL() { return getToken(WaccParser.CALL, 0); }
		public Pair_elemContext pair_elem() {
			return getRuleContext(Pair_elemContext.class,0);
		}
		public Arg_listContext arg_list() {
			return getRuleContext(Arg_listContext.class,0);
		}
		public Array_litContext array_lit() {
			return getRuleContext(Array_litContext.class,0);
		}
		public TerminalNode OPEN_PAREN() { return getToken(WaccParser.OPEN_PAREN, 0); }
		public Assign_rhsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign_rhs; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterAssign_rhs(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitAssign_rhs(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitAssign_rhs(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Assign_rhsContext assign_rhs() throws RecognitionException {
		Assign_rhsContext _localctx = new Assign_rhsContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_assign_rhs);
		int _la;
		try {
			setState(213);
			switch (_input.LA(1)) {
			case BOOL_LIT:
			case STRING_LIT:
			case CHAR_LIT:
			case PAIR_LIT:
			case OPEN_PAREN:
			case MINUS:
			case UNARY_OP:
			case ID:
			case INT_LIT:
				enterOuterAlt(_localctx, 1);
				{
				setState(196); expr(0);
				}
				break;
			case OPEN_BRACKET:
				enterOuterAlt(_localctx, 2);
				{
				setState(197); array_lit();
				}
				break;
			case NEWPAIR:
				enterOuterAlt(_localctx, 3);
				{
				setState(198); match(NEWPAIR);
				setState(199); match(OPEN_PAREN);
				setState(200); expr(0);
				setState(201); match(COMMA);
				setState(202); expr(0);
				setState(203); match(CLOSE_PAREN);
				}
				break;
			case FST:
			case SND:
				enterOuterAlt(_localctx, 4);
				{
				setState(205); pair_elem();
				}
				break;
			case CALL:
				enterOuterAlt(_localctx, 5);
				{
				setState(206); match(CALL);
				setState(207); match(ID);
				setState(208); match(OPEN_PAREN);
				setState(210);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << CHAR_LIT) | (1L << PAIR_LIT) | (1L << OPEN_PAREN) | (1L << MINUS) | (1L << UNARY_OP) | (1L << ID) | (1L << INT_LIT))) != 0)) {
					{
					setState(209); arg_list();
					}
				}

				setState(212); match(CLOSE_PAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arg_listContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(WaccParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(WaccParser.COMMA, i);
		}
		public Arg_listContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg_list; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterArg_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitArg_list(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitArg_list(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Arg_listContext arg_list() throws RecognitionException {
		Arg_listContext _localctx = new Arg_listContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_arg_list);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(215); expr(0);
			setState(220);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==COMMA) {
				{
				{
				setState(216); match(COMMA);
				setState(217); expr(0);
				}
				}
				setState(222);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pair_elemContext extends ParserRuleContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode SND() { return getToken(WaccParser.SND, 0); }
		public TerminalNode FST() { return getToken(WaccParser.FST, 0); }
		public Pair_elemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pair_elem; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterPair_elem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitPair_elem(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitPair_elem(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Pair_elemContext pair_elem() throws RecognitionException {
		Pair_elemContext _localctx = new Pair_elemContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_pair_elem);
		try {
			setState(227);
			switch (_input.LA(1)) {
			case FST:
				enterOuterAlt(_localctx, 1);
				{
				setState(223); match(FST);
				setState(224); expr(0);
				}
				break;
			case SND:
				enterOuterAlt(_localctx, 2);
				{
				setState(225); match(SND);
				setState(226); expr(0);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypeContext extends ParserRuleContext {
		public Pair_typeContext pair_type() {
			return getRuleContext(Pair_typeContext.class,0);
		}
		public Base_typeContext base_type() {
			return getRuleContext(Base_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitType(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitType(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_type);
		try {
			setState(232);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(229); base_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(230); array_type();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(231); pair_type();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Base_typeContext extends ParserRuleContext {
		public TerminalNode BOOL() { return getToken(WaccParser.BOOL, 0); }
		public TerminalNode STRING() { return getToken(WaccParser.STRING, 0); }
		public TerminalNode CHAR() { return getToken(WaccParser.CHAR, 0); }
		public TerminalNode INT() { return getToken(WaccParser.INT, 0); }
		public Base_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_base_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterBase_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitBase_type(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitBase_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Base_typeContext base_type() throws RecognitionException {
		Base_typeContext _localctx = new Base_typeContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_base_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(234);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << BOOL) | (1L << CHAR) | (1L << STRING))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			consume();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_typeContext extends ParserRuleContext {
		public Pair_typeContext pair_type() {
			return getRuleContext(Pair_typeContext.class,0);
		}
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(WaccParser.OPEN_BRACKET); }
		public Base_typeContext base_type() {
			return getRuleContext(Base_typeContext.class,0);
		}
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(WaccParser.OPEN_BRACKET, i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(WaccParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(WaccParser.CLOSE_BRACKET, i);
		}
		public Array_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterArray_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitArray_type(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitArray_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_typeContext array_type() throws RecognitionException {
		Array_typeContext _localctx = new Array_typeContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_array_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			switch (_input.LA(1)) {
			case INT:
			case BOOL:
			case CHAR:
			case STRING:
				{
				setState(236); base_type();
				}
				break;
			case PAIR:
				{
				setState(237); pair_type();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(242); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(240); match(OPEN_BRACKET);
				setState(241); match(CLOSE_BRACKET);
				}
				}
				setState(244); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==OPEN_BRACKET );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pair_typeContext extends ParserRuleContext {
		public List<Pair_elem_typeContext> pair_elem_type() {
			return getRuleContexts(Pair_elem_typeContext.class);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(WaccParser.CLOSE_PAREN, 0); }
		public TerminalNode PAIR() { return getToken(WaccParser.PAIR, 0); }
		public TerminalNode COMMA() { return getToken(WaccParser.COMMA, 0); }
		public Pair_elem_typeContext pair_elem_type(int i) {
			return getRuleContext(Pair_elem_typeContext.class,i);
		}
		public TerminalNode OPEN_PAREN() { return getToken(WaccParser.OPEN_PAREN, 0); }
		public Pair_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pair_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterPair_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitPair_type(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitPair_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Pair_typeContext pair_type() throws RecognitionException {
		Pair_typeContext _localctx = new Pair_typeContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_pair_type);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(246); match(PAIR);
			setState(247); match(OPEN_PAREN);
			setState(248); pair_elem_type();
			setState(249); match(COMMA);
			setState(250); pair_elem_type();
			setState(251); match(CLOSE_PAREN);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Pair_elem_typeContext extends ParserRuleContext {
		public TerminalNode PAIR() { return getToken(WaccParser.PAIR, 0); }
		public Base_typeContext base_type() {
			return getRuleContext(Base_typeContext.class,0);
		}
		public Array_typeContext array_type() {
			return getRuleContext(Array_typeContext.class,0);
		}
		public Pair_elem_typeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pair_elem_type; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterPair_elem_type(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitPair_elem_type(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitPair_elem_type(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Pair_elem_typeContext pair_elem_type() throws RecognitionException {
		Pair_elem_typeContext _localctx = new Pair_elem_typeContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_pair_elem_type);
		try {
			setState(256);
			switch ( getInterpreter().adaptivePredict(_input,27,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(253); base_type();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(254); array_type();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(255); match(PAIR);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public TerminalNode BIN_OP3() { return getToken(WaccParser.BIN_OP3, 0); }
		public TerminalNode BIN_OP4() { return getToken(WaccParser.BIN_OP4, 0); }
		public TerminalNode CHAR_LIT() { return getToken(WaccParser.CHAR_LIT, 0); }
		public TerminalNode BIN_OP0() { return getToken(WaccParser.BIN_OP0, 0); }
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode UNARY_OP() { return getToken(WaccParser.UNARY_OP, 0); }
		public TerminalNode BIN_OP1() { return getToken(WaccParser.BIN_OP1, 0); }
		public TerminalNode OPEN_PAREN() { return getToken(WaccParser.OPEN_PAREN, 0); }
		public TerminalNode BIN_OP2() { return getToken(WaccParser.BIN_OP2, 0); }
		public TerminalNode INT_LIT() { return getToken(WaccParser.INT_LIT, 0); }
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public TerminalNode PAIR_LIT() { return getToken(WaccParser.PAIR_LIT, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public TerminalNode CLOSE_PAREN() { return getToken(WaccParser.CLOSE_PAREN, 0); }
		public TerminalNode BOOL_LIT() { return getToken(WaccParser.BOOL_LIT, 0); }
		public TerminalNode STRING_LIT() { return getToken(WaccParser.STRING_LIT, 0); }
		public TerminalNode MINUS() { return getToken(WaccParser.MINUS, 0); }
		public Array_elemContext array_elem() {
			return getRuleContext(Array_elemContext.class,0);
		}
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterExpr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitExpr(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitExpr(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 30;
		enterRecursionRule(_localctx, 30, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(272);
			switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
			case 1:
				{
				setState(259);
				_la = _input.LA(1);
				if ( !(_la==MINUS || _la==UNARY_OP) ) {
				_errHandler.recoverInline(this);
				}
				consume();
				setState(260); expr(14);
				}
				break;
			case 2:
				{
				setState(261); match(OPEN_PAREN);
				setState(262); expr(0);
				setState(263); match(CLOSE_PAREN);
				}
				break;
			case 3:
				{
				setState(265); array_elem();
				}
				break;
			case 4:
				{
				setState(266); match(INT_LIT);
				}
				break;
			case 5:
				{
				setState(267); match(BOOL_LIT);
				}
				break;
			case 6:
				{
				setState(268); match(CHAR_LIT);
				}
				break;
			case 7:
				{
				setState(269); match(STRING_LIT);
				}
				break;
			case 8:
				{
				setState(270); match(PAIR_LIT);
				}
				break;
			case 9:
				{
				setState(271); match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(291);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(289);
					switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
					case 1:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(274);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(275); match(BIN_OP0);
						setState(276); expr(14);
						}
						break;
					case 2:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(277);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(278);
						_la = _input.LA(1);
						if ( !(_la==MINUS || _la==BIN_OP1) ) {
						_errHandler.recoverInline(this);
						}
						consume();
						setState(279); expr(13);
						}
						break;
					case 3:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(280);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(281); match(BIN_OP2);
						setState(282); expr(12);
						}
						break;
					case 4:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(283);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(284); match(BIN_OP3);
						setState(285); expr(11);
						}
						break;
					case 5:
						{
						_localctx = new ExprContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(286);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(287); match(BIN_OP4);
						setState(288); expr(10);
						}
						break;
					}
					} 
				}
				setState(293);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,30,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Array_elemContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(WaccParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public List<TerminalNode> OPEN_BRACKET() { return getTokens(WaccParser.OPEN_BRACKET); }
		public TerminalNode OPEN_BRACKET(int i) {
			return getToken(WaccParser.OPEN_BRACKET, i);
		}
		public List<TerminalNode> CLOSE_BRACKET() { return getTokens(WaccParser.CLOSE_BRACKET); }
		public TerminalNode CLOSE_BRACKET(int i) {
			return getToken(WaccParser.CLOSE_BRACKET, i);
		}
		public Array_elemContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_elem; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterArray_elem(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitArray_elem(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitArray_elem(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_elemContext array_elem() throws RecognitionException {
		Array_elemContext _localctx = new Array_elemContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_array_elem);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(294); match(ID);
			setState(299); 
			_errHandler.sync(this);
			_alt = 1;
			do {
				switch (_alt) {
				case 1:
					{
					{
					setState(295); match(OPEN_BRACKET);
					setState(296); expr(0);
					setState(297); match(CLOSE_BRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(301); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			} while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Array_litContext extends ParserRuleContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OPEN_BRACKET() { return getToken(WaccParser.OPEN_BRACKET, 0); }
		public List<TerminalNode> COMMA() { return getTokens(WaccParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(WaccParser.COMMA, i);
		}
		public TerminalNode CLOSE_BRACKET() { return getToken(WaccParser.CLOSE_BRACKET, 0); }
		public Array_litContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array_lit; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).enterArray_lit(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof WaccParserListener ) ((WaccParserListener)listener).exitArray_lit(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof WaccParserVisitor ) return ((WaccParserVisitor<? extends T>)visitor).visitArray_lit(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Array_litContext array_lit() throws RecognitionException {
		Array_litContext _localctx = new Array_litContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_array_lit);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303); match(OPEN_BRACKET);
			setState(312);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << BOOL_LIT) | (1L << STRING_LIT) | (1L << CHAR_LIT) | (1L << PAIR_LIT) | (1L << OPEN_PAREN) | (1L << MINUS) | (1L << UNARY_OP) | (1L << ID) | (1L << INT_LIT))) != 0)) {
				{
				setState(304); expr(0);
				setState(309);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(305); match(COMMA);
					setState(306); expr(0);
					}
					}
					setState(311);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			setState(314); match(CLOSE_BRACKET);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2: return func_sempred((FuncContext)_localctx, predIndex);
		case 5: return stat_sempred((StatContext)_localctx, predIndex);
		case 15: return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean stat_sempred(StatContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1: return _localctx.x == 0;
		case 2: return _localctx.x == 1;
		case 3: return _localctx.x == 1;
		case 4: return _localctx.x == 0;
		case 5: return _localctx.x == 1;
		case 6: return _localctx.x == 0;
		}
		return true;
	}
	private boolean func_sempred(FuncContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0: return _localctx.rs > 0;
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 7: return precpred(_ctx, 13);
		case 8: return precpred(_ctx, 12);
		case 9: return precpred(_ctx, 11);
		case 10: return precpred(_ctx, 10);
		case 11: return precpred(_ctx, 9);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\64\u013f\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\3\2\3\2\3\2\3\3\3\3\7\3,\n\3\f\3\16\3/\13\3\3\3\3\3\3\3\3\4"+
		"\3\4\3\4\3\4\5\48\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\7\5C\n\5\f\5"+
		"\16\5F\13\5\3\6\3\6\3\6\3\7\3\7\3\7\5\7N\n\7\3\7\3\7\3\7\3\7\3\7\3\7\5"+
		"\7V\n\7\3\7\3\7\3\7\3\7\3\7\5\7]\n\7\3\7\3\7\3\7\3\7\5\7c\n\7\3\7\3\7"+
		"\3\7\3\7\5\7i\n\7\3\7\3\7\3\7\3\7\3\7\5\7p\n\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\5\7x\n\7\3\7\3\7\3\7\3\7\5\7~\n\7\3\7\3\7\3\7\3\7\5\7\u0084\n\7\3\7\3"+
		"\7\3\7\3\7\3\7\3\7\5\7\u008c\n\7\3\7\3\7\3\7\3\7\3\7\5\7\u0093\n\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00a2\n\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ae\n\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\5\7\u00b7\n\7\3\7\3\7\3\7\3\7\3\7\5\7\u00be\n\7\5\7\u00c0\n\7\3\b"+
		"\3\b\3\b\5\b\u00c5\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t"+
		"\3\t\3\t\5\t\u00d5\n\t\3\t\5\t\u00d8\n\t\3\n\3\n\3\n\7\n\u00dd\n\n\f\n"+
		"\16\n\u00e0\13\n\3\13\3\13\3\13\3\13\5\13\u00e6\n\13\3\f\3\f\3\f\5\f\u00eb"+
		"\n\f\3\r\3\r\3\16\3\16\5\16\u00f1\n\16\3\16\3\16\6\16\u00f5\n\16\r\16"+
		"\16\16\u00f6\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\20\5\20\u0103"+
		"\n\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\5\21\u0113\n\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21"+
		"\3\21\3\21\3\21\3\21\3\21\7\21\u0124\n\21\f\21\16\21\u0127\13\21\3\22"+
		"\3\22\3\22\3\22\3\22\6\22\u012e\n\22\r\22\16\22\u012f\3\23\3\23\3\23\3"+
		"\23\7\23\u0136\n\23\f\23\16\23\u0139\13\23\5\23\u013b\n\23\3\23\3\23\3"+
		"\23\2\3 \24\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$\2\5\3\2\17\22\3"+
		"\2,-\4\2,,//\u016b\2&\3\2\2\2\4)\3\2\2\2\6\63\3\2\2\2\b?\3\2\2\2\nG\3"+
		"\2\2\2\f\u00bf\3\2\2\2\16\u00c4\3\2\2\2\20\u00d7\3\2\2\2\22\u00d9\3\2"+
		"\2\2\24\u00e5\3\2\2\2\26\u00ea\3\2\2\2\30\u00ec\3\2\2\2\32\u00f0\3\2\2"+
		"\2\34\u00f8\3\2\2\2\36\u0102\3\2\2\2 \u0112\3\2\2\2\"\u0128\3\2\2\2$\u0131"+
		"\3\2\2\2&\'\5\4\3\2\'(\7\2\2\3(\3\3\2\2\2)-\7\32\2\2*,\5\6\4\2+*\3\2\2"+
		"\2,/\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\60\3\2\2\2/-\3\2\2\2\60\61\5\f\7\2\61"+
		"\62\7\33\2\2\62\5\3\2\2\2\63\64\5\26\f\2\64\65\7\63\2\2\65\67\7\13\2\2"+
		"\668\5\b\5\2\67\66\3\2\2\2\678\3\2\2\289\3\2\2\29:\7\f\2\2:;\7\34\2\2"+
		";<\5\f\7\2<=\7\33\2\2=>\6\4\2\3>\7\3\2\2\2?D\5\n\6\2@A\7\31\2\2AC\5\n"+
		"\6\2B@\3\2\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\t\3\2\2\2FD\3\2\2\2GH\5"+
		"\26\f\2HI\7\63\2\2I\13\3\2\2\2JM\7\35\2\2KL\7(\2\2LN\5\f\7\2MK\3\2\2\2"+
		"MN\3\2\2\2N\u00c0\3\2\2\2OP\5\26\f\2PQ\7\63\2\2QR\7\24\2\2RU\5\20\t\2"+
		"ST\7(\2\2TV\5\f\7\2US\3\2\2\2UV\3\2\2\2V\u00c0\3\2\2\2WX\5\16\b\2XY\7"+
		"\24\2\2Y\\\5\20\t\2Z[\7(\2\2[]\5\f\7\2\\Z\3\2\2\2\\]\3\2\2\2]\u00c0\3"+
		"\2\2\2^_\7\36\2\2_b\5\16\b\2`a\7(\2\2ac\5\f\7\2b`\3\2\2\2bc\3\2\2\2c\u00c0"+
		"\3\2\2\2de\7\37\2\2eh\5 \21\2fg\7(\2\2gi\5\f\7\2hf\3\2\2\2hi\3\2\2\2i"+
		"\u00c0\3\2\2\2jk\6\7\3\3kl\7!\2\2lo\5 \21\2mn\7(\2\2np\5\f\7\2om\3\2\2"+
		"\2op\3\2\2\2p\u00c0\3\2\2\2qr\6\7\4\3rs\7!\2\2st\5 \21\2tw\b\7\1\2uv\7"+
		"(\2\2vx\5\f\7\2wu\3\2\2\2wx\3\2\2\2x\u00c0\3\2\2\2yz\7\"\2\2z}\5 \21\2"+
		"{|\7(\2\2|~\5\f\7\2}{\3\2\2\2}~\3\2\2\2~\u00c0\3\2\2\2\177\u0080\7#\2"+
		"\2\u0080\u0083\5 \21\2\u0081\u0082\7(\2\2\u0082\u0084\5\f\7\2\u0083\u0081"+
		"\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u00c0\3\2\2\2\u0085\u0086\6\7\5\3\u0086"+
		"\u0087\7 \2\2\u0087\u0088\5 \21\2\u0088\u008b\b\7\1\2\u0089\u008a\7(\2"+
		"\2\u008a\u008c\5\f\7\2\u008b\u0089\3\2\2\2\u008b\u008c\3\2\2\2\u008c\u00c0"+
		"\3\2\2\2\u008d\u008e\6\7\6\3\u008e\u008f\7 \2\2\u008f\u0092\5 \21\2\u0090"+
		"\u0091\7(\2\2\u0091\u0093\5\f\7\2\u0092\u0090\3\2\2\2\u0092\u0093\3\2"+
		"\2\2\u0093\u00c0\3\2\2\2\u0094\u0095\6\7\7\3\u0095\u0096\7$\2\2\u0096"+
		"\u0097\5 \21\2\u0097\u0098\b\7\1\2\u0098\u0099\7%\2\2\u0099\u009a\5\f"+
		"\7\2\u009a\u009b\b\7\1\2\u009b\u009c\7&\2\2\u009c\u009d\5\f\7\2\u009d"+
		"\u009e\b\7\1\2\u009e\u00a1\7\'\2\2\u009f\u00a0\7(\2\2\u00a0\u00a2\5\f"+
		"\7\2\u00a1\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00c0\3\2\2\2\u00a3"+
		"\u00a4\6\7\b\3\u00a4\u00a5\7$\2\2\u00a5\u00a6\5 \21\2\u00a6\u00a7\7%\2"+
		"\2\u00a7\u00a8\5\f\7\2\u00a8\u00a9\7&\2\2\u00a9\u00aa\5\f\7\2\u00aa\u00ad"+
		"\7\'\2\2\u00ab\u00ac\7(\2\2\u00ac\u00ae\5\f\7\2\u00ad\u00ab\3\2\2\2\u00ad"+
		"\u00ae\3\2\2\2\u00ae\u00c0\3\2\2\2\u00af\u00b0\7)\2\2\u00b0\u00b1\5 \21"+
		"\2\u00b1\u00b2\7*\2\2\u00b2\u00b3\5\f\7\2\u00b3\u00b6\7+\2\2\u00b4\u00b5"+
		"\7(\2\2\u00b5\u00b7\5\f\7\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7"+
		"\u00c0\3\2\2\2\u00b8\u00b9\7\32\2\2\u00b9\u00ba\5\f\7\2\u00ba\u00bd\7"+
		"\33\2\2\u00bb\u00bc\7(\2\2\u00bc\u00be\5\f\7\2\u00bd\u00bb\3\2\2\2\u00bd"+
		"\u00be\3\2\2\2\u00be\u00c0\3\2\2\2\u00bfJ\3\2\2\2\u00bfO\3\2\2\2\u00bf"+
		"W\3\2\2\2\u00bf^\3\2\2\2\u00bfd\3\2\2\2\u00bfj\3\2\2\2\u00bfq\3\2\2\2"+
		"\u00bfy\3\2\2\2\u00bf\177\3\2\2\2\u00bf\u0085\3\2\2\2\u00bf\u008d\3\2"+
		"\2\2\u00bf\u0094\3\2\2\2\u00bf\u00a3\3\2\2\2\u00bf\u00af\3\2\2\2\u00bf"+
		"\u00b8\3\2\2\2\u00c0\r\3\2\2\2\u00c1\u00c5\7\63\2\2\u00c2\u00c5\5\"\22"+
		"\2\u00c3\u00c5\5\24\13\2\u00c4\u00c1\3\2\2\2\u00c4\u00c2\3\2\2\2\u00c4"+
		"\u00c3\3\2\2\2\u00c5\17\3\2\2\2\u00c6\u00d8\5 \21\2\u00c7\u00d8\5$\23"+
		"\2\u00c8\u00c9\7\27\2\2\u00c9\u00ca\7\13\2\2\u00ca\u00cb\5 \21\2\u00cb"+
		"\u00cc\7\31\2\2\u00cc\u00cd\5 \21\2\u00cd\u00ce\7\f\2\2\u00ce\u00d8\3"+
		"\2\2\2\u00cf\u00d8\5\24\13\2\u00d0\u00d1\7\30\2\2\u00d1\u00d2\7\63\2\2"+
		"\u00d2\u00d4\7\13\2\2\u00d3\u00d5\5\22\n\2\u00d4\u00d3\3\2\2\2\u00d4\u00d5"+
		"\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6\u00d8\7\f\2\2\u00d7\u00c6\3\2\2\2\u00d7"+
		"\u00c7\3\2\2\2\u00d7\u00c8\3\2\2\2\u00d7\u00cf\3\2\2\2\u00d7\u00d0\3\2"+
		"\2\2\u00d8\21\3\2\2\2\u00d9\u00de\5 \21\2\u00da\u00db\7\31\2\2\u00db\u00dd"+
		"\5 \21\2\u00dc\u00da\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de\u00dc\3\2\2\2\u00de"+
		"\u00df\3\2\2\2\u00df\23\3\2\2\2\u00e0\u00de\3\2\2\2\u00e1\u00e2\7\25\2"+
		"\2\u00e2\u00e6\5 \21\2\u00e3\u00e4\7\26\2\2\u00e4\u00e6\5 \21\2\u00e5"+
		"\u00e1\3\2\2\2\u00e5\u00e3\3\2\2\2\u00e6\25\3\2\2\2\u00e7\u00eb\5\30\r"+
		"\2\u00e8\u00eb\5\32\16\2\u00e9\u00eb\5\34\17\2\u00ea\u00e7\3\2\2\2\u00ea"+
		"\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2\u00eb\27\3\2\2\2\u00ec\u00ed\t\2\2"+
		"\2\u00ed\31\3\2\2\2\u00ee\u00f1\5\30\r\2\u00ef\u00f1\5\34\17\2\u00f0\u00ee"+
		"\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f4\3\2\2\2\u00f2\u00f3\7\t\2\2\u00f3"+
		"\u00f5\7\n\2\2\u00f4\u00f2\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3\2"+
		"\2\2\u00f6\u00f7\3\2\2\2\u00f7\33\3\2\2\2\u00f8\u00f9\7\23\2\2\u00f9\u00fa"+
		"\7\13\2\2\u00fa\u00fb\5\36\20\2\u00fb\u00fc\7\31\2\2\u00fc\u00fd\5\36"+
		"\20\2\u00fd\u00fe\7\f\2\2\u00fe\35\3\2\2\2\u00ff\u0103\5\30\r\2\u0100"+
		"\u0103\5\32\16\2\u0101\u0103\7\23\2\2\u0102\u00ff\3\2\2\2\u0102\u0100"+
		"\3\2\2\2\u0102\u0101\3\2\2\2\u0103\37\3\2\2\2\u0104\u0105\b\21\1\2\u0105"+
		"\u0106\t\3\2\2\u0106\u0113\5 \21\20\u0107\u0108\7\13\2\2\u0108\u0109\5"+
		" \21\2\u0109\u010a\7\f\2\2\u010a\u0113\3\2\2\2\u010b\u0113\5\"\22\2\u010c"+
		"\u0113\7\64\2\2\u010d\u0113\7\5\2\2\u010e\u0113\7\7\2\2\u010f\u0113\7"+
		"\6\2\2\u0110\u0113\7\b\2\2\u0111\u0113\7\63\2\2\u0112\u0104\3\2\2\2\u0112"+
		"\u0107\3\2\2\2\u0112\u010b\3\2\2\2\u0112\u010c\3\2\2\2\u0112\u010d\3\2"+
		"\2\2\u0112\u010e\3\2\2\2\u0112\u010f\3\2\2\2\u0112\u0110\3\2\2\2\u0112"+
		"\u0111\3\2\2\2\u0113\u0125\3\2\2\2\u0114\u0115\f\17\2\2\u0115\u0116\7"+
		".\2\2\u0116\u0124\5 \21\20\u0117\u0118\f\16\2\2\u0118\u0119\t\4\2\2\u0119"+
		"\u0124\5 \21\17\u011a\u011b\f\r\2\2\u011b\u011c\7\60\2\2\u011c\u0124\5"+
		" \21\16\u011d\u011e\f\f\2\2\u011e\u011f\7\61\2\2\u011f\u0124\5 \21\r\u0120"+
		"\u0121\f\13\2\2\u0121\u0122\7\62\2\2\u0122\u0124\5 \21\f\u0123\u0114\3"+
		"\2\2\2\u0123\u0117\3\2\2\2\u0123\u011a\3\2\2\2\u0123\u011d\3\2\2\2\u0123"+
		"\u0120\3\2\2\2\u0124\u0127\3\2\2\2\u0125\u0123\3\2\2\2\u0125\u0126\3\2"+
		"\2\2\u0126!\3\2\2\2\u0127\u0125\3\2\2\2\u0128\u012d\7\63\2\2\u0129\u012a"+
		"\7\t\2\2\u012a\u012b\5 \21\2\u012b\u012c\7\n\2\2\u012c\u012e\3\2\2\2\u012d"+
		"\u0129\3\2\2\2\u012e\u012f\3\2\2\2\u012f\u012d\3\2\2\2\u012f\u0130\3\2"+
		"\2\2\u0130#\3\2\2\2\u0131\u013a\7\t\2\2\u0132\u0137\5 \21\2\u0133\u0134"+
		"\7\31\2\2\u0134\u0136\5 \21\2\u0135\u0133\3\2\2\2\u0136\u0139\3\2\2\2"+
		"\u0137\u0135\3\2\2\2\u0137\u0138\3\2\2\2\u0138\u013b\3\2\2\2\u0139\u0137"+
		"\3\2\2\2\u013a\u0132\3\2\2\2\u013a\u013b\3\2\2\2\u013b\u013c\3\2\2\2\u013c"+
		"\u013d\7\n\2\2\u013d%\3\2\2\2$-\67DMU\\bhow}\u0083\u008b\u0092\u00a1\u00ad"+
		"\u00b6\u00bd\u00bf\u00c4\u00d4\u00d7\u00de\u00e5\u00ea\u00f0\u00f6\u0102"+
		"\u0112\u0123\u0125\u012f\u0137\u013a";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}