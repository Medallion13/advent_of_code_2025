from pathlib import Path


def solve_part1(filepath: Path) -> int:
    # define the start point in 50
    start_point: int = 50
    instruction_list: list[str]
    count: int = 0

    # Get all the values from the document and split with the line breaks
    with open(filepath, encoding="utf-8") as file:
        content = file.read()
        instruction_list = content.splitlines()

    # Go throw every instruction
    for instruction in instruction_list:
        # transform the end part of the string into a number
        value = int(instruction[1:])

        # Check if i go left (-) or if I go right (+)
        if instruction[0:1] == "L":
            start_point -= value
        else:
            start_point += value

        if start_point == 0 or abs(start_point) % 100 == 0:
            count += 1

    return count


def solve_part2(filepath: Path) -> int:
    # define the start point in 50
    current_pos: int = 50
    distance_to_cero = 100  # max distance
    instruction_list: list[str]
    count: int = 0

    # Get all the values from the document and split with the line breaks
    with open(filepath, encoding="utf-8") as file:
        content = file.read()
        instruction_list = content.splitlines()

    for instruction in instruction_list:
        direction = instruction[0]
        aument = int(instruction[1:])

        if direction == "R":
            distance_to_cero = (
                100 - current_pos
            ) % 100  # how far I am from the 0 in opposite direction
            current_pos = (current_pos + aument) % 100  # Move to rigth ew position
        else:
            distance_to_cero = current_pos % 100  # This time the distance is the current position
            current_pos = (current_pos - aument) % 100  # Move to left to new position

        if distance_to_cero == 0:  # I'm in 0
            distance_to_cero = 100  # have to come back to 0

        # check if i cross 0
        if aument >= distance_to_cero:
            # Get the number of turns for values greater than 100
            turns = (aument - distance_to_cero) // 100
            count += 1 + turns

    return count


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    sample_input = script_dir / "input.md"
    print(f"the password for part 1 is: {solve_part1(sample_input)} \n")
    print(f"the password for part 2 is: {solve_part2(sample_input)}")
