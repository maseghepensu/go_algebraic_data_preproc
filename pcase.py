#calcparser.py
# Yacc example


reserved = { 'case' : 'CASE' }
tokens = [ 'LP','RP','COMMA', 'ID' ] + list(reserved.values())

# Tokens

t_LP  = r'\('
t_RP  = r'\)'
#t_CASE = 'case'
#t_ID    = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMA = r','

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

import ply.yacc as yacc

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

import gen_case
import gen_class


# ============ classi di supporto ======================
# rappresenta un caso di match:
class Case:
  def __init__(self, nomeCostruttore, figli):
      self.nomeCostruttore = nomeCostruttore
      self.figli = figli
  def __str__(self):
      return self.nomeCostruttore + "(" + ','.join([str(c) for c in self.figli]) + ")"


'''
  case p1 ':'
     codice...
'''     



# Get the token map from the lexer.  This is required.
#from calclex import tokens

def p_case(p):
    'case : CASE pattern'
    p[0] = p[2]

def p_pattern(p):
    '''pattern : ID LP plist RP
               | ID '''
    if len(p) == 2:
       p[0] = '%s' % p[1]
    else:   
       p[0] = Case(p[1], p[3])
    

    
def p_plist(p):    
    '''plist : plist COMMA pattern
          | pattern'''
    if len(p) < 4:
       #print('caso pattern')
       p[0] = [p[1]]
       #print('p0=',p[0])
    else:
       #print('caso seq pattern')
       p[1].append(p[3])
       p[0] = p[1]
       #print('p0:')
       #for e in p[0]:
       #  print(e, end=' ; ')


def p_empty(p):
    'empty :'
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

parser = yacc.yacc()

# Build the parser
#parser = yacc.yacc()
#dataparser = yacc.yacc(tabmodule='dataparsetab')

'''
s = 'case Sum(x,y)'
result = parser.parse(s) #, debug=True)
print(result)

s = 'case Sum(el,Num(y))'
result = parser.parse(s) #, debug=True)
print(result)

s = 'case Sum(Sum(el,Num(y)),Sum(ex,k))'
result = parser.parse(s) #, debug=True)
print(result)
ind = gen_case.gen(result, 'E')
print('ind=',ind)
'''
#test_parser(parser)
#test_parser1(parser, dataparser)
#test_parser1(None,None)
#test_parser2()