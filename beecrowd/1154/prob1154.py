
sum = 0
count = 0

while True:
    number = int(input())
    if number < 0:
        break
    sum = sum + number      # sum += number
    count = count + 1       # count += 1

average = sum / count
print('%0.2f' % (average))
