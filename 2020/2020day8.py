import copy

data, data2 = [], []
a = 0

f = open("input/2020_8.txt", "r")
for x in f:
    data.append(x.rstrip())

while a < len(data):
    data2.append((a, data[a].split()))
    a += 1


def code(instructions):
    acc_val, b = 0, 0
    handled_rows = []

    while b < len(instructions):
        if b in handled_rows:
            return False, acc_val
        else:
            handled_rows.append(b)
            if instructions[b][1][0] == 'nop':
                b += 1
            elif instructions[b][1][0] == 'acc':
                acc_val += int(instructions[b][1][1])
                b += 1
            elif instructions[b][1][0] == 'jmp':
                b += int(instructions[b][1][1])
            else:
                print("\nIncorrect code", instructions[b][1][0])
                return False, acc_val
        if b == len(instructions):
            return True, acc_val


def fix_code(broken_commands):
    loop = False
    c = 0

    while loop is False and c < len(broken_commands):
        commands = copy.deepcopy(broken_commands)
        if commands[c][1][0] == 'nop':
            commands[c][1][0] = 'jmp'
        elif commands[c][1][0] == 'jmp':
            commands[c][1][0] = 'nop'
        if commands[c][1][0] != 'acc':
            loop, acc_value = code(commands)
        c += 1
    return loop, acc_value



fixable, accumulator = fix_code(data2)
# Part 1
print("\nWithout fixing the program the accumulator gets value", code(data2)[1])

# Part 2
if fixable is True:
    print("\nAfter hours of hard work the program was fixed and accumulator gets value", accumulator)
else:
    print("\nProgram could not be fixed with by this lousy coder :'(")


