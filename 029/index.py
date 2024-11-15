salar = float(input('Escreva seu atual salário: '))

increase = (10 / 100) * salar

result = salar + increase

if salar >= 1250:
    print('Seu salário sofreu um aumento de 10%, resultando em {:.2f}'.format(result))
else:
    new_increase = (15 / 100) * salar
    print('Seu salário sofreu um aumento de 15%, resultando em {:.2f}'.format(new_increase + salar))