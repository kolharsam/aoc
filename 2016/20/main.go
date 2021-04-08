package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
	// "sort"
)

type rangeTuple struct {
	start uint32
	end   uint32
}

// type allowedIPs []uint32

// func (a allowedIPs) Len() int {
// 	return len(a)
// }

// func (a allowedIPs) Swap(i, j int) {
// 	a[i], a[j] = a[j], a[i]
// }

// func (a allowedIPs) Less(i, j int) bool {
// 	return a[i] < a[j]
// }

func main() {
	data, err := ioutil.ReadFile("input")
	if err != nil {
		panic(err.Error())
	}
	lines := strings.Split(string(data), "\n")

	rangeList := make([]rangeTuple, 0)

	for _, line := range lines {
		var newRT rangeTuple
		parts := strings.Split(line, "-")
		p1, err := strconv.Atoi(parts[0])
		if err != nil {
			panic(err.Error())
		}
		newRT.start = uint32(p1)
		p2, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err.Error())
		}
		newRT.end = uint32(p2)
		rangeList = append(rangeList, newRT)
	}

	var counter uint32 = 0
	count := 0

	for counter != 4294967295 {
		found := false
		for _, rng := range rangeList {
			if rng.start <= counter && rng.end >= counter {
				found = true
				break
			}
		}
		if !found {
			if count == 0 {
				// Part 1
				fmt.Println(counter)
			}
			count += 1
		}
		counter += 1
	}

	// sort.Sort(allowedIPs(allowlist))

	// Part 2
	fmt.Println(count)
}
