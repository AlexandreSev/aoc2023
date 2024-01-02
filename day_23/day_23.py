# Part 1

if False:
    import sys

    sys.setrecursionlimit(4000)

    with open('input.txt', 'r') as f:
        maps = [list(line.strip()) for line in f]

    starting_y = 0
    for idx, c in enumerate(maps[0]):
        if c == '.':
            starting_x = idx
            break


    ending_y = len(maps) - 1
    for idx, c in enumerate(maps[-1]):
        if c == '.':
            ending_x = idx
            break


    def find_path_rec(x, y, seen_tiles):
        # print(f"Called with {x}, {y}")

        if x == ending_x and y == ending_y:
            return len(seen_tiles)

        if maps[y][x] == '>':
            possible_movements = [(1, 0)]
        elif maps[y][x] == '<':
            possible_movements = [(-1, 0)]
        elif maps[y][x] == '^':
            possible_movements = [(0, -1)]
        elif maps[y][x] == 'v':
            possible_movements = [(0, 1)]
        else:
            possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]


        longest_path_length = 0
        for dx, dy in possible_movements:
            if (
                (x + dx) >= 0 and (x + dx) < len(maps[0])
                and (y + dy) >= 0 and (y + dy) < len(maps)
                and maps[y + dy][x + dx] != '#' and (x + dx, y + dy) not in seen_tiles
            ):
                path_length = find_path_rec(x + dx, y + dy, seen_tiles | {(x + dx, y + dy)})
                longest_path_length = max(longest_path_length, path_length)

        return longest_path_length



    seen_tiles = {(starting_x, starting_y)}

    print(find_path_rec(starting_x, starting_y, seen_tiles) - 1)

# Part 2
import sys

sys.setrecursionlimit(8000)

with open('input.txt', 'r') as f:
    maps = [list(line.strip()) for line in f]

starting_y = 0
for idx, c in enumerate(maps[0]):
    if c == '.':
        starting_x = idx
        break


ending_y = len(maps) - 1
for idx, c in enumerate(maps[-1]):
    if c == '.':
        ending_x = idx
        break


# Micro opti
def find_first_intersection(x, y, seen_tiles):
    possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    true_movements = []
    for dx, dy in possible_movements:
        if (
            (x + dx) >= 0 and (x + dx) < len(maps[0])
            and (y + dy) >= 0 and (y + dy) < len(maps)
            and maps[y + dy][x + dx] != '#' and (x + dx, y + dy) not in seen_tiles
        ):
            true_movements.append((x + dx, y + dy))

    if len(true_movements) > 1:
        return x, y, seen_tiles, None

    if len(true_movements) == 0:
        return x, y, seen_tiles, (x == ending_x and y == ending_y)

    new_x, new_y = true_movements[0]
    return find_first_intersection(new_x, new_y, seen_tiles | {(new_x, new_y)})

lvl_1_x, lvl_1_y, lvl_1_path, _ = find_first_intersection(ending_x, ending_y, {(ending_x, ending_y)})

possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
lvl_1_possibilities = []
for dx, dy in possible_movements:
    if (
        (lvl_1_x + dx) >= 0 and (lvl_1_x + dx) < len(maps[0])
        and (lvl_1_y + dy) >= 0 and (lvl_1_y + dy) < len(maps)
        and maps[lvl_1_y + dy][lvl_1_x + dx] != '#' and (lvl_1_x + dx, lvl_1_y + dy) not in lvl_1_path
    ):
        lvl_1_possibilities.append((lvl_1_x + dx, lvl_1_y + dy))

lvl_2 = []
for x, y in lvl_1_possibilities:
    lvl_2_x, lvl_2_y, path, _ = find_first_intersection(x, y, lvl_1_path)
    lvl_2.append((lvl_2_x, lvl_2_y, path))


# Forced paths
def find_pool(x, y):
    seen_tiles = {(x, y)}
    possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    todos = [(x, y)]
    exits = []
    while todos:
        x, y = todos.pop()
        n_movements = 0
        for dx, dy in possible_movements:
            if (
                (x + dx) >= 0 and (x + dx) < len(maps[0])
                and (y + dy) >= 0 and (y + dy) < len(maps)
                and maps[y + dy][x + dx] != '#'
            ):
                n_movements += 1
                if (x + dx, y + dy) not in seen_tiles:
                    todos.append((x + dx, y + dy))
                    seen_tiles.add((x + dx, y + dy))

        if n_movements == 2:
            exits.append((x, y))
            if len(exits) > 2:
                return None

    return exits, seen_tiles






def find_forced_path():
    possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    forced_path = {}
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == '#':
                continue
            movements = []
            for dx, dy in possible_movements:
                if (
                    (x + dx) >= 0 and (x + dx) < len(maps[0])
                    and (y + dy) >= 0 and (y + dy) < len(maps)
                    and maps[y + dy][x + dx] != '#'
                ):
                    movements.append((x + dx, y + dy))

            if len(movements) < 3:
                continue

            forced_path[(x, y)] = {}
            for new_x, new_y in movements:
                final_x, final_y, seen_tiles, terminal = find_first_intersection(new_x, new_y, {(new_x, new_y), (x, y)})
                if terminal is None or terminal:
                    forced_path[(x, y)][(new_x, new_y)] = final_x, final_y, seen_tiles


    seen_intersect = set()
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if maps[y][x] == '#' or (x,y) in seen_intersect:
                continue
            movements = []
            for dx, dy in possible_movements:
                if (
                    (x + dx) >= 0 and (x + dx) < len(maps[0])
                    and (y + dy) >= 0 and (y + dy) < len(maps)
                    and maps[y + dy][x + dx] != '#'
                ):
                    movements.append((x + dx, y + dy))

            if len(movements) < 3:
                continue

            current_pool = find_pool(x, y)

            if current_pool is None:
                continue

            




    return forced_path

forced_paths = find_forced_path()

# import json
# with open('/tmp/forced_paths.txt', 'w') as f:
#     f.write(str(forced_paths))
# stop

class Logger:

    def __init__(self):
        self.current_max = -1
        self.nb_call = 0

    def log(self, x):
        self.nb_call += 1
        self.current_max = max(self.current_max, x)

        if self.nb_call % 10000 == 0:
            print(f"Current maximum - {self.current_max}")


logger = Logger()
# Path finding
def find_path_rec(x, y, seen_tiles):

    if x == ending_x and y == ending_y:
        return len(seen_tiles)

    if (lvl_1_x, lvl_1_y) in seen_tiles and (x, y) not in lvl_1_path:
        return 0

    lvl_2_path_exists = False
    for (lvl_2_x, lvl_2_y, lvl_2_path) in lvl_2:
        if (lvl_2_x, lvl_2_y) not in seen_tiles or (x, y) in lvl_2_path:
            lvl_2_path_exists = True
            break

    if not lvl_2_path_exists:
        return 0

    possible_movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]


    longest_path_length = 0
    for dx, dy in possible_movements:
        if (
            (x + dx) >= 0 and (x + dx) < len(maps[0])
            and (y + dy) >= 0 and (y + dy) < len(maps)
            and maps[y + dy][x + dx] != '#' and (x + dx, y + dy) not in seen_tiles
        ):
            if (x, y) in forced_paths and (x + dx, y + dy) in forced_paths[(x, y)]:
                shortcut = forced_paths[(x, y)][(x + dx, y + dy)]
                if shortcut is None:
                    continue
                shortcut_x, shortcut_y, shortcut_path = shortcut
                if (shortcut_x, shortcut_y) in seen_tiles:
                    continue
                path_length = find_path_rec(shortcut_x, shortcut_y, seen_tiles | shortcut_path)
            else:
                path_length = find_path_rec(x + dx, y + dy, seen_tiles | {(x + dx, y + dy)})
            longest_path_length = max(longest_path_length, path_length)

    logger.log(longest_path_length)
    return longest_path_length



seen_tiles = {(starting_x, starting_y)}

print(find_path_rec(starting_x, starting_y, seen_tiles) - 1)
