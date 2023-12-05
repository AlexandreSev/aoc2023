import re
 
 # Part 1
max_cubes = {'red': 12, 'green': 13, 'blue': 14}
current_sum = 0
with open('day_2_1.txt', 'r') as f:
    for line in f.readlines():
        game_id = int(line.split(':')[0][5:])
        games = line.split(': ')[1].split('; ')
        possible = True
        for game in games:
            cubes = game.split(', ')
            for cube in cubes:
                nb, color = cube.split(' ')
                if int(nb) > max_cubes[color.strip()]:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            current_sum += int(game_id)
print(current_sum)


# Part 2
import re

current_sum = 0
with open('day_2_2.txt', 'r') as f:
    for line in f.readlines():
        game_id = int(line.split(':')[0][5:])
        games = line.split(': ')[1].split('; ')
        max_cubes = {'red': 0, 'green': 0, 'blue': 0}
        for game in games:
            cubes = game.split(', ')
            for cube in cubes:
                number, color = cube.split(' ')
                color = color.strip()
                max_cubes[color] = max(max_cubes[color], int(number))
        current_sum += max_cubes['red'] * max_cubes['green'] * max_cubes['blue']
print(current_sum)


