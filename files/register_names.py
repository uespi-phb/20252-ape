
import sys

argc = len(sys.argv)
if argc != 2:
    print('usage: register_names.py FILE')
    exit(1)
    
filename = sys.argv[1]
names_file = open(filename, 'wt')

while True:
    name = input()
    if name == '':
        break
    
    names_file.write(f'{name}\n')
    
names_file.close()

names_file = open(filename, 'rt')

row = 0
for line in names_file.readlines():
    row += 1
    print(f'{row}: {line}', end='')

names_file.close()
