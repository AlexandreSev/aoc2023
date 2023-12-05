# Day 1.1
current_sum = 0
with open('day_1_1.txt', 'r') as f:
	for line in f.readlines():
		integers = [c for c in line if c.isnumeric()]
		current_sum += int(integers[0] + integers[-1])

print(current_sum)

# Day 1.2
current_sum = 0
with open('day_1_2.txt', 'r') as f:
	for line in f.readlines():
		first_integer = None
		last_integer = None

		for idx in range(len(line)):
			if line[idx].isnumeric():
				if first_integer is None:
					first_integer = line[idx]
				last_integer = line[idx]

			for number, spelling in zip('123456789', ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
				if idx + len(spelling) > len(line):
					continue
				if line[idx:idx+len(spelling)] == spelling:
					if first_integer is None:
						first_integer = number
					last_integer = number

		current_sum += int(first_integer + last_integer)
print(current_sum)