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

type Point struct {
	x, y int
}

type Scan []bool

type Grid map[Point]bool

func (g Grid) countLights() (c int) {
	for _, v := range g {
		if v {
			c++
		}
	}

	return
}

func (p Point) neighbours(g Grid) []bool {
	pts := make([]bool, 0)

	for _, i := range []int{-1, 0, 1} {
		for _, j := range []int{-1, 0, 1} {
			val := false

			pt := Point{p.x + i, p.y + j}
			if v, ok := g[pt]; ok && v {
				val = v
			}

			pts = append(pts, val)
		}
	}

	return pts
}

func (s Scan) newPoint(pts []bool) bool {
	str := make([]string, 0)

	for _, i := range pts {
		if i {
			str = append(str, "1")
		} else {
			str = append(str, "0")
		}
	}

	st := strings.Join(str, "")
	o, e := strconv.ParseInt(st, 2, 32)
	check(e)

	return s[int(o)]
}

func (g Grid) getMaxDims() (maxX, maxY int) {
	for k := range g {
		if k.x > maxX {
			maxX = k.x
		}
		if k.y > maxY {
			maxY = k.y
		}
	}

	return
}

func (g Grid) iterate(inc, maxX, maxY int, sl Scan) Grid {
	newGrid := make(Grid)
	newGrid = g

	for x := -inc; x < maxX+inc; x++ {
		for y := -inc; y < maxY+inc; y++ {
			p := Point{x, y}
			// fmt.Println(p)
			ns := p.neighbours(g)
			nw := sl.newPoint(ns)
			newGrid[p] = nw
		}
	}

	return newGrid
}

func readFile(fileName string) (Scan, Grid) {
	f, err := ioutil.ReadFile(fileName)
	check(err)

	inp_splits := strings.Split(string(f), "\n\n")
	scan_sp := inp_splits[0]
	image_sp := inp_splits[1]

	scan := make(Scan, 0)
	grid := make(Grid)

	for _, s := range strings.Split(scan_sp, "") {
		if s == "#" {
			scan = append(scan, true)
		} else if s == "." {
			scan = append(scan, false)
		}
	}

	for i, st := range strings.Split(image_sp, "\n") {
		for j, str := range strings.Split(st, "") {
			if str == "#" {
				grid[Point{i, j}] = true
			} else if str == "." {
				grid[Point{i, j}] = false
			}
		}
	}

	return scan, grid
}

func (g Grid) print(c, mx, my int) {
	for x := -c; x < my+1; x++ {
		for y := -c; y < mx+1; y++ {
			p := Point{x, y}
			if v := g[p]; v {
				fmt.Print("#")
			} else {
				fmt.Print(".")
			}
		}
		fmt.Println()
	}
}

func main() {
	fileName := os.Args[1]
	scanline, grid := readFile(fileName)

	maxX, maxY := grid.getMaxDims()

	c := 0
	for c != 50 {
		ng := make(Grid)
		ng = grid.iterate(c+1, maxX, maxY, scanline)
		grid = ng
		if c == 2 {
			// part 1
			fmt.Println(grid.countLights())
		}
		c++
	}

	// part 2
	fmt.Println(grid.countLights())
}
