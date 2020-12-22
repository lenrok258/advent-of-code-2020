from collections import deque
import functools

# test: 306
# input: 32102

blocks = open('input.txt', 'r').read().split('\n\n')

deck1 = deque(map(int, blocks[0].splitlines()[1:]))
deck2 = deque(map(int, blocks[1].splitlines()[1:]))

while True:
    card1, card2 = deck1.popleft(), deck2.popleft()
    
    if card1 > card2:
        deck1.extend([card1, card2])
    else:
        deck2.extend([card2, card1])

    if not deck1 or not deck2:
        break

win_deck = deck1 if len(deck2) == 0 else deck2
print(sum([i * k for i, k in enumerate(reversed(win_deck), start=1)]))