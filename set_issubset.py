# ISSUBSET
# quando um conjunto é SUB-CONJUNTO de outro.

conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

# "Todos os elementos de A pertencem a B?"
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

# "Todos os elementos de B pertencem a A?"
resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)