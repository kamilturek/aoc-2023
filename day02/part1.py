import re
import sys


def solve(input):
    """
    >>> solve(open('input1.txt'))
    8
    >>> solve(open('input2.txt'))
    1867
    """
    maxes = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    total = 0

    for game in input:
        game_maxes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        game_id, cube_sets = re.match(r"Game (\d+): (.*)", game).groups()
        cube_sets = cube_sets.split(";")

        for cube_set in cube_sets:
            for count, color in re.findall("(\d+) (\w+)", cube_set):
                game_maxes[color] = max(game_maxes[color], int(count))

        for color, max_count in maxes.items():
            if game_maxes[color] > max_count:
                break
        else:
            total += int(game_id)

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
