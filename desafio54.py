import datetime

atual = datetime.date.today().year
contMaior = 0
contMenor = 0
for c in range(0, 7):
    nascimento = int(input('Digite sua data de nascimento:'))
    idade = atual - nascimento
    if idade >= 21:
        contMaior += 1
    elif idade < 21:
        contMenor += 1

print("A quantidade de maiores de idade é:{}".format(contMaior))
print("A quantidade de menores de idade é:{}".format(contMenor))