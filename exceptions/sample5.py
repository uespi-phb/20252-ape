print('>>> INÍCIO')

def age_in_months(age):
    if age < 0:
        raise ValueError("Idade não pode ser negativa.")
    return age * 12

try:
    age = int(input('Idade: '))
    print(age,'anos =', age_in_months(age),'meses')
    print(age,'anos =', age_in_months(-age),'meses')
except ValueError as error:
    print("Erro:", error)
    
print('>>> FIM')

