package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

const gridBoxPrefix string = "/dev/grid/node-"

// NOTE: only x = 0 and y = 0 has full access to node data

type gridStoreItem struct {
	x           int
	y           int
	total       int
	free        int
	used        int
	usedPercent int
	fullAccess  bool
}

type gridStore []gridStoreItem

func (g gridStore) findViablePairs() int {
	count := 0
	for _, gsi := range g {
		for _, gsj := range g {
			if gsi.x == gsj.x && gsi.y == gsj.y {
				continue
			}
			if gsi.used == 0 {
				continue
			}
			if gsi.used < gsj.free {
				fmt.Println(gsi.x, gsi.y, gsj.x, gsj.y)
				count += 1
			}
		}
	}
	return count
}

func (g gridStore) findHighestX() int {
	high := 0
	for _, gsi := range g {
		if gsi.x > high && gsi.y == 0 {
			high = gsi.x
		}
	}
	return high
}

func (g gridStore) findMinSteps() int {
	steps := 0
	high_x := g.findHighestX()
	fmt.Println(high_x)

	return steps
}

func parseInfo(filename string) (*gridStore, error) {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(string(data), "\n")

	gs := make(gridStore, 0)
	for i, line := range lines {
		if i == 0 || i == 1 {
			continue
		}
		re := regexp.MustCompile(`\d+`)
		ll := re.FindAll([]byte(line), -1)

		gridNums := make([]int, 0)
		for _, b := range ll {
			bi := string(b)
			bin, err := strconv.Atoi(bi)
			if err != nil {
				panic(err.Error())
			}
			gridNums = append(gridNums, bin)
		}
		var gsi gridStoreItem
		gsi.x = gridNums[0]
		gsi.y = gridNums[1]
		gsi.total = gridNums[2]
		gsi.used = gridNums[3]
		gsi.free = gridNums[4]
		gsi.usedPercent = gridNums[5]
		gsi.fullAccess = false
		if gridNums[0] == 0 && gridNums[1] == 0 {
			gsi.fullAccess = true
		}

		gs = append(gs, gsi)
	}

	return &gs, nil
}

func main() {
	store, err := parseInfo("sample")
	if err != nil {
		panic(err.Error())
	}
	// part 1
	fmt.Println(store.findViablePairs())
	// part 2
	fmt.Println(store.findMinSteps())
}
