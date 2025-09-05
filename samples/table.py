
header_name = ('Fruta','Preço')
fruit_name = ('Ata','Abacate','Mamão','Maçã','Uva Top','Tangerina')
fruit_price = (21.76, 9.55, 11.98, 5.76, 100.90, 13.54)

col_name_width = len(header_name[0])
col_price_width = len(header_name[1])
for i in range(len(fruit_name)):
    col_name_width = max(col_name_width, len(fruit_name[i]))

    price = '%0.2f' % (fruit_price[i])
    col_price_width = max(col_price_width, len(price))

table_width = col_name_width + col_price_width + 1
print('-' * table_width)
header_line = '%*s|%*s' % (
    -col_name_width, header_name[0],
    col_price_width, header_name[1]
)
print(header_line)
print('-' * table_width)

for i in range(len(fruit_name)):
    price = '%0.2f' % (fruit_price[i])
    line = '%-*s|%*s' % (col_name_width, fruit_name[i], col_price_width, price)
    print(line)