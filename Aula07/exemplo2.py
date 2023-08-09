#Operações sobre lista () List Comprehension
lista = [10,20,5,50,100,6]
#Criar uma nova lista com o dobro dos valores da lista anterior
lista2 = []
for i in lista:
    lista2.append(i*2)
print(lista2)
#Outra forma de duplicar 
lista3 = [i*2 for i in lista]  
print(lista3)
#Criar uma nova lista com a metade dos valores da lista anterior
lista4 = [i/2 for i in lista]
print(lista4)
#Criar uma nova lista com valores acima de 10, com base nos itens da lista
lista5 = [i for i in lista if i>10]
print(lista5)
#Criar uma nova lista com valores pares, com base nos itens da lista
lista6 = [i for i in lista if i%2==0]
print(lista6)
