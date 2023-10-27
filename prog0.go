package main

import (
 "fmt"

)

|data exp = Num int | Sum exp exp



func main() {

if 1 == 1 {
   var d1 exp = _Sum(_Sum(_Num(3), _Num(5)), _Sum(_Num(8), _Num(9)))

   |match d1

   |case Sum(Sum(el,Num(y)),Sum(ex,k))
       fmt.Println(el)
       fmt.Println(y)
       fmt.Println(ex)
       fmt.Println(k)
   |endcase
   |case Sum(el,Num(y)) 
       fmt.Println("el=",el)
       fmt.Println("y =",y)
   |endcase
   |endmatch   
} else {
   fmt.Println("mah")
}
}