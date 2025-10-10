
input()
data = map(int, input().split())

multiple_2 = 0
multiple_3 = 0
multiple_4 = 0
multiple_5 = 0
for value in data:
    if value % 2 == 0:
        multiple_2 += 1
    if value % 3 == 0:
        multiple_3 += 1
    if value % 4 == 0:
        multiple_4 += 1
    if value % 5 == 0:
        multiple_5 += 1

print(f'{multiple_2} Multiplo(s) de 2')
print(f'{multiple_3} Multiplo(s) de 3')
print(f'{multiple_4} Multiplo(s) de 4')
print(f'{multiple_5} Multiplo(s) de 5')

