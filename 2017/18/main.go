package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func parseInput(filename string) []string {
	readlines, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Print("could not open the file")
	}
	lines := strings.Split(string(readlines), "\n")
	return lines
}

func main() {
	commands := parseInput("18.in")
	regMap := make(map[string]int)
	sound := 0
	addr := 0

	for addr < len(commands) {
		command := commands[addr]
		spl := strings.Split(command, " ")
		cmd := spl[0]
		reg := ""
		val := ""
		numVal := -1
		if len(spl) == 3 {
			reg = spl[1]
			val = spl[2]
		} else {
			if cmd == "snd" {
				val = spl[1]
			} else {
				reg = spl[1]
			}
		}
		num, err := strconv.Atoi(val)
		if err != nil {
			numVal = regMap[val]
		} else {
			numVal = num
		}

		// fmt.Println(regMap, reg, addr, numVal, cmd)
		found := false

		switch cmd {
		case "set":
			regMap[reg] = numVal
		case "add":
			regMap[reg] += numVal
		case "mul":
			regMap[reg] *= numVal
		case "mod":
			regMap[reg] %= numVal
		case "snd":
			sound = numVal
		case "rcv":
			if regMap[reg] != 0 {
				regMap[reg] = sound
				found = true
			}
		case "jgz":
			if regMap[reg] != 0 {
				addr += numVal - 1
			}
		}
		if found {
			break
		}
		addr += 1
	}
	// Part 1
	fmt.Println(sound)

	// for part 2
}
