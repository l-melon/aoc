from pathlib import Path

path = Path(__file__).parent / "input.txt"

with path.open() as f:
    line = f.read().strip()

if len(line) // 2 != 0:
    line += "0"

disk_map = [
    [[value, int(line[i])], [".", int(line[i + 1])]]
    for value, i in enumerate(range(0, len(line), 2))
]

for r in range(len(disk_map) - 1, -1, -1):
    r_value = disk_map[r][0][0]
    r_file = disk_map[r][0][1]
    r_free = disk_map[r][1][1]
    if r_file <= 0:
        continue

    for l in range(r):
        l_file = disk_map[l][0][1]
        l_free = disk_map[l][-1][1]
        if l_free < r_file:
            continue

        # right side
        disk_map[r][0] = [".", r_file]

        # left side
        disk_map[l][-1:] = [[r_value, r_file], [".", l_free - r_file]]
        break

disk_list = []
for disk in disk_map:
    for d in disk:
        disk_list.extend([d[0]] * d[1])

total = 0
for i, d in enumerate(disk_list):
    if d != ".":
        total += i * int(d)

print(total)
