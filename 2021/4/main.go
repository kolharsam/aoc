package main

import (
	"fmt"
	"io/ioutil"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func makeNumbers(numsLine string) []int {
	numis := make([]int, 0)
	nums := strings.Split(numsLine, ",")
	for _, num := range nums {
		numi, err := strconv.Atoi(num)
		check(err)
		numis = append(numis, numi)
	}

	return numis
}

func makeBoard(boardStr string) Board {
	board := make([][]Cell, 0)

	bRows := strings.Split(boardStr, "\n")

	for _, r := range bRows {
		bSplits := strings.Split(r, " ")
		cells := make([]Cell, 0)

		for _, mr := range bSplits {
			if mr != "" {
				num, err := strconv.Atoi(mr)
				check(err)
				cells = append(cells, Cell{Set: false, Number: num})
			}
		}

		board = append(board, cells)
	}

	return board
}

func readFile(fileName string) (Game, []int) {
	f, err := ioutil.ReadFile(fileName)
	check(err)

	lines := strings.Split(string(f), "\n\n")

	nums := make([]int, 0)
	game := make([]Board, 0)

	for i, line := range lines {
		if i == 0 {
			nums = makeNumbers(line)
			continue
		}

		game = append(game, makeBoard(line))
	}

	return game, nums
}

type Cell struct {
	Number int
	Set    bool
}

func (c *Cell) setMatch(currentNumber int) {
	if c.Number == currentNumber {
		c.Set = true
	}
}

type Board = [][]Cell

type Game = []Board

func setMatches(g Game, currentNumber int) {
	for _, board := range g {
		setMatchesOnBoard(board, currentNumber)
	}
}

func setMatchesOnBoard(b Board, currentNumber int) {
	for i, r := range b {
		for j := range r {
			b[i][j].setMatch(currentNumber)
		}
	}
}

func checkWinner(g Game) *Board {
	var winner Board

	for _, board := range g {
		if isBoardWinner(board) {
			winner = board
			break
		}
	}

	return &winner
}

func isBoardWinner(b Board) bool {
	return isRowAWinnerOnBoard(b) || isColAWinnerOnBoard(b)
}

func isRowAWinnerOnBoard(b Board) bool {
	for _, row := range b {
		full := true

		for _, cell := range row {
			full = full && cell.Set
		}
		if full {
			return true
		}
	}

	return false
}

func isColAWinnerOnBoard(b Board) bool {
	i, j := 0, 0

	for i != 5 {
		full := true
		for j != 5 {
			full = full && b[j][i].Set
			j++
		}
		if full {
			return true
		}
		i++
		j = 0
	}
	return false
}

func getSum(b Board) int {
	sum := 0
	for _, row := range b {
		for _, cell := range row {
			if !cell.Set {
				sum += cell.Number
			}
		}
	}

	return sum
}

func playGame(g Game, numbers []int) {
	for _, currentNumber := range numbers {
		setMatches(g, currentNumber)

		winnerBoard := checkWinner(g)

		if len(*winnerBoard) != 0 {
			// Part 1 Answer
			fmt.Println(getSum(*winnerBoard) * currentNumber)
			break
		}
	}
}

func contains(l []int, elem int) bool {
	for _, i := range l {
		if i == elem {
			return true
		}
	}

	return false
}

func findLastWinner(g Game, numbers []int) {
	winBoardsCount, winNumber, winIndex := 0, 0, 0
	winIndexes := make([]int, 0)

	for _, currentNumber := range numbers {
		setMatches(g, currentNumber)

		for i, board := range g {
			if isBoardWinner(board) && !contains(winIndexes, i) {
				winIndex = i
				winBoardsCount++
				winNumber = currentNumber
				winIndexes = append(winIndexes, i)
			}
		}

		if len(g) == winBoardsCount {
			break
		}
	}

	// Part 2 Answer
	fmt.Println(getSum(g[winIndex]) * winNumber)
}

func resetGame(g Game) {
	for _, board := range g {
		for _, row := range board {
			for i := range row {
				row[i].Set = false
			}
		}
	}
}

func main() {
	fileName := os.Args[1]
	game, numbers := readFile(fileName)

	playGame(game, numbers)
	resetGame(game)
	findLastWinner(game, numbers)
}
