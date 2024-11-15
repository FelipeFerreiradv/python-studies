number = int(input('Digite um numero entre 0 e 9999: '))
u = number // 1 % 10 
d = number // 10 % 10 
c = number // 100 % 10 
m = number // 1000 % 10 

if number < 0 | number > 9999:
    print('type other number')
else:
    print('Unidade:  {}'.format(u))
    print('Dezena:  {}'.format(d))
    print('Centena:  {}'.format(c))
    print('Milhar:  {}'.format(m))