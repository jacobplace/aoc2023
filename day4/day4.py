import re


def calculate_p2(cards: list) -> int:
    total = 0
    for i in range(len(cards)):
        for j in range(cards[i][1]):
            cards[j + i + 1] = (cards[j + i + 1][0] + cards[i][0], cards[j + i + 1][1])
    for card in cards:
        total += card[0]
    return total


def parse_hands(line: str) -> set:
    _, line = line.split(":")
    win, hand = line.split("|")
    win = set([int(m) for m in re.findall(r"\d+", win)])
    hand = set([int(m) for m in re.findall(r"\d+", hand)])
    return win.intersection(hand)


def main():
    with open("input") as ifile:
        points = 0
        cards = list()
        for line in ifile:
            match = parse_hands(line)
            cards.append((1, len(match)))
            if match:
                points += 2 ** (len(match) - 1)
    print(f"P1:{points}\tP2:{calculate_p2(cards)}")


if __name__ == "__main__":
    main()
