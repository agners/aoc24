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

def get_next_page(pages: list[int], page_order: dict[int, list[int]]) -> int:
    """Get next page"""

    for i in range(len(pages)):
        if pages[i] not in page_order:
            return i
        valid = True
        for v in page_order[pages[i]]:
            for j in range(0, len(pages)):
                if i == j:
                    continue
                if pages[j] == v:
                    valid = False
        if valid:
            return i
    return -1

def fix_page_order(pages: list[int], page_order: dict[int, list[int]]) -> list[int]:
    """Fix page order"""

    new_pages: list[int] = []
    while True:
        page_index = get_next_page(pages, page_order)
        if page_index == -1:
            break
        new_pages.append(pages[page_index])
        del pages[page_index]

    return new_pages

with open("input.txt") as f:
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

            if not validate_page(pages, page_order):
                new_pages = fix_page_order(pages, page_order)
                count += new_pages[int(len(new_pages)/2)]
        

    print(count)

