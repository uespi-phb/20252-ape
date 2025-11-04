
class Rational:
    def __init__(self, num, den=None):       
        if isinstance(num, int):
           if den is None:
               den = 1

           if not isinstance(den, int):
               raise TypeError('Denominator must be integer')
        elif isinstance(num, str):
            values = num.split('/')
            if len(values) != 2:
                raise ValueError('Rational string format is invalid')
            if values[0].isdigit() and values[1].isdigit():
                num = int(values[0])
                den = int(values[1])
            else:
                raise ValueError('Rational string format is invalid')                
        else:
            raise TypeError('Numerator must be integer')
        
        self.num = num
        self.den = den


    def __str__(self):
        return f'{self.num}/{self.den}'
        

    def add(self, r):
        num = self.num*r.den + r.num*self.den
        den = self.den*r.den
        return Rational(num, den).simplify()


    def sub(self, r):
        num = self.num*r.den - r.num*self.den
        den = self.den*r.den
        return Rational(num, den).simplify()


    def mul(self, r):
        num = self.num*r.num
        den = self.den*r.den
        return Rational(num, den).simplify()


    def div(self, r):
        num = self.num*r.den
        den = self.den*r.num
        return Rational(num, den).simplify()


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

        
    def show(self):
        print(f'{self.num}/{self.den}')
