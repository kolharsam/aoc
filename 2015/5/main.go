package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func vowelCond(s string) bool {
	flag := false
	vowelCount := 0

	for _, v := range s {
		if v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u' {
			vowelCount++
		}
	}

	if vowelCount >= 3 {
		flag = true
	}

	return flag
}

func doubleLetter(s string) bool {
	flag := false
	i := 0

	for i < len(s)-1 {
		if s[i] == s[i+1] {
			flag = true
			break
		}
		i++
	}

	return flag
}

func restrict(s string) bool {
	flag := true

	if strings.Contains(s, "ab") || strings.Contains(s, "cd") || strings.Contains(s, "pq") || strings.Contains(s, "xy") {
		flag = false
	}

	return flag
}

func isStringNice(s string) bool {
	flag := false

	if vowelCond(s) && doubleLetter(s) && restrict(s) {
		flag = true
	}

	return flag
}

func rule1(s string) bool { // check this functions again once
	flag := false
	i := 0

	for i < len(s)-1 {
		a := s[i]
		b := s[i+1]
		j := 0

		for j < len(s)-1 {
			if j == i {
				j += 2
				continue
			}

			if s[j] == a && s[j+1] == b {
				flag = true
				break
			}

			j += 2
		}
		if flag {
			break
		}
		i++
	}

	return flag
}

func rule2(s string) bool {
	flag := false
	i := 0

	for i < len(s)-2 {
		if s[i] == s[i+2] {
			flag = true
		}
		i++
	}

	return flag
}

func isStringNoice(s string) bool {
	flag := false

	if rule1(s) && rule2(s) {
		flag = true
	}

	return flag
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	count1 := 0
	count2 := 0

	for scanner.Scan() {
		cw := scanner.Text()

		if isStringNice(cw) {
			count1++ // for part 1 alone
		}

		if isStringNoice(cw) {
			count2++ // for part 2 alone
		}
	}

	fmt.Println(count1) // part 1
	fmt.Println(count2) // part 2
}
