# Part 1

def find_hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


with open('input.txt', 'r') as f:
    instructions = next(f).strip().split(',')


result = 0
for instruction in instructions:
    # print(instruction, find_hash(instruction))
    result += find_hash(instruction)

print(result)


# Part 2

def find_hash(s):
    current_value = 0
    for c in s:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value


class Boxes:

    def __init__(self):
        self.boxes = [[] for _ in range(256)]

    def remove(self, label):
        h = find_hash(label)
        box = self.boxes[h]
        idx_to_remove = None
        for idx, lens in enumerate(box):
            if lens[0] == label:
                idx_to_remove = idx
                break

        if idx_to_remove is not None:
            box.pop(idx_to_remove)

    def add(self, label, focal):
        h = find_hash(label)
        box = self.boxes[h]
        has_been_added = False
        for idx, lens in enumerate(box):
            if lens[0] == label:
                lens[1] = focal
                has_been_added = True
                break

        if not has_been_added:
            box.append([label, focal])

    def focusing_power(self):
        focusing_power = 0
        for box_idx, box in enumerate(self.boxes):
            for lens_idx, lens in enumerate(box):
                focusing_power += (box_idx + 1) * (lens_idx + 1) * lens[1]
        return focusing_power




with open('input.txt', 'r') as f:
    instructions = next(f).strip().split(',')


boxes = Boxes()
for instruction in instructions:
    # print(instruction)
    if instruction[-1] == '-':
        label = instruction[:-1]
        # print(f'Removing {label}')
        boxes.remove(label)
    else:
        label, focal = instruction.split('=')
        # print(f"Adding {label}, {focal}")
        boxes.add(label, int(focal))

    # print(boxes.boxes[:4])

print(boxes.focusing_power())


