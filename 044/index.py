s = 0

for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c

print('A soma entre os valores de 1 a 500 sendo multiplos de 3 é igual a {}'.format(s))
print('ACABOU')