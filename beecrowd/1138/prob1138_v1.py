
while True:
    line = input()
    data = line.split()
    a = int(data[0])
    b = int(data[1])
    if (a == 0) and (b == 0):
        break
    
    digit_counter = [0] * 10    # [0,0,0,0,0,0,0,0,0,0]
    for n in range(a, b + 1):
        while n != 0:
            digit = n % 10
            digit_counter[digit] += 1
            n = n // 10         # n //= 10
    
    for i in range(10):
        print(digit_counter[i], end='')
        if i < 9:
            print(' ', end='')
    print()
