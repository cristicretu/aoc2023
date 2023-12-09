lines = open("input.txt").read().splitlines()

nums = []
nums1 = []


def is_zero(vec):
    for i in vec:
        if i != 0:
            return False
    return True


for line in lines:
    row = [int(x) for x in line.split(" ")]

    diff_f = [row[i + 1] - row[i] for i in range(len(row) - 1)]

    last_diff = [diff_f[-1]]
    first_diff = [row[0], diff_f[0]]

    while not is_zero(diff_f):
        diff_f = [diff_f[i + 1] - diff_f[i] for i in range(len(diff_f) - 1)]
        last_diff.append(diff_f[-1])
        first_diff.append(diff_f[0])

    # part 1
    nums.append(row[-1] + sum(last_diff))

    ans = [0]
    for i in range(len(first_diff) - 1, -1, -1):
        ans.append(first_diff[i - 1] - ans[len(first_diff) - 1 - i])

    # part 2
    nums1.append(ans[-2])

# print(nums)
print(sum(nums))
# print(nums1)
print(sum(nums1))
