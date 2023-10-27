class Num:
   def __init__(self, n ):
     self.n = n
   def __str__(self):
      return 'Num(%s)' % (str(self.n))
class Sum:
   def __init__(self, e1,e2 ):
     self.e1 = e1
     self.e2 = e2
   def __str__(self):
      return 'Sum(%s,%s)' % (str(self.e1),str(self.e2))


if 1 == 1:
   d1 = Sum(Sum(Num(3), Num(5)), Sum(Num(8), Num(9)))


#  Sum(Sum(el,Num(y)),Sum(ex,k))
   if isinstance(d1, Sum):
      t0 = d1.e1
      t1 = d1.e2
      if isinstance(t0, Sum):
         el = t0.e1
         t2 = t0.e2
         if isinstance(t2, Num):
            y = t2.n
            if isinstance(t1, Sum):
               ex = t1.e1
               k = t1.e2
               print(el)
               print(y),
               print(ex)
               print(k)
               
#  Sum(el,Num(y))
   if isinstance(d1, Sum):
      el = d1.e1
      t3 = d1.e2
      if isinstance(t3, Num):
         y = t3.n
         print("el=",el)
         print("y =",y)
         
else:
   print('mah')
