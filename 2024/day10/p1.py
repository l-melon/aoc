from pathlib import Path
from collections import deque

path = Path(__file__).parent / "input.txt"

with path.open() as f:
    grid = [list(map(int, line)) for line in f.read().splitlines()]

rows = len(grid)
cols = len(grid[0])

directions = [
    (0, 1),  # Right
    (0, -1),  # Left
    (1, 0),  # Down
    (-1, 0),  # Up
]


def is_valid_move(x, y, curr_height):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == curr_height + 1


def bfs(start_x, start_y):
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_x, start_y, 0)])
    reachable_nines = set()

    while queue:
        x, y, curr_height = queue.popleft()

        visited[x][y] = True

        if grid[x][y] == 9:
            reachable_nines.add((x, y))
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid_move(nx, ny, curr_height) and not visited[nx][ny]:
                queue.append((nx, ny, grid[nx][ny]))

    return len(reachable_nines)


trailhead_scores = []
for x in range(rows):
    for y in range(cols):
        if grid[x][y] == 0:
            score = bfs(x, y)
            trailhead_scores.append(((x, y), score))

score = sum([score for _, score in trailhead_scores])
print(score)
