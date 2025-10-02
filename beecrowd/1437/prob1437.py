
cardinals = 'NLSO'

while True:
    n = int(input())
    if n == 0:
        break
    
    position = 0
    
    commands = input()
    for cmd in commands:
        position += 1 if cmd == 'D' else -1
        # if cmd == 'D':
        #     position += 1
        # else:
        #     position -= 1
    
    print(cardinals[position % 4])
