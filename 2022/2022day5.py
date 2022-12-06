crates, moves = [], []

f = open("input/day5/crates.txt", "r")
for x in f:
    crates.append(x.rstrip('\n'))

columns = int(((len(crates[0])+1)/4))
crateColumns = {i: [] for i in range(1, columns+1, 1)}
row = [[] for i in range(1, columns+1, 1)]
i, j, k = 0, 1, 0

for y in crates:
    while j < len(crates[i]):
        row[k].append(crates[i][j])
        j += 4
    i += 1
    k += 1
    j = 1

i, j, k = len(row), 0, 1
while i > 0:
    i -= 1
    while j < len(row[i]):
        if row[i][j] != ' ':
            crateColumns[k].append(row[i][j])
        j += 1
        k += 1
    j, k = 0, 1


def move_crane_9000(source, target, amount):
    m = 0
    stack = []
    while m < amount:
        stack.append(crateColumns[source].pop())
        m += 1
    for n in stack:
        crateColumns[target].append(n)
    return crateColumns


def move_crane_9001(source, target, amount):
    m = 0
    stack = []
    while m < amount:
        stack.append(crateColumns[source].pop(-(amount-m)))
        m += 1
    for n in stack:
        crateColumns[target].append(n)
    return crateColumns


f2 = open("input/day5/input.txt", "r")
for y in f2:
    moves.append(y.rstrip('\n').split(" "))


for a in moves:
    crateColumns = move_crane_9001(int(a[3]), int(a[5]), int(a[1]))


answer = ""
for b in crateColumns:
    answer += crateColumns[b][-1:][0]

print("Top crates of each column:", answer)
