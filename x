import sys
import re
import go_gen_case
import go_gen_class
import go_pdata
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
interfaceName = ''
for r in inp:
     s = r.rstrip()
     if s.startswith('|data'):
        result = go_pdata.dataparser.parse(s[1:],lexer=go_pdata.lexer) #, debug=True) #, debug=True)
        interfaceName = result[0]
        go_gen_class.gen_interface(interfaceName)
        for d in result[1]:
           member_names = go_gen_class.gen_class(d, interfaceName)
           go_gen_case.diz[d.getName()] = d
           go_gen_case.diz_struct_members_by_struct_name[d.getName()] = member_names
           #for mname_type in go_gen_case.diz_struct_members_by_struct_name[d.getName()]:
           #   print(d.getName(), '->', mname_type) 
     elif ca.match(s):#s.startswith('|case'):
        ic = ca.match(s).start(1)
        result = pcase.parser.parse(s[ic+1:], lexer=pcase.lexer)
        
        #print('# pcase produce :',result, 'tipo:', type(result))
    #    ind = gen_case.gen(result, 'E' , primo_case, ic) - 1
        go_gen_case.pila = [] 
        ind = go_gen_case.gen(result, curr_match , primo_case, interfaceName, ic ) - 1
        #print("PILA=",go_gen_case.pila)
        #print('>>>>>>>>>>>>>>')
        primo_case = False
     elif cm.match(s):
        ic = cm.match(s).start(1)
        curr_match = pmatch.matchparser.parse(s[ic+1:], lexer=pmatch.lexer)
     elif ce.match(s):
         ind = 0
     else:        
        if ind > 0:
           #print('++++++++++++++++')  
           if '|endcase' == s.strip():
              go_gen_case.pila.reverse()  
              for p in go_gen_case.pila:
                 print(' '* p[0],p[1],sep='')
           else:
                 print(' ' * ind,s.strip())
  
        else:
           print(s)
