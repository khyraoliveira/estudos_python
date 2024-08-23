# É para ADICIONAR elementos à lista, juntar duas listas!

linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"])

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

# detalhe: ele NÃO elimina os valores duplicados!