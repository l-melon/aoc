from collections import Counter

with open("input.txt") as f:
    lines = f.readlines()

left, right = zip(*((int(a), int(b)) for a, b in (line.split() for line in lines)))

similarity = Counter(right)

score = sum(l * similarity.get(l, 0) for l in left)

print(score)
