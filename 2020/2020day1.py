entries = []

f = open("input/2020_1.txt", "r")
for x in f:
    entries.append(int(x))

entries = sorted(entries)

print("Finding two values having sum 2020 and multiply them")
for a in range(len(entries)):
    for b in range(len(entries)):
        if int(entries[a]) + int(entries[b]) == 2020:
            print(entries[a], "+", entries[b], "= 2020")
            print(entries[a], "*", entries[b], "=", int(entries[a]) * int(entries[b]))
            break
    else:
        continue
    break

print("\nFinding three values having sum 2020 and multiply them")
for a in range(len(entries)):
    for b in range(len(entries)):
        for c in range(len(entries)):
            if int(entries[a]) + int(entries[b])+ int(entries[c]) == 2020:
                print(entries[a], "+", entries[b], "+", entries[c], "= 2020")
                print(entries[a], "*", entries[b], "*", entries[c], "=", int(entries[a]) * int(entries[b]) * int(entries[c]))
                break
        else:
            continue
        break
    else:
        continue
    break
