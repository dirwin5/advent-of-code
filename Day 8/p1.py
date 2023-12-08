input_list = open('input.txt', 'r').read().splitlines()

instructions = input_list.pop(0)
instructions = instructions.replace("L", "0")
instructions = instructions.replace("R", "1")
instructions = list(instructions)
instructions = [int(number) for number in instructions]

input_list.pop(0)

input_dict = {}
for line in input_list:
    line_split = line.split('=')
    tup = line_split[1].replace('(', '').replace(')', '').split(',')
    input_dict[line_split[0].strip()] = (tup[0].strip(), tup[1].strip())

start = 'AAA'
end = 'ZZZ'

location = start
steps = 0
while location != end:
    for number in instructions:
        location = input_dict[location][number]
        steps += 1

print(f'Total steps: {steps}')
print('Process complete')