"""Advent of Code 2024 Day 9"""

import time

start = time.monotonic()

test_data = "2333133121414131402"

checksum = 0
pos = 0

end_pos = len(test_data) - 1

length = 0
file_id_end = -1

def get_blocks(index: int) -> tuple[int, int]:
    """Returns file id and length"""
    while index % 2 == 1:
        index -= 1
    
    return (index, int(test_data[index]))

for i in range(len(test_data)):
    if i % 2 == 0:
        file_id = int(i/2)
        if file_id == file_id_end:
            len_start = length
        else:
            len_start = int(test_data[i])
        for j in range(len_start):
            checksum += pos * file_id
            pos += 1
    else:
        for j in range(int(test_data[i])):
            if length == 0:
                end_pos, length = get_blocks(end_pos)
                file_id_end = int(end_pos/2)
                end_pos -= 1
            checksum += pos * file_id_end
            pos += 1
            length -= 1
    if end_pos < i:
        break

print(checksum)
print("Time:", time.monotonic() - start)
