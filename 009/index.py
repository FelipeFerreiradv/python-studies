days = int(input('Quantos dias você esteve com o carro? '))

distance = float(input('Quando km você rodou com o carro? '))

result = (60 * days) + (0.15 * distance)

print('O total a pagar é de R${:.2f}'.format(result))