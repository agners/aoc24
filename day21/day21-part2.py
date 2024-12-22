"""Advent of Code 2024 Day 21 part 2"""

from itertools import permutations

"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+
"""

from enum import IntEnum

class Direction(IntEnum):
    """Direction"""
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    ACTIVATE = 10
    FORBIDDEN = 11


def validate_sequence(sequence: list[int], start_x: int, start_y: int, forbidden_x: int, forbidden_y: int) -> bool:
    """Make sure we don't hit the forbidden field"""
    for digit in sequence:
        if digit == Direction.UP:
            start_y -= 1
        elif digit == Direction.DOWN:
            start_y += 1
        elif digit == Direction.LEFT:
            start_x -= 1
        elif digit == Direction.RIGHT:
            start_x += 1
        if start_x == forbidden_x and start_y == forbidden_y:
            return False
    return True

def list_sequences(start_x: int, start_y: int, end_x: int, end_y: int) -> set[list[Direction]]:
    """Find shortest sequences"""
    sequence = []
    while start_x < end_x:
        start_x += 1
        sequence.append(Direction.RIGHT)
    while start_x > end_x:
        start_x -= 1
        sequence.append(Direction.LEFT)
    while start_y > end_y:
        start_y -= 1
        sequence.append(Direction.UP)
    while start_y < end_y:
        start_y += 1
        sequence.append(Direction.DOWN)
    return map(list, set(permutations(sequence)))

def list_sequences_by_button(keypad_positions: dict[int, tuple[int, int]], start: int, end: int) -> set[list[Direction]]:
    start_x, start_y = keypad_positions[start]
    end_x, end_y = keypad_positions[end]
    forbidden_x, forbidden_y = keypad_positions[Direction.FORBIDDEN]
    for sequence in list_sequences(start_x, start_y, end_x, end_y):
        if validate_sequence(sequence, start_x, start_y, forbidden_x, forbidden_y):
            yield sequence

def generate_paths_for_keypad(keypad_positions: dict[int, tuple[int, int]], sequence: list[int]):
    """Generate paths"""
    start = Direction.ACTIVATE
    for end in sequence:
        paths = []
        for path in list_sequences_by_button(keypad_positions, start, end):
            path.append(Direction.ACTIVATE)
            paths.append(path)
        yield paths
        start = end


keypad_numeric = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, Direction.ACTIVATE]
]
keypad_numeric_positions = {
    7: (0, 0),
    8: (1, 0),
    9: (2, 0),
    4: (0, 1),
    5: (1, 1),
    6: (2, 1),
    1: (0, 2),
    2: (1, 2),
    3: (2, 2),
    Direction.FORBIDDEN: (0, 3),
    0: (1, 3),
    Direction.ACTIVATE: (2, 3)
}

keypad_directional = [
    [ None, Direction.UP, Direction.ACTIVATE ],
    [ Direction.LEFT, Direction.DOWN, Direction.RIGHT ]
]
keypad_directional_positions = {
    Direction.FORBIDDEN: (0, 0),
    Direction.UP: (1, 0),
    Direction.ACTIVATE: (2, 0),
    Direction.LEFT: (0, 1),
    Direction.DOWN: (1, 1),
    Direction.RIGHT: (2, 1),
}

cache: dict = {}

def find_shortest_path_directional(sequence: list[int], nesting: int) -> int:
    """Shortest path"""
    nesting -= 1
    total_shortest_path = 0
    for paths in generate_paths_for_keypad(keypad_directional_positions, sequence):
        shortest_path = 999999999999999999
        for path in paths:
            if nesting == 0:
                overall_path_len = len(path)
            else:
                sequence_tuple = tuple(path)
                if (sequence_tuple, nesting) in cache:
                    overall_path_len = cache[(sequence_tuple, nesting)]
                else:
                    overall_path_len = find_shortest_path_directional(path, nesting)
                    cache[(sequence_tuple, nesting)] = overall_path_len
            if overall_path_len < shortest_path:
                shortest_path = overall_path_len
        total_shortest_path += shortest_path
    return total_shortest_path

def find_shortest_path_numeric(sequence: list[int], num_directional_keypads: int) -> int:
    """Shortest path"""
    total_shortest_path = 0
    for paths in generate_paths_for_keypad(keypad_numeric_positions, sequence):
        shortest_path = 999999999999999999
        for path in paths:
            overall_path_len = find_shortest_path_directional(path, num_directional_keypads)
            if overall_path_len < shortest_path:
                shortest_path = overall_path_len
        total_shortest_path += shortest_path
    return total_shortest_path

with open("test-data.txt") as f:
    sum_complexity = 0
    keypads: list = []
    keypads.append(keypad_numeric_positions)
    for i in range(25):
        keypads.append(keypad_directional_positions)
    for line in f:
        sequence_str = line.strip()
        print(f"Sequence Numpad: {sequence_str}")
        sequence: list[int] = []
        for digit in sequence_str:
            if digit == "A":
                digit = Direction.ACTIVATE
            sequence.append(int(digit))

        # Numeric pad...
        total_shortest_path_num = find_shortest_path_numeric(sequence, 25)
        sum_complexity += total_shortest_path_num * int(sequence_str[:-1])
        print("Shortest path: ", total_shortest_path_num)

    print("Sum complexity: ", sum_complexity)

