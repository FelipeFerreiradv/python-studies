count = 1

soma = 0

num = int(input('Diigte um número [999 para parar]: '))

while num != 999:
    count += 1


    soma  += num
    num = int(input('Diigte um número [999 para parar]: '))
print('Voce digitou {} número e a soma entre eles é igual á {}'.format(count - 1, soma))