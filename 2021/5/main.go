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
	X int
	Y int
}

type Line struct {
	P1 Point
	P2 Point
}

func readFile(fileName string) []Line {
	body, err := ioutil.ReadFile(fileName)
	check(err)

	lines := strings.Split(string(body), "\n")

	lineList := make([]Line, 0)

	for _, line := range lines {
		ps := strings.Split(line, " -> ")
		var newLine Line
		for i, p := range ps {
			psp := strings.Split(p, ",")
			num1, err := strconv.Atoi(psp[0])
			check(err)
			num2, err := strconv.Atoi(psp[1])
			check(err)
			if i == 0 {
				newLine.P1 = Point{X: num1, Y: num2}
			} else if i == 1 {
				newLine.P2 = Point{X: num1, Y: num2}
			}
		}
		lineList = append(lineList, newLine)
	}

	return lineList
}

func solve(lines []Line) {
	lineMap := make(map[Point]int)
	lineMap2 := make(map[Point]int)

	for _, line := range lines {
		if line.P1.X == line.P2.X {
			if line.P2.Y > line.P1.Y {
				for i := line.P1.Y; i <= line.P2.Y; i++ {
					lineMap[Point{X: line.P1.X, Y: i}]++
					lineMap2[Point{X: line.P1.X, Y: i}]++
				}
			} else {
				for i := line.P1.Y; i >= line.P2.Y; i-- {
					lineMap[Point{X: line.P1.X, Y: i}]++
					lineMap2[Point{X: line.P1.X, Y: i}]++
				}
			}
		} else if line.P2.Y == line.P1.Y {
			if line.P1.X < line.P2.X {
				for i := line.P1.X; i <= line.P2.X; i++ {
					lineMap[Point{X: i, Y: line.P1.Y}]++
					lineMap2[Point{X: i, Y: line.P1.Y}]++
				}
			} else {
				for i := line.P1.X; i >= line.P2.X; i-- {
					lineMap[Point{X: i, Y: line.P1.Y}]++
					lineMap2[Point{X: i, Y: line.P1.Y}]++
				}
			}
		} else {
			// Part 2 stuff
			if line.P1.X < line.P2.X {
				yIncr := 1
				if line.P1.Y > line.P2.Y {
					yIncr = -1
				}
				y := line.P1.Y
				for x := line.P1.X; x <= line.P2.X; x++ {
					lineMap2[Point{x, y}]++
					y += yIncr
				}
			} else {
				yIncr := 1
				if line.P1.Y > line.P2.Y {
					yIncr = -1
				}
				y := line.P1.Y
				for x := line.P1.X; x >= line.P2.X; x-- {
					lineMap2[Point{x, y}]++
					y += yIncr
				}
			}
		}
	}

	fmt.Println(makeCount(lineMap))
	fmt.Println(makeCount(lineMap2))
}

func makeCount(lineMap map[Point]int) int {
	count := 0

	for _, v := range lineMap {
		if v >= 2 {
			count++
		}
	}

	return count
}

func main() {
	fileName := os.Args[1]
	lines := readFile(fileName)
	solve(lines)
}
