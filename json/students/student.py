
from utils import clear_screen, print_title, line, wait_key

def student_table(students):
    print(f"{'ID':<4} {'NOME':<15} {'NOTA'}")  
    print(f"{line(4)} {line(15)} {line(4)}")  
    for student in students:
        id = student['id']
        name = student['name']
        score = student['score']
        print(f"{id:>4} {name:<15} {score:>4}")


def student_list(students):
    clear_screen()
    print_title('LISTA DE ESTUDANTES', 2)
    
    student_table(students)
    
    wait_key('Pressione enter para continuar.', 2)


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


def student_del(students):
    clear_screen()
    print_title('REMOVER ESTUDANTE', 2)

    student_table(students)
    
    id = int(input('\nId do estudante a ser removido\n> '))
    
    removed = False
    for i in range(len(students)):
        if students[i]['id'] == id:
            students.pop(i)
            removed = True
            break                    
        
    if removed:
        message = 'Estudante removido com sucesso!'
    else:
        message = 'Estudante não encontrado!'
        
    wait_key(message, 2)


def student_search(students):
    clear_screen()
    print_title('BUSCAR ESTUDANTE', 2)
   
    id = int(input('Id do estudante\n> '))
    
    student_found = None
    for student in students:
        if student['id'] == id:
            student_found = student
            break
    
    if student_found:
        print()
        print_title('DADOS DO ESTUDANTE')
        print('Id  :', student_found['id'])
        print('Nome:', student_found['name'])
        print('Nota:', student_found['score'])
        message = 'Pressione Enter para continuar'
    else:
        message = 'Estudante não encontrado!'
            
            
    wait_key(message, 2)
    