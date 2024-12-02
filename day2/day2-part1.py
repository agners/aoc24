"""Advent of Code 2024 Day 2"""


def check_report(data: str) -> bool:
    """Check if levels of a report are safe"""
    levels = data.split(" ")
    prev_level = int(levels[0])
    cur_level = int(levels[1])
    is_increase = prev_level < cur_level
    for level in levels[1:]:
        cur_level = int(level)
        diff = cur_level - prev_level
        if is_increase and diff < 0:
            return False
        elif not is_increase and diff > 0:
            return False

        change = abs(diff)
        if change < 1 or change > 3:
            return False
        prev_level = cur_level

    return True

with open("input.txt") as f:
    save = 0
    lines = f.readlines()
    
    for line in lines:
        if check_report(line):
            print(line.strip() + ": Safe")
            save += 1
        else:
            print(line.strip() + ": Unafe")
        print("Total safe reports: ", save)

