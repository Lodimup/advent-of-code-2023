"""Parse the input into game numbers, winning numbers, and hands, then check if the hand is in the winning numbers.
1 win => 1 point
more than 1 wins => 2 ** (number of hands - 1) points
"""
import re
from utils import read_input


def solution(file_path: str) -> int:
    """Solution for day 4, part 1
    Args:
        file_path (str): The input file path
    Returns:
        int: The total
    """
    data = read_input(file_path)
    total: int = 0

    for line in data:
        round_ = {}
        game_num = line \
                .split(":")[0] \
                .split(" ")[1]
        game_num = re.search(r"\d+", game_num)[0]
        game_num = int(game_num)
        round_["game_num"] = game_num

        winning_nums = line \
                .split(":")[1] \
                .split("|")[0] \
                .strip() \
                .split(" ")
        winning_nums = [num.strip() for num in winning_nums if num.strip() != ""]

        hands = line \
                .split(":")[1] \
                .split("|")[1] \
                .strip() \
                .split(" ")
        hands = [hand.strip() for hand in hands if hand.strip() != ""]
        
        wins = set(hands) & set(winning_nums)

        if len(wins) > 1:
            total += 2 ** (len(wins) - 1)
        elif len(wins) == 1:
            total += 1

    return int(total)


if __name__ == "__main__":
    print(solution("inputs/day_04_1.txt"))