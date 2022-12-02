entries = []

f = open("input/day2/input.txt", "r")
for x in f:
    entries.append(x.rstrip('\n'))

print("Calculating puzzle")

i = 0

for a in entries:
    if a[2] == 'X':
        i += 1
    if a[2] == 'Y':
        i += 2
    if a[2] == 'Z':
        i += 3
    if a[0] == 'A' and a[2] == 'X':
        i += 3
    if a[0] == 'A' and a[2] == 'Y':
        i += 6
    if a[0] == 'B' and a[2] == 'Y':
        i += 3
    if a[0] == 'B' and a[2] == 'Z':
        i += 6
    if a[0] == 'C' and a[2] == 'Z':
        i += 3
    if a[0] == 'C' and a[2] == 'X':
        i += 6

print("Strategy 1", i)

i = 0

for a in entries:
    if a[0] == 'A' and a[2] == 'Y':
        i += 4
    if a[0] == 'A' and a[2] == 'Z':
        i += 8
    if a[0] == 'A' and a[2] == 'X':
        i += 3
    if a[0] == 'B' and a[2] == 'Y':
        i += 5
    if a[0] == 'B' and a[2] == 'Z':
        i += 9
    if a[0] == 'B' and a[2] == 'X':
        i += 1
    if a[0] == 'C' and a[2] == 'Y':
        i += 6
    if a[0] == 'C' and a[2] == 'Z':
        i += 7
    if a[0] == 'C' and a[2] == 'X':
        i += 2

print("Strategy 2", i)
