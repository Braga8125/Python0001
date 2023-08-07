#Criar uma lista de notas
notas = [6.25,2,10,9,8.8]
#Valor máximo ou maior valor de uma nota
print('Maior valor:',max(notas))
#Valor máximo ou maior valor de uma nota
print('Menor valor:',min(notas))
#Quantidade de itens na lista de notas
print('Quantidade de notas:',len(notas))
#Soma total das notas da lista
print('Soma das notas:',sum(notas))
#Mostrar média das notas
print(f'Média aritmética:{sum(notas)/len(notas):.2f}')
#Operador in(saber se o item está na lista)
print(11 in notas)
#Loop for com listas
print(notas)
for i in notas:
    print(i,end=' ')
#leia 5 notas utilizando lista
# notas2 = []
# for i in range(5):
#     num = float(input('Informe a nota'))
#     notas2.append(num)
# print('Todas as notas informadas: ',notas2)
# print('A quantidade de notas:', len(notas2))
# print('A soma das notas é:', sum(notas2))

#leia uma quantidade de notas determinada pelo usuário e faça a soma dos valores
qtd = int(input('Informe a quantidade de notas:'))
cont = 1
notas3 = []
#Adicionar somente notas de zero até dez
while cont<=qtd:
    num = float(input('Informe a nota: '))
    if num>=0 and num <=10:
       notas3.append(num)    
    else:
        continue
    cont+=1
print('Total é:', sum(notas3))




