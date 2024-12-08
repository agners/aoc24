"""Advent of Code 2024 Day 8"""

import time

def check_bounds(resonance: tuple[int, int], x_size: int, y_size: int) -> bool:
    return resonance[0] >= 0 and resonance[0] < x_size and resonance[1] >= 0 and resonance[1] < y_size

start = time.monotonic()
with open("input.txt") as f:
    total = 0
    antennas: dict[list[tuple[int, int]]] = {}

    lines = f.readlines()
    x = 0
    y = 0
    
    for line in lines:
        x = 0
        for c in line:
            if c.isdigit() or c.isalpha():
                if c in antennas:
                    antennas[c].append((x, y))
                else:
                    antennas[c] = [(x, y)]
            x += 1
        y += 1
    
    x_size = x
    y_size = y
    print("Size", x_size, y_size)

    resonance_nodes = set()

    for k, v in antennas.items():
        for v1 in v:
            for v2 in antennas[k]:
                if v1 == v2:
                    continue
                r1 = (v1[0] - (v2[0] - v1[0]), v1[1] - (v2[1] - v1[1]))
                if check_bounds(r1, x_size, y_size):
                    resonance_nodes.add(r1)

    print(len(resonance_nodes))

print("Time:", time.monotonic() - start)
