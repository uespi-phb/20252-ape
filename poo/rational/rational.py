
import re

class Rational:
    def __init__(self, num, den=None):       

        if isinstance(num, str):
            if den is not None:
                raise TypeError('Rational string must be alone')
            
            pattern = r'^[-+]?\d+/[-+]?\d+$'
            if re.match(pattern, num) is None:
                raise ValueError(f'Rational string is invalid: "{num}"')
            
            num, den = map(int, num.split('/'))
            
        elif isinstance(num, int):
            if den is None:
                den = 1
            elif not isinstance(den, int):
                raise TypeError(f'Denominator must be an integer: {den}')
        else:
            raise TypeError(f'Numerator and denominator must be integers: {num}, {den}')    
        
        if den == 0:
            raise ValueError('Denominator cannot be zero')
        
        if den < 0:
            num = -num
            den = -den
        
        self.__num = num
        self.__den = den
                
        self.__simplify()
        

    def __repr__(self):
        return f'Rational({self.__num},{self.__den})'


    def __str__(self):
        return f'{self.__num}/{self.__den}'
        

    def __add__(self, r):
        r = self.__validate(r)            
        
        num = self.__num*r.__den + r.__num*self.__den
        den = self.__den*r.__den
        return Rational(num, den)

    
    def __radd__(self, r):
        r = self.__validate(r)            
        return r + self
        

    def __sub__(self, r):
        r = self.__validate(r)            

        num = self.__num*r.__den - r.__num*self.__den
        den = self.__den*r.__den
        return Rational(num, den)


    def __rsub__(self, r):
        r = self.__validate(r)            
        return r + self


    def __mul__(self, r):
        r = self.__validate(r)            

        num = self.__num*r.__num
        den = self.__den*r.__den
        return Rational(num, den)


    def __rmul__(self, r):
        r = self.__validate(r)            
        return r * self


    def __truediv__(self, r):
        r = self.__validate(r)            

        num = self.__num*r.__den
        den = self.__den*r.__num
        return Rational(num, den)


    def __rtruediv__(self, r):
        r = self.__validate(r)            
        return r / self
    

    def __pow__(self, power):
        if not isinstance(power, (int, float)):
            raise TypeError('Power value must be int or float')
        
        return Rational(self.__num ** power, self.__den ** power)


    def __neg__(self):
        return Rational(-self.__num, self.__den)


    def __validate(self, r):
        if not isinstance(r, (int, Rational)):
            raise TypeError('Right operand must be Rational or int')
        
        if isinstance(r, int):
            r = Rational(r)
        
        return r
        

    def __simplify(self):
        num = self.__num
        den = self.__den
        
        div = 2
        while div <= min(abs(num), abs(den)):
            if (num % div == 0) and (den % div == 0):
                num = num // div
                den = den // div
            else:
                div += 1
            
        self.__num = num
        self.__den = den
        
    
    def num(self):
        return self.__num
    
    
    def den(self):
        return self.__den

