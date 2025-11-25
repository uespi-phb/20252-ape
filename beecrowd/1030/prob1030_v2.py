
test_cases = int(input())
for test_case in range(test_cases):
    
    persons, skip = map(int, input().split())

    circle = list(range(1, persons + 1))
    index = 0
    counter = 1
    steps = 0
    while len(circle) > 1:
        if counter == skip:
            del circle[index]
            counter = 1
        
        steps += 1
        counter += 1
        index += 1
        if index >= len(circle):
            index = 0


    print(f'Case {test_case + 1}: {circle[0]}')
