from collections import deque

# test: 291
# input: 34173 (~14s)

blocks = open('input.txt', 'r').read().split('\n\n')

deck1 = deque(map(int, blocks[0].splitlines()[1:]))
deck2 = deque(map(int, blocks[1].splitlines()[1:]))

def play_game(deck1, deck2):
    deck1_history, deck2_history = [], []

    while True:
        # break inf. loop
        if deck1 in deck1_history and deck2 in deck2_history:
            return (1, deck1)

        deck1_history.append(deck1.copy())
        deck2_history.append(deck2.copy())

        card1, card2 = deck1.popleft(), deck2.popleft()

        # recursive turn
        if card1 <= len(deck1) and card2 <= len(deck2):
            deck1_copy = deque(list(deck1)[:card1])
            deck2_copy = deque(list(deck2)[:card2])

            winner = play_game(deck1_copy, deck2_copy)
            if winner[0] == 1:
                deck1.extend([card1, card2])
            elif winner[0] == 2:
                deck2.extend([card2, card1])
        
        # normal turn
        else:    
            if card1 > card2:
                deck1.extend([card1, card2])
            else:
                deck2.extend([card2, card1])

        # end of game
        if not deck1 or not deck2:
            return (1, deck1) if not deck2 else (2, deck2)


winner = play_game(deck1, deck2)
print(sum([i * k for i, k in enumerate(reversed(winner[1]), start=1)]))