package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// operators := [">", "<", "==", "!=", "<=", ">="]
// operations := ["inc", "dec"]

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func isKeyThere(m map[string]int, key string) bool {
	_, ok := m[key]
	return ok
}

func isConditionTrue(operand1 int, operand2 int, operator string) bool {
	switch operator {
	case ">":
		return operand1 > operand2
	case "<":
		return operand1 < operand2
	case "==":
		return operand1 == operand2
	case "!=":
		return operand1 != operand2
	case "<=":
		return operand1 <= operand2
	case ">=":
		return operand1 >= operand2
	}

	return false
}

func getMaxFromMap(m map[string]int) int {
	max := 0

	for k, v := range m {
		if m[k] > max {
			max = v
		}
	}

	return max
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	allVars := make(map[string]int)

	maxOverall := 0

	for scanner.Scan() {
		currentLine := strings.Split(scanner.Text(), " ")

		register := currentLine[0]                      // register to perform the operation on
		operation := currentLine[1]                     // inc or dec
		operationArg, e := strconv.Atoi(currentLine[2]) // inc/dec by number
		isError(e)
		currentOperator := currentLine[5]            // >=, != ...
		operand1 := currentLine[4]                   // reg to check
		operand2, e2 := strconv.Atoi(currentLine[6]) // number / reg to check
		isError(e2)

		if !isKeyThere(allVars, register) {
			allVars[register] = 0
		}

		if !isKeyThere(allVars, operand1) {
			allVars[operand1] = 0
		}

		if isConditionTrue(allVars[operand1], operand2, currentOperator) {
			if operation == "inc" {
				allVars[register] += operationArg
			} else if operation == "dec" {
				allVars[register] -= operationArg
			}
		}

		mx := getMaxFromMap(allVars)

		if mx > maxOverall {
			maxOverall = mx
		}
	}

	maxValue := getMaxFromMap(allVars)

	fmt.Println(maxValue, maxOverall)
}
