# Part 1
maps = []

with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))


row_to_add = set()
for i, row in enumerate(maps):
    if all([c == '.' for c in row]):
        row_to_add.add(i)

columns_to_add = set()
for i in range(len(maps[0])):
    if all([row[i] == '.' for row in maps]):
        columns_to_add.add(i)


galaxies = []
for y, row in enumerate(maps):
    for x, c in enumerate(row):
        if c == '#':
            galaxies.append((x, y))


def distances_with_expansions(x1, y1, x2, y2, row_to_add, columns_to_add):
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    distance = x2 - x1 + y2 - y1 
    distance += len([x for x in range(x1 + 1, x2) if x in columns_to_add])
    distance += len([y for y in range(y1 + 1, y2) if y in row_to_add])

    return distance

total_distance = 0
for i, (x1, y1) in enumerate(galaxies):
    for x2, y2 in galaxies[i + 1:]:
        distance = distances_with_expansions(x1, y1, x2, y2, row_to_add, columns_to_add)
        # print(f"({x1}, {y1}) - ({x2, y2}): {distance}")
        total_distance += distance

print(total_distance)

# Part 2
maps = []

with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))


row_to_add = set()
for i, row in enumerate(maps):
    if all([c == '.' for c in row]):
        row_to_add.add(i)

columns_to_add = set()
for i in range(len(maps[0])):
    if all([row[i] == '.' for row in maps]):
        columns_to_add.add(i)


galaxies = []
for y, row in enumerate(maps):
    for x, c in enumerate(row):
        if c == '#':
            galaxies.append((x, y))


def distances_with_expansions(x1, y1, x2, y2, row_to_add, columns_to_add):
    if x2 < x1:
        x1, x2 = x2, x1
    if y2 < y1:
        y1, y2 = y2, y1

    distance = x2 - x1 + y2 - y1 
    distance += (len([x for x in range(x1 + 1, x2) if x in columns_to_add]) * 999999)
    distance += (len([y for y in range(y1 + 1, y2) if y in row_to_add]) * 999999)

    return distance

total_distance = 0
for i, (x1, y1) in enumerate(galaxies):
    for x2, y2 in galaxies[i + 1:]:
        distance = distances_with_expansions(x1, y1, x2, y2, row_to_add, columns_to_add)
        # print(f"({x1}, {y1}) - ({x2, y2}): {distance}")
        total_distance += distance

print(total_distance)