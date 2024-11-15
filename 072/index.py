from random import randint

number_random = randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)

print('Os valores sorteados foram ', end=' ')

for c in number_random:
    print(f'{c}', end=' ')
print(f'O maior valor sorteado foi {max(number_random)}')
print(f'O menor valor sorteado foi {min(number_random)}')