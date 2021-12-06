package main

import (
	"fmt"
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

type FishMap map[int]int

func readFile(fileName string) FishMap {
	body, err := ioutil.ReadFile(fileName)
	check(err)

	line := strings.Split(string(body), "\n")

	numStrs := strings.Split(line[0], ",")

	nums := make(FishMap)

	for _, numStr := range numStrs {
		num, err := strconv.Atoi(numStr)
		check(err)
		nums[num]++
	}

	return nums
}

func (fm FishMap) solve(stop int) {
	dayCount := 0

	for dayCount != stop {
		oldFM := fm
		fm = make(FishMap)
		for k, v := range oldFM {
			if k == 0 {
				fm[6] += v
				fm[8] += v
				continue
			}
			fm[k-1] += v
		}
		dayCount++
	}

	count := 0
	for _, v := range fm {
		count += v
	}
	fmt.Println(count)
}

func main() {
	fileName := os.Args[1]
	fishMap := readFile(fileName)

	fishMap.solve(80)
	fishMap.solve(256)
}
