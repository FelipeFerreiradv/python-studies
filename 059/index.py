print('-=' * 10, end=' ')
print('Gerador de PA', end=' ')
print('-=' * 10)

first_termo = int(input('Primeiro termo: '))
second_termo = int(input('Razão PA: '))

result = first_termo

more_term = 10

c = 1

tot =  0

while more_term != 0:
    tot = tot + more_term
    while c <= tot:
        c += 1
        result += second_termo

        print('{} ->'.format(result), end=' ')
    print('PAUSA')
    more_term = int(input('Quantos termos você quer mostrar mais? '))
print('Progressção finalizada com {} termos mostrados'.format(c + more_term))