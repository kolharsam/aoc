package main

import (
	"fmt"
	"strings"
)

var probInput string = "cqjxjnds"
var sampleInput string = "ghijklmn"
var sample2Input string = "abcdefgh"
var part1answer string = "cqjxxyzz"

func includesStraight(password string) bool {
	r := []rune(password)

	for i := 0; i < len(password); i++ {
		for j := 1; j < len(password); j++ {
			for k := 1; k < len(password); k++ {
				if (int(r[k])-int(r[j]) == 1) && (int(r[j])-int(r[i]) == 1) && (int(r[k])-int(r[i]) == 2) && (k-j == 1) && (j-i == 1) && (k-i == 2) {
					return true
				}
			}
		}
	}

	return false
}

func noIncludeInvalid(password string) bool {
	return !strings.ContainsAny(password, "ilo")
}

func containsPairs(password string) bool {
	count := 0
	r := []rune(password)
	seenMap := make(map[string]bool)
	for i := 0; i < len(password)-1; i++ {
		if r[i] == r[i+1] {
			if _, ok := seenMap[string(r[i])]; ok {
				continue
			} else {
				count++
				seenMap[string(r[i])] = true
			}
		}
	}

	return count >= 2
}

func isValidPassword(password string) bool {
	return includesStraight(password) && noIncludeInvalid(password) && containsPairs(password)
}

func reverse(xt []rune) []rune {
	n := len(xt)
	x := make([]rune, n)
	copy(x, xt)
	for i := 0; i+i < n; i++ {
		x[i], x[n-1-i] = x[n-1-i], x[i]
	}
	return x
}

func getNextWord(r []rune, c int) ([]rune, int) {
	new_r := make([]rune, len(r))
	copy(new_r, r)

	for i := 0; i < len(r); i++ {
		if string(new_r[i]) != "z" {
			new_r[i] = rune(int(new_r[i]) + 1)
			return new_r, c + 1
		}
		new_r[i] = []rune("a")[0]
	}

	return new_r, c + 1
}

func main() {
	starter := part1answer
	runeStarter := []rune(starter)
	runeStarter = reverse(runeStarter)
	newPassword := ""
	count := 0

	for {
		runeStarter, count = getNextWord(runeStarter, count)
		r := reverse(runeStarter)
		if isValidPassword(string(r)) {
			newPassword = string(r)
			break
		}
	}

	fmt.Println(newPassword, count)
}
