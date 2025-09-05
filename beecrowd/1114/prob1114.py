
correct_password = '2002'

while True:
    password = input()
    if password == correct_password:
        print('Acesso Permitido')
        break
    else:
        print('Senha Invalida')
        
