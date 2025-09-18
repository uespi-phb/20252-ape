
import sys

for line in sys.stdin.readlines():
# for line in ['xyzzy']:
    line = line.strip()
    line = line.replace(' ', '')
    chars = list(set(line))
    chars.sort()
    
    if len(chars) == 0:
        print()
        continue
    
    ranges = []
    range_begin = chars[0]
    range_end = chars[0]
    for char in chars[1:]:
        if ord(char) - ord(range_end) != 1:
            range = '%s:%s' % (range_begin, range_end)
            ranges.append(range)
            range_begin = range_end = char
        else:
            range_end = char

    if (len(ranges) == 0) or (ranges[-1][2] != range_end):
        range = '%s:%s' % (range_begin, range_end)
        ranges.append(range)

    print(', '.join(ranges))
    