curso = "Python"

print(curso.center(10, "#"))
# aqui o número diz QUANTOS caracteres a string irá ocupar
# aí, no caso, são 10 (6 da string Python e + 4 de '#')
# e a string centralizada nesses 10 caracteres

print(".".join(curso))
# aqui é uma JUNÇÃO - com o método 'join'
# aqui CADA caractere será SEPARADO pelo símbolo escolhido
# no exemplo acima, cada caractere será separado por um '.'