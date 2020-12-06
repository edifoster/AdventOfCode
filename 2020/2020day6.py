data = []

f = open("input/2020_6.txt", "r")
for x in f:
    data.append(x.rstrip())

a, answers, group_data = 0, [], []
for a in data:
    if a != '' or a is None:
        group_data.append(a)
    else:
        answers.append(group_data)
        group_data = []
answers.append(group_data)


def check_unique_yes_answers_in_group(group_answers):
    b, q = 0, []
    while b < len(group_answers):
        c = 0
        while c < len(group_answers[b]):
            if group_answers[b][c] not in q:
                q.append(group_answers[b][c])
            c += 1
        b += 1
    return q, len(q)


def check_common_yes_answers_in_group(group_answers):
    d = 0
    common_yes = group_answers[0]
    while d < len(group_answers[0]):
        e = 0
        while e < len(group_answers):
            if group_answers[0][d] not in group_answers[e]:
                common_yes = common_yes.replace(group_answers[0][d], '')
                e = len(group_answers)
            e += 1
        d += 1
    return common_yes, len(common_yes)


yes_answers_total_part1, yes_answers_total_part2 = 0, 0
for group in answers:
    yes_answers_total_part1 += check_unique_yes_answers_in_group(group)[1]
    yes_answers_total_part2 += check_common_yes_answers_in_group(group)[1]


print("\nPart 1:\n Sum of unique answers for each group is", yes_answers_total_part1)

print("\nPart 2:\n Sum of answers common for each group is", yes_answers_total_part2)

