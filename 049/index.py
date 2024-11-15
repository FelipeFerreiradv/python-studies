phrase = input('Digite uma frase: ').strip().upper()

words = phrase.split()

join = ''.join(words)

invert =  join[::-1]

# for lettering in range(len(join) - 1, -1, -1):
#     invert += join[lettering]
# print(join, invert)

print(join, invert)
if join == invert:
    print('É UM PALINDROMO')
else:
    print('Não é um palindromo')