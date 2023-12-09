from time import time
import pandas as pd

start_time = time()

input_list = open('input.txt', 'r').read().splitlines()

# test = [1, 3, 6, 10, 15, 21, 28]

total = 0

for line in input_list:
    line_split = line.split()
    line_split.reverse()

    df = pd.DataFrame(line_split, columns=[0])
    df[0] = pd.to_numeric(df[0])

    i = 1
    df[i] = df[0] - df[0].shift(1)
    while df[i].sum() != 0:
        i += 1
        df[i] = df[i-1] - df[i-1].shift(1)

    df.loc[len(df.index), i] = 0

    i -= 1
    while i >= 0:
        df.loc[len(df.index) - 1, i] = df.loc[len(df.index) - 1, i + 1] + df.loc[len(df.index) - 2, i]
        i -= 1

    total += int(df.loc[len(df.index) - 1, 0])

print(f'Total: {total}')
print('Process complete')
print(f"Process time: {round(time() - start_time, 2)} seconds.")