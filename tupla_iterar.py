# Para iterar é a mesma coisa das listas:
# utiliza o FOR e passa de elemento por elemento.

carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


# Função ENUMERATE para saber qual é o índice do objeto
# dentro do laço FOR:

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")