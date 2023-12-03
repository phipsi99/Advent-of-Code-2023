from pathlib import Path
import re

def do_main():
    with open(Path('input.txt')) as file:
        lines = [line.rstrip() for line in file]

    sum = 0
    sum_gears = 0
    for line_index, line in enumerate(lines):
        digits = re.compile(r"\d+")
        for digit in digits.finditer(line):
            digit_start = digit.start()
            digit_end = digit.end()
            digit_number =  digit.group()
            symbol_adjectand = False
            for i in range(digit_start-1, digit_end+1):
                if i < 0 or i > len(lines) -1:
                    continue
                for j in range(-1, 2):
                    print(line_index)
                    if 0 < line_index+1+j < len(lines):
                        char = lines[line_index + j][i]
                        if char != '.' and not re.match(r'\d', char):
                            symbol_adjectand = True
                            break
            if symbol_adjectand:
                sum += int(digit_number)

        stars = re.compile(r"\*")
        for star in stars.finditer(line):
            star_start = star.start()
            found_digits=[]
            digits = re.compile(r"\d+")
            for i in range(-1, 2):
                if 1 <= line_index < len(lines)-1:
                    for digit in digits.finditer(lines[line_index+i]):
                        if abs(digit.start() - star_start) <= 1 or abs(digit.end()-1 - star_start) <= 1:
                            found_digits.append(int(digit.group()))
            if len(found_digits) == 2:
                sum_gears += found_digits[0] * found_digits[1]

    print(sum)
    print(sum_gears)

if __name__ == '__main__':
    do_main()