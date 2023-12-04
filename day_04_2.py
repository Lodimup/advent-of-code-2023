"""If there is a winning number on a card, the next card(s) is duplicated and added to the end of the list.
Then, count the number of cards in the list.
"""
import re
from functools import lru_cache
from utils import read_input

@lru_cache(maxsize=None)  # this line speeds up the function by caching the results; speed improvement 0m24.522s -> 0m0.647s
def parse_data(data: str) -> tuple[int, int]:
    """Parse data into Card
    Args:
        data (str): The data to parse
    Returns:
        tuple[int, int]: The card number and number of wins
    """
    card_num = data \
            .split(":")[0]
    
    card_num = re.search(r"\d+", card_num)[0]
    card_num = int(card_num)

    winning_nums = data \
            .split(":")[1] \
            .split("|")[0] \
            .strip() \
            .split(" ")
    winning_nums = [num.strip() for num in winning_nums if num.strip() != ""]

    hands = data \
            .split(":")[1] \
            .split("|")[1] \
            .strip() \
            .split(" ")
    hands = [hand.strip() for hand in hands if hand.strip() != ""]
    num_of_wins = len(set(hands) & set(winning_nums))
    
    return card_num, num_of_wins


def solution(file_path: str) -> int:
    """Solution to day 4 part 2.
    Args:
        file_path (str): The input file path
    Returns:
        int: The total
    """
    data = read_input(file_path)
    for line in data:
        card_num, num_of_wins = parse_data(line)
        if num_of_wins > 0:
            for i in range(num_of_wins):
                try:
                    data.append(data[card_num + i])
                except IndexError:
                    pass
    
    return len(data)


if __name__ == "__main__":
    print(solution("inputs/day_04_2.txt"))