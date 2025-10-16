
import json

from student import student_add, student_del, student_list, student_search
from utils import clear_screen


students_file = 'students.json'
students = []


def data_save():
    fo = open(students_file, 'wt')
    json.dump(students, fo)
    fo.close()


def data_load():
    global students
    
    fi = open(students_file, 'rt')
    students = json.load(fi)
    fi.close()
    

def main_menu():
    options = ('0','1','2','3','4')
    title = 'CADASTRO DE ALUNOS'
    line = '-' * len(title)
    
    while True: 
        clear_screen()
        print(students)
        
        print(f'{title}\n{line}')
        print('  1.Listar')
        print('  2.Adicionar')
        print('  3.Remover')
        print('  4.Buscar')
        print('  0.Sair')
        
        print('> ', end='')
        option = input()
        if option in options:
            break
        
    return option


data_load()

while True:
    option = main_menu()
    if option == '1':
        student_list()
    elif option == '2':
        student_add(students)
    elif option == '3':
        student_del()
    elif option == '4':
        student_search()
    elif option == '0':
        break

data_save()
