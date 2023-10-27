# rappresenta un caso di match:
'''
class Case:
  def __init__(self, nomeCostruttore, figli):
      self.nomeCostruttore = nomeCostruttore
      self.figli = figli
  def __str__(self):
      return self.nomeCostruttore + "(" + ','.join([str(c) for c in self.figli]) + ")"


class Data:
  def __init__(self, costrname, cnames):
      self.costrname = costrname
      self.cnames = cnames  # nella versione go, questi sono tipi
                            # e i nomi sono generati in sequenza 
  def getName(self):   
      return self.costrname
  def __str__(self):
      return 'data(%s)' % ','.join([str(c) for c in self.cnames])


'''
# XXXXXXXXXX PER TEST !!!!!

'''
d1 = Data('Num', ['n'])
d2 = Data('Sum', ['e1', 'e2'])

diz = { d1.getName() : d1, d2.getName() : d2 }
'''
diz = {}
diz_struct_members_by_struct_name = {} # contiene liste di coppie [n,t] per ogni nome di struct, con nome membro e tipo
temp=0
# temporanei per il patter matching
def newtemp():
    global temp
    r = 't%d' % temp
    temp += 1
    return r


# genera il codice per il pattern matching di un "case"
pila = []
curr_ok = 0

def gen(c, match_id, primocase, interfaceName, ind=0):
   global pila, curr_ok
   cname = c.nomeCostruttore
   #ars = getVars(c.figli)
   #print('cname',cname)
   #rint(','.join(vars))
   ic = 0

   cldef = diz[cname] # trova la definizione del costruttore di valore del dato algebrico
   #ind = 3 # a caso qui!
   ifs = 'if'
   #xxxif not primocase:
   #xxx   ifs = 'else if'

   if_ind = ind - 1
   print("%s// %s isinstance(%s, %s) {" % (' ' * ind, ifs, match_id, cname))
   c_match_id = '_' + match_id
   print('%s%s, ok%s := %s.(%s)' % (' ' * ind,c_match_id, curr_ok, match_id, cname))
   print("%sif ok%s {" % (' ' * ind, curr_ok))

   pila.append((ind,'}'))
   curr_ok += 1
   temps = []
   for ch in c.figli:
       name_m = diz_struct_members_by_struct_name[cname][ic][0] # [1] e' il tipo del membro
       if isinstance(ch,str):
          print("%s%s := %s.%s" % (' ' * (ind+3), ch, c_match_id, name_m)) # cldef.cnames[ic]))
       else:
          t = newtemp()   
          temps.append(t)
          print("%s%s := %s.%s" % (' ' * (ind+3), t, c_match_id, name_m)) #cldef.cnames[ic]))
       ic += 1
   #print(' ' * (ind+1),'}')
   nt = 0 
   ind += 3         
   sind = ind
   for ch in c.figli:
       if not isinstance(ch,str):
          #print('ch=>',ch)
          sind = gen(ch, temps[nt], True, ind)
          nt += 1   
          #ind += 6
          ind = sind
   #print(' ' * (if_ind),'}')     
   return sind # ritorna la massima indentazione

