
use_cases = 0
while True:
    use_cases += 1
    
    n = int(input())
    if n == 0:
        break

    max_len = 0
    lines = []
    for k in range(n):
        line = input().strip()
        
        line_len = 0
        prev_len = 1
        while line_len != prev_len:
            prev_len = len(line)
            line = line.replace('  ', ' ')
            line_len = len(line)

        if line_len > max_len:
            max_len = line_len
            
        lines.append(line)

    if use_cases > 1:
        print()
        
    for line in lines:
        print(line.rjust(max_len))
