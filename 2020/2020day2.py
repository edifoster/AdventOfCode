entries = []
limit = ""
lowerlimit = 0
upperlimit = 0
keychar = ""
password = ""
validpasswords = 0

f = open("input/2020_2.txt", "r")
for x in f:
    entries.append(x.rstrip())

print("Checking valid passwords (correct amount of characters)")
for a in entries:
    limit = a.split()[0]
    lowerlimit = int(limit.split('-')[0])
    upperlimit = int(limit.split('-')[1])
    keychar = a.split()[1][:1]
    password = a.split()[2]
    i = 0
    for b in password:
        if b == keychar:
            i += 1
    if i >= lowerlimit and i <= upperlimit:
        validpasswords += 1

print("There were", validpasswords, "valid passwords")

print("\nChecking valid passwords (positions matter)")
validpasswords = 0
for a in entries:
    limit = a.split()[0]
    lowerlimit = int(limit.split('-')[0])
    upperlimit = int(limit.split('-')[1])
    keychar = a.split()[1][:1]
    password = a.split()[2]
    i = 0
    if password[lowerlimit - 1] == keychar:
        i += 1
    if password[upperlimit - 1] == keychar:
        i += 1
    if i == 1:
        validpasswords += 1


print("There were", validpasswords, "valid passwords")
