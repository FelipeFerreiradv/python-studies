phrase  = input('Digite uma frase: ').upper().strip()

print('A letra A aparece {} vezes na frase.'.format(phrase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(phrase.find('A') + 1))
print('A primeira letra A apareceu na posição {}'.format(phrase.rfind('A') + 1))