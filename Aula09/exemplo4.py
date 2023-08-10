#Mostrar exceção ao digitar números negativos
from tkinter import N


n = float(input('Informe um valor positivo:'))

if n<0 :
    raise ValueError('Número negativo =(')