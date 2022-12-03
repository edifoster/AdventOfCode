entries = []

f = open("input/day3/input.txt", "r")
for x in f:
    entries.append(x.rstrip('\n'))

print("Calculating priorities...")

i = 0
common_item = ''
priority = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in entries:
    first = a[0:len(a)//2]
    last = a[len(a)//2:]
    common_item = ''.join(set(first).intersection(last))
    i += priority.index(common_item) + 1

print("Sum of combined items:", i)

c = 0
j = 0
auth_item = ''

while c < len(entries):
    auth_item = ''.join(set(''.join(set(entries[c]).intersection(entries[c+1]))).intersection(entries[c+2]))
    c += 3
    j += priority.index(auth_item) + 1

print("Sum of authentication badges items:", j)



