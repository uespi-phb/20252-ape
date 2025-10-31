
def convert_to_celsius(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Temperatura em Celsius deve ser numérico')
    
    return value * 9/5 + 32

def main():
    while True:
        try:
            temp = float(input('Temperatura (F): '))
            celsius = convert_to_celsius(temp)
            print(f'{temp}ºF = {celsius:0.2f}ºC')
            break
        except ValueError:
            print('Temperatura inválida. Tente novamente!\n')


if __name__ == '__main__':
    main()
