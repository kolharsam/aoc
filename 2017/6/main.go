package main

import (
	"bufio"
	"fmt"
	"os"
	"reflect"
	"strconv"
	"strings"
)

type stateVar struct {
	stateArr []int
}

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func wasDone(state [][]int, current []int) bool {
	flag := false

	for i := range state {
		if reflect.DeepEqual(state[i], current) {
			flag = true
			break
		}
	}

	return flag
}

func getMax(arr []int) (int, int) {
	max := arr[0]
	index := 0

	for i, num := range arr {
		if num > max {
			max = num
			index = i
		}
	}

	return max, index
}

func redistribute(arr []int, amount int, index int) []int {
	temp := arr
	n := 0

	pointer := index + 1

	temp[index] = 0

	size := len(arr)

	for n < amount {
		temp[pointer%size]++
		pointer++
		n++
	}

	return temp
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	state := []int{}

	init := []string{}

	for scanner.Scan() {
		init = strings.Split(scanner.Text(), "\t")
	}

	allStates := []stateVar{}

	for i := range init {
		number, err := strconv.Atoi(init[i])
		isError(err)
		state = append(state, number)
	}

	count := 0

	for { // THIS PROCESS CAN BE EASILY CONVERTED TO A RECURSIVE PROCESS
		currentLargest, position := getMax(state)

		count++

		fmt.Println(state)

		allStates = append(allStates, stateVar{stateArr: redistribute(state, currentLargest, position)})

		fmt.Println("State : ", allStates)

		if count > 5 {
			break
		}

		// if wasDone(allStates, temp) {
		// 	break
		// } else {q
		// 	allStates = append(allStates, temp)
		// 	state = temp
		// 	fmt.Println(state, allStates)
		// }
	}

	fmt.Println(count-1, allStates)
}
