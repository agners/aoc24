"""Advent of Code 2024 Day 23 part 1"""

with open("test-data.txt") as f:
    read_map: bool = True
    lines = f.readlines()
    connections: dict[str, set[str]] = {}

    for line in lines:
        a, b = line.strip().split("-")
        connections.setdefault(a, set()).add(b)
        connections.setdefault(b, set()).add(a)

    triplets: set = set()
    for key in connections.keys():
        for key2 in connections[key]:
            for key3 in connections[key2]:
                if key3 in connections[key]:
                    if key[0] == "t" or key2[0] == "t" or key3[0] == "t":
                        triplet = [key, key2, key3]
                        triplet.sort()
                        triplets.add(tuple(triplet))

    print(len(triplets))

