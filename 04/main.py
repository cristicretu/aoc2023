input = open("input.txt").read().strip()
lines = input.split("\n")


nums = []
nums2 = [0] * (len(lines) + 1)

for i, line in enumerate(lines):
    _, game = line.split(":", 1)
    wins, checks = [set(g.split()) for g in game.split("|")]

    count = len(wins & checks)
    if count > 0:
        nums.append(2 ** (count - 1))
        for j in range(i + 2, i + count + 2):
            nums2[j] += nums2[i + 1] + 1

nums2 = [num + 1 for num in nums2][1:]
print(f"Part1: {sum(nums)}")
print(f"Part2: {sum(nums2)}")
