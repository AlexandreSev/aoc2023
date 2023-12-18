# Part 1

right_left_delta = {
    ('U', 'U'): 0,
    ('U', 'D'): 0,
    ('U', 'R'): 1,
    ('U', 'L'): -1,
    ('D', 'U'): 0,
    ('D', 'D'): 0,
    ('D', 'R'): -1,
    ('D', 'L'): 1,
    ('R', 'U'): -1,
    ('R', 'D'): 1,
    ('R', 'R'): 0,
    ('R', 'L'): 0,
    ('L', 'U'): 1,
    ('L', 'D'): -1,
    ('L', 'R'): 0,
    ('L', 'L'): 0,
}

last_d = None
right_left_counter = 0
instructions = []
with open('test.txt', 'r') as f:
    for line in f:
        d, n, c = line.strip().split(' ')
        instructions.append((d, int(n), c))
        if last_d is not None:
            right_left_counter += right_left_delta[(last_d, d)]
        last_d = d

min_x, max_x, min_y, max_y = 0, 0, 0, 0
x, y = 0, 0
for d, n, _ in instructions:
    if d == 'U':
        y -= n
        min_y = min(min_y, y)
    elif d == 'D':
        y += n
        max_y = max(max_y, y)
    elif d == 'R':
        x += n
        max_x = max(max_x, x)
    elif d == 'L':
        x -= n
        min_x = min(min_x, x)

x -= min_x
y -= min_y

len_x = max_x - min_x
len_y = max_y - min_y

maps = [['.' for _ in range(len_x + 1)] for _ in range(len_y + 1)]
maps[y][x] = '#'

starting_point_to_flood = set()
for d, n, _ in instructions:
    for _ in range(n):
        if d == 'U':
            y -= 1
            if right_left_counter > 0:
                starting_point_to_flood.add((x + 1, y))
            else:
                starting_point_to_flood.add((x - 1, y))
        elif d == 'D':
            y += 1
            if right_left_counter > 0:
                starting_point_to_flood.add((x - 1, y))
            else:
                starting_point_to_flood.add((x + 1, y))
        elif d == 'R':
            x += 1
            if right_left_counter > 0:
                starting_point_to_flood.add((x, y + 1))
            else:
                starting_point_to_flood.add((x, y - 1))
        elif d == 'L':
            x -= 1
            if right_left_counter > 0:
                starting_point_to_flood.add((x, y - 1))
            else:
                starting_point_to_flood.add((x, y + 1))
        maps[y][x] = '#'

while starting_point_to_flood:
    x, y = starting_point_to_flood.pop()
    if maps[y][x] == '#':
        continue
    maps[y][x] = '#'
    for x2, y2 in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
        if x2 >= 0 and x2 <= len_x and y2 >= 0 and y2 <= len_y and maps[y2][x2] == '.':
            starting_point_to_flood.add((x2, y2))

result = 0
for row in maps:
    result += len([c for c in row if c == '#'])

print(result)

# Part 2

right_left_delta = {
    ('U', 'U'): 0,
    ('U', 'D'): 0,
    ('U', 'R'): 1,
    ('U', 'L'): -1,
    ('D', 'U'): 0,
    ('D', 'D'): 0,
    ('D', 'R'): -1,
    ('D', 'L'): 1,
    ('R', 'U'): -1,
    ('R', 'D'): 1,
    ('R', 'R'): 0,
    ('R', 'L'): 0,
    ('L', 'U'): 1,
    ('L', 'D'): -1,
    ('L', 'R'): 0,
    ('L', 'L'): 0,
}

from_int_to_d = {0: 'R', 1: 'D', 2: 'L', 3: 'U'}

last_d = None
right_left_counter = 0
instructions = []
with open('input.txt', 'r') as f:
    for line in f:
        d, n, c = line.strip().split(' ')
        n = int(c[2: -2], 16)
        d = from_int_to_d[int(c[-2], 16)]
        instructions.append((d, int(n), c))
        if last_d is not None:
            right_left_counter += right_left_delta[(last_d, d)]
        last_d = d

if right_left_counter < 0:
    instructions = instructions[::-1]


min_x, max_x, min_y, max_y = 0, 0, 0, 0
x, y = 0, 0
for d, n, _ in instructions:
    if d == 'U':
        y -= n
        min_y = min(min_y, y)
    elif d == 'D':
        y += n
        max_y = max(max_y, y)
    elif d == 'R':
        x += n
        max_x = max(max_x, x)
    elif d == 'L':
        x -= n
        min_x = min(min_x, x)

x -= min_x
y -= min_y

len_x = max_x - min_x
len_y = max_y - min_y


result = 0
for idx, (d, n, _) in enumerate(instructions):
    last_d = instructions[idx - 1][0]

    if idx < len(instructions) - 1:
        next_d = instructions[idx + 1][0]
    else:
        next_d = instructions[0][0]

    if d == 'U':
        y -= n
        result -= ((n + 1) * x)
    elif d == 'D':
        y += n
        result += ((n + 1) * (x + 1))
    elif d == 'R':
        x += n
        if last_d == 'D' and next_d == 'U':
            result += n - 1
        elif last_d == 'D' and next_d == 'D':
            result -= (x + 1 - n)
        elif last_d == 'U' and next_d == 'U':
            result += x
    elif d == 'L':
        x -= n
        if last_d == 'D' and next_d == 'D':
            result -= (x + 1)
        elif last_d == 'U' and next_d == 'D':
            result += (n - 1)
        elif last_d == 'U' and next_d == 'U':
            result += x + n

print(result)



