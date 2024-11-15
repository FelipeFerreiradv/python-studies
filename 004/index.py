value = float(input('Quando você tem na carteira? R$:'))

result = value / 5.59

print('Com o valor de R${:.2f} você pode comprar US{:.2f} dólares'.format(value, result))