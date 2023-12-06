"""
- get seed
- get maps
- convert till we get locations
- get lowest location
"""
import re
from typing import List, Tuple
from functools import lru_cache
from utils import read_input


class Mapper:
    """Mapper class
    use parse to convert value to another value
    Args:
        data (List[Tuple[int, int, int]]): The data to parse


    Example
    seed-to-soil map:
    50 98 2
    52 50 48

    means

    98-100 is mapped to 50-52
    """

    def __init__(self, data: List[Tuple[int, int, int]]):
        self.data = data

    @lru_cache(maxsize=None)
    def convert(self, value: int):
        """
        if value between, then it can be converted
        else, return value
        """
        for dst, src, rng in self.data:
            if value >= src and value <= src + rng - 1:
                return dst + (value - src)

        return value


def parse_seeds(s: str) -> list[int]:
    """parse seeds
    Args:
        s (str): the string to parse
    Returns:
        list[int]: the parsed seeds
    """
    return [int(i) for i in re.findall(r"\d+", s)]


def parse_for_mapper(table_name: str, data: list[str]) -> Mapper:
    """Returns mapper given table name
    Args:
        table_name (str): the table name
        data (list[str]): the data
    Returns:
        Mapper: the mapper
    """
    raw = []
    keep = False
    for line in data:
        if table_name in line:
            keep = True
            continue
        if keep and line == "":
            break
        if keep:
            raw.append(line)
    data = [tuple([int(i) for i in re.findall(r"\d+", line)]) for line in raw]  # oh no
    return Mapper(data)


def solution(file_path: str):
    """Solution to day 5 part 1"""
    data = read_input(file_path)
    seeds = parse_seeds(data[0])
    seed2soil = parse_for_mapper("seed-to-soil", data)
    soil2fertilizer = parse_for_mapper("soil-to-fertilizer", data)
    fertillizer2water = parse_for_mapper("fertilizer-to-water", data)
    water2light = parse_for_mapper("water-to-light", data)
    light2temperature = parse_for_mapper("light-to-temperature", data)
    temperature2humidity = parse_for_mapper("temperature-to-humidity", data)
    humidity2location = parse_for_mapper("humidity-to-location", data)

    minimum = -1
    for seed in seeds:
        soil = seed2soil.convert(seed)
        fertilizer = soil2fertilizer.convert(soil)
        water = fertillizer2water.convert(fertilizer)
        light = water2light.convert(water)
        temperature = light2temperature.convert(light)
        humidity = temperature2humidity.convert(temperature)
        location = humidity2location.convert(humidity)
        if minimum == -1 or location < minimum:
            minimum = location

    return minimum


if __name__ == "__main__":
    file_path = "inputs/day_05.txt"
    print(solution(file_path))
