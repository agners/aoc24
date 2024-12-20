"""Advent of Code 2024 Day 20 part 1"""

from enum import IntEnum
import sys

sys.setrecursionlimit(10000)

Point = tuple[int, int]

cheats: dict[tuple[Point, Point]] = {}


def scout_for_cheapest_path(
        map: list[list[str]],
        path: set[Point],
        path_cost: dict[Point, int],
        pos: tuple[int, int],
        goal: tuple[int, int],
        score: int,
    ) -> None:
    """Find the cheapest path from start to end"""
    if pos in path:
        return
    path = path.copy()
    path.add(pos)
    path_cost[pos] = score

    if pos == goal:
        return

    # Try to move
    # UP
    if map[pos[1] - 1][pos[0]] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0], pos[1] - 1), goal, score + 1)
    # RIGHT
    if map[pos[1]][pos[0] + 1] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0] + 1, pos[1]), goal, score + 1)
    # DOWN
    if map[pos[1] + 1][pos[0]] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0], pos[1] + 1), goal, score + 1)
    # LEFT
    if map[pos[1]][pos[0] - 1] != "#":
        scout_for_cheapest_path(map, path, path_cost, (pos[0] - 1, pos[1]), goal, score + 1)


def find_cheapest_path(
        map: list[list[str]],
        cheat_start: tuple[int, int] | None,
        cheat_end: tuple[int, int] | None,
        path: set[Point],
        path_cost: dict[Point, int],
        pos: tuple[int, int],
        goal: tuple[int, int],
        score: int,
    ) -> None:
    """Find the cheapest path from start to end"""
    if pos in path:
        return
    path = path.copy()
    path.add(pos)
    
    if cheat_start is not None and cheat_end is None and map[pos[1]][pos[0]] != "#":
        cheat_end = pos
        if path_cost[pos] - 100 >= score:
            print(f"Found cheat from {cheat_start} to {cheat_end} saves {path_cost[pos] - score} steps")
            cheats[cheat_start, cheat_end] = score
        return

    #if pos == goal:
    #    cheats[cheat_start, cheat_end] = score
    #    print(f"Path cost with cheat from {cheat_start} to {cheat_end} is {score}")
    #    return

    # Try to move
    # UP
    if pos[1] > 0 and map[pos[1] - 1][pos[0]] != "#":
        find_cheapest_path(map, cheat_start, cheat_end, path, path_cost, (pos[0], pos[1] - 1), goal, score + 1)
    # RIGHT
    if pos[0] < len(map[pos[1]]) - 1 and map[pos[1]][pos[0] + 1] != "#":
        find_cheapest_path(map, cheat_start, cheat_end, path, path_cost, (pos[0] + 1, pos[1]), goal, score + 1)
    # DOWN
    if pos[1] < len(map) - 1 and map[pos[1] + 1][pos[0]] != "#":
        find_cheapest_path(map, cheat_start, cheat_end, path, path_cost, (pos[0], pos[1] + 1), goal, score + 1)
    # LEFT
    if pos[0] > 0 and map[pos[1]][pos[0] - 1] != "#":
        find_cheapest_path(map, cheat_start, cheat_end, path, path_cost, (pos[0] - 1, pos[1]), goal, score + 1)

    if cheat_start is None:
        # UP
        if map[pos[1] - 1][pos[0]] == "#":
            find_cheapest_path(map, pos, cheat_end, path, path_cost, (pos[0], pos[1] - 1), goal, score + 1)
        # RIGHT
        if map[pos[1]][pos[0] + 1] == "#":
            find_cheapest_path(map, pos, cheat_end, path, path_cost, (pos[0] + 1, pos[1]), goal, score + 1)
        # DOWN
        if map[pos[1] + 1][pos[0]] == "#":
            find_cheapest_path(map, pos, cheat_end, path, path_cost, (pos[0], pos[1] + 1), goal, score + 1)
        # LEFT
        if map[pos[1]][pos[0] - 1] == "#":
            find_cheapest_path(map, pos, cheat_end, path, path_cost, (pos[0] - 1, pos[1]), goal, score + 1)



def print_map(map: list[list[str]]) -> None:
    """Print map"""
    for l in map:
        for c in l:
            print(c, end="")
        print()

with open("input.txt") as f:
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

    path_cost: dict[Point, int] = {}
    scout_for_cheapest_path(map, set(), path_cost, (start_x, start_y), (end_x, end_y), 0)
    #print(path_cost)
    find_cheapest_path(map, None, None, set(), path_cost, (start_x, start_y), (end_x, end_y), 0)


    print("Cost without cheat: ", path_cost[(end_x, end_y)])
    print("Cheats: ", len(cheats))

    #cost_without_cheat = cheats[None, None]
    #print("Cost without cheat: ", cost_without_cheat)

    # Find the best cheats
    #best_cheats: dict[int, set[Point]] = {}
    #for cheat, cost in cheats.items():
    #    if cost >= cost_without_cheat:
    #        continue
    #
    #    if cost not in best_cheats:
    #        best_cheats[cost] = set()
    #    best_cheats[cost].add(cheat)
    #
    #for cost, cheats in best_cheats.items():
    #    print(f"Cost: {cost}, Cheats: {len(cheats)}")
        
    


