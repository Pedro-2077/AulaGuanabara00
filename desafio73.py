
tabela = ('Palmeiras', 'Grêmio', 'Atletico Mineiro', 'Flamengo', 'Botafogo',
          'Red Bull Bragantino', 'Fluminense', 'Athletico-PR', 'Internacional',
          'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians', 'Cruzeiro', 'Vasco da Gama',
          'Bahia', 'Santos', 'Goiáis', 'Curitiba', 'América-MG')

print(f'Os 5 primeiros são: {tabela[:6]}')
print(f'Os 4 ultimos colocados na tabela: {tabela[-4:]}')
print(f'Times em ordem é {sorted(tabela)}')
print(f'O vasco está na {tabela.index('Botafogo')+1}')

