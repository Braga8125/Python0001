#leia um número real e armazene o valor em uma variável
num = float(input('Informe um número:'))
print(type(num))
#Verificar se o número informado é positivo
if num>0: #Teste for True
    print('O valor informado é positivo!')
elif num==0:
    print('O valor informado é neutro')    
else:     #Teste for False
    print('O valor informado é negativo!') 
print('Aqui finaliza o script!!!')  
