#Anotações sobre array, para identifica-lo usa-se os [], cada elemento dentro dos cochetes tem uma posição, começando pelo 0 
#Exemplo
""" 
sequencia = [1, 2]
print(sequencia[0])
"""

#para indicar uma posição específica usamos [numero da posição]

#a funcionalidade .append adiciona elementos ao array
#exemplo
""" 
sequencia.append(3)
print(sequencia)
"""


#Exercício em que o usuário informa as notas e temos que retornar a média aritmética

control = True
notas= []
somadenotas = 0
while(control):
    nota = input("Nota: ")
    if (nota == "-1"):
        control = False
    else:
        notas.append(nota)
        somadenotas = somadenotas + int(nota)
print(somadenotas/len(notas))