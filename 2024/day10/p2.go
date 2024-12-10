//go:build part2

package main

import (
	"container/list"
	"fmt"
	"os"
	"strings"
	"unicode"
)

func ParseMapFromFile(filename string) ([][]int, error) {
	data, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}

	lines := strings.Split(strings.TrimSpace(string(data)), "\n")
	grid := make([][]int, 0, len(lines))

	for _, line := range lines {
		line = strings.TrimSpace(line)
		if len(line) == 0 {
			continue
		}
		row := make([]int, 0, len(line))
		for _, char := range line {
			if unicode.IsDigit(char) {
				row = append(row, int(char-'0'))
			}
		}
		if len(row) > 0 {
			grid = append(grid, row)
		}
	}
	return grid, nil
}

func IsValidMove(grid [][]int, x, y, currHeight int) bool {
	rows, cols := len(grid), len(grid[0])

	return x >= 0 && x < rows && y >= 0 && y < cols && grid[x][y] == currHeight+1
}

// BFS performs BSF to find all reachable 9s from a trailhead
func BFS(grid [][]int, startX, startY int) int {
	rows, cols := len(grid), len(grid[0])
	visited := make([][]bool, rows)

	for i := range visited {
		visited[i] = make([]bool, cols)
	}

	queue := list.New()
	queue.PushBack([3]int{startX, startY, 0}) // (x, y, current height)

	var reachableNines []struct{ x, y int }

	directions := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for queue.Len() > 0 {
		front := queue.Remove(queue.Front()).([3]int)
		x, y, currHeight := front[0], front[1], front[2]

		visited[x][y] = true

		if grid[x][y] == 9 {
			reachableNines = append(reachableNines, struct{ x, y int }{x, y})
			continue
		}
		for _, dir := range directions {
			nx, ny := x+dir[0], y+dir[1]
			if IsValidMove(grid, nx, ny, currHeight) && !visited[nx][ny] {
				queue.PushBack([3]int{nx, ny, grid[nx][ny]})
			}
		}

	}
	return len(reachableNines)
}

func CalculateTrailheadScores(grid [][]int) map[[2]int]int {
	rows, cols := len(grid), len(grid[0])

	trailheadScores := make(map[[2]int]int)

	for x := 0; x < rows; x++ {
		for y := 0; y < cols; y++ {
			if grid[x][y] == 0 {
				score := BFS(grid, x, y)
				trailheadScores[[2]int{x, y}] = score
			}
		}
	}

	return trailheadScores
}

func main() {
	fileName := "input.txt"

	grid, err := ParseMapFromFile(fileName)
	if err != nil {
		os.Exit(1)
	}

	trailheadScores := CalculateTrailheadScores(grid)

	total := 0
	for _, score := range trailheadScores {
		total += score
	}

	fmt.Print(total)
}
