from day_03_1 import solution as part1
from day_03_2 import solution as part2


def test_part1():
    """Test part 1"""
    assert part1("tests/inputs/day_03.txt") == 4361

def test_part2():
    """Test part 2"""
    assert part2("tests/inputs/day_03.txt") == 467835