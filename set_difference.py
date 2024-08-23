# DIFFERENCE: tudo o que tem em UM conjunto que NÃO ESTÁ NO OUTRO!

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)



# e tem o SYMMETRIC DIFFERENCE:
# são TODOS OS ELEMENTOS que não estão na intersecção dos conjuntos!
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)