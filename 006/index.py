price = float(input('Qual é o preço do produto? R$'))

discount = (5 / 100) * price

result = price - discount

print('O produto que custava R${:.2f}, na promoção com desocnto de 5% vai custar {:.2f}'.format(price, result))