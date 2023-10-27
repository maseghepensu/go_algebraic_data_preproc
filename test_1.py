import sys
import re
import gen_case
import gen_class
import pdata
import pcase
import pmatch
#import ply.yacc as yacc



#from lexer_data import get_lexer 

'''
import sys

ss = [ '|data exp = Num n | Sum e1 e2' ] 
for s in ss:
       if s.startswith('|data'):
        print('***************************')
        #dataparser = yacc.yacc(tabmodule='dataparsetab')
        result = pdata.dataparser.parse(s[1:],lexer=pdata.lexer) #, debug=True) #, debug=True)
        for d in result:
           gen_class.gen_class(d)
'''

ca = re.compile(r' *(\|case )')
cm = re.compile(r' *(\|match )')
ce = re.compile(r' *(\|endmatch)')

#test_parser()

inp = open(sys.argv[1])
ind = 0    
primo_case = True
curr_match = None
for r in inp:
     s = r.rstrip()
     if s.startswith('|data'):
        result = pdata.dataparser.parse(s[1:],lexer=pdata.lexer) #, debug=True) #, debug=True)
        for d in result:
           gen_class.gen_class(d)
           gen_case.diz[d.getName()] = d
     elif ca.match(s):#s.startswith('|case'):
        ic = ca.match(s).start(1)
        result = pcase.parser.parse(s[ic+1:], lexer=pcase.lexer)
        print('# ',result)
    #    ind = gen_case.gen(result, 'E' , primo_case, ic) - 1
        ind = gen_case.gen(result, curr_match , primo_case, ic) - 1
        primo_case = False
     elif cm.match(s):
        ic = cm.match(s).start(1)
        curr_match = pmatch.matchparser.parse(s[ic+1:], lexer=pmatch.lexer)
     elif ce.match(s):
         ind = 0
     else:        
        if ind > 0:
           print(' ' * ind,s.strip())
        else:
           print(s)
