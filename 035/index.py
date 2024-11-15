first_note = float( input('Sua primeira nota: '))
second_note = float( input('Sua segunda nota: '))

result = (first_note + second_note) / 2

if result < 5:
    print('Quem tirou {} e {}, tem a média de {} \n VOCÊ FOI REPROVADO'. format(first_note, second_note, result))
elif result >= 5 and result <= 6.9:
    print('Quem tirou {} e {}, tem a média de {} \n VOCÊ ESTÁ DE RECUPERAÇÃO'. format(first_note, second_note, result))
elif result >= 7:
    print('Quem tirou {} e {}, tem a média de {} \n VOCÊ ESTÁ APROVADO'. format(first_note, second_note, result))