
# test: 10:92658374, 100:67384529
# input: 49725386

line = open('input.txt', 'r').readline()
cups = list(map(int, list(line)))
print(cups)
print()

min_cup = min(cups)
max_cup = max(cups)


def get_trio_idx(cups, curr_idx):
    idx_1 = (curr_idx + 1) % len(cups)
    idx_2 = (curr_idx + 2) % len(cups)
    idx_3 = (curr_idx + 3) % len(cups)
    return (idx_1, idx_2, idx_3)


def get_trio(trio_idx):
    return (cups[trio_idx[0]], cups[trio_idx[1]], cups[trio_idx[2]])


def remove_trio(cups, trio):
    # works only if values are unique!
    cups.remove(trio[0])
    cups.remove(trio[1])
    cups.remove(trio[2])


def insert_trio(cups, trio, dest_idx):
    cups.insert(dest_idx+1, trio[0])
    cups.insert(dest_idx+2, trio[1])
    cups.insert(dest_idx+3, trio[2])


def play(cups):

    current_idx = 0
    current_value = cups[0]

    for i in range(100):

        print(f"--- move {i+1} ---")

        print(f"Cups:\t\t{cups}")
        print(f"Curr val:\t{current_value}")

        trio_idxs = get_trio_idx(cups, current_idx)
        trio = get_trio(trio_idxs)
        print(f"Trio:\t\t{trio}")
        remove_trio(cups, trio)
        # print(f"No trio:\t{cups}")

        dest_value = current_value
        dest_idx = current_idx
        while True:
            
            dest_value -= 1

            if dest_value < min_cup:
                dest_value = max_cup

            if dest_value in trio:
                continue

            if dest_value in cups:
                dest_idx = cups.index(dest_value)
                break

        print(f"Destination:\t{dest_value}")
        insert_trio(cups, trio, dest_idx)
        # print(f"Cups with trio:\t{cups}")

        current_idx = cups.index(current_value)
        current_idx = (current_idx + 1) % len(cups)
        current_value = cups[current_idx]

        print()



play(cups)
print(cups)

oneoneonei = cups.index(1)

result = cups[oneoneonei+1:] + cups[:oneoneonei]
print("".join([str(r) for r in result]))