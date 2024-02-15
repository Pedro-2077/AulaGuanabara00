
valor = []
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor:')))

print(f'Foram digitados {valor}')
print(f'O maior valor foi {max(valor)} na posição {valor.index(max(valor))}')
print(f'O menor valor foi {min(valor)} na posição {valor.index(min(valor))}')
