#Ler nome e e-mail e armazenar no arquivos dados3.txt

from errno import ECONNREFUSED


try:
    txt = open("Python0001/Aula09/dados3.txt","a+",encoding='utf-8')
    nome = input("Informe o nome:")
    email = input("Informe o e-mail:")
    txt.write(f"{nome:>2} - {email:>5}\n")
except:
    print("Erro ao gravar os dados!!!")    