"""
1.	Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente.
"""
# Vlr_cont1= int(input('Digite o valor inicial da contagem :'))    
# Vlr_cont2= int(input('Digite o valor finalda contagem:')) 

# while Vlr_cont1:
#           print(Vlr_cont1,end=' ')
#           Vlr_cont1-=1
# print('\n','-'*50) 

# while Vlr_cont2:
#           print(Vlr_cont2,end=' ')
#           Vlr_cont2-=1
# print('\n','-'*50)

"""
2.	Faça um script que mostre uma contagem iniciando em 10, finalizando em 500 com incremento de 5 em 5
"""
# cont=10
# while cont<=500:
#   print(cont,end=' ')
#   cont+=5

"""
3.	Faça um script que mostre os números pares em um intervalo definido pelo usuário.
"""
# for i in range(1,10):
#         if i%2==0:   
#             print(i,end=" ")    
"""

4.	Faça um script que leia dois valores positivos e mostre a soma dos números ímpares entre eles.

"""    
# num1 = int(input('Entre com o valor inicial positivo: '))
# num2 = int(input('Entre com o valor final positivo: '))
# soma = 0
# for i in range(num1, num2 + 1):
#     if i % 2 != 0:
#      soma=soma+i
# print('A soma é', soma)
"""
5.	Faça um script que mostre uma sequência numérica iniciando em 63, terminado em 129, calcule e mostre a soma destes valores.
"""
# soma=0
# for i in range(63,130):
#     print(i,end=" ")
#     soma+=i
# print('-'*50,soma) 

"""
6.	Faça um script em Python para receber dois números informados pelo usuário, mostre o valor da soma de todos os números entre eles e a média dos valores.
"""
# num1 = int(input('Entre com o valor inicial: '))
# num2 = int(input('Entre com o valor final: '))
# soma = 0
# for i in range(num1, num2 + 1):
#        soma=soma+i
# print('A soma é', soma)

"""
7.	Faça um script em Python mostre a tabuada de multiplicação do 8, iniciando do 0 até o 10.
"""

# num=8
# for count in range(11):
#     print("%d x %d = %d" % (num, count+0, num*(count+0)) ) 

"""
8.	Crie um script em Python que leia dez números e mostre a média dos valores informados.
"""
# soma=0
# for i in range(10):
#     num = int(input(' Informe o valor: '))
#     soma+=num
# print('A soma dos números é:', soma)                 

"""
9.	Crie um script em Python que leia 5 números e mostre o maior valor informado.
"""
# n1 = int (input('Digite um valor: '))
# n2 = int (input('Digite um valor: '))
# n3 = int (input('Digite um valor: '))
# n4 = int (input('Digite um valor: '))
# n5 = int (input('Digite um valor: '))
# l = [n1, n2, n3,n4,n5]

# print('O maior numero é {}'.format(max(l)))

"""
10.	Crie um script em Python que leia 5 números e mostre o maior valor e o menor valor informado.
"""
# n1 = int (input('Digite um valor: '))
# n2 = int (input('Digite um valor: '))
# n3 = int (input('Digite um valor: '))
# n4 = int (input('Digite um valor: '))
# n5 = int (input('Digite um valor: '))
# l = [n1, n2, n3,n4,n5]

# print('O maior numero é {}'.format(max(l)))
# print('O menor numero é {}'.format(min(l)))

"""
11. Faça um script em Python que leia 10 valores positivos e mostre, no final, a soma dos números pares e a soma dos números ímpares. 
"""
somaimpar = 0
somapar = 0
cont = 0
for i in range(10):
    num = int(input(' Informe um valor: '))
    if num%2!=0:
        somaimpar +=num
        cont+=1
    if num%2==0:
        somapar +=num
        cont+=1    
    
print('A soma dos ímpares é:', somaimpar)      
print('A soma dos pares é:', somapar) 
  
print('\n','-'*50)  
        