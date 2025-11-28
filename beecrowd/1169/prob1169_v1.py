
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    slots = int(input())
    count = 0
    grains = 0
    while slots > 0:
        slots -= 1
        
        if count:
            count = count * 2
        else:
            count = 1
            
        grains += count
        
    weight = grains // 12000
    
    print(f'{weight} kg')