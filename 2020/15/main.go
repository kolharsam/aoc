package main

func main() {
	pInput := []int{14, 1, 17, 0, 3, 20}
	countMap := map[int][]int{}
	for i, v := range pInput {
		countMap[v] = []int{i + 1}
	}
	iter := len(pInput) + 1
	last := pInput[len(pInput)-1]
	for iter <= 30000000 {
		// because the counting started from 1
		if iter == 2021 {
			println("part 1: ", last)
		}
		if v, ok := countMap[last]; ok {
			if len(v) == 1 {
				// most recently spoken and new
				a := countMap[0]
				a = append(a, iter)
				countMap[0] = a
				last = 0
			} else {
				// number was spoken previously
				a := countMap[last]
				lenA := len(a)
				l1 := a[lenA-1]
				l2 := a[lenA-2]
				newNum := l1 - l2
				last = newNum
				if _, ok := countMap[newNum]; ok {
					b := countMap[newNum]
					b = append(b, iter)
					countMap[newNum] = b
				} else {
					countMap[newNum] = []int{iter}
				}
			}
			iter++
		} else {
			panic("This shouldn't be the case!")
		}
	}
	println("part 2:", last)
}
