count = 0

more  = 0
less = 0
med = 0

soma = 0

quests = 'S'
while quests in 'Ss':
    count += 1

    number = int(input('Digite um número: '))
    quests = str(input('Quer continuar? [S/N]' )).upper().strip()[0]

    soma += number
    med = soma / count

    if count == 1:
        more = less = number
    else:
        if number > more:
            more = number
        elif number < less:
            less = number
print('Você digitou {} e a media foi {:.2f}'.format(count, med))
print('O maior valor foi {} e o menor foi {}'.format(more, less))