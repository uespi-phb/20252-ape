
from utils import clear_screen

def student_list():
    print('LISTA ESTUDANTES\n')
    input()

def student_add(students):
    clear_screen()
    print('CADASTRA ESTUDANTE')
    print('------------------')
    id = input('Id  : ')
    name = input('Nome: ')
    score = input('Nota: ')
    
    student = {
        'id': int(id),
        'name': name,
        'score': float(score)
    }
    students.append(student)
    
    print('\n\nEstudante criado com sucesso!')
    input()


def student_del():
    print('REMOVE ESTUDANTE\n')
    input()


def student_search():
    print('BUSCA ESTUDANTE\n')
    input()
