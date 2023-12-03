import re
import sys

PATTERN = re.compile(r"(1|2|3|4|5|6|7|8|9)")


def get_first_and_last(line):
    found = PATTERN.findall(line)
    first, last = found[0], found[-1]
    return int(f"{first}{last}")


def solve(input):
    """
    >>> solve(open('input1.txt'))
    142
    >>> solve(open('input2.txt'))
    56108
    """
    return sum(get_first_and_last(line) for line in input)


if __name__ == "__main__":
    print(solve(sys.stdin))
