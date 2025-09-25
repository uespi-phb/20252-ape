
def item_key(elem):
    return elem[1]

def chars_frequency(text):
    char_count = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            char_count[char] = char_count.get(char, 0) + 1

    freqs = list(char_count.items())
    freqs.sort(key=item_key, reverse=True)
    
    output = ''
    max_freq = freqs[0][1]
    for char, freq in freqs:
        if freq == max_freq:
            output += char
        else:
            break
    
    return ''.join(sorted(output))


test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    text = input().strip()
    chars = chars_frequency(text)
    print(chars)
