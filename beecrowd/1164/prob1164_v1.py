
test_cases = int(input())

case = 0
while case < test_cases:
    case += 1    # case = case + 1
    
    number = int(input())
    
    sum = 0
    div = 1
    while div < number:
        if number % div == 0:
            sum += div      # sum = sum + div
        div += 1
        
    if number == sum:
        print(number,'eh perfeito')
    else:
        print(number,'nao eh perfeito')
