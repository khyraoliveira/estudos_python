curso = "    Python "

print(curso.strip())
# aqui todos os espaços em branco - da esquerda e da direita - são removidos.

print(curso.lstrip())
# aqui todos os espaços em branco da esquerda são removidos.

print(curso.rstrip())
# aqui todos os espaços em branco da direita são removidos.

print(curso.lstrip() + "!")
# aqui todos os espaços em branco da esquerda são removidos.
# e, também, será acrescentado um "!" ao final da string.