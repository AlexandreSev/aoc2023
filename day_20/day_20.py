# Part 1
modules = {}
with open('input.txt', 'r') as f:
    for line in f:
        name, destinations = line.strip().split(' -> ')
        destinations = destinations.split(', ')
        if name == 'broadcaster':
            modules['broadcaster'] = {'type': 'broadcast', 'destinations': destinations}
        elif name[0] == '%':
            modules[name[1:]] = {'type': 'flipflop', 'destinations': destinations, 'state': False}
        elif name[0] == '&':
            modules[name[1:]] = {'type': 'conjunction', 'destinations': destinations, 'state': {}}


termination_nodes = set()
for name, config in modules.items():
    for module in config['destinations']:
        if module not in modules:
            termination_nodes.add(module)
        elif modules[module]['type'] == 'conjunction':
            modules[module]['state'][name] = False



def send_pulse(module, high, sender):
    if module['type'] == 'broadcast':
        return module['destinations'], high
    elif module['type'] == 'flipflop' and not high:
        module['state'] = not module['state']
        return module['destinations'], module['state']
    elif module['type'] == 'conjunction':
        module['state'][sender] = high
        return_low = True
        for state in module['state'].values():
            return_low = return_low and state

        return module['destinations'], not return_low
    return [], None


nb_pulses = {True: 0, False: 0}
for loop_idx in range(1000):

    pulses = [('broadcaster', False, 'button')]
    while pulses:
        receiver, high, sender = pulses.pop(0)
        # print(f"{sender} -{'high' if high else 'low'}-> {receiver}")
        nb_pulses[high] += 1

        if receiver not in termination_nodes:
            destinations, high = send_pulse(modules[receiver], high, sender)
            for destination in destinations:
                pulses.append((destination, high, receiver))


print(nb_pulses[True] * nb_pulses[False])


# Part 2
import json


modules = {}
with open('input.txt', 'r') as f:
    for line in f:
        name, destinations = line.strip().split(' -> ')
        destinations = destinations.split(', ')
        if name == 'broadcaster':
            modules['broadcaster'] = {'type': 'broadcast', 'destinations': destinations}
        elif name[0] == '%':
            modules[name[1:]] = {'type': 'flipflop', 'destinations': destinations, 'state': False}
        elif name[0] == '&':
            modules[name[1:]] = {'type': 'conjunction', 'destinations': destinations, 'state': {}}


termination_nodes = set()
for name, config in modules.items():
    for module in config['destinations']:
        if module not in modules:
            termination_nodes.add(module)
        elif modules[module]['type'] == 'conjunction':
            modules[module]['state'][name] = False



def send_pulse(module, high, sender):
    if module['type'] == 'broadcast':
        return module['destinations'], high
    elif module['type'] == 'flipflop' and not high:
        module['state'] = not module['state']
        return module['destinations'], module['state']
    elif module['type'] == 'conjunction':
        module['state'][sender] = high
        return_low = True
        for state in module['state'].values():
            return_low = return_low and state

        return module['destinations'], not return_low
    return [], None


nb_button_pressed = 0
threshold = 10

# rx Low == ql send low == fh high, mf high, fz high, ss high
# Let's try our luck, consider that they will send high in a regular manner and that they will fire
# only once when we press the button
loops = {}


while True:
    nb_button_pressed += 1
    if nb_button_pressed == threshold:
        print(f"Pressed button {nb_button_pressed} times")
        threshold *= 10

    pulses = [('broadcaster', False, 'button')]
    while pulses:
        receiver, high, sender = pulses.pop(0)
        # print(f"{sender} -{'high' if high else 'low'}-> {receiver}")

        if sender in {'fh', 'mf', 'fz', 'ss'} and high and sender not in loops:
            loops[sender] = nb_button_pressed


        if receiver not in termination_nodes:
            destinations, high = send_pulse(modules[receiver], high, sender)
            for destination in destinations:
                pulses.append((destination, high, receiver))


    if len(loops) == 4:
        break


current_loop = loops['fh']
for loop in [loops['mf'], loops['fz'], loops['ss']]:
    result = current_loop
    while result % loop:
        result += current_loop
    current_loop = result

print(current_loop)