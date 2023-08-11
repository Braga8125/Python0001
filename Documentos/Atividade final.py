"""
Tarefas:
Crie um arquivo com o nome “dados_produtos” e a extensão ".txt".
"""
"""
Salvando no Diário:
Após cada reflexão digitada, salve-a no arquivo do diário.
Certifique-se de adicionar uma linha em branco entre cada reflexão.
"""
"""
Lendo o Diário:
Crie uma opção para o usuário ler o conteúdo do diário.
Trate exceções ao tentar abrir o arquivo e imprimir o conteúdo na tela.
"""
# try:
#     txt = open("Documentos/dados_produtos.txt","a+")
#     print("Arquivo encontrado!")
#     txt.seek(0)
#     print(txt.read())
# except:
#     print("Problemas ao abrir o arquivo...")

# txt.close()

"""
Escrevendo no Diário:
Peça ao usuário para digitar o nome do produto, valor do produto e quantidade vendida.
Trate exceções para lidar com erros de entrada do usuário.
"""

try:
    txt = open("Documentos/dados_produtos.txt","a+",encoding='utf-8')
    produto = input("Informe o nome do produto:") 
    vlorproduto = float(input("Informe o valor do produto:"))
    qtdvendida = float(input("Informe a quantidade vendida:"))
    if vlorproduto<0 or qtdvendida<0 :
       raise ValueError('Número negativo =(')
    else:
        txt.write(f"O produto é {produto:>2}\n - o valor do produto é R${vlorproduto:>2}\n - quantidade vendida {qtdvendida:>2}\n") 

      
    

    

except:
    print("Erro ao gravar os dados!!!") 


      

txt.close()

with open("Documentos/dados_produtos.txt","r",encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)
