# Como acessar os valores nas listas:
# Acesso direto:

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[0])  # maçã, é o 1o elemento, o índice 0.
print(frutas[2])  # uva

# Acessando índices negativos, conta do final para o começo da lista:
# Mas no negativo, o começo da lista é o índice '-1' e não zero!
print(frutas[-1])  # pera
print(frutas[-3])  # laranja