#calcparser.py
# Yacc example


import ply.yacc as yacc

reserved = { 'data' : 'DATA' }
tokens = [ 'OR','ID', 'EQ'  ] + list(reserved.values())

# Tokens

#t_LP  = r'\('
#t_RP  = r'\)'
#t_CASE = 'case'
# t_COMMA = r','
t_EQ = r'='
t_OR = r'\|'

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

# ============ classi di supporto ======================
# rappresenta un caso di match:
class Data:
  def __init__(self, costrname, cnames):
      self.costrname = costrname
      self.cnames = cnames
  def getName(self):
      return self.costrname
  def __str__(self):
      return 'data(%s, %s)' % (self.costrname, ','.join([str(c) for c in self.cnames]))


def p_data(p):
    'data : DATA ID EQ vlist'
    p[0] = p[4]

def p_vlist(p):
    '''vlist   : vlist OR v 
               | v'''
    if len(p) == 2:
       p[0] = [p[1]]
    else:   
       p[1].append(p[3])
       p[0] = p[1]
    
def p_v(p):
    'v :   ID vs'
    p[0] = Data(p[1], p[2])
    
def p_vs(p):
    '''vs : vs ID
          | empty'''
    if len(p) == 2:
       p[0] = []
    else:
       p[1].append(p[2])
       p[0] = p[1]

def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


dataparser = yacc.yacc(tabmodule='dataparsetab')



