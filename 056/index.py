exit = False

while not exit:
    first_value = float(input('Primeiro valor: '))
    second_value = float(input('Primeiro valor: '))

    soma = first_value + second_value
    multiply = first_value * second_value

    print('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novoc numeros
    [ 5 ] sair do programa
    ''')

    choose = int(input('Qual é a sua opção? '))

    if choose == 1:
        print('A soma ente {:.0f} e {:.0f} é igual á {}'.format(first_value, second_value, soma))
    elif choose == 2:
        print('A multiplicação ente {:.0f} e {:.0f} é igual à {}'.format(first_value, second_value, multiply))
    elif choose == 3:
        if first_value > second_value:
            print('O maior número é igual a {}'.format(first_value))
        else:
            print('O maior número é igual a {}'.format(second_value))
    elif choose == 4:
        first_value = float(input('Primeiro valor: '))
        second_value = float(input('Primeiro valor: '))
        
        choose = int(input('Qual é a sua opção? '))
    elif choose == 5:
        exit = True
print('Voce saiu do game!')