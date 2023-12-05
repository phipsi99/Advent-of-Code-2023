from pathlib import Path
import re
from tqdm import tqdm

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

    locations = []
    for seed in maps['seeds']:
        curr_val = seed
        for k, amap in maps.items():
            if k == 'seeds':
                continue

            val = None
            for i in range(0, int(len(amap)/3)):
                offset = i*3
                if curr_val in range(amap[offset +1], amap[offset+1] + amap[offset+2]):
                    val = curr_val + amap[offset] - amap[offset+1]

            if not val:
                val = curr_val
            curr_val = val
        locations.append(curr_val)
    print(min(locations))

if __name__ == '__main__':
    do_main()