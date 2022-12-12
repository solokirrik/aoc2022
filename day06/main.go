package main

import (
	_ "embed"
	"fmt"
)

//go:embed day6
var day6inp string

const msgLen = 14

func main() {
	fmt.Println(getPos(day6inp))
}

func getPos(inp string) int {
	i := 0

	q := queue{s: []byte{}, m: make(map[byte]int)}

	for {
		if q.Len() < msgLen {
			q.push(inp[i])

			i++

			continue
		}

		if q.gotDoubles() {
			q.pop()
			q.push(inp[i])

			i++

			continue
		} else {
			break
		}
	}

	return i
}

type queue struct {
	s []byte
	m map[byte]int
}

func (q *queue) Len() int {
	return len(q.s)
}

func (q *queue) gotDoubles() bool {
	return len(q.s) != len(q.m)
}

func (q *queue) push(b byte) {
	q.s = append(q.s, b)
	val, _ := q.m[b]
	val++
	q.m[b] = val
}

func (q *queue) pop() byte {
	ch := q.s[0]
	q.s = q.s[1:]
	val := q.m[ch]

	if val == 1 {
		delete(q.m, ch)
	}

	if val > 1 {
		val--
		q.m[ch] = val
	}

	return ch
}
