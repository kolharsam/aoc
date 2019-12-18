// The base pattern is 0, 1, 0, -1.

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func getNumber(s string) int {
	num, err := strconv.Atoi(s)
	isError(err)
	return num
}

func toStr(i int) string {
	num := strconv.Itoa(i)
	return num
}

func getBases(base []int, times int) [][]int {
	res := [][]int{}
	i, j, k := 0, 0, 0

	for i < times {
		list := []int{}
		for j < len(base) {
			curr := base[j]
			for k < i+1 {
				list = append(list, curr)
				k++
			}
			j++
			k = 0
		}
		res = append(res, list)
		j = 0
		i++
	}

	return res
}

func printFirstN(o []int, n int) {
	for i, v := range o {
		fmt.Printf("%d", v)
		if i >= n-1 {
			fmt.Println()
			break
		}
	}
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)
	inputPhase := []int{}
	basePattern := []int{0, 1, 0, -1}
	inputOffset := ""

	for scanner.Scan() {
		temp := strings.Split(scanner.Text(), "")
		for i := range temp {
			inputPhase = append(inputPhase, getNumber(temp[i]))
			if i < 7 {
				inputOffset += temp[i]
			}
		}
	}

	inputPhaseLen := len(inputPhase)
	inputPhaseCopy := append([]int(nil), inputPhase...)
	basePatterns := getBases(basePattern, inputPhaseLen)
	inOffsetNumber := getNumber(inputOffset)

	do := 0
	limit := 100

	for do < limit {
		i, j := 0, 0
		p := []int{}

		for i < inputPhaseLen {
			currentBase := basePatterns[i]
			point := 1
			res := 0
			for j < inputPhaseLen {
				prod := inputPhase[j] * currentBase[point%len(currentBase)]
				res += prod
				point++
				j++
			}
			strNum := toStr(res)
			num := getNumber(strNum[len(strNum)-1:])
			p = append(p, num)
			j = 0
			i++
		}

		inputPhase = p
		i = 0
		do++
	}

	printFirstN(inputPhase, 8) // part 1    ---- Mutations are being performed on the input itself. Which is bad!

	// part 2
	newInputPhase := []int{}
	counter := 0

	for counter < 10000 {
		newInputPhase = append(newInputPhase, inputPhaseCopy...)
		counter++
	}

	newInputPhaseLen := len(newInputPhase)
	basePatterns = getBases(basePattern, newInputPhaseLen)

	fmt.Println(newInputPhaseLen)

	do = 0
	limit = 100

	for do < limit {
		i, j := 0, 0
		p := []int{}

		for i < newInputPhaseLen {
			currentBase := basePatterns[i]
			point := 1
			res := 0
			for j < newInputPhaseLen {
				prod := newInputPhase[j] * currentBase[point%len(currentBase)]
				res += prod
				point++
				j++
			}
			strNum := toStr(res)
			num := getNumber(strNum[len(strNum)-1:])
			p = append(p, num)
			j = 0
			i++
		}

		newInputPhase = p
		i = 0
		do++
		fmt.Println("done : ", do)
	}

	fmt.Println(newInputPhase[inOffsetNumber : inOffsetNumber+8]) // part 2

}
