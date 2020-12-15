package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type packet struct {
	depth   int
	ran     int
	reverse bool
}

func parseInput(filename string) []packet {
	readLines, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Failed to read file")
	}

	fileLines := string(readLines)
	lines := strings.Split(fileLines, "\n")
	parsedList := make([]packet, len(lines))

	for i, v := range lines {
		lSplit := strings.Split(v, ": ")
		numD, err := strconv.Atoi(lSplit[0])
		if err != nil {
			fmt.Println("There was an error in conversion")
		}
		numR, err := strconv.Atoi(lSplit[1])
		if err != nil {
			fmt.Println("There was an error in conversion")
		}
		parsedList[i] = packet{
			depth:   numD,
			ran:     numR,
			reverse: false,
		}
	}
	return parsedList
}

// basically only looking at the depth
func contains(list []packet, elem int) bool {
	for _, v := range list {
		if v.depth == elem {
			return true
		}
	}
	return false
}

func main() {
	parsedList := parseInput("13.in")
	depths := make(map[int]packet)
	currentPos := make(map[int]int)
	max := 0
	for _, v := range parsedList {
		currentPos[v.depth] = 0
		depths[v.depth] = v
		if v.depth > max {
			max = v.depth
		}
	}
	caught := make([]packet, 0, max)
	clock := 0
	for clock <= max {
		// first part will handle the packet's movement
		if clock == 0 {
			caught = append(caught, depths[0])
		} else if contains(parsedList, clock) {
			if currentPos[clock] == 0 {
				caught = append(caught, depths[clock])
			}
		}
		// second part would be handling the movement of scanner
		for k, v := range depths {
			currentDiv := (currentPos[k]+1)%v.ran == 0
			if v.reverse && currentPos[k] == 0 {
				depths[k] = packet{
					depth:   depths[k].depth,
					ran:     depths[k].ran,
					reverse: false,
				}
				currentPos[k]++
			} else if v.reverse && !currentDiv {
				currentPos[k]--
			} else if !v.reverse && !currentDiv {
				currentPos[k]++
			} else if !v.reverse && currentDiv {
				depths[k] = packet{
					depth:   depths[k].depth,
					ran:     depths[k].ran,
					reverse: true,
				}
				currentPos[k]--
			}
		}
		clock++
	}
	// part 1 severity score
	ans := 0
	for _, v := range caught {
		ans += v.depth * v.ran
	}
	fmt.Println(ans)

	// part 2 find delay time
	// the only method I knew of was to brute force the whole thing
	// until the caught list is empty at a particular delay time.

	// the one other way I can think of is to use something like the chinese
	// remainder theorem repeatedly until we are able to find one number from where
	// we can successfully go through all of the depths without encountering
	// them scanners
}
