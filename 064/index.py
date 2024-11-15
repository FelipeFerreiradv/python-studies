while True:
    number = int(input('Quer ver a tabuada de qual valor? '))

    print('-' * 30)
    for c in range(1, 11):
        result = number * c

        print(f'{number} x {c} = {result}')
    print('-' * 30)

    if number <= 0:
        break
print('A sua seleção de tabuada foi finalizada')