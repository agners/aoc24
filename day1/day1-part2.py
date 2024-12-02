"""Advent of Code 2024 Day 1"""

with open("input.txt") as f:
    similarity_score = 0
    lines = f.readlines()
    list1: list[int] = []
    list2: list[int] = []
    
    for line in lines:
        location1, location2 = line.split()
        list1.append(int(location1))
        list2.append(int(location2))

    list2.sort()
    dict2: dict[int, int] = {}

    for value in list2:
        dict2[value] = dict2.get(value, 0) +  value

    for value in list1:
        if value in dict2:
            print("Add to similarity score: ", dict2[value])
            similarity_score += dict2[value]

    print("Total similarity score is: ", similarity_score)

