print('===== DESAFIO 36 =====')

valorCasa = float(input('Digite o valor da casa:'))
salario = float(input('Digite seu salario:'))
anos = int(input('Digite quantos anos voce vai pagar:'))

prestacao = (valorCasa / anos) / 12
salarioLimite = salario * 0.30

if prestacao > salarioLimite:
    print('Tentativa Negada')
elif prestacao <= salarioLimite:
    print('Tentativa Permitida')

    