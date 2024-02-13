print('====== DESAFIO 56 ====')

nomeVelho = ''
mulheresM20 = 0
idadeVelho = 0
media = 0
soma = 0

for c in range(0,4):
    nome = str(input('Digite seu nome:'))
    idade = int(input('Digite a idade:'))

    soma += idade

    sexo = str(input('Digite o sexo M ou F: ')).upper().strip()
    if sexo == 'M':
        if idade > idadeVelho:
            idadeVelho = idade
            nomeVelho = nome
    if sexo == 'F':
        if idade < 20:
            mulheresM20 += 1

media = soma / 4

print('A media de idade do grupo é {}'.format(media))
print('O homem mais velho é {}'.format(nomeVelho))
print('Ao todo temos {} mulheres com menos de 20 anos'.format(mulheresM20))