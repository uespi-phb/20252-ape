
from utils import clear_screen, print_title, line, wait_key


def student_list(students):
    clear_screen()
    print_title('LISTA DE ESTUDANTES', 2)

    print(f"{'ID':<4} {'NOME':<15} {'NOTA'}")  
    print(f"{line(4)} {line(15)} {line(4)}")  
    for student in students:
        id = student['id']
        name = student['name']
        score = student['score']
        print(f"{id:>4} {name:<15} {score:>4}")

    wait_key('Pressione qualquer tecla para continuar.', 2)


def student_add(students):
    clear_screen()
    print_title('CADASTRA ESTUDANTE', 2)

    id = input('Id  : ')
    name = input('Nome: ')
    score = input('Nota: ')
    
    student = {
        'id': int(id),
        'name': name,
        'score': float(score)
    }
    students.append(student)
    
    wait_key('Estudante criado com sucesso!', 2)


def student_del():
    print('REMOVE ESTUDANTE\n')
    input()


def student_search():
    print('BUSCA ESTUDANTE\n')
    input()
