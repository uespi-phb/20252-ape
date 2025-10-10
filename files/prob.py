
test_cases = int(input())

while test_cases > 0:
    test_cases -= 1
    
    number = int(input())
    
    is_prime = True
    for div in range(2, number):
        if number % div == 0:
            is_prime = False
            break
    
    if is_prime:
        print(number,'eh primo')
    else:
        print(number,'nao eh primo')
