
from stopwatch import Stopwatch

watch = Stopwatch()

while True:
    print('\033c')
    print('  1. Iniciar Cronômetro')
    print('  2. Parar   Cronômetro')
    print('  3. Tempo Decorrido')
    print('  0. Sair')
    
    option = input('> ')
    
    match option:
        case '0':
            break
        case '1':
            watch.start()
        case '2':
            watch.stop()
        case '3':
            enlapsed = watch.enlapsed()
            print(f'\nTempo: {enlapsed}s')
            input()