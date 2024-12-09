"""Advent of Code 2024 Day 9"""

import time

start = time.monotonic()

test_data = "2333133121414131402"

data = [ int(x) for x in test_data ]

pos = 0
checksum = 0
is_file = True

moved_files = set()

def find_file(data: list[int], max_length: int, min_idx: int) -> tuple[int, int]:
    """Returns file id and length"""
    for i in range(len(data) - 1, -1, -1):
        if i < min_idx:
            break

        if i % 2 == 0:
            if i in moved_files:
                continue
            length = int(data[i])
            if length <= max_length:
                moved_files.add(i)
                return (int(i/2), length)
    return (-1, -1)

for i in range(len(data)):
    length = data[i]
    if is_file:
        file_id = int(i/2)
        if i in moved_files:
            file_id = 0
        for j in range(length):
            checksum += file_id * pos
            pos += 1
    else:
        # Not a file, free space, try to find a fitting file from the end
        while length > 0:
            file_id, file_length = find_file(data, length, i)
            if file_id == -1:
                break
            for j in range(file_length):
                checksum += file_id * pos
                length -= 1
                pos += 1
        for j in range(length):
            pos += 1
    is_file = not is_file

print()
print(checksum)
print("Time:", time.monotonic() - start)
