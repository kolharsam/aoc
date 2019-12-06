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

func processInput(in string) []int {
	splitString := strings.Split(in, " ")
	out := []int{}

	for i, el := range splitString {
		if el != "" {
			cur := strings.TrimSpace(splitString[i])
			ele, err := strconv.Atoi(cur)
			isError(err)
			out = append(out, ele)
		}
	}

	return out
}

func checkIfTriangle(numbers []int) bool {
	flag := false

	a, b, c := numbers[0], numbers[1], numbers[2]

	if a+b > c && b+c > a && c+a > b {
		flag = true
	}

	return flag
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	col1, col2, col3 := []int{}, []int{}, []int{}
	counter := 0
	tc := 0

	for scanner.Scan() {
		currentLine := scanner.Text()
		in := processInput(currentLine)

		// to read column wise
		col1 = append(col1, in[0])
		col2 = append(col2, in[1])
		col3 = append(col3, in[2])

		if checkIfTriangle(in) {
			counter++
		}
		tc++
	}

	fmt.Println(counter) // part 1

	i := 0
	counter = 0

	for i < (len(col1) - 2) {
		a, b, c := col1[i], col1[i+1], col1[i+2]
		if checkIfTriangle([]int{a, b, c}) {
			counter++
		}
		i += 3
	}

	i = 0

	for i < (len(col2) - 2) {
		a, b, c := col2[i], col2[i+1], col2[i+2]
		if checkIfTriangle([]int{a, b, c}) {
			counter++
		}
		i += 3
	}

	i = 0

	for i < (len(col3) - 2) {
		a, b, c := col3[i], col3[i+1], col3[i+2]
		if checkIfTriangle([]int{a, b, c}) {
			counter++
		}
		i += 3
	}

	fmt.Println(counter) // part 2
}
