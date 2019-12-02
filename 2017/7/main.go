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

func find(slice []string, element string) bool {
	flag := false

	for _, elem := range slice {
		if elem == element {
			flag = true
			break
		}
	}

	return flag
}

func main() {
	file, err := os.Open("input2")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	nodes := []string{}
	keyMap := make(map[string]bool)
	processes := []string{}
	weights := []int{}
	allProcesses := []string{}
	allKeysMap := make(map[string]int)

	for scanner.Scan() {
		currentLine := scanner.Text()
		splitter := " -> "

		if strings.Contains(currentLine, splitter) {
			split := strings.Split(currentLine, splitter)

			keySplit := strings.Split(split[0], "(")
			key := keySplit[0]
			weight := strings.Split(keySplit[1], ")")[0]
			values := strings.Split(split[1], ",")

			key = strings.TrimSpace(key)
			weight = strings.TrimSpace(weight)
			weightInt, err := strconv.Atoi(weight)
			isError(err)

			for i := range values {
				values[i] = strings.TrimSpace(values[i])
			}

			nodes = append(nodes, values...)
			keyMap[key] = true
			processes = append(processes, key)
			weights = append(weights, weightInt)
			allProcesses = append(allProcesses, key)
			allKeysMap[key] = weightInt
		} else {
			keyWeightSplit := strings.Split(currentLine, "(")
			key := strings.TrimSpace(keyWeightSplit[0])
			weight, err := strconv.Atoi(strings.Split(keyWeightSplit[1], ")")[0])
			isError(err)

			allProcesses = append(allProcesses, key)
			allKeysMap[key] = weight
		}
	}

	rootNode := ""

	for _, process := range processes {
		if find(nodes, process) {
			delete(keyMap, process)
		} else {
			rootNode = process
		}
	}

	fmt.Println(keyMap, rootNode)
	fmt.Print("\n\n")
	fmt.Println(allKeysMap)
	fmt.Print("\n\n")
	fmt.Println(allProcesses)
}
