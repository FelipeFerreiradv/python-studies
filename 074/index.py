print('-' * 60)
print('                     LISTAGEM DE PREÇOS')
print('-' * 60)

items = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 4.20, 'Transferidor', 9.99, 'Compasso', 120.32, 'Mochila', 'Canetas', 22.30, 'Livro', 34.90)

for i in range(0, len(items)):
    if i % 2 == 0:
        print(f'{items[i]:.<30}', end='')
    else:
        print(f'R${items[i]:>7}')