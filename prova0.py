|data exp = Num n | Sum e1 e2

if 2 == 2:
   if 1 == 1:

      d1 = Sum(Sum(Num(3), Num(5)), Sum(Num(8), Num(9)))

     |match d1

     |case Sum(Sum(el,Num(y)),Sum(ex,Num(k)))
          print(el)
          print(y),
          print(ex)
          print(k)
     |case Sum(el,Num(y))
          print("el=",el)
          print("y =",y)
     |endmatch
   else:
     print('mah')
else:
   print('boh')
