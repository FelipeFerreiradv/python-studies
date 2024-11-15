print('-' * 10 , end=' ')
print('Sequência de Fibonacci', end=' ')
print('-' * 10)

number = int(input('Quantos termos você quer mostrar? '))

c = 3

t1 = 0
t2 = 1

print('{} -> {}'.format(t1, t2), end=' ')

while c != number:
    t3 = t1 + t2
    t1 = t2
    t2 = t3

    c += 1

    print('->  {}'.format(t3), end=' ')
print('FIM')