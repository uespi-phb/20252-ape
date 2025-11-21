
class PrimeNumbers:
    
    def __init__(self, n = None):
        if isinstance(n, int):
            if n < 1:
                raise ValueError(f'N is invalid: {n}')

        self.__count = n
        self.__index = None
        self.__last = None

    
    def __str__(self):
        return f'PrimeNumber({self.__count})'
    

    def __repr__(self):
        return str(self)


    def __iter__(self):
        return self
        
        
    def __next__(self):
        try:
            next_prime = self.next()
        except IndexError:
            raise StopIteration()
        return next_prime
    
    
    def __is_prime(self, n):
        max_div = int(n ** 0.5)
        for div in range(2, max_div + 1):
            if n % div == 0:
                return False
        return True
    
    
    def next(self):
        if self.is_finite() and self.__index == self.__count - 1:
            raise IndexError('No more prime numbers')
        
        if self.__index is None:
            self.__index = 0
            self.__last = 2
            return self.__last
        
        if self.__index == 0:
            self.__index += 1
            self.__last = 3
            return self.__last
        
        prime_cand = self.__last + 2
        while not self.__is_prime(prime_cand):
            prime_cand += 2
        
        self.__last = prime_cand
        self.__index += 1
        
        return self.__last

    
    def reset(self):
        self.__index = None
        self.__last = None
            
        
    def is_finite(self):
        return self.__count is not None
    
    
    def is_infinite(self):
        return not self.is_finite()
