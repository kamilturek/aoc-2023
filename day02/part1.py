import re
import sys


def parse_game(game):
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

    return int(game_id), game_maxes


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

    return sum(
        game_id
        for game_id, game_maxes in (parse_game(line) for line in input)
        if all(count <= maxes[color] for color, count in game_maxes.items())
    )


if __name__ == "__main__":
    print(solve(sys.stdin))
