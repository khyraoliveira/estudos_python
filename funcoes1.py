# FUNÇÃO: é um bloco de código identificado por um nome.
# E pode receber uma lista de parâmetros.
# A FUNÇÃO pode retornar valores, pode retornar mais do que um único valor.
# Os parâmetros são as entradas das FUNÇÕES e os retornos são as saídas delas.

def exibir_mensagem():
    print("Olá, mundo!")
exibir_mensagem()

def exibir_msg(nome):
    print(f"Olá, {nome}!")      # esse 'f' é para transformar isso num 'template literals'!
exibir_msg("Carol")             # em Python: fstring.

def calcular_total(numeros):
    return sum(numeros)
calcular_total([2, 8, 4, 10])