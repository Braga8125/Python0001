try:
    txt = open("Python0001/Aula09/dados.txt","a+")
    print("Arquivo encontrado!")
    txt.seek(0)
    print(txt.read())
except:
    print("Problemas ao abrir o arquivo...")    