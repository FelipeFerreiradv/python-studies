print('-' * 30)
print('     CADASTRE UMA PESSOA      ')
print('-' * 30)

count_18 = count_man = count_woman = 0

while True:
    print('-=' * 20)
    age = int(input('Idade: '))
    sex =  str(input('[M/F]: ')).upper().strip()[0]
    print('-=' * 20)

    choose = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('-=' * 30)

    if age > 18:
        count_18 += 1

    elif sex == 'M':
        count_man += 1

    elif age < 20:
        count_woman += 1

    if choose in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {count_18}')
print(f'Ao todo temos {count_man} homens cadastrados')
print(f'Ao todo temos {count_woman} mulheres com menos de 20 anos')