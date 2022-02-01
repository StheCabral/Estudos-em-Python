#Exercício para fornecer o máximo, o mínimo e a média entre 10 números fornecidos pelo usuário
#Usamos o conhecimento em arrys, operadores relacionais, laços de repetição e condicionais

numeros = []
somadenumeros = 0
mínimo = 0
máximo = 10
menor = máximo
maior = mínimo

for i in range(10):
    numero = int(input("informe: "))
    if(numero<menor):
        menor = numero
    if(numero>maior):
        maior = numero
    numeros.append(numero)
    somadenumeros = somadenumeros + int(numero)

print("A média é: " + str(somadenumeros/len(numeros)))
print("o máx é: " + str(maior))
print("o mín é: " + str(menor))