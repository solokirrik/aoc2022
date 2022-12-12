package main

import (
	"fmt"
	"sort"
)

var actToPrint = map[int]bool{
	1:     true,
	20:    true,
	1000:  true,
	2000:  true,
	3000:  true,
	4000:  true,
	5000:  true,
	6000:  true,
	7000:  true,
	8000:  true,
	9000:  true,
	10000: true,
}

func printActivity(r int, m []Monkey) {
	if ok := actToPrint[r]; !ok {
		return
	}

	sort.Slice(m, func(i, j int) bool {
		return m[i].ID < m[j].ID
	})

	fmt.Println(fmt.Sprintf("Round %d", r))

	for i := range m {
		fmt.Println(fmt.Sprintf("Monkey %d: %v", m[i].ID, m[i].Activity))
	}

	fmt.Println("\n")
}

func printMonkeyItems(monkeys []Monkey) {
	for m := range monkeys {
		fmt.Println(fmt.Sprintf("Monkey %d: %v", monkeys[m].ID, monkeys[m].Items))
	}
}
