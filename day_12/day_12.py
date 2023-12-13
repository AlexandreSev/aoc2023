# Part 1

def recursive_solver(code, groups, current_sol=""):
    # print(f"Called with {code}, {groups}")

    if len(code) == 0:
        return (1, [current_sol]) if len(groups) == 0 else (0, [])
    if len(groups) == 0:
        return (1, [current_sol]) if all([c != '#' for c in code]) else (0, [])
    if len(code) < groups[0]:
        return 0, []

    c = code[0]
    if c == '.':
        return recursive_solver(code[1:], groups, current_sol + ".")
    elif c == '#':
        for i in range(1, groups[0]):
            if code[i] == '.':
                return 0, []
        if len(code) > groups[0] and code[groups[0]] == '#':
            return 0, []
        next_sol = current_sol + '#' * groups[0] + ('.' if len(code) > groups[0] else '')
        return recursive_solver(code[groups[0] + 1:], groups[1:], next_sol)
    elif c == '?':
        current_result, sols = recursive_solver(code[1:], groups, current_sol + '.')
        can_be_hashtag = True
        for i in range(1, groups[0]):
            if code[i] == '.':
                can_be_hashtag = False
                break
        if len(code) > groups[0] and code[groups[0]] == '#':
            can_be_hashtag = False
        if can_be_hashtag:
            next_sol = current_sol + '#' * groups[0] + ('.' if len(code) > groups[0] else '')
            current_result_bis, sols_bis = recursive_solver(code[groups[0] + 1:], groups[1:], next_sol)
            current_result += current_result_bis
            sols += sols_bis
        return current_result, sols


results = 0
with open('input.txt', 'r') as f:
    for line in f:
        code, groups = line.strip().split(' ')
        groups = list(map(int, groups.split(',')))
        result, possibilites = recursive_solver(code, groups)
        results += result

        print(line.strip(), ' ', result, possibilites)

print(results)

# Part 2

def recursive_solver(code, groups, memory={}):
    # print(f"Called with {code}, {groups}")

    if len(code) == 0:
        #return (1, [current_sol]) if len(groups) == 0 else (0, [])
        return 1 if len(groups) == 0 else 0
    if len(groups) == 0:
        #return (1, [current_sol]) if all([c != '#' for c in code]) else (0, [])
        return 1 if all([c != '#' for c in code]) else 0
    if len(code) < groups[0]:
        return 0#, []

    memory_key = (code, '.'.join(map(str, groups)))
    if memory_key in memory:
        return memory[memory_key]

    c = code[0]
    if c == '.':
        result = recursive_solver(code[1:], groups)#, current_sol + ".")
        memory[memory_key] = result
        return result
    elif c == '#':
        for i in range(1, groups[0]):
            if code[i] == '.':
                memory[memory_key] = 0
                return 0#, []
        if len(code) > groups[0] and code[groups[0]] == '#':
            memory[memory_key] = 0
            return 0#, []
        #next_sol = current_sol + '#' * groups[0] + ('.' if len(code) > groups[0] else '')
        result = recursive_solver(code[groups[0] + 1:], groups[1:])#, next_sol)
        memory[memory_key] = result
        return result
    elif c == '?':
        #current_result, sols = recursive_solver(code[1:], groups, current_sol + '.')
        current_result = recursive_solver(code[1:], groups)
        can_be_hashtag = True
        for i in range(1, groups[0]):
            if code[i] == '.':
                can_be_hashtag = False
                break
        if len(code) > groups[0] and code[groups[0]] == '#':
            can_be_hashtag = False
        if can_be_hashtag:
            # next_sol = current_sol + '#' * groups[0] + ('.' if len(code) > groups[0] else '')
            # current_result_bis, sols_bis = recursive_solver(code[groups[0] + 1:], groups[1:], next_sol)
            current_result_bis = recursive_solver(code[groups[0] + 1:], groups[1:])#, next_sol)
            current_result += current_result_bis
            #sols += sols_bis
        memory[memory_key] = current_result
        return current_result#, sols


results = 0
idx = 1
with open('input.txt', 'r') as f:
    for line in f:
        code, groups = line.strip().split(' ')
        groups = list(map(int, groups.split(',')))

        code = "?".join([code for _ in range(5)])
        groups *= 5

        result = recursive_solver(code, groups, {})
        results += result
        print(idx)
        idx += 1
        # print(line.strip(), ' ', result, possibilites)

print(results)

