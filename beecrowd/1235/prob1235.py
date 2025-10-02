
def fix_text(text):
    middle = len(text) // 2
    # return text[:middle][::-1] + text[middle:][::-1]

    left_part = text[:middle]
    right_part = text[middle:]

    fixed_left_part = left_part[::-1]
    fixed_right_part = right_part[::-1]
    
    return fixed_left_part + fixed_right_part


test_cases = int(input())
for k in range(test_cases):
    wrong_text = input()
    right_text = fix_text(wrong_text)
    print(right_text)