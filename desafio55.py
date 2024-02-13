print('====== DESAFIO 55 ====')

pesoMenor = 0
pesoMaior = 0

for c in range(0, 5):
    peso = float(input('Digite o seu peso:'))
    if pesoMenor == 0:
        pesoMenor = peso
    if peso < pesoMenor:
        pesoMenor = peso
    if peso > pesoMaior:
        pesoMaior = peso

print('O maior peso é:{}'.format(pesoMaior))
print('o menor peso é:{}'.format(pesoMenor))