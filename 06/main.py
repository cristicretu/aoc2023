input = open("input.txt", "r").read()
lines = input.split("\n")

time = [int(c) for c in lines[0].split(":")[1].split(" ") if c != ""]
dist = [int(c) for c in lines[1].split(":")[1].split(" ") if c != ""]

nums = [
    sum(1 for x in range(time[t]) if x * (time[t] - x) - dist[t] > 0)
    for t in range(len(time))
]

ans1 = 1
for n in nums:
    ans1 *= n

print(ans1)

time = int("".join([c for c in lines[0].split(":")[1].split(" ") if c != ""]))
dist = int("".join([c for c in lines[1].split(":")[1].split(" ") if c != ""]))

delta = time * time - 4 * dist

x1 = (-time - delta**0.5) / -2
x2 = (-time + delta**0.5) / -2

ans2 = abs(x1 - x2)

print(int(ans2))
