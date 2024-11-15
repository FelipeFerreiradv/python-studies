distance =  float(input('Qual é a distancia de sua viagem? '))

result_low = distance * .50
result_hight = distance * .45

if distance <= 200:
    print('Você terá que pagar o valor de R${:.2f}'.format(result_low))
else:
    print('Você terá que pagar o valor de R${:.2f}'.format(result_hight))