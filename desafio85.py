print('===== DESAFIO 85 =====')

numeros = list()
numeros2 = [[], []]
dadoP = list()
dadoI = list()
copia = 0
"""
for c in range(0,7):
    copia = int(input('Digite:'))
    if copia % 2 == 0:
        dadoP.append(copia)
    else:
        dadoI.append(copia)

dadoP.sort()
dadoI.sort()
numeros.append(dadoP[:])
numeros.append(dadoI[:])
print(numeros)
"""

for c in range(0,7):
    copia = int(input('Digite:'))
    if copia % 2 == 0:
        numeros2[0].append(copia)
    else:
        numeros2[1].append(copia)

numeros2.sort()
print(numeros2)
print(numeros2[0])
print(numeros2[1])

