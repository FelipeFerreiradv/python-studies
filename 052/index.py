name_maior = ''
maior =  0
menor = 0

for p in range(1, 5):
    # faz os inputs
    print('----- {}° PESSOA -----'.format(p))
    name = input('Name: ').strip()
    age = int(input('Age: '))
    sex = input('Sexo [M/F]: ').strip()

    if age == 1 and sex in 'Mm':
        maior = age
        name_maior - name
    elif sex in 'Mm' and age > maior:
        maior = age
        name_maior = name

    elif age < 20 and sex in 'Ff':
        menor +=1
    
    average = age / 4 # soma as médias dos nomes
print('A média de idade do grupo é de {}'.format(average))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, name_maior))
print('Ao todo {} mulheres tem idade abaixo de 20 anos'.format(menor))