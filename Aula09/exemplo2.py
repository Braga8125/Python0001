from logging import exception
from tkinter import E


x=0
try:
    print(x)
except Exception as e:
      print('Falha ao acessar variável')
      print(e)
else:
    print('Parabéns!!! seu script funcionou perfeitamente.')        
finally:
    print('Fim do tratamento de exceções')    