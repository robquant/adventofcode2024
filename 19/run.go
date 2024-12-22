package main

import (
	"bytes"
	"fmt"
	"os"
)

var cache = make(map[string]uint64)

func count(design []byte, towels [][]byte) uint64 {
	if count, ok := cache[string(design)]; ok {
		return count
	}
	if len(design) == 0 {
		return 1
	}
	possible_from_here := uint64(0)
	for _, towel := range towels {
		if len(towel) > len(design) {
			continue
		}
		if bytes.HasPrefix(design, towel) {
			possible_from_here += count(design[len(towel):], towels)
		}
	}
	cache[string(design)] = possible_from_here
	return possible_from_here
}

func main() {

	var content []byte
	if len(os.Args) != 2 {
		content, _ = os.ReadFile("input")
	} else {
		content, _ = os.ReadFile(os.Args[1])
	}
	lines := bytes.Split(content, []byte("\n"))

	towels_raw := bytes.Split(lines[0], []byte(","))
	towels := make([][]byte, 0)

	for _, towel := range towels_raw {
		trimmed := bytes.Trim(towel, " ")
		if len(trimmed) == 0 {
			continue
		}
		towels = append(towels, trimmed)
	}

	var total_possible uint64 = 0
	possible := 0
	for _, design := range lines[2:] {
		if len(design) == 0 {
			continue
		}
		design_possible := count(design, towels)
		if design_possible > 0 {
			possible++
			total_possible += design_possible
		}
	}
	fmt.Println("Part 1:", possible)
	fmt.Println("Part 2:", total_possible)
}
