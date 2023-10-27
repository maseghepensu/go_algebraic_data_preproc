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
      self.cnames = cnames
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

temp=0
# temporanei per il patter matching
def newtemp():
    global temp
    r = 't%d' % temp
    temp += 1
    return r


# genera il codice per il pattern matching di un "case"
def gen(c, match_id, primocase, ind=0):
   cname = c.nomeCostruttore
   #ars = getVars(c.figli)
   #print('cname',cname)
   #rint(','.join(vars))
   ic = 0

   cldef = diz[cname] # trova la definizione del costruttore di valore del dato algebrico
   #ind = 3 # a caso qui!
   ifs = 'if'
   #xxxif not primocase:
   #xxx   ifs = 'elif'

   print("%s%s isinstance(%s, %s):" % (' ' * ind, ifs, match_id, cname))
   temps = []
   for ch in c.figli:
       if isinstance(ch,str):
          print("%s%s = %s.%s" % (' ' * (ind+3), ch, match_id, cldef.cnames[ic]))
       else:
          t = newtemp()   
          temps.append(t)
          print("%s%s = %s.%s" % (' ' * (ind+3), t, match_id, cldef.cnames[ic]))
       ic += 1
   nt = 0 
   ind += 3         
   sind = ind 
   for ch in c.figli:
       if not isinstance(ch,str):
          sind = gen(ch, temps[nt], True, ind)
          nt += 1   
          #ind += 6
          ind = sind
   return sind # ritorna la massima indentazione

