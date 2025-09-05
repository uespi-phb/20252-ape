#
# Escreva um programa que leia uma seqüência de números inteiros positivos 
# terminada por –1 e imprima na tela o maior e o menor números lidos.
# 
# Obs: o valor –1 é somente um terminador e não deve ser considerado nos cálculos.
#
major = None
minor = None

while True:
    n = int(input())
    if n == -1:
        break

    if (major is None) or (n > major):
        major = n
    if (minor is None) or (n < minor):
        minor = n

print(minor, major)
