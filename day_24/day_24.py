# Part 1
hailstones = []

with open('input.txt', 'r') as f:
    for line in f:
        pos, speed = line.strip().split(' @ ')
        x, y, z = map(int, pos.split(', '))
        vx, vy, vz = map(int, speed.split(', '))

        hailstones.append({'x': x, 'y': y, 'vx': vx, 'vy': vy})

result = 0

XMIN, XMAX, YMIN, YMAX = 200000000000000, 400000000000000, 200000000000000, 400000000000000

for i, hailstone in enumerate(hailstones):
    x, y, vx, vy = hailstone['x'], hailstone['y'], hailstone['vx'], hailstone['vy']

    P = [[vx, -vy], [vy, vx]]
    det = (vx * vx + vy * vy)
    Pm1 = [[vx / det, vy / det], [- vy / det, vx / det]]
    for other_hailstone in hailstones[i + 1:]:
        x2, y2, vx2, vy2 = other_hailstone['x'], other_hailstone['y'], other_hailstone['vx'], other_hailstone['vy']

        x2p = x2 - x
        y2p = y2 - y

        x2in1 = Pm1[0][0] * x2p + Pm1[0][1] * y2p
        y2in1 = Pm1[1][0] * x2p + Pm1[1][1] * y2p

        vx2in1 = Pm1[0][0] * vx2 + Pm1[0][1] * vy2
        vy2in1 = Pm1[1][0] * vx2 + Pm1[1][1] * vy2

        if vy2in1 == 0:
            continue

        t = - y2in1 / vy2in1
        if t < 0:
            continue
        x_final_in_1 = x2in1 + t * vx2in1
        if x_final_in_1 < 0:
            continue


        xf2 = P[0][0] * x_final_in_1
        yf2 = P[1][0] * x_final_in_1
        xf2 += x
        yf2 += y

        if xf2 >= XMIN and xf2 <= XMAX and yf2 >= YMIN and yf2 <= YMAX:
            result += 1



print(result)


# Part 2
hailstones = []

with open('input.txt', 'r') as f:
    for line in f:
        pos, speed = line.strip().split(' @ ')
        x, y, z = map(int, pos.split(', '))
        vx, vy, vz = map(int, speed.split(', '))

        hailstones.append({'x': x, 'y': y, 'z': z, 'vx': vx, 'vy': vy, 'vz': vz})


def find_instersect(h1, h2):
    x, y, vx, vy = h1['x'], h1['y'], h1['vx'], h1['vy']

    P = [[vx, -vy], [vy, vx]]
    det = (vx * vx + vy * vy)
    Pm1 = [[vx / det, vy / det], [- vy / det, vx / det]]

    x2, y2, vx2, vy2 = h2['x'], h2['y'], h2['vx'], h2['vy']

    x2p = x2 - x
    y2p = y2 - y

    x2in1 = Pm1[0][0] * x2p + Pm1[0][1] * y2p
    y2in1 = Pm1[1][0] * x2p + Pm1[1][1] * y2p

    vx2in1 = Pm1[0][0] * vx2 + Pm1[0][1] * vy2
    vy2in1 = Pm1[1][0] * vx2 + Pm1[1][1] * vy2

    if vy2in1 == 0:
        return None, None

    t = - y2in1 / vy2in1
    if t < 0:
        return None, None
    x_final_in_1 = x2in1 + t * vx2in1


    xf2 = P[0][0] * x_final_in_1
    yf2 = P[1][0] * x_final_in_1
    xf2 += x
    yf2 += y

    if abs(round(xf2) - xf2) < 1e-8:
        xf2 = round(xf2)

    if abs(round(yf2) - yf2) < 1e-8:
        yf2 = round(yf2)

    return xf2, yf2


possible_vx, possible_vy, possible_vz = set(), set(), set()
for i, hailstone in enumerate(hailstones):
    x, y, z, vx, vy, vz = hailstone['x'], hailstone['y'], hailstone['z'], hailstone['vx'], hailstone['vy'], hailstone['vz']
    for other_hailstone in hailstones[i + 1:]:
        x2, y2, z2, vx2, vy2, vz2 = other_hailstone['x'], other_hailstone['y'], other_hailstone['z'], other_hailstone['vx'], other_hailstone['vy'], other_hailstone['vz']

        if vx == vx2:
            if vz != vz2:
                h1 = hailstone
                h2 = other_hailstone
            # print(f'VX - {vx} - {x} - {x2}')
            possible_vx.add((x, x2, vx))
        if vy == vy2:
            # print(f"VY - {vy} - {y} - {y2}")
            possible_vy.add((y, y2, vy))
        if vz == vz2:
            # print(f"VZ - {vz} - {z} - {z2}")
            possible_vz.add((z, z2, vz))
        continue

# Find vx, vy, vz       
v = 1
vxr, vyr, vzr = None, None, None
while True:
    if v % 10000 == 0:
        print(vxr, vyr, vzr)
        

    # X
    possible = True
    for x, x2, vx in possible_vx:
        if vx == v:
            possible = possible and (x == x2)
            continue
        found_t_p = (x - x2) / (vx - v)
        found_t_m = (x - x2) / (v - vx)
        if abs(found_t_p - round(found_t_p)) > 1e-8 and abs(found_t_m - round(found_t_m)) > 1e-8:
            possible = False



    if possible:
        vxr = v

    possible = True
    for x, x2, vx in possible_vx:
        if vx == -v:
            possible = possible and (x == x2)
            continue
        found_t_p = (x - x2) / (vx + v)
        found_t_m = (x - x2) / (- v - vx)
        if abs(found_t_p - round(found_t_p)) > 1e-8 and abs(found_t_m - round(found_t_m)) > 1e-8:
            possible = False



    if possible:
        vxr = - v

    # Y
    possible = True
    for y, y2, vy in possible_vy:
        if vy == v:
            possible = possible and (y == y2)
            continue
        found_t_p = (y - y2) / (vy - v)
        found_t_m = (y - y2) / (v - vy)
        if abs(found_t_p - round(found_t_p)) > 1e-8 and abs(found_t_m - round(found_t_m)) > 1e-8:
            possible = False



    if possible:
        vyr = v

    possible = True
    for y, y2, vy in possible_vy:
        if vy == -v:
            possible = possible and (y == y2)
            continue
        found_t_p = (y - y2) / (vy + v)
        found_t_m = (y - y2) / (-v - vy)
        if abs(found_t_p - round(found_t_p)) > 1e-8 and abs(found_t_m - round(found_t_m)) > 1e-8:
            possible = False



    if possible:
        vyr = -v

    # Z
    possible = True
    for z, z2, vz in possible_vz:
        if vz == v:
            possible = possible and (z == z2)
            continue
        found_t_p = (z - z2) / (vz - v)
        found_t_m = (z - z2) / (v - vz)
        if abs(found_t_p - round(found_t_p)) > 1e-8 and abs(found_t_m - round(found_t_m)) > 1e-8:
            possible = False



    if possible:
        vzr = v

    possible = True
    for z, z2, vz in possible_vz:
        if vz == -v:
            possible = possible and (z == z2)
            continue
        found_t_p = (z - z2) / (vz + v)
        found_t_m = (z - z2) / (- v - vz)
        if abs(found_t_p - round(found_t_p)) > 1e-8 and abs(found_t_m - round(found_t_m)) > 1e-8:
            possible = False



    if possible:
        vzr = -v

    if vxr is not None and vyr is not None and vzr is not None:
        break
    v += 1

# Work on h1, h2

x2, y2, z2, vx2, vy2, vz2 = h1['x'], h1['y'], h1['z'], h1['vx'], h1['vy'], h1['vz']
x1, y1, z1, vx1, vy1, vz1 = h2['x'], h2['y'], h2['z'], h2['vx'], h2['vy'], h2['vz']

h = round((x2 - x1) / (vxr - vx1))
t = round((z2 + h * vz2 - z1 - h * vzr) / (vz1 - vz2))

rock = {
    'x': x1 + t * (vx1 - vxr), 'y': y1 + t * (vy1 - vyr), 'z': z1 + t * (vz1 - vzr),
    'vx': vxr, 'vy': vyr, 'vz': vzr}

print(rock)

