package main

import (
	"fmt"
)

var input int = 371

func run(limit int) []int {
	pos := 0
	number := 1
	list := make([]int, 0, limit)
	list = append(list, number)
	mod := input
	for number != limit {
		if pos == 0 {
			pos++
			list = append(list, number)
		} else {
			number++
			indexToInsert := (pos + mod) % len(list)
			pos = indexToInsert + 1
			l2 := make([]int, len(list))
			copy(l2, list)
			list = append(append(list[:indexToInsert+1], number), l2[indexToInsert+1:]...)
		}
	}
	return list
}

func main() {
	list := run(2017)
	// part 1
	for i, v := range list {
		if v == 2017 {
			fmt.Println(list[i+1])
			break
		}
	}

	// part 2
	res := 0
	head := 0
	for i := 1; i <= 50000000; i++ {
		head += input
		head %= i
		if head == 0 {
			res = i
		}
		head++
	}
	fmt.Println(res)
}
