print('===== DESAFIO 40 =====')

av1 = float(input('Digite a primeira nota:'))
av2 = float(input('Digite a segunda nota:'))

media = (av1+av2) / 2

if media < 5:
    print('Reprovado')

elif media >= 5 and media <= 6.9:
    print('Recuperação')

elif media > 6.9:
    print('Aprovado')