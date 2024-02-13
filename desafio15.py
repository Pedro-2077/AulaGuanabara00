km = float(input('Quantos quilometros rodado:'))
dias = int(input("Quantos dias foi alugado"))

km *= 0.15
dias *= 60

valor = km + dias

print('O vaor total a pagar é:R${}'.format(valor))