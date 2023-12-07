# Part 1
from collections import defaultdict


with open('input.txt', 'r') as f:
    hands_and_bets = {line.strip().split(' ')[0]: int(line.strip().split(' ')[1]) for line in f}

def get_value(hand):
    card_value = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    counter = defaultdict(int)
    for c in hand:
        counter[c] += 1

    nb_pairs = 0
    max_value = 0
    for nb_same_cards in counter.values():
        if nb_same_cards == 2:
            nb_pairs += 1
        max_value = max(max_value, nb_same_cards)

    if max_value == 2 and nb_pairs == 2:
        max_value = 3
    elif max_value == 3:
        max_value = 4 + (1 if nb_pairs == 1 else 0)
    elif max_value > 3:
        max_value += 2

    hand_card_values = []
    for c in hand:
        if c in card_value:
            hand_card_values.append(card_value[c])
        else:
            hand_card_values.append(int(c))

    return (max_value, hand_card_values)


hands = list(hands_and_bets.keys())
sorted_hands = sorted(hands, key=get_value)

winnings = 0
for idx, hand in enumerate(sorted_hands):
    winnings += (idx + 1) * hands_and_bets[hand]

print(winnings)


# Part 2
from collections import defaultdict


with open('input.txt', 'r') as f:
    hands_and_bets = {line.strip().split(' ')[0]: int(line.strip().split(' ')[1]) for line in f}

def get_value(hand):
    card_value = {"T": 10, "J": 1, "Q": 12, "K": 13, "A": 14}
    counter = defaultdict(int)
    for c in hand:
        counter[c] += 1

    nb_pairs = 0
    nb_jokers = counter['J']
    max_value = 0
    for card, nb_same_cards in counter.items():
        if card == 'J':
            continue
        if nb_same_cards == 2:
            nb_pairs += 1
        max_value = max(max_value, nb_same_cards)

    max_value += nb_jokers
    
    if max_value == 2 and nb_pairs == 2:
        max_value = 3
    elif max_value == 3:
        max_value = 4
        if nb_pairs == 1 and nb_jokers == 0:
            max_value = 5
        elif nb_pairs == 2 and nb_jokers == 1:
            max_value = 5
    elif max_value > 3:
        max_value += 2

    hand_card_values = []
    for c in hand:
        if c in card_value:
            hand_card_values.append(card_value[c])
        else:
            hand_card_values.append(int(c))

    return (max_value, hand_card_values)


hands = list(hands_and_bets.keys())
sorted_hands = sorted(hands, key=get_value)

winnings = 0
for idx, hand in enumerate(sorted_hands):
    winnings += (idx + 1) * hands_and_bets[hand]

print(winnings)
