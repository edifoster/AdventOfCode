datastream = []
i, j, k = 0, 0, 0

f = open("input/day6/test.txt", "r")
for x in f:
    datastream.append(x)


def find_marker(inputstring):
    a = []
    for b in inputstring:
        if b not in a and inputstring.count(b) > 1:
            a.append(b)
    if len(a) == 0:
        return True
    else:
        return False


for y in datastream:
    print("*********** Handling stream", j, "***********")
    while i < len(datastream[j]) - 14:
        while k < len(datastream[j])-4:
            if find_marker(datastream[j][k:k + 4]):
                print("Start-of-packet marker is complete after:", k + 4, "charaters on stream", j)
                k += len(datastream[j])
            k += 1
        if find_marker(datastream[j][i:i + 14]):
            print("Start-of-message marker is complete after:", i + 14, "charaters on stream", j)
            i += len(datastream[j])
        i += 1
    i, k = 0, 0
    j += 1
