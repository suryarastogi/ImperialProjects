lexer grammar WaccLexer;

WS : [ \t\r\n]+ -> skip ;
COMMENT: '#' .*? '\n'  -> skip;

BOOL_LIT: 'true' | 'false';

STRING_LIT: DOUBLEQUOTE CHARACTER* DOUBLEQUOTE;
CHAR_LIT: SINGLEQUOTE CHARACTER SINGLEQUOTE;
PAIR_LIT: 'null';

OPEN_BRACKET: '[';
CLOSE_BRACKET: ']';

OPEN_PAREN: '(';
CLOSE_PAREN: ')';

DOUBLEQUOTE: '"';
SINGLEQUOTE: '\'';

//types
INT: 'int';
BOOL: 'bool';
CHAR: 'char';
STRING: 'string';
PAIR: 'pair';

EQUALS: '=';

FST: 'fst';
SND: 'snd';
NEWPAIR: 'newpair';

CALL: 'call';

COMMA: ',';

//program begin/end
BEGIN: 'begin';
END: 'end';

IS: 'is';

SKIP: 'skip';
READ: 'read';
FREE: 'free';
RETURN: 'return';
EXIT: 'exit';
PRINT: 'print';
PRINTLN: 'println';

//if
IF: 'if';
THEN: 'then';
ELSE: 'else';
FI: 'fi';

SEMICOLON: ';';

//while
WHILE: 'while';
DO: 'do';
DONE: 'done';

MINUS: '-';
UNARY_OP: '!' | 'len' | 'ord' | 'chr';
// Binds stronger to weaker
BIN_OP0: '*' | '/' | '%';
BIN_OP1: '+';
BIN_OP2: '==' | '!=';
BIN_OP3: '>=' | '>' | '<' | '<=';
BIN_OP4: '&&' | '||';

ID: ([a-zA-Z] | '_') ([a-zA-Z] | '_' | [0-9])*;

INT_LIT: ('+' | '-')? [0-9]+ {new Long(getText()) <= 2147483647 && new Long(getText()) >= -2147483648}?;

fragment ESCAPED_CHAR: ('0' | 'b' | 't' | 'n' | 'f' | '"' | '\'' | '\\');
fragment CHARACTER: (~[\\\'\"] | '\\' ESCAPED_CHAR);
