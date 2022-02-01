#Este exercício simula uma lojiha, em que o catálogo abriga os itens e seus valores, e o usuário pode informar a quantidade desejada de cada item e será informado do valor total da compra
#Usamos o conhecimento em arrays, laço de repetição, concatenação, conversão de tipos, input e output de dados e operadores matemáticos

item1 = ["aquarela", 50]
item2 = ["pincel", 10]
item3 = ["tinta", 3.50]
item4 = ["caneta", 6]
item5 = ["borracha", 2]
catalogo = [item1, item2, item3, item4, item5]
valortotal = 0
i = 0
for i in range(len(catalogo)):
    pedido = int(input(str(catalogo[i][0]) + ": "))
    valortotal = valortotal + float(pedido * catalogo[i][1])
print("O valor da compra é: " + str(valortotal))



