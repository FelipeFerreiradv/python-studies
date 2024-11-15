import random

first_student = input('Primeiro Aluno: ')
second_student = input('Primeiro Aluno: ')
third_student = input('Primeiro Aluno: ')
fourth_student = input('Primeiro Aluno: ')

random_student = [first_student, second_student, third_student, fourth_student]

random.shuffle(random_student)

print(' O aluno escolhido foi {}'.format(random_student))