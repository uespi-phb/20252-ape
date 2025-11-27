
class Pixel:
    
    def __init__(self, red, green, blue):
        
        self.__validate(red, green, blue)
        
        self.__r = red
        self.__g = green
        self.__b = blue
        
        
    def __validate(self, *values):
        for value in values:
            if not isinstance(value, int):
                raise TypeError('Pixel arguments must be integer')

            if value < 0 or value > 255:
                raise ValueError('Pixel arguments must be between 0 and 255')
        

    def __repr__(self):
        return f'Pixel({self.__r},{self.__g},{self.__b})'
        
        
    def __str__(self):
        red = f'{hex(self.__r)[2:]:>02}'
        green = f'{hex(self.__g)[2:]:>02}'
        blue = f'{hex(self.__b)[2:]:>02}'
        return f'#{red}{green}{blue}' 
    
        
    def brightness(self):
        return (self.__r + self.__g + self.__b) / 3
    
    
    def invert(self):
        return Pixel(
            255 - self.__r,
            255 - self.__g,
            255 - self.__b,
        )
