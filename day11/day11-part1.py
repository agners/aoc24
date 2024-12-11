"""Advent of Code 2024 Day 11 part 1"""

import time
from typing import Generator

start = time.monotonic()

stone_str = "125 17"

stones = [int(x) for x in stone_str.split()]

def blink(stones: list[int]) -> list[int]:
    """Transform stone for one blink"""
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == 0:
            new_stones.append(1)
        elif len(str(stones[i])) % 2 == 0:
            split_at = len(str(stones[i])) // 2
            new_stones.append(int(str(stones[i])[:split_at]))
            new_stones.append(int(str(stones[i])[split_at:]))
        else:
            new_stones.append(stones[i] * 2024)
    return new_stones

for i in range(25):
    stones = blink(stones)
print("Stones:", stones)
print("Stone count", len(stones))


print("Time:", time.monotonic() - start)



