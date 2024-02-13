
mais18 = 0
contHomens = 0
mulheres20 = 0
while True:
    idade = int(input('Digite sua idade:'))
    if idade > 18:
        mais18 += 1

    sexo = str(input('Digite seu Sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF': #ENQUANTO SEXO NAO FOR M ou F continue // sexo == 'M' or sexo == 'F'
        sexo = str(input('Digite seu sexo [M/F]:  '))

    if sexo in 'M':
        contHomens += 1

    elif sexo in 'F' and idade <= 20:
        mulheres20 += 1

    continuar = str(input('Deseja continuar [S/N]?')).strip().upper()

    if continuar == 'N':
        print('-='*20)
        print('PROGRAMA FINALIZADO')
        print('-=' * 20)
        break

    print('-='*20)
    print('Pessoa Cadastrada')
    print('-='*20)

print('='*20)

print(f'{contHomens} homens foram cadastradas')
print(f'{mulheres20} mulheres com menos de 20')
print(f'{mais18} Pessoas com mais de 18 anos ')