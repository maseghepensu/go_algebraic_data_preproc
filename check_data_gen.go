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

func _Num(a0 int) *Num {
	o := Num{}
	o.a0 = a0
	return &o
}
func (o *Num) isa_exp() {}
func (o *Num) String() string {
	s := fmt.Sprintf("Num(%v)", o.a0)
	return s
}

type Sum struct {
	a0 exp
	a1 exp
}

func _Sum(a0 exp, a1 exp) *Sum {
	o := Sum{}
	o.a0 = a0
	o.a1 = a1
	return &o
}
func (o *Sum) isa_exp() {}
func (o *Sum) String() string {
	s := fmt.Sprintf("Sum(%v,%v)", o.a0, o.a1)
	return s
}

func main() {
	n0 := _Num(3)
	n1 := _Num(5)
	s := _Sum(n0, n1)
	fmt.Printf("sum=%s\n", s)
}
