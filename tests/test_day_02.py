from day_02_1 import solution as part1
from day_02_2 import solution as part2


def test_part1():
    """Test part 1"""
    assert part1("tests/inputs/day_02.txt", 12, 13, 14) == 8


def test_part2():
    """Test part 2"""
    assert part2("tests/inputs/day_02.txt") == 2286
