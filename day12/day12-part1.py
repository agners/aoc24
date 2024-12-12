"""Advent of Code 2024 Day 12 part 1"""

from dataclasses import dataclass, field

@dataclass
class AreaInfo:
    """Area information"""
    code: str
    area: int
    fence_length: int
    places: set[tuple[int, int]] = field(default_factory=set)


def map_area(map: list[str], x: int, y: int, area: AreaInfo) -> bool:
    """Find connecting area"""

    if (x, y) in area.places:
        return True

    if map[y][x] != area.code:
        return False
    
    area.area += 1
    area.places.add((x, y))
    print(x, y, area.area)
    if x == 0:
        area.fence_length += 1
    else:
        if not map_area(map, x - 1, y, area):
            area.fence_length += 1

    if y == 0:
        area.fence_length += 1
    else:
        if not map_area(map, x, y - 1, area):
            area.fence_length += 1

    if x == len(map[0]) - 1:
        area.fence_length += 1
    else:
        if not map_area(map, x + 1, y, area):
            area.fence_length += 1

    if y == len(map) - 1:
        area.fence_length += 1
    else:
        if not map_area(map, x, y + 1, area):
            area.fence_length += 1

    return True

with open("input.txt") as f:
    lines = f.readlines()
    map: list[str] = []
    size_x = 0
    size_y = 0

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            break

        if size_y == 0:
            size_x = len(line)
        size_y += 1
        map.append([c for c in line])

    print(f"Map size: {size_x}x{size_y}")
    areas: dict[tuple[int, int], AreaInfo] = {}
    price = 0
    for x in range(size_x):
        for y in range(size_y):
            if (x, y) in areas:
                continue
            area = AreaInfo(map[y][x], 0, 0)
            map_area(map, x, y, area)
            for place in area.places:
                areas[place] = area
            print (f"Area: {area.area}, Fence: {area.fence_length}")
            price += area.area * area.fence_length
    

    print(price)

