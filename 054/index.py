sex = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sex not in 'MmFf':
    sex = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Dados registrados, seu sexo {} foi enviado'.format(sex))