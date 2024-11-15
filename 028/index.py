first_value = float(input('Primeiro valor: '))
second_value = float(input('Segundo valor: '))
third_value = float(input('Terceiro valor: '))

biggest_value = first_value

if first_value < second_value and first_value < third_value:
    print('O primeiro valor {:.0f} é o menor valor'.format(first_value))
elif first_value > second_value and first_value > third_value:
    print('O primeiro valor {:.0f} é o maior valor'.format(first_value))

if second_value < first_value and second_value < third_value:
    print('O segundo valor {:.0f} é o menor valor'.format(second_value))
elif second_value > first_value and second_value > third_value:
    print('O segundo valor {:.0f} é o maior valor'.format(second_value))

if third_value < first_value and third_value < second_value:
    print('O terceiro valor {:.0f} é o menor valor'.format(third_value))
elif third_value > second_value and third_value > first_value:
    print('O terceiro valor {:.0f} é o maior valor'.format(third_value))