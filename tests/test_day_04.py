from day_04_1 import solution as part1
from day_04_2 import solution as part2


def test_part1():
    """Test part 1"""
    assert part1("tests/test_day_04_1.txt") == 13


def test_part2():
    """Test part 2"""
    assert part2("tests/test_day_04_2.txt") == 30
