number_first = float(input('Primeiro número:'))
number_second = float(input('Segundo número:'))

if number_first > number_second:
    print('O PRIMEIRO valor é maior')
elif number_second > number_first:
    print('O SEGUNDO valor é maior')
else:
    print('Não existe número maior, os dois são iguais')