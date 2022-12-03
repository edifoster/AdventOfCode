entries = []

f = open("input/day2/input.txt", "r")
for x in f:
    entries.append(x.rstrip('\n'))

print("Calculating results...")

i = 0

for a in entries:
    if a[0] == 'A' and a[2] == 'X':
        i += 3 + 1
    elif a[0] == 'A' and a[2] == 'Y':
        i += 6 + 2
    elif a[0] == 'A' and a[2] == 'Z':
        i += 0 + 3
    elif a[0] == 'B' and a[2] == 'Y':
        i += 3 + 2
    elif a[0] == 'B' and a[2] == 'Z':
        i += 6 + 3
    elif a[0] == 'B' and a[2] == 'X':
        i += 0 + 1
    elif a[0] == 'C' and a[2] == 'Z':
        i += 3 + 3
    elif a[0] == 'C' and a[2] == 'X':
        i += 6 + 1
    elif a[0] == 'C' and a[2] == 'Y':
        i += 0 + 2

print("Score with strategy 1", i)

j = 0

for a in entries:
    if a[0] == 'A' and a[2] == 'Y':
        j += 4
    elif a[0] == 'A' and a[2] == 'Z':
        j += 8
    elif a[0] == 'A' and a[2] == 'X':
        j += 3
    elif a[0] == 'B' and a[2] == 'Y':
        j += 5
    elif a[0] == 'B' and a[2] == 'Z':
        j += 9
    elif a[0] == 'B' and a[2] == 'X':
        j += 1
    elif a[0] == 'C' and a[2] == 'Y':
        j += 6
    elif a[0] == 'C' and a[2] == 'Z':
        j += 7
    elif a[0] == 'C' and a[2] == 'X':
        j += 2

print("Score with strategy 2", j)
