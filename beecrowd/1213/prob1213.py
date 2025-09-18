import sys

for line in sys.stdin.readlines():   
    n = int(line)
    m = 1
    while m % n != 0:
        m = m*10 + 1
    
    print(len(str(m)))
