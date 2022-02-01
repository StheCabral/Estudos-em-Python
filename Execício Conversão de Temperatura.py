#Exercício de conversão de temperatura de Celsius para Fahrenheit feito em Pyhton
#Usamos o conhecimento em input e output de dados, conversão de tipos e operadores matemáticos

celsius = int(input('Informe a temperatura em celsius: '))
#input vem como string por isso precisa ser convertido para inteiro através do comand "int()"
print("A temperatura em Fahrenheit é: " + str((celsius*9 + 160)//5))
#A concatenação só pode ser rralizada com strings, por isso é necessário a conversão do resultado do cálculo de inteiro para string através do comando "str()"