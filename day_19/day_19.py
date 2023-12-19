# Part 1
workflows = {}
parts = []
with open('input.txt', 'r') as f:
    for line in f:
        if line == '\n':
            break

        name, rules = line.strip().split('{')
        rules = rules[:-1].split(',')
        rules = [rule.split(':') for rule in rules]
        workflows[name] = rules

    for line in f:
        part = line.strip()[1:-1].split(',')
        part = [int(p.split('=')[1]) for p in part]
        parts.append({'x': part[0], 'm': part[1], 'a': part[2], 's': part[3]})


def process_workflow(part, rules):
    for rule in rules:
        if len(rule) == 1:
            return rule[0]

        key = rule[0][0]
        if rule[0][1] == '>':
            if part[key] > int(rule[0][2:]):
                return rule[1]
            continue
        elif rule[0][1] == '<':
            if part[key] < int(rule[0][2:]):
                return rule[1]
            continue
        else:
            raise Exception('Rule not understood')

result = 0
for part in parts:
    current_workflow = 'in'
    while current_workflow not in ('A', 'R'):
        current_workflow = process_workflow(part, workflows[current_workflow])

    if current_workflow == 'A':
        result += sum(part.values())

print(result)

# Part 2
from copy import deepcopy

workflows = {}
parts = []
with open('input.txt', 'r') as f:
    for line in f:
        if line == '\n':
            break

        name, rules = line.strip().split('{')
        rules = rules[:-1].split(',')
        rules = [rule.split(':') for rule in rules]
        workflows[name] = rules

ranges_to_process = [({'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}, 'in')]
accepted_range = []
while ranges_to_process:
    xmas_range, workflow = ranges_to_process.pop()

    if workflow == 'R':
        continue

    elif workflow == 'A':
        accepted_range.append(xmas_range)
        continue

    for rule in workflows[workflow]:

        if len(rule) == 1:
            ranges_to_process.append((xmas_range, rule[0]))
            break

        rule, next_workflow = rule
        key = rule[0]
        next_range = deepcopy(xmas_range)
        if rule[1] == '>':
            next_range[key][0] = max(next_range[key][0], int(rule[2:]) + 1)
            if next_range[key][0] <= next_range[key][1]:
                ranges_to_process.append((next_range, next_workflow))
            xmas_range[key][1] = min(xmas_range[key][1], int(rule[2:]))
            if xmas_range[key][0] > xmas_range[key][1]:
                break

        elif rule[1] == '<':
            next_range[key][1] = min(next_range[key][1], int(rule[2:]) - 1)
            if next_range[key][0] <= next_range[key][1]:
                ranges_to_process.append((next_range, next_workflow))
            xmas_range[key][0] = max(xmas_range[key][0], int(rule[2:]))
            if xmas_range[key][0] > xmas_range[key][1]:
                break

result = 0
for xmas_range in accepted_range:
    current_result = 1
    for key in 'xmas':
        current_result *= (xmas_range[key][1] - xmas_range[key][0] + 1)
    result += current_result

print(result)
