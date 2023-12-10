import functools
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
    288
    >>> solve(open('input2.txt'))
    293046
    """
    races = zip(
        (int(n) for n in re.findall(r"\d+", input.readline())),
        (int(n) for n in re.findall(r"\d+", input.readline())),
    )

    return functools.reduce(lambda mul, race: mul * get_wins(*race), races, 1)


if __name__ == "__main__":
    print(solve(sys.stdin))
