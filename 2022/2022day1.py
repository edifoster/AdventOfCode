entries = []

f = open("input/day1/input.txt", "r")
for x in f:
    entries.append(x.rstrip('\n'))

print("Calculating calories")

calories = []
i = 0

for a in entries:
    if a == '':
        calories.append(i)
        i = 0
    else:
        i += int(a)

print("Maximum package by calories is:", max(calories))
print("Sum of top three packages by calories is", sum(sorted(calories)[-3:]))
