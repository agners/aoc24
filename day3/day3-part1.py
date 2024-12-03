"""Advent of Code 2024 Day 3"""

from enum import IntEnum


class State(IntEnum):
    """State of the program"""
    READ_INSTRUCTON = 0
    FIRST_FACTOR = 1
    SECOND_FACTOR = 2

with open("input.txt") as f:
    state: State = State.READ_INSTRUCTON
    total = 0
    factor1: str = ""
    factor2: str = ""
    while True:
        char = f.read(1)          
        if not char: 
            break

        if state == State.READ_INSTRUCTON:
            factor1 = ""
            factor2 = ""
            if char == "m":
                char = f.read(1)
                if char == "u":
                    char = f.read(1)
                    if char == "l":
                        char = f.read(1)
                        if char == "(":
                            state = State.FIRST_FACTOR
                            continue
            state = State.READ_INSTRUCTON
        elif state == State.FIRST_FACTOR:
            if char.isdigit():
                factor1 += char
                continue
            elif char == ",":
                state = State.SECOND_FACTOR
                continue
            state = State.READ_INSTRUCTON
        elif state == State.SECOND_FACTOR:
            if char.isdigit():
                factor2 += char
                continue
            elif char == ")":
                # Execute multiplication
                total += int(factor1) * int(factor2)
            state = State.READ_INSTRUCTON
        
    print(total)

