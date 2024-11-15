number = []

while True:
    number_add = int(input('Digite um valor: '))

    if number_add not in number:
        number.append(number_add)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado, não vou adicionar')

    choosen = str(input('Quer continuar? [S/N] '))

    if choosen in 'Nn':
        break
print('-=' * 20)
number.sort();
print(f'Os valores digitados são {number}')