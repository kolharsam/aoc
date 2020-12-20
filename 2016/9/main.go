package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseInput(filename string) string {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("failed to open the file")
	}
	line := strings.Split(string(buf), "\n")

	return line[0]
}

func countExpandedChars(line string, p2 bool) int {
	iter := 0
	tc := 0
	left := 0
	exp := false

	for iter < len(line) {
		current := string(line[iter])
		if current == " " {
			iter++
			continue
		}
		if !exp && current != "(" {
			tc++
		} else if !exp && current == "(" {
			it2 := iter + 1
			decom := ""

			for string(line[it2]) != ")" {
				decom += string(line[it2])
				it2++
			}
			it2++

			sp := strings.Split(decom, "x")
			n1, err := strconv.Atoi(sp[0])
			if err != nil {
				fmt.Printf("Failed to convert number %s\n", sp[0])
			}
			n2, err := strconv.Atoi(sp[1])
			if err != nil {
				fmt.Printf("Failed to convert number %s\n", sp[1])
			}

			exp = true
			if p2 {
				nn := countExpandedChars(string([]rune(line)[it2:it2+n1]), true)
				tc += nn * n2
			} else {
				tc += (n1 * n2)
			}
			iter += (it2 - iter)
			left = n1 - 1
			continue
		} else if exp && left == 0 {
			exp = false
		} else if exp && left != 0 {
			left--
		}
		iter++
	}

	return tc
}

func main() {
	readLine := parseInput("9.in")
	n := countExpandedChars(readLine, false)
	fmt.Println("Part 1: ", n)
	n2 := countExpandedChars(readLine, true)
	fmt.Println("Part 2: ", n2)
}
