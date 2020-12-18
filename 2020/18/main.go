package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseInput(filename string) []string {
	readlines, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("failed to read the file")
	}
	return strings.Split(string(readlines), "\n")
}

func evaluate(expr []rune) int {
	sum := 0
	iter := 0
	emp := make([]int, 0, 2)
	storage := make([]int, 0, 2)
	var lastOp rune

	for iter < len(expr) {
		if len(storage) == 2 {
			iter++
			if lastOp == '+' {
				sum += storage[0] + storage[1]
				storage = emp
				continue
			} else if lastOp == '*' {
				sum += storage[0] * storage[1]
				storage = emp
				continue
			}
		}
		current := expr[iter]
		fmt.Println(current, iter)
		if current != '(' && current != ')' && current != '+' && current != '*' {
			// it's a number
			n, err := strconv.Atoi(string(current))
			if err != nil {
				fmt.Println("failed to convert to number")
			}
			storage = append(storage, n)
			iter++
			continue
		}
		if current == '+' || current == '*' {
			lastOp = current
			iter++
			continue
		}
		if current == '(' {
			// recursive call to evaluate
			fmt.Println("Here")
			sub := make([]rune, 0, len(expr))
			it2 := iter + 1
			openCount := 1
			for openCount != 0 {
				if expr[it2] == ')' {
					openCount--
				} else if expr[it2] == '(' {
					openCount++
				}
				sub = append(sub, expr[it2])
				it2++
			}
			r := []rune(sub)
			// to remove the outer bracket
			fmt.Println(string(r[1 : len(r)-2]))
			storage = append(storage, evaluate(sub))
			// unsure of this
			iter += len(sub)
			continue
		}
	}

	return sum
}

func main() {
	parsedInput := parseInput("18-sample.in")
	sums := make([]int, 0, len(parsedInput))

	for _, str := range parsedInput {
		r := []rune(str)
		fmt.Println(str, r)
		r2 := make([]rune, 0, len(r))
		for _, v := range r2 {
			if v != ' ' {
				r2 = append(r2, v)
			}
		}
		fmt.Println(r2)
		num := evaluate(r2)
		sums = append(sums, num)
	}

	fmt.Println(sums)

	sum := 0
	for _, v := range sums {
		sum += v
	}
	// part 1
	fmt.Println(sum)
}
