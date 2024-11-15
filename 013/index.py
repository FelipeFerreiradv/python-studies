opposite_side = float(input('Comprimento do Cateto oposto: ')) 
adjacent_side = float(input('Comprimento do Cateto adjacente: '))

hypotenuse = (opposite_side ** 2 + adjacent_side ** 2) ** (1/2)

print('A hipotenusa vai media {:.2f}'.format(hypotenuse))