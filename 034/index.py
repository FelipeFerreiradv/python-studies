nasciment = int(input('Ano de dascimento: '))

nasciment_count = 2024 - nasciment

still_counts = 18 - nasciment_count

nasciment_next = 2024 + still_counts

if still_counts != 0:
    print('''
    Quem nasceu em {} tem {} anos em 2024.
    Ainda faltam {} anos para o alistamento.
    Seu alistamento será em {}
    '''.format(nasciment, nasciment_count, still_counts, nasciment_next))
elif still_counts == 0:
    print('''
    Quem nasceu em {} tem {} anos em 2024.
    Ainda precisa se alistar IMEDIATAMENTE.
    Seu alistamento será em {}
    '''.format(nasciment, nasciment_count, nasciment_next))