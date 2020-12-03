maprows = []
routex = 0
routey = 0

f = open("input/2020_3.txt", "r")
for x in f:
    maprows.append(x.rstrip())
routex = len(maprows[0])
routey = len(maprows)

def calculate_trees(slopex, slopey):
    n = 1
    a = slopey
    b = 1
    trees = 0
    while a < routey:
        if maprows[a][((b + (slopex * n)) % routex) - 1] == '#':
            trees += 1
        n += 1
        a += slopey
    return trees

print("There were",calculate_trees(1, 1),"on the route 1/1")
print("There were",calculate_trees(3, 1),"on the route 3/1")  #218
print("There were",calculate_trees(5, 1),"on the route 5/1")
print("There were",calculate_trees(7, 1),"on the route 7/1")
print("There were",calculate_trees(1, 2),"on the route 1/2")

print("Multiplied number of trees on the routes (1,1),(3,1),(5,1),(7,1) and (1,2) is",calculate_trees(1, 1) * calculate_trees(3, 1) * calculate_trees(5, 1) * calculate_trees(7, 1) * calculate_trees(1, 2))




