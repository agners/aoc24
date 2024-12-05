"""Advent of Code 2024 Day 5"""

def validate_page(pages: list[int], page_order: dict[int, list[int]]) -> bool:
    """Validate page order"""


    for i in range(len(pages) - 1):
        if pages[i] not in page_order:
            continue
        for v in page_order[pages[i]]:
            for j in range(i, len(pages)):
                if pages[j] == v:
                    return False
    return True

with open("test-data.txt") as f:
    count = 0
    validate: bool = False
    page_order: dict[int, list[int]] = {}

    lines = f.readlines()        

    for line in lines:
        line = line.strip()
        if len(line) == 0:
            print("Start validating")
            validate = True
            continue

        if not validate:
            before, after = line.split("|")
            if page_order.get(int(after)) is None:
                page_order[int(after)] = []
            page_order[int(after)].append(int(before))
        else:
            pages: list[int] = []
            for value in line.split(","):
                pages.append(int(value))
            
            is_valid: bool = True
            
            if validate_page(pages, page_order):
                count += pages[int(len(pages)/2)]
        

    print(count)

