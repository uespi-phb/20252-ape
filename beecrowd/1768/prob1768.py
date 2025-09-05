
from sys import stdin

for line in stdin.readlines():
    n = int(line)
        
    for step in range(2):
        # if step == 0:
        #     rows = (n // 2) + 1
        # else:
        #     rows = 2
        
        rows = (n // 2) + 1 if step == 0 else 2
        
        row_spaces = n // 2
        row_stars = 1
        for row in range(rows):
            line = (' ' * row_spaces) + ('*' * row_stars)
            print(line)
            
            row_spaces -= 1
            row_stars  += 2

    print()
