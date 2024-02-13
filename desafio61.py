from time import sleep

print('====== DESAFIO 61 ====')

termo = int(input('Digite o termo:'))
razao = int(input('Digite a razão:'))
soma = termo
cont = 0
paQtd = 10
contTermo = 10

while cont < paQtd:
    print("{}".format(soma), end=' ')
    cont +=1
    soma += razao
    if cont == paQtd:
        print('PAUSA')
        sleep(1)

        paQtd = int (input('Quantos termos a mais voce quer mostrar?:  '))

        if paQtd > 0:
            cont = 0
            contTermo += paQtd

print("Voce fez {} termos".format(contTermo))