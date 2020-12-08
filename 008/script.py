lines = open('input.txt', 'r').read().splitlines()

idx = 0
acc = 0
while True:
    line = lines[idx]
    
    if 'TERM' in line:
        break

    line_array = line.split(" ")
    code = line_array[0]
    value = int(line_array[1])
    print(f"{line_array} acc:{acc}")

    if code == 'nop':
        lines[idx] = 'TERM'
        idx += 1
    elif code == 'acc':
        lines[idx] = 'TERM'
        idx += 1
        acc += value
    elif code == 'jmp':
        lines[idx] = 'TERM'
        idx += value

print("Answer 1: {}".format(acc))
