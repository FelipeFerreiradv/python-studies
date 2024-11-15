side = float(input('Primeiro segmento: '))
second_side = float(input('Segundo segmento: '))
third_side = float(input('Terceiro segmento: '))

if side + second_side > third_side:
    print('O triângulo pode ser formado')
else:
    print('O triângulo não pode ser formado')

if side == second_side == third_side:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
elif side != second_side != third_side != side:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
else:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')