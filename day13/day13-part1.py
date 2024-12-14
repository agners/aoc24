"""Advent of Code 2024 Day 13 part 1"""



def parse_button(line: str) -> tuple[int, int]:
    """Parse button move"""
    data = line[10:].split(", ")
    return (int(data[0].strip()[1:]), int(data[1].strip()[1:]))

with open("input.txt") as f:
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
            print(line)
            button_a_move = parse_button(line)
        if line.startswith("Button B: "):
            print(line)
            button_b_move = parse_button(line)
        
        # Parse Price
        # Prize: X=8400, Y=5400
        if line.startswith("Prize: "):
            print(line)
            data = line[6:].split(", ")
            price_position = (int(data[0].strip()[2:]), int(data[1].strip()[2:]))
        
        if line.strip() == "":
            print(f"Button A: {button_a_move}")
            print(f"Button B: {button_b_move}")
            print(f"Price: {price_position}")

            for button_b in range(100 + 1):
                for button_a in range(100 + 1):

                    if button_a * button_a_move[0] + button_b * button_b_move[0] == price_position[0] and button_a * button_a_move[1] + button_b * button_b_move[1] == price_position[1]:
                        tokens = button_a * button_a_price + button_b * button_b_price
                        print(f"Button A: {button_a}, Button B: {button_b}, Tokens: {tokens}")
                        total_tokens += button_a * button_a_price + button_b * button_b_price
                        break
    print(total_tokens)

            

