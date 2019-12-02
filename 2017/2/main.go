package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func convertToInt(number string) int {
	numberInt, err := strconv.Atoi(number)
	isError(err)
	return numberInt
}

func convertArrayToInt(array []string) []int {
	result := []int{}

	for i := range array {
		result = append(result, convertToInt(array[i]))
	}

	return result
}

func minmax(array []string) (int, int) {
	numberArray := convertArrayToInt(array)
	size := len(numberArray)
	sort.Ints(numberArray)

	return numberArray[0], numberArray[size-1]
}

func getNumbers(array []string) (int, int) {
	numberArray := convertArrayToInt(array)
	sort.Ints(numberArray)

	var num1 int = 0
	var num2 int = 0
	var flag bool = false

	for i := range numberArray {
		for j := range numberArray {
			if j != i {
				if numberArray[j]%numberArray[i] == 0 {
					num1 = numberArray[i]
					num2 = numberArray[j]
					flag = true
					break
				}
			}
		}
		if flag {
			break
		}
	}

	return num1, num2
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var checksum int = 0
	// var min int = 0
	// var max int = 0
	var num1 int = 0
	var num2 int = 0

	for scanner.Scan() {
		currentText := scanner.Text()
		currentLine := strings.Split(currentText, "\t")

		// min, max = minmax(currentLine)
		num1, num2 = getNumbers(currentLine)

		// checksum += (max - min)
		checksum += (num2 / num1)
	}

	isError(scanner.Err())

	fmt.Println(checksum)
}
