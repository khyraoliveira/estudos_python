carros = {"gol", "celta", "palio"}

# a forma mais comum para percorrer os dados de um conjunto é com o FOR:
for carro in carros:
    print(carro)

# às vezes é necessário saber qual é o índice do objeto dentro do FOR.
# para isso podemos usar a função 'enumerate':
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")