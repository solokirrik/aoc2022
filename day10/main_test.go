package main

import (
	_ "embed"
	"testing"

	"github.com/stretchr/testify/assert"
)

//go:embed example
var testInp string

func Test_part1(t *testing.T) {
	expected := 13140
	got := part1(testInp)

	assert.Equal(t, expected, got)
}

func Test_part2(t *testing.T) {
	expected := 0
	got := part2(testInp)

	assert.Equal(t, expected, got)
}
