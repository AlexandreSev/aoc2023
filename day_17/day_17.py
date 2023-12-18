# Part 1
from queue import PriorityQueue

maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(map(int, line.strip())))

current_x, current_y = (0, 0)
current_loss = 0
min_estimate = len(maps) + len(maps[0])
current_dir = ((0, 0), 0)

memory = {}
todo = PriorityQueue()
todo.put((current_loss + min_estimate, (current_x, current_y), current_loss, current_dir))

min_loss = 999999999999

idx = 0
t = 10

while True:
    item = todo.get()
    # print(item)
    estimate_loss, (x, y), loss, current_dir = item

    if estimate_loss > min_loss: 
        break

    memory_key = (x, y, current_dir[0])

    if memory_key in memory:
        step_to_loss = memory[memory_key]
        should_continue = False
        for step in range(1, current_dir[1] + 1):
            if step_to_loss.get(step, 9999999) <= loss:
                should_continue = True
                break
        if should_continue:
            continue
    else:
        memory[memory_key] = {}

    memory[memory_key][current_dir[1]] = loss

    idx += 1

    # if idx % t == 0:
    #     print(idx)
    #     t *= 10


    if x == len(maps[0]) - 1 and y == len(maps) - 1:
        min_loss = min(loss, min_loss)

    if y > 0 and current_dir[0] != 'S' and (current_dir[0] != 'N' or current_dir[1] < 3):
        next_estimate = (len(maps) - 1 - y + 1) + (len(maps[0]) - 1 - x)
        next_loss = loss + maps[y - 1][x]
        if current_dir[0] == 'N':
            next_dir = ('N', current_dir[1] + 1)
        else:
            next_dir = ('N', 1)
        if (next_loss + next_estimate) < min_loss:
            # print('Add N')
            todo.put((next_loss + next_estimate, (x, y - 1), next_loss, next_dir))
        
    if x > 0 and current_dir[0] != 'E' and (current_dir[0] != 'W' or current_dir[1] < 3):
        next_estimate = (len(maps) - 1 - y) + (len(maps[0]) - 1 - x + 1)
        next_loss = loss + maps[y][x - 1]
        if current_dir[0] == 'W':
            next_dir = ('W', current_dir[1] + 1)
        else:
            next_dir = ('W', 1)
        if (next_loss + next_estimate) < min_loss:
            # print('Add W')
            todo.put((next_loss + next_estimate, (x - 1, y), next_loss, next_dir))
        
    if y < len(maps) - 1 and current_dir[0] != 'N' and (current_dir[0] != 'S' or current_dir[1] < 3):
        next_estimate = (len(maps) - 1 - y - 1) + (len(maps[0]) - 1 - x)
        next_loss = loss + maps[y + 1][x]
        if current_dir[0] == 'S':
            next_dir = ('S', current_dir[1] + 1)
        else:
            next_dir = ('S', 1)
        if (next_loss + next_estimate) < min_loss:
            # print('Add S')
            todo.put((next_loss + next_estimate, (x, y + 1), next_loss, next_dir))
        
    if x < len(maps[0]) - 1 and current_dir[0] != 'W' and (current_dir[0] != 'E' or current_dir[1] < 3):
        next_estimate = (len(maps) - 1 - y) + (len(maps[0]) - 1 - x - 1)
        next_loss = loss + maps[y][x + 1]
        if current_dir[0] == 'E':
            next_dir = ('E', current_dir[1] + 1)
        else:
            next_dir = ('E', 1)
        if (next_loss + next_estimate) < min_loss:
            # print('Add E')
            todo.put((next_loss + next_estimate, (x + 1, y), next_loss, next_dir))

# print(idx)
print(min_loss)


# Part 2
print('######')
print('Part 2')
print('######')
from queue import PriorityQueue

maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(map(int, line.strip())))

len_x = len(maps[0])
len_y = len(maps)

print(len_x, len_y)

current_x, current_y = (0, 0)
current_loss = 0
min_estimate = len_x + len_y
current_dir = ((0, 0), 0)

memory = {}
todo = PriorityQueue()
todo.put((current_loss + min_estimate, (current_x, current_y), current_loss, current_dir))

min_loss = 999999999999

idx = 0
t = 10

while True:
    item = todo.get()
    # print(item)
    estimate_loss, (x, y), loss, current_dir = item

    if estimate_loss > min_loss: 
        break

    memory_key = (x, y, current_dir[0])

    if memory_key in memory:
        step_to_loss = memory[memory_key]
        should_continue = False
        for step in range(1, current_dir[1] + 1):
            if step_to_loss.get(step, 9999999) <= loss:
                should_continue = True
                break
        if should_continue:
            continue
    else:
        memory[memory_key] = {}

    memory[memory_key][current_dir[1]] = loss

    idx += 1

    if idx % t == 0:
        print(idx)
        t *= 10


    if x == len_x - 1 and y == len_y - 1:
        min_loss = min(loss, min_loss)

    if current_dir[0] != 'S' and ((current_dir[0] != 'N' and y > 3) or (current_dir[0] == 'N' and current_dir[1] < 10 and y > 0)):
        if current_dir[0] == 'N':
            next_dir = ('N', current_dir[1] + 1)
            next_loss = loss + maps[y - 1][x]
            next_y = y - 1
        else:
            next_dir = ('N', 4)
            next_loss = loss + maps[y - 1][x] + maps[y - 2][x] + maps[y - 3][x] + maps[y - 4][x]
            next_y = y - 4
        next_estimate = (len_y - 1 - next_y) + (len_x - 1 - x)
        if (next_loss + next_estimate) < min_loss:
            # print('Add N')
            todo.put((next_loss + next_estimate, (x, next_y), next_loss, next_dir))
        
    if current_dir[0] != 'E' and ((current_dir[0] != 'W' and x > 3) or (current_dir[0] == 'W' and current_dir[1] < 10 and x > 0)):
        if current_dir[0] == 'W':
            next_dir = ('W', current_dir[1] + 1)
            next_loss = loss + maps[y][x - 1]
            next_x = x - 1
        else:
            next_dir = ('W', 4)
            next_loss = loss + maps[y][x - 1] + maps[y][x - 2] + maps[y][x - 3] + maps[y][x - 4]
            next_x = x - 4
        next_estimate = (len_y - 1 - y) + (len_x - 1 - next_x)
        if (next_loss + next_estimate) < min_loss:
            # print('Add W')
            todo.put((next_loss + next_estimate, (next_x, y), next_loss, next_dir))
        
    if current_dir[0] != 'N' and ((current_dir[0] != 'S' and y < len_y - 4) or (current_dir[0] == 'S' and current_dir[1] < 10 and y < len_y - 1)):
        if current_dir[0] == 'S':
            next_dir = ('S', current_dir[1] + 1)
            next_loss = loss + maps[y + 1][x]
            next_y = y + 1
        else:
            next_dir = ('S', 4)
            next_loss = loss + maps[y + 1][x] + maps[y + 2][x] + maps[y + 3][x] + maps[y + 4][x]
            next_y = y + 4
        next_estimate = (len_y - 1 - next_y) + (len_x - 1 - x)
        if (next_loss + next_estimate) < min_loss:
            # print('Add S')
            todo.put((next_loss + next_estimate, (x, next_y), next_loss, next_dir))
        
    if current_dir[0] != 'W' and ((current_dir[0] != 'E' and x < len_x - 4) or (current_dir[0] == 'E' and current_dir[1] < 10 and x < len_x - 1)):
        if current_dir[0] == 'E':
            next_dir = ('E', current_dir[1] + 1)
            next_loss = loss + maps[y][x + 1]
            next_x = x + 1
        else:
            next_dir = ('E', 4)
            next_loss = loss + maps[y][x + 1] + maps[y][x + 2] + maps[y][x + 3] + maps[y][x + 4]
            next_x = x + 4
        next_estimate = (len_y - 1 - y) + (len_x - 1 - next_x)
        if (next_loss + next_estimate) < min_loss:
            # print('Add E')
            todo.put((next_loss + next_estimate, (next_x, y), next_loss, next_dir))

print(idx)
print(min_loss)