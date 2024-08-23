# Quando você quer CRIAR UMA LISTA NOVA com base nos valores da lista
# existente (filtro) ou gerar uma nova lista aplicando alguma modificação
# nos elementos de uma lista existente!

# Filtrar lista - versão comum
# -- Pegar todos os número PARES da lista fornecida:
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)
# a função append é para ADICIONAR NOVOS VALORES a nossa lista.

# # Filtrar lista - versão COMPREHENSION
# -- Pegar todos os número PARES da lista fornecida:
numeros = [1, 30, 21, 2, 9, 65, 34]
pares2 = [numero for numero in numeros if numero % 2 == 0]
print(pares2)

# Modificar valores
# Pega o número da lista e o eleva ao quadrado:
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)