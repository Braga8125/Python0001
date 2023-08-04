valor1=45
valor2=258.45

#operadores aritméticos
print("Soma:",valor1+valor2)
print("Subtração:",valor1-valor2)
print("Multiplicação:",valor1*valor2)
print("Divisão:",valor1/valor2)
print(f"Divisão com 2 casas decimais:{valor1/valor2:.2f}")
print(f"valor 2: {valor2:.1f}")
#obter dados do teclado (Entrada de dados)
usuario= input("Informe o seu nome:")
print(f"Seja bem-vindo (a) {usuario}")
#Conversão de tipo de dados - casting
idade= int(input("Informe sua idade:"))
print(f"o nome do usúario é {usuario} e sua idade atual é {idade}")
#Mostrar o dobro da idade informada pelo usuario
print(f"o dobro da idade é: {idade*2}")
#Mostrar tipos de dados variáveis
print("idade:",type(idade))
print("usuario:", type(usuario))
valor_curso = float(input("Informe o valor pago pelo curso:"))
print(f" O valor informado foi {valor_curso}")
#Mostrar uma msg com 25% do valor do curso
#Parabéns !!! vc ganhou <valor> de crédito na próxima compra
print(f"Parabéns vc ganhou R$ {valor_curso*25/100} de crédito na próxima compra")
#solicitar quantidade de parcelas do pagamento
Parcelas=int(input("Informe qtde de parcelas para pagamento:"))
#mostrar valor das parcelas sem juros
print(f"O valor de cada parcela será de R$ {valor_curso/Parcelas:.2f}")





