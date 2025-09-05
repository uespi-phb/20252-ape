
while True:
    orginal_text = input()

    dancing_text = ''

    to_upper = True
    for char in orginal_text:
        if char.isalpha():
            if to_upper:
                char = char.upper()
            else:
                char = char.lower()
            to_upper = not to_upper
                
        dancing_text = dancing_text + char
    
    print(dancing_text)
