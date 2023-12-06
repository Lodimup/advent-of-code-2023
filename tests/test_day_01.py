from day_01_1 import solution as part_1
from day_01_1 import solution2 as part_1_2
from day_01_2 import solution as part_2

def test_part1():
    """Test part 1"""
    assert part_1("tests/inputs/day_01.txt") == 142

def test_part1_2():
    """Test part 1's alternate solution"""
    assert part_1_2("tests/inputs/day_01.txt") == 142

def test_part2():
    """Test part 2"""
    assert part_2("tests/inputs/day_01_2.txt") == 281