"""Advent of Code 2024 Day 12 part 2"""

from dataclasses import dataclass, field
from enum import IntEnum
import time

class Direction(IntEnum):
    """Direction"""
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

@dataclass
class AreaInfo:
    """Area information"""
    code: str
    area: int
    fence_length: int
    fence_sides: int
    places: set[tuple[int, int]] = field(default_factory=set)
    fences: dict[Direction, set[tuple[int, int]]] = field(default_factory=lambda: {Direction.UP: set(), Direction.DOWN: set(), Direction.LEFT: set(), Direction.RIGHT: set()})

def find_sides(map: list[str], area: AreaInfo, direction: Direction) -> None:
    """Find the sides of this area"""
    fences: set[tuple[int, int]] = area.fences[direction]

    while len(fences) > 0:
        current = fences.pop()
        if direction == Direction.UP or direction == Direction.DOWN:
            area.fence_sides += 1
            # Remove all connecting places
            x = current[0] + 1
            while (x, current[1]) in fences:
                fences.remove((x, current[1]))
                x += 1
            x = current[0] - 1
            while (x, current[1]) in fences:
                fences.remove((x, current[1]))
                x -= 1
        else:
            area.fence_sides += 1
            # Remove all connecting places
            y = current[1] + 1
            while (current[0], y) in fences:
                fences.remove((current[0], y))
                y += 1
            y = current[1] - 1
            while (current[0], y) in fences:
                fences.remove((current[0], y))
                y -= 1

def map_area(map: list[str], x: int, y: int, area: AreaInfo) -> bool:
    """Find connecting area"""

    if (x, y) in area.places:
        return True

    if map[y][x] != area.code:
        return False
    
    area.area += 1
    area.places.add((x, y))

    if x == 0:
        area.fence_length += 1
        area.fences[Direction.LEFT].add((x, y))
    else:
        if not map_area(map, x - 1, y, area):
            area.fence_length += 1
            area.fences[Direction.LEFT].add((x, y))

    if y == 0:
        area.fence_length += 1
        area.fences[Direction.UP].add((x, y))
    else:
        if not map_area(map, x, y - 1, area):
            area.fence_length += 1
            area.fences[Direction.UP].add((x, y))

    if x == len(map[0]) - 1:
        area.fence_length += 1
        area.fences[Direction.RIGHT].add((x, y))
    else:
        if not map_area(map, x + 1, y, area):
            area.fence_length += 1
            area.fences[Direction.RIGHT].add((x, y))

    if y == len(map) - 1:
        area.fence_length += 1
        area.fences[Direction.DOWN].add((x, y))
    else:
        if not map_area(map, x, y + 1, area):
            area.fence_length += 1
            area.fences[Direction.DOWN].add((x, y))

    return True

with open("test-data3.txt") as f:
    lines = f.readlines()
    map: list[str] = []
    size_x = 0
    size_y = 0


    start = time.monotonic()
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
            area = AreaInfo(map[y][x], 0, 0, 0)
            map_area(map, x, y, area)
            for place in area.places:
                areas[place] = area

            for direction in Direction:
                find_sides(map, area, direction)
            print (f"Area: {area.area}, Fence: {area.fence_length}, Sides: {area.fence_sides}")
            price += area.area * area.fence_sides
    
    print("Time:", time.monotonic() - start)

    print(price)

