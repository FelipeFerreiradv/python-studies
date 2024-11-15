from datetime import date

year = int(input('Escreva o ano que quer analizar, caso queira analizar o ano atual digite 0: '))

if year == 0:
    year = date.today().year
    
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('O ano {} é um ano BISSESTO'.format(year))
else:
    print('O ano {} é um ano NÃO É UM ANO BISSESTO'.format(year))
