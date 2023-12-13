# Part 1

def check_vertical_reflexion(pattern, idx):
    left_idx = idx
    right_idx = idx + 1
    while left_idx >= 0 and right_idx < len(pattern[0]):
        for row in pattern:
            if row[left_idx] != row[right_idx]:
                return False
        left_idx -= 1
        right_idx += 1
    return True



def find_vertical_reflexion(pattern):
    possible_vertical_line = {i for i in range(len(pattern[0]) - 1)}
    for row in pattern:
        idx_to_remove = set()
        for idx in possible_vertical_line:
            if row[idx] != row[idx + 1]:
                idx_to_remove.add(idx)

        possible_vertical_line -= idx_to_remove

    for idx in possible_vertical_line:
        if check_vertical_reflexion(pattern, idx):
            return idx

    return None


def find_reflexion(pattern):
    # print(f"Called with pattern {pattern}")
    idx = find_vertical_reflexion(pattern)
    if idx is not None:
        # print(f"Found reflexion in column {idx}")
        return idx + 1

    transposed_pattern = [[row[j] for row in pattern] for j in range(len(pattern[0]))]
    
    idx = find_vertical_reflexion(transposed_pattern)
    if idx is not None:
        # print(f"Found reflexion in row {idx}")
        return (idx + 1) * 100


with open('input.txt', 'r') as f:
    current_pattern = []
    results = 0
    for line in f:
        if not line.strip():
            results += find_reflexion(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(list(line.strip()))

results += find_reflexion(current_pattern)

print(results)

# Part 2
def check_vertical_reflexion(pattern, idx):
    left_idx = idx
    right_idx = idx + 1
    nb_diff = 0
    while left_idx >= 0 and right_idx < len(pattern[0]):
        for row in pattern:
            if row[left_idx] != row[right_idx]:
                nb_diff += 1
                if nb_diff > 1:
                    return False
        left_idx -= 1
        right_idx += 1

    if nb_diff == 0:
        return False
    return True

def find_vertical_reflexion(pattern):
    possible_vertical_line = {i for i in range(len(pattern[0]) - 1)}
    seen_idx = set()
    for row in pattern:
        idx_to_remove = set()
        for idx in possible_vertical_line:
            if row[idx] != row[idx + 1]:
                idx_to_remove.add(idx)

        for idx in idx_to_remove:
            if idx in seen_idx and idx in possible_vertical_line:
                possible_vertical_line.remove(idx)
            seen_idx.add(idx)

    for idx in possible_vertical_line:
        if check_vertical_reflexion(pattern, idx):
            return idx

    return None

def find_reflexion(pattern):
    # print(f"Called with pattern {pattern}")
    idx = find_vertical_reflexion(pattern)
    if idx is not None:
        # print(f"Found reflexion in column {idx}")
        return idx + 1

    transposed_pattern = [[row[j] for row in pattern] for j in range(len(pattern[0]))]
    
    idx = find_vertical_reflexion(transposed_pattern)
    if idx is not None:
        # print(f"Found reflexion in row {idx}")
        return (idx + 1) * 100

with open('input.txt', 'r') as f:
    current_pattern = []
    results = 0
    for line in f:
        if not line.strip():
            results += find_reflexion(current_pattern)
            current_pattern = []
        else:
            current_pattern.append(list(line.strip()))

results += find_reflexion(current_pattern)

print(results)