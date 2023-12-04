from pathlib import Path
import re

def do_main():
    with open(Path('input.txt')) as file:
        lines = [line.rstrip() for line in file]

    point_sum = 0
    cards = [1 for _ in range(len(lines))]

    for line_index, line in enumerate(lines):
        match = re.search(r'([\d\s]+)\s\|\s([\d\s]+)', line)
        numbers_before = list(map(int, match.group(1).split()))
        numbers_after = list(map(int, match.group(2).split()))

        copy_index = 1
        points = 0
        for num in numbers_after:
            if num in numbers_before:
                cards[line_index+copy_index] += (1 * cards[line_index])
                copy_index += 1
                if points == 0:
                    points = 1
                    continue
                points = points * 2
        point_sum += points

    print(point_sum)
    print(sum(cards))

if __name__ == '__main__':
    do_main()