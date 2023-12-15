# Part 1

maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))

transposed_maps = [[row[j] for row in maps] for j in range(len(maps[0]))]

total_load = 0
for row in transposed_maps:
    next_idx = 0
    for idx, c in enumerate(row):
        if c == 'O':
            total_load += len(row) - next_idx
            next_idx += 1
        elif c == '#':
            next_idx = idx + 1

print(total_load)


# Part 2
import json
from tqdm import tqdm


maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))

initial_maps = maps

def rotate(l):
    transposed = [[row[j] for row in l] for j in range(len(l[0]))]
    return [row[::-1] for row in transposed]

def tilt_west(maps):
    titled_maps = []
    for row in maps:
        new_row = ['.' for c in row]
        next_idx = 0
        for idx, c in enumerate(row):
            if c == 'O':
                new_row[next_idx] = 'O'
                next_idx += 1
            elif c == '#':
                new_row[idx] = '#'
                next_idx = idx + 1
        titled_maps.append(new_row)

    return titled_maps


loop = {}

maps = rotate(rotate(maps))
nb_cycles = 1000000000
for c_idx in tqdm(range(nb_cycles)):
    for _ in range(4):
        maps = rotate(maps)
        maps = tilt_west(maps)

    # print("\n".join(["".join(row) for row in rotate(rotate(maps))]))
    # print()

    memory_key = json.dumps(maps)
    if memory_key in loop:
        break
    loop[memory_key] = c_idx

loop_len = c_idx - loop[memory_key]
nb_cycles_left = ((nb_cycles - loop[memory_key]) % loop_len) - 1

for c_idx in tqdm(range(nb_cycles_left)):
    for _ in range(4):
        maps = rotate(maps)
        maps = tilt_west(maps)

maps = rotate(rotate(maps))
# print("\n".join(["".join(row) for row in maps]))
# print()

total_load = 0
for idx, row in enumerate(maps):
    current_load = len(maps) - idx
    total_load += (current_load * len([c for c in row if c == 'O']))

print(total_load)




