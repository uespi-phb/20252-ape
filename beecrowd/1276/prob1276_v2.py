
import sys

for line in sys.stdin.readlines():
# for line in ['abc']:
    chars = sorted(set(char for char in line if char.isalpha()))
    
    if not chars:
        print()
        continue
    
    ranges = []
    range_begin = range_end = chars[0]
    for char in chars[1:]:
        if ord(char) - ord(range_end) != 1:
            range = '%s:%s' % (range_begin, range_end)
            ranges.append(range)
            range_begin = range_end = char
        else:
            range_end = char

    range = '%s:%s' % (range_begin, range_end)
    ranges.append(range)

    print(', '.join(ranges))
    