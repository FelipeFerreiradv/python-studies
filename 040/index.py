from random import randint
items = ('Pedra', 'Papel', 'Tesoura')

adversary = randint(0,2)

print('''Suas opções:
        [ 0 ] PEDRA
        [ 1 ] PAPEL
        [ 2 ] TESOURA''')

player = int(input('Qual é a sua jogada? '))

print('-=' * 11)
print('Computador jogou {}'.format(items[adversary]))
print('Jogador jogou {}'.format(items[player]))
print('-=' * 11)

if adversary  ==  0: # computador jogou pedra
    if player == 0:
        print('\033[36mEMPATE\033[m')
    elif player == 1:
        print('\033[32mVOCÊ GANHOU\033[m')
    elif player == 2:
        print('\033[31mVOCE PERDEU\033[m')
    else:
        print('\033[31mJOGADA INVÁIDA\033[m')

if adversary  ==  1: # computador jogou papel
    if player == 1:
        print('\033[36mEMPATE\033[m')
    elif player == 2:
        print('\033[32mVOCÊ GANHOU\033[m')
    elif player == 0:
        print('\033[31mVOCÊ PERDEU\033[m')
    else:
        print('\033[31mJOGADA INVÁIDA\033[m')

if adversary  ==  2: # computador jogou tesoura
    if player == 2:
        print('\033[36mEMPATE\033[m')
    elif player == 1:
        print('\033[32mVOCÊ GANHOU\033[m')
    elif player == 0:
        print('\033[31mVOCÊ PERDEU\033[m')
    else:
        print('\033[31mJOGADA INVÁIDA\033[m')