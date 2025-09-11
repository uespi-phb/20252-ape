# J=R+L

import sys

for expr in ['3+8=J', '5+L=5', 'R+7=5']: # sys.stdin.readlines():
    left, j = expr.split('=')
    r, l = left.split('+')
    if j == 'J':
        v = int(r) + int(l)
    elif r == 'R':
        v = int(j) - int(l)
    else:
        v = int(j) - int(r)
        
    print(v)
