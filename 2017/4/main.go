package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func sortWord(word string) string {
	byteWord := []byte(word)

	sort.Slice(byteWord, func(i int, j int) bool {
		return byteWord[i] < byteWord[j]
	})

	str := ""

	for i := range byteWord {
		str += string(byteWord[i])
	}

	return str
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	count := 0

	for scanner.Scan() {
		currentLine := scanner.Text()
		words := strings.Split(currentLine, " ")
		wordList := map[string]bool{}
		sortedWords := []string{}

		for i := range words {
			sortedWords = append(sortedWords, sortWord(words[i]))
		}

		for i := range sortedWords {
			wordList[sortedWords[i]] = true
		}

		if len(words) == len(wordList) {
			count++
		}
	}

	fmt.Println(count)
}
