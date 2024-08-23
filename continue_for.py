# o CONTINUE serve para pular tal condição
# no caso aqui, irá pular o número 15

for numero in range(20):

    if numero == 15:
        continue

    print(numero, end=" ")