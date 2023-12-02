import functools
import operator
import re
import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    2286
    >>> solve(open('input2.txt'))
    84538
    """
    total = 0

    for game in input:
        game_maxes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        cube_sets = re.match(r"Game \d+: (.*)", game).group(0)
        cube_sets = cube_sets.split(";")

        for cube_set in cube_sets:
            for count, color in re.findall("(\d+) (\w+)", cube_set):
                game_maxes[color] = max(game_maxes[color], int(count))

        power = functools.reduce(operator.mul, game_maxes.values())
        total += power

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
