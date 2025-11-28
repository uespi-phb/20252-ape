
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    slots = int(input())
    grains = 2**slots - 1        
    weight = grains // 12000
    
    print(f'{weight} kg')