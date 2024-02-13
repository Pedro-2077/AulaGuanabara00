print('===== DESAFIO 67 =====')

while True:
    tabuada = int(input('Digite qual tabuada você quer:'))

    if tabuada >= 0:
        for c in range(1,11):
            print(f'{tabuada} X {c} = {tabuada*c}')

    elif tabuada < 0:
        break