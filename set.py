# set é uma coleção que não possui objetos repetidos.
# Usamos sets para eliminar itens duplicados de um iterável.

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4} eliminou os valores DUPLICADOS!

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)

# DETALHE: o 'set' não garante a ordem dos elementos como vem no objeto.
# Se precisar que venha em ordem, tem que meter um 'sort' ou algo do tipo!