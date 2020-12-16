import re
import itertools

# test: ?
# input : 855275529001

validations = {}
my_ticket = []
tickets = []

input_blocks = open('input.txt', 'r').read().split("\n\n")
for line in input_blocks[0].splitlines():
    tiles = re.split(": | or ", line)
    validations[tiles[0]] = (tiles[1], tiles[2])
for line in input_blocks[1].splitlines()[1:]:
    my_ticket = line.split(',')
tickets.append(my_ticket)
for line in input_blocks[2].splitlines()[1:]:
    tickets.append(line.split(','))



# print(validations)
# print(my_ticket)
# print(tickets)
print("------")


def is_value_valid(val):
    for valid_key, valid_values in validations.items():
        for vv in valid_values:
            v_min, v_max = map(int, vv.split("-"))
            if (v_min <= int(val) <= v_max):
                return True
    return False


def matching_fields(val):
    fields = []
    for valid_key, valid_values in validations.items():
        for vv in valid_values:
            v_min, v_max = map(int, vv.split("-"))
            if (v_min <= int(val) <= v_max):
                fields.append(valid_key)
    return fields


def is_ticket_valid(tic):
    for v in tic:
        if not is_value_valid(v):
            return False
    return True


# def resolve_fields(valid_tickets):
#     fields_order = {}
#     for tic in valid_tickets:
#         for idx, v in enumerate(tic):
#             fields = matching_fields(v)
#             # print(f"{v} {fields}")
#             if len(fields) == 1:
#                 print(fields)
#                 f_resolved = fields[0]
#                 if f_resolved not in fields_order:
#                     fields_order[idx] = f_resolved
#                     del validations[f_resolved]
#     return fields_order

def resolve_fields(tickets):
    fields_order = []
    # final_solution = [] * 
    for i in range(len(validations)):
        fields_order.append(list(validations.keys()).copy())
    
    # --------

    for idx in range(len(tickets[0])):
        for tic in tickets:
            tic_val = tic[idx]
            matching_list = matching_fields(tic_val)
            intersection = set(fields_order[idx]) & set(matching_list)
            # print(f"{tic_val}: {fields_order[idx]} - {matching_list} = {intersection}")
            # print(intersection)
            fields_order[idx] = list(intersection)
        # break

    # --------

    # for idx, field in enumerate(fields_order):
    #     if len(field) == 1:
    #         final_solution[idx] = field
            # for field in fields_order:
            #     if len(field) > 1:


    return fields_order



valid_tickets = list(filter(is_ticket_valid, tickets))
# print(valid_tickets)
final_solution = resolve_fields(valid_tickets)

# print(tickets)
for i in final_solution:
    print(i)
    # print(len(i))

fields_order = ['departure track','arrival track','wagon','arrival platform','departure location','departure date','row','seat','departure station','route','arrival station','departure time','type','train','zone','arrival location','duration','class','departure platform','price']

solution = ''
for i, f in enumerate(fields_order):
    if f.startswith('departure'):
        solution += f" * {my_ticket[i]}"
print(solution)