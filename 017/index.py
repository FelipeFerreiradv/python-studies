name = input('Digite seu nome completo: ').strip()

print(name.upper())
print(name.lower())
print('Seu nome ao todo tem  {}'.format(len(name) - name.count(' ')))
# print('Seu primeiro noem tem {} letras'.format(name.find(' ')))
split = name.split()
print('Seu primeiro nome é {}, ele tem {} letras'.format(split[0], len(split[0])))
print('Seu primeiro nome é {}, ele tem {} letras'.format(split[1], len(split[1])))
print('Seu primeiro nome é {}, ele tem {} letras'.format(split[2], len(split[2])))
print('Seu primeiro nome é {}, ele tem {} letras'.format(split[3], len(split[3])))