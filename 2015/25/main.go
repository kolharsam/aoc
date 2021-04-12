package main

import "fmt"

const rowNum int = 2947
const colNum int = 3029

func next(num uint64) uint64 {
	multiplier := uint64(252533)
	divisor := uint64(33554393)
	return (num * multiplier) % divisor
}

func main() {
	i, j, k := 1, 1, 1
	num := uint64(20151125)

	for {
		if j == k {
			k++
			i = k
			j = 1
		} else {
			i--
			j++
		}
		num = next(num)
		if i == rowNum && j == colNum {
			break
		}
	}
	// Part 1
	fmt.Println(num)
}
