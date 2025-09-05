
test_cases = int(input())

case = 0
while case < test_cases:
    case += 1    # case = case + 1
    
    number = int(input())
    
    sum = 0
    for div in range(1, number):    
        if number % div == 0:
            sum += div      # sum = sum + div
        
    if number == sum:
        print(number,'eh perfeito')
    else:
        print(number,'nao eh perfeito')
