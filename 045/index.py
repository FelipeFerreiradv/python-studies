print('\033[33m*=\033[m' * 15)
print('\033[33mTABUADA DA FELICIDADE\033[m')
print('\033[33m*=\033[m' * 15)

number =  float(input('Digite um número: '))

for c in range(1, 11):
    value = number * c

    print('{:.0f} x {} = {:.0f}'.format(number, c, value))
print('\033[33mOBRIGADO!\033[m')