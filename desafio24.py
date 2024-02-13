print('===== DESAFIO 24 =====')

cidade = str(input('Digite a cidade que nasceu:'))
cidade = cidade.strip()
cidade = cidade[:6]
cidade = cidade.upper()
print('SANTO' in cidade)

#OU

cidade2 = str(input('Digite a cidade que nasceu:')).strip().upper()
print(cidade2[:5] == 'RIO')#DA para colocar o igual no print
