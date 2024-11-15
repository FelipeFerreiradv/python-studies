print('Digite um numero para')
number = float(input('Calcular seu fatorial: '))
c = number
f = 1

while c > 0:
    print('{:.0f} x'.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))