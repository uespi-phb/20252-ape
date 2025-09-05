#
# Leia duas strings pelo teclado e gere uma lista contendo cada um dos
# caracteres das strings intercaladamente.
# A lista gerada deve conter todos os caracteres das duas strings.
#
# Ex:
#   Se 
#     s1 = 'UESPI', s2 = 'Parnaiba'
#   Então a lista a ser gerada deverá ser:
#     ['U','P','E','a','S','r','P','n','I','a','i','b','a']
#

text1 = input('1º Texto: ')
text2 = input('2º Texto: ')

text1_len = len(text1)
text2_len = len(text2)

result = []
for i in range(max(text1_len, text2_len)):
    if i < text1_len:
        result.append(text1[i])
    if i < text2_len:
        result.append(text2[i])

print(result)
