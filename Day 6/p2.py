input_list = open('input.txt', 'r').read().splitlines()

time = int
distance_record = int

for line in input_list:
    if line.startswith('Time:'):
        time = line.split(':')[1]
        time = int(time.replace(' ', ''))
    if line.startswith('Distance:'):
        distance_record = line.split(':')[1]
        distance_record = int(distance_record.replace(' ', ''))

ways_to_beat = 0
for j in range(time):
    speed = j
    travel_time = time - j
    distance = speed * travel_time
    if distance > distance_record:
        ways_to_beat += 1

print(f'Total: {ways_to_beat}')
print('Process complete')