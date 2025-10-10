
file_name = 'prob.py'
fi = open(file_name,'r')
lines = fi.readlines()
fi.close()

width = len(str(len(lines)))
row = 0
for line in lines:
    row += 1
    print(f'{row:>{width}}: {line}', end='')
