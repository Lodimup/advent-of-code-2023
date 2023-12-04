"""Parse the input into Nums and Symbols, then check if the symbol is adjacent exactly to two numbers.
If so, multiply the gear ratio of the two numbers and add it to the total.
"""
from typing import List
from utils import read_input
from day_03_1 import Num, Symbol


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
        num_adjecent = 0
        gear_ratios = []
        for i, num in enumerate(nums, 1):
            if symbol.is_adjacent_to(num):
                num_adjecent += 1
                gear_ratios.append(num.value)

            if num_adjecent > 2:
                break

            if i == len(nums) and num_adjecent == 2:
                total += gear_ratios[0] * gear_ratios[1]

    return total


if __name__ == "__main__":
    print(solution("inputs/day_03_2.txt"))
