package main

import (
	"bytes"
	"os"
	"strconv"
)

func mix(a, b uint64) uint64 {
	return a ^ b
}

func prune(a uint64) uint64 {
	return a % 16777216
}

func evolve(a uint64) uint64 {
	b := prune(mix(a, a*64))
	c := prune(mix(b/32, b))
	return prune(mix(c, c*2048))
}

func evolve_n(a uint64, n int) uint64 {
	for _ = range n {
		a = evolve(a)
	}
	return a
}

func main() {
	content, _ := os.ReadFile("input")
	lines := bytes.Split(content, []byte("\n"))
	total := uint64(0)
	for _, line := range lines {
		if len(line) == 0 {
			continue
		}
		num, _ := strconv.Atoi(string(line))
		total += evolve_n(uint64(num), 2000)
	}
	println(total)
}
