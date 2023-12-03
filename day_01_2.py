import re
from utils import read_input

def _map_alpha_to_digit(num: str) -> str:
    """Converts a string representation of a number to a digit.
    Args:
        num (str): String representation of a number
    Returns:
        str: Digit representation of the number.
    Raises:
        ValueError: If the input is not a valid number string.
    """
    TABLE = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0'
    }

    if num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return num

    ret = TABLE.get(num, None)
    if ret is None:
        raise ValueError(f"Invalid input: {num}")
    
    return ret


def solution(file_path: str) -> int:
    """Solution for day 01 part 2
    - parse the input file to array of digits
    - take the first and last digits
    - add the two digits together
    - convert to int

    ?= in regex is a lookahead assertion. This means that the regex will match overlapping patterns.

    Args:
        file_path (str): Path to the input file.
    Returns:
        int: Solution to the problem.
    """
    total: int = 0

    data = read_input(file_path)

    for line in data:
        regex = r"(?=(\d|one|two|three|four|five|six|seven|eight|nine|zero))"
        nums = re.findall(regex, line)
        first_num: str = nums[0]
        last_num: str = nums[-1]
        total += int(_map_alpha_to_digit(first_num) + _map_alpha_to_digit(last_num))

    return total


if __name__ == "__main__":
    print(solution("inputs/day_01_2.txt"))