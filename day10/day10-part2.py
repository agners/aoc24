"""Advent of Code 2024 Day 10 part 1"""

import time

start = time.monotonic()

def walk_path(map: list[list[int]], path: list[tuple[int, int]], step: tuple[int, int]) -> tuple[int, int]:
    height = map[step[1]][step[0]]
    if height == 9:
        path.append(step)
        yield path
        return

    new_height = height + 1

    if step[0] > 0:
        # West
        if map[step[1]][step[0] - 1] == new_height:
            new_path = path.copy()
            new_path.append(step)
            for return_path in walk_path(map, new_path, (step[0] - 1, step[1])):
                yield return_path
    if step[1] > 0:
        # Nord
        if map[step[1] - 1][step[0]] == new_height:
            new_path = path.copy()
            new_path.append(step)
            for return_path in walk_path(map, new_path, (step[0], step[1] - 1)):
                yield return_path
    if step[0] < len(map[0]) - 1:
        # East
        if map[step[1]][step[0] + 1] == new_height:
            new_path = path.copy()
            new_path.append(step)
            for return_path in walk_path(map, new_path, (step[0] + 1, step[1])):
                yield return_path
    if step[1] < len(map) - 1:
        # South
        if map[step[1] + 1][step[0]] == new_height:
            new_path = path.copy()
            new_path.append(step)
            for return_path in walk_path(map, new_path, (step[0], step[1] + 1)):
                yield return_path

    return


with open("input.txt") as f:

    lines = f.readlines()
    score = 0

    map: list[list[int]] = []

    for line in lines:
        map.append([int(c) for c in line.strip()])

    print(map)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 0:
                for path in walk_path(map, [], (j, i)):
                    score += 1

    print("Score:", score)


print("Time:", time.monotonic() - start)
