# Part 1
total = 0
with open('day_4.txt', 'r') as f:
	for line in f.readlines():
		numbers = line.strip().split(': ')[1]
		winning, gotten = numbers.split(' | ')
		winning = set([int(i) for i in winning.split(' ') if i])
		gotten = set([int(i) for i in gotten.split(' ') if i])
		score = 0
		if len(gotten & winning):
			score = 2 ** (len(gotten & winning) - 1)
		total += score

print(total)

# Part 2
from collections import defaultdict

total = defaultdict(int)
with open('day_4.txt', 'r') as f:
	for line in f.readlines():

		card_id, numbers = line.strip().split(': ')
		card_id = int(card_id.split(' ')[-1])

		total[card_id] += 1
		winning, gotten = numbers.split(' | ')
		winning = set([int(i) for i in winning.split(' ') if i])
		gotten = set([int(i) for i in gotten.split(' ') if i])
		
		for idx in range(card_id + 1, card_id + 1 + len(gotten & winning)):
			total[idx] += total[card_id]

print(sum(total.values()))