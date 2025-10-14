
from sys import argv

argc = len(argv)
if argc != 3:
    print(f'usage: {argv[0]} SOURCE TARGET')
    exit(-1)

block_size = 1024
ifile = open(argv[1], 'rb')
ofile = open(argv[2], 'wb')

while True:
    buffer = ifile.read(block_size)
    ofile.write(buffer)
    if len(buffer) < block_size:
        break
    
ifile.close()
ofile.close()