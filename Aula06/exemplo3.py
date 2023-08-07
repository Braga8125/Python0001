#Listas compostas
pc = ['Processador', 'Mouse', 'Teclado',['Memória RAM','HD','SSD'],'Webcam']
print('Item 1:',pc[0])
print('Item 4',pc[3])
print('Primeiro Item da sublista  4.1',pc[3][0])
print('Último Item da sublista 4.1',pc[3][-1])
#print(sorted(pc)) não funciona estrutura muito complexa
#Substituição:
pc[0] = 'Fonte'
print(pc)
#Substituir Memória Ram por Memória flash:
pc[3][0] = 'Memória flash'
print(pc)
