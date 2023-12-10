# Part 1

maps = []

with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        maps.append(list(line.strip()))
        for x, c in enumerate(line.strip()):
            if c == 'S':
                starting_x, starting_y = x, y


pipes = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(1, 0), (0, -1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)]
}

if maps[starting_y][starting_x + 1] in ('-', '7', 'J'):
    next_x = starting_x + 1
    next_y = starting_y
elif maps[starting_y + 1][starting_x] in ('|', 'J', 'L'):
    next_x = starting_x
    next_y = starting_y + 1
elif maps[starting_y - 1][starting_x] in ('|', '7', 'F'):
    next_x = starting_x
    next_y = starting_y - 1


steps = 0
current_x, current_y = starting_x, starting_y
while (next_x, next_y) != (starting_x, starting_y):
    steps += 1
    previous_x, previous_y = current_x, current_y
    current_x, current_y = next_x, next_y
    for dx, dy in pipes[maps[current_y][current_x]]:
        if (current_x + dx, current_y + dy) != (previous_x, previous_y):
            next_x, next_y = (current_x + dx, current_y + dy)

print((steps + 1) / 2)

# Part 2
maps = []

with open('input.txt', 'r') as f:
    for y, line in enumerate(f):
        maps.append(list(line.strip()))
        for x, c in enumerate(line.strip()):
            if c == 'S':
                starting_x, starting_y = x, y


pipes = {
    '|': [(0, 1), (0, -1)],
    '-': [(1, 0), (-1, 0)],
    'L': [(1, 0), (0, -1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(-1, 0), (0, 1)],
    'F': [(1, 0), (0, 1)]
}

if maps[starting_y][starting_x + 1] in ('-', '7', 'J'):
    next_x = starting_x + 1
    next_y = starting_y
elif maps[starting_y + 1][starting_x] in ('|', 'J', 'L'):
    next_x = starting_x
    next_y = starting_y + 1
elif maps[starting_y - 1][starting_x] in ('|', '7', 'F'):
    next_x = starting_x
    next_y = starting_y - 1


loop = []
current_x, current_y = starting_x, starting_y
while (next_x, next_y) != (starting_x, starting_y):
    loop.append((current_x, current_y))
    previous_x, previous_y = current_x, current_y
    current_x, current_y = next_x, next_y
    for dx, dy in pipes[maps[current_y][current_x]]:
        if (current_x + dx, current_y + dy) != (previous_x, previous_y):
            next_x, next_y = (current_x + dx, current_y + dy)

loop.append((current_x, current_y))

loop_idx = {(x + 1, y + 1): idx for idx, (x, y) in enumerate(loop)}

draft_maps = [['0'] + ['.' for _ in range(len(maps[0]))] + ['0'] for _ in range(len(maps))]
draft_maps = [['0' for _ in range(len(maps[0]) + 2)]] + draft_maps + [['0' for _ in range(len(maps[0]) + 2)]]

for (x, y) in loop:
    draft_maps[y + 1][x + 1] = 'X'

max_x = len(draft_maps[0]) - 1.5
max_y = len(draft_maps) - 1.5

print(max_x, max_y)

flood_starting_point = []
for x in range(len(draft_maps[0]) - 1):
    flood_starting_point.append((x + 0.5, 0.5))
    flood_starting_point.append((x + 0.5, max_y))

for y in range(1, len(draft_maps) - 1):
    flood_starting_point.append((0.5, y + 0.5))
    flood_starting_point.append((max_x, y + 0.5))


seen_points = set(flood_starting_point)
while flood_starting_point:
    current_x, current_y = flood_starting_point.pop()
    # print(f"Starting with {current_x, current_y}")
    if (
        current_x < max_x and
        (
            draft_maps[int(current_y + 0.5)][int(current_x + 0.5)] != 'X' or 
            draft_maps[int(current_y - 0.5)][int(current_x + 0.5)] != 'X' or 
            abs(loop_idx[(int(current_x + 0.5), int(current_y + 0.5))] - loop_idx[(int(current_x + 0.5), int(current_y - 0.5))]) not in (1, len(loop) - 1)
        )
    ):
        if (current_x + 1, current_y) not in seen_points: 
            flood_starting_point.append((current_x + 1, current_y))
        seen_points.add((current_x + 1, current_y))
        # print(1)
        if draft_maps[int(current_y - 0.5)][int(current_x + 0.5)] != 'X':
            # print(1.1)
            draft_maps[int(current_y - 0.5)][int(current_x + 0.5)] = 'O'
        if draft_maps[int(current_y + 0.5)][int(current_x + 0.5)] != 'X':
            # print(1.2)
            draft_maps[int(current_y + 0.5)][int(current_x + 0.5)] = 'O'

    if (
        current_x > 0.5 and
        (
            draft_maps[int(current_y + 0.5)][int(current_x - 0.5)] != 'X' or 
            draft_maps[int(current_y - 0.5)][int(current_x - 0.5)] != 'X' or 
            abs(loop_idx[(int(current_x - 0.5), int(current_y + 0.5))] - loop_idx[(int(current_x - 0.5), int(current_y - 0.5))]) not in (1, len(loop) - 1)
        )
    ):
        # print(2)
        if (current_x - 1, current_y) not in seen_points:
            flood_starting_point.append((current_x - 1, current_y))
        seen_points.add((current_x - 1, current_y))
        if draft_maps[int(current_y - 0.5)][int(current_x - 0.5)] != 'X':
            # print(2.1)
            draft_maps[int(current_y - 0.5)][int(current_x - 0.5)] = 'O'
        if draft_maps[int(current_y + 0.5)][int(current_x - 0.5)] != 'X':
            # print(2.2)
            draft_maps[int(current_y + 0.5)][int(current_x - 0.5)] = 'O'

    if (
        current_y < max_y and
        (
            draft_maps[int(current_y + 0.5)][int(current_x + 0.5)] != 'X' or 
            draft_maps[int(current_y + 0.5)][int(current_x - 0.5)] != 'X' or 
            abs(loop_idx[(int(current_x + 0.5), int(current_y + 0.5))] - loop_idx[(int(current_x - 0.5), int(current_y + 0.5))]) not in (1, len(loop) - 1)
        )
    ):
        # print(3)
        if (current_x, current_y + 1) not in seen_points:
            flood_starting_point.append((current_x, current_y + 1))
        seen_points.add((current_x, current_y + 1))
        if draft_maps[int(current_y + 0.5)][int(current_x - 0.5)] != 'X':
            # print(3.1)
            draft_maps[int(current_y + 0.5)][int(current_x - 0.5)] = 'O'
        if draft_maps[int(current_y + 0.5)][int(current_x + 0.5)] != 'X':
            # print(3.2)
            draft_maps[int(current_y + 0.5)][int(current_x + 0.5)] = 'O'

    if (
        current_y > 0.5 and
        (
            draft_maps[int(current_y - 0.5)][int(current_x + 0.5)] != 'X' or 
            draft_maps[int(current_y - 0.5)][int(current_x - 0.5)] != 'X' or 
            abs(loop_idx[(int(current_x + 0.5), int(current_y - 0.5))] - loop_idx[(int(current_x - 0.5), int(current_y - 0.5))]) not in (1, len(loop) - 1)
        )
    ):
        # print(4)
        if (current_x, current_y - 1) not in seen_points:
            flood_starting_point.append((current_x, current_y - 1))
        seen_points.add((current_x, current_y - 1))
        if draft_maps[int(current_y - 0.5)][int(current_x - 0.5)] != 'X':
            # print(4.1)
            draft_maps[int(current_y - 0.5)][int(current_x - 0.5)] = 'O'
        if draft_maps[int(current_y - 0.5)][int(current_x + 0.5)] != 'X':
            # print(4.2)
            draft_maps[int(current_y - 0.5)][int(current_x + 0.5)] = 'O'

print('\n'.join([''.join(m) for m in draft_maps]))
nb_enclosed = 0
for row in draft_maps:
    nb_enclosed += len([c for c in row if c == '.'])

print(nb_enclosed)

