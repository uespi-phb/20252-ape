
while True:
    try:
        input()
    except:
        break

    expr = input().split(' + ')
    deriv = []
    
    for term in expr:
        c, e = map(int, term.split('x'))
        d = f'{c * e}'
        if e > 2:
            d += f'x{e - 1}'
        elif e == 2:
            d += f'x'
        deriv.append(d)
        
    print(' + '.join(deriv))
