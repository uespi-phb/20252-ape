# 
# Escreva um programa que leia dois números inteiros
# e exiba na tela esses números no seguinte formato:
#
# Ex: para entradas 5 e 10
#     15 + 10 = 25
#     15 - 10 = 5
#     15 x 10 = 150
#     15 : 10 = 1.5
#
print('### OPERAÇÕES ARITMÉTICAS BÁSICAS ###')

a = int(input('Informe o 1º número:'))
b = int(input('Informe o 2º número:'))


print(a,'+',b,'=',a + b)

print(a,'-',b,'=',a - b)
print(a,'x',b,'=',a * b)
print(a,':',b,'=',a / b)
