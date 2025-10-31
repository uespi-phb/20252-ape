print('>>> INÍCIO')

try:
    n = int(input("Digite um número: "))
    print(10 / n)
except (ZeroDivisionError, ValueError):
    print("Erro: valor inválido ou divisão por zero.")

print('<<< FIM')
