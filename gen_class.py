# genera la classe da una definizione Data creata
# dal parser del (futuro) preprocessore:
def gen_class(dt):
   print('class %s:' % dt.costrname)
   # costruttore:
   print('   def __init__(self',end='')
   if len(dt.cnames) == 0:
      print('):')
      print('   pass')
   else:
      print(',',','.join(dt.cnames),'):')   
      for c in dt.cnames:
         print('     self.%s = %s' % (c,c))
   # str
   # 'Sum(%s,%s)' % (str(self.e1), str(self.e2))
   print('   def __str__(self):')
   fmt = ','.join(['%s' for c in dt.cnames])
   print("      return '%s(%s)' %% (%s)" % (dt.costrname, fmt, ','.join(['str(self.%s)' % c for c in dt.cnames])))
