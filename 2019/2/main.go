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

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	input := []int{}

	for scanner.Scan() {
		currentLine := scanner.Text()

		inputSplit := strings.Split(currentLine, ",")

		for _, in := range inputSplit {
			inputInt, err := strconv.Atoi(in)
			isError(err)
			input = append(input, inputInt)
		}
	}

	input[1] = 12
	input[2] = 2

	pos := 0

	for {
		if input[pos] == 1 {
			sum := input[input[pos+1]] + input[input[pos+2]]
			input[input[pos+3]] = sum
			pos += 4
		} else if input[pos] == 2 {
			product := input[input[pos+1]] * input[input[pos+2]]
			input[input[pos+3]] = product
			pos += 4
		} else if input[pos] == 99 {
			break
		}
	}

	fmt.Println(input[0])
}
