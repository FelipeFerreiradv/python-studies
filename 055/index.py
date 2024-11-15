from random import randint

print('''-----GAME DE ADIVINHAÇÃ0-----
      Sou seu computador
      Acabei de pensar em um número entre 0 e 10.
      Consegue adivinhar qual foi?''')

number_computer = randint(0, 10)

count = 0

acert = False

while not acert:
    quest = int(input('Qual é o seu palpite? '))
    count += 1

    if quest == number_computer:
        acert = True
    if number_computer > quest:
        print('Mais... Tente mais una vez.')
    elif number_computer < quest:
        print('Menos... Tente mais uma vez.')
print('Acertou com {}'.format(count))