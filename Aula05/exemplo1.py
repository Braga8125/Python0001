#Exemplo da função range()
from ast import Num
from doctest import OutputChecker


print(list(range(2,55)))
print(list(range(10)))
print(range(10))
print(list(range(10,100,5)))
print('-'*50)
#Loop for
for i in range(10):
    print(i,end=" ")
print('\nValor final do contador:',i)   
print('-'*50) 
#Contagem de 20 até 30 usando laço for
for i in range(20,31):
    print(i,end=" ")
print('-'*50) 
#Contagem de 10 até 0 usando laço for
# for i in range(10,0,-1):
#     print(i,end=" ")
#Ou
for i in range(10,-1,-1):
    print(i,end=' ')
print('-'*50) 
#Leia 5 números inteiros e mostre uma mensagem quando o número for par
# for i in range(5):
#     num = int(input(' Informe o valor: '))
#     if num%2==0:
#         print('O valor informado é par:')
# print('-'*50) 
#Leia 5 números e some somente os valores ímpares
# soma = 0
# for i in range(5):
#     num = int(input(' Informe o valor: '))
#     if num%2!=0:
#         soma +=num
# print('A soma dos ímpares é:', soma)        

#Leia 5 números e some somente os valores ímpares e mostre a qauntidade de ímpares 
soma = 0
cont = 0
for i in range(5):
    num = int(input(' Informe um valor: '))
    if num%2!=0:
        soma +=num
        cont+=1
print('A soma dos ímpares é:', soma)      
print('A quantidade dos ímpares é:', cont)   
print(f'A média é: {soma/cont:.2f}')    
print('\n','-'*50)   