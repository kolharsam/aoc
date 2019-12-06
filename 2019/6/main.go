package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var planetMap map[string][]string = make(map[string][]string)

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func counter(key string) int {
	count := 0

	for _, child := range planetMap[key] {
		count += counter(child) // for the indirect relation with it's children
		count++                 // for the direct relation
	}

	return count
}

// Count function to count the relations between the planets
func Count() int {
	count := 0

	for k := range planetMap {
		count += counter(k)
	}

	return count
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		current := strings.Split(scanner.Text(), ")")
		ob1 := current[0]
		ob2 := current[1]
		planetMap[ob1] = append(planetMap[ob1], ob2)
	}

	count := Count()
	fmt.Println(count) // # part 1
}
