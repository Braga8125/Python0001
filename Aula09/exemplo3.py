#Ler a idade de un funcionário e tratar possíveis números negativos ou valores acima de 130
from logging import raiseExceptions


idade = int(input('Informe a sua idade:'))

if idade<0 or idade>=130:
    raise Exception('Valor informado está incorretp ')