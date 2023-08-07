#Tupla ela não muda é imútavel/ se trocar por colchete ai sim vc pode mexer, pq lista pode

# Cidades = ('Manaus','Coari','Parintins','Manacapuru','Anori')
# print(type(Cidades))
# #Mostrar o último item da tupla
# print(Cidades[-1])
# #Mostrar o primeiro item da tupla
# print(Cidades[0])
# #Mostrar itens ordenados
# print(sorted(Cidades))
# #Cidades.sort() - so pode exibir ela ordenada e não mudar de fato  e nao funiona na tupla so na lista
# print(Cidades.count('Manaus'))
#Leia 3 números positivos e armazene os dados em uma lista, mostre os valores dados em ordem cresecnte, o maior valor e menor informado.
cont = 1
lista1 = []
while cont<=3:
    num = float(input('Informe o valor:'))
    if num < 0:
        continue
    lista1.append(num)
    cont+=1
print('Lista ordenada:', sorted(lista1))
print('Maior valor:', max(lista1))
print('Menor valor:', min(lista1))  

