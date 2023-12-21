from time import time


def hash(item):
    current_value = 0
    for char in item:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256

    return current_value


def remove_lens(boxes, label, box_no):
    lenses = boxes.get(box_no, [])
    if lenses == []:
        return boxes
    for i, lens in enumerate(lenses):
        if lens[0] == label:
            lenses.pop(i)
            boxes[box_no] = lenses
            break

    return boxes


def add_lens(boxes, label, foc_len, box_no):
    lenses = boxes.get(box_no, [])
    # check if lens already exists with this label, and replace it if yes
    for i, lens in enumerate(lenses):
        if lens[0] == label:
            lenses[i] = (label, foc_len)
            boxes[box_no] = lenses
            return boxes
    # if no lens with this label, add it to end
    lenses.append((label, foc_len))
    boxes[box_no] = lenses
    return boxes


start_time = time()

init_seq = open('input.txt', 'r').read()
# init_seq = open('test.txt', 'r').read()

init_seq = init_seq.split(',')

# create boxes dict
boxes = {}

for item in init_seq:
    operator = '='
    if '-' in item:
        operator = '-'
    label = item.split(operator)[0]
    box_no = hash(label)
    if operator == '-':
        boxes = remove_lens(boxes, label, box_no)
    if operator == '=':
        foc_len = int(item.split(operator)[1])
        boxes = add_lens(boxes, label, foc_len, box_no)

total = 0
for box_no, lenses in boxes.items():
    for i, lens in enumerate(lenses):
        power = (box_no + 1) * (i + 1) * lens[1]
        total += power


print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")