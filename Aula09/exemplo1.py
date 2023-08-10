#Ler 2 números e executar a divisão dos valores

# try:
#     n1 = float(input("Informe o numerador:"))
#     n2 = float(input("Informe um denominador:"))
#     print(f"Oresultado da divisão é {n1/n2:.2f}")
# except ValueError:
#     print("O valor informado está incorreto!!!")
# except ZeroDivisionError:
#     print("Houve um problema ao executar a divisão...")


try:
    n1 = float(input("Informe o numerador:"))
    n2 = float(input("Informe um denominador:"))
    print(f"Oresultado da divisão é {n1/n2:.2f}")
except:
    print("Não foi possível completar a operação!!!")