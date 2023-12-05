input = open("input.txt", "r").read().strip()
lines = input.split("\n")

seeds = [int(c) for c in lines[0].split(":")[1].strip().split(" ")]

maps = []


def convert(seed, maps):
    for end, start, dist in maps:
        if seed >= start and seed < (start + dist):
            return seed + end - start
    return seed


def p2(seeds, maps):
    def map_range(seed_range, map_list):
        result = []
        seed_start, seed_len = seed_range
        for dest, source, range_len in sorted(map_list, key=lambda x: x[1]):
            offset = dest - source
            if seed_start >= source and seed_start < source + range_len:
                res_start = seed_start + offset

                if source + range_len >= seed_start + seed_len:
                    result.append((res_start, seed_len))
                else:
                    new_seed_len = seed_start + seed_len - source - range_len
                    result.append((res_start, seed_len - new_seed_len))
                    seed_len = new_seed_len
                    seed_start = source + range_len
        if not result:
            result.append(seed_range)
        return result

    my_list = []
    for sp in pairwise(seeds):
        seed_ranges = [sp]
        for m in maps:
            new_s = []
            for s in seed_ranges:
                new_s.extend(map_range(s, m))
            seed_ranges = new_s[:]
        my_list.append(min(x for x, _ in seed_ranges))
    print(min(my_list))


def pairwise(iterable):
    a = iter(iterable)
    return zip(a, a)


for line in lines[2:]:
    if line.endswith("map:"):
        curr = []
        continue
    if line == "":
        maps.append(curr)
        continue

    curr.append([int(c) for c in line.split(" ")])


# print(maps)

# print(seeds)
# print(min(seeds))
p2(seeds, maps)

for i in range(len(seeds)):
    for m in maps:
        seeds[i] = convert(seeds[i], m)
