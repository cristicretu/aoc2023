from queue import Queue


lines = open("input.txt").read().strip().split("\n")

n = {
    "|": [(0, -1), (0, 1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(-1, 0), (0, 1)],
    "F": [(1, 0), (0, 1)],
}

sx, sy = None, None

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "S":
            sx, sy = j, i
            break

q = Queue()

for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
    char = lines[sy + dy][sx + dx]
    if char in n:
        for dx2, dy2 in n[char]:
            if sx == sx + dx + dx2 and sy == sy + dy + dy2:
                q.put((1, (sx + dx, sy + dy)))

dists = {(sx, sy): 0}

while not q.empty():
    d, (sx, sy) = q.get()

    if (sx, sy) in dists:
        continue

    dists[(sx, sy)] = d

    for dx, dy in n[lines[sy][sx]]:
        q.put((d + 1, (sx + dx, sy + dy)))


print(max(dists.values()))


ans = 0
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if (x, y) in dists:
            continue

        cross = 0
        x2, y2 = x, y

        while x2 < len(lines[0]) and y2 < len(lines):
            c2 = lines[y2][x2]

            if (x2, y2) in dists and c2 != "L" and c2 != "7":
                cross += 1

            x2 += 1
            y2 += 1

        if cross % 2 == 1:
            ans += 1

print(ans)
