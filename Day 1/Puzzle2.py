import pandas as pd

input_list = open('input.csv', 'r').read().splitlines()

letters_dict = {'one': 1,
                'two': 2,
                'three': 3,
                'four': 4,
                'five': 5,
                'six': 6,
                'seven': 7,
                'eight': 8,
                'nine': 9}

first_digits = []
last_digits = []
for input in input_list:
    input_numbers_dict = {}
    for letter_str, number in letters_dict.items():
        index = input.find(letter_str)
        index_r = input.rfind(letter_str)
        if index != -1:
            input_numbers_dict[index] = number
        if index_r != -1 and index_r != index:
            input_numbers_dict[index_r] = number
    for i in range(1, 10):
        index = input.find(str(i))
        index_r = input.rfind(str(i))
        if index != -1:
            input_numbers_dict[index] = i
        if index_r != -1 and index_r != index:
            input_numbers_dict[index_r] = i

    min_index = min(list(input_numbers_dict))
    max_index = max(list(input_numbers_dict))
    first_digits.append(input_numbers_dict[min_index])
    last_digits.append(input_numbers_dict[max_index])

full_numbers = []
for i, first_digit in enumerate(first_digits):
    full_numbers.append(int(str(first_digit) + str(last_digits[i])))

total = sum(full_numbers)
print(total)

# df = pd.DataFrame(data=input_list, columns=['input'])
# df['First_digits'] = first_digits
# df['Last_digits'] = last_digits

print('Process complete')