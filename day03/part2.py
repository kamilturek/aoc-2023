import sys
from collections import defaultdict


def get_neighbours(y, x, height, width):
    return [
        (j, i)
        for j, i in [
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x - 1),
            (y + 1, x),
            (y + 1, x + 1),
        ]
        if 0 <= j < height and 0 <= i < width
    ]


def solve(input):
    """
    >>> solve(open('input1.txt'))
    467835
    >>> solve(open('input2.txt'))
    81997870
    """
    matrix = [list(line.strip()) for line in input]
    gears = defaultdict(list)

    for y, row in enumerate(matrix):
        has_gear = False
        gear_x, gear_y = None, None
        number = ""

        for x, cell in enumerate(row):
            if cell.isdigit():
                number += cell

                if has_gear is False:
                    neighbours = get_neighbours(y, x, len(matrix), len(row))
                    for ny, nx in neighbours:
                        neighbour = matrix[ny][nx]
                        if neighbour == "*":
                            has_gear = True
                            gear_x, gear_y = nx, ny
                            break
            else:
                if has_gear is True:
                    gears[(gear_y, gear_x)].append(int(number))

                number = ""
                has_gear = False

        if has_gear is True:
            gears[(gear_y, gear_x)].append(int(number))

    return sum(ratios[0] * ratios[1] for _, ratios in gears.items() if len(ratios) == 2)


if __name__ == "__main__":
    print(solve(sys.stdin))
