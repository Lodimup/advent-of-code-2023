"""Parse the input into Nums and Symbols, then check if the symbol is adjacent to the number.
"""
from typing import List, Tuple
from utils import read_input


class Num:
    """Represents a number
    Args:
        value (str): The number in str
        coords (List[Tuple[int, int]]): The coordinates of the number
    """

    def __init__(self, value: int, coords: List[Tuple[int, int]]):
        self.value = value
        self.coords = coords

    def add_coord(self, coord: Tuple[int, int]):
        """Add a coordinate to the number
        Args:
            coord (Tuple[int, int]): The coordinate to add
        """
        self.coords.append(coord)

    def __repr__(self):
        return f"Num({self.value}, {self.coords})"

    def __str__(self):
        return self.__repr__()


class Symbol:
    """Represents a symbol
    Args:
        value (str): The symbol
        coord (Tuple[int, int]): The coordinate of the symbol
    """

    def __init__(self, value: str, coord: Tuple[int, int]):
        self.value = value
        self.coord = coord

    def is_adjacent_to(self, num: Num) -> bool:
        """Check if the symbol is adjacent to a number
        Args:
            num (Num): The number to check
        Returns:
            bool: True if adjacent, False otherwise
        """
        matchers = [
            (self.coord[0] - 1, self.coord[1]),
            (self.coord[0] - 1, self.coord[1] - 1),
            (self.coord[0] - 1, self.coord[1] + 1),
            (self.coord[0] + 1, self.coord[1]),
            (self.coord[0] + 1, self.coord[1] - 1),
            (self.coord[0] + 1, self.coord[1] + 1),
            (self.coord[0], self.coord[1] - 1),
            (self.coord[0], self.coord[1] + 1),
        ]
        for matcher in matchers:
            if matcher in num.coords:
                return True

        return False

    def __repr__(self):
        return f"Symbol({self.value}, {self.coord})"

    def __str__(self):
        return self.__repr__()


def solution(file_path: str) -> int:
    total: int = 0
    nums: List[Num] = []
    symbols: List[Symbol] = []

    data = read_input(file_path)

    symbol_chars = set([i for i in "".join(data) if i not in "0123456789."])
    line_len = len(data[0])

    for y, line in enumerate(data):
        num_str = ""
        coords = []
        for x, char in enumerate(line):
            if char.isdigit():
                num_str += char
                coords.append((x, y))

            if char in symbol_chars:
                symbols.append(Symbol(char, (x, y)))

            # logic on how to add the num to the list, then reset the num_str and coords
            # if we are at the end of the line, and there is num in mem, add the num to the list
            if x == line_len - 1 and num_str != "":
                nums.append(Num(int(num_str), coords))
                num_str = ""
                coords = []
            # if we see a dot, and there is num in mem, add the num to the list
            elif char == "." and num_str != "":
                nums.append(Num(int(num_str), coords))
                num_str = ""
                coords = []
            # if we see a symbol, and there is num in mem, add the num to the list, also add the symbol to the list
            elif char in symbol_chars and num_str != "":
                nums.append(Num(int(num_str), coords))
                num_str = ""
                coords = []

    for symbol in symbols:
        for num in nums:
            if symbol.is_adjacent_to(num):
                total += num.value

    return total
