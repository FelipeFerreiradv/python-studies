velocity = float(input('Qual é a velocidade atual do carro? '))

if velocity > 80:
    mult = (velocity - 80)  * 7

    print('MULTADO! Você excedeu o limite permitido que é 80km/h')
    print('Você deve pagar a multa de R${:.2f}'.format(mult))
    print('Tenha um bom dia! Dirija com segurança')
else:
    print('Tenha um bom dia! Dirija com segurança')
