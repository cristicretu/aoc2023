input = open("input.txt").read().strip()
lines = input.split("\n")


nums = []
nums2 = [0] * len(lines) + [0]

for i, line in enumerate(lines):
    game = line.split(":")[1]

    s = set()
    count = 0
    for win in game.split("|")[0].split(" "):
        if win != "":
            s.add(win)

    for c in game.split("|")[1].split(" "):
        if c in s:
            count += 1

    if count > 0:
        nums.append(2 ** (count - 1))

        # part 2
        # go through all games
        for j in range(i + 2, i + count + 2):
            nums2[j] += nums2[i + 1] + 1
            pass


nums2 = [num + 1 for num in nums2][1:]
print(sum(nums))
# print(nums2)
print(sum(nums2))
