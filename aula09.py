#Aparti do desafio 21

#Manipulano Texto

frase = 'Quem leu chupa meu saco'

#É um vetor na qual voce pode escolhe uma indice

#EX

print(frase[3])#aqui vai mostra o M

#agora com outra sintaxe

print(frase[0:8]) #Aqui ele vai ate o indice 7 da frase
print(frase[5:24])#sempre tem que colocar uma indice acimna pro final
print(frase[5:24:2])#vai pular de dois em dois o ultimo parametro
print(frase[:8])#Vai ate o leu nao quando esta vazio o primeiro parametro ele pega do inicio
print(frase[15:])#mesma coisa que o anterio so que aocontrario
print(frase[9::2])#deixo pra ir ate o final da indice pulando de dois em dois

#Quantas indices tem
print(len(frase))

#Contador

print(frase.count('a')) #conta quantos o tem na frase/indice

print(frase.count('a', 0, 15))#Aqui ele vai ver quantos a tem da indice 0 a 14

#find

print(frase.find('saco'))#Acha a pocição referente ao que pedi no caso o saco começa no 19

print(frase.find('maminha'))#Como ele não achou a frase maminha ele coloca -1 como resultado

#in
print('chupa' in frase) #vai preocura se tem a palavra chupa na frase se tiver vai da TRUE se não FALSE


#Transformação

#replace
print(frase.replace('chupa', 'Maminha'))#Muda algo que voce quer por outra

#UPPER

print(frase.upper())#Letras Grandes

#lower

print(frase.lower())#Letras pequenas

#Capitalize

print(frase.capitalize())#Vai deixa so a letra do inicio grande e o resto pequeno

#title

print(frase.title())#Ele vai pegar cada inicio de palavra e colocar em maiculo a letra,sabendo pelo espaços

#strip

frase2 = '     Chupa meu saco     '

print(frase2.strip())#Retira todos os espaços desnecesarios

#rstrip

print(frase2.rstrip())#vai tirar so o espaço da esquerda

#lstrip

print(frase2.lstrip())#vai retirar o espaço da direita

#split

print(frase.split())#Ele separa toda a string cada uma com um novo nome de 0 ate onde for e cada palavra tem sua indiceses
frase4 = frase.split()
print(frase4[2][3])#Tranformei a frase em varios vetores com suas indices e ae puxei o vetor 2 que e chupa e a posição 3 que é p
#join

frase3 = frase.split()
print('-'.join(frase3)) #Aqui o join ele junta os vetores e coloca oque pedimos a ele na separação

#Printando texto no formato que voce quiser macete

print('''\n\nChame a função subjacente da API da plataforma. 
O parâmetro sound pode ser um nome de arquivo, um alias de som do sistema, 
dados de áudio como um objeto semelhante a bytes ou . Sua interpretação depende do valor de flags , 
que pode ser uma combinação ORed bit a bit das constantes descritas abaixo. Se o parâmetro sound
for , qualquer som de forma de onda atualmente reproduzido será interrompido. Se o''')
