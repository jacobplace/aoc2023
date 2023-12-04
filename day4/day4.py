import re

with open('input') as ifile:
    points = 0
    cards = list()
    for line in ifile:
        card, line = line.split(':')
        win, hand = line.split('|')
        win = set([int(m) for m in re.findall(r'\d+', win)])
        hand = set([int(m) for m in re.findall(r'\d+', hand)])
        match = win.intersection(hand)
        cards.append((1, len(match)))
        if match:
            points += 2 ** (len(match) - 1)
total = 0
for i in range(len(cards)):
    for j in range(cards[i][1]):
        cards[j+i+1] = (cards[j+i+1][0] + cards[i][0], cards[j+i+1][1])
for card in cards:
    total += card[0]
print(points)
print(total)