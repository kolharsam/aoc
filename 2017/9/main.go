package main

import (
	"bufio"
	"container/list"
	"fmt"
	"os"
)

// groups are present within {} - are nestable
// "things" are comma(,) separated
// either another group or garbage

// garbage is enclosed btw <>
// another < in an open < does not make a diff.

// any character after ! must be ignored

// score is given based on the depth of the group that it is found

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	input := ""

	for scanner.Scan() {
		input = scanner.Text()
	}

	inputsize := len(input)
	pointer := 0
	stack := list.New()
	ignoreFlag := false
	totalScore := 0
	canceled := 0

	for pointer < inputsize {
		currentChar := string(input[pointer])

		if currentChar == "{" && !ignoreFlag {
			stack.PushFront("{")
			pointer++
		} else if currentChar == "}" && !ignoreFlag {
			totalScore += stack.Len()
			stack.Remove(stack.Front())
			pointer++
		} else if currentChar == "<" && !ignoreFlag {
			ignoreFlag = true
			pointer++
		} else if currentChar == ">" && ignoreFlag {
			ignoreFlag = false
			pointer++
		} else if currentChar == "!" {
			pointer += 2
		} else if ignoreFlag {
			canceled++
			pointer++
		} else {
			pointer++
		}

	}

	fmt.Println(totalScore)
	fmt.Println(len(input), canceled)
}
