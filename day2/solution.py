import re
from pathlib import Path


def check_if_not_valid(value: str) -> bool:
    length = len(value)
    if length % 2 != 0:
        return False

    if value[: length // 2] == value[length // 2 :]:
        return True
    return False


def solve_part1(filepath: Path) -> None:
    range_list: list[str] = []
    total: int = 0
    with open(filepath, encoding="utf-8") as file:
        content = file.read()
        range_list = content.split(",")

    ids_to_check = map(lambda ids: ids.split("-"), range_list)

    for ids in ids_to_check:
        for value in range(int(ids[0]), int(ids[1]) + 1):
            if check_if_not_valid(str(value)):
                total += value

    print(total)


def check_if_not_valid_2(value: str) -> bool:
    substring = re.match(r"^(.+?)\1+$", value)
    if substring:
        return True

    return False


def solve_part2(filepath: Path) -> None:
    range_list: list[str] = []
    total: int = 0
    with open(filepath, encoding="utf-8") as file:
        content = file.read()
        range_list = content.split(",")

    ids_to_check = map(lambda ids: ids.split("-"), range_list)

    for ids in ids_to_check:
        for value in range(int(ids[0]), int(ids[1]) + 1):
            if check_if_not_valid_2(str(value)):
                total += value

    print(total)


if __name__ == "__main__":
    script_dir = Path(__file__).parent
    sample_input = script_dir / "input.txt"
    solve_part1(sample_input)
    solve_part2(sample_input)
