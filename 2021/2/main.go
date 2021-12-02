package main

import (
	"fmt"
	"io/ioutil"
	"math"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readFile(fileName string) []string {
	f, err := ioutil.ReadFile(fileName)
	check(err)

	return strings.Split(string(f), "\n")
}

type Position struct {
	X   int
	Z   int
	Aim int
}

func (p *Position) MoveForward(unit int, toChangeAim bool) {
	p.X += unit
	if toChangeAim {
		p.Z += (p.Aim * unit)
	}
}

func (p *Position) MoveDepth(unit int, toChangeAim bool) {
	if !toChangeAim {
		p.Z += unit
		return
	}
	p.moveAim(unit)
}

func (p *Position) moveAim(unit int) {
	p.Aim += unit
}

func (p Position) Result() int {
	return int(math.Abs(float64(p.X * p.Z)))
}

func solve(insts []string, toChangeAim bool) {
	p := Position{X: 0, Z: 0, Aim: 0}

	for _, instStr := range insts {
		is := strings.Split(instStr, " ")
		inst := is[0]
		num, err := strconv.Atoi(is[1])
		check(err)

		if inst == "forward" {
			p.MoveForward(num, toChangeAim)
		} else if inst == "up" {
			p.MoveDepth(num, toChangeAim)
		} else if inst == "down" {
			p.MoveDepth(-num, toChangeAim)
		}
	}

	fmt.Println(p.Result())
}

func main() {
	fileName := os.Args[1]
	lines := readFile(fileName)

	solve(lines, false)
	solve(lines, true)
}
