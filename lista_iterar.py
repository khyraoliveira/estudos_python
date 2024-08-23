carros = ["gol", "celta", "palio"]

# 'carro' é cada item dentro da lista carros!
for carro in carros:
    print(carro)

# quando usa o 'enumerate: passo o iterável entre parênteses
# e aí ele me retorna 2 valores: um é o contador (começa em zero tb)
# o outro é o item da iteração:
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")