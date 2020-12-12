data = []
f = open("input/2020_12.txt", "r")
for x in f:
    data.append(x.rstrip())


def move_boat(order, position_x, position_y, direction):
    new_position_x, new_position_y = position_x, position_y
    if order[0] == 'F':
        order = direction + order[1:]
    if order[0] == 'N':
        new_position_y = int(position_y) + int(order[1:])
    elif order[0] == 'S':
        new_position_y = int(position_y) - int(order[1:])
    elif order[0] == 'E':
        new_position_x = int(position_x) + int(order[1:])
    elif order[0] == 'W':
        new_position_x = int(position_x) - int(order[1:])
    return new_position_x, new_position_y


def turn_boat(order, direction):
    compass = ['N', 'E', 'S', 'W']
    new_direction = direction
    direction_index = compass.index(direction)
    if order[0] == 'L':
        new_direction = compass[(int(direction_index) - int((int(order[1:]) / 90)))%4]
    elif order[0] == 'R':
        new_direction = compass[(int(direction_index) + int((int(order[1:]) / 90)))%4]
    return new_direction


def check_winds(ew, ns):
    if ew > 0:
        east_or_west = 'east'
    else:
        east_or_west = 'west'
    if ns > 0:
        north_or_south = 'north'
    else:
        north_or_south = 'south'
    return east_or_west, north_or_south


boat = [0, 0, 'E']
a = 0

while a < len(data):
    if data[a][0] in ['N', 'E', 'S', 'W', 'F']:
        boat[0], boat[1] = move_boat(data[a], boat[0], boat[1], boat[2])
    elif data[a][0] in ['L', 'R']:
        boat[2] = turn_boat(data[a], boat[2])
    a += 1


east_west, north_south = check_winds(boat[0],boat[1])

print("After the great storm we thought that the boat location and direction are:", east_west, abs(boat[0]), north_south, abs(boat[1]),
      "facing", boat[2], ".\nManhattan distance is therefore", abs(boat[0]) + abs(boat[1]))

# part 2


def move_boat_wp(order, position_x, position_y, waypoint_x, waypoint_y):
    distance = int(order[1:])
    new_position_x = position_x + (distance * waypoint_x)
    new_position_y = position_y + (distance * waypoint_y)
    return new_position_x, new_position_y


def turn_wp(order, waypoint_x, waypoint_y):
    new_waypoint_x, new_waypoint_y = int(waypoint_x), int(waypoint_y)
    if order[1:] == '180':
        new_waypoint_x = -1 * waypoint_x
        new_waypoint_y = -1 * waypoint_y
    elif order == 'R90' or order == 'L270':
        new_waypoint_x = waypoint_y
        new_waypoint_y = -1 * waypoint_x
    elif order == 'L90' or order == 'R270':
        new_waypoint_x = -1 * waypoint_y
        new_waypoint_y = waypoint_x
    return new_waypoint_x, new_waypoint_y


boat = [0, 0, 'E']
waypoint = [10, 1]
a = 0

while a < len(data):
    if data[a][0] in ['N', 'E', 'S', 'W']:
        waypoint[0], waypoint[1] = move_boat(data[a], waypoint[0], waypoint[1], 'X')
    elif data[a][0] == 'F':
        boat[0], boat[1] = move_boat_wp(data[a], boat[0], boat[1], waypoint[0], waypoint[1])
    elif data[a][0] in ['L', 'R']:
        waypoint[0], waypoint[1] = turn_wp(data[a], waypoint[0], waypoint[1])
    a += 1

east_west, north_south = check_winds(boat[0],boat[1])

print("\nAfter the great storm the boat location and direction really is:", east_west, abs(boat[0]), north_south, abs(boat[1]),
      "\nManhattan distance is therefore", abs(boat[0]) + abs(boat[1]))  ##23987 - 29231
