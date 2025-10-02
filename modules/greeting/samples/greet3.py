from modules.greet import greet_user as greet_user2

def greet_user(name):
    return name

my_name = input('Digite seu nome: ')
print( greet_user(my_name) )
print( greet_user2(my_name) )
