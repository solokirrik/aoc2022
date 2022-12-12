package main

import (
	"testing"

	"github.com/stretchr/testify/assert"
)

func Test_getPos(t *testing.T) {
	tests := []struct {
		name string
		inp  string
		want int
	}{
		{inp: "mjqjpqmgbljsphdztnvjfqwrcgsmlb", want: 7},
		{inp: "bvwbjplbgvbhsrlpgdmjqwftvncz", want: 5},
		{inp: "nppdvjthqldpwncqszvftbrmjlhg", want: 6},
		{inp: "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", want: 10},
		{inp: "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", want: 11},
	}
	for _, tt := range tests {
		t.Run(tt.inp, func(t *testing.T) {
			assert.Equal(t, tt.want, getPos(tt.inp))
		})
	}
}
