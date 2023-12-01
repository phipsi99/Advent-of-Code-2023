from pathlib import Path
import re

def convert_text_digits(input_string: str):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i, number in enumerate(numbers):
        input_string = input_string.replace(number, number[0] + str(i+1) + number[-1])
    return input_string

with open(Path('input.txt')) as file:
    lines = [convert_text_digits(line.rstrip()) for line in file]

result = []
for line in lines:
    digits = re.findall('\d', line)
    first_val = digits[0]
    last_val = digits[-1]
    result.append(f'{first_val}{last_val}')

sum = 0
for num in result:
    sum += int(num)
print (sum)