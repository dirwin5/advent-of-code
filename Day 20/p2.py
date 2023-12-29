from time import time
from dataclasses import dataclass, field

MODULES_DICT = {}


@dataclass
class Module:
    name: str
    type: str
    dest_modules: list


@dataclass
class FlipFlop(Module):
    on: bool = False


@dataclass
class Conjunction(Module):
    # dict of each connected input module name and last pulse type
    connected_inputs: dict = field(default_factory=dict)


@dataclass
class Broadcast(Module):
    pass


@dataclass
class Button(Module):
    name: str = 'button'
    type: str = 'button'
    dest_modules: list = field(default_factory=lambda: ['broadcaster'])


@dataclass
class Output(Module):
    type: str = 'output'
    dest_modules: list = field(default_factory=list)


@dataclass
class Pulse:
    low: bool
    from_module: str
    to_module: str


def process_pulse(pulse):
    ret_list = []
    # output
    if pulse.to_module.type == 'output':
        return ret_list
    # broadcaster
    if pulse.to_module.type == 'broadcaster':
        output_low = pulse.low
    # flip flop
    if pulse.to_module.type == '%':
        if pulse.low is False:
            return ret_list
        if pulse.to_module.on:
            pulse.to_module.on = False
            output_low = True
        else:
            pulse.to_module.on = True
            output_low = False
    # conjunction
    if pulse.to_module.type == '&':
        # update last received pulse type
        pulse.to_module.connected_inputs[pulse.from_module.name] = pulse.low
        # if any last pulses were low, send high. Else if all last pulses were high, send low.
        if any(pulse.to_module.connected_inputs.values()):
            output_low = False
        else:
            output_low = True

    # create output pulse list for returning
    for dest_module in pulse.to_module.dest_modules:
        ret_list.append(Pulse(output_low, pulse.to_module, MODULES_DICT[dest_module]))
    return ret_list


def main():
    input_list = open('input.txt', 'r').read().splitlines()
    # input_list = open('test2.txt', 'r').read().splitlines()

    # populate MODULES_DICT from input
    MODULES_DICT['button'] = Button()
    conjunction_modules_list = []
    for line in input_list:
        module_type_name = line.split('->')[0].strip()
        dest_modules = line.split('->')[1].split(',')
        dest_modules_stripped = []
        for dest_module in dest_modules:
            dest_modules_stripped.append(dest_module.strip())
        if module_type_name[0] == '%':
            module = FlipFlop(name=module_type_name[1:], type='%', dest_modules=dest_modules_stripped)
        elif module_type_name[0] == '&':
            module = Conjunction(name=module_type_name[1:], type='&', dest_modules=dest_modules_stripped)
            conjunction_modules_list.append(module.name)
        elif module_type_name == 'broadcaster':
            module = Broadcast(name=module_type_name, type=module_type_name, dest_modules=dest_modules_stripped)

        MODULES_DICT[module.name] = module

    # populate input modules to conjunction modules
    for module_name, module in MODULES_DICT.items():
        conjunction_dests = list(set(module.dest_modules).intersection(conjunction_modules_list))
        for conjunction_dest in conjunction_dests:
            MODULES_DICT[conjunction_dest].connected_inputs[module_name] = True

    # find output module names and add to MODULES_DICT
    output_module_names = []
    for module_name, module in MODULES_DICT.items():
        for dest_module in module.dest_modules:
            try:
                MODULES_DICT[dest_module]
            except KeyError:
                output_module_names.append(dest_module)
    for output_module_name in output_module_names:
        MODULES_DICT[output_module_name] = Output(name=output_module_name)

    pulses = []
    # press button until single loe pulse to rx
    i = 0
    while True:
        i += 1
        low_to_rx = 0
        pulses.append(Pulse(True, MODULES_DICT['button'], MODULES_DICT['broadcaster']))
        while len(pulses) != 0:
            pulse = pulses.pop(0)
            next_pulses = process_pulse(pulse)
            for next_pulse in next_pulses:
                pulses.append(next_pulse)
                if next_pulse.to_module.name == 'rx' and next_pulse.low:
                    low_to_rx += 1

        if i % 1000000 == 0:
            print(f'Button presses so far: {i}')
        if low_to_rx > 0:
            print(f'Low: {low_to_rx}')
        if low_to_rx == 1:
            break

    print(f'Total button presses: {i}')

    # print(f'Total low pulses: {low_pulses}')
    # print(f'Total high pulses: {high_pulses}')
    # print(f'Total: {low_pulses * high_pulses}')


if __name__ == '__main__':
    start_time = time()
    main()
    print('\nProcess complete')
    print(f"Process time: {round(time() - start_time, 2)} seconds.")
