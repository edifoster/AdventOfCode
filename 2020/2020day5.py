import copy

data = []

f = open("input/2020_5.txt", "r")
for x in f:
    data.append(x.rstrip())

testset = ['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

def row_calulator(row):
    i = 0
    upper = 127
    lower = 0
    while i < 7:
        if row[i] == 'F':
            upper = upper - ((upper - lower + 1) / 2)
        elif row[i] == 'B':
            lower = lower + ((upper - lower + 1) / 2)
        else:
            print("Invalid character", row[i], i)
            break
        i += 1
        #print(lower, upper)
    if lower == upper:
        return lower
    else:
        print("Invalid calculation", lower, upper, row)



def column_calulator(column):
    i = 7
    upper = 7
    lower = 0
    while i < 10:
        if column[i] == 'L':
            upper = upper - ((upper - lower + 1) / 2)
        elif column[i] == 'R':
            lower = lower + ((upper - lower + 1) / 2)
        else:
            print("Invalid character", column[i], i)
            break
        i += 1
        #print(lower, upper)
    if lower == upper:
        return lower
    else:
        print("Invalid calculation", lower, upper, column)

def maximum_seat_id(seats):
    a = 0
    max_seat_id = 0
    while a < len(seats):
        seat_id = row_calulator(seats[a]) * 8 + column_calulator(seats[a])
        if seat_id > max_seat_id:
            max_seat_id = seat_id
        a += 1
    return max_seat_id

print("\nPart 1")
print("Maximum seat id from test set is ",maximum_seat_id(testset))
print("Maximum seat id from input is ",maximum_seat_id(data))

plane = []
pr = 0
pc = 0
while pr < 128:
    while pc < 8:
        pseat = []
        pseat.append(pr)
        pseat.append(pc)
        pseat.append(pr * 8 + pc)
        plane.append(pseat)
        pc += 1
    pr += 1
    pc = 0

def remove_occupied_seats(boardpasses, seatmap):
    a = 0
    while a < len(boardpasses):
        seat = []
        seat.append(row_calulator(boardpasses[a]))
        seat.append(column_calulator(boardpasses[a]))
        seat.append(row_calulator(boardpasses[a]) * 8 + column_calulator(boardpasses[a]))
        if seat in seatmap:
            seatmap.remove(seat)
        a += 1
    return seatmap

def check_nearby_seats_by_id(openseats, seatmap):
    a = 0
    while a < len(openseats):
        seatmap.remove(openseats[a])
        a += 1

    a = 0
    while a < len(openseats):
        previous_seat = []
        next_seat = []
        for seat in seatmap:
            if seat[2] == (openseats[a][2] - 1):
                previous_seat = seat
            elif seat[2] == (openseats[a][2] + 1):
                next_seat = seat
        if previous_seat != [] and next_seat != []:
            return openseats[a]

        a += 1


os = remove_occupied_seats(data, copy.deepcopy(plane))
myseat = check_nearby_seats_by_id(os, copy.deepcopy(plane))

print("\nPart 2")
print("My seat is at row:", myseat[0],"column:", myseat[1],"and it has id:", myseat[2])

