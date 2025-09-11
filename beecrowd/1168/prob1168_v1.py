
leds = (
    6,
    2,
    5,
    5,
    4,
    5,
    6,
    3,
    7,
    6,
)

test_cases = int(input())
while test_cases > 0:
    test_cases -= 1
    
    number = input()        
    
    number_leds = 0
    for digit in number:
        digit = int(digit)
        number_leds += leds[digit]
    print(number_leds, 'leds')
