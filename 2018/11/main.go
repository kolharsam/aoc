package main

import "fmt"

const (
	// puzzleInput int = 7511
	puzzleInput int = 18 // Sample
)

type FuelCell struct {
	x          int
	y          int
	id         int
	powerLevel int
}

type FuelCellGrid []FuelCell

func getPowerLevel(y, id int) int {
	p1 := (((id * y) + puzzleInput) * id)
	p2 := (p1 / 100) % 10
	return p2 - 5
}

func (fc FuelCell) getGrid(grid FuelCellGrid, num int) (FuelCellGrid, bool) {
	fcg := make([]FuelCell, 0)

	if num == 1 {
		return []FuelCell{fc}, true
	}

	// NOTE: here fc, is assumed to be the top-left fuel cell in the grid
	for i := fc.x; i < fc.x+num; i++ {
		for j := fc.y; j < fc.y+num; j++ {
			if i >= 1 && i < 300 && j >= 1 && j < 300 {
				fcg = append(fcg, grid.getCell(i, j))
			} else {
				return fcg, false
			}
		}
	}

	return fcg, true
}

func (fcg FuelCellGrid) getCell(i, j int) FuelCell {
	f := FuelCell{}

	for _, fc := range fcg {
		if fc.x == i && fc.y == j {
			f = fc
			break
		}
	}

	return f
}

func (fcg FuelCellGrid) calcGridPowerLevel() int {
	level := 0

	for _, fc := range fcg {
		level += fc.powerLevel
	}

	return level
}

func (fcg FuelCellGrid) calcHighestPowerCell() {
	currentGrid, ok := fcg[0].getGrid(fcg, 3)
	if !ok {
		panic("Some issue here")
	}

	highest := currentGrid.calcGridPowerLevel()
	cornerFC := fcg[0]

	for _, fc := range fcg {
		cg, ok := fc.getGrid(fcg, 3)
		if !ok {
			continue
		}
		score := cg.calcGridPowerLevel()
		if score > highest {
			highest = score
			cornerFC = fc
		}
	}

	fmt.Println(highest, cornerFC.x, cornerFC.y)
}

func initGrid() FuelCellGrid {
	fcg := make(FuelCellGrid, 0)

	for i := 1; i <= 300; i++ {
		for j := 1; j <= 300; j++ {
			var newFuelCell FuelCell

			id := i + 10
			newFuelCell.x = i
			newFuelCell.y = j
			newFuelCell.id = id
			newFuelCell.powerLevel = getPowerLevel(j, id)

			fcg = append(fcg, newFuelCell)
		}
	}

	return fcg
}

func (fcg FuelCellGrid) calcHighestPowerCellInfinite() {
	currentGrid, ok := fcg[0].getGrid(fcg, 1)
	if !ok {
		panic("Some issue here")
	}

	highest := currentGrid.calcGridPowerLevel()
	cornerFC := fcg[0]
	size := 0

	for _, fc := range fcg {
		for i := 1; i <= 300; i++ {
			cg, ok := fc.getGrid(fcg, i)
			if !ok {
				continue
			}
			// FIXME: can be done in a much faster manner using goroutines
			score := cg.calcGridPowerLevel()
			if score > highest {
				highest = score
				cornerFC = fc
				size = i
			}
		}
	}

	fmt.Println(highest, cornerFC.x, cornerFC.y, size)
}

func main() {
	fcg := initGrid()
	// Part 1
	fcg.calcHighestPowerCell()
	// Part 2
	fcg.calcHighestPowerCellInfinite()
}
