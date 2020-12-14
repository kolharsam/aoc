package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func exchange(l1, l2 int, word string) string {
	tempStr := []rune(word)
	tempStr[l1] = rune(word[l2])
	tempStr[l2] = rune(word[l1])
	return string(tempStr)
}

func swap(l1, l2, word string) string {
	// this works because each letter is unique
	var pos1, pos2 int
	for i, c := range word {
		if string(c) == l1 {
			pos1 = int(i)
			continue
		}
		if string(c) == l2 {
			pos2 = int(i)
			continue
		}
	}
	return exchange(pos1, pos2, word)
}

func turn(wrune []rune, s int) []rune {
	wruneLen := len(wrune)
	for i := 0; i < s; i++ {
		wrune = append(wrune[wruneLen-1:wruneLen], wrune[:wruneLen-1]...)
	}
	return wrune
}

func spin(word string, s int) string {
	strLen := len(word)
	wrune := []rune(word)
	num := s % strLen
	if num == 0 {
		return word
	}
	return string(turn(wrune, num))
}

func run(word string, instructions []string) string {
	spinChar := "s"
	exchangeChar := "x"
	partnerChar := "p"
	for _, inst := range instructions {
		dance := string(inst[0])
		todo := string(inst[1:])
		switch dance {
		case spinChar:
			num, err := strconv.Atoi(todo)
			if err != nil {
				fmt.Println("Failed to get the required number")
			}
			word = spin(word, num)
			break
		case exchangeChar:
			pairs := strings.Split(todo, "/")
			num1, err := strconv.Atoi(pairs[0])
			if err != nil {
				fmt.Println("Failed to get the required number")
			}
			num2, err := strconv.Atoi(pairs[1])
			if err != nil {
				fmt.Println("Failed to get the required number")
			}
			word = exchange(num1, num2, word)
			break
		case partnerChar:
			pairs := strings.Split(todo, "/")
			word = swap(pairs[0], pairs[1], word)
			break
		}
	}
	return word
}

func main() {
	mainStr := "abcdefghijklmnop"
	m2 := mainStr

	readFile, err := ioutil.ReadFile("16.in")
	if err != nil {
		fmt.Println("Failed to read file")
	}
	line := string(readFile)
	lines := strings.Split(line, ",")

	mainStr = run(mainStr, lines)

	// part 1
	fmt.Println(mainStr)

	// part 2 - perform a billion dances!
	// to be slightly better on performance, we can cache the words, if they're already there,
	// then we could return those itself
	part2Inp := m2
	lim := 1000000000
	cache := map[string]string{}
	cache[part2Inp] = mainStr
	iters := 0
	for iters != lim {
		if val, ok := cache[part2Inp]; ok {
			part2Inp = val
			iters++
			continue
		}
		p2 := run(part2Inp, lines)
		cache[part2Inp] = p2
		part2Inp = p2
		iters++
	}
	fmt.Println(part2Inp)
}
