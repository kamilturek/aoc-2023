import functools
import re
import sys


class RangeMap:
    def __init__(self, ranges: list[tuple[int, int, int]]) -> None:
        self.ranges = ranges

    def __getitem__(self, key: int) -> int:
        for dst_start, src_start, size in self.ranges:
            if src_start <= key < src_start + size:
                offset = key - src_start
                return dst_start + offset
        return key


def solve(input):
    """
    >>> solve(open('input1.txt'))
    35
    >>> solve(open('input2.txt'))
    331445006
    """
    seeds = [int(s) for s in re.findall(r"\d+", input.readline())]
    raw_range_maps = input.read().strip().split("\n\n")
    range_maps = [
        RangeMap(
            [
                [int(n) for n in line.split()]
                for line in raw_map.splitlines()
                if "map" not in line
            ]
        )
        for raw_map in raw_range_maps
    ]

    return min(
        functools.reduce(lambda key, range_map: range_map[key], range_maps, seed)
        for seed in seeds
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
