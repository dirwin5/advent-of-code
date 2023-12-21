from time import time

start_time = time()

init_seq = open('input.txt', 'r').read()
# init_seq = open('test.txt', 'r').read()

init_seq = init_seq.split(',')

total = 0
for item in init_seq:
    current_value = 0
    for char in item:
        current_value += ord(char)
        current_value *= 17
        current_value %= 256
    total += current_value


print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")