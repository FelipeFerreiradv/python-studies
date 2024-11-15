number_input = int(input('Digite um número: '))

numbers = 'zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 'desesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'


for c in range(0, 20):
    if number_input > 20:
      number_input = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o numero: {numbers[number_input]}')