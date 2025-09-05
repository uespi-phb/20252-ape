
print('### TRIÂNGULO DE PASCAL ###\n')

n = int(input('Nº de linhas: '))

pascal_triangle = []
elem_max = 1
for i in range(n):
    curr_line = []
    for j in range(i + 1):
        if j == 0 or j == i:
            elem = 1
        else:
            prev_line = pascal_triangle[i - 1]
            elem = prev_line[j] + prev_line[j - 1]
        
        if elem > elem_max:
            elem_max = elem

        curr_line.append(elem)
    pascal_triangle.append(curr_line)

# [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

elem_width = len(str(elem_max)) + 1
for line in pascal_triangle:
    for elem in line:
        data = '%*d' % (elem_width, elem)
        print(data, end='')
    print()
