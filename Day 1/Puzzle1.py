input_list = open('input.csv', 'r').read().splitlines()

first_digits = []
last_digits = []
for input in input_list:
    first_digit = None
    last_digit = None
    for i in range(len(input)):
        if input[i].isnumeric() and first_digit is None:
            first_digit = input[i]
        if input[i].isnumeric():
            last_digit = input[i]
    first_digits.append(first_digit)
    last_digits.append(last_digit)

full_numbers = []
for i, first_digit in enumerate(first_digits):
    full_numbers.append(int(str(first_digit) + str(last_digits[i])))

total = sum(full_numbers)
print(total)

print('Process complete')