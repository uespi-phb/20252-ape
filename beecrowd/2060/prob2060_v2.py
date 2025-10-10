
input()
data = map(int, input().split())

multiples = { 
    2: 0, 
    3: 0, 
    4: 0, 
    5: 0,
}

for value in data:
    for key in multiples:
        if value % key == 0:
            multiples[key] += 1

for key in multiples:
    print(f'{multiples[key]} Multiplo(s) de {key}')

