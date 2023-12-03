"""
This is the solution for day 2, part 1.
This problems seems like a good candidate for OOP. There are 3 kinds of entities:
- Game: A game consists of multiple rounds
- GameRound: A game round consists of multiple hands
- Bag: A bag consists of red, green, and blue cubes
Let's create classes for each of these entities, so we can hold data and perform operations on them.
"""

from typing import List
from utils import read_input


class GameRound:
    """A game round
    Args:
        red (int): Number of red cubes drawn
        green (int): Number of green cubes drawn
        blue (int): Number of blue cubes drawn
    """

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"GameRound({self.red}, {self.green}, {self.blue})"

    def __str__(self):
        return self.__repr__()


class Game:
    """A game
    Args:
        data (str): The input data eg.
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    """

    def __init__(self, data: str):
        self.data = data

        self.rounds = self.parse_rounds()

    @property
    def game_num(self) -> int:
        """Returns the game_number
        Just to demonstrate @property, this is calculated each time it is called
        Wastes CPU juice in this case
        """
        return int(self.data.split(":")[0].split(" ")[-1])

    def parse_rounds(self) -> List[GameRound]:
        """Returns the rounds
        Just to demonstrate __init__, this is calculated once when the object is created
        Saves CPU juice in this case
        """
        rounds = []
        for round_ in self.data.split(":")[1].split(";"):
            red: int = 0
            green: int = 0
            blue: int = 0

            round_ = round_.strip()
            if round_ == "":
                continue
            hands = round_.split(",")
            for hand in hands:
                hand = hand.strip()
                if "red" in hand:
                    red = int(hand.split(" ")[0])
                elif "green" in hand:
                    green = int(hand.split(" ")[0])
                elif "blue" in hand:
                    blue = int(hand.split(" ")[0])
            rounds.append(GameRound(int(red), int(green), int(blue)))

        return rounds

    def __len__(self):
        return len(self.rounds)

    def __repr__(self):
        return f"Game({self.data})"

    def __str__(self):
        return self.__repr__()


class Bag:
    """A bag of red, green, and blue cubes"""

    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

    def is_game_possible(self, game_round: GameRound) -> bool:
        """Checks if the game is possible"""
        if game_round.red > self.red:
            return False
        elif game_round.green > self.green:
            return False
        elif game_round.blue > self.blue:
            return False

        return True

    def __repr__(self):
        return f"Bag({self.red}, {self.green}, {self.blue})"

    def __str__(self):
        return self.__repr__()


def solution(
    file_path: str,
    bag_red: int,
    bag_green: int,
    bag_blue: int,
):
    """Solution for day 2, part 1
    - Create a Bag
    - Create a Game
    - Check if the game is possible by checking if the bag has enough cubes for each round
    - A game is not possible if one of the rounds is not possible
    - if the add the game's game_num to the total
    Args:
        data (str): The input data eg.
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
            Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
            Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
            Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
            Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
            "
    Returns:
        int: sum of the game numbers that are possible
    """
    total: int = 0

    data = read_input(file_path)
    bag = Bag(bag_red, bag_green, bag_blue)
    for line in data:
        game = Game(line)
        check_possibles: List[bool] = []  # list comprehension is possible but not as efficient
        for round_ in game.rounds:
            is_possible = bag.is_game_possible(round_)
            if not is_possible:
                check_possibles.append(is_possible)
                break
            check_possibles.append(is_possible)
        if all(check_possibles):
            total += game.game_num

    return total


if __name__ == "__main__":
    print(solution("inputs/day_02_1.txt", 12, 13, 14))
