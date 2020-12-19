package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type instr struct {
	cmd string
	op1 string
	op2 string
}

func parseInput(filename string) []instr {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Failed to read file")
	}
	lines := strings.Split(string(buf), "\n")
	list := make([]instr, 0, len(lines))

	for _, v := range lines {
		spl := strings.Split(v, " ")
		if len(spl) == 3 {
			list = append(list, instr{
				cmd: spl[0],
				op1: spl[1],
				op2: spl[2],
			})
		} else {
			list = append(list, instr{
				cmd: spl[0],
				op1: spl[1],
				op2: "",
			})
		}
	}

	return list
}

func runProgram(initMap map[string]int, insts []instr) map[string]int {
	iter := 0
	regMap := initMap

	for iter < len(insts) {
		curr := insts[iter]
		// fmt.Println(curr)
		if curr.cmd == "inc" {
			regMap[curr.op1]++
		} else if curr.cmd == "dec" {
			regMap[curr.op1]--
		} else if curr.cmd == "cpy" {
			n, err := strconv.Atoi(curr.op1)
			if err == nil {
				regMap[curr.op2] = n
			} else {
				regMap[curr.op2] = regMap[curr.op1]
			}
		} else if curr.cmd == "jnz" {
			n2, err := strconv.Atoi(curr.op1)
			if err == nil {
				if n2 != 0 {
					n, err := strconv.Atoi(curr.op2)
					if err == nil {
						iter += n - 1
					}
				}
			} else {
				if regMap[curr.op1] != 0 {
					n, err := strconv.Atoi(curr.op2)
					if err == nil {
						iter += n - 1
					}
				}
			}
		}
		iter++
	}

	return regMap
}

func main() {
	parsedInput := parseInput("12.in")

	regMap := map[string]int{
		"a": 0,
		"b": 0,
		"c": 0,
		"d": 0,
	}
	regMap2 := map[string]int{
		"a": 0,
		"b": 0,
		"c": 1,
		"d": 0,
	}

	regMap = runProgram(regMap, parsedInput)
	regMap2 = runProgram(regMap2, parsedInput)

	fmt.Println("Part A: ", regMap["a"])
	fmt.Println("Part B:", regMap2["a"])
}
