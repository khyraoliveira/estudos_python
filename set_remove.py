# REMOVE: aqui remove o elemento, mas tem que dizer qual elemento quer ser removido!

numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(0))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# DETALHE: se colocar para remover um elemento que NÃO EXISTE, ele dá erro!
# diferente do DISCARD, que não dá erro se pedir p/ remover um elemento que não existe.