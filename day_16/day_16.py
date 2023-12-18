# Part 1

maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))


seen_cases = {}
beams = [((0, -1), (0, 1))] # list of beams to process, starting point x direction

case_direction_mappings = {
    '.': {
        (-1, 0): [(-1, 0)],
        (1, 0): [(1, 0)],
        (0, -1): [(0, -1)],
        (0, 1): [(0, 1)]
    },
    '|': {
        (-1, 0): [(-1, 0)],
        (1, 0): [(1, 0)],
        (0, -1): [(-1, 0), (1, 0)],
        (0, 1): [(-1, 0), (1, 0)]
    },
    '-': {
        (-1, 0): [(0, -1), (0, 1)],
        (1, 0): [(0, -1), (0, 1)],
        (0, -1): [(0, -1)],
        (0, 1): [(0, 1)]
    },
    '/': {
        (-1, 0): [(0, 1)],
        (1, 0): [(0, -1)],
        (0, -1): [(1, 0)],
        (0, 1): [(-1, 0)] 
    },
    '\\': {
        (-1, 0): [(0, -1)],
        (1, 0): [(0, 1)],
        (0, -1): [(-1, 0)],
        (0, 1): [(1, 0)] 
    }
}


draft = [['.' for _ in range(len(maps[0]))] for _ in range(len(maps))]

while beams:
    (case_y, case_x), (direction_y, direction_x) = beams.pop()
    while ((case_y, case_x) not in seen_cases
        or (direction_y, direction_x) not in seen_cases[(case_y, case_x)]):

        if (case_y, case_x) not in seen_cases:
            seen_cases[(case_y, case_x)] = set()
        seen_cases[(case_y, case_x)].add((direction_y, direction_x))

        
        case_x += direction_x
        case_y += direction_y
        if case_x < 0 or case_x >= len(maps[0]) or case_y < 0 or case_y >= len(maps):
            break
        draft[case_y][case_x] = '#'

        if (case_y, case_x) not in seen_cases:
            seen_cases[(case_y, case_x)] = set()

        next_dirs = list(case_direction_mappings[maps[case_y][case_x]][(direction_y, direction_x)])

        while len(next_dirs) > 1:
            next_dir = next_dirs.pop()
            if next_dir not in seen_cases[(case_y, case_x)]:
                beams.append(((case_y, case_x), next_dir))

        next_dir = next_dirs.pop()
        if next_dir in seen_cases[(case_y, case_x)]:
            break

        direction_y, direction_x = next_dir


# print("\n".join(["".join(row) for row in draft]))

print(len(seen_cases) - 1)

# Part 2
from tqdm import tqdm

maps = []
with open('input.txt', 'r') as f:
    for line in f:
        maps.append(list(line.strip()))


case_direction_mappings = {
    '.': {
        (-1, 0): [(-1, 0)],
        (1, 0): [(1, 0)],
        (0, -1): [(0, -1)],
        (0, 1): [(0, 1)]
    },
    '|': {
        (-1, 0): [(-1, 0)],
        (1, 0): [(1, 0)],
        (0, -1): [(-1, 0), (1, 0)],
        (0, 1): [(-1, 0), (1, 0)]
    },
    '-': {
        (-1, 0): [(0, -1), (0, 1)],
        (1, 0): [(0, -1), (0, 1)],
        (0, -1): [(0, -1)],
        (0, 1): [(0, 1)]
    },
    '/': {
        (-1, 0): [(0, 1)],
        (1, 0): [(0, -1)],
        (0, -1): [(1, 0)],
        (0, 1): [(-1, 0)] 
    },
    '\\': {
        (-1, 0): [(0, -1)],
        (1, 0): [(0, 1)],
        (0, -1): [(-1, 0)],
        (0, 1): [(1, 0)] 
    }
}


starting_config = [((y, -1), (0, 1)) for y in range(len(maps))]
starting_config += [((y, len(maps[0])), (0, -1)) for y in range(len(maps))]
starting_config += [((-1, x), (1, 0)) for x in range(len(maps[0]))]
starting_config += [((len(maps), x), (-1, 0)) for x in range(len(maps[0]))]


max_energized_tiles = 0

for start_conf in tqdm(starting_config):

    seen_cases = {}
    beams = [start_conf] # list of beams to process, starting point x direction
    while beams:
        (case_y, case_x), (direction_y, direction_x) = beams.pop()
        while ((case_y, case_x) not in seen_cases
            or (direction_y, direction_x) not in seen_cases[(case_y, case_x)]):

            if (case_y, case_x) not in seen_cases:
                seen_cases[(case_y, case_x)] = set()
            seen_cases[(case_y, case_x)].add((direction_y, direction_x))

            
            case_x += direction_x
            case_y += direction_y
            if case_x < 0 or case_x >= len(maps[0]) or case_y < 0 or case_y >= len(maps):
                break

            if (case_y, case_x) not in seen_cases:
                seen_cases[(case_y, case_x)] = set()

            next_dirs = list(case_direction_mappings[maps[case_y][case_x]][(direction_y, direction_x)])

            while len(next_dirs) > 1:
                next_dir = next_dirs.pop()
                if next_dir not in seen_cases[(case_y, case_x)]:
                    beams.append(((case_y, case_x), next_dir))

            next_dir = next_dirs.pop()
            if next_dir in seen_cases[(case_y, case_x)]:
                break

            direction_y, direction_x = next_dir

            max_energized_tiles = max(len(seen_cases) - 1, max_energized_tiles)

print(max_energized_tiles)



