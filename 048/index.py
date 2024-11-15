number = int(input('Digite um número: '))
tot = 0

for c in range(1, number + 1):
    if number % c == 0:
        tot +=1
    else: 
        tot +=1

    print(c, end = ' ')
print('o numero {} foi divisível {} vezes'. format(number, tot))

if tot == 2:
    print('E por isso que ele É PRIMO');
else:
    print('è por isso que ele NÃO É PRIMO')