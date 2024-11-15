count = soma = 0

while True:
    count += 1
    number = int(input('Digite um numero (999 para parar): '))


    if number == 999:
        break

    soma += number
print(f'A soma dos {count - 1} valores foi {soma}')