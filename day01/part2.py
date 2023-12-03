import re
import sys

DIGITS = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
PATTERN = re.compile(rf"(?=({'|'.join(DIGITS)}))")


def get_first_and_last(line):
    found = PATTERN.findall(line)
    first, last = DIGITS[found[0]], DIGITS[found[-1]]
    return int(f"{first}{last}")


def solve(input):
    """
    >>> solve(open('input3.txt'))
    281
    >>> solve(open('input2.txt'))
    55652
    """
    return sum(get_first_and_last(line) for line in input)


if __name__ == "__main__":
    print(solve(sys.stdin))
