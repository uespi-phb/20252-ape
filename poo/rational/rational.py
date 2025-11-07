
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
        
        self.num = num
        self.den = den


    def __repr__(self):
        return f'Rational({self.num},{self.den})'


    def __str__(self):
        return f'{self.num}/{self.den}'
        

    def __add__(self, r):
        r = self.validate(r)            
        
        num = self.num*r.den + r.num*self.den
        den = self.den*r.den
        return Rational(num, den).simplify()


    def __sub__(self, r):
        r = self.validate(r)            

        num = self.num*r.den - r.num*self.den
        den = self.den*r.den
        return Rational(num, den).simplify()


    def __mul__(self, r):
        r = self.validate(r)            

        num = self.num*r.num
        den = self.den*r.den
        return Rational(num, den).simplify()


    def __truediv__(self, r):
        r = self.validate(r)            

        num = self.num*r.den
        den = self.den*r.num
        return Rational(num, den).simplify()

    def validate(self, r):
        if not isinstance(r, (int, Rational)):
            raise TypeError('Right operand must be Rational or int')
        
        if isinstance(r, int):
            r = Rational(r)
        
        return r
        

    def simplify(self):
        num = self.num
        den = self.den
        
        div = 2
        while div <= min(abs(num), abs(den)):
            if (num % div == 0) and (den % div == 0):
                num = num // div
                den = den // div
            else:
                div += 1
            
        return Rational(num, den)



r1 = Rational(-1,4)
r2 = Rational(3,7)
