from utils import read_input
import re

def _map_alpha_to_digit(num: str) -> str:
    """Converts a string representation of a number to a digit.
    Args:
        num (str): String representation of a number
    Returns:
        str: Digit representation of the number.
    """
    if num in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return num

    if num == 'one':
        return '1'
    elif num == 'two':
        return '2'
    elif num == 'three':
        return '3'
    elif num == 'four':
        return '4'
    elif num == 'five':
        return '5'
    elif num == 'six':
        return '6'
    elif num == 'seven':
        return '7'
    elif num == 'eight':
        return '8'
    elif num == 'nine':
        return '9'
    elif num == 'zero':
        return '0'
    else:
        raise ValueError(f"Invalid input: {num}")


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