package main

import (
	_ "embed"
	"fmt"
	"sort"
	"strconv"
	"strings"
)

//go:embed day11
var inp string

func main() {
	part1(inp)
	part2(inp)
}

func part1(in string) {
	monkeys := buildMonkeys(in)

	const part = 1
	const rounds = 20
	const calmDiv = int64(3)

	for i := 0; i < rounds; i++ {
		for m := 0; m < len(monkeys); m++ {
			if len(monkeys[m].Items) < 1 {
				continue
			}

			for len(monkeys[m].Items) > 0 {
				monkeys[m].DoInspection(part, calmDiv)
				monkeys[m].Activity++

				item := monkeys[m].Items[0]
				throwItemMonkeyID := monkeys[m].ChoseToThrow()

				monkeys[m].Items = monkeys[m].Items[1:]
				monkeys[throwItemMonkeyID].Items = append(monkeys[throwItemMonkeyID].Items, item)
			}
		}

		printActivity(i+1, monkeys)
		//printMonkeyItems(monkeys)
	}

	sort.Slice(monkeys, func(i, j int) bool {
		return monkeys[i].Activity > monkeys[j].Activity
	})

	fmt.Println(monkeys[0].Activity * monkeys[1].Activity)
}

func part2(in string) {
	monkeys := buildMonkeys(in)

	const part = 2
	const rounds = 10_000

	var calmDiv = int64(1)

	for i := range monkeys {
		calmDiv *= monkeys[i].TestDivBy
	}

	for i := 0; i < rounds; i++ {
		for m := 0; m < len(monkeys); m++ {
			if len(monkeys[m].Items) < 1 {
				continue
			}

			for len(monkeys[m].Items) > 0 {
				monkeys[m].DoInspection(part, calmDiv)
				monkeys[m].Activity++

				item := monkeys[m].Items[0]
				throwItemMonkeyID := monkeys[m].ChoseToThrow()

				monkeys[m].Items = monkeys[m].Items[1:]
				monkeys[throwItemMonkeyID].Items = append(monkeys[throwItemMonkeyID].Items, item)
			}
		}

		printActivity(i+1, monkeys)
		//printMonkeyItems(monkeys)
	}

	sort.Slice(monkeys, func(i, j int) bool {
		return monkeys[i].Activity > monkeys[j].Activity
	})

	fmt.Println(monkeys[0].Activity * monkeys[1].Activity)
}

func buildMonkeys(in string) []Monkey {
	m := -1
	rows := strings.Split(in, "\n")
	monkeys := []Monkey{}

	for i := range rows {
		rows[i] = strings.TrimRight(rows[i], "\n")

		if strings.HasPrefix(rows[i], "Monkey ") {
			m++
			monkeys = append(monkeys, Monkey{})

			mID := strings.TrimRight(strings.TrimLeft(rows[i], "Monkey "), ":")
			monkeys[m].ID, _ = strconv.ParseInt(mID, 10, 64)
			continue
		}

		if strings.HasPrefix(rows[i], "  Starting items: ") {
			monkeys[m].Items = getItems(strings.TrimLeft(rows[i], "  Starting items: "))
			continue
		}

		if strings.HasPrefix(rows[i], "  Operation: ") {
			monkeys[m].Op = getOperationEx(strings.TrimLeft(rows[i], "  Operation: new = "))
			continue
		}

		if strings.HasPrefix(rows[i], "  Test: divisible by ") {
			divBy := strings.TrimLeft(rows[i], "  Test: divisible by ")
			monkeys[m].TestDivBy, _ = strconv.ParseInt(divBy, 10, 64)
			continue
		}

		if strings.HasPrefix(rows[i], "    If true: throw to monkey ") {
			trueID := strings.TrimLeft(rows[i], "    If true: throw to monkey ")
			monkeys[m].TestTrueID, _ = strconv.ParseInt(trueID, 10, 64)
			continue
		}

		if strings.HasPrefix(rows[i], "    If false: throw to monkey ") {
			falseID := strings.TrimLeft(rows[i], "    If false: throw to monkey ")
			monkeys[m].TestFalseID, _ = strconv.ParseInt(falseID, 10, 64)
			continue
		}
	}

	return monkeys
}

func getItems(in string) []int64 {
	sts := strings.Split(in, ", ")
	out := make([]int64, len(sts))

	for i := range sts {
		out[i], _ = strconv.ParseInt(sts[i], 10, 64)
	}

	return out
}

func getOperationEx(in string) OperationEx {
	out := OperationEx{}

	opParts := strings.Split(in, " ")

	if opParts[1] == "+" {
		out.Op = OpSum
	}
	if opParts[1] == "*" {
		out.Op = OpMult
	}

	out.Str = opParts[2]
	if out.Str == oldVal {
		return out
	}

	out.Val, _ = strconv.ParseInt(out.Str, 10, 64)

	return out
}
