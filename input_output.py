# par aprender as funções de entrada e saída do Python

nome = input("Informe o seu nome: ")
idade = input("Digite aqui a sua idade: ")

print(nome, idade)
print(nome, idade, end="...\n")
print(nome, idade, sep="#", end="...\n")
print(nome, idade, sep="#")

first_name = "Guilherme"
last_name = "Carvalho"

print(first_name, last_name) # aqui vai imprimir normal na tela
print(first_name, last_name, end="...\n") # aqui vai imprimir com as reticências
print(first_name, last_name, sep="#") # aqui vai imprimir separando as variáveis pelo símbolo que quiser.

