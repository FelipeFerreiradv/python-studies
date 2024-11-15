print('\033[33m*=\033[m' * 15)
print('\033[33m     10 TERMOS DE UMA PA\033[m')
print('\033[33m*=\033[m' * 15)

term = int(input('Primeiro termo: '))
racion = int(input('Razão: '))
dec = term + (10 -1) * racion

for c in range(term, dec, racion):
    print('{}  -> '.format(c), end= ' ')
print('ACABOU')