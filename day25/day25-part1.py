"""Advent of Code 2024 Day 25 part 1"""

def parse_line(line: str, pin: list[int]):
    for i in range(5):
        if line[i] == "#":
            pin[i] += 1

def check_match(key: tuple[int, int, int, int, int], lock: tuple[int, int, int, int, int]) -> bool:
    for i in range(5):
        if key[i] + lock[i] > 5:
            return False
    return True

with open("input.txt") as f:
    keys: set[tuple[int, int, int, int, int]] = set()
    locks: set[tuple[int, int, int, int, int]] = set()

    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        if line == "#####":
            pin = [ 0, 0, 0, 0, 0]
            for i in range(5):
                parse_line(f.readline().strip(), pin)
            locks.add(tuple(pin))
            assert f.readline().strip() == "....."
        elif line == ".....":
            pin = [ 0, 0, 0, 0, 0]
            for i in range(5):
                parse_line(f.readline().strip(), pin)
            keys.add(tuple(pin))
            assert f.readline().strip() == "#####"

    
    print("Keys:", len(keys))
    print("Locks:", len(locks))

    matches: set[tuple[tuple[int, int, int, int, int], tuple[int, int, int, int, int]]] = set()
    for key in keys:
        for lock in locks:
            if check_match(key, lock):
                matches.add((key, lock))

    print("Matches:", len(matches))
