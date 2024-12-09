from pathlib import Path

path = Path(__file__).parent / "input.txt"

with path.open() as f:
    line = f.read().strip()

if len(line) // 2 != 0:
    line += "0"

disk_map = [(int(line[i]), int(line[i + 1])) for i in range(0, len(line), 2)]

disk_list = []
for i, disk in enumerate(disk_map):
    disk_list.extend([i] * disk[0])
    disk_list.extend(['.'] * disk[1])

n = len(disk_list)

for i in range(n - 1, -1, -1):
    if all(disk_list[k] != "." for k in range(0, i)):
        break
    if disk_list[i] != ".":
        for j in range(n):
            if disk_list[j] == ".":
                disk_list[j], disk_list[i] = disk_list[i], disk_list[j]
                break

total = 0
for i, disk_list in enumerate(disk_list):
    if disk_list != ".":
        total += i * int(disk_list)

print(total)
