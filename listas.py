# Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto.
# É uma sequência e pode armazenar qualquer tipo de objeto.

# Essa é a forma mais comum de se declarar uma lista:
frutas = ["laranja", "maca", "uva"]
print(frutas)

# Aqui é a declaração de uma lista vazia:
frutas = []
print(frutas)

# Aqui é a declaração com um 'construtor'
# É uma lista onde CADA LETRA é um elemento:
letras = list("python")
print(letras)

# Aqui é a declaração com um 'construtor'
# É uma lista com a função range
# É uma lista para cada elemento, até 10:
numeros = list(range(10))
print(numeros)

# Uma lista com cada atributo de um carro
# Uma lista com os mais variados tipos de elementos:
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)