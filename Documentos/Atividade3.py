"""
1.	Crie um dicionário contendo os nomes dos estados abreviados (Chave) e os nomes das capitais (Valor) da região norte e nordeste. Mostre ao final as informações relacionadas ao amazonas e Sergipe.
"""
Estados = {'AM':'Manaus','PA':'Belém','AC':'Rio Branco','RO':'Porto Velho','RR':'Boa Vista','AP':'Macapá','TO':'Palmas','AL':'Maceio','BA':'Salvador','CE':'Fortaleza','MA':'São Luiz','PB':'João Pessoa','PE':'Recife','PI':'Teresina','RN':'Natal','SE':'Aracaju'}
print(Estados['AM'],Estados['SE'])
"""
2.	Crie um script que leia o nome de 5 alunos e mostre os dados informados em ordem alfabética
"""
# alunos = []
# for i in range(5):
#      aluno = str(input('Informe um nome'))
#      alunos.append(aluno)
# print(sorted(alunos))     
"""
3.	Crie uma lista com os seguintes valores: 
[2,10,30,85,2,6,0,4]

 	- Mostre apenas o terceiro valor
	- Mostre apenas o último valor
- Mostre o dobro de cada valor
"""
# lista = [2,10,30,85,2,6,0,4]
# print(lista)
# print(lista[3])
# print(lista[-1])
# lista1 = [i*2 for i in lista]
# print(lista1)
  
"""   
4.	Qual a principal diferença entre uma lista e uma tupla em Python?
""" 
print('Tupla ela não muda é imútavel se trocar por colchete ai sim vc pode mexer','já na Lista ela é mútavel ')
"""
5.	Pesquise e responda quais a principais características da Estrutura Set em Python    
"""
print('Sets são desordenados','\nNão possuem elementos duplicados, ou seja, cada elemento é único. ','\nUm set em si pode ser modificado, contudo os elementos contidos dentro dele precisam ser de tipos imutáveis.')
"""
6.	Descreva quatro exemplos de funções/métodos que podem ser aplicados em um dicionário.
"""
print('Mostrar primeiro item do dicionário: ex:print(alunos[111])','\nMostrar somente as chaves do dicionário: ex2:print(alunos.keys())','\nMostrar somente os valores armazenados no dicionário: ex3:print(alunos.values())','\nMostrar todos os itens do dicionário: ex4:print(alunos.items())')
"""
7.	Crie um script que leia dez números positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e menor valor informado.
"""
# cont = 1
# lista2 = []
# while cont<=10:
#     num = float(input('Informe o valor:'))
#     if num < 0:
#         continue
#     lista2.append(num)
#     cont+=1
# print('Lista ordenada:', sorted(lista2))
# print('Maior valor:', max(lista2))
# print('Menor valor:', min(lista2))      


