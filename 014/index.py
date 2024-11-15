from math import radians, sin,cos,tan
angle = float(input('Digite o ângulo desejado: '))

sin = sin(radians(angle))
cos = cos(radians(angle))
tan = tan(radians(angle))

print('O ângulo {} \n tem o seno de {:.2f}, \n seu cosseno é {:.2f} \n e sua tangente é {:.2f}'.format(angle, sin, cos, tan))