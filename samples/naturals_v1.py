#
# Exiba no console os N primeiros números naturais, 
# onde N é um dado de entrada. Os números devem
# ser exibidos um ao lado do outro, separados por ",".
# 

print('## EXIBE OS N PRIMEIROS NÚMEROS NATURAIS ##')

n = int(input('Informe o valor de N: '))

k = 1
while k <= n:
    print(k, end=',')
    k = k + 1
print('\b ')
