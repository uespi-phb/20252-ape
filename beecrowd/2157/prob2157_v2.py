
def mirror_sequence(first, last):
    sequence = ''.join(map(str, range(first, last + 1)))
    return sequence + sequence[::-1]
    

test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    first, last = map(int, input().split())
    print(mirror_sequence(first, last))
