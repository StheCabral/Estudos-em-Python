#Exercício para produzir a sequência de Fibonacci (o valor seguir é a soma dos dois anteriores 

quant = int(input("Informe a quantidade de números na sequencia: "))
valoratual = 0
valoranterior = 0
for i in range(quant):
    print(valoratual)
    valoratual = valoratual + valoranterior
    valoranterior = valoratual-valoranterior
    if(valoratual == 0):
      valoratual = 1