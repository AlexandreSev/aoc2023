# Part 1
from collections import defaultdict

from tqdm import tqdm

links = defaultdict(set)
with open('input.txt', 'r') as f:
    for line in f:
        source, connexions = line.strip().split(': ')
        for target in connexions.split(' '):
            links[target].add(source)
            links[source].add(target)


print(len(links))
def find_shortest_path(n1, links, memory):

    todos = [[n1]]
    seen = set()

    while todos:
        path = todos[0]
        todos = todos[1:]

        for n_co in links[path[-1]]:
            if (n1, n_co) not in memory:
                memory[(n1, n_co)] = path + [n_co]
                todos.append(path + [n_co])



memory = {}
for n1 in tqdm(links):
    find_shortest_path(n1, links, memory)

counter = defaultdict(int)

for path in memory.values():
    for idx in range(len(path) - 1):
        n1, n2 = path[idx], path[idx + 1]
        n1, n2 = min(n1, n2), max(n1, n2)

        counter[(n1, n2)] += 1

to_cut = sorted(counter.items(), key=lambda x: -x[1])
for (n1, n2), _ in to_cut[:3]:
    links[n1].remove(n2)
    links[n2].remove(n1)

memory_bis = {}
find_shortest_path(n1, links, memory_bis)

print(len(memory_bis), len(links) - len(memory_bis))
print(len(memory_bis) * (len(links) - len(memory_bis)))