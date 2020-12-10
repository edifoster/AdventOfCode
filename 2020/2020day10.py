data = [0]
f = open("input/2020_10.txt", "r")
for x in f:
    data.append(int(x.rstrip()))

data = sorted(data)
data.append(data[-1]+3)

differences = []
min_dist, max_dist, x = 0, 0, 1

while x < len(data):
    if int(data[x]) - int(data[x-1]) == 1:
        min_dist += 1
        differences.append(1)
    elif int(data[x]) - int(data[x - 1]) == 3:
        max_dist += 1
        differences.append(3)
    x += 1

print("Part 1:\nJolting multiplier value:", min_dist*max_dist)


y, series = 0, []

while y < len(differences):
    if differences[y] == 1:
        counter = 0
        while differences[y] == 1:
            counter += 1
            y += 1
        series.append(counter)
    y += 1


variations = 1

for z in series:
    if z == 1:
        variations *= 1
    if z == 2:
        variations *= 2
    if z == 3:
        variations *= 4
    if z == 4:
        variations *= 7

print("\nPart 2:\nThere are", variations, "among all adapters")
