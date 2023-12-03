import sys


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
    4361
    >>> solve(open('input2.txt'))
    550934
    """
    total = 0
    matrix = [list(line.strip()) for line in input]

    for y, row in enumerate(matrix):
        is_part_number = False
        number = ""

        for x, cell in enumerate(row):
            if cell.isdigit():
                number += cell

                if is_part_number is False:
                    neighbours = get_neighbours(y, x, len(matrix), len(row))
                    for ny, nx in neighbours:
                        neighbour = matrix[ny][nx]
                        if neighbour.isdigit() is False and neighbour != ".":
                            is_part_number = True
                            break
            else:
                if is_part_number is True:
                    total += int(number)

                number = ""
                is_part_number = False

        if is_part_number is True:
            total += int(number)

    return total


if __name__ == "__main__":
    print(solve(sys.stdin))
