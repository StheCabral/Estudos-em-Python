#Algumas anotações avulsas sobre a sintaxe do Python, entre elas exemplos de concatenações, conversões e operações matemáticas com e sem biblioteca


import math
#Para importar bibliotecas se usa o import, tudo que está acima do import não obedecerá a biblioteca importada

#Exemplo de operação matemtica
print(12/3)
# * é multiplicação, + é soma, / é divisão, 0.3 é decimal
#podemos usar esses sinais com qualquer tipo de número, inclusive os complexos que são representados com a letra j

#Exemplo de representação de números complexos, entre () pois é um número só
print(4j+3)

#Exemplo de concateção (como juntar dois textos)
print("hello world, "+"sthefany")

print("O resultado da soma de 2+3 é: " + str(2+3))
#str() transforma o número em string automaticamente, nesse caso se torna necessário pois só podemos concatenar string com string

print(int("1") +5)
#int() tranforma texto em número

print(float(34))
#float() tranforma o elemento em float

print("2312" + "231")
#a soma de 2 textos sempre é concatenação

#Exemplo de raíz quadrada (square root) usando a bibli  math
print(math.sqrt(25)) 

#Exemplo de raíz quadrada (square root) sem a bibli math
print(27**(1/3)) 

print(math.pi)
#py calcula até +- 15 casas decimais, para mais demora muito

print(math.cos(120))
#cos é função, os números que vc coloca dentro dela está em radianos

print(math.degrees(120))
#transforma rad em ângulo

print(math.cos(math.degrees(120)))
#cos diretamente em ângulo, vindo de rad

print(math.radians(180))
#tranforma ângulo em rad




