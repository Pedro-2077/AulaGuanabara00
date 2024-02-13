from time import sleep
print('===== DESAFIO 57 =====')

sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()

while sexo != 'M' and sexo != 'F':
    print('Erro de digitação:')
    sleep(2)
    sexo = str(input('Digite o sexo M o F:')).upper()

