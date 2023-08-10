"""
Crie uma função que leia o nome e as notas de um aluno e salve em um arquivo o nome, a média e data do registro.
"""

try:
    txt = open("Python0001/Aula09/atividade5.txt","a+",encoding='utf-8')
    nome = input("Informe o nome:")
    nota1 = float(input('Informe a nota:'))
    nota2 = float(input('Informe a nota:'))
    data = int(input('Informe a data completa:'))
    soma = nota1+nota2  
    txt.write(f"{nome:} - {soma/2:} - {data:>}\n") 
   
except:
    print("Erro ao gravar os dados!!!") 
      

"""
Crie uma função que leia o nome do curso, carga horária e valor e registre em um arquivo
"""
"""
Crie uma função mostre todos os dados cursos registrados na questão anterior.
"""
"""
Pesquise funções/métodos para apagar um arquivo e aplique um exemplo.
"""