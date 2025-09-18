
def bin_ones(number):
    one_counter = 0
    while number != 0:
        if number % 2 == 1:
            one_counter += 1
        number = number // 2
    return one_counter


test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    n = int(input())
    print(bin_ones(n))
