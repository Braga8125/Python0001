#Funções com retorno
def soma(v1,v2):
    total = v1+v2
    return total

#Funções para calcular a média de valores
def media_tres(v1,v2,v3):
    return (v1+v2+v3)/3

#Função para mostrar o maior valor a partir de dois números
# def maior_valor(vlor1,vlor2):
#     return max(vlor1,vlor2)

# print(maior_valor(10,5))

#outro jeito de fazer
def mostrar_maior(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2
print(mostrar_maior(10,20))            
# print(soma(10,20))  
#Mostrar o dobro do resultado da função
# v1 =  soma(100,300) 
# print(v1*2)

#calcular a média
# print(media_tres(10,8,6))