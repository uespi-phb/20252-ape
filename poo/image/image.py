
from pixel import Pixel
from random import randint


class Image:
    
    def __init__(self, width, height = None):
        if height is None:
            height = width
        
        self.__validate(width, height)
        
        self.__width = width
        self.__height = height
        self.__matrix = []
        
        for r in range(height):
            row = []
            for w in range(width):
                red = randint(0,255)
                green = randint(0,255)
                blue = randint(0,255)
                pixel = Pixel(red,green,blue)
                row.append(pixel)
            self.__matrix.append(row)

        
    def __validate(self, *values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError('Image dimension must be integer')

            if value < 0:
                raise ValueError('Image dimension must be non negative')
    
    
    def average_brightness(self):
        sum = 0
        for row in self.__matrix:
            for pixel in row:
                sum += pixel.brightness()
        return sum / (self.__width * self.__height)
    
    
    def get_pixel(self, x, y):
        if (x < 0 or x >= self.__width or 
           y < 0 or y >= self.__height):
               raise ValueError(f'Invalid pixel position: ({x},{y})')
           
        return self.__matrix[y][x]
    
    
    def invert_colors(self):
        for row in self.__matrix:
            for i in range(len(row)):
                row[i] = row[i].invert()

    def show(self):
        for row in self.__matrix:
            for pixel in row:
                char = ' ' if pixel.brightness() < 128 else '.'
                print(char,end='')
            print()
        