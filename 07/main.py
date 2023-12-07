from functools import cmp_to_key

lines = open("input.txt", "r").read().splitlines()
part2 = False

d = {}
m = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

for line in lines:
    d[line.split(" ")[0]] = int(line.split(" ")[1])


def determine_hand(hand):
    freq = {}
    for card in hand:
        if card[0] not in freq:
            freq[card[0]] = 1
        else:
            freq[card[0]] += 1

    if part2:
        j_freq = freq["J"] if "J" in freq else 0

        if j_freq == 5:
            return 10  # five of a kind

        sorted_d = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        if j_freq > 0:
            for i in range(len(sorted_d)):
                if sorted_d[i][0] != "J":
                    sorted_d[i] = (sorted_d[i][0], sorted_d[i][1] + j_freq)
                    break

        freq = {k: v for k, v in sorted_d if k != "J"}

    if len(freq) == 1:
        return 10  # five of a kind
    elif len(freq) == 2:
        if 4 in freq.values():
            return 9  # four of a kind
        else:
            return 8  # full house
    elif len(freq) == 3:
        if 3 in freq.values():
            return 7  # three of a kind
        else:
            return 6  # two pair
    elif len(freq) == 4:
        return 5  # one pair
    else:
        return 4  # high card


def compare(a, b):
    if determine_hand(a) > determine_hand(b):
        return 1
    elif determine_hand(a) < determine_hand(b):
        return -1
    else:
        for i in range(len(a)):
            if m.index(a[i]) > m.index(b[i]):
                return 1
            elif m.index(a[i]) < m.index(b[i]):
                return -1


def hand_to_list(hand_str):
    return [hand_str[i : i + 1] for i in range(0, len(hand_str), 1)]


hands = [hand_to_list(hand) for hand in d.keys()]
sorted_hands = sorted(hands, key=cmp_to_key(compare))

# part 1
ans = 0
for i, h in enumerate(sorted_hands):
    ans += (i + 1) * d["".join(h)]
print(ans)

# part 2
m = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
part2 = True
sorted_hands = sorted(hands, key=cmp_to_key(compare))
# sorted_d = {"".join(hand): d["".join(hand)] for hand in sorted_hands}
# print(sorted_d)

ans1 = 0
for i, h in enumerate(sorted_hands):
    ans1 += (i + 1) * d["".join(h)]
print(ans1)
