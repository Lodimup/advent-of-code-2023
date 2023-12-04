"""Part 2 is very simple. We just need to find the maximum number of cubes foreach round
and multiply them together. Then add them all up.
Since we already have the Game class, we can just use that.
"""

from day_02_1 import Game
from utils import read_input


def solution(file_path: str) -> int:
    """Solution for day 2, part 2
    """
    total: int = 0

    data = read_input(file_path)
    games = [Game(d) for d in data]

    for game in games:
        red: int = 0
        green: int = 0
        blue: int = 0
        for round_ in game.rounds:
            if round_.red > red:
                red = round_.red
            if round_.green > green:
                green = round_.green
            if round_.blue > blue:
                blue = round_.blue
        power = red * green * blue
        total += power

    return total


if __name__ == "__main__":
    print(solution("inputs/day_02_2.txt"))