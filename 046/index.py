s = 0
count = 0

for c in range(0, 6):
    num = int(input('Digite um número inteiro: '))

    if num % 2 == 0:
        s += num
        count += 1

print('A soma de {} pares são IGUAIS Á {}'.format(count, s))
print('OBRIGADO!')