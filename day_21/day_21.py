# Part 1

maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))


starting_x = None
for y, row in enumerate(maps):
    for x, c in enumerate(row):
        if c == 'S':
            starting_x, starting_y = x, y
            break

    if starting_x is not None:
        break


current_positions = {(starting_x, starting_y)}
for step in range(64):
    next_positions = set()
    for (x, y) in current_positions:
        
        if x > 0 and maps[y][x - 1] in 'S.':
            next_positions.add((x - 1, y))
        
        if x < len(maps[0]) and maps[y][x + 1] in 'S.':
            next_positions.add((x + 1, y))
        
        if y > 0 and maps[y-1][x] in 'S.':
            next_positions.add((x, y - 1))
        
        if y < len(maps) and maps[y + 1][x] in 'S.':
            next_positions.add((x, y + 1))

    current_positions = next_positions

print(len(current_positions))

# Part 2
from copy import deepcopy
import json

n_steps = 26501365

def get_garden_coord(x, y, len_x, len_y):
    if x >= 0:
        garden_x = x // len_x
    else:
        garden_x = - (-(x + 1) // len_x ) - 1
    if y >= 0:
        garden_y = y // len_y
    else:
        garden_y = - (-(y + 1) // len_y ) - 1

    return garden_x, garden_y
        


maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))


starting_x = None
for y, row in enumerate(maps):
    for x, c in enumerate(row):
        if c == 'S':
            starting_x, starting_y = x, y
            break

    if starting_x is not None:
        break

len_x = len(maps[0])
len_y = len(maps)


max_coord_garden = int((n_steps - starting_x - 1) / len_x)
final_n_step_left_straight = n_steps - 66 - max_coord_garden * 131
final_n_step_left_diag = final_n_step_left_straight - 66


tmp = [
    ((0, 65), final_n_step_left_straight),
    ((130, 65), final_n_step_left_straight),
    ((65, 0), final_n_step_left_straight),
    ((65, 130), final_n_step_left_straight),
    ((0, 0), final_n_step_left_diag),
    ((0, 130), final_n_step_left_diag),
    ((130, 0), final_n_step_left_diag),
    ((130, 130), final_n_step_left_diag),
]


results = {}
for (starting_x, starting_y), n_steps_left in tmp:

    current_positions = {(starting_x, starting_y)}

    seen_positions = {0: set(), 1: set()}

    first_garden_accession = {}

    for step in range(n_steps):

        if (step + 1) % 100 == 0:
            print(step + 1)

        next_positions = set()
        for (x, y) in current_positions:

            if x > 0 and maps[y][x - 1] in 'S.':
                next_positions.add((x - 1, y))
            
            if x < len(maps[0]) - 1 and maps[y][x + 1] in 'S.':
                next_positions.add((x + 1, y))
            
            if y > 0 and maps[y-1][x] in 'S.':
                next_positions.add((x, y - 1))
            
            if y < len(maps) - 1 and maps[y + 1][x] in 'S.':
                next_positions.add((x, y + 1))

        current_positions = (next_positions - seen_positions[(step + 1) % 2])
        seen_positions[(step + 1) % 2] |= next_positions

        if ((step + 1) % len_x) == n_steps_left:
            results[(starting_x, starting_y), step + 1] = {0: len(seen_positions[0]), 1: len(seen_positions[1])}

            if step + 1 > 131 and results[(starting_x, starting_y), step + 1] == results[(starting_x, starting_y), step + 1 - 131]:
                break


final_count = 0
to_add = results[(0, 0), 457][1]
current = 1
n = 0
step = 66
while step + 131 < n_steps:
    final_count += results[(0, 65), 392][current]
    current = 1 - current
    step += 131
    n += 1

for starting_point in [(0, 65), (130, 65), (65, 0), (65, 130)]:
    to_add += results[(starting_point, 130)][current]

for starting_point in [(0, 0), (0, 130), (130, 0), (130, 130)]:
    to_add += results[(starting_point, 64)][current]


current = 1
for n_L in range(n - 1, -1, -1):
    n_not_current = n_L // 2
    final_count += n_not_current * results[(0, 0), 457][1 - current]
    final_count += (n_L - n_not_current) * results[(0, 0), 457][current]
    
    entering_pair = 1 - current if n_L % 2 else current

    for starting_point in [(0, 0), (0, 130), (130, 0), (130, 130)]:
        to_add += results[(starting_point, 195)][entering_pair]
        to_add += results[(starting_point, 64)][1 - entering_pair]

    current = 1 - current
    

final_count *= 4
final_count += to_add
print(final_count)

