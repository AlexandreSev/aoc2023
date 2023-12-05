# Day 3 part 1

symbol_pos = set()

maps = []
with open('day_3.txt', 'r') as f:
	for y, line in enumerate(f.readlines()):
		maps.append(line.strip())
		for x, c in enumerate(line.strip()):
			if not c.isnumeric() and c != '.':
				symbol_pos.add((x, y))

number_pos = []
for y, row in enumerate(maps):
	current_num = ""
	start, end = -1, -1
	for x, c in enumerate(row):
		if c.isnumeric():
			if current_num:
				# print(f"Here 1: {c}")
				current_num += c
				end = x
			else:
				# print(f"Here 2: {c}")
				start = x
				end = x
				current_num = c
		else:
			if current_num:
				# print(f"Found: {current_num} in pos {y}, {start} -> {end}")
				number_pos.append((int(current_num), y, start, end))
				current_num = ""
				start, end = -1, -1
	if current_num:
		# print(f"Found: {current_num} in pos {y}, {start} -> {end}")
		number_pos.append((int(current_num), y, start, end))
		current_num = ""
		start, end = -1, -1

engine_part = 0
for number, y_num, start, end in sorted(number_pos, key=lambda x: x[1:]):
	to_include = False
	for x in range(start-1, end+2):
		for y in range(y_num - 1, y_num + 2):
			if (x, y) in symbol_pos:
				to_include = True
				break
		if to_include:
			break
	# print(f"Y: {y_num}, X: {start} -> {end}, NB: {number}, to_include: {to_include}")
	if to_include:
		engine_part += number

print(engine_part)


# Day 3 part 2
from collections import defaultdict

symbol_pos = set()

maps = []
with open('day_3.txt', 'r') as f:
	for y, line in enumerate(f.readlines()):
		maps.append(line.strip())
		for x, c in enumerate(line.strip()):
			if not c.isnumeric() and c != '.':
				symbol_pos.add((x, y, c))

number_pos = []
for y, row in enumerate(maps):
	current_num = ""
	start, end = -1, -1
	for x, c in enumerate(row):
		if c.isnumeric():
			if current_num:
				# print(f"Here 1: {c}")
				current_num += c
				end = x
			else:
				# print(f"Here 2: {c}")
				start = x
				end = x
				current_num = c
		else:
			if current_num:
				# print(f"Found: {current_num} in pos {y}, {start} -> {end}")
				number_pos.append((int(current_num), y, start, end))
				current_num = ""
				start, end = -1, -1
	if current_num:
		# print(f"Found: {current_num} in pos {y}, {start} -> {end}")
		number_pos.append((int(current_num), y, start, end))
		current_num = ""
		start, end = -1, -1


gears_numbers = defaultdict(set)
for number, y_num, start, end in sorted(number_pos, key=lambda x: x[1:]):
	for x in range(start-1, end+2):
		for y in range(y_num - 1, y_num + 2):
			if (x, y, '*') in symbol_pos:
				gears_numbers[(x, y)].add((number, y_num, start, end))
	# print(f"Y: {y_num}, X: {start} -> {end}, NB: {number}, to_include: {to_include}")

gears_ratio_sums = 0
for gear, numbers in gears_numbers.items():
	if len(numbers) != 2:
		continue
	numbers = list(numbers)
	gears_ratio_sums += numbers[0][0] * numbers[1][0]

print(gears_ratio_sums)



