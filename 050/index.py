count = 0
count_menor = 0

for c in range(0, 7):

    person = int(input('Em que ano a primeira pessoa nasceu? '))

    result = 2024 - person

    if result >= 18:
        count +=1
    else:
        count_menor +=1

print('{} SÃO MAIORES DE IDADE'.format(count))
print('{} SÃO MENORES DE IDADE'.format(count_menor))