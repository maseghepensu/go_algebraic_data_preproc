// vedi https://tour.golang.org/methods/15
package main

import (
	"fmt"
)
/*
package main

import "fmt"

func main() {
var i interface{} = "hello"

s := i.(string)
fmt.Println(s)

s, ok := i.(string)
fmt.Println(s, ok)

// f
i, ok := i.(float64)
fmt.Println(f, ok)

f = i.(float64) // panic
fmt.Println(f)
}

output:

hello
hello true
0 false
panic: interface conversion: interface {} is string, not float64

/*

/* in python avevi:

|data exp = Num n | Sum e1 e2

if 1 == 1:
  d1 = Sum(Sum(Num(3), Num(5)), Sum(Num(8), Num(9)))

  |match d1

  |case Sum(Sum(el,Num(y)),Sum(ex,k))
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

che generava:

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
   # Sum(Sum(el,Num(y)),Sum(ex,k))
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

   # Sum(el,Num(y))
    if isinstance(d1, Sum):
       el = d1.e1
       t3 = d1.e2
       if isinstance(t3, Num):
          y = t3.n
          print("el=",el)
          print("y =",y)
   else:
    print('mah')

 */


type Node interface {
	 isNode()
}

type Num struct {
	n int
}
func _Num(i int) *Num { // costruttore
   return &Num{i}
}
func (n *Num) isNode() {}
func (n *Num) String() string {
	return fmt.Sprintf("Num(%d)", n.n)
}

/*

class Sum:
  def __init__(self, e1,e2 ):
      self.e1 = e1
      self.e2 = e2
  def __str__(self):
      return 'Sum(%s,%s)' % (str(self.e1),str(self.e2))
*/
type Sum struct {
  e1 Node
  e2 Node
}
func (s *Sum) isNode() {}
func _Sum(n1, n2 Node) *Sum {
	return &Sum{n1,n2}
}
func (n *Sum) String() string {
	return fmt.Sprintf("Sum(%s,%s)", n.e1, n.e2 )
}


func provaDiscern(n Node) {
	num, ok := n.(*Num)
	if ok {
	   fmt.Printf("Num->%d\n", num.n)	
	}

	switch v := n.(type) {
	  case *Num: fmt.Println(v)	
	  case *Sum: fmt.Println(v)
	  default:
		fmt.Println("????")
    }		
 	
}

func demoMatch(d1 Node) {
   // tenta il match  d1  con Sum(Sum(el,Num(y)),Sum(ex,k))
   // se d1 == Sum(Sum( Num(3),Num(5)) , Sum( Num(8), Num(9)))
   //          Sum(Sum( el  ,  Num(y)) , Sum( ex,     k     ))
   //  dovrebbe stampare
   // Num(3)
   // 5
   // Num(8)
   // Num(9)
   d1_ , ok := d1.(*Sum)
   if ok {
       t0 := d1_.e1
       t1 := d1_.e2
       t0_ , ok := t0.(*Sum)
       if ok {
          el := t0_.e1
          t2 := t0_.e2
          t2_, ok := t2.(*Num)
          if ok {
             y := t2_.n
             t1_, ok := t1.(*Sum)
             if ok {
             	ex := t1_.e1.n
                k  := t1_.e2.n
                fmt.Println(el)
                fmt.Println(y)
                fmt.Println(ex)
                fmt.Println(k)
             }
          }   
       }   
   }
}

func main()  {
   var uno Node = _Num(3)
   provaDiscern(uno)
   var due Node = _Num(4)
   var s1 Node = _Sum(uno, due)
   provaDiscern(s1)

   d1 := _Sum(_Sum(_Num(3), _Num(5)), _Sum(_Num(8), _Num(9)))
   provaDiscern(d1)
   demoMatch(d1)



}




