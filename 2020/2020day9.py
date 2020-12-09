data, data_test = [], []

f = open("input/2020_9_test.txt", "r")
for x in f:
    data_test.append(x.rstrip())

f = open("input/2020_9.txt", "r")
for x in f:
    data.append(x.rstrip())


def check_sum(dataset, preamble, offset=0, valid=False):
    a = preamble
    while a < len(dataset):

        valid = False
        for b in dataset[offset:preamble + offset]:
            for c in dataset[offset:preamble + offset]:
                # print(int(b) + int(c), data[a])
                if b != c and int(b) + int(c) == int(dataset[a]):
                    # print("Hit! Where", b, "and", c, "equals", dataset[a])
                    offset += 1
                    valid = True
                if valid:
                    break
            if valid:
                break
        if not valid:
            return dataset[a], a, valid
        a += 1
    return 0, valid


def find_sum(dataset, starting_point):
    a = starting_point
    while a > 0:
        b, sub_sum = 2, [int(dataset[a-1])]
        while sum(sub_sum) < int(dataset[starting_point]):
            sub_sum.append(int(dataset[a-b]))
            b += 1
        if sum(sub_sum) == int(dataset[starting_point]):
            return sub_sum
        a -= 1
    return []


# value,  value_index, status = check_sum(data_test, 5)
value, value_index, status = check_sum(data, 25)

if not status:
    print(value, "is not following the Rule")
else:
    print("All values are following the Rule")

weak_list = sorted(find_sum(data, value_index))

if weak_list:
    print("Encryption weakness found! It is ", int(weak_list[0]) + int(weak_list[-1]))
else:
    print("List was bulletproof!")