package main

import (
	"fmt"
	"io/ioutil"
	"strings"
)

const inputFile = "sample"

// const inputFile = "input"

func readLinesFromFile(filename string) []string {
	readlines, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Printf("failed to read from file: %s", filename)
	}
	return strings.Split(string(readlines), "\n")
}

func makeRule(ruleStr string) []string {
	return strings.Split(ruleStr, "/")
}

type Rule struct {
	match  []string
	result []string
}

func checkMatch(pat []string, mat []string) bool {
	eq := false
	for i, m := range mat {
		if m == pat[i] {
			eq = true
			continue
		}
		return false
	}
	return eq
}

func getResult(currentPattern []string, rules []Rule) []string {
	for _, m := range rules {
		if checkMatch(currentPattern, m.match) {
			return m.result
		}
	}
	// should be unlikely to get here
	return nil
}

func rotateMatch(m []string) []string {
	mCopy := make([]string, 0)
	copy(mCopy, m)

	return mCopy
}

func reverseStr(str string) (result string) {
	for _, v := range str {
		result = string(v) + result
	}
	return
}

func flipVertical(m []string) []string {
	mNew := make([]string, 0)

	for _, r := range m {
		mNew = append(mNew, reverseStr(r))
	}

	return mNew
}

func flipHorizontal(m []string) []string {
	mNew := make([]string, 0)

	return mNew
}

func makeRules(ruleLines []string) []Rule {
	sep := " => "
	ruleArr := make([]Rule, 0)
	for _, rule := range ruleLines {
		ruleSplt := strings.Split(rule, sep)
		lRule := makeRule(ruleSplt[0])
		rRule := makeRule(ruleSplt[1])
		ruleArr = append(ruleArr, Rule{match: lRule, result: rRule})
		// TODO: rotate and flip and add them as new rules
	}

	return ruleArr
}

type Pattern struct {
	grid []string
}

func newPattern() Pattern {
	newGrid := make([]string, 0)
	newGrid = append(newGrid, ".#.")
	newGrid = append(newGrid, "..#")
	newGrid = append(newGrid, "###")
	return Pattern{grid: newGrid}
}

func (p Pattern) size() int {
	return len(p.grid[0])
}

func getCountOnForRow(rowStr string) int {
	return strings.Count(rowStr, "#")
}

func (p Pattern) countOn() int {
	count := 0
	for _, row := range p.grid {
		count += getCountOnForRow(row)
	}
	return count
}

func (p *Pattern) splitGrid(n int) {
	if n != 2 && n != 3 {
		panic("the grid can only be split by 2 or 3")
	}

	if !(n == 3 && p.size() == 3) {

	}
}

func main() {
	ruleLines := readLinesFromFile(inputFile)
	rules := makeRules(ruleLines)
	pat := newPattern()
	fmt.Println(pat, rules, pat.countOn(), pat.size())
}
