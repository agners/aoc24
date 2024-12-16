"""Advent of Code 2024 Day 16 part 1"""

from enum import IntEnum
import sys

sys.setrecursionlimit(10000)

class Direction(IntEnum):
    """Direction"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


def find_cheapest_path(map: list[list[str]], cheapest_paths: dict[tuple[int, int], int], pos: tuple[int, int], direction: Direction, goal: tuple[int, int], score) -> None:
    """Find the cheapest path from start to end"""
    if (*pos, direction) in cheapest_paths:
        if cheapest_paths[(*pos, direction)] <= score:
            return

    # This is the first time or cheapest time to get here, so search further    
    cheapest_paths[(*pos, direction)] = score

    if pos == goal:
        return

    # Turn right
    next_direction = Direction((direction + 1) % len(Direction))
    find_cheapest_path(map, cheapest_paths, pos, next_direction, goal, score + 1000)
    # Turn left
    next_direction = Direction((direction - 1) % len(Direction))
    find_cheapest_path(map, cheapest_paths, pos, next_direction, goal, score + 1000)

    # Try to move
    if direction == Direction.UP and map[pos[1] - 1][pos[0]] != "#":
        find_cheapest_path(map, cheapest_paths, (pos[0], pos[1] - 1), Direction.UP, goal, score + 1)
    elif direction == Direction.RIGHT and map[pos[1]][pos[0] + 1] != "#":
        find_cheapest_path(map, cheapest_paths, (pos[0] + 1, pos[1]), Direction.RIGHT, goal, score + 1)
    elif direction == Direction.DOWN and map[pos[1] + 1][pos[0]] != "#":
        find_cheapest_path(map, cheapest_paths, (pos[0], pos[1] + 1), Direction.DOWN, goal, score + 1)
    elif direction == Direction.LEFT and map[pos[1]][pos[0] - 1] != "#":
        find_cheapest_path(map, cheapest_paths, (pos[0] - 1, pos[1]), Direction.LEFT, goal, score + 1)



def print_map(map: list[list[str]]) -> None:
    """Print map"""
    for l in map:
        for c in l:
            print(c, end="")
        print()

with open("test-data.txt") as f:
    read_map: bool = True
    lines = f.readlines()
    map: list[list[str]] = []
    size_x = 0
    size_y = 0
    start_x = 0
    start_y = 0
    end_x = 0
    end_y = 0

    for line in lines:
        line = line.strip()
        if read_map:
            if len(line) == 0:
                read_map = False
                print(f"Map size: {size_x}x{size_y}")
                continue

            if size_y == 0:
                size_x = len(line)
            map.append([])
            for c in line:
                map[size_y].append(c)
                if c == "S":
                    start_x = len(map[size_y]) - 1
                    start_y = len(map) - 1
                elif c == "E":
                    end_x = len(map[size_y]) - 1
                    end_y = len(map) - 1
            size_y += 1
    
    print(f"Start: {start_x}, {start_y}, End: {end_x}, {end_y}")
    print_map(map)

    cheapest_paths: dict[tuple[int, int, Direction], int] = {}

    find_cheapest_path(map, cheapest_paths, (start_x, start_y), Direction.RIGHT, (end_x, end_y), 0)
    #print(cheapest_paths)

    scores = []
    for d in Direction:
        if (end_x, end_y, d) in cheapest_paths:
            print(d, cheapest_paths[(end_x, end_y, d)])
            scores.append(cheapest_paths[(end_x, end_y, d)])
    print("Cheapest path:", min(scores))
    


