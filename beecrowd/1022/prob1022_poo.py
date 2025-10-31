
class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
    def add(self, r):
        x = self.num*r.den + r.num*self.den
        y = self.den*r.den
        return Rational(x, y)
        
    def show(self):
        print(f'{self.num}/{self.den}')

