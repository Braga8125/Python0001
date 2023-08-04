#Estrutura de repetição while
cont = 0
while cont<=100:
    print(cont,end=" ")
    cont = cont+1
print('\nvalor final do contador:',cont)
print('-'*50)
#Contagem iniciando em 50 até 200
cont = 50
while cont<=200:
    print(cont,end=' ')
    cont += 1
print('-'*50)
#Contagem iniciando em 10 e finalizando em 80, incrementando os valores de 10 em 10
cont = 10
while cont<=80:
    print(cont,end=' ')
    cont+= 10
print('\n','-'*50,)
#Mostrar a mensagem "Eu quero estudar" 300x
cont = 1
while cont<=300:
    print(cont,'-Eu tenho que estudar!!!') 
    cont+= 1
#Leia um número e mostre a contagem a partir do zero até o número informado
Vlr_final= int(input('Informe o valor final:'))
cont = 0
while cont <= Vlr_final:
    print(cont,end=' ')
    cont+=1
print('\n','-'*50)    
#Contagem decrescente iniciando em 23 até 0
cont = 23
while cont>=0:
    print(cont,end=' ')
    cont-=1
print('\n','-'*50) 
#Leia 2 números e mostre a contagem do intervalo dos valores informados
Vlr_cont1= int(input('Digite o valor inicial da contagem :'))    
Vlr_cont2= int(input('Digite o valor finalda contagem:')) 

while Vlr_cont1 <= Vlr_cont2:
          print(Vlr_cont1)
          Vlr_cont1+=1

