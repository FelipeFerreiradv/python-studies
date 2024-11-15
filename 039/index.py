print('===============  LOJAS FELIPE FERREIRA ===============')

price = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
        [ 1 ] à vista dinehiro/cheque
        [ 2 ] à vista cartão
        [ 3 ] 2x nmo cartão
        [ 4 ] 3x ou mais no cartão''')
option = int(input('Qual é a opção? '))

discont_cash = (10 / 100) * price
discont_card = (5 / 100) * price
taxes = (20 / 100) * price

if(option == 1):
    print('O valor que terá que pagar será de {:.2f}'.format(price - discont_cash))
if(option == 2):
    print('O valor que terá que pagar será de {:.2f}'.format(price - discont_card))
if(option == 3):
    print('O valor que terá que pagar será de {:.2f}'.format(price))
if(option == 4):
    print('O valor que terá que pagar será de {:.2f}'.format(price + taxes))