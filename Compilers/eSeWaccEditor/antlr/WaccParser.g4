parser grammar WaccParser;

options {
  tokenVocab=WaccLexer;
}

// EOF indicates that the program must consume to the end of the input.
start: prog EOF;

//Programs
prog: BEGIN func* stat[0] END;

func
locals [ int rs = 0, int ps = 0 ]
  : type ID OPEN_PAREN param_list? CLOSE_PAREN IS stat[1] END {$rs > 0}?;

param_list : param (COMMA param)*;
param: type ID;

stat[int x]
  : SKIP (SEMICOLON stat[$x])?
  | type ID EQUALS assign_rhs (SEMICOLON stat[$x])?
  | assign_lhs EQUALS assign_rhs (SEMICOLON stat[$x])?
  | READ assign_lhs (SEMICOLON stat[$x])?
  | FREE expr (SEMICOLON stat[$x])?
//  | {$x == 0}? EXIT expr
//  | {$x == 1}? EXIT expr {$func::rs++;}
  | {$x == 0}? EXIT expr (SEMICOLON stat[$x])?
  | {$x == 1}? EXIT expr {$func::rs++;} (SEMICOLON stat[$x])?
  | PRINT expr (SEMICOLON stat[$x])?
  | PRINTLN expr (SEMICOLON stat[$x])?
  | {$x == 1}? RETURN expr {$func::rs++;} (SEMICOLON stat[$x])?
  | {$x == 0}? RETURN expr (SEMICOLON stat[$x])? // This allows return statements in main prog
  | {$x == 1}? IF expr {$func::rs = 0;} THEN stat[$x] {$func::ps = $func::rs; $func::rs = 0;} ELSE stat[$x] {if($func::ps != $func::rs) {$func::rs = 0;}} FI (SEMICOLON stat[$x])?
  | {$x == 0}? IF expr THEN stat[$x] ELSE stat[$x] FI (SEMICOLON stat[$x])?
  | WHILE expr DO stat[$x] DONE (SEMICOLON stat[$x])?
  | BEGIN stat[$x] END (SEMICOLON stat[$x])?;

assign_lhs: ID | array_elem | pair_elem;

assign_rhs: expr
          | array_lit
          | NEWPAIR OPEN_PAREN expr COMMA expr CLOSE_PAREN
          | pair_elem
		  | CALL ID OPEN_PAREN arg_list? CLOSE_PAREN;

arg_list: expr (COMMA expr)*;

pair_elem: FST expr | SND expr;
type: base_type | array_type | pair_type;
base_type: INT | BOOL | CHAR | STRING;
array_type: (base_type | pair_type) (OPEN_BRACKET CLOSE_BRACKET)+;
pair_type: PAIR OPEN_PAREN pair_elem_type COMMA pair_elem_type CLOSE_PAREN;
pair_elem_type: base_type | array_type | PAIR;

expr:
    (UNARY_OP|MINUS) expr
    | expr BIN_OP0 expr
    | expr (BIN_OP1|MINUS) expr
    | expr BIN_OP2 expr
    | expr BIN_OP3 expr
    | expr BIN_OP4 expr
    | OPEN_PAREN expr CLOSE_PAREN
    | array_elem
    | INT_LIT
    | BOOL_LIT
    | CHAR_LIT 
    | STRING_LIT 
    | PAIR_LIT
    | ID;

array_elem: ID (OPEN_BRACKET expr CLOSE_BRACKET)+;

array_lit: OPEN_BRACKET (expr (COMMA expr)*)? CLOSE_BRACKET;
