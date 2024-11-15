number = []

maior = menor = 0

for i in range(0, 5):
    number.append(int(input(f'Digite um numero para a posições {i}: ')))

    if i == 0:
        maior = menor = number[i]

    elif number[i] > maior:
        maior = number[i]
    elif number[i] < menor:
        menor = number[i]
print('-=' * 20)
print(f'Você digitou os vlaores {number}')
print(f'O maior valor digitado foi {maior}')
print(f'O menor valor digitado foi {menor}')