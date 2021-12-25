package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

type Coord struct {
	Row, Col int
}

func (pos *Coord) Wrap(max Coord) {
	if pos.Row >= max.Row {
		pos.Row = 0
	}
	if pos.Col >= max.Col {
		pos.Col = 0
	}
}

// Be careful: empty = no cucumber, true = downward cucumber, false = rightward
type Board map[Coord]bool

func (b Board) Print(max Coord) {
	for r := 0; r < max.Row; r++ {
		for c := 0; c < max.Col; c++ {
			if south, occupied := b[Coord{r, c}]; !occupied {
				fmt.Printf(".")
			} else if south {
				fmt.Printf("v")
			} else {
				fmt.Printf(">")
			}
		}
		fmt.Println()
	}
}

func readFile(fileName string) (Board, Coord) {
	b := make(Board)
	max := Coord{Row: 0, Col: 0}

	bytes, err := ioutil.ReadFile(fileName)
	if err != nil {
		panic(err)
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n")
	split = split[:len(split)-1]

	max.Row = len(split)
	max.Col = len(split[0])

	for r, line := range split {
		for c, elem := range line {
			switch elem {
			case '.':
				// Do nothing.
			case '>':
				b[Coord{r, c}] = false
			case 'v':
				b[Coord{r, c}] = true
			}
		}
	}

	return b, max
}

func main() {
	fileName := os.Args[1]
	board, max := readFile(fileName)

	var toggle bool
	var prevMoved bool
	for steps := 1; ; steps++ {
		var anyMoved bool
		next := make(Board)
		for src, south := range board {
			if south == toggle {
				dst := src
				if toggle {
					dst.Row++
				} else {
					dst.Col++
				}
				dst.Wrap(max)
				if _, occupied := board[dst]; !occupied {
					next[dst] = south
					anyMoved = true
				} else {
					next[src] = south
				}
			} else {
				next[src] = south
			}
		}
		board = next
		toggle = !toggle
		if !anyMoved && !prevMoved {
			fmt.Println((steps + 1) / 2)
			break
		}
		prevMoved = anyMoved
	}
}
