package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseInput(filename string) []string {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("failed to open file")
	}
	lines := strings.Split(string(buf), "\n")

	return lines
}

func dealNewSet(xs []int) []int {
	n := len(xs)
	x := make([]int, n)
	copy(x, xs)

	for i := 0; i+i < n; i++ {
		x[i], x[n-1-i] = x[n-1-i], x[i]
	}

	return x
}

func cutCards(xs []int, num int) []int {
	if num > 0 {
		cut := xs[0:num]
		return append(xs[num:], cut...)
	}
	cut := xs[len(xs)+num:]
	rest := xs[:len(xs)+num]

	return append(cut, rest...)
}

func incrementDeal(xs []int, num int) []int {
	n := len(xs)
	counter := 0
	multi := 0
	x := make([]int, n)
	copy(x, xs)

	for counter != n {
		x[multi] = xs[counter]
		multi += num
		multi %= n
		counter++
	}

	return x
}

func convertToNumber(str string) int {
	n, err := strconv.Atoi(str)
	if err != nil {
		fmt.Println("Failed to convert number")
	}
	return n
}

func main() {
	parsedInput := parseInput("22.in")
	lim := 10007
	deck := make([]int, 0, lim)

	for i := 0; i < lim; i++ {
		deck = append(deck, i)
	}

	for _, line := range parsedInput {
		if strings.Contains(line, "cut") {
			spl := strings.Split(line, " ")
			n := convertToNumber(spl[1])
			deck = cutCards(deck, n)
		} else if strings.Contains(line, "increment") {
			spl := strings.Split(line, " ")
			n := convertToNumber(spl[3])
			deck = incrementDeal(deck, n)
		} else if strings.Contains(line, "new") {
			deck = dealNewSet(deck)
		} else {
			panic("New unidentified option!")
		}
	}

	// part 1
	for i, n := range deck {
		if n == 2019 {
			fmt.Println(i)
			break
		}
	}
	// part 2 - is a lot harder because it involves a lot of concepts from
	// combinatorics and number theory. Will take another crack at it soon
}
