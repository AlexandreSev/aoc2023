# Part 1
if False:
	with open('day_5.txt', 'r') as f:
		line = next(f)
		initial_seeds = map(int, line.strip().split(': ')[-1].split(' '))

		maps = {}
		
		current_category = None
		for line in f:
			line = line.strip()
			if not line:
				continue
			
			if line[0].isalpha():
				source, destination = line.split(' ')[0].split('-to-')
				current_category = (source, destination)
				if source not in maps:
					maps[source] = {}
				if destination not in maps[source]:
					maps[source][destination] = {}
			else:
				destination_start, source_start, length = map(int, line.split(' '))
				maps[current_category[0]][current_category[1]][(source_start, length)] = destination_start - source_start


	def find_location(category, nb):
		# print(f"Called with {category} {nb}")
		if category == 'location':
			return nb
		if category not in maps:
			return None

		next_nb = None
		for destination, mapping in maps[category].items():
			for (range_start, range_len), offset in mapping.items():
				if range_start <= nb and range_start + range_len > nb:
					next_nb = nb + offset
					# print(f"range_start: {range_start}")
			if next_nb is None:
				next_nb = nb
			
			result = find_location(destination, next_nb)
			if result:
				return result
		return None


	min_loc = 99999999999
	for seed in initial_seeds:
		location = find_location('seed', seed)
		print(seed, location)
		min_loc = min(min_loc, location)

	print(min_loc)

# Part 2
with open('day_5.txt', 'r') as f:
	line = next(f)
	initial_seeds = list(map(int, line.strip().split(': ')[-1].split(' ')))
	initial_seeds = [initial_seeds[x: x + 2] for x in range(0, len(initial_seeds), 2)]

	maps = {}
	
	current_category = None
	for line in f:
		line = line.strip()
		if not line:
			continue
		
		if line[0].isalpha():
			source, destination = line.split(' ')[0].split('-to-')
			current_category = (source, destination)
			if source not in maps:
				maps[source] = {}
			if destination not in maps[source]:
				maps[source][destination] = {}
		else:
			destination_start, source_start, length = map(int, line.split(' '))
			maps[current_category[0]][current_category[1]][(source_start, length)] = destination_start - source_start


def find_location(category, ranges):
	print(f"Called with {category} {ranges}")
	if category == 'location':
		return ranges

	next_category = list(maps[category].keys())[0]
	mapping = maps[category][next_category]
	next_ranges = []
	for source_range, offset in mapping.items():
		next_round_ranges = []
		for goal_range in ranges:
			destination_range, left_ranges = find_intersect(goal_range, source_range)
			next_round_ranges += left_ranges
			if destination_range is not None:
				next_ranges.append((destination_range[0] + offset, destination_range[1]))
		ranges = next_round_ranges

	return find_location(next_category, next_ranges + ranges)



def min_range(ranges):
	return min([range_start for (range_start, _) in ranges])

def find_intersect(r1, r2):
	start_1, len_1 = r1
	start_2, len_2 = r2

	if start_1 < start_2 and start_1 + len_1 < start_2:
		return None, [r1]

	if start_2 < start_1 and start_2 + len_2 < start_1:
		return None, [r1]

	start_f = max(start_1, start_2)
	len_f = min(len_1 - max(0, (start_2 - start_1)), len_2 - max(0, (start_1 - start_2)))

	left_ranges = []
	if start_1 < start_f:
		left_ranges.append((start_1, (start_f - start_1)))
	if start_1 + len_1 > start_f + len_f:
		left_ranges.append((start_f + len_f, start_1 + len_1 - start_f - len_f))

	return ((start_f, len_f), left_ranges)



min_loc = 99999999999
for seed_range in initial_seeds:
	location_ranges = find_location('seed', [seed_range])
	print(seed_range, location_ranges)
	min_loc = min(min_loc, min_range(location_ranges))

print(min_loc)
