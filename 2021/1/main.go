package main

import (
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readFile(fileName string) []int {
	body, err := ioutil.ReadFile(fileName)
	check(err)

	lines := strings.Split(string(body), "\n")

	nums := make([]int, 2000)

	for _, str := range lines {
		num, err := strconv.Atoi(str)
		check(err)
		nums = append(nums, num)
	}

	return nums
}

func partOne(nums []int) {
	cin := 0

	for i, num := range nums {
		if i != 0 && num > nums[i-1] {
			cin++
		}
	}

	println(cin - 1)
}

func partTwo(nums []int) {
	cin := 0

	for i, num := range nums {
		if i < 3 {
			continue
		}

		if num > nums[i-3] {
			cin++
		}

		if i >= len(nums)-3 {
			break
		}
	}

	println(cin - 1)
}

func main() {
	fileName := os.Args[1]
	nums := readFile(fileName)

	partOne(nums)
	partTwo(nums)
}
