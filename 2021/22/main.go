package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

type Line struct {
	fromX, toX, fromY, toY, fromZ, toZ int64
	on                                 bool
}

func readToFrom(str string) (to, from int64) {
	strs := strings.Split(str, "=")
	str_sp := strings.Split(strs[1], "..")

	f, err := strconv.Atoi(str_sp[0])
	check(err)
	from = int64(f)

	t, err := strconv.Atoi(str_sp[1])
	check(err)
	to = int64(t)

	return
}

func readFile(fileName string) []Line {
	l := make([]Line, 0)

	f, err := ioutil.ReadFile(fileName)
	check(err)
	ls := strings.Split(string(f), "\n")

	for _, li := range ls {
		line_sp := strings.Split(li, " ")
		line := Line{}

		if line_sp[0] == "on" {
			line.on = true
		} else {
			line.on = false
		}

		csp := strings.Split(line_sp[1], ",")
		line.toX, line.fromX = readToFrom(csp[0])
		line.toY, line.fromY = readToFrom(csp[1])
		line.toZ, line.fromZ = readToFrom(csp[2])

		l = append(l, line)
	}

	return l
}

type Coord struct {
	x, y, z int64
}

type Grid map[Coord]bool

func (g Grid) lightsOn(p1 bool) (on uint64) {
	if p1 {
		for x := -50; x <= 50; x++ {
			for y := -50; y <= 50; y++ {
				for z := -50; z <= 50; z++ {
					if v, ok := g[Coord{int64(x), int64(y), int64(z)}]; v && ok {
						on++
					}
				}
			}
		}

		return
	}

	for _, v := range g {
		if v {
			on++
		}
	}

	return
}

func follow(insts []Line, p1 bool) {
	g := make(Grid)

	for _, line := range insts {
		if p1 && !(line.fromX >= -50 && line.fromX <= 50 && line.fromY >= -50 && line.fromY <= 50 && line.fromZ >= -50 && line.fromZ <= 50 && line.toX >= -50 && line.toX <= 50 && line.toY >= -50 && line.toY <= 50 && line.toZ >= -50 && line.toZ <= 50) {
			continue
		}
		for x := line.fromX; x <= line.toX; x++ {
			for y := line.fromY; y <= line.toY; y++ {
				for z := line.fromZ; z <= line.toZ; z++ {
					toSet := false
					if line.on {
						toSet = true
					}
					g[Coord{x, y, z}] = toSet
				}
			}
		}
	}

	fmt.Println(g.lightsOn(p1))
}

func main() {
	fileName := os.Args[1]
	lines := readFile(fileName)

	follow(lines, true)
	follow(lines, false)
}
