def get_num_by_line(line):
    nums_vec = [int(x) for x in line if x >= "0" and x <= "9"]

    return (
        (nums_vec[0] * 10 + nums_vec[-1])
        if len(nums_vec) > 1
        else (nums_vec[0] * 10 + nums_vec[0])
    )


with open("input1.txt", "r") as f:
    lines = f.readlines()
    nums = []
    for line in lines:
        nums.append(get_num_by_line(line))

    print(sum(nums))

digits = [
    ("zero", 0),
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]


def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)


with open("input2.txt", "r") as f:
    lines = f.readlines()

    nums = []
    for line in lines:
        lowest_index = len(line)
        lowest_nr = 10

        last_index = -1
        last_nr = -1

        for digit in digits:
            occ = list(find_all(line, digit[0]))
            if len(occ) > 0:
                if occ[0] < lowest_index:
                    lowest_index = occ[0]
                    lowest_nr = digit[1]

                if occ[-1] > last_index:
                    last_index = occ[-1]
                    last_nr = digit[1]

        for i, c in enumerate(line):
            if c >= "0" and c <= "9":
                if i < lowest_index:
                    lowest_index = i
                    lowest_nr = int(c)

                if i > last_index:
                    last_index = i
                    last_nr = int(c)

        num = (
            (lowest_nr * 10 + last_nr)
            if lowest_index != last_index
            else (lowest_nr * 10 + lowest_nr)
        )
        nums.append(num)

    print(sum(nums))


"""
find first position of digit
and last position of digit
"""
