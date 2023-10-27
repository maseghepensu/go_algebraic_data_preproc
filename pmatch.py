#calcparser.py
# Yacc example


import ply.yacc as yacc

reserved = { 'match' : 'MATCH' }
tokens = [ 'ID'  ] + list(reserved.values())

# Tokens

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t


# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex
lexer = lex.lex()



def p_match(p):
    'match : MATCH ID'
    p[0] = p[2]



# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


matchparser = yacc.yacc(tabmodule='matchparsetab')



