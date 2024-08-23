# Ele retira da lista o ÚLTIMO elemento que foi adicionado

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c

# mas você tb pode passar qual é o ÍNDICE que deseja remover:
print(linguagens.pop(0))  # python
