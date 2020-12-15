# test: 1325
# input - part 1: 1325
# input - part 2: 59006

numbers = list(
    map(int, open('input.txt', 'r').read().splitlines()[0].split(',')))


def play_the_game(rounds):
    observer = 1000
    i, prv_n, turns = 0, -1, dict()

    while(i < len(numbers)):
        n = numbers[i]
        turns[n] = (-1, i)
        prv_n = n
        i += 1

    while(i < rounds):
        n = prv_n
        number_idxs = turns[n]
        if number_idxs[0] == -1:
            new_n = 0
        else:
            new_n = number_idxs[1] - number_idxs[0]

        if new_n not in turns:
            turns[new_n] = (-1, -1)
        turns[new_n] = (turns[new_n][1], i)

        prv_n = new_n

        i += 1

        if i > observer:
            print(i)
            observer *= 10

    return prv_n


print(f"Star1: {play_the_game(2020)}")
print(f"Star2: {play_the_game(30000000)}")
