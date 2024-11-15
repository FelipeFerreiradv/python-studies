number = int(input('Digite um número inteiro: '))
# result =  

print('Escolha uma das bases para conversão: ')
print('[ 1 ] Convertar para BINÁRIO')
print('[ 2 ] Convertar para OCTAL')
print('[ 3 ] Convertar para HEAXADECIMAL')

choose = int(input('Sua opção: '))

if choose == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(number, bin(number)[2:]))
elif choose == 2:
    print('{} convertido para OCTAL é igual a {}'.format(number, oct(number)[2:]))
elif choose == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(number, hex(number)[2:]))
else:
    print('Tente novamente, por favor digite outro número')