#Exercício para calcular rendimentos de um investimento, usuário fornece o capital, tempo em anos, taxa de juros mensal e informamos o quanto rendeu

capital = int(input("informe o capital: "))
anos = int(input("Quantos anos: "))
rendimentomensal= float(input("Informe a taxa(em decimal) de juros mensal: "))

print(capital + (capital*rendimentomensal*(anos*12)))
#Cálculo em juros simples

print(capital*(1+rendimentomensal)**(anos*12))
#Cáluclo em juros compostos