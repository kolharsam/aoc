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

func toInt(i string) int {
	num, err := strconv.Atoi(i)
	isError(err)
	return num
}

func calcArea(l, w, h int) int {
	return (2 * l * w) + (2 * w * h) + (2 * h * l)
}

func greatest(a, b, c int) int {
	res := c

	if a >= b && a >= c {
		res = a
	} else if a <= b && c <= b {
		res = b
	}

	return res
}

func getSurfaceArea(l, b, h int) int {
	max := greatest(l, b, h)
	sum := l + b + h
	return 2 * (sum - max)
}

func calcVolume(l, b, h int) int {
	return l * b * h
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	area := 0
	ribbon := 0

	for scanner.Scan() {
		curBox := scanner.Text()
		dims := strings.Split(curBox, "x")
		l, w, h := toInt(dims[0]), toInt(dims[1]), toInt(dims[2])
		area += (calcArea(l, w, h) + ((l * w * h) / greatest(l, w, h)))
		ribbon += (getSurfaceArea(l, w, h) + calcVolume(l, w, h))
	}

	fmt.Println(area)   // part 1
	fmt.Println(ribbon) // part 2
}
