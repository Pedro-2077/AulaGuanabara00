print('===== DESAFIO 97 =====')

def escreva(txt):
    tam = len(txt)
    print('~' * (tam + 4))
    print(f'  {txt}')
    print('~' * (tam + 4))


palavra = str(input('Digite algo: ')).strip()
escreva(palavra)