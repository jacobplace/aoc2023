import re

with open('test') as ifile:
    points = 0
    cards = {}
    for line in ifile:
        card, line = line.split(':')
        card = [int(m) for m in re.findall(r'\d+', card)][0]
        win, hand = line.split('|')
        win = set([int(m) for m in re.findall(r'\d+', win)])
        hand = set([int(m) for m in re.findall(r'\d+', hand)])
        match = win.intersection(hand)
        cards[card] = list(match)
        if match:
            points += 2 ** (len(match) - 1)
print(points)

#p2
