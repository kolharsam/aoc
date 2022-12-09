package main

import (
	"fmt"
	"os"
	"strings"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func readFileToLines(fileName string) []string {
	data, err := os.ReadFile(fileName)
	check(err)
	return strings.Split(string(data), "\n")
}

func main() {
	argsWithoutProg := os.Args[1:]
	fileName := "10.in"
	if len(argsWithoutProg) > 0 {
		fileName = argsWithoutProg[0]
	}

	fmt.Println(readFileToLines(fileName))
}
