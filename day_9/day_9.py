
# Part 1
results = 0
with open('test.txt', 'r') as f:
    for line in f:
        last_numbers = []
        numbers = list(map(int, line.strip().split(' ')))
        while any([n != 0 for n in numbers]):
            last_numbers.append(numbers[-1])
            numbers = [numbers[i + 1]  - numbers[i] for i in range(len(numbers) - 1)]

        results += sum(last_numbers)

print(results)

# Part 2
results = 0
with open('input.txt', 'r') as f:
    for line in f:
        first_numbers = []
        numbers = list(map(int, line.strip().split(' ')))
        numbers = numbers
        while any([n != 0 for n in numbers]):
            first_numbers.append(numbers[0])
            numbers = [numbers[i + 1]  - numbers[i] for i in range(len(numbers) - 1)]

        current_results = 0
        for n in first_numbers[::-1]:
            current_results = n - current_results
        results += current_results

print(results)