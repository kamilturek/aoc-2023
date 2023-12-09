import re
import sys

PATTERN = re.compile(r"^Card\s+\d+:\s+([\d\s]+)\s\|\s+([\d\s]+)")


def count_matches(card):
    groups = [set(re.split("\s+", group)) for group in PATTERN.match(card).groups()]
    winning_numbers, numbers = groups
    return len(winning_numbers & numbers)


def solve(input):
    """
    >>> solve(open('input1.txt'))
    30
    >>> solve(open('input2.txt'))
    5095824
    """
    cards = input.read().splitlines()
    cards_count = {card_id: 1 for card_id in range(1, len(cards) + 1)}

    for current_card_id, card in enumerate(cards, 1):
        points = count_matches(card)

        for next_card_id in range(current_card_id + 1, current_card_id + 1 + points):
            if next_card_id > len(cards_count):
                break

            cards_count[next_card_id] += 1 * cards_count[current_card_id]

    return sum(cards_count.values())


if __name__ == "__main__":
    print(solve(sys.stdin))
