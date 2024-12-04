with open("input.txt") as f:
    lines = [list(line.strip()) for line in f.readlines()]

rows = len(lines)
cols = len(lines[0])
word = "MAS"
reversed_word = word[::-1]
word_len = len(word)


def check_word(x, y, dx, dy, word):
    for i in range(word_len):
        nx, ny = x + i * dx, y + i * dy
        if not (0 <= nx < rows and 0 <= ny < cols):
            return False
        if lines[nx][ny] != word[i]:
            return False
    return True


occurrences = []
for x in range(1, rows - 1):
    for y in range(1, cols - 1):
        if lines[x][y] == "A":
            top_left_to_bottom_right = check_word(
                x - 1, y - 1, 1, 1, word
            ) or check_word(x - 1, y - 1, 1, 1, reversed_word)

            top_right_to_bottom_left = check_word(
                x - 1, y + 1, 1, -1, word
            ) or check_word(x - 1, y + 1, 1, -1, reversed_word)

            if top_left_to_bottom_right and top_right_to_bottom_left:
                occurrences.append((x, y))

print(len(occurrences))
