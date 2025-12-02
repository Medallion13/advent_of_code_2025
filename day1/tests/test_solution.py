from pathlib import Path

import pytest

from day1.solution import solve_part1, solve_part2


@pytest.fixture
def sample_input_file(tmp_path: Path) -> Path:
    input_file = tmp_path / "test_input.md"
    content = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
R268"""
    input_file.write_text(content, encoding="utf-8")
    return input_file


def test_solve_part1(sample_input_file: Path):
    """Example tests"""
    result = solve_part1(sample_input_file)
    assert result == 4


def test_solve_part2(sample_input_file: Path):
    result = solve_part2(sample_input_file)
    assert result == 9
