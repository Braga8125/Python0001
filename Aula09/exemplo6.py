#Abertura de um arquivo chamado dados2.txt
#Ler o nome de uma pessoa


try:
    txt = open("Python0001/Aula09/dados2.txt","w+")
    for i in range(10):   
        nome = input("Informe o nome da pessoa:")
        txt.write(f"Nome: {nome}\n")
 
except:
    print("Não foi possível encontrar o arquivo!")    
else:
    txt.seek(0)  
    print(txt.read()) 
    txt.close() 

#ou ler 10 nomes de outro jeito   
# try:
#     txt = open("Python0001/Aula09/dados2.txt","a+")
#     for i in range(1,11):   
#         nome = input("Informe o nome da pessoa:")
#         txt.write(f"{i} - Nome: {nome}\n")
 
# except:
#     print("Não foi possível encontrar o arquivo!")    
# else:
#     txt.close() 

  