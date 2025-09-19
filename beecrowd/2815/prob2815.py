
def fix_stutted_word(word):
    if word[:2] == word[2:4]:
        word = word[2:]
    return word


text_stutted = input().strip()

text_fixed = []
for word in text_stutted.split():
    fixed_word = fix_stutted_word(word)
    text_fixed.append(fixed_word)
    
sentence = ' '.join(text_fixed)
print(sentence)
