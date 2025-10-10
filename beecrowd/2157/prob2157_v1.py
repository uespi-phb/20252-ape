
def mirror_sequence(first, last):
    sequence = ''
    for value in range(first, last + 1):
        sequence += str(value)
    sequence += sequence[::-1]
    return sequence
    

test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    first, last = map(int, input().split())
    print(mirror_sequence(first, last))
