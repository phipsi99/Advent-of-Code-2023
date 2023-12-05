from collections import OrderedDict
from pathlib import Path
from tqdm import tqdm
import re

def do_main():
    with open(Path('input.txt')) as file:
        content = file.read()
        pattern = r'(\w+-to-\w+ map:|seeds:)'
        map_pattern = r'\d+'
        sections = re.split(pattern, content)

        maps = {}

        for i in range(1, len(sections), 2):
            heading = sections[i].strip().replace(':','').replace('-', '_')
            values = re.findall(map_pattern, sections[i + 1])
            maps[heading] = list(map(int, values))

        print(maps)

    reversed_maps = OrderedDict(reversed(list(maps.items()))).items()

    # reversed the maps, so it's running way less long. still brute forcing, started from 0
    # then found out where the number is, so the 28500000 is just for quicker reproduction,.
    # with another input start from 0 is needed
    for location in tqdm(range(28500000, 10000000000000000)):
        curr_val = location
        for k, amap in reversed_maps:
            if k == 'seeds':
                continue

            val = None
            for i in range(0, int(len(amap)/3)):
                offset = i*3
                if curr_val in range(amap[offset], amap[offset] + amap[offset+2]):
                    val = curr_val + amap[offset+1] - amap[offset]

            if not val:
                val = curr_val

            if val < 0:
                break
            curr_val = val

        seed_rng =  int(len(maps['seeds']) / 2)
        for x in range(0,seed_rng):
            if maps['seeds'][x * 2] <= curr_val <= maps['seeds'][x * 2] + maps['seeds'][x * 2 + 1]:
                print(curr_val, location)
                return

if __name__ == '__main__':
    do_main()