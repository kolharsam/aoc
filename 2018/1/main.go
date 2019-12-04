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

func hasKey(m map[int]bool, key int) bool {
	_, ok := m[key]
	return ok
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	sum := 0
	lis := []int{}

	for scanner.Scan() {
		c := scanner.Text()
		p, err := strconv.Atoi(c)
		isError(err)
		lis = append(lis, p)
	}

	iter := 0
	for iter < len(lis) {
		sum += lis[iter]
		iter++
	}

	fmt.Println(sum) // part 1

	res := make(map[int]bool)
	pointer := 0
	sum = 0

	for {
		sum += lis[pointer]

		if hasKey(res, sum) {
			fmt.Println(lis[pointer], sum, pointer) // part 2
			break
		} else {
			res[sum] = true
			pointer = (pointer + 1) % len(lis)
		}
	}
}
