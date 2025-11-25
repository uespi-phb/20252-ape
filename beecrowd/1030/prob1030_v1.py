
test_cases = int(input())
for test_case in range(test_cases):
    
    persons, skip = map(int, input().split())

    circle = [True] * persons
    alive = persons
    index = 0
    counter = 0
    steps = 0
    while alive > 1:
        if circle[index]:
            counter += 1
            if counter == skip:
                circle[index] = False
                counter = 0
                alive -= 1
        
        steps += 1
        index += 1
        if index == persons:
            index = 0

    index = circle.index(True)
    print(f'Case {test_case + 1}: {index + 1} - {steps}')
