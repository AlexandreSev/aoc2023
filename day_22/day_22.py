# Part 1

bricks = []
with open('input.txt', 'r') as f:
    for line in f:
        pos1, pos2 = line.strip().split('~')
        pos1 = tuple(map(int, pos1.split(',')))
        pos2 = tuple(map(int, pos2.split(',')))

        bricks.append((pos1, pos2))


bricks = sorted(bricks, key=lambda x: min(x[0][2], x[1][2]))


min_x, max_x, min_y, max_y, min_z, max_z = 999999, 0, 999999, 0, 999999, 0
for pos1, pos2 in bricks:
    min_x = min(min_x, pos1[0], pos2[0])
    max_x = max(max_x, pos1[0], pos2[0])
    min_y = min(min_y, pos1[1], pos2[1])
    max_y = max(max_x, pos1[1], pos2[1])
    min_z = min(min_z, pos1[2], pos2[2])
    max_z = max(max_z, pos1[2], pos2[2])

ground = [
            [
                [None for _ in range(min_z, max_z + 1)]
                for _ in range(min_x, max_x + 1)
            ] for y in range(min_y, max_y + 1)
        ]

def find_last_not_null(zs):
    for idx, z in enumerate(zs[::-1]):
        if z is not None:
            return len(zs) - idx
    return 0


for idx, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
    low_z = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            low_z = max(low_z, find_last_not_null(ground[y][x]))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(low_z, low_z + (z2 - z1 + 1)):
                ground[y][x][z] = idx

links = {i: [] for i in range(len(bricks))}

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        zs = ground[y][x]
        for i in range(len(zs) - 1):
            if zs[i] is not None and zs[i + 1] is not None and zs[i] != zs[i + 1]:
                links[zs[i + 1]].append(zs[i])

can_be_desintegrated = set(i for i in range(len(bricks)))

for linked in links.values():
    linked = list(set(linked))
    if len(linked) == 1 and linked[0] in can_be_desintegrated:
        can_be_desintegrated.remove(linked[0])

print(len(can_be_desintegrated))


# Part 2

bricks = []
with open('input.txt', 'r') as f:
    for line in f:
        pos1, pos2 = line.strip().split('~')
        pos1 = tuple(map(int, pos1.split(',')))
        pos2 = tuple(map(int, pos2.split(',')))

        bricks.append((pos1, pos2))


bricks = sorted(bricks, key=lambda x: min(x[0][2], x[1][2]))


min_x, max_x, min_y, max_y, min_z, max_z = 999999, 0, 999999, 0, 999999, 0
for pos1, pos2 in bricks:
    min_x = min(min_x, pos1[0], pos2[0])
    max_x = max(max_x, pos1[0], pos2[0])
    min_y = min(min_y, pos1[1], pos2[1])
    max_y = max(max_x, pos1[1], pos2[1])
    min_z = min(min_z, pos1[2], pos2[2])
    max_z = max(max_z, pos1[2], pos2[2])

ground = [
            [
                [None for _ in range(min_z, max_z + 1)]
                for _ in range(min_x, max_x + 1)
            ] for y in range(min_y, max_y + 1)
        ]

def find_last_not_null(zs):
    for idx, z in enumerate(zs[::-1]):
        if z is not None:
            return len(zs) - idx
    return 0


for idx, ((x1, y1, z1), (x2, y2, z2)) in enumerate(bricks):
    low_z = 0
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            low_z = max(low_z, find_last_not_null(ground[y][x]))
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            for z in range(low_z, low_z + (z2 - z1 + 1)):
                ground[y][x][z] = idx

links = {i: [] for i in range(len(bricks))}

for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        zs = ground[y][x]
        for i in range(len(zs) - 1):
            if zs[i] is not None and zs[i + 1] is not None and zs[i] != zs[i + 1]:
                links[zs[i + 1]].append(zs[i])


can_be_desintegrated = set(i for i in range(len(bricks)))

reverse_links = {i: [] for i in range(len(bricks))}

for idx in links:
    links[idx] = list(set(links[idx]))
    for other_idx in links[idx]:
        reverse_links[other_idx].append(idx)

for linked in links.values():
    if len(linked) == 1 and linked[0] in can_be_desintegrated:
        can_be_desintegrated.remove(linked[0])

n_fall = 0

for idx in range(len(bricks)):
    if idx in can_be_desintegrated:
        continue

    to_check = reverse_links[idx]
    will_fall = {idx}
    next_to_check = []
    while True:
        for brick in to_check:
            if len(set(links[brick]) - will_fall) == 0:
                will_fall.add(brick)
                next_to_check += reverse_links[brick]
            else:
                next_to_check.append(brick)

        next_to_check.sort()
        if next_to_check == to_check:
            break
        to_check = next_to_check
        next_to_check = []
    n_fall += len(will_fall) - 1

print(n_fall)


