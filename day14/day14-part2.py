"""Advent of Code 2024 Day 14 part 2"""

from dataclasses import dataclass

@dataclass
class Robot:
    """Robot"""
    pos: tuple[int, int]
    vel: tuple[int, int]

def print_robots(positions: dict[tuple[int, int], list[Robot]], size_x: int, size_y: int) -> None:
    """Print robots"""
    for y in range(size_y):
        line = ""
        for x in range(size_x):
            if (x, y) in positions:
                num = len(positions[(x, y)])
                if num > 9:
                    line += "X"
                else:
                    line += str(num)
            else:
                line += "."
        print(line)

def check_is_tree(positions: dict[tuple[int, int], list[Robot]]) -> bool:
    """Check if the positions are a tree"""
    for y in range(size_y):
        is_tree = True
        for x in range(37, 68, 1):
            if (x, y) not in positions:
                is_tree = False
                break
        if is_tree:
            return True
    return False

with open("input.txt") as f:
    size_x, size_y = (101, 103)
    lines = f.readlines()

    robots: list[Robot] = []
    positions: dict[tuple[int, int], list[Robot]] = {}

    for line in lines:
        # Parse robot information p=0,4 v=3,-3
        pos_str, vel_str = line.split(" ")
        pos = tuple([ int(x) for x in pos_str[2:].split(",") ])
        vel = tuple([ int(x) for x in vel_str[2:].split(",") ])
        robots.append(Robot(pos, vel))

    # Move robots
    i = 0
    # Found a bit of an arrangement at time 83, 184, 285, ...
    display = 83
    while True:
        positions = {}
        for robot in robots:
            new_pos = ((robot.pos[0] + robot.vel[0]) % size_x, (robot.pos[1] + robot.vel[1]) % size_y)
            robot.pos = new_pos
            if new_pos in positions:
                positions[new_pos].append(robot)
            else:
                positions[new_pos] = [robot]

        # Check arrangement and its multiplies
        #if i == display:
        #    print("Robots at time", i)
        #    print_robots(positions, size_x, size_y)
        #    print()
        #    display += 101
        #    import time
        #    time.sleep(0.3)
        
        # Helped me to find the tree at 7860, MIND OF BY ONE!
        
        if check_is_tree(positions):
            print("Robots at time", i)
            print_robots(positions, size_x, size_y)
            print()
            break
        i += 1
        