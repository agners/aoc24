"""Advent of Code 2024 Day 7"""

def find_operand(operands: list[str], test_value: int) -> bool:
    """Find the operand"""
    if len(operands) < 2:
        return False
    result = operands[0] + operands[1]
    if result == test_value and len(operands) == 2:
        return True
    else:
        new_operands = operands[1:]
        new_operands[0] = result
        if find_operand(new_operands, test_value):
            return True
    
    result = operands[0] * operands[1]
    if result == test_value and len(operands) == 2:
        return True
    else:
        new_operands = operands[1:]
        new_operands[0] = result
        if find_operand(new_operands, test_value):
            return True

    result = int(str(operands[0]) + str(operands[1]))
    if result == test_value and len(operands) == 2:
        return True
    else:
        new_operands = operands[1:]
        new_operands[0] = result
        if find_operand(new_operands, test_value):
            return True

    return False

with open("input.txt") as f:
    total = 0

    lines = f.readlines()
    
    for line in lines:
        test_value, operands = line.strip().split(":")
        operands = operands.strip().split(" ")
        test_value = int(test_value)
        if find_operand([int(operand) for operand in operands], test_value):
            total += test_value
    print(total)

    