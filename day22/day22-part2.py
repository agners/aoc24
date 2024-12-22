"""Advent of Code 2024 Day 22 part 2"""

def mix(secret: int, number: int) -> int:
    """Mix the secret"""
    return secret ^ number

def prune(secret: int) -> int:
    """Prune the secret"""
    return secret % 16777216

def calculate_next_secret(secret: int) -> int:
    """Calculate the next secret"""
    res1 = prune(mix(secret, secret * 64))
    res2 = prune(mix(res1, int(res1 / 32)))
    return prune(mix(res2, res2 * 2048))

def calculate_price_change_sequence(start_secret: int, iterations: int) -> dict[tuple[int, int, int, int], int]:
    """Calculate price change sequence"""
    price_for_change: dict[tuple[int, int, int, int], int] = {}
    queue = []
    for i in range(0, iterations):
        next_secret = calculate_next_secret(start_secret)
        queue.append(next_secret % 10 - start_secret % 10)
        start_secret = next_secret
        if len(queue) == 4:
            sequence = tuple(queue)
            if sequence not in price_for_change:
                price_for_change[tuple(queue)] = next_secret % 10
            queue.pop(0)
    return price_for_change

def calculate_price_for_sequence(
        sequence: tuple[int, int, int, int], 
        list_of_price_for_change: list[tuple[tuple[int, int, int, int], int]]
    ) -> int:
    """Calculate the price for a sequence"""
    price = 0
    for price_for_change in list_of_price_for_change:
        if sequence in price_for_change:
            price += price_for_change[sequence]
    return price


with open("test-data.txt") as f:
    lines = f.readlines()

    #print(calculate_price_change_sequence(123, 10))
    
    # Calculate list of sequences and their associated price
    list_of_changes: list[dict[tuple[int, int, int, int], int]] = []
    for line in lines:
        start_secret = int(line.strip())
        price_for_change = calculate_price_change_sequence(start_secret, 2000)
        list_of_changes.append(price_for_change)

    best_sequence = (0, 0, 0, 0)
    best_value = 0
    for c1 in range(-9, 10):
        for c2 in range(-9, 10):
            for c3 in range(-9, 10):
                for c4 in range(-9, 10):
                    sequence = (c1, c2, c3, c4)
                    value = 0
                    for changes in list_of_changes:
                        if sequence in changes:
                            value += changes[sequence]
                    if value > best_value:
                        best_value = value
                        best_sequence = sequence
                    
    print(f"Best sequence is {best_sequence} with value {best_value}")
