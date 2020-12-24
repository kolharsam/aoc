package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

var sampleInputFile string = "24-sample.in"
var probInputFile string = "24.in"

type coord struct {
	x int
	y int
	z int
}

func (c coord) getAdjacentTiles() []coord {
	return []coord{
		{
			x: c.x + 1,
			y: c.y - 1,
			z: c.z,
		},
		{
			x: c.x - 1,
			y: c.y + 1,
			z: c.z,
		},
		{
			x: c.x - 1,
			y: c.y,
			z: c.z + 1,
		},
		{
			x: c.x + 1,
			y: c.y,
			z: c.z - 1,
		},
		{
			x: c.x,
			y: c.y - 1,
			z: c.z + 1,
		},
		{
			x: c.x,
			y: c.y + 1,
			z: c.z - 1,
		},
	}
}

func (c coord) getNeighbours(m map[coord]bool) int {
	count := 0
	for _, v := range c.getAdjacentTiles() {
		if m[v] {
			count++
		}
	}
	return count
}

func parseDirections(str string) []string {
	a := make([]string, 0, len(str))
	iter := 0
	ar := []rune(str)

	// e, se, sw, w, nw, and ne
	for iter < len(ar) {
		curr := string(ar[iter])
		if curr == "e" || curr == "w" {
			a = append(a, curr)
			iter++
			continue
		} else {
			dir := curr + string(ar[iter+1])
			a = append(a, dir)
			iter += 2
		}
	}

	return a
}

func parseInput(filename string) [][]string {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Unable to read the file")
	}
	lines := strings.Split(string(buf), "\n")
	dirs := make([][]string, len(lines))

	for i, v := range lines {
		dirs[i] = parseDirections(v)
	}

	return dirs
}

func main() {
	parsedInput := parseInput(probInputFile)
	// false - white and black - true
	knownTiles := make(map[coord]bool)
	start := coord{
		x: 0,
		y: 0,
		z: 0,
	}

	for _, tileInstr := range parsedInput {
		tile := start
		for _, v := range tileInstr {
			switch v {
			case "e":
				tile.x++
				tile.y--
				break
			case "w":
				tile.x--
				tile.y++
				break
			case "se":
				tile.z++
				tile.y--
				break
			case "sw":
				tile.x--
				tile.z++
				break
			case "ne":
				tile.x++
				tile.z--
				break
			case "nw":
				tile.z--
				tile.y++
				break
			}
		}
		if _, ok := knownTiles[tile]; ok {
			if knownTiles[tile] {
				delete(knownTiles, tile)
			}
		} else {
			knownTiles[tile] = true
		}
	}

	// Part 1
	fmt.Println(len(knownTiles))

	// Part 2 - Game of life with hexagonal tiles!
	r := 1
	for r <= 100 {
		newKnownMap := make(map[coord]bool)
		prevActiveMap := make(map[coord]bool)
		// update known tiles with neighbours of current known tiles
		for k := range knownTiles {
			upd := k.getAdjacentTiles()
			for _, v := range upd {
				if _, ok := knownTiles[v]; !ok {
					prevActiveMap[v] = false
				}
			}
			prevActiveMap[k] = true
		}
		for k, v := range prevActiveMap {
			aliveNeighbours := k.getNeighbours(prevActiveMap)
			if v {
				if aliveNeighbours == 1 || aliveNeighbours == 2 {
					newKnownMap[k] = true
				}
			} else {
				if aliveNeighbours == 2 {
					newKnownMap[k] = true
				}
			}
		}
		knownTiles = newKnownMap
		r++
	}
	fmt.Printf("Day %d: %d\n", r-1, len(knownTiles))
}
