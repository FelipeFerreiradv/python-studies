wage = float(input('Qual é o  salário do Funcionário? R$'))

increase = (15 / 100) * wage

result = wage + increase

print('Um funcionário qye ganhava {:.2f}, com 15% de aumento, passa a receber {:.2f}'.format(wage, result))