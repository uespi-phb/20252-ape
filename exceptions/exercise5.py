
def read_file(path):
    fi = open(path, 'rt')
    
    lines = []
    while True:
        line = fi.readline()
        if not line:
            break
        lines.append(line)

    fi.close()
    
    return lines

def main():
    filename = input('Arquivo: ')
    try:
        lines = read_file(filename)
        print(lines)
    except FileNotFoundError:
        print('Arquivo não encontrado:', filename)
    except PermissionError:
        print('Permissão negada!')


if __name__ == '__main__':
    main()
