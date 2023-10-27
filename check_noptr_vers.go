// vedi https://tour.golang.org/methods/15
package main

import (
	"fmt"
)

type exp interface {
	isa_exp()
}

type Num struct {
	a0 int
}

func _Num(a0 int) Num {
	o := Num{}
	o.a0 = a0
	return o
}
func (o Num) isa_exp() {}
func (o Num) String() string {
	s := fmt.Sprintf("Num(%v)", o.a0)
	return s
}

type Sum struct {
	a0 exp
	a1 exp
}

func _Sum(a0 exp, a1 exp) Sum {
	o := Sum{}
	o.a0 = a0
	o.a1 = a1
	return o
}
func (o Sum) isa_exp() {}
func (o Sum) String() string {
	s := fmt.Sprintf("Sum(%v,%v)", o.a0, o.a1)
	return s
}

func main() {
	if 1 == 1 {
		var d1 exp = Sum(Sum(Num(3), Num(5)), Sum(Num(8), Num(9)))

		// if isinstance(d1, Sum) {
		_d1, ok0 := d1.(Sum)
		if ok0 {
			t0 := _d1.a0
			t1 := _d1.a1
			// if isinstance(t0, Sum) {
			_t0, ok1 := t0.(Sum)
			if ok1 {
				el := _t0.a0
				t2 := _t0.a1
				// if isinstance(t2, Num) {
				_t2, ok2 := t2.(Num)
				if ok2 {
					y := _t2.a0
					// if isinstance(t1, Sum) {
					_t1, ok3 := t1.(Sum)
					if ok3 {
						ex := _t1.a0
						k := _t1.a1
						fmt.Println(el)
						fmt.Println(y)
						fmt.Println(ex)
						fmt.Println(k)
					}
				}
			}
		}
		// if isinstance(d1, Sum) {
		_d1, ok4 := d1.(Sum)
		if ok4 {
			el := _d1.a0
			t3 := _d1.a1
			// if isinstance(t3, Num) {
			_t3, ok5 := t3.(Num)
			if ok5 {
				y := _t3.a0
				fmt.Println("el=", el)
				fmt.Println("y =", y)
			}
		}
	}
}
