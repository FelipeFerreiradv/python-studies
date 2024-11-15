maior = 0
menor = 0

for p in range(1, 6):
    weight = float(input('O peso da  {}° pessoa: '.format(p)))

    if weight == 1:
        maior = weight
        menor = weight
    else:
        if weight > maior: 
            maior = weight
        elif weight < menor:
            menor = weight
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))