#Aplicar operadores lógicos com if
#Leia a qtd de faltas de um aluno e sua média final
qtd_faltas = int(input('Informe a quantidade de faltas:'))
media = float(input('Informe a média final:'))
#Condições de reprovação:
#qtd de faltas maior que 8 ou média menor do que 7
print('Resultado:',qtd_faltas>8 or media<7)
print('*'*50)
if qtd_faltas > 8 or media <7:
    print('Aluno Reprovado')
else:
    print('Aluno Aprovado') 

 #Analisar a condição do aluno somente se o valor das faltas for maior ou igual a zero
if qtd_faltas>=0:
   if qtd_faltas>8 or media<7: 
        
       if qtd_faltas>8:
            print('Aluno Reprovado por falta')
       if media<7:
            print('Aluno Reprovado por média')
    
   else:
        print('Aluno aprovado')
              
else:
        print('Valor de faltas inválido')      


       