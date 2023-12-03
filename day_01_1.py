import re
from utils import read_input

def solution(file_path: str) -> int:
    """Solution for day 01 part 1
    - parse the input file to array of digits
    - take the first and last digits
    - add the two digits together
    - convert to int
    - add to total
    Args:
        file_path (str): Path to the input file.
    Returns:
        int: Solution to the problem.
    """
    total: int = 0

    data = read_input(file_path)
    
    for line in data:
        nums = [char for char in line if char.isdigit()]
        nums = nums[0] + nums[-1]
        total += int("".join(nums))
    
    return total


def solution2(file_path: str) -> int:
    """Alternative solution for day 01 part 1
    """
    total: int = 0

    data = read_input(file_path)

    for line in data:
        regex = r"\d"
        nums = re.findall(regex, line)
        first_num: str = nums[0]
        last_num: str = nums[-1]
        total += int(first_num + last_num)

    return total

if __name__ == "__main__":
    print(solution("inputs/day_01_1.txt"))
    print(solution2("inputs/day_01_1.txt"))