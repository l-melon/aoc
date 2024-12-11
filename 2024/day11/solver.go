package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var cache = make(map[[2]int]int)

// ParseNumberFromFile read the input file and parses its content into a slice of integers.
func ParseNumberFromFile(filename string) ([]int, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	line := strings.TrimSpace(string(data))
	strNumbers := strings.Fields(line)

	numbers := make([]int, 0, len(strNumbers))
	for _, str := range strNumbers {
		num, err := strconv.Atoi(str)
		if err != nil {
			return nil, err
		}
		numbers = append(numbers, num)
	}

	return numbers, nil
}

func Blink(stone, iters int) int {
	key := [2]int{stone, iters}
	if val, found := cache[key]; found {
		return val
	}

	if iters == 0 {
		return 1
	}

	if stone == 0 {
		cache[key] = Blink(1, iters-1)
		return cache[key]
	}

	lStone := len(strconv.Itoa((stone)))
	divisor := int(math.Pow10(lStone / 2))
	var result int

	if lStone%2 == 0 {
		result = Blink(stone/divisor, iters-1) + Blink(stone%divisor, iters-1)
	} else {
		result = Blink(stone*2024, iters-1)
	}

	cache[key] = result
	return result
}

func main() {
	filename := "input.txt"
	numbers, err := ParseNumberFromFile(filename)
	if err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	total := 0
	for _, num := range numbers {
		blink := Blink(num, 75)
		total += blink
	}

	fmt.Print(total)
}
