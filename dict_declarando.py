# DICIONÁRIO:
# é um conjunto NÃO ordenado de pares 'chave-valor'
# onde as chaves são únicas em dada instância do dicionário

# Os dicionários são delimitados por chaves {}
# e contém uma lista de pares 'chave-valor' separada por vírgula ','


# aqui a chave é 'nome' e o valor dela é 'Guilherme'
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# aqui é a mesma coisa, mas usando o construtor DICT
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# aqui é para adicionar uma chave a um dicionário que JÁ EXISTE:
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)