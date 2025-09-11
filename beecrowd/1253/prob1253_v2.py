
test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    crypto = input()
    shift = int(input())
    
    text = ''
    for char in crypto:
        index = ord(char) - ord('A') - shift
        if index < 0:
            index = 26 + index
        code = ord('A') + index
        text += chr(code)
    
    print(text)
