"""Advent of Code 2024 Day 11 part 2"""

import time
from typing import Generator

start = time.monotonic()

stone_str = "125 17"

stones = [int(x) for x in stone_str.split()]

solution: dict[(int, int), int] = {}

def blink(stone: int, iteration: int) -> int:
    """Transform stone for one blink"""

    if (stone, iteration) in solution:
        return solution[(stone, iteration)]

    if iteration == 0:
        return 1

    if stone == 0:
        return blink(1, iteration - 1)
    else:
        num = stone
        count = 0
        while num > 0:
            num //= 10  # Perform integer division by 10
            count += 1
        if count % 2 == 0:
            split_at = count // 2
            stone_str = str(stone)
            count = blink(int(stone_str[:split_at]), iteration - 1)
            count += blink(int(stone_str[split_at:]), iteration - 1)
            if (stone, iteration) not in solution:
                solution[(stone, iteration)] = count
            return count
        else:
            return blink(stone * 2024, iteration - 1)

total_stones = 0
for stone in stones:
    #print("Stone", stone)
    total_stones += blink(stone, 75)

print("Total Stones:", total_stones)

print("Time:", time.monotonic() - start)



