# É outra forma de remover elementos de uma lista.
# Diferente do .pop(), lugar de passar o índice do seu objeto
# Aqui você escreve qual objeto deseja que seja removido!

linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c")

print(linguagens)  # ["python", "js", "java", "csharp"]

# detalhe: se tiverem elementos duplicados
# ele tirará apenas o primeiro que aparece na lista!