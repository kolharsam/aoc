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

func getFuel(module int) int {
	total := 0
	fuel := module

	for fuel >= 0 {
		nextfuel := (fuel / 3) - 2
		if nextfuel >= 0 {
			total += nextfuel
			fuel = nextfuel
		} else {
			break
		}
	}

	return total
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	total := 0

	for scanner.Scan() {
		number, err := strconv.Atoi(scanner.Text())
		isError(err)

		total += getFuel(number)
	}

	fmt.Println(total)
}
