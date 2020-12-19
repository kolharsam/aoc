package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type rect struct {
	row int
	col int
}

type rotate struct {
	dim   string
	coord int
	by    int
}

type inst struct {
	name string
	rec  rect
	rot  rotate
}

// NOTE: another go-lang-y way of handling this would be to,
// create `type grid [][]string` and then make all/most
// of these functions so that I don't have to keep passing
// grid aound

func convertToNumber(str string) int {
	n, err := strconv.Atoi(str)
	if err != nil {
		fmt.Println("error in converting the number")
	}
	return n
}

func parseFile(filename string) []inst {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Unable to read the file")
	}
	lines := strings.Split(string(buf), "\n")
	l := make([]inst, 0, len(lines))

	for _, v := range lines {
		spl := strings.Split(v, " ")
		current := inst{}
		if spl[0] == "rect" {
			current.name = "rect"
			nums := strings.Split(spl[1], "x")
			current.rec.row = convertToNumber(nums[0])
			current.rec.col = convertToNumber(nums[1])
		} else {
			current.name = "rotate"
			current.rot.dim = spl[1]
			current.rot.by = convertToNumber(spl[4])
			sp := strings.Split(spl[2], "=")
			current.rot.coord = convertToNumber(sp[1])
		}
		l = append(l, current)
	}

	return l
}

func lightsOn(grid [][]string) int {
	s := 0

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] == "#" {
				s++
			}
		}
	}

	return s
}

func printGrid(grid [][]string) {
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			fmt.Print(grid[i][j])
		}
		fmt.Print("\n")
	}
	fmt.Print("\n\n")
}

func getInitGrid(x, y int) [][]string {
	g := make([][]string, 0, y)

	for i := 0; i < y; i++ {
		gx := make([]string, 0, x)
		for j := 0; j < x; j++ {
			gx = append(gx, ".")
		}
		g = append(g, gx)
	}

	return g
}

func drawRect(x, y int, grid [][]string) [][]string {
	for i := 0; i < y; i++ {
		for j := 0; j < x; j++ {
			grid[i][j] = "#"
		}
	}

	return grid
}

func rot(st []string, k int) []string {
	lst := len(st)
	k = k % lst
	if k != 0 {
		copy(st, append(st[lst-k:], st[:lst-k]...))
	}

	return st
}

func rotCol(grid [][]string, no, by int) [][]string {
	colElems := make([]string, len(grid))
	for i := 0; i < len(grid); i++ {
		colElems[i] = grid[i][no]
	}
	colElems = rot(colElems, by)
	for i := 0; i < len(grid); i++ {
		grid[i][no] = colElems[i]
	}
	return grid
}

func rotRow(grid [][]string, no, by int) [][]string {
	grid[no] = rot(grid[no], by)
	return grid
}

func runDisplay(x, y int, lines []inst) [][]string {
	grid := getInitGrid(x, y)

	for _, v := range lines {
		if v.name == "rect" {
			grid = drawRect(v.rec.row, v.rec.col, grid)
		} else { // rotate
			if v.rot.dim == "row" {
				grid = rotRow(grid, v.rot.coord, v.rot.by)
			} else {
				grid = rotCol(grid, v.rot.coord, v.rot.by)
			}
		}
		// Needed for Part 2
		printGrid(grid)
	}

	return grid
}

func main() {
	parsedInput := parseFile("8.in")

	litGrid := runDisplay(50, 6, parsedInput)
	// part 1
	fmt.Println("Part 1: ", lightsOn(litGrid))
}
