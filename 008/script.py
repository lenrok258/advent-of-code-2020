
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

        code, value = parse_line(line)
        print(f"{code}:{value}\t\tacc:{acc}")

        if code == 'nop':
            idx += 1
        elif code == 'acc':
            idx += 1
            acc += value
        elif code == 'jmp':
            idx += value


lines = open('input.txt', 'r').read().splitlines()

# star 1
result = execute_program(lines.copy())
print(f"\n░░░ {result} ░░░\n")

# star 2
for i in range(len(lines)):
    code_mutation = lines.copy()
    candidate = code_mutation[i]

    if 'jmp' in candidate:
        code_mutation[i] = candidate.replace('jmp', 'nop')
    elif 'nop' in candidate:
        code_mutation[i] = candidate.replace('nop', 'jmp')
    else:
        continue

    exit_code, acc = execute_program(code_mutation)
    print(f"\n░░░ {exit_code}, acc:{acc} ░░░\n")
    
    if exit_code == 'BOOTED':
        break
    