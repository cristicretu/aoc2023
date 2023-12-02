input = open("input.txt").read().strip()
lines = input.split("\n")

max_sack = {
    "blue": 14,
    "green": 13,
    "red": 12,
}

ans = []
ans2 = []
for i, line in enumerate(lines):
    game = line.split(":")[1]

    ok = True

    max_game = {
        "blue": 0,
        "green": 0,
        "red": 0,
    }

    for round in game.split(";"):
        sack_dict = {
            "blue": 0,
            "green": 0,
            "red": 0,
        }

        for ball in round.split(","):
            num = int(ball.split(" ")[1])
            color = ball.split(" ")[2]
            sack_dict[color] = num

        for color, num in sack_dict.items():
            if num > max_sack[color]:
                ok = False
                break

        for color, _ in max_game.items():
            max_game[color] = max(max_game[color], sack_dict[color])

    if ok:
        ans.append(i + 1)

    ans2.append(max_game["blue"] * max_game["green"] * max_game["red"])

print(sum(ans))
print(sum(ans2))
