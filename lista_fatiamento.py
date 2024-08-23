# É uma forma de passar um índice inicial e/ou um final para acessar o conjunto.

lista = ["p", "y", "t", "h", "o", "n"]

# a partir do índice 2 até o final
print(lista[2:])  # ["t", "h", "o", "n"]

# do índice 0 até o índice 2
print(lista[:2])  # ["p", "y"]

# do índice 1 até o 3
print(lista[1:3])  # ["y", "t"]

# do índice 0 até o 3 pulando 2 índices!
print(lista[0:3:2])  # ["p", "t"]

# gera uma cópia da lista
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]

# gera a lista ao contrário!
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]