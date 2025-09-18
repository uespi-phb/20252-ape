
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    n = int(input())
    print(bin(n).count('1'))
