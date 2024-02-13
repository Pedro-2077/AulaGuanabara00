import math

cateto_oposto = float(input('Digite o comprimeto:'))
cateto_adjacente = float(input('Digite o comprimeto:'))

hipotenusa = math.pow(cateto_adjacente,2) + math.pow(cateto_oposto,2)

hipotenusaR = math.sqrt(hipotenusa)

print('O resultado é {:.2f}'.format(hipotenusaR))

