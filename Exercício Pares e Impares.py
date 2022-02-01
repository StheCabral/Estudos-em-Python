#Aqui há 3 formas diferentes de retornar os números pares e impares de uma sequência fornecida, da mais rudimentar para a mais arrumadinha

#Exercício para determinar os números pares e impares de uma sequência sem usar arrays ou laços de repetição

numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))
numero3 = int(input("Número 3: "))
numero4 = int(input("Número 4: "))
numero5 = int(input("Número 5: "))
numero6 = int(input("Número 6: "))
numero7 = int(input("Número 7: "))
numero8 = int(input("Número 8: "))
numero9 = int(input("Número 9: "))
numero10 = int(input("Número 10: "))
pares = ""
impares = ""

if numero1 % 2 == 0:
    pares = str(pares) + str(numero1)
else:
    impares = impares + " " + str(numero1)

if numero2 % 2 == 0:
    pares = pares + " " + str(numero2)
else:
    impares = impares + " " + str(numero2)

if numero3 % 2 == 0:
    pares = pares + " " + str(numero3)
else:
    impares = impares + " " + str(numero3)

if numero4 % 2 == 0:
    pares = pares + " " + str(numero4)
else:
    impares = impares + " " + str(numero4)

if numero5 % 2 == 0:
    pares = pares + " " + str(numero5)
else:
    impares = impares + " " + str(numero5)

if numero6 % 2 == 0:
    pares = pares + " " + str(numero6)
else:
    impares = impares + " " + str(numero6)

if numero7 % 2 == 0:
    pares = pares + " " + str(numero7)
else:
    impares = impares + " " + str(numero7)

if numero8 % 2 == 0:
    pares = pares + " " + str(numero8)
else:
    impares = impares + " " + str(numero8)

if numero9 % 2 == 0:
    pares = pares + " " + str(numero9)
else:
    impares = impares + " " + str(numero9)

if numero10 % 2 == 0:
    pares = pares + " " + str(numero10)
else:
    impares = impares + " " + str(numero10)

print(str(pares) + " são pares")
print(str(impares) + " são impares")

#Exercício para determinar os números pares e impares de uma sequência sem usar arrays, com laços de repetição, strings e concatenação
pares = ""
numero = ""

for i in range(10):
    numero = int(input("Informe o número: "))
    if numero % 2 == 0:
        pares = str(pares) + " " + str(numero)
    else:
        impares = str(impares) + " " + str(numero)

print(str(pares) + " são pares")
print(str(impares) + " são impares")

#Exercício para determinar os números pares e impares de uma sequência usando arrays e laços de repetição

impares = []
pares = []

for i in range(10):
    numero = int(input("Informe o número: "))
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(str(pares) + " são pares")
print(str(impares) + " são impares")