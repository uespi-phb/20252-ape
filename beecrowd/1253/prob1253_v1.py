
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    crypto = input()
    shift = int(input())
    
    text = ''
    for char in crypto:
        index = alpha.index(char) - shift
        text += alpha[index]
    
    print(text)
