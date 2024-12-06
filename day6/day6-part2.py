"""Advent of Code 2024 Day 5"""

def walk(map: list[str], start_X: int, start_y: int):
    """Walk on the map"""
    block_count = 0
    use_block = False
    use_block_next = False
    size_x = len(map[0])
    size_y = len(map)
    x = start_X
    y = start_y
    while True:
        if map[y][x] == "^":
            if y == 0:
                map[y][x] = "^"
                break
            if map[y-1][x] == "#":
                # Turn right
                map[y][x] = ">"
                use_block = False
            else:
                if use_block_next:
                    block_count += 1
                    use_block_next = False
                    print(f"Block at {x}, {y}")
                map[y][x] = "^"
                y -= 1
                for i in range(x, size_x):
                    if map[y][i] == ">":
                        use_block_next = True
                map[y][x] = "^"
        elif map[y][x] == ">":
            if x == size_x - 1:
                map[y][x] = ">"
                break
            if map[y][x+1] == "#":
                # Turn right
                map[y][x] = "v"
                use_block = False
            else:
                if use_block_next:
                    block_count += 1
                    use_block_next = False
                    print(f"Block at {x}, {y}")
                map[y][x] = ">"
                x += 1
                for i in range(y, size_y):
                    if map[i][x] == "v":
                        use_block_next = True
                map[y][x] = ">"
        elif map[y][x] == "v":
            if y == size_y - 1:
                map[y][x] = "v"
                break
            if map[y+1][x] == "#":
                # Turn right
                map[y][x] = "<"
                use_block = False
            else:
                if use_block_next:
                    block_count += 1
                    use_block_next = False
                    print(f"Block at {x}, {y}")
                map[y][x] = "v"
                y += 1
                for i in range(0, x + 1):
                    if map[y][i] == "<":
                        use_block_next = True
                map[y][x] = "v"
        elif map[y][x] == "<":
            if x == 0:
                map[y][x] = "<"
                break
            if map[y][x-1] == "#":
                # Turn right
                map[y][x] = "^"
                use_block = False
            else:
                if use_block_next:
                    block_count += 1
                    use_block_next = False
                    print(f"Block at {x}, {y}")
                map[y][x] = "<"
                x -= 1
                for i in range(0, y + 1):
                    if map[i][x] == "^":
                        use_block_next = True
                map[y][x] = "<"
    print(f"Block count: {block_count}")    


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
    walk(map, start_x, start_y)
    for line in map:
        for c in line:
            if c == "O":
                count += 1
    

    print(count)

