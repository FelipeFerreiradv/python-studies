from random import randint

print('=' * 70)
print('Vou pensar em um numero  entre 0 e 5. Tente adivinhar...')
print('=' * 70)

number_computer = randint(0, 5) # faz o computador pensar
number = int(input('Em que numero eu pensei? ')) # numero escolhido pelo jogador

if number == number_computer:
    print('\033[36mProcessando...\033[m')
    print('\033[30;42mPARABENSS! Voce ganhou o desafio\033[m')
else:
    print('\033[36mProcessando...\033[m')
    print('\033[30;41mERRADO, o computador ganhou hahaha, eu pensei no número {} e não no {}\033[m'.format(number_computer, number))