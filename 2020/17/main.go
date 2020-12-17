package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

type Point struct {
	W, X, Y, Z int
}

func (c Point) fetchAdjacent(isPart2 bool) []Point {
	var coords []Point
	for xOffset := -1; xOffset <= 1; xOffset++ {
		for yOffset := -1; yOffset <= 1; yOffset++ {
			for zOffset := -1; zOffset <= 1; zOffset++ {
				for wOffset := -1; wOffset <= 1; wOffset++ {
					if wOffset != 0 && !isPart2 {
						continue
					}
					if xOffset == 0 && yOffset == 0 && zOffset == 0 && wOffset == 0 {
						continue
					}
					coords = append(coords, Point{c.W + wOffset, c.X + xOffset, c.Y + yOffset, c.Z + zOffset})
				}
			}
		}
	}
	return coords
}

func (c Point) getNeighbours(active map[Point]bool, isPart2 bool) int {
	count := 0
	for _, n := range c.fetchAdjacent(isPart2) {
		if active[n] {
			count++
		}
	}
	return count
}

func playGame(active map[Point]bool, isPart2 bool) map[Point]bool {
	new_active := active
	for i := 0; i < 6; i++ {
		prevActive := make(map[Point]bool)
		for k := range active {
			for _, n := range k.fetchAdjacent(isPart2) {
				if _, exists := prevActive[n]; !exists {
					prevActive[n] = false
				}
			}
			prevActive[k] = true
		}

		for k, act := range prevActive {
			if act {
				activeNeighbors := k.getNeighbours(prevActive, isPart2)
				if activeNeighbors != 2 && activeNeighbors != 3 {
					delete(new_active, k)
				}
			} else {
				if k.getNeighbours(prevActive, isPart2) == 3 {
					new_active[k] = true
				}
			}
		}
	}
	return new_active
}

func main() {
	bytes, err := ioutil.ReadFile("17.in")
	if err != nil {
		return
	}
	contents := string(bytes)
	split := strings.Split(contents, "\n")
	split = split[:len(split)-1]
	active := make(map[Point]bool)
	active2 := make(map[Point]bool)
	for y, s := range split {
		for x, v := range s {
			switch v {
			case '#':
				active[Point{0, x, y, 0}] = true
				active2[Point{0, x, y, 0}] = true
			}
		}
	}

	a1 := playGame(active, false)
	result := 0
	for _, v := range a1 {
		if v {
			result++
		}
	}
	// part 1
	fmt.Println(result)

	a2 := playGame(active2, true)
	result = 0
	for _, v := range a2 {
		if v {
			result++
		}
	}
	// part 2
	fmt.Println(result)
}
