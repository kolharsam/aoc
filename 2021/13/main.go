package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

type Point struct {
	X, Y int
}

type Paper map[Point]bool

type Fold struct {
	X    bool
	Unit int
}

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func readFile(fileName string) (Paper, []Fold) {
	bytes, err := ioutil.ReadFile(fileName)
	check(err)

	split := strings.Split(string(bytes), "\n")

	parsingCoordinates := true
	paper := make(Paper)
	var folds []Fold
	for _, s := range split {
		if s == "" {
			parsingCoordinates = false
			continue
		}
		if parsingCoordinates {
			parts := strings.Split(s, ",")
			x, _ := strconv.Atoi(parts[0])
			y, _ := strconv.Atoi(parts[1])
			paper[Point{x, y}] = true
		} else {
			var fold Fold
			if s[len("fold along ")] == byte('x') {
				fold.X = true
			}
			fold.Unit, _ = strconv.Atoi(s[len("fold along x="):])
			folds = append(folds, fold)
		}
	}

	return paper, folds
}

func (f Fold) makeFold(p Paper) Paper {
	newPaper := make(Paper)
	for coord := range p {
		var diff int
		if f.X {
			diff = coord.X - f.Unit
		} else {
			diff = coord.Y - f.Unit
		}
		if diff > 0 {
			// Mirror it over the Offset line.
			if f.X {
				coord.X = f.Unit - diff
			} else {
				coord.Y = f.Unit - diff
			}
			newPaper[coord] = true
		} else if diff < 0 {
			// Retain its current position.
			newPaper[coord] = true
		} else {
			// We should never fold on a dot.
			fmt.Printf("Attempted to fold on X=%d, but dot on line.\n", f.Unit)
		}
	}
	return newPaper
}

func main() {
	fileName := os.Args[1]
	paper, folds := readFile(fileName)

	for i, f := range folds {
		paper = f.makeFold(paper)
		if i == 0 {
			// Part 1
			fmt.Println(len(paper))
		}
	}

	var maxX, maxY int
	for coords := range paper {
		if coords.X > maxX {
			maxX = coords.X
		}
		if coords.Y > maxY {
			maxY = coords.Y
		}
	}
	// Part 2 - printing after the folds
	for y := 0; y <= maxY; y++ {
		for x := 0; x <= maxX; x++ {
			if paper[Point{x, y}] {
				fmt.Printf("#")
			} else {
				fmt.Printf(".")
			}
		}
		fmt.Println()
	}
}
