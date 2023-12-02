import re
from pathlib import Path

def match_numbers(match_string, line):
    match = re.findall(r'(\d+)\s' + match_string, line)
    return list(map(int, match))

def do_main():
    sum_1 = 0
    sum_2 = 0
    with open(Path('input.txt')) as file:
        lines = [line.rstrip() for line in file]

    for i, game in enumerate(lines):
        reds = match_numbers('red', game)
        blues = match_numbers('blue', game)
        greens = match_numbers('green', game)

        min_red = max(reds)
        min_blue = max(blues)
        min_green = max(greens)
        min_set = min_red * min_blue * min_green
        sum_2 += min_set

        if any(num > 12 for num in reds) or any(num > 13 for num in greens) or any(num > 14 for num in blues):
            continue

        sum_1 += i + 1

    print(sum_1)
    print(sum_2)

if __name__ == '__main__':
    do_main()