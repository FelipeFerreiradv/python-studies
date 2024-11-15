width = float(input('Largura da parede:'))
height = float(input('Altura da parede:'))

area = width * height

liters = area / 2

print('Sua parede tem a dimensãop de {}x{} e sua área é de {}m².'.format(width, height, area))
print('para printar essa parede, você precisara de {} de tinta.'.format(liters))