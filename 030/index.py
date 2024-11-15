print('=' * 70)
print('Analisador de Triaângulos')
print('=' * 70)

segment = float(input('Primeiro segmento: '))
second_segment = float(input('Segundo segmento: '))
third_segment = float(input('Terceiro segmento: '))

if segment < second_segment + third_segment and second_segment < segment + third_segment and third_segment < second_segment + segment:
    print('os segmentos acima PODEM FORMAR um triângulo!')
else:
    print('os segmentos acima NÃO PODEM FORMAR um triângulo!')