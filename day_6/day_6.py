# Part 1
import math


with open('input.txt', 'r') as f:
    times = next(f).split(':')[1].strip().split(' ')
    times = [int(t) for t in times if t]
    distances = next(f).split(':')[1].strip().split(' ')
    distances = [int(d) for d in distances if d]


answer = 1

for t, d in zip(times, distances):
    delta = t * t - 4 * d
    rdelta = math.sqrt(delta)
    r1 = ( t - rdelta) / 2
    r2 = ( t + rdelta) / 2
    if math.ceil(r1) == r1:
        r1 += 1
    if math.floor(r2) == r2:
        r2 -= 1

    answer *= (math.floor(r2) - math.ceil(r1) + 1)

print(answer)


# Part 2
import math


with open('input.txt', 'r') as f:
    t = int(next(f).split(':')[1].strip().replace(' ', ''))
    d = int(next(f).split(':')[1].strip().replace(' ', ''))



delta = t * t - 4 * d
rdelta = math.sqrt(delta)
r1 = ( t - rdelta) / 2
r2 = ( t + rdelta) / 2
if math.ceil(r1) == r1:
    r1 += 1
if math.floor(r2) == r2:
    r2 -= 1

answer = (math.floor(r2) - math.ceil(r1) + 1)

print(answer)



# (7 - x ) * x > 9
# -x2 + 7x - 9 > 0

