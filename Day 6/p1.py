input_list = open('input.txt', 'r').read().splitlines()

time_list = []
distance_list = []

for line in input_list:
    if line.startswith('Time:'):
        time_list = line.split(':')[1].split()
        time_list = [int(time) for time in time_list]
    if line.startswith('Distance:'):
        distance_list = line.split(':')[1].split()
        distance_list = [int(distance) for distance in distance_list]

ways_to_beat_list = []
for i, time in enumerate(time_list):
    ways_to_beat = 0
    for j in range(time):
        speed = j
        travel_time = time - j
        distance = speed * travel_time
        if distance > distance_list[i]:
            ways_to_beat += 1
    ways_to_beat_list.append(ways_to_beat)

total = 1
for ways_to_beat in ways_to_beat_list:
    total *= ways_to_beat

print(f'Total: {total}')
print('Process complete')