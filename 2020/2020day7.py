data = []

f = open("input/2020_7.txt", "r")
for x in f:
    data.append(x.rstrip())

bags, bags2 = [], {}


for word in data:
    main_bag = word.split()[0] + ' ' + word.split()[1]
    # main_bag[-1] = main_bag[-1].replace('bags', 'bag')
    a, contain_bag = 0, []

    while (a + 1) * 4 < len(word.split()):
        cb = word.split()[4 + (4 * a):8 + (4 * a)]
        cb[0] = cb[0].replace('no', '0')
        contain_bag = [cb[1] + ' ' + cb[2], cb[0]]
        contain_bag2 = (int(cb[0]), cb[1] + ' ' + cb[2])
        a += 1
        bag = (main_bag, contain_bag)
        bags.append(bag)
        bags2.setdefault(main_bag, []).append(contain_bag2)


def check_bags(colour, outer_colour=[], checked_colours=[]):
    check_colour = []

    for b in bags:
        if colour in b[1] and b[0] not in outer_colour:
            outer_colour.append(b[0])
            check_colour.append(b[0])
    if colour not in checked_colours:
        checked_colours.append(colour)
        for c in check_colour:
            # print("Checking", c)
            check_bags(c)
    return outer_colour


colour_to_be_checked = 'shiny gold'
chb = check_bags('shiny gold')
print("\n", colour_to_be_checked, "bag can be found from these bags:", chb, "\nwhat equals", len(chb), "different colours")


def count_children(colour):
    count = 1
    for quantity, colour in bags2[colour]:
        if colour != 'other bags.':
            count += int(quantity) * count_children(colour)
    return count


colour_to_be_counted = 'shiny gold'
print("\n", colour_to_be_counted, "bag needs to fit", count_children(colour_to_be_counted)-1, "bags inside")
