futebol = 'Botafogo', 'Palmeiras', 'Fortaleza', 'Flamengo', 'São Paulo', 'Internacional', 'Bahia', 'Cruzeiro', 'Atletico-MG', 'Vasco', 'Fluminense', 'Criciúma', 'Grêmio', 'Gragantino', 'Juventude', 'Vtória', 'Corinthians', 'Atletico-PR', 'Cuiabá', 'Atletico-GO'

print('-=' * 45)
print(f'Lista de times do brasileirão: {futebol}')
print('-=' * 45)
print(f'Os 5 primeiros são {futebol[:5]}')
print('-=' * 45)
print(f'Os 4 ultimos são {futebol[-4:]}')
print('-=' * 45)
print(f'Times em ordem aufabética são {sorted(futebol)}')
print('-=' * 45)
print(f'O chapecoense está na', end=' ')
print(futebol.index('Atletico-MG'))