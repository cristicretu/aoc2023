lines = [
    [int(i) for i in s.split()]
    for s in open("input.txt").read().split("\n")
    if s.strip()
]


def solve(line):
    diff_f = [line[i + 1] - line[i] for i in range(len(line) - 1)]

    last_diff = [diff_f[-1]]
    while not all([x == 0 for x in diff_f]):
        diff_f = [diff_f[i + 1] - diff_f[i] for i in range(len(diff_f) - 1)]
        last_diff.append(diff_f[-1])

    return line[-1] + sum(last_diff)


print(sum(solve(line) for line in lines))
print(sum(solve(line[::-1]) for line in lines))
