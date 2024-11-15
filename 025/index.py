number = int(input('Digite um numero: '))

result = number %  2

if result == 0:
    print('Seu número {} é PAR!'.format(number))
else:
    print('Seu numero {} é IMPAR'.format(number))