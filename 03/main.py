input = open("input.txt").read().strip()
lines = input.split("\n")

nums = []
nums2 = []
ans = 0

di = [-1, -1, -1, 0, 1, 1, 1, 0]
dj = [-1, 0, 1, 1, 1, 0, -1, -1]


def check_symbol(c):
    return c != "." and not c.isdigit()


def check_neigh(lines, i, j):
    if not lines[i][j].isdigit():
        return 0, 0, 0

    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        if ni < 0 or nj < 0 or ni >= len(lines) or nj >= len(lines[ni]):
            continue
        if check_symbol(lines[ni][nj]):
            return (lines[ni][nj], ni, nj)
    return (0, 0, 0)


for i, line in enumerate(lines):
    j = 0
    while j < len(line):
        check_result, ni, nj = check_neigh(lines, i, j)
        if check_result:
            # number is good =>
            # go find the start and end of the number
            start = j
            end = j

            while (
                start > 0 and lines[i][start - 1] >= "0" and lines[i][start - 1] <= "9"
            ):
                start -= 1

            while (
                end < len(lines[i]) - 1
                and lines[i][end + 1] >= "0"
                and lines[i][end + 1] <= "9"
            ):
                end += 1

            nums.append(int(lines[i][start : end + 1]))

            if check_result == "*":
                n = {
                    f"{ni},{nj}": int(lines[i][start : end + 1]),
                }
                nums2.append(n)

            # skip adding the number multiple times
            j = end + 1
        else:
            j += 1


print(sum(nums))

# part 2
count_dict = {}
value_dict = {}

for d in nums2:
    for key, value in d.items():
        if key not in count_dict:
            count_dict[key] = 1
            value_dict[key] = [value]
        else:
            count_dict[key] += 1
            value_dict[key].append(value)

result = sum(
    value_dict[key][0] * value_dict[key][1]
    for key in count_dict
    if count_dict[key] == 2
)

print(result)
