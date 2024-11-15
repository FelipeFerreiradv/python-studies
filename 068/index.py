print('=' * 30)
print('         BANCO FELIPE')
print('=' * 30)

value = int(input('que valor você quer sacar? R$'))
tot = value
ced = 50
totced = 0

while True:
    if tot >= ced:
        tot -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if tot == 0:
            break