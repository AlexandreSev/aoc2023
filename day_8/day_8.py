# Part 1

with open('input.txt', 'r') as f:
    instructions = next(f).strip()
    next(f)
    nodes = {}
    for line in f:
        node, linked = line.strip().split(' = ')
        link_l, link_r = linked.split(', ')
        link_l = link_l[1:]
        link_r = link_r[:-1]
        nodes[node] = {'L': link_l, 'R': link_r}

current_node = 'AAA'
step = 0
while current_node != 'ZZZ':
    current_node = nodes[current_node][instructions[step%len(instructions)]]
    step += 1

print(step)


# Part 2
from collections import defaultdict


current_nodes = []

with open('input.txt', 'r') as f:
    instructions = next(f).strip()
    next(f)
    nodes = {}
    for line in f:
        node, linked = line.strip().split(' = ')
        link_l, link_r = linked.split(', ')
        link_l = link_l[1:]
        link_r = link_r[:-1]
        nodes[node] = {'L': link_l, 'R': link_r}
        if node[-1] == 'A':
            current_nodes.append(node)

offsets = {}
winning_loop_positions = {}
loop_lengths = {}

for node_idx, current_node in enumerate(current_nodes):
    step = 0
    seen_nodes = {} # (node, step % intructions)
    seen_nodes_arrays = []
    while (current_node, step % len(instructions)) not in seen_nodes:
        memory_key = (current_node, step % len(instructions))
        seen_nodes[memory_key] = step
        seen_nodes_arrays.append(memory_key)
        current_node = nodes[current_node][instructions[step % len(instructions)]]
        step += 1
    
    memory_key = (current_node, step % len(instructions))
    offset = seen_nodes[memory_key]
    loop = seen_nodes_arrays[seen_nodes[memory_key]:]
    winning_loop_pos = [idx for idx, node in enumerate(loop) if node[0][-1] == 'Z']

    offsets[node_idx] = offset
    winning_loop_positions[node_idx] = winning_loop_pos
    loop_lengths[node_idx] = len(loop)


step = offsets[0] + winning_loop_positions[0][0] # There is only 1 winning pos for idx 0
current_loop_len = loop_lengths[0]
for idx in range(1, len(current_nodes)):
    print(idx, step, current_loop_len)
    working_steps = []
    for _ in range(2):
        while all([((step - offsets[idx] - w_p) % loop_lengths[idx] != 0) for w_p in winning_loop_positions[idx]]):
            step += current_loop_len
        working_steps.append(step)
        step += current_loop_len
    current_loop_len = working_steps[1] - working_steps[0]
    step = working_steps[0]

print("Won !!!")
print(step)