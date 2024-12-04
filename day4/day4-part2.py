"""Advent of Code 2024 Day 4"""

def count_xmas(data: str) -> int:
    """Count XMAS"""
    return data.count("XMAS") + data.count("SAMX")

def check_x_mas(data: list[str]) -> bool:
    """Takes a 3x3 grid and checks if it contains XMAS"""
    if not (data[0][0] == "M" and data[1][1] == "A" and data[2][2] == "S" or data[0][0] == "S" and data[1][1] == "A" and data[2][2] == "M"):
        return False
    if not (data[2][0] == "M" and data[1][1] == "A" and data[0][2] == "S" or data[2][0] == "S" and data[1][1] == "A" and data[0][2] == "M"):
        return False
    return True

with open("input.txt") as f:
    count = 0

    lines = f.readlines()

    x_size = len(lines[0].strip())
    y_size = len(lines)

    for y in range(y_size - 2):
        for x in range(x_size - 2):
            data = []
            data.append(lines[y][x:x+3])
            data.append(lines[y+1][x:x+3])
            data.append(lines[y+2][x:x+3])
            if check_x_mas(data):
                count += 1

    print(count)

