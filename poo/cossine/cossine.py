
class Cossine:
    
    def __init__(self, angle, terms = None):
        if not isinstance(angle, (int, float)):
            raise TypeError('Angle must be int or float')
        if not isinstance(terms, int) and (terms is not None):
            raise TypeError('Terms must be int or None')
        
        self.__angle = angle
        self.__terms = terms
        self.__index = None


    def __iter__(self):
        # print('__iter__()')
        self.__index = 0
        return self
    
    
    def __next__(self):
        if self.__index == 0:
            term = '1'
        else:
            signal = '+' if (self.__index % 2 == 0) else '-'
            term = f'{signal}{self.__angle}^{self.__index * 2}/{self.__index * 2}!'
        self.__index += 1
        if (self.__terms is not None) and (self.__index > self.__terms):
            raise StopIteration()
        
        return term    

    def terms(self):
        return self.__terms


    def angle(self):
        return self.__angle
    
    
    def is_finite(self):
        return self.__terms is not None


    def is_infinite(self):
        return self.__terms is None


s1 = Cossine(2,10)
s2 = Cossine(-5)
