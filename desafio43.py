print('===== DESAFIO 43 =====')

peso = float(input('Digite seu peso:'))
altura = float(input('Digite sua altura:'))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você esta abaixo do peso seu imc:{:.2f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Peso ideal seu imc é:{:.2f}'.format(imc))
elif 25 <= imc <30:
    print('Sobrepeso seu imc é:{:.2f}'.format(imc))
elif 30 <= imc <40:
    print('Obesidade seu imc é:{:.2f}'.format(imc))
else:
    print('Obesidade Morbida seu imc:{:.2f}'.format(imc))