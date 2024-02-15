print('===== DESAFIO 80 =====')

n = []
copia = 0

for c in range(0, 5):
    copia = int(input('Digite um valor: '))
    if c == 0 or copia > n[-1]:
        n.append(copia)
        print(f'Adicionado na posição {c}')

    else:
        cont =0
        while cont < len(n):
            if copia <= n[cont]:
                n.insert(cont, copia)
                print(f'Adicionado na pocição {cont}')
                break

print(f'Os valores digitados são {n}')