lines = open("input.txt").read().splitlines()

directions = lines[0]

dict = {}

for line in lines[2:]:
    dict[line.split("=")[0].strip()] = (
        line.split("=")[1].strip().split(",")[0][1:],
        line.split("=")[1].strip().split(",")[1][:-1].strip(),
    )


steps = 0
curr = "AAA"
while True:
    direction = directions[steps % len(directions)]
    if curr == "ZZZ":
        print(steps)
        break

    if direction == "L":
        curr = dict[curr][0]
        steps += 1
    elif direction == "R":
        curr = dict[curr][1]
        steps += 1
