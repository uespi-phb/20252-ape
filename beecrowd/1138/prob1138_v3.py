
while True:
    a, b = map(int, input().split())
    if a + b == 0:
        break
    
    digit_counter = [0] * 10
    for n in range(a, b + 1):
        for digit in map(int, str(n)):
            digit_counter[digit] += 1
            
    print(' '.join(map(str, digit_counter)))