from dataclasses import dataclass
import cProfile

# test: 149245887792
# input: 538935646702 (~20s)


@dataclass
class Cup:

    value = 0
    next = None
    prev = None

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        if self.next and self.prev:
            return f"Cup[{self.value}, p={self.prev.value}, n={self.next.value}]"
        if self.next and not self.prev:
            return f"Cup[{self.value}, n={self.next.value}]" 
        if self.prev and not self.next:
            return f"Cup[{self.value}, p={self.prev.value}]" 
        return f"Cup[{self.value}, next={self.next}]"


line = open('input.txt', 'r').readline()
init_cups = list(map(int, list(line)))

first_cup = Cup(init_cups[0])
cup_1 = None

# Wiring next
prv_c = first_cup
for ic in init_cups[1:]:
    c = Cup(ic)
    prv_c.next = c
    prv_c = c

# Finding cup_1
cup_s = first_cup
while True:
    if not cup_s.next:
        break
    if cup_s.value == 1:
        cup_1 = cup_s
        break
    cup_s = cup_s.next

# Wiring prev
cup = first_cup
search_cup = first_cup
while True:
    search_value = cup.value - 1
    while True:
        if search_value == search_cup.value:
            cup.prev = search_cup
            break
        if not search_cup.next:
            break

        search_cup = search_cup.next
    search_cup = first_cup

    if not cup.next:
        break
    cup = cup.next


# Adding to 1_000_000
last_cup = first_cup
cup_9 = first_cup
while True:
    if not last_cup.next:
        break
    last_cup = last_cup.next
    if last_cup.value == 9:
        cup_9 = last_cup

prev_cup = Cup(10, cup_9, None)
last_cup.next = prev_cup
for i in range(11, 1000001):
    c = Cup(i, prev_cup, None)
    prev_cup.next = c
    c.prev = prev_cup
    prev_cup = c



# Star 1 Wiring last and first cup
min_val_cup = first_cup
max_val_cup = first_cup
cc = first_cup
while True:
    if cc.value < min_val_cup.value:
        min_val_cup = cc
    if cc.value > max_val_cup.value:
        max_val_cup = cc
    if not cc.next:
        # last one:
        cc.next = first_cup
        min_val_cup.prev = max_val_cup
        break
    cc = cc.next



LEN_CUPS = 30

def print_cups(cup):
    for i in range(LEN_CUPS):
        print(f"{cup.value} ", end='')
        cup = cup.next
    print("\n\n")


def print_cups_full(cup):
    for i in range(LEN_CUPS):
        print(f"{cup} ")
        cup = cup.next
    print()

# ------------------------------------------------------------------


def make_a_move(current):
    trio_start = current.next
    current.next = trio_start.next.next.next
    
    trio_vals = []
    trio_i = trio_start
    for i in range(3):
        trio_vals.append(trio_i.value)
        trio_i = trio_i.next

    prev_s = current.prev
    while prev_s.value in trio_vals:
        prev_s = prev_s.prev

    trio_start.next.next.next = prev_s.next
    prev_s.next = trio_start

    return current.next



print("----- start ----- \n")
print_cups(first_cup)
print_cups_full(first_cup)

curr = first_cup
for i in range(10000000):
    curr = make_a_move(curr)

print("----- stop ----- \n")
print_cups(first_cup)
print_cups_full(first_cup)

print(cup_1)
print(cup_1.next)
print(cup_1.next.next)

print(cup_1.next.value * cup_1.next.next.value)