"""Advent of Code 2024 Day 2"""


def check_report(report: list[int]) -> bool:
    """Check if levels of a report are safe"""
    prev_level = report[0]
    cur_level = report[1]
    is_increase = prev_level < cur_level
    for cur_level in report[1:]:
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
        report = [ int(level) for level in line.split(" ") ]
        if check_report(report):
            print(line.strip() + ": Safe")
            save += 1
        else:
            # Try with dampening
            for i in range(len(report)):
                if check_report(report[:i] + report[i+1:]):
                    print(line.strip() + ": Safe (dampened)")
                    save += 1
                    break
            print(line.strip() + ": Unsafe")

    print("Total safe reports: ", save)

