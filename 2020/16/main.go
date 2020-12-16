package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type Range struct {
	num1 int
	num2 int
}

type RangeObj struct {
	name string
	ran1 Range
	ran2 Range
}

func parseInput(filename string) []string {
	fileInp, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Failed to read the file")
	}
	strInput := string(fileInp)
	lines := strings.Split(strInput, "\n\n")
	return lines
}

func checkIsPresentInRange(ranges []RangeObj, currentNum int) bool {
	for _, v := range ranges {
		if v.ran1.num1 <= currentNum && v.ran1.num2 >= currentNum {
			return true
		} else if v.ran2.num1 <= currentNum && v.ran2.num2 >= currentNum {
			return true
		}
	}
	return false
}

func removeTicket(arr []int, index int) []int {
	return append(arr[:index], arr[index+1:]...)
}

func contains(arr []int, item int) bool {
	for _, v := range arr {
		if v == item {
			return true
		}
	}
	return false
}

func main() {
	parsedInput := parseInput("16.in")
	rangesStr := strings.Split(parsedInput[0], "\n")
	myTicketsStr := strings.Split(strings.Split(parsedInput[1], "\n")[1], ",")
	ticketRangeStr := strings.Split(parsedInput[2], "\n")[1:]
	myRanges := make([]RangeObj, 0, len(rangesStr))
	myTickets := make([]int, 0, len(myTicketsStr))
	ticketsRange := make([][]int, len(ticketRangeStr))
	rangeMap := make(map[string]int)

	for _, v := range myTicketsStr {
		num, err := strconv.Atoi(v)
		if err != nil {
			fmt.Println("failed to parse number")
		}
		myTickets = append(myTickets, num)
	}

	for i, v := range ticketRangeStr {
		vSpl := strings.Split(v, ",")
		newRanges := make([]int, 0, len(vSpl))
		for _, u := range vSpl {
			num, err := strconv.Atoi(u)
			if err != nil {
				fmt.Println("failed to parse number")
			}
			newRanges = append(newRanges, num)
		}
		ticketsRange[i] = newRanges
	}

	for _, v := range rangesStr {
		vSpl := strings.Split(v, ": ")
		name := vSpl[0]
		rangeMap[name] = -1
		rs := strings.Split(vSpl[1], " or ")
		r1s := strings.Split(rs[0], "-")
		r2s := strings.Split(rs[1], "-")
		r1 := make([]int, 0, 2)
		r2 := make([]int, 0, 2)
		for _, i := range r1s {
			num, err := strconv.Atoi(i)
			if err != nil {
				fmt.Println("failed to parse number")
			}
			r1 = append(r1, num)
		}
		for _, i := range r2s {
			num, err := strconv.Atoi(i)
			if err != nil {
				fmt.Println("failed to parse number")
			}
			r2 = append(r2, num)
		}
		r := RangeObj{
			name: name,
			ran1: Range{
				num1: r1[0],
				num2: r1[1],
			},
			ran2: Range{
				num1: r2[0],
				num2: r2[1],
			},
		}
		myRanges = append(myRanges, r)
	}

	// part 1
	errRate := 0
	for i, v := range ticketsRange {
		newRan := make([]int, len(v))
		copy(newRan, v)
		fmt.Println("bef: ", newRan, i, len(newRan))
		for j, u := range v {
			if !checkIsPresentInRange(myRanges, u) {
				errRate += u
				newRan = removeTicket(v, j)
				fmt.Println("after:", newRan, len(newRan), u)
			}
		}
		ticketsRange[i] = newRan
	}
	fmt.Println("Part 1: ", errRate)

	// part 2
	max := len(myRanges)
	found := make([]int, 0, max)
	for len(found) != max {
		for ti, v := range ticketsRange {
			for _, u := range myRanges {
				if i, _ := rangeMap[u.name]; i != -1 {
					continue
				} else {
					if len(found) == max-1 && !contains(found, ti) {
						rangeMap[u.name] = ti
						found = append(found, ti)
						break
					}
					follow := true
					for _, n := range v {
						if (n >= u.ran1.num1 && n <= u.ran1.num2) || (n >= u.ran2.num1 && n <= u.ran2.num2) {
							continue
						} else {
							follow = false
						}
					}
					if follow && !contains(found, ti) {
						found = append(found, ti)
						rangeMap[u.name] = ti
						break
					}
				}
			}
		}
	}
	pr := 1
	for k, v := range rangeMap {
		if strings.Contains(k, "departure") {
			fmt.Println(k, v, myTickets[v])
			pr *= myTickets[v]
		}
	}
	fmt.Println("Part 2: ", pr)
	fmt.Println("Rmap", rangeMap)
}
