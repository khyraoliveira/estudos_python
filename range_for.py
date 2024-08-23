# É usada para produzir uma sequ~encia de números inteiros a partir
# de um início (inclusivo) para um fim (exclusivo).
# Ela recebe 3 argumentos: stop (obrigatório), start (opcional) e step (opcional).

print(list(range(4))) # ele vai imprimir do 0 ao 3.

for numero in range(0,11):
    print(numero, end=" ") # ele vai imprimir do 0 ao 10.


# Tabuada de 5:
for numero in range(0, 51, 5):
    print(numero, end=" ")

# o 0 é o start, o 51 é o fim e o 5 é o step.
# ou seja, aqui tá dizendo que é pra ir de 0 a 50 de 5 em 5.
