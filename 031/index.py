house_value = float(input('Valor da casa: '))
salar = float(input('Salário do comprador: '))
years = float(input('Quantos anos de financimento: '))

installments = (years * 12) / house_value

porcent = (30 / 100) * salar

if installments <= porcent:
    print('Para pagar uma cada de {:.2f}  em {:.0f} a prestração será de {:.2f}'.format(house_value, years, installments))
    print('\033[0;31mEmpréstimo negado\033[m')
else:
    print('Para pagar uma cada de {:.2f}  em {:.0f} a prestração será de {:.2f}'.format(house_value, years, installments))
    print('\033[0;32mEmpréstimo aceito\033[m')