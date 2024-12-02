with open("input.txt") as f:
    lines = f.readlines()

left, right = zip(*((int(a), int(b)) for a, b in (line.split() for line in lines)))


left = sorted(left)
right = sorted(right)

distant = sum(abs(l - r) for l, r in zip(left, right))

print(distant)
