nasciment = int(input('Ano em que você nasceu: '))

result = 2024 - nasciment

if result <= 9:
    print('\033[32mCLASSIFICAÇÃO: MIRIM\033[m')
elif result <= 14:
    print('\033[32mCLASSIFICAÇÃO: INFANTIL\033[m')
elif result <= 19:
    print('\033[32mCLASSIFICAÇÃO: JUNIOR033[m')
elif result <= 25:
    print('\033[32mCLASSIFICAÇÃO: SÊNIOR\033[m')
else:
    print('\033[32mCLASSIFICAÇÃO: MASTER\033[m')