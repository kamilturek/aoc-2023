import re
import sys


def get_wins(time, distance):
    return sum(
        1
        for charge_time in range(time)
        if charge_time * (time - charge_time) > distance
    )


def solve(input):
    """
    >>> solve(open('input1.txt'))
    71503
    >>> solve(open('input2.txt'))
    35150181
    """
    time = int("".join(re.findall(r"\d+", input.readline())))
    distance = int("".join(re.findall(r"\d+", input.readline())))

    return get_wins(time, distance)


if __name__ == "__main__":
    print(solve(sys.stdin))
