package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func convertToInt(s string) int {
	num, err := strconv.Atoi(s)
	isError(err)
	return num
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	lightGrid := [][]bool{}
	i, j := 0, 0

	for i < 1000 {
		j = 0
		tempLine := []bool{}
		for j < 1000 {
			tempLine = append(tempLine, false)
			j++
		}
		lightGrid = append(lightGrid, tempLine)
		i++
	}

	for scanner.Scan() {
		currentInstr := scanner.Text()
		strSplit := strings.Split(currentInstr, " through ")
		instr := -1
		instLen := len(strSplit)

		locSplittemp := strings.Split(strSplit[0], " ")
		loc1Split := strings.Split(locSplittemp[len(locSplittemp)-1], ",")
		loc2Split := strings.Split(strSplit[instLen-1], ",")

		if locSplittemp[0] == "turn" {
			if locSplittemp[1] == "on" {
				instr = 1
			} else if locSplittemp[1] == "off" {
				instr = 0
			}
		} else {
			instr = 2
		}

		fromX, fromY := convertToInt(loc1Split[0]), convertToInt(loc1Split[1])
		toX, toY := convertToInt(loc2Split[0]), convertToInt(loc2Split[1])

		tempY := fromY

		for fromX <= toX {
			fromY = tempY
			for fromY <= toY {

				if instr == 0 {
					lightGrid[fromX][fromY] = false
				} else if instr == 1 {
					lightGrid[fromX][fromY] = true
				} else if instr == 2 {
					lightGrid[fromX][fromY] = !lightGrid[fromX][fromY]
				}

				fromY++
			}
			fromX++
		}
	}

	i, j = 0, 0
	counts := 0

	for i < 1000 {
		j = 0
		for j < 1000 {
			if lightGrid[i][j] == true {
				counts++
			}
			j++
		}
		i++
	}

	i, j = 0, 0

	// for i < 1000 {
	// 	for j < 1000 {
	// implement part 2 here
	// 	}
	// }

	fmt.Println(counts) // Part 1
}
