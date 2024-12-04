"""Advent of Code 2024 Day 4"""

def generate_string_forward(lines: list[str]) -> str:
    """Generate a string"""
    searchstring = ""
    for line in lines:
        searchstring += line.strip() + "."
    return searchstring

def generate_string_downwards(lines: list[str]) -> str:
    """Generate a string"""
    searchstring = ""
    for i in range(len(lines[0]) - 1):
        for line in lines:
            searchstring += line[i]
        searchstring += "."
    return searchstring

def generate_string_diagonal_left_right(lines: list[str]) -> str:
    """Generate a string"""
    searchstring = ""

    x_size = len(lines[0].strip())
    y_size = len(lines)

    for i in range(x_size):
        for j in range(y_size - i):
            searchstring += lines[j][i + j]
        searchstring += "."
    
    for i in range(1, y_size):
        for j in range(x_size - i):
            searchstring += lines[i + j][j]
        searchstring += "."

    return searchstring

def generate_string_diagonal_right_left(lines: list[str]) -> str:
    """Generate a string"""
    searchstring = ""

    x_size = len(lines[0].strip())
    y_size = len(lines)

    for j in range(y_size):
        for i in range(x_size - j):
            searchstring += lines[y_size - j - i - 1][i]
        searchstring += "."

    for i in range(1, x_size):
        for j in range(y_size - i):
            searchstring += lines[y_size - j - 1][i + j]
        searchstring += "."
    

    return searchstring

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

