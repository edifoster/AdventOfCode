import re
entries = []
i, j, k = 0, 0, 0

f = open("input/day4/input.txt", "r")
for x in f:
    a = x.rstrip("\n").split(",")
    b = a[0].split("-")
    b.append(a[1].split("-")[0])
    b.append(a[1].split("-")[1])
    k += 1
    if (int(b[2]) >= int(b[0]) and int(b[3]) <= int(b[1])) or (int(b[0]) >= int(b[2]) and int(b[1]) <= int(b[3])):
        i += 1
    if int(b[2]) > int(b[1]) or int(b[3]) < int(b[0]):
        j += 1

print("There are", i, "pairs having completely overlapping sections")
print("There are", k-j, "pairs having some overlapping sections")

