package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"sort"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readFile(fileName string) [][]string {
	f, err := ioutil.ReadFile(fileName)
	check(err)
	lines := strings.Split(string(f), "\n")

	chars := make([][]string, 0)

	for _, line := range lines {
		chars = append(chars, strings.Split(line, ""))
	}

	return chars
}

func tops(s []string) string {
	return s[len(s)-1]
}

func makeScore(f map[string]int) int {
	sc := 0

	for k, v := range f {
		if k == ")" {
			sc += (v * 3)
		} else if k == "}" {
			sc += (v * 1197)
		} else if k == ">" {
			sc += (v * 25137)
		} else if k == "]" {
			sc += (v * 57)
		} else {
			panic(fmt.Sprintf("found %s", k))
		}
	}

	return sc
}

func makeScore2(s []int) int {
	sort.Ints(s)
	return s[(len(s)-1)/2]
}

func main() {
	fileName := os.Args[1]
	chars := readFile(fileName)

	fails := make(map[string]int)
	nonCorrupt := make([][]string, 0)

	for _, line := range chars {
		s := make([]string, 0)
		fail := false
		for _, char := range line {
			if char == "<" || char == "(" || char == "[" || char == "{" {
				s = append(s, char)
				continue
			}

			top := tops(s)

			if !((char == ">" && top == "<") || (char == "]" && top == "[") || (char == "}" && top == "{") || (char == ")" && top == "(")) {
				fails[char] += 1
				fail = true
			}

			// remove the top char
			s = s[:len(s)-1]
		}
		if !fail {
			nonCorrupt = append(nonCorrupt, line)
		}
	}

	// part 1
	fmt.Println(makeScore(fails))

	scs := make([]int, 0)
	for _, line := range nonCorrupt {
		s := make([]string, 0)
		for _, char := range line {
			if char == "<" || char == "(" || char == "[" || char == "{" {
				s = append(s, char)
				continue
			}

			top := tops(s)

			if (char == ">" && top == "<") || (char == "]" && top == "[") || (char == "}" && top == "{") || (char == ")" && top == "(") {
				s = s[:len(s)-1]
			}
		}
		sc := 0
		for _, char := range rev(s) {
			sc *= 5
			if char == "(" {
				sc += 1
			} else if char == "[" {
				sc += 2
			} else if char == "{" {
				sc += 3
			} else if char == "<" {
				sc += 4
			}
		}
		scs = append(scs, sc)
	}

	// part 2
	fmt.Println(makeScore2(scs))
}

func rev(arr []string) []string {
	for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
		arr[i], arr[j] = arr[j], arr[i]
	}
	return arr
}
