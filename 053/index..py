r = 'S'
par = impar = 0
while r == 'S':
    n = int((input('Digite um vlaor: ')))
    r = input('Voce quer continuar?[S/N]: ').upper()

    if n % 2 == 0:
        par +=1
    else:
        impar +=1
print('Voce digitou {} número pares e {} número impares'.format(par, impar))
print('FIM')