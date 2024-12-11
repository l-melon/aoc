from functools import cache
from pathlib import Path
from itertools import repeat

path = Path(__file__).parent / "input.txt"

with path.open() as f:
    line = [*map(int, f.read().split())]


@cache
def blink(stone, iters):
    if iters == 0:
        return 1
    if stone == 0:
        return blink(1, iters - 1)
    stone_str = str(stone)
    l_stone = len(stone_str)
    if not l_stone % 2:
        return blink(int(stone_str[: l_stone // 2]), iters - 1) + blink(
            int(stone_str[l_stone // 2 :]), iters - 1
        )
    return blink(stone * 2024, iters - 1)


print(sum(map(blink, line, repeat(75))))
