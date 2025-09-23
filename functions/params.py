
def avg(values):
    if isinstance(values, (int, float)):
        return values
    
    if not isinstance(values, (list, tuple)):
        return 0.0
        
    count = len(values)
    if count == 0:
        return 0.0
    
    sum = 0.0
    for value in values:
        sum += value
    return sum / len(values)

