with open("input.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

rows = len(lines)
cols = len(lines[0])
word = "XMAS"
word_len = len(word)

directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


def check_word(x, y, dx, dy):
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < rows and 0 <= ny < cols):
            return False
        if lines[nx][ny] != word[i]:
            return False
    return True


occurrences = []
for x in range(rows):
    for y in range(cols):
        for dx, dy in directions:
            if check_word(x, y, dx, dy):
                occurrences.append((x, y, dx, dy))

print(len(occurrences))
