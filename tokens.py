code = """if a > b {
				return a;
			}"""

tokens = (
	# assignment
	'IDENTIFIER',
	'ASSIGNMENT',
	'SEMICOLON',
	'COLON',
	'COMMA',

	'COMMENTBEGIN',
	'COMMENTEND',

	# functions
	'RETURN',

	# control flow
	'IF',
	'ELSE',
	'WHILE',

	# logic
	'AND',
	'OR',

	# comparations
	'EQUAL',
	'NEQUAL',
	'LT',
	'GT',
	'LTE',
	'GTE',

	# operations
	'PLUS',
	'MINUS',
	'TIMES',
	'DIV',
	'MOD',

	# other
	'LBRACKET',
	'RBRACKET',
	'LPAREN',
	'RPAREN',

	# types
	'VOID',
	'BOOL',
	'INTEGER',
	'ARRAY',
	'STRING',

	# types names
	'TVOIDE',
	'TBOOL',
	'TINTEGER',
	'TARRAY',
	'TSTRING',
)


# Regular statement rules for tokens
t_ASSIGNMENT 	= r"\="
t_SEMICOLON  	= r"\;"
t_COLON      	= r"\:"
t_COMMA			= r"\,"

t_COMMENTBEGIN 	= r"\{\*"
t_COMMENTEND 	= r"\*\}"

t_AND 			= r"\&\&"
t_OR 			= r"\|\|"
t_EQUAL 		= r"\=\="
t_NEQUAL 		= r"\!\="
t_LT			= r"\<"
t_GT			= r"\>"
t_LTE			= r"\<\="
t_GTE			= r"\>\="

t_PLUS			= r"\+"
t_MINUS			= r"\-"
t_TIMES			= r"\*"
t_DIV			= r"/"
t_MOD 			= r"\%"

t_LBRACKET		= r"\{"
t_RBRACKET		= r"\}"
t_LPAREN		= r"\("
t_RPAREN		= r"\)"

t_INTEGER		= r"(\-)*[0-9]+"
#t_BOOL 			= r"true||false"

reserved_keywords = {	
	'return':	'RETURN',

	'if':		'IF',
	'else':		'ELSE',
	'while':	'WHILE',

	'void':		'TVOID',
	'bool':		'TBOOL',	
	'int':		'TINTEGER',
	'array':	'TARRAY',
	'string':	'TSTRING',
}

'''def t_INTEGER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t'''

def t_IDENTIFIER(t):
	r"[a-zA-Z]([a-zA-Z0-9])*"
	if t.value.lower() in reserved_keywords:
		t.type = reserved_keywords[t.value.lower()]
	return t

def t_STRING(t): 
    r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"
    escaped = 0 
    str = t.value[1:-1] 
    new_str = "" 
    for i in range(0, len(str)): 
        c = str[i] 
        if escaped: 
            if c == "n": 
                c = "\n" 
            elif c == "t": 
                c = "\t" 
            new_str += c 
            escaped = 0 
        else: 
            if c == "\\": 
                escaped = 1 
            else: 
                new_str += c 
    t.value = new_str 
    return t

def t_COMMENT(t):
	r"{\*[^}]*\*}"

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



if __name__ == '__main__':
	# Build the lexer
	from ply import lex
	import sys 
	
	lex.lex()

	"""if len(sys.argv) > 1:
		f = open(sys.argv[1],"r")
		data = f.read()
		f.close()
	else:
		data = ""
		while 1:
			try:
				data += input('> ') + "\n"
			except:
				break"""
	
	lex.input(code)
	
	# Tokenize
	while 1:
	    tok = lex.token()
	    if not tok: break      # No more input
	    print(tok)