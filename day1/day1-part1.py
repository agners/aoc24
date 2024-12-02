"""Advent of Code 2024 Day 1"""

with open("input.txt") as f:
    distance = 0
    lines = f.readlines()
    list1: list[int] = []
    list2: list[int] = []
    
    for line in lines:
        location1, location2 = line.split()
        list1.append(int(location1))
        list2.append(int(location2))

    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        distance += abs(list1[i] - list2[i])

    print("Total distance is: ", distance)

