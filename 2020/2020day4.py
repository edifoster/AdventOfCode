import re
test_set_invalid = ['eyr:1972 cid:100 hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926', 'iyr:2019 hcl:#602927 eyr:1967 hgt:170cm ecl:grn pid:012533040 byr:1946',
                'hcl:dab227 iyr:2012 ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277', 'hgt:59cm ecl:zzz eyr:2038 hcl:74454a iyr:2023 pid:3556412378 byr:2007']
test_set_valid = ['pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980 hcl:#623a2f', 'eyr:2029 ecl:blu cid:129 byr:1989 iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm',
              'hcl:#888785 hgt:164cm byr:2001 iyr:2015 cid:88 pid:545766238 ecl:hzl eyr:2022', 'iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719']

print("Testing test sets..")
test_byr = ['byr:2002', 'byr:2003']
test_hgt = ['hgt:60in', 'hgt:190cm', 'hgt:190in', 'hgt:190']
test_hcl = ['hcl:#123abc', 'hcl:#123abz', 'hcl:123abc']
test_ecl = ['ecl:brn', 'ecl:wat']
test_pid = ['pid:000000001', 'pid:0123456789', 'pid:123']

print("Testing byr validation...")
c = 0
while c < len(test_byr):
    if 'byr' in test_byr[c]:
        if 1920 <= int(re.search('(?<=byr:)[0-9]{4}', test_byr[c])[0]) <= 2002:
            print("valid:", test_byr[c])
        else:
            print("invalid:", test_byr[c])
    c += 1

print("Testing hgt validation...")
c = 0
while c < len(test_hgt):
    if 'hgt' in test_hgt[c]:
        m = re.search('(?<=hgt:)[0-9]{2,3}[a-z]{2}', test_hgt[c])
        if m is not None:
            if m[0][-2:] == 'cm' and 150 <= int(m[0][:-2]) <= 193:
                print("valid:", test_hgt[c])
            elif m[0][-2:] == 'in' and 59 <= int(m[0][:-2]) <= 76:
                print("valid:", test_hgt[c])
            else:
                print("invalid:", test_hgt[c])
        else:
            print("invalid:", test_hgt[c])
    c += 1

print("Testing hcl validation...")
c = 0
while c < len(test_hcl):
    if 'hcl' in test_hcl[c]:
        if re.search('(?<=hcl:#)[A-Za-z0-9]{6}', test_hcl[c]):
            print("valid:", test_hcl[c])
        else:
            print("invalid:", test_hcl[c])
    c += 1

print("Testing ecl validation...")
c = 0
while c < len(test_ecl):
    if 'ecl' in test_ecl[c]:
        m = re.search('(?<=ecl:)[a-zA-Z0-9]{0,3}', test_ecl[c])
        if m[0] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            print("valid:", test_ecl[c])
        else:
            print("invalid:", test_ecl[c])
    c += 1

print("Testing pid validation...")
c = 0
while c < len(test_pid):
    if 'pid' in test_pid[c]:
        m = re.search('(?<=pid:)[0-9]{0,10}', test_pid[c])
        if len(m[0]) == 9:
            print("valid:", test_pid[c])
        else:
            print("invalid:", test_pid[c])
    c += 1


data = []
data2 = ['']

a = 0
b = 0

f = open("input/2020_4.txt", "r")
for x in f:
    data.append(x.rstrip())

while a < len(data):
    if data[a] == '':
        b += 1
        data2.append('')
    else:
        data2[b] += data[a] + ' '
    a += 1


def validate_password_elements(passports):

    c = 0
    checksum = 0
    valid_passports = 0

    while c < len(passports):
        if 'byr' in passports[c]:
            checksum += 1
        if 'iyr' in passports[c]:
            checksum += 1
        if 'eyr' in passports[c]:
            checksum += 1
        if 'hgt' in passports[c]:
            checksum += 1
        if 'hcl' in passports[c]:
            checksum += 1
        if 'ecl' in passports[c]:
            checksum += 1
        if 'pid' in passports[c]:
            checksum += 1
        if 'cid' in passports[c]:
            checksum += 0.5
        if checksum == 7 or checksum == 7.5:
            valid_passports += 1
        c += 1
        checksum = 0
    return valid_passports


def validate_password_contents(passports):

    c = 0
    checksum = 0
    valid_passports = 0

    while c < len(passports):
        if 'byr' in passports[c]:
            if 1920 <= int(re.search('(?<=byr:)[0-9]{4}', passports[c])[0]) <= 2002:
                checksum += 1
        if 'iyr' in passports[c]:
            if 2010 <= int(re.search('(?<=iyr:)[0-9]{4}', passports[c])[0]) <= 2020:
                checksum += 1
        if 'eyr' in passports[c]:
            if 2020 <= int(re.search('(?<=eyr:)[0-9]{4}', passports[c])[0]) <= 2030:
                checksum += 1
        if 'hgt' in passports[c]:
            m = re.search('(?<=hgt:)[0-9]{2,3}[a-z]{2}', passports[c])
            if m is not None:
                if m[0][-2:] == 'cm' and 150 <= int(m[0][:-2]) <= 193:
                    checksum += 1
                if m[0][-2:] == 'in' and 59 <= int(m[0][:-2]) <= 76:
                    checksum += 1
        if 'hcl' in passports[c]:
            if re.search('(?<=hcl:#)[A-Za-z0-9]{6}', passports[c]):
                checksum += 1
        if 'ecl' in passports[c]:
            m = re.search('(?<=ecl:)[a-zA-Z0-9]{0,3}', passports[c])
            if m[0] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                checksum += 1
        if 'pid' in passports[c]:
            m = re.search('(?<=pid:)[0-9]{0,10}', passports[c])
            if len(m[0]) == 9:
                checksum += 1
        if 'cid' in passports[c]:
            checksum += 0.5
        if checksum == 7 or checksum == 7.5:
            valid_passports += 1
        c += 1
        checksum = 0
    return valid_passports


print("Checking valid passports based on elements from input...")
print("There are", validate_password_elements(data2), "valid passwords with correct elements")

print("Checking valid passports based on content of the elements")
print("There are", validate_password_contents(test_set_invalid), "valid passwords with correct elements and valid values (invalid set)")
print("There are", validate_password_contents(test_set_valid), "valid passwords with correct elements and valid values (valid set)")
print("There are", validate_password_contents(data2), "valid passwords with correct elements and valid values with input file")


