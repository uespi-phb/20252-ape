
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    line = input().strip()
    a, b = line.split()
    
    len_a = len(a)
    len_b = len(b)
    if (len_a >= len_b) and (a[-len(b):] == b):
        print('encaixa')
    else:
        print('nao encaixa')
