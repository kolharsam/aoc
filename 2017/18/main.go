package main

import (
	"container/list"
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type prg struct {
	pos      int
	name     string
	register string
	op       string
}

func parseInput(filename string) []string {
	readlines, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Print("could not open the file")
	}
	lines := strings.Split(string(readlines), "\n")
	return lines
}

func getNumValue(regMap map[string]int, op string) int {
	n, err := strconv.Atoi(op)
	if err == nil {
		return n
	}
	return regMap[op]
}

func reverseList(a []prg) []prg {
	for i := len(a)/2 - 1; i >= 0; i-- {
		opp := len(a) - 1 - i
		a[i], a[opp] = a[opp], a[i]
	}
	return a
}

func main() {
	parsedInput := parseInput("18.in")
	prgQ := list.New()
	insts := make([]prg, 0, len(parsedInput))

	for i, v := range parsedInput {
		currLine := strings.Split(v, " ")
		cmd := currLine[0]
		reg := currLine[1]
		if len(currLine) > 2 {
			op := currLine[2]
			currPrg := prg{pos: i, name: cmd, register: reg, op: op}
			prgQ.PushBack(currPrg)
			insts = append(insts, currPrg)
		} else {
			currPrg := prg{pos: i, name: cmd, register: reg, op: ""}
			prgQ.PushBack(currPrg)
			insts = append(insts, currPrg)
		}
	}

	regMap := make(map[string]int)
	lastSnd := -1
	rcv := -1

	for prgQ.Len() != 0 {
		currInstElem := prgQ.Front()
		currInst := (currInstElem.Value).(prg)

		// fmt.Println(currInst, regMap)

		switch currInst.name {
		case "set":
			regMap[currInst.register] = getNumValue(regMap, currInst.op)
		case "add":
			regMap[currInst.register] += getNumValue(regMap, currInst.op)
		case "mul":
			regMap[currInst.register] *= getNumValue(regMap, currInst.op)
		case "mod":
			regMap[currInst.register] %= getNumValue(regMap, currInst.op)
		case "rcv":
			if regMap[currInst.register] != 0 {
				fmt.Println("here", lastSnd, currInst.pos)
				rcv = lastSnd
				break
			}
		case "snd":
			lastSnd = regMap[currInst.register]
			// fmt.Println(lastSnd, currInst.pos)
		case "jgz":
			prgJmp := getNumValue(regMap, currInst.op)
			if regMap[currInst.register] != 0 {
				if prgJmp != 0 {
					rem := true
					splits := insts
					jmpCount := currInst.pos + prgJmp
					if jmpCount < currInst.pos {
						rem = false
					}
					if !rem {
						splits = reverseList(insts[jmpCount:currInst.pos])
						for _, v := range splits {
							prgQ.PushFront(v)
						}
					} else {
						i := currInst.pos
						for i != currInst.pos+prgJmp {
							e := prgQ.Front()
							prgQ.Remove(e)
							i++
						}
					}
				}
			} else {
				num, err := strconv.Atoi(currInst.register)
				if err == nil && num > 0 {
					prgQ.PushFront(insts[currInst.pos+prgJmp])
				} else {
					prgQ.Remove(currInstElem)
				}
			}
		}
		if currInst.name != "jgz" {
			prgQ.Remove(currInstElem)
		}
	}

	fmt.Println("part 1:", rcv, lastSnd)
}
