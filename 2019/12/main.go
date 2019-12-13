package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"reflect"
	"strconv"
	"strings"
)

type pair struct {
	a, b int
}

type moonlocation struct {
	x, y, z int
}

type moonvelocity struct {
	x, y, z int
}

type universestate struct {
	mp []moonlocation
	mv []moonvelocity
}

func isError(e error) {
	if e != nil {
		panic(e)
	}
}

func convertToInt(s string) int {
	num, err := strconv.Atoi(s)
	isError(err)
	return num
}

func getCombinations() []pair {
	l := []int{0, 1, 2, 3}
	j := 1

	allPairs := []pair{}

	for i := range l {
		li := []pair{}
		for j < len(l) {
			li = append(li, pair{a: i, b: j})
			j++
		}
		allPairs = append(allPairs, li...)
		i++
		j = i + 1
	}

	return allPairs
}

func compareX(m1 moonlocation, m2 moonlocation) (int, int) {
	if m1.x > m2.x {
		return -1, 1
	} else if m1.x < m2.x {
		return 1, -1
	} else {
		return 0, 0
	}
}

func compareY(m1 moonlocation, m2 moonlocation) (int, int) {
	if m1.y > m2.y {
		return -1, 1
	} else if m1.y < m2.y {
		return 1, -1
	} else {
		return 0, 0
	}
}

func compareZ(m1 moonlocation, m2 moonlocation) (int, int) {
	if m1.z > m2.z {
		return -1, 1
	} else if m1.z < m2.z {
		return 1, -1
	} else {
		return 0, 0
	}
}

func getAbsInt(i int) int {
	fI := float64(i)
	absI := math.Abs(fI)
	return int(absI)
}

func getEnergy(mp []moonlocation, mv []moonvelocity) int {
	pe, ke, tot := 0, 0, 0
	i := 0

	for i < len(mp) {
		pe += getAbsInt(mp[i].x) + getAbsInt(mp[i].y) + getAbsInt(mp[i].z)
		ke += getAbsInt(mv[i].x) + getAbsInt(mv[i].y) + getAbsInt(mv[i].z)
		tot += (pe * ke)
		pe, ke = 0, 0
		i++
	}

	return tot
}

func checkArr(m []universestate, state universestate) bool {
	flag := false

	for _, st := range m {
		if reflect.DeepEqual(st, state) {
			flag = true
			break
		}
	}

	return flag
}

func main() {
	file, err := os.Open("input")
	isError(err)
	defer file.Close()

	scanner := bufio.NewScanner(file)

	moonPositions := []moonlocation{}
	moonVelocities := []moonvelocity{}

	for scanner.Scan() {
		currentLine := scanner.Text()
		strSplit := strings.Split(currentLine, "=")
		xSplit := strings.Split(strSplit[1], ",")
		ySplit := strings.Split(strSplit[2], ",")
		zSplit := strings.Split(strSplit[3], ">")

		x := convertToInt(xSplit[0])
		y := convertToInt(ySplit[0])
		z := convertToInt(zSplit[0])

		temp := moonlocation{x, y, z}
		moonPositions = append(moonPositions, temp)
		moonVelocities = append(moonVelocities, moonvelocity{x: 0, y: 0, z: 0})
	}

	tmpMP := make([]moonlocation, len(moonPositions))
	tmpMV := make([]moonvelocity, len(moonVelocities))

	copy(tmpMP, moonPositions)
	copy(tmpMV, moonVelocities)

	stateMap := []universestate{}
	stateMap = append(stateMap, universestate{mp: tmpMP, mv: tmpMV})

	combinations := getCombinations()
	var c int64
	c = 1000000000000000

	for c > 1000000 {
		for _, pair := range combinations {
			i1 := pair.a
			i2 := pair.b

			res1x, res2x := compareX(moonPositions[i1], moonPositions[i2])
			res1y, res2y := compareY(moonPositions[i1], moonPositions[i2])
			res1z, res2z := compareZ(moonPositions[i1], moonPositions[i2])

			moonVelocities[i1].x += res1x
			moonVelocities[i2].x += res2x
			moonVelocities[i1].y += res1y
			moonVelocities[i2].y += res2y
			moonVelocities[i1].z += res1z
			moonVelocities[i2].z += res2z
		}

		for i, tuple := range moonVelocities {
			moonPositions[i].x += tuple.x
			moonPositions[i].y += tuple.y
			moonPositions[i].z += tuple.z
		}

		MPS := make([]moonlocation, len(moonPositions))
		MVS := make([]moonvelocity, len(moonVelocities))

		copy(MPS, moonPositions)
		copy(MVS, moonVelocities)

		currentState := universestate{mp: MPS, mv: MVS}

		if checkArr(stateMap, currentState) {
			break
		} else {
			stateMap = append(stateMap, currentState)
			fmt.Println(c)
			c--
			continue
		}
	}

	/*
		A more innovative approach for Part - 2 will be the fact that we
		recognise that the 3 axis are functioning independent of each other
		Moreover, since the process is reversible, the cycles will start at
		time 0, and the overall cycle length is simply the
		lowest common multiple of all of them.
	*/

	// energy := getEnergy(moonPositions, moonVelocities)
	// fmt.Println(energy) // part 1
	fmt.Println(len(stateMap)) // part 2
}
