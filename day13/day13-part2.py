"""Advent of Code 2024 Day 12 part 1"""

def parse_button(line: str) -> tuple[int, int]:
    """Parse button move"""
    data = line[10:].split(", ")
    return (int(data[0].strip()[1:]), int(data[1].strip()[1:]))

with open("test-data.txt") as f:
    lines = f.readlines()
    total_tokens = 0

    button_a_move: tuple[int, int] = (0, 0)
    button_a_price = 3
    button_b_move: tuple[int, int] = (0, 0)
    button_b_price = 1
    price_position: tuple[int, int] = (0, 0)
    for line in lines:
        if line.startswith("Button A: "):
            # Format Button A: X+94, Y+342
            button_a_move = parse_button(line)
        if line.startswith("Button B: "):
            button_b_move = parse_button(line)
        
        # Parse Price
        # Prize: X=8400, Y=5400
        if line.startswith("Prize: "):
            data = line[6:].split(", ")
            price_position = (int(data[0].strip()[2:]) + 10000000000000, int(data[1].strip()[2:]) + 10000000000000)
            #price_position = (int(data[0].strip()[2:]), int(data[1].strip()[2:]))
        
        if line.strip() == "":
            print(f"Button A: {button_a_move}")
            print(f"Button B: {button_b_move}")
            print(f"Price: {price_position}")

            # Two equations, solve by substitution
            #button_a_move[0] * button_a_count + button_b_move[0] * button_b_count = price_position[0]
            #button_a_move[1] * button_a_count + button_b_move[1] * button_b_count = price_position[1]

            button_b_count = (price_position[0] * button_a_move[1] - button_a_move[0] * price_position[1]) / (button_a_move[1] * button_b_move[0] - button_a_move[0] * button_b_move[1])
            button_a_count = (price_position[1] - button_b_move[1] * button_b_count) / button_a_move[1]
            print(button_a_count, button_b_count)
            if button_a_count % 1 != 0 or button_b_count % 1 != 0:
                continue

            print()
            button_a_count = int(button_a_count)
            button_b_count = int(button_b_count)
            tokens = button_a_count * button_a_price + button_b_count * button_b_price
            print(f"Button A: {button_a_count}, Button B: {button_b_count}, Tokens: {tokens}")
            total_tokens += tokens
    print(total_tokens)

            

