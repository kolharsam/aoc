package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type point struct {
	x int
	y int
}

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func convertToNumber(s string) int {
	num, err := strconv.Atoi(s)
	isError(err)
	return num
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	grid := make(map[point][]int)
	emptyIntArr := []int{}
	ids := make(map[int]bool)
	i, j := 0, 0

	for i < 1000 {
		for j < 1000 {
			grid[point{x: i, y: j}] = emptyIntArr
			j++
		}
		i++
		j = 0
	}

	for scanner.Scan() {
		currentLine := scanner.Text()
		strSplit := strings.Split(currentLine, " ")

		// ugly stuff down here. but essentially the point is to just split the string
		// and subsequently obtain all the values that we care about
		// and later place the id on the respective point{} present in the map

		id := convertToNumber(strings.Split(strSplit[0], "#")[1])
		ids[id] = true
		remCol := strings.Split(strings.Split(strSplit[2], ":")[0], ",")
		itersX, itersY := convertToNumber(remCol[0]), convertToNumber(remCol[1])
		dims := strings.Split(strSplit[3], "x")
		dimX, dimY := convertToNumber(dims[0]), convertToNumber(dims[1])

		maxX, maxY := itersX+dimX, itersY+dimY

		for itersX < maxX {
			for itersY < maxY {
				currentPoint := point{
					x: itersX,
					y: itersY,
				}
				grid[currentPoint] = append(grid[currentPoint], id)
				itersY++
			}
			itersX++
			itersY = convertToNumber(remCol[1])
		}
	}

	ans1 := make(map[point][]int)

	for k, v := range grid {
		if len(v) > 1 {
			ans1[k] = v
			t := 0
			for t < len(v) {
				ids[v[t]] = false
				t++
			}
		}
	}

	fmt.Println(len(ans1)) // part 1

	for k := range ids {
		if ids[k] == true {
			fmt.Println(k) // part 2
		}
	}
}
