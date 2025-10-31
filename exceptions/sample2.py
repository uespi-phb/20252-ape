print('>>> INÍCIO')

try:
    number = int(input("Digite um número: "))
    result = 10 / number
    print("Resultado:", result)
except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")
except ValueError:
    print("Erro: entrada inválida, digite um número inteiro.")
else:
    print('Não ocorreu erros!')
finally:
    print('Bloco finally')

print('<<< FIM')
