import re

class Temperature:
    valid_units = ('C', 'F', 'K')
    regex_pattern = r'^[+-]?\d+\.?\d*[CFK]?$'
    
    def __init__(self, value, unit = None):
        if isinstance(value, (int, float)):
            if unit is None:
                unit = 'K'
            
            if unit not in Temperature.valid_unit:
                raise ValueError(f'Invalid temperature unit: {unit}')
            
            value = float(value)
            
        elif isinstance(value, str):
            if unit is not None:
                raise ValueError('Cannot specify unit when temperature is string')
            
            if re.match(Temperature.regex_pattern, value) is None:
                raise ValueError('Invalid temperature string')
            
            if value[-1].isalpha():
                unit = value[-1]
                value = float(value[0:-1])
            else:
                unit = 'K'
                value = float(value)
        else:
            raise TypeError('Invalid temperature')

        self.__value = value
        self.__unit = unit
    
        if self.to_kelvin() < 0:
            raise ValueError(f'Invalid temperature: {value}')
    

    def __str__(self):
        return f'{self.__value:0.2f}{self.__unit}'


    def __repr__(self):
        return f'Temperature({self.__value:0.2f}{self.__unit})'
        

    def to_kelvin(self):
        match self.__unit:
            case 'F':
                value = 5/9 * (self.__value + 459.67)
            case 'C':
                value = self.__value + 273.15
            case 'K':
                value = self.__value

        return value
        
        
    def to_celcius(self):
        match self.__unit:
            case 'F':
                value = 5/9 * (self.__value - 32)
            case 'C':
                value = self.__value
            case 'K':
                value = self.__value - 273.15

        return value
        
        
    def to_fahrenheit(self):
        match self.__unit:
            case 'F':
                value = self.__value
            case 'C':
                value = self.__value * 9/5 + 32
            case 'K':
                value = self.__value * 9/5 + 459.67

        return value

    def increase(self, delta = 1):
        value = self.to_kelvin()
        if value + delta < 0:
            raise ValueError(f'Cannot increase temperature by {delta}')
        
        self.__value += delta


    def decrease(self, delta = 1):
        value = self.to_kelvin()
        if value - delta < 0:
            raise ValueError(f'Cannot increase temperature by {delta}')

        self.__value -= delta

