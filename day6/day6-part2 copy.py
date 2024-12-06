"""Advent of Code 2024 Day 6"""

from collections.abc import Iterator

def walk_check(map: list[str], start_X: int, start_y: int, direction: str) -> bool:
    """Walk on the map and check if this would lead to a loop"""
    size_x = len(map[0])
    size_y = len(map)
    x = start_X
    y = start_y
    while True:
        if direction == "^":
            if y == 0:
                return False
            if map[y-1][x] == "#":
                # We've been here before? Yes, we have a loop
                if map[y][x] == ">":
                    return True
                # Turn right and keep going
                direction = ">"
            else:
                y -= 1
        elif map[y][x] == ">":
            if x == size_x - 1:
                return False
            if map[y][x+1] == "#":
                # We've been here before? Yes, we have a loop
                if map[y][x] == "v":
                    return True
                # Turn right and keep going
                direction = "v"
            else:
                x += 1
        elif map[y][x] == "v":
            if y == size_y - 1:
                return False
            if map[y+1][x] == "#":
                # We've been here before? Yes, we have a loop
                if map[y][x] == "<":
                    return True
                # Turn right and keep going
                direction = "<"
            else:
                y += 1
        elif map[y][x] == "<":
            if x == 0:
                return False
            if map[y][x-1] == "#":
                # We've been here before? Yes, we have a loop
                if map[y][x] == "^":
                    return True
                # Turn right and keep going
                direction = "^"
            else:
                x -= 1


def walk(map: list[str], start_X: int, start_y: int) -> Iterator[tuple[int, int]]:
    """Walk on the map"""
    size_x = len(map[0])
    size_y = len(map)
    x = start_X
    y = start_y
    block_count = 0
    while True:
        if map[y][x] == "^":
            if y == 0:
                map[y][x] = "^"
                break
            if map[y-1][x] == "#":
                # Turn right
                map[y][x] = ">"
                use_block_next = False
            else:
                map[y][x] = "^"
                y -= 1
                if walk_check(map, x, y, "^"):
                    yield (x, y)

                for i in range(x, size_x):
                    if map[y][i] in ">":
                        use_block_next = True
                    elif map[y][i] == "v" and map[y][i+1] == "#":
                        use_block_next = True
                    if map[y][i] == "#":
                        break
                map[y][x] = "^"
        elif map[y][x] == ">":
            if x == size_x - 1:
                map[y][x] = ">"
                break
            if map[y][x+1] == "#":
                # Turn right
                map[y][x] = "v"
                use_block_next = False
            else:
                map[y][x] = ">"
                x += 1
                if use_block_next:
                    yield (x, y)
                    use_block_next = False
                for i in range(y, size_y):
                    if map[i][x] == "v":
                        use_block_next = True
                    elif map[i][x] == "<" and map[i+1][x] == "#":
                        use_block_next = True
                    if map[i][x] == "#":
                        break
                map[y][x] = ">"
        elif map[y][x] == "v":
            if y == size_y - 1:
                map[y][x] = "v"
                break
            if map[y+1][x] == "#":
                # Turn right
                map[y][x] = "<"
                use_block_next = False
            else:
                map[y][x] = "v"
                y += 1
                if use_block_next:
                    yield (x, y)
                    use_block_next = False
                for i in range(x, -1, -1):
                    if map[y][i] == "<":
                        use_block_next = True
                    elif map[y][i] == "^" and map[y][i-1] == "#":
                        use_block_next = True
                    if map[y][i] == "#":
                        break
                map[y][x] = "v"
        elif map[y][x] == "<":
            if x == 0:
                map[y][x] = "<"
                break
            if map[y][x-1] == "#":
                # Turn right
                map[y][x] = "^"
                use_block_next = False
            else:
                map[y][x] = "<"
                x -= 1
                if use_block_next:
                    yield (x, y)
                    use_block_next = False
                for i in range(y, -1, -1):
                    if map[i][x] == "^":
                        use_block_next = True
                    elif map[i][x] == ">" and map[i-1][x] == "#":
                        use_block_next = True
                    if map[i][x] == "#":
                        break
                map[y][x] = "<"

        if use_block_next:
            block_count += 1
            print(f"Block at {x}, {y}")
            if block_count == 2:
                for line in map:
                    print("".join(line))
                break


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
    solution = [(3,6), (6,7), (7,7), (1,8), (3,8), (7,9)]
    for block in walk(map, start_x, start_y):
        print(block)
        if block in solution:
            del solution[solution.index(block)]
        else:
            print(f"Block {block} not in solution")
        count += 1


    for line in map:
        for c in line:
            if c == "O":
                count += 1
    

    print(count)

