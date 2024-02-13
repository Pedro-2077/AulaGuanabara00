#Cores Terminal

#Padrão ansi  \033[0:33:44m Sendo  que 0 é o estilo do texto, 33 é a cor do texto e 44 é o background

#Style do texto:

#0 none (nada)
#1 Bolde (letra mais grosa)
#4 underline(linha embaixo)
#5 Negative (Inverte as cores do background para o texto)

#Text

#30 Cor Branca
#31 Cor Vermelha
#32 Cor Verde
#33 Cor Amarelo
#34 Cor Azul
#35 roxo
#36 Ciano
#37 Cinza

#Background

#40 Branco
#41 Vermelho
#42 Verde
#43 Amarelo
#44 Azul
#45 Roxo
#46 Ciano
#47 Cinza

#Padrão ansi  \033[0:33:44m

#PRATICA

print('\033[1;31;43mOla mundo') #AQui eu coloquei o padra ANSI visto acima
print("\033[1;31;43mOla mundo\033[m") #Aqui no final chama o codigo denovo para fechar a formatação

print("\033[1;;45mMama Minha Pica")
print('\033[7;40mOla bumbum\033[m')

n = 1
n2 = 2

print('O resultado entre \033[1;31;43m{}\033[m e \033[1;31;43m{}\033[m é = {}'.format(n,n2,n+n2))

print('O resultado é {}{}{}'.format('\033[4;31;43m', n, '\033[m')) #Da para fazer assim com o formate

cores = {'limpa': '\033[m', 'azul': '\033[34m', 'amarelo': '\033[33m'}

print('O resultado é {}{}{}'.format(cores['amarelo'], n, cores['limpa']))

s = 'prova de python'
print(len(s))

