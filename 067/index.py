print('-' * 30) 
print('         LOJA BARATÃO')
print('-' * 30) 

tot = count = count_1000 = barato = 0

name_barato = ''

while True:
    name_product = str(input('Nome do produto: '))
    price = float(input('Preço: R$'))
    choosen = str(input('Quer continuar? [S/N] '))

    count += 1

    tot += price

    if price > 1000:
        count_1000 += 1

    if count == 1:
        barato = price
        name_barato = name_product
    elif price < barato:
        barato = price
        name_barato = name_product

    if choosen in 'Nn':
        break
print('-' * 30, end=' ')
print('FIM DO PROGRAMA', end=' ')
print('-' * 30)
print(f'O total da compra foi R${tot:.2f}')
print(f'Temos {count_1000} produto custando mais de R$1000.00')
print(f'O produto mais barato foi {name_barato} que custa {barato}')