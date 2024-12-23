"""Advent of Code 2024 Day 23 part 2"""

interconnections: set[str] = set()

def find_interconnections(connections: dict[str, set[str]], interconnection: set[str], new: str):
    """Find set of connections that are connected to each other"""
    for key in connections[new]:
        if key not in interconnection:
            valid = True
            for key_present in interconnection:
                if key not in connections[key_present]:
                    valid = False
                    break
            if valid:
                interconnection.add(key)
                interconnection_list = list(interconnection)
                interconnection_list.sort()
                interconnection_tuplet = tuple(interconnection_list)
                if interconnection_tuplet not in interconnections:
                    interconnections.add(interconnection_tuplet)
                find_interconnections(connections, interconnection, key)

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
        find_interconnections(connections, set([key]), key)
    
    longest_interconnection = next(iter(interconnections))
    for interconnection in interconnections:
        if len(longest_interconnection) < len(interconnection):
            longest_interconnection = interconnection

    longest_interconnection_list = list(longest_interconnection)
    longest_interconnection_list.sort()
    
    print(",".join(longest_interconnection_list))

    print(len(longest_interconnection))

