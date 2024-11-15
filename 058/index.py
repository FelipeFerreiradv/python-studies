print('-=' * 10, end = ' ')
print('Gerador de PA', end = ' ')
print('-=' * 10)

first_term = int(input('Primeiro termo: '))
second_term = int(input('Razão da PA: '))

term = first_term

c = 1
while c <= 10:
    term += second_term
    c+=1

    print('{} ->'.format(term), end = ' ')
print('FIM')