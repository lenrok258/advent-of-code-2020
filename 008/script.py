
def parse_line(line):
    tiles = line.split(" ")
    return (tiles[0], int(tiles[1]))

def execute_program(code_to_test):
    idx = acc = 0
    while True:
        if idx >= len(code_to_test):
            return ('BOOTED', acc)

        line = code_to_test[idx]
        code_to_test[idx] = 'INF_LOOP'
        
        if 'INF_LOOP' in line:
            return ('INF_LOOP', acc)

        instr, value = parse_line(line)
        print(f"{instr}:{value}\t\tacc:{acc}")

        if instr == 'nop':
            idx += 1
        elif instr == 'acc':
            idx += 1
            acc += value
        elif instr == 'jmp':
            idx += value


lines = open('input.txt', 'r').read().splitlines()

# star 1
result = execute_program(lines.copy())
print(f"\n░░░ {result} ░░░\n")

# star 2
for i in range(len(lines)):
    code_mutation = lines.copy()
    candidate = code_mutation[i]

    instr, value = parse_line(candidate)
    if instr in ['jmp', 'nop']:
        mutated_instr = 'nop' if instr == 'jmp' else 'jmp'
        code_mutation[i] = f"{mutated_instr} {value}"
        exit_code, acc = execute_program(code_mutation)
        print(f"\n░░░ {exit_code}, acc:{acc} ░░░\n")

        if exit_code == 'BOOTED':
            break