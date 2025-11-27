
from image import Image


def main():
    image = Image(5,3)
    
    image.show()
    print('Brilho médio:', image.average_brightness())
    
    image.invert_colors()
    
    image.show()
    print('Brilho médio:', image.average_brightness())


if __name__ == '__main__':
    main()