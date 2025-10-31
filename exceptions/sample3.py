print('>>> INÍCIO')

try:
    number = int(input("Divisor: "))
    result = 10 / number
    print('Resultado:', result)
except ArithmeticError as error:
    print("Ocorreu um erro aritmético!'\n", error)
except Exception as error:
    print('Error não previsto!\n', error)
    
print('<<< FIM')
