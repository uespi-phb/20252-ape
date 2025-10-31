

def rational_add(r1, r2):
    num = r1[0] * r2[1] + r2[0] * r1[1]
    den = r1[1] * r2[1]
    return (num, den)


def rational_sub(r1, r2):
    num = r1[0] * r2[1] - r2[0] * r1[1]
    den = r1[1] * r2[1]
    return (num, den)


def rational_mul(r1, r2):
    num = r1[0] * r2[0]
    den = r1[1] * r2[1]
    return (num, den)


def rational_div(r1, r2):
    num = r1[0] * r2[1]
    den = r1[1] * r2[0]
    return (num, den)


def rational_simplify(r):
    num, den = r
    
    div = 2
    while div <= min(abs(num), abs(den)):
        if (num % div == 0) and (den % div == 0):
            num = num // div
            den = den // div
        else:
            div += 1
            
    return (num, den)


def main():
    test_cases = int(input())
    while test_cases > 0:
        test_cases -= 1
        
        expr = input().split()
        r1 = (int(expr[0]), int(expr[2])) 
        r2 = (int(expr[4]), int(expr[6])) 
        operator = expr[3]
        
        match operator:
            case '+':
                r = rational_add(r1, r2)
            case '-':
                r = rational_sub(r1, r2)
            case '*':
                r = rational_mul(r1, r2)
            case '/':
                r = rational_div(r1, r2)

        s = rational_simplify(r)

        print(f'{r[0]}/{r[1]} = {s[0]}/{s[1]}')        


if __name__ == '__main__':
    main()
