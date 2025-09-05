
major = 0
position = 0

k = 0
while k < 100:
    k += 1
    number = int(input())
    if number > major:
        major = number
        position = k
        
print(major)
print(position)
