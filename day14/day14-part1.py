"""Advent of Code 2024 Day 14 part 1"""

from dataclasses import dataclass

@dataclass
class Robot:
    """Robot"""
    pos: tuple[int, int]
    vel: tuple[int, int]

with open("test-data.txt") as f:
    size_x, size_y = (11, 7)
    #size_x, size_y = (101, 103)
    lines = f.readlines()

    robots: list[Robot] = []

    for line in lines:
        # Parse robot information p=0,4 v=3,-3
        pos_str, vel_str = line.split(" ")
        pos = tuple([ int(x) for x in pos_str[2:].split(",") ])
        vel = tuple([ int(x) for x in vel_str[2:].split(",") ])
        robots.append(Robot(pos, vel))

    # Move robots
    for i in range(100):
        for robot in robots:
            robot.pos = ((robot.pos[0] + robot.vel[0]) % size_x, (robot.pos[1] + robot.vel[1]) % size_y)
    
    qsize_x, qsize_y = (int((size_x - 1) / 2), int((size_y - 1) / 2))
    quadrant_starts = [(0, 0), (0, qsize_y + 1), (qsize_x + 1, 0), ((qsize_x + 1, qsize_y + 1))]
    safety_factor = 1
    for start in quadrant_starts:
        robot_count = 0
        for robot in robots:
            if robot.pos[0] >= start[0] and robot.pos[0] < start[0] + qsize_x and robot.pos[1] >= start[1] and robot.pos[1] < start[1] + qsize_y:
                robot_count+= 1
        safety_factor *= robot_count

    print(safety_factor)