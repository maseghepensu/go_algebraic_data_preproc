# genera la classe da una definizione Data creata
# dal parser del (futuro) preprocessore:
def gen_interface(interfaceName):
   print('type %s interface {' % interfaceName)
   print('  isa_%s()' % interfaceName)
   print('}')
   print('\n')
def gen_class(dt, interfaceName):

   ints = [i for i in range(len(dt.costrname))]

   dt_cnames = [['a%d' % v[0], '%s' % v[1]]  for v in zip(ints, dt.cnames)]
   
   print('type %s struct {' % dt.costrname)
   for e in dt_cnames:
      print( '   %s %s' % (e[0],e[1]))
   print('}')

   # costruttore:
   print('func _%s(' % dt.costrname, end='')

   if len(dt.cnames) == 0:
      print('):')
      print('   pass')
   else:
      print(','.join([' '.join(e) for e in dt_cnames]),') *%s {' % dt.costrname)
      print('   o := %s{}' % dt.costrname)
      for c in dt_cnames:
        print('   o.%s = %s' % (c[0],c[0]))
      print('   return &o')  
   print('}')

   print('func (o *%s) isa_%s() {}' % (dt.costrname, interfaceName))
      
   # String() string
   # 'Sum(%s,%s)' % (str(self.e1), str(self.e2))
   print('func', '(o *%s) String() string {' % dt.costrname)
   #fmt = ','.join(['%s' for c in dt.cnames])
   nplaces = ','.join(['%v' for x in range(len(dt.cnames))])
   s = 's := fmt.Sprintf("%s(%s)",%s)' % (dt.costrname, nplaces, ','.join(['o.%s' % c[0] for c in dt_cnames]))
   print('    %s' % s)
   print('    return s') # % s)    
   print('}')
