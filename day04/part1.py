import re
import sys

PATTERN = re.compile(r"^Card\s+\d+:\s+([\d\s]+)\s\|\s+([\d\s]+)\n")


def count_points(card):
    groups = [set(re.split("\s+", group)) for group in PATTERN.match(card).groups()]
    winning_numbers, numbers = groups
    count = len(winning_numbers & numbers)
    return 2 ** (count - 1) if count else 0


def solve(input):
    """
    >>> solve(open('input1.txt'))
    13
    >>> solve(open('input2.txt'))
    22897
    """
    return sum(count_points(card) for card in input)


if __name__ == "__main__":
    print(solve(sys.stdin))
