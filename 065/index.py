from random import randint

count_win = 0

while True:
    print('-='  * 20)
    print('VAMOS JOGAR PAR OU ÍMPAR')
    print('-='  * 20)

    number = int(input('Diga um valor (entre 0 e 10): '))
    number_computer = randint(0, 10)
    result = number + number_computer

    choose = str(input('Par ou Ímpar?[P/I] ')).upper().strip()

    print('-' * 50)
    print(f'Você jogou {number} e o computador {number_computer}. Total de {result}', end=' ')
    if result % 2 == 0:
        print('DEU PAR')
    else:
        print('DEU IMPAR')
    print('-' * 50)

    if choose in 'Pp' and result % 2 == 0:
        count_win += 1

        print('Você VENCEU!')
        print('Vamos jogar novamente...')
    else:
        break

print('Você PERDEU!')
print('-='  * 10)
print(f'GAME OVER! Você venceu {count_win} vezes.')