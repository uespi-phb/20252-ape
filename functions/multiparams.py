
def avg(*values):
    count = len(values)
    if count == 0:
        return 0.0
    
    sum = 0.0
    for value in values:
        sum += value
    return sum / count
    
    
def print_avg(prompt, *values):
    average = avg(*values)
    print(prompt, average)

print_avg('média:')