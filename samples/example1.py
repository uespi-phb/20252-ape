from random import randint

def rand_number(digits):
    min = 10 ** (digits -1)
    max = 10 ** digits -1
    return randint(min, max)

def lsd(n):
    return n % 10

lsd2 = lambda n: n % 10

numbers = []
for k in range(10):
    digits = randint(1,5)
    numbers.append(rand_number(digits))
    
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(key=lambda n: n % 10)
print(numbers)
numbers.sort(key=lsd)
print(numbers)
numbers.sort(key=lsd2)
print(numbers)
