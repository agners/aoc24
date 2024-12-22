"""Advent of Code 2024 Day 22 part 1"""

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

def calculate_secret_iterations(start_secret: int, iterations: int) -> int:
    """Calculate the secret iterations"""
    secret = start_secret
    for i in range(0, iterations):
        secret = calculate_next_secret(secret)
        #print(f"{secret}")
    return secret


with open("input.txt") as f:
    lines = f.readlines()

    #calculate_secret_iterations(123, 10)
    total_price = 0
    for line in lines:
        start_secret = int(line.strip())
        total_price += calculate_secret_iterations(start_secret, 2000)
    
    print(f"Total price: {total_price}")



