#Comecando do desafio 28

nome = input('Digite seu nome:')

if nome == 'Pedro':
    print('Seu nome é de um cara Gostoso')
else:
    print('Seu nome e de quem tem pinto pequeno')
print('Bom dia {}'.format(nome))

av1 = float(input('Digite a sua primeira nota: '))
av2 = float(input('Digite a sua segunda nota:'))

media = (av1 + av2) / 2

if media >= 6:
    print('Você tirou uma boa media passou')
else:
    print('Sua media foi menor que 6 foi reprovado e tera que fazer AV3')


#SIMPLIFICANDO IF

print('Parabens Passou' if media >=6 else 'Sua media foi horrivel, não passou')#Tudo feito numa linha só