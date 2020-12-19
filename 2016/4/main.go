package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

type word struct {
	words    []string
	checksum []string
	id       int
}

func runeToStrList(p []rune) []string {
	acc := make([]string, 0, len(p))
	for _, v := range p {
		acc = append(acc, string(v))
	}
	return acc
}

func parseInput(filename string) []word {
	buf, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("failed to read the file %s\n", filename)
	}
	lines := strings.Split(string(buf), "\n")
	wordsList := make([]word, 0, len(lines))

	for _, w := range lines {
		splits := strings.Split(w, "-")
		splLen := len(splits)
		sidchk := splits[splLen-1]
		spl2 := strings.Split(sidchk, "[")
		chkstr := spl2[0]
		chknum, err := strconv.Atoi(chkstr)
		if err != nil {
			fmt.Printf("failed to convert the number %s: %s", chkstr, err.Error())
		}
		ch := strings.Split(spl2[1], "]")
		chsum := runeToStrList([]rune(ch[0]))

		wordsList = append(wordsList, word{
			words:    splits[:splLen-1],
			id:       chknum,
			checksum: chsum,
		})
	}

	return wordsList
}

type srt struct {
	letter string
	count  int
}

// return the five most `popular` characters
func getSortedList(freqMap map[string]int) []string {
	freqList := make([]srt, 0, 26)
	for k, v := range freqMap {
		freqList = append(freqList, srt{letter: k, count: v})
	}

	// sort against value and char
	for i := 0; i < len(freqList); i++ {
		for j := 0; j < len(freqList); j++ {
			if i == j {
				continue
			}
			if freqList[i].count > freqList[j].count {
				t := freqList[i]
				freqList[i] = freqList[j]
				freqList[j] = t
				continue
			}
			if freqList[i].count == freqList[j].count {
				cmp := strings.Compare(freqList[i].letter, freqList[j].letter)
				if cmp == -1 {
					t := freqList[i]
					freqList[i] = freqList[j]
					freqList[j] = t
					continue
				}
			}
		}
	}

	l := make([]string, 0, 5)
	for _, v := range freqList[:5] {
		l = append(l, v.letter)
	}

	return l
}

func isValidRoom(room word) bool {
	freq := make(map[string]int)
	for _, v := range room.words {
		for _, w := range v {
			freq[string(w)]++
		}
	}

	freqSet := getSortedList(freq)
	for i, v := range freqSet {
		if v != room.checksum[i] {
			return false
		}
	}

	return true
}

func shift(char string, by int) string {
	alphabets := "abcdefghijklmnopqrstuvwxyz"
	pos := 0
	for i, c := range alphabets {
		if string(c) == char {
			pos = i
			break
		}
	}

	return string(alphabets[(pos+by)%26])
}

func shiftCipher(w word) string {
	n := ""
	for _, v := range w.words {
		p := ""
		for _, s := range v {
			p += shift(string(s), w.id)
		}
		n += p + " "
	}

	return n
}

func main() {
	parsedInput := parseInput("4.in")
	// part 1
	sum := 0
	for _, v := range parsedInput {
		if isValidRoom(v) {
			sum += v.id
		}
	}
	fmt.Println("Part 1: ", sum)
	// part 2
	for _, v := range parsedInput {
		s := shiftCipher(v)
		if strings.Contains(s, "northpole") {
			fmt.Println("Part 2: ", v.id)
			break
		}
	}
}
