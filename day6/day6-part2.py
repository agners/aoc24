"""Advent of Code 2024 Day 6"""

from collections.abc import Iterator

def walk_check(map: list[str], x: int, y: int, direction: str) -> bool:
    """Walk on the map and check if this would lead to a loop"""
    size_x = len(map[0])
    size_y = len(map)
    path = set()
    while True:
        if direction == "^":
            if y == 0:
                return False
            if map[y-1][x] == "#":
                # Turn right and keep going
                direction = ">"
            else:
                y -= 1
                if (x, y, direction) in path:
                    return True
                path.add((x, y, direction))
        elif direction == ">":
            if x == size_x - 1:
                return False
            if map[y][x+1] == "#":
                # Turn right and keep going
                direction = "v"
            else:
                x += 1
                if (x, y, direction) in path:
                    return True
                path.add((x, y, direction))
        elif direction == "v":
            if y == size_y - 1:
                return False
            if map[y+1][x] == "#":
                # Turn right and keep going
                direction = "<"
            else:
                y += 1
                if (x, y, direction) in path:
                    return True
                path.add((x, y, direction))
        elif direction == "<":
            if x == 0:
                return False
            if map[y][x-1] == "#":
                # Turn right and keep going
                direction = "^"
            else:
                x -= 1
                if (x, y, direction) in path:
                    return True
                path.add((x, y, direction))



def walk(map: list[str], x: int, y: int) -> Iterator[tuple[int, int]]:
    """Walk on the map"""
    size_x = len(map[0])
    size_y = len(map)
    while True:
        if map[y][x] == "^":
            if y == 0:
                break
            if map[y-1][x] == "#":
                # Turn right
                map[y][x] = ">"
            else:
                y -= 1
                # What if we add a block here?
                if map[y][x] == ".":
                    map[y][x] = "#"
                    if walk_check(map, x, y + 1, ">"):
                        yield (y, x)
                map[y][x] = "^"
        elif map[y][x] == ">":
            if x == size_x - 1:
                break
            if map[y][x+1] == "#":
                # Turn right
                map[y][x] = "v"
            else:
                x += 1
                # What if we add a block here?
                if map[y][x] == ".":
                    map[y][x] = "#"
                    if walk_check(map, x - 1, y, "v"):
                        yield (y, x)
                map[y][x] = ">"
        elif map[y][x] == "v":
            if y == size_y - 1:
                break
            if map[y+1][x] == "#":
                # Turn right
                map[y][x] = "<"
            else:
                y += 1
                # What if we add a block here?
                if map[y][x] == ".":
                    map[y][x] = "#"
                    if walk_check(map, x, y - 1, "<"):
                        yield (y, x)
                map[y][x] = "v"
        elif map[y][x] == "<":
            if x == 0:
                break
            if map[y][x-1] == "#":
                # Turn right
                map[y][x] = "^"
            else:
                x -= 1
                # What if we add a block here?
                if map[y][x] == ".":
                    map[y][x] = "#"
                    if walk_check(map, x + 1, y, "^"):
                        yield (y, x)
                map[y][x] = "<"


with open("input.txt") as f:
    count = 0
    validate: bool = False
    page_order: dict[int, list[int]] = {}

    lines = f.readlines()
    map: list[str] = []
    start_x = -1
    start_y = -1
    size_x = 0
    size_y = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            break

        if "^" in line:
            start_x = line.index("^")
            start_y = size_y

        if size_y == 0:
            size_x = len(line)
        size_y += 1
        map.append([c for c in line])

    print(f"Map size: {size_x}x{size_y}")
    #solution = [(3,6), (6,7), (7,7), (1,8), (3,8), (7,9)]
    solution = False
    
    block_list = set()
    for block in walk(map, start_x, start_y):
        block_list.add(block)
        count += 1
        if solution:
            if block in solution:
                solution.remove(block)
            else:
                print(f"Block {block} not in solution")

    #print(block_list)
    print(len(block_list))