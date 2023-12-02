import re
import sys


def solve(input):
    """
    >>> solve(open('input3.txt'))
    281
    >>> solve(open('input2.txt'))
    55652
    """
    digits = {
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

    total = 0
    pattern = re.compile(rf"(?=({'|'.join(digits)}))")

    for line in input:
        found = pattern.findall(line)
        first, last = digits[found[0]], digits[found[-1]]
        total += int(f"{first}{last}")

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
