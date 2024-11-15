number = int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: '))

print(f'Você digitou os valores {number}')
print(f'O valor número 9 apareceu {number.count(9)} vezes')
print(f'O valor {number[1]} apareceu na 2° posição')
print(f'O valores pares digitados foram ', end=' ') 

for i  in number:
    if i % 2 == 0:
        print(i, end=' ')