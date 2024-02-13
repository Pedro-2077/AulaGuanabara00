#Condições Aninhadas

#temos o if, elif e else

#PRATICA

nome = str(input('Digite seu nome:'))

if nome == 'Pedro':
    print('O seu nome e lindo')
elif nome == 'Erica':
    print('Seu nome é de uma pessoa incrivel')
elif nome == 'Daniel':
    print('Nome de que tem um pau pequeno e é chenobil')
elif nome in 'Ana Marcos Reijane':#E para colocar varios nome
    print('Nome normal')
else:
    print('Seu nome é normal')

print('Prazer em te conhecer {}!'.format(nome))