
from sys import argv

def file_stats(filename):
    ifile = open(filename, 'rt')

    line_count = 0
    word_count = 0
    for line in ifile.readlines():
        line_words = len(line.split())
        word_count += line_words
        line_count += 1
    ifile.close()
    
    # word_average = word_count / line_count if line_count != 0 else 0.0
    if line_count != 0:
        word_average = word_count / line_count
    else:
        word_average = 0.0

    print(f'{filename}:')
    print(f'\tlines: {line_count}')
    print(f'\twords: {word_count}')
    print(f'\taverage: {word_average:0.1f}')


argc = len(argv)
if argc < 2:
    print(f'usage: {argv[0]} FILE...')
    exit(-1)

for filename in argv[1:]:
    file_stats(filename)
