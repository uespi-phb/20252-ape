from math import sqrt, floor

def prime(n):
    max = floor(sqrt(n))
    for div in range(2, max + 1):
        if n % div == 0:
            return False
    return True


print('### VERIFICA SE INTEIRO É PRIMO ###\n')
number = int(input('Digite um inteiro: '))

if prime(number):
    print(number,'é primo.')
else:
    print(number,'não é primo.')

print('\n### GERA TODOS OS PRIMOS ENTRE 1 E',number,' ###\n')

primes = [str(n) for n in range(1,number + 1) if prime(n)]
print(', '.join(primes))

# for p in primes:
#     print(p,' ', end='')
