"""Advent of Code 2024 Day 18 part 1"""

from enum import IntEnum
import sys

sys.setrecursionlimit(10000)

class Direction(IntEnum):
    """Direction"""
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def scout_for_cheapest_path(
        map: list[list[str]],
        path: set[tuple[int, int]],
        path_cost: dict[tuple[int, int], int],
        pos: tuple[int, int],
        goal: tuple[int, int],
        score: int,
    ) -> int:
    """Find the cheapest path from start to end"""
    if pos in path:
        return
    path = path.copy()
    path.add(pos)
    if pos in path_cost:
        if path_cost[pos] <= score:
            return
    path_cost[pos] = score

    if pos == goal:
        return

    # Try to move
    # UP
    if pos[1] > 0 and map[pos[1] - 1][pos[0]] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0], pos[1] - 1), goal, score + 1)
    # RIGHT
    if pos[0] < len(map[0]) - 1 and map[pos[1]][pos[0] + 1] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0] + 1, pos[1]), goal, score + 1)
    # DOWN
    if pos[1] < len(map) - 1 and map[pos[1] + 1][pos[0]] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0], pos[1] + 1), goal, score + 1)
    # LEFT
    if pos[0] > 0 and map[pos[1]][pos[0] - 1] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0] - 1, pos[1]), goal, score + 1)

def print_map(map: list[list[str]]) -> None:
    """Print map"""
    for l in map:
        for c in l:
            print(c, end="")
        print()

with open("input.txt") as f:
    map: list[list[str]] = []
    size_x = 71
    size_y = 71

    for y in range(size_y):
        x_list = []
        for x in range(size_x):
            x_list.append(".")
        map.append(x_list)

    after_bytes = 1024
    while True:
        line = f.readline()
        if line == "":
            break
        x_str, y_str = line.strip().split(",")
        map[int(y_str)][int(x_str)] = "#"
        after_bytes -= 1
        if after_bytes == 0:
            break

    print_map(map)

    path_cost: dict[tuple[int, int], int] = {}
    goal = (size_x - 1,  size_y - 1)
    scout_for_cheapest_path(map, set(), path_cost, (0, 0), goal, 0)
    print(path_cost[goal])


