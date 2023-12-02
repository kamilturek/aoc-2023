import re
import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    142
    >>> solve(open('input2.txt'))
    56108
    """
    total = 0
    pattern = re.compile(r"(1|2|3|4|5|6|7|8|9)")

    for line in input:
        found = pattern.findall(line)
        first, last = found[0], found[-1]
        total += int(f"{first}{last}")

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
