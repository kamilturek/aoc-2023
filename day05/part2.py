import itertools
import re
import sys


class RangeMap:
    def __init__(self, ranges: list[tuple[int, int, int]]) -> None:
        self.ranges = ranges

    def __getitem__(self, key: int) -> int:
        for src_start, dst_start, size in self.ranges:
            if src_start <= key < src_start + size:
                offset = key - src_start
                return dst_start + offset
        return key


class RangeSet:
    def __init__(self, ranges: list[tuple[int, int]]) -> None:
        self.ranges = ranges

    def __contains__(self, key: int) -> bool:
        return any(start <= key < start + size for start, size in self.ranges)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    46
    >>> solve(open('input2.txt'))
    6472060
    """
    seeds = RangeSet(
        [
            [int(n) for n in pair.split()]
            for pair in re.findall(r"\d+ \d+", input.readline())
        ]
    )

    raw_range_maps = input.read().strip().split("\n\n")
    range_maps = list(
        reversed(
            [
                RangeMap(
                    [
                        [int(n) for n in line.split()]
                        for line in raw_map.splitlines()
                        if "map" not in line
                    ]
                )
                for raw_map in raw_range_maps
            ]
        )
    )

    for location in itertools.count():
        key = location

        for range_map in range_maps:
            key = range_map[key]

        if key in seeds:
            return location


if __name__ == "__main__":
    print(solve(sys.stdin))
