package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
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
		currentNumber, err := strconv.Atoi(scanner.Text())
		isError(err)
		input = append(input, currentNumber)
	}

	inputSize := len(input)
	steps := 0
	pointer := 0
	prev := 0

	for pointer < inputSize {
		prev = pointer
		pointer += input[pointer]

		if pointer-prev >= 3 {
			input[prev]--
		} else {
			input[prev]++
		}

		steps++
	}

	fmt.Println(steps)
}
